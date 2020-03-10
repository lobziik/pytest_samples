"""
http://doc.pytest.org/en/latest/mark.html#mark
http://doc.pytest.org/en/latest/example/markers.html#mark-run
https://docs.pytest.org/en/latest/fixture.html#usefixtures
"""
import pytest


pytestmark = [pytest.mark.whole_module, pytest.mark.usefixtures('some_fixture')]


@pytest.mark.some_mark
def test_one():
    assert False


@pytest.mark.other_mark
def test_two():
    assert False


@pytest.mark.third_mark
def test_three():
    assert False
