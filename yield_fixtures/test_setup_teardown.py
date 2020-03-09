import pytest


class TestCaseWithSetupTeardown:

    @pytest.fixture(autouse=True, scope='class')
    def setup_whole_test_case(self):
        print('CLASS LEVEL SETUP CODE')
        yield
        print('CLASS LEVEL TEARDOWN CODE')

    @pytest.fixture(autouse=True, scope='function')
    def setup_paticular_test(self):
        print('FUNCTION LEVEL SETUP CODE')
        yield
        print('FUNCTION LEVEL TEARDOWN CODE')

    def test_something(self, request):
        print(request.node.name)
        assert False

    def test_something_else(self, request):
        print(request.node.name)
        assert False

    def test_something_else_again(self, request):
        print(request.node.name)
        assert False


class TestCaseWithoutSetup:

    def test_something(self, request):
        print(request.node.name)
        assert False
