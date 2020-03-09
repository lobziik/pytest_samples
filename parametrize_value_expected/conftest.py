import pytest

parametrize_value_expected = lambda *values: pytest.mark.parametrize('value, expected', values)
