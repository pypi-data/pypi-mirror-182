import json
from typing import List

import pytest  # type: ignore
import responses  # type: ignore

from pytos2.securechange import ScwAPI
from pytos2.securechange.entrypoint import Scw
from pytos2.securechange.ticket import Ticket, ApplicationDetails
from tests.securetrack.conftest import (
    st,
    network_objects_mock,
    devices_mock,
    device_rules_mock,
)  # noqa
from pytos2.securechange.fields import MultiAccessRequest

from pytos2.securetrack.device import Device
from pytos2.securetrack.rule import SecurityRule
from pytos2.securetrack.network_object import NetworkObject

from pytos2.securetrack import St


class MockExit(Exception):
    pass


def _api_path(path):
    return f"https://198.18.0.1/securechangeworkflow/api/securechange/{path}"


@pytest.fixture
def st_api():
    return StAPI(username="username", password="password", hostname="198.18.0.1")


@pytest.fixture
def st():
    return St(username="username", password="password", hostname="198.18.0.1")


@pytest.fixture
def device_20_network_objects():
    js = json.load(open("tests/securetrack/json/network_objects/20.json"))
    objects = [
        NetworkObject.kwargify(j) for j in js["network_objects"]["network_object"]
    ]
    return objects


@pytest.fixture
def device_20_rules():
    dev = json.load(open("tests/securetrack/json/devices/device-20.json"))
    dev = Device.kwargify(dev)

    js = json.load(open("tests/securetrack/json/rules/device-20.json"))
    rules = [SecurityRule.kwargify(j) for j in js["rules"]["rule"]]

    for rule in rules:
        rule.device = dev

    return rules


@pytest.fixture
def mock_devices() -> List[Device]:
    js = json.load(open("tests/securetrack/json/devices/devices.json"))
    devices = [Device.kwargify(j) for j in js["devices"]["device"]]
    return devices


@pytest.fixture
def st_devices_mock(st):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices",
        json=json.load(open(f"tests/securetrack/json/devices/devices.json")),
    )


@pytest.fixture
def device_20_rules_mock(st, st_devices_mock):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/20/rules",
        json=json.load(open(f"tests/securetrack/json/rules/device-20.json")),
    )


@pytest.fixture
def device_1_rules():
    dev = json.load(open("tests/securetrack/json/devices/device-1.json"))
    dev = Device.kwargify(dev)

    js = json.load(open("tests/securetrack/json/rules/device-1.json"))
    rules = [SecurityRule.kwargify(j) for j in js["rules"]["rule"]]

    for rule in rules:
        rule.device = dev

    return rules


@pytest.fixture
def all_fields_ticket_json():
    return json.load(open("tests/securechange/json/ticket/all_fields-ticket.json"))


@pytest.fixture
def all_fields_workflow_json(scw_api, all_fields_ticket_json):
    return json.load(open("tests/securechange/json/all_fields-workflow.json"))


@pytest.fixture
def all_fields_step_json(all_fields_ticket_json):
    return [step["name"] for step in all_fields_ticket_json["ticket"]["steps"]["step"]]


@pytest.fixture
def all_fields_field_json(all_fields_ticket_json):
    return all_fields_ticket_json["ticket"]["steps"]["step"][0]["tasks"]["task"][
        "fields"
    ]


@pytest.fixture
def application_details():
    return ApplicationDetails.kwargify(
        json.load(open("tests/securechange/json/application_details.json"))
    )


@pytest.fixture
def post_bad_ticket_json():
    json.load(open("tests/securechange/json/ticket/post_bad_ticket.json"))


@pytest.fixture
def closed_group_modify_ticket(scw_api):
    return Ticket.kwargify(
        json.load(
            open("tests/securechange/json/ticket/closed_group_modify-ticket.json")
        )
    )


@pytest.fixture
def closed_ticket(scw_api):
    return Ticket.kwargify(json.load(open("tests/securechange/json/ticket/redo.json")))


@pytest.fixture
def first_step_ticket(scw_api):
    ticket = json.load(open("tests/securechange/json/ticket/redo.json"))
    redo = ticket["ticket"]
    step_one = redo["steps"]["step"][0]
    redo["status"] = "In Progress"
    redo["steps"]["step"] = [step_one]
    redo["current_step"] = {"id": step_one["id"], "name": step_one["name"]}
    return Ticket.kwargify(ticket)


@pytest.fixture
def redo_ticket(scw_api):
    ticket = json.load(open("tests/securechange/json/ticket/redo.json"))
    redo = ticket["ticket"]
    step_two = redo["steps"]["step"][1]
    redo["status"] = "In Progress"
    redo["steps"]["step"] = redo["steps"]["step"][0:2]
    redo["current_step"] = {"id": step_two["id"], "name": step_two["name"]}
    return Ticket.kwargify(ticket)


@pytest.fixture
def open_access_request_ticket(scw_api):
    return Ticket.kwargify(
        json.load(
            open("tests/securechange/json/ticket/open_with_access_request-ticket.json")
        )
    )


@pytest.fixture
def open_group_modify_ticket(scw_api):
    return Ticket.kwargify(
        json.load(
            open("tests/securechange/json/ticket/open_with_group_modify-ticket.json")
        )
    )


@pytest.fixture
def ar_with_designer_results():
    return MultiAccessRequest.kwargify(
        json.load(
            open(
                "tests/securechange/json/field/multi_access_request_with_designer_results-field.json"
            )
        )
    )


@pytest.fixture
def tickets_mock():
    responses.add(
        responses.GET,
        "https://198.18.0.1/securechangeworkflow/api/securechange/tickets",
        json=json.load(open("tests/securechange/json/ticket/tickets-0-99.json")),
    )

    responses.add(
        responses.GET,
        "https://10.100.0.1/securechangeworkflow/api/securechange/tickets/fake-url-due-to-params/count_100/start_100",
        json=json.load(open("tests/securechange/json/ticket/tickets-100-199.json")),
    )


@pytest.fixture
def scw_api():
    return ScwAPI(username="username", password="password", hostname="198.18.0.1")


@pytest.fixture
def scw():
    return Scw(username="username", password="password", hostname="198.18.0.1")


@pytest.fixture
def ticket_search_mock():
    ticket_search_by_status = json.load(
        open("tests/securechange/json/ticket/ticket_search_assigned.json")
    )

    ticket_search_by_step = json.load(
        open("tests/securechange/json/ticket/ticket_search_by_step_name.json")
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/search?status=ASSIGNED",
        json=ticket_search_by_status,
        match_querystring=True,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/search?current_step=manual%20step",
        json=ticket_search_by_step,
    )


@pytest.fixture
@responses.activate
def all_fields_mock(scw_api, all_fields_ticket_json):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/283",
        json=all_fields_ticket_json,
    )
    return Ticket.get(283)


@pytest.fixture
def all_fields_ticket(scw_api, all_fields_ticket_json):
    return Ticket.kwargify(all_fields_ticket_json)


@pytest.fixture
def dynamic_assignment_ticket(scw_api, all_fields_ticket_json):
    return Ticket.kwargify(
        json.load(open("tests/securechange/json/ticket/dynamic_assignment-ticket.json"))
    )


@pytest.fixture
def get_test_field():
    def f(field_cls):
        xsi_type = [
            a.default for a in field_cls.__attrs_attrs__ if a.name == "xsi_type"
        ][0]
        return field_cls.kwargify(
            json.load(
                open(f"tests/securechange/json/field/{xsi_type.value}-field.json")
            )
        )

    return f


@pytest.fixture
def users_mock():
    users_json = json.load(open("tests/securechange/json/users/users_by_username.json"))
    all_users_json = json.load(open("tests/securechange/json/users/all_users.json"))

    responses.add(
        responses.GET,
        _api_path("users?user_name=r&exact_name=True"),
        match_querystring=True,
        json=users_json,
    )

    responses.add(responses.GET, _api_path("users"), json=all_users_json)


@pytest.fixture
def user_mock():
    user_json = json.load(open("tests/securechange/json/users/user_45.json"))

    responses.add(
        responses.GET, _api_path("users/45"), match_querystring=True, json=user_json
    )

    pass
