import pytest


@pytest.fixture(scope='module', autouse=True)
def module_level_setup():
    print('MODULE LEVEL SETUP CODE')
    yield
    print('MODULE LEVEL TEARDOWN CODE')
