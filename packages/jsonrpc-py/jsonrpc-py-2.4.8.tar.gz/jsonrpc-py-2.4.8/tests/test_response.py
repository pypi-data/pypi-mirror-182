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

from collections.abc import Iterable, MutableSequence
from typing import Final
from unittest.case import TestCase
from uuid import UUID, uuid4

from jsonrpc._errors import Error, ErrorEnum
from jsonrpc._response import BatchResponse, Response
from jsonrpc._utilities import Undefined


class TestResponse(TestCase):
    @property
    def random_id(self) -> str:
        uuid: Final[UUID] = uuid4()
        return str(uuid)

    def test_is_body_and_error_valid(self) -> None:
        with self.assertRaises(TypeError) as context:
            Response(body=Undefined, error=Undefined)

        self.assertEqual(str(context.exception), "Either 'body' or 'error' attribute must be set")

        error: Error = Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes")
        with self.assertRaises(TypeError) as context:
            Response(body=[1, 2, 3], error=error)

        self.assertEqual(str(context.exception), "Either 'body' or 'error' attribute must be set")

    def test_is_response_id_valid(self) -> None:
        for response_id in ("1", 2, Undefined, None):
            with self.subTest(response_id=response_id):
                try:
                    Response(body="for testing purposes", response_id=response_id)
                except TypeError as exception:
                    self.fail(exception)

        with self.assertRaises(TypeError) as context:
            Response(body="for testing purposes", response_id=[1, 2, 3])

        self.assertIn("must be an optional string or number", str(context.exception))

    def test_hash(self) -> None:
        response_id0: str = self.random_id
        actual0: int = hash(Response(body=[1, 2, 3], response_id=response_id0))
        expected0: int = hash(((1, 2, 3), Undefined, response_id0))
        self.assertEqual(actual0, expected0)

        response_id1: str = self.random_id
        actual1: int = hash(Response(body={"a": True, "b": False}, response_id=response_id1))
        expected1: int = hash(((("a", True), ("b", False)), Undefined, response_id1))
        self.assertEqual(actual1, expected1)

        response_id2: str = self.random_id
        actual2: int = hash(Response(body={"a": True, "b": [1, 2, 3]}, response_id=response_id2))
        expected2: int = hash(((("a", True), ("b", (1, 2, 3))), Undefined, response_id2))
        self.assertEqual(actual2, expected2)

        actual3: int = hash(Response(error=Error(code=ErrorEnum.INTERNAL_ERROR, message="response3")))
        expected3: int = hash((Undefined, (ErrorEnum.INTERNAL_ERROR, "response3", Undefined), Undefined))
        self.assertEqual(actual3, expected3)

        response_id4: str = self.random_id
        actual4: int = hash(Response(error=Error(code=ErrorEnum.INTERNAL_ERROR, message="ERROR", data=[1, 2, 3]), response_id=response_id4))
        expected4: int = hash((Undefined, (ErrorEnum.INTERNAL_ERROR, "ERROR", (1, 2, 3)), response_id4))
        self.assertEqual(actual4, expected4)

    def test_equality(self) -> None:
        response_id: str = self.random_id
        response: Response = Response(body="for testing purposes", response_id=response_id)
        self.assertEqual(response, Response(body="for testing purposes", response_id=response_id))
        self.assertNotEqual(response, object())
        self.assertNotEqual(response, Response(body="for testing purposes", response_id=self.random_id))

    def test_properties(self) -> None:
        response_id: str = self.random_id
        successful_response: Response = Response(body="for testing purposes", response_id=response_id)
        self.assertTrue(successful_response.is_successful)
        self.assertEqual(successful_response.body, "for testing purposes")
        self.assertEqual(successful_response.response_id, response_id)

        with self.assertRaises(AttributeError) as context:
            getattr(successful_response, "error")

        self.assertEqual(str(context.exception), "Successful response has not a 'error' attribute")

        error: Error = Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes")
        erroneous_response: Response = Response(error=error, response_id=None)
        self.assertFalse(erroneous_response.is_successful)
        self.assertEqual(erroneous_response.error, error)
        self.assertIsNone(erroneous_response.response_id)

        with self.assertRaises(AttributeError) as context:
            getattr(erroneous_response, "body")

        self.assertEqual(str(context.exception), "Erroneous response has not a 'body' attribute")

    def test_json(self) -> None:
        response_id: str = self.random_id
        successful_response: Response = Response(body="for testing purposes", response_id=response_id)
        self.assertDictEqual(successful_response.json, {"jsonrpc": "2.0", "result": "for testing purposes", "id": response_id})

        error: Error = Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes", data=[1, 2, 3])
        erroneous_response: Response = Response(error=error)
        self.assertDictEqual(
            erroneous_response.json,
            {
                "jsonrpc": "2.0",
                "error": {
                    "code": ErrorEnum.INTERNAL_ERROR,
                    "message": "for testing purposes",
                    "data": [1, 2, 3],
                },
            },
        )


class TestBatchResponse(TestCase):
    @property
    def random_id(self) -> int:
        uuid: Final[UUID] = uuid4()
        return int(uuid)

    def test_hash(self) -> None:
        responses: list[Response] = [
            Response(body=[1, 2, 3], response_id=self.random_id),
            Response(body={"a": True, "b": False}, response_id=self.random_id),
            Response(body={"a": True, "b": [1, 2, 3]}, response_id=self.random_id),
            Response(error=Error(code=ErrorEnum.INTERNAL_ERROR, message="response3")),
            Response(error=Error(code=ErrorEnum.INTERNAL_ERROR, message="response4", data=[1, 2, 3]), response_id=self.random_id),
        ]
        batch_response: BatchResponse = BatchResponse(responses)
        self.assertEqual(hash(batch_response), hash(tuple(responses)))

    def test_equality(self) -> None:
        error: Error = Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes", data=[1, 2, 3])
        responses: list[Response] = [
            Response(body="for testing purposes", response_id=self.random_id),
            Response(error=error),
        ]
        batch_response: BatchResponse = BatchResponse(responses)
        self.assertEqual(batch_response, BatchResponse(responses))
        self.assertNotEqual(batch_response, None)

    def test_iterable(self) -> None:
        error: Error = Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes", data=[1, 2, 3])
        batch_response: BatchResponse = BatchResponse(
            [
                Response(body="for testing purposes", response_id=self.random_id),
                Response(error=error),
            ]
        )

        self.assertIsInstance(batch_response, Iterable)
        self.assertTrue(batch_response)
        self.assertEqual(len(batch_response), 2)

        for response in batch_response:
            with self.subTest(response=response):
                self.assertIsInstance(response, Response)

    def test_json(self) -> None:
        response_id: int = self.random_id
        error: Error = Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes", data=[1, 2, 3])
        batch_response: BatchResponse = BatchResponse(
            [
                Response(body="for testing purposes", response_id=response_id),
                Response(error=error),
            ]
        )

        self.assertIsInstance(response_data := batch_response.json, MutableSequence)
        self.assertEqual(len(response_data), 2)
        self.assertIn(
            {
                "jsonrpc": "2.0",
                "result": "for testing purposes",
                "id": response_id,
            },
            response_data,
        )
        self.assertIn(
            {
                "jsonrpc": "2.0",
                "error": {
                    "code": ErrorEnum.INTERNAL_ERROR,
                    "message": "for testing purposes",
                    "data": [1, 2, 3],
                },
            },
            response_data,
        )
