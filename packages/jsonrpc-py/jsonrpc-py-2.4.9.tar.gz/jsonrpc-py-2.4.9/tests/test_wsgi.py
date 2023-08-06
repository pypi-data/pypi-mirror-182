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

from collections.abc import MutableMapping, MutableSequence
from http import HTTPStatus
from io import StringIO
from os import urandom
from typing import Any, Final
from unittest.case import TestCase
from unittest.mock import patch
from uuid import UUID, uuid4

from werkzeug.test import Client, EnvironBuilder, TestResponse

from jsonrpc._errors import Error, ErrorEnum
from jsonrpc._request import BatchRequest, Request
from jsonrpc._response import BatchResponse, Response
from jsonrpc._wsgi import BaseWSGIHandler, WSGIHandler


class TestWSGIHandler(TestCase):
    @property
    def random_id(self) -> str:
        uuid: Final[UUID] = uuid4()
        return str(uuid)

    def setUp(self) -> None:
        self.application: WSGIHandler = WSGIHandler()
        self.client: Client = Client(self.application, use_cookies=False)
        self.collection: list[str] = list()

        @self.application.dispatcher.register(function_name="sum")
        def _(a: float, b: float) -> float:
            return a + b

        @self.application.dispatcher.register
        def div(*, a: float, b: float) -> float:
            return a / b

        @self.application.dispatcher.register
        def append(obj: str) -> None:
            self.collection.append(obj)

    def test_abc(self) -> None:
        self.assertIsInstance(self.application, BaseWSGIHandler)
        self.assertIsInstance(self.application, MutableMapping)

    def test_handle_request_raw_batch_request(self) -> None:
        batch_request: BatchRequest = BatchRequest.from_json(
            [
                {"jsonrpc": "2.0", "method": "sum", "params": [8192, 1024], "id": self.random_id},
                {"jsonrpc": "2.0", "method": "div", "params": {"a": 8192, "b": 1024}, "id": self.random_id},
            ]
        )
        self.assertIsInstance(batch_response := self.application.handle_request(batch_request), BatchResponse)

        for response in batch_response:
            with self.subTest(response=response):
                self.assertIsInstance(response, Response)
                self.assertTrue(response.is_successful)

    def test_handle_request_unsupported_types(self) -> None:
        tests: tuple[Any, ...] = None, True, False, "string", b"bytestring", object()
        for obj in tests:
            with (self.subTest(obj=obj), self.assertRaises(ValueError) as context):
                self.application.handle_request(obj)

            self.assertIsInstance(context.exception, ValueError)
            self.assertEqual(str(context.exception), f"Unsupported type {type(obj).__name__!r}")

    def test_handle_request_raw_request(self) -> None:
        request: Request = Request(method="div", params=[8192, 1024], request_id=self.random_id)
        self.assertIsInstance(response := self.application.handle_request(request), Response)
        self.assertFalse(response.is_successful)
        self.assertIn("too many positional arguments", response.error.message)

    def test_handle_request_raw_error(self) -> None:
        error: Error = Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes")
        self.assertIsInstance(response := self.application.handle_request(error), Response)
        self.assertFalse(response.is_successful)
        self.assertEqual("for testing purposes", response.error.message)

    def test_handle_request_runtime_error(self) -> None:
        with StringIO() as raw_buffer:
            request: EnvironBuilder = EnvironBuilder(
                method="POST",
                errors_stream=raw_buffer,
                json={"jsonrpc": "2.0", "method": "print"},
            )

            with patch.object(WSGIHandler, "_read_request_body") as mock:
                mock.side_effect = RuntimeError("for testing purposes")

                with self.assertRaises(RuntimeError) as context:
                    self.client.open(request)

            self.assertIsInstance(context.exception, RuntimeError)
            self.assertEqual(str(context.exception), "for testing purposes")
            self.assertIn("RuntimeError: for testing purposes", raw_buffer.getvalue())

    def test_forbidden_methods(self) -> None:
        responses: tuple[TestResponse, ...] = (
            self.client.head("/testHead/"),
            self.client.get("/testGet/"),
            self.client.patch(data=b""),
            self.client.delete(data=b""),
            self.client.options("/testOptions/"),
            self.client.trace("/testTrace/"),
        )
        for response in responses:
            with self.subTest(response=response):
                self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)
                self.assertIn("POST", response.allow)
                self.assertIn("PUT", response.allow)
                self.assertEqual(response.data, b"")

    def test_empty_request(self) -> None:
        responses: tuple[TestResponse, ...] = (
            self.client.post(data=b""),
            self.client.put(data=b""),
        )
        for response in responses:
            with self.subTest(response=response):
                self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
                self.assertEqual(response.data, b"")

    def test_positional_parameters(self) -> None:
        uuid: str = self.random_id
        response: TestResponse = self.client.post(json={"jsonrpc": "2.0", "method": "sum", "params": [8192, 1024], "id": uuid})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableMapping)

        for key in ("jsonrpc", "result", "id"):
            with self.subTest(key=key):
                self.assertIn(key, response_data)

        self.assertEqual(response_data["jsonrpc"], "2.0")
        self.assertEqual(response_data["result"], 9216)
        self.assertEqual(response_data["id"], uuid)

    def test_named_parameters(self) -> None:
        uuid: str = self.random_id
        response: TestResponse = self.client.post(json={"jsonrpc": "2.0", "method": "div", "params": {"a": 8192, "b": 1024}, "id": uuid})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableMapping)

        for key in ("jsonrpc", "result", "id"):
            with self.subTest(key=key):
                self.assertIn(key, response_data)

        self.assertEqual(response_data["jsonrpc"], "2.0")
        self.assertEqual(response_data["result"], 8.0)
        self.assertEqual(response_data["id"], uuid)

    def test_notification(self) -> None:
        self.assertEqual(len(self.collection), 0)

        response: TestResponse = self.client.put(json={"jsonrpc": "2.0", "method": "append", "params": ["hello world"]})
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(response.data, b"")
        self.assertIn("hello world", self.collection)

    def test_large_request_body(self) -> None:
        for payload in (
            payload0 := urandom(50 * 1024 * 1024).hex(),
            payload1 := urandom(50 * 1024 * 1024).hex(),
            payload2 := urandom(50 * 1024 * 1024).hex(),
        ):
            with self.subTest(payload=payload):
                self.assertNotIn(payload, self.collection)

        response: TestResponse = self.client.put(
            json=[
                {"jsonrpc": "2.0", "method": "append", "params": [payload0]},
                {"jsonrpc": "2.0", "method": "append", "params": [payload1]},
                {"jsonrpc": "2.0", "method": "append", "params": [payload2]},
            ]
        )
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)
        self.assertEqual(response.data, b"")

        for payload in (payload0, payload1, payload2):
            with self.subTest(payload=payload):
                self.assertIn(payload, self.collection)

    def test_unexpected_client_disconnected(self) -> None:
        with StringIO() as raw_buffer:
            request: EnvironBuilder = EnvironBuilder(
                method="PUT",
                errors_stream=raw_buffer,
                environ_overrides={"CONTENT_LENGTH": "1000"},
                json={
                    "jsonrpc": "2.0",
                    "method": "append",
                    "params": ["Unexpected client disconnected"],
                },
            )

            with self.assertRaises(EOFError) as context:
                self.client.open(request)

            self.assertNotIn("Unexpected client disconnected", self.collection)
            self.assertIn("Client disconnected", str(context.exception))
            self.assertIn("more bytes were expected", raw_buffer.getvalue())

    def test_non_existent_method(self) -> None:
        uuid: str = self.random_id
        response: TestResponse = self.client.post(json={"jsonrpc": "2.0", "method": "foobar", "id": uuid})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableMapping)

        for key in ("jsonrpc", "error", "id"):
            with self.subTest(key=key):
                self.assertIn(key, response_data)

        self.assertEqual(response_data["jsonrpc"], "2.0")
        self.assertIsInstance(response_data["error"], MutableMapping)
        self.assertEqual(response_data["id"], uuid)

        for key in ("code", "message"):
            with self.subTest(key=key):
                self.assertIn(key, response_data["error"])

        self.assertEqual(response_data["error"]["code"], ErrorEnum.METHOD_NOT_FOUND)
        self.assertIsInstance(response_data["error"]["message"], str)

    def test_invalid_json(self) -> None:
        response: TestResponse = self.client.post(data=b'{"jsonrpc": "2.0", "method": "foobar, "params": "bar", "baz]')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableMapping)

        for key in ("jsonrpc", "error", "id"):
            with self.subTest(key=key):
                self.assertIn(key, response_data)

        self.assertEqual(response_data["jsonrpc"], "2.0")
        self.assertIsInstance(response_data["error"], MutableMapping)
        self.assertIsNone(response_data["id"])

        for key in ("code", "message"):
            with self.subTest(key=key):
                self.assertIn(key, response_data["error"])

        self.assertEqual(response_data["error"]["code"], ErrorEnum.PARSE_ERROR)
        self.assertIsInstance(response_data["error"]["message"], str)

    def test_invalid_request_object(self) -> None:
        response: TestResponse = self.client.post(json={"jsonrpc": "2.0", "method": 1, "params": "bar"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableMapping)

        for key in ("jsonrpc", "error", "id"):
            with self.subTest(key=key):
                self.assertIn(key, response_data)

        self.assertEqual(response_data["jsonrpc"], "2.0")
        self.assertIsInstance(response_data["error"], MutableMapping)
        self.assertIsNone(response_data["id"])

        for key in ("code", "message"):
            with self.subTest(key=key):
                self.assertIn(key, response_data["error"])

        self.assertEqual(response_data["error"]["code"], ErrorEnum.INVALID_REQUEST)
        self.assertIsInstance(response_data["error"]["message"], str)

    def test_batch_invalid_json(self) -> None:
        response: TestResponse = self.client.post(
            data=b"""
        [
            {"jsonrpc": "2.0", "method": "sum", "params": [8192, 1024], "id": 4}
            {"jsonrpc": "2.0", "method"
        ]
        """
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableMapping)

        for key in ("jsonrpc", "error", "id"):
            with self.subTest(key=key):
                self.assertIn(key, response_data)

        self.assertEqual(response_data["jsonrpc"], "2.0")
        self.assertIsInstance(response_data["error"], MutableMapping)
        self.assertIsNone(response_data["id"])

        for key in ("code", "message"):
            with self.subTest(key=key):
                self.assertIn(key, response_data["error"])

        self.assertEqual(response_data["error"]["code"], ErrorEnum.PARSE_ERROR)
        self.assertIsInstance(response_data["error"]["message"], str)

    def test_empty_array(self) -> None:
        response: TestResponse = self.client.post(json=[])
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableMapping)

        for key in ("jsonrpc", "error", "id"):
            with self.subTest(key=key):
                self.assertIn(key, response_data)

        self.assertEqual(response_data["jsonrpc"], "2.0")
        self.assertIsInstance(response_data["error"], MutableMapping)
        self.assertIsNone(response_data["id"])

        for key in ("code", "message"):
            with self.subTest(key=key):
                self.assertIn(key, response_data["error"])

        self.assertEqual(response_data["error"]["code"], ErrorEnum.INVALID_REQUEST)
        self.assertIsInstance(response_data["error"]["message"], str)

    def test_invalid_not_empty_batch(self) -> None:
        response: TestResponse = self.client.post(json=[1])
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableSequence)
        self.assertEqual(len(response_data), 1)
        self.assertIsInstance(error := response_data[0], MutableMapping)

        for key in ("jsonrpc", "error", "id"):
            with self.subTest(key=key):
                self.assertIn(key, error)

        self.assertEqual(error["jsonrpc"], "2.0")
        self.assertIsInstance(error["error"], MutableMapping)
        self.assertIsNone(error["id"])

        for key in ("code", "message"):
            with self.subTest(key=key):
                self.assertIn(key, error["error"])

        self.assertEqual(error["error"]["code"], ErrorEnum.INVALID_REQUEST)
        self.assertIsInstance(error["error"]["message"], str)

    def test_invalid_batch(self) -> None:
        response: TestResponse = self.client.post(json=[1, 2, 3])
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableSequence)
        self.assertEqual(len(response_data), 3)

        for error in response_data:
            with self.subTest(error=error):
                self.assertIsInstance(error, MutableMapping)

                for key in ("jsonrpc", "error", "id"):
                    with self.subTest(key=key):
                        self.assertIn(key, error)

                self.assertEqual(error["jsonrpc"], "2.0")
                self.assertIsInstance(error["error"], MutableMapping)
                self.assertIsNone(error["id"])

                for key in ("code", "message"):
                    with self.subTest(key=key):
                        self.assertIn(key, error["error"])

                self.assertEqual(error["error"]["code"], ErrorEnum.INVALID_REQUEST)
                self.assertIsInstance(error["error"]["message"], str)

    def test_invalid_json_response(self) -> None:
        self.application.dispatcher.register(lambda: object(), function_name="lambda")

        response: TestResponse = self.client.post(json={"jsonrpc": "2.0", "method": "lambda", "id": self.random_id})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.is_json)
        self.assertIsInstance(response_data := response.json, MutableMapping)

        for key in ("jsonrpc", "error", "id"):
            with self.subTest(key=key):
                self.assertIn(key, response_data)

        self.assertEqual(response_data["jsonrpc"], "2.0")
        self.assertIsInstance(response_data["error"], MutableMapping)
        self.assertIsNone(response_data["id"])

        for key in ("code", "message"):
            with self.subTest(key=key):
                self.assertIn(key, response_data["error"])

        self.assertEqual(response_data["error"]["code"], ErrorEnum.PARSE_ERROR)
        self.assertIsInstance(response_data["error"]["message"], str)

    def tearDown(self) -> None:
        self.application.dispatcher.clear()
        self.collection.clear()
