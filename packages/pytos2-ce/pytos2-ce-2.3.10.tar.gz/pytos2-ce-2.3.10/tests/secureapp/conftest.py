import json
import re

import pytest  # type: ignore
import responses

from pytos2.secureapp import SaAPI
from pytos2.secureapp.entrypoint import Sa


@pytest.fixture
def sa_api():
    return SaAPI(username="username", password="password", hostname="198.18.0.1")


@pytest.fixture
def sa():
    return Sa(username="username", password="password", hostname="198.18.0.1")


@pytest.fixture
def application_identities_mock():
    application_identities_json = json.load(
        open("tests/secureapp/json/application_identities.json")
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securechangeworkflow/api/secureapp/repository/application_identities",
        json=application_identities_json,
    )


@pytest.fixture
def failure_mock():
    responses.add(
        responses.GET,
        re.compile("https://198.18.0.1/securechangeworkflow/api/secureapp.*"),
        status=500,
    )
