import tasting

from .report import results

import os.path
import json


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


def pytest_sessionfinish(session, exitstatus):
    logfile = "tasting.output"
    dirname = os.path.dirname(os.path.abspath(logfile))
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    logfile = open(logfile, "w", encoding="utf-8")

    json.dump(
        {
            "results": [
                {
                    "needs": result.needs.name,
                    "reason": result.needs.reason,
                    "checkpoint": result.checkpoint.description,
                }
                for result in results()
            ]
        },
        logfile,
    )

    logfile.close()
