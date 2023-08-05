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

from collections.abc import Callable, Hashable, MutableMapping
from random import uniform
from types import FunctionType, LambdaType
from typing import Literal, NoReturn, SupportsInt, TypeVar
from unittest.case import TestCase

from jsonrpc._dispatcher import BaseDispatcher, Dispatcher
from jsonrpc._errors import Error, ErrorEnum

_T = TypeVar("_T")


class TestDispatcher(TestCase):
    def setUp(self) -> None:
        self.dispatcher: Dispatcher = Dispatcher()

    def test_abc(self) -> None:
        self.assertIsInstance(self.dispatcher, BaseDispatcher)
        self.assertIsInstance(self.dispatcher, MutableMapping)

    def test_hash(self) -> None:
        lambda_true: Callable[..., Literal[True]] = lambda: True
        lambda_false: Callable[..., Literal[False]] = lambda: False

        self.dispatcher["lambda_true"] = lambda_true
        self.assertIn("lambda_true", self.dispatcher)
        self.assertIsInstance(self.dispatcher["lambda_true"], LambdaType)
        self.assertEqual(self.dispatcher["lambda_true"], lambda_true)

        self.dispatcher["lambda_false"] = lambda_false
        self.assertIn("lambda_false", self.dispatcher)
        self.assertIsInstance(self.dispatcher["lambda_false"], LambdaType)
        self.assertEqual(self.dispatcher["lambda_false"], lambda_false)

        self.assertIsInstance(self.dispatcher, Hashable)
        self.assertEqual(hash(self.dispatcher), hash(frozenset(self.dispatcher.items())))

    def test_register_not_function(self) -> None:
        with self.assertRaises(RuntimeError) as context:
            self.dispatcher.register(print)

        self.assertIn("isn't a user-defined function", str(context.exception))

    def test_register_already_defined(self) -> None:
        sentinel: Callable[..., None] = lambda: None
        self.dispatcher.register(sentinel, function_name="lambda")

        with self.assertRaises(RuntimeError) as context:
            self.dispatcher.register(sentinel, function_name="lambda")

        self.assertIn("is already defined", str(context.exception))

    def test_dispatch_non_existent_function(self) -> None:
        with self.assertRaises(Error) as context:
            self.dispatcher.dispatch("non_existent_function")

        self.assertEqual(context.exception.code, ErrorEnum.METHOD_NOT_FOUND)

    def test_dispatch_non_existent_parameter(self) -> None:
        sentinel: Callable[[_T], _T] = self.dispatcher.register(lambda obj: obj)
        self.assertIn(sentinel.__name__, self.dispatcher)

        with self.assertRaises(Error) as context:
            self.dispatcher.dispatch(sentinel.__name__, non_existent_parameter="non_existent_parameter")

        self.assertEqual(context.exception.code, ErrorEnum.INVALID_PARAMETERS)

    def test_dispatch_division(self) -> None:
        @self.dispatcher.register(function_name="my_div")
        def div(a: float, b: float) -> float:
            return a / b

        self.assertNotIn("div", self.dispatcher)
        self.assertIn("my_div", self.dispatcher)
        self.assertIsInstance(self.dispatcher["my_div"], FunctionType)
        self.assertEqual(self.dispatcher["my_div"], div)

        with self.assertRaises(Error) as context:
            self.dispatcher.dispatch("my_div", 1024.0, 0.0)

        self.assertEqual(context.exception.code, ErrorEnum.INTERNAL_ERROR)
        self.assertIn("division by zero", context.exception.message)

        for a, b in zip((uniform(0.0, 1000.0) for _ in range(10)), (uniform(1000.0, 2000.0) for _ in range(10))):
            with self.subTest(a=a, b=b):
                self.assertEqual(self.dispatcher.dispatch("my_div", a, b), div(a, b))

    def test_dispatch_raising(self) -> None:
        @self.dispatcher.register
        def raising(*, code: SupportsInt, message: str) -> NoReturn:
            raise Error(code=code, message=message)

        self.assertIn("raising", self.dispatcher)
        self.assertIsInstance(self.dispatcher["raising"], FunctionType)
        self.assertEqual(self.dispatcher["raising"], raising)

        with self.assertRaises(Error) as context:
            self.dispatcher.dispatch("raising", code=ErrorEnum.INTERNAL_ERROR, message="for testing purposes")

        self.assertEqual(context.exception.code, ErrorEnum.INTERNAL_ERROR)
        self.assertEqual(context.exception.message, "for testing purposes")
