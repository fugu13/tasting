import tasting


def pytest_addoption(parser):
    group = parser.getgroup("tasting")
    group.addoption(
        "--tasting",
        action="store_true",
        dest="tasting",
        default=False,
        help="Collect and report QA needs using the tasting library",
    )


def pytest_cmdline_main(config):
    tasting.TASTE_CHECKING = config.getoption("tasting")
