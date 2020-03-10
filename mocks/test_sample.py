from unittest.mock import patch

import pytest


class SomeClass:

    def some_method(self):
        return "NOT PATCHED"


def test_sample_context_manager():

    with patch('mocks.test_sample.SomeClass.some_method') as patched:
        patched.return_value = "BOOM"
        assert SomeClass().some_method() == "BOOM"


@patch('mocks.test_sample.SomeClass.some_method', lambda self: "BOOOM")
def test_decorator():
        assert SomeClass().some_method() == "BOOOM"


class TestEvenWithFixtures:

    @pytest.fixture(scope='class')
    def patched_class(self):
        with patch('mocks.test_sample.SomeClass.some_method') as patched:
            patched.return_value = "BOOM"
            yield

    def test_not_patched(self):
        assert SomeClass().some_method() == "NOT PATCHED"

    def test_patched(self, patched_class):
        assert SomeClass().some_method() == "BOOM"
