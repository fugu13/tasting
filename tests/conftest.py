import pytest

import tasting


pytest_plugins = ["pytester"]


@pytest.fixture
def taste():
    tasting.TASTE_CHECKING = True
    yield
    tasting.TASTE_CHECKING = False
