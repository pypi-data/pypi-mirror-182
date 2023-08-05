# Pure zero-dependency JSON-RPC 2.0 implementation.
# Copyright © 2022 Andrew Malchuk. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections.abc import Iterable
from typing import Any, Final
from unittest.case import TestCase
from uuid import UUID, uuid4

from jsonrpc._errors import Error, ErrorEnum
from jsonrpc._request import BatchRequest, Request
from jsonrpc._utilities import Undefined


class TestRequest(TestCase):
    @property
    def random_id(self) -> int:
        uuid: Final[UUID] = uuid4()
        return int(uuid)

    def test_is_method_valid(self) -> None:
        with self.assertRaises(Error) as context:
            Request(method=None)

        self.assertEqual(context.exception.code, ErrorEnum.INVALID_REQUEST)
        self.assertIn("must be a string", context.exception.message)

        with self.assertRaises(Error) as context:
            Request(method="rpc.print")

        self.assertEqual(context.exception.code, ErrorEnum.INVALID_REQUEST)
        self.assertEqual(context.exception.message, "Request method must be a string and should not have a 'rpc.' prefix")

        request: Request = Request(method="print")
        self.assertEqual(request.method, "print")

    def test_is_params_valid(self) -> None:
        with self.assertRaises(Error) as context:
            Request(method="print", params=None)

        self.assertEqual(context.exception.code, ErrorEnum.INVALID_REQUEST)

        request_with_args: Request = Request(method="print", params=["1024", "2048", "4096"])
        self.assertTupleEqual(request_with_args.args, ("1024", "2048", "4096"))
        self.assertDictEqual(request_with_args.kwargs, {})

        request_with_kwargs: Request = Request(method="print", params={"a": 1024, "b": 2048})
        self.assertTupleEqual(request_with_kwargs.args, ())
        self.assertDictEqual(request_with_kwargs.kwargs, {"a": 1024, "b": 2048})

    def test_is_request_id_valid(self) -> None:
        with self.assertRaises(Error) as context:
            Request(method="print", request_id=None)

        self.assertEqual(context.exception.code, ErrorEnum.INVALID_REQUEST)

        request_id: int = self.random_id
        request: Request = Request(method="print", request_id=request_id)
        self.assertEqual(request.request_id, request_id)

    def test_hash(self) -> None:
        request_id0: int = self.random_id
        actual0: int = hash(Request(method="request0", request_id=request_id0))
        expected0: int = hash(("request0", Undefined, request_id0))
        self.assertEqual(actual0, expected0)

        request_id1: int = self.random_id
        actual1: int = hash(Request(method="request1", params=[1, 2, 3], request_id=request_id1))
        expected1: int = hash(("request1", (1, 2, 3), request_id1))
        self.assertEqual(actual1, expected1)

        request_id2: int = self.random_id
        actual2: int = hash(Request(method="request2", params={"a": True, "b": False}, request_id=request_id2))
        expected2: int = hash(("request2", (("a", True), ("b", False)), request_id2))
        self.assertEqual(actual2, expected2)

        actual3: int = hash(Request(method="request3", params={"a": True, "b": [1, 2, 3]}))
        expected3: int = hash(("request3", (("a", True), ("b", (1, 2, 3))), Undefined))
        self.assertEqual(actual3, expected3)

    def test_equality(self) -> None:
        request_id: int = self.random_id
        request: Request = Request(method="print", request_id=request_id)
        self.assertEqual(request, Request(method="print", request_id=request_id))
        self.assertNotEqual(request, object())
        self.assertNotEqual(request, Request(method="print", request_id=self.random_id))
        self.assertNotEqual(request, Request(method="print", params=["1024", "2048", "4096"]))
        self.assertNotEqual(request, Request(method="print", params={"a": 1024, "b": 2048}))

    def test_is_notification(self) -> None:
        request_with_id: Request = Request(method="print", request_id=self.random_id)
        self.assertFalse(request_with_id.is_notification)

        request: Request = Request(method="print")
        self.assertTrue(request.is_notification)

    def test_from_json(self) -> None:
        errors: tuple[Error, ...] = (
            Request.from_json(None),
            Request.from_json({}),
            Request.from_json({"jsonrpc": "2.0"}),
            Request.from_json({"jsonrpc": "2.1", "method": "print"}),
            Request.from_json({"jsonrpc": "2.0", "method": None}),
            Request.from_json({"jsonrpc": "2.0", "method": "print", "params": None}),
            Request.from_json({"jsonrpc": "2.0", "method": "print", "id": None}),
        )
        for error in errors:
            with self.subTest(error=error):
                self.assertIsInstance(error, Error)

        requests: tuple[Request, ...] = (
            Request.from_json({"jsonrpc": "2.0", "method": "print0", "params": ["1024", "2048", "4096"], "id": self.random_id}),
            Request.from_json({"jsonrpc": "2.0", "method": "print1", "params": {"a": 1024, "b": 2048}}),
            Request.from_json({"jsonrpc": "2.0", "method": "print2", "id": self.random_id}),
            Request.from_json({"jsonrpc": "2.0", "method": "print3"}),
        )
        for request in requests:
            with self.subTest(request=request):
                self.assertIsInstance(request, Request)


class TestBatchRequest(TestCase):
    @property
    def random_id(self) -> str:
        uuid: Final[UUID] = uuid4()
        return str(uuid)

    def test_hash(self) -> None:
        requests: list[Request | Error] = [
            Request(method="request0", request_id=self.random_id),
            Request(method="request1", params=[1, 2, 3], request_id=self.random_id),
            Request(method="request2", params={"a": True, "b": False}, request_id=self.random_id),
            Request(method="request3", params={"a": True, "b": [1, 2, 3]}),
            Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes"),
            Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes", data=[1, 2, 3]),
        ]
        batch_request: BatchRequest = BatchRequest(requests)
        self.assertEqual(hash(batch_request), hash(tuple(requests)))

    def test_equality(self) -> None:
        requests: list[Request] = [
            Request(method="print0", params=["1024", "2048", "4096"]),
            Request(method="print1", request_id=self.random_id),
        ]
        batch_request: BatchRequest = BatchRequest(requests)
        self.assertEqual(batch_request, BatchRequest(requests))
        self.assertNotEqual(batch_request, None)

    def test_iterable(self) -> None:
        batch_request: BatchRequest = BatchRequest(
            [
                Request(method="print0", params=["1024", "2048", "4096"]),
                Request(method="print1", request_id=self.random_id),
            ]
        )
        self.assertIsInstance(batch_request, Iterable)
        self.assertTrue(batch_request)
        self.assertEqual(len(batch_request), 2)

        for request in batch_request:
            with self.subTest(request=request):
                self.assertIsInstance(request, Request)

    def test_from_json(self) -> None:
        invalid_requests: list[dict[str, Any] | None] = [
            None,
            {},
            {"jsonrpc": "2.0"},
            {"jsonrpc": "2.1", "method": "print"},
            {"jsonrpc": "2.0", "method": None},
            {"jsonrpc": "2.0", "method": "print", "params": None},
            {"jsonrpc": "2.0", "method": "print", "id": None},
        ]
        invalid_batch_request: BatchRequest = BatchRequest.from_json(invalid_requests)
        self.assertEqual(len(invalid_requests), len(invalid_batch_request))

        for request in invalid_batch_request:
            with self.subTest(request=request):
                self.assertIsInstance(request, Error)

        requests: list[dict[str, Any]] = [
            {"jsonrpc": "2.0", "method": "print0", "params": ["1024", "2048", "4096"], "id": self.random_id},
            {"jsonrpc": "2.0", "method": "print1", "params": {"a": 1024, "b": 2048}},
            {"jsonrpc": "2.0", "method": "print2", "id": self.random_id},
            {"jsonrpc": "2.0", "method": "print3"},
        ]
        batch_request: BatchRequest = BatchRequest.from_json(requests)
        self.assertEqual(len(requests), len(batch_request))

        for request in batch_request:
            with self.subTest(request=request):
                self.assertIsInstance(request, Request)
