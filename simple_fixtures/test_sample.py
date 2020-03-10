import pytest


@pytest.fixture
def first():
    print('FIRST')


@pytest.fixture
def second(first):
    print('SECOND')


def test_sample_first(first):
    assert False


def test_sample_second(second):
    assert False

