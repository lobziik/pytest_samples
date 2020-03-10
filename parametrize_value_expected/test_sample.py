from .conftest import parametrize_value_expected


@parametrize_value_expected(
    ('value', 'value'),
    ('other_value', 'other_value'),
    ('boom', 'it_will_fail')
)
def test_something(value, expected):
    assert value == expected
