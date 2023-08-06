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

from collections.abc import MutableMapping
from unittest.case import TestCase

from jsonrpc._errors import Error, ErrorEnum
from jsonrpc._utilities import Undefined


class TestError(TestCase):
    def setUp(self) -> None:
        self.error: Error = Error(
            code=ErrorEnum.INTERNAL_ERROR,
            message="for testing purposes",
            data={"additional": "information"},
        )

    def test_string_representation(self) -> None:
        self.assertEqual(str(self.error), f"{self.error.message!s} ({self.error.code:d})")

    def test_hash(self) -> None:
        actual0: int = hash(Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes"))
        expected0: int = hash((ErrorEnum.INTERNAL_ERROR, "for testing purposes", Undefined))
        self.assertEqual(actual0, expected0)

        actual1: int = hash(Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes", data=[1, 2, 3]))
        expected1: int = hash((ErrorEnum.INTERNAL_ERROR, "for testing purposes", (1, 2, 3)))
        self.assertEqual(actual1, expected1)

    def test_equality(self) -> None:
        self.assertNotEqual(self.error, object())
        error: Error = Error(
            code=ErrorEnum.INTERNAL_ERROR,
            message="for testing purposes",
            data={"additional": "information"},
        )
        self.assertEqual(self.error.code, error.code)
        self.assertEqual(self.error.message, error.message)
        self.assertEqual(self.error.data, error.data)

        self.assertEqual(self.error, error)
        self.assertNotEqual(self.error, Error(code=ErrorEnum.INTERNAL_ERROR, message="for production purposes"))

    def test_json(self) -> None:
        self.assertIsInstance(self.error.json, MutableMapping)
        for key in ("code", "message", "data"):
            with self.subTest(key=key):
                self.assertIn(key, self.error.json)

        self.assertDictEqual(
            self.error.json,
            {
                "code": ErrorEnum.INTERNAL_ERROR,
                "message": "for testing purposes",
                "data": {"additional": "information"},
            },
        )

        error: Error = Error(code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes")
        self.assertNotIn("data", error.json)
        self.assertDictEqual(error.json, {"code": ErrorEnum.INTERNAL_ERROR, "message": "for testing purposes"})
