import datetime

import pytest
from freezegun import freeze_time

real_today = datetime.date.today()
real_now = datetime.datetime.now()


@freeze_time("3020-11-12")
def test_back_to_the_future_date():
    assert datetime.date.today() == real_today


@freeze_time("3020-11-12")
def test_back_to_the_future_datetime():
    assert datetime.datetime.now() == real_now


def test_future_as_context_manager():
    with freeze_time(datetime.datetime(year=3020, month=3, day=12)):
        assert datetime.datetime.now() == real_now


class TestWithFixtures:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        with freeze_time("3020-11-12"):
            yield

    def test_is_it_real_freezed(self):
        assert datetime.datetime.now() == real_now
