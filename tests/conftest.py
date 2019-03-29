import pytest

import tasting


pytest_plugins = ["pytester"]


@pytest.fixture
def taste():
    tasting.TASTE_CHECKING = True
    yield
    tasting.TASTE_CHECKING = False


@pytest.fixture
def needs():
    return tasting.needs.qa("Needs!")


@pytest.fixture
def checkpoint():
    return tasting.checkpoint("Checkpoint!")


@pytest.fixture
def simple_nesting(needs, checkpoint):
    @needs
    def inner():
        pass

    @checkpoint
    def outer():
        inner()

    return outer
