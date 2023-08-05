import json
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import re
import os

import pytest
import responses

from pytos2.securetrack import StAPI
from pytos2.securetrack.entrypoint import St


@pytest.fixture
def st_api():
    return StAPI(username="username", password="password", hostname="198.18.0.1")


@pytest.fixture
def st():
    return St(username="username", password="password", hostname="198.18.0.1")


@pytest.fixture
def st_no_cache():
    return St(
        username="username",
        password="password",
        hostname="198.18.0.1",
        cache=False,
        default=False,
    )


@pytest.fixture
def generic_devices_mock(st):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/generic_devices",
        json=json.load(
            open("tests/securetrack/json/generic_devices/generic_devices.json")
        ),
        match_querystring=True,
    ),

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/generic_devices?name=vm",
        json=json.load(
            open("tests/securetrack/json/generic_devices/generic_devices_filtered.json")
        ),
        match_querystring=True,
    ),

    responses.add(
        responses.POST, "https://198.18.0.1/securetrack/api/generic_devices", status=201
    )

    responses.add(
        responses.PUT,
        "https://198.18.0.1/securetrack/api/generic_devices/2",
        status=204,
    )

    responses.add(
        responses.DELETE,
        "https://198.18.0.1/securetrack/api/generic_devices/3?update_topology=False",
        status=204,
    )


@pytest.fixture
def generic_devices_getter_error(st):
    responses.add(
        responses.GET, "https://198.18.0.1/securetrack/api/generic_devices", status=500
    ),
    pass


@pytest.fixture
def generic_devices_error_mock(st):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/generic_devices",
        json=json.load(
            open("tests/securetrack/json/generic_devices/generic_devices.json")
        ),
    ),

    responses.add(
        responses.POST, "https://198.18.0.1/securetrack/api/generic_devices", status=400
    )

    responses.add(
        responses.PUT,
        "https://198.18.0.1/securetrack/api/generic_devices/2",
        status=400,
    )

    responses.add(
        responses.DELETE,
        "https://198.18.0.1/securetrack/api/generic_devices/3?update_topology=False",
        status=400,
    )


@pytest.fixture
def sample_generic_device_csv():
    return open(
        "tests/securetrack/json/generic_devices/sample_generic_device.csv"
    ).read()


@pytest.fixture
def topology_sync_mock():
    responses.add(
        responses.POST,
        "https://198.18.0.1/securetrack/api/topology/synchronize",
        status=200,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/topology/synchronize/status",
        status=200,
        json=json.load(open("tests/securetrack/json/topology/status.json")),
    )


@pytest.fixture
def topology_sync_auth_error_mock():
    responses.add(
        responses.POST,
        "https://198.18.0.1/securetrack/api/topology/synchronize",
        status=401,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/topology/synchronize/status",
        status=401,
    )


@pytest.fixture
def topology_sync_500_mock():
    responses.add(
        responses.POST,
        "https://198.18.0.1/securetrack/api/topology/synchronize",
        status=500,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/topology/synchronize/status",
        status=500,
    )


@pytest.fixture
def topology_sync_502_mock():
    responses.add(
        responses.POST,
        "https://198.18.0.1/securetrack/api/topology/synchronize",
        status=502,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/topology/synchronize/status",
        status=502,
    )


@pytest.fixture
def devices_mock(st):
    def device_callback(request):
        parts = request.url.split("/")
        _id = int(parts[-1])

        try:
            _json = json.load(open(f"tests/securetrack/json/devices/device-{_id}.json"))
        except FileNotFoundError:
            return (404, {}, "{}")

        _json = {"device": _json}
        return (200, {}, json.dumps(_json))

    responses.add_callback(
        responses.GET,
        re.compile("https://198.18.0.1/securetrack/api/devices/(\\d+)$"),
        callback=device_callback,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices",
        json=json.load(open("tests/securetrack/json/devices/devices.json")),
    )


@pytest.fixture
def device_rules_mock(st):
    def device_rules_callback(request):
        parts = request.url.split("/")
        _id = int(parts[-1])

        try:
            _json = json.load(open(f"tests/securetrack/json/rules/device-{_id}.json"))
        except FileNotFoundError:
            return (404, {}, "{}")

        return (200, {}, json.dumps(_json))

    responses.add_callback(
        responses.GET,
        re.compile("https://198.18.0.1/securetrack/api/devices/(\\d+)$"),
        callback=device_rules_callback,
    )


@pytest.fixture
def device_policies_mock():
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/20/policies",
        json=json.load(open("tests/securetrack/json/policies/20.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/400000/policies",
        status=404,
    )


@pytest.fixture
def devices_for_rule_test_mock(st):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices",
        json=json.load(open("tests/securetrack/json/devices/for-rule-test.json")),
    )


@pytest.fixture
def search_rules_mock(st):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/rule_search",
        json=json.load(open("tests/securetrack/json/rules/rule_search-105.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/rule_search/105?start=0&count=3000",
        json=json.load(open("tests/securetrack/json/rules/rule_search-105-all-1.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/rule_search/105?start=3000&count=3000",
        json=json.load(open("tests/securetrack/json/rules/rule_search-105-all-2.json")),
    )


@pytest.fixture
def rules_mock(st):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/8/rules",
        json=json.load(open("tests/securetrack/json/rules/device-8.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/20/rules?add=documentation&uid=%7b3A1BA062-6B19-4C97-8F18-79CBA9EF0AA6%7d",
        json=json.load(open("tests/securetrack/json/rules/device-20-with-uid.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/revisions/2285/rules?add=documentation&uid=Datacenter_access_in_@_8",
        json=json.load(
            open("tests/securetrack/json/rules/revision-2285-with-uid.json")
        ),
    )

    for i in (1, 5, 7, 20, 21):
        responses.add(
            responses.GET,
            f"https://198.18.0.1/securetrack/api/devices/{i}/rules?add=documentation",
            json=json.load(
                open(f"tests/securetrack/json/rules/device-{i}-add-documentation.json")
            ),
        )
    responses.add(
        responses.GET, "https://198.18.0.1/securetrack/api/devices/10/rules", status=500
    )
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/revisions/2285/rules",
        json=json.load(open("tests/securetrack/json/rules/device-8.json")),
    )
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/revisions/2226/rules",
        status=500,
    )


@pytest.fixture
def revisions_mock(st):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/8/latest_revision",
        json=json.load(
            open("tests/securetrack/json/revisions/device-8-latest-revision.json")
        ),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/100000",
        status=404,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/100000/latest_revision",
        status=404,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/100000/revisions",
        status=404,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/8/revisions",
        json=json.load(open("tests/securetrack/json/revisions/device-8.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/revisions/2226",
        json=json.load(open("tests/securetrack/json/revisions/revision-2226.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/revisions/2285",
        json=json.load(open("tests/securetrack/json/revisions/revision-2285.json")),
    )

    responses.add(
        responses.GET, "https://198.18.0.1/securetrack/api/revisions/400000", status=404
    )


@pytest.fixture
def network_objects_mock(devices_mock):
    def device_cb(request):
        device_id = request.path_url.split("/")[-2]

        fileString = f"tests/securetrack/json/network_objects/{device_id}.json"

        if not os.path.exists(fileString):
            return (404, {}, "")
        else:
            return (200, {}, open(fileString).read())

    def search_cb(request):
        # key: value dictionary of params, but the value is a list in case there are multiple values for a single query param
        params = parse_qs(urlparse(request.path_url).query)
        if params.get("filter", [None])[0] == "uid":
            uid = params.get("uid", [None])[0]
            _json = Path(f"tests/securetrack/json/network_objects/{uid}.json")
            if _json.is_file():
                return (200, {}, _json.open().read())
        return (200, {}, json.dumps({"network_objects": {}}))

    responses.add_callback(
        responses.GET,
        re.compile(r"https://198.18.0.1/securetrack/api/devices/\d+/network_objects"),
        callback=device_cb,
    )

    responses.add_callback(
        responses.GET,
        re.compile(r"https://198.18.0.1/securetrack/api/network_objects/search"),
        callback=search_cb,
    )


@pytest.fixture
def services_mock():
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/devices/1/services",
        json=json.load(open("tests/securetrack/json/services/1.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/services/search?filter=uid&uid=3fbd8116-3801-4bee-8593-3cbf999da671",
        match_querystring=True,
        json=json.load(
            open(
                "tests/securetrack/json/services/search-3fbd8116-3801-4bee-8593-3cbf999da671.json"
            )
        ),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/services/search?filter=uid&uid=3fbd8116-3801-4bee-8593-3cbf999da671&device_id=1",
        match_querystring=True,
        json=json.load(
            open(
                "tests/securetrack/json/services/search-device-1-3fbd8116-3801-4bee-8593-3cbf999da671.json"
            )
        ),
    )


@pytest.fixture
def zone_subnets_mock(st):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/zones/78/entries",
        json=json.load(open("tests/securetrack/json/zones/zone-entries-78.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/zones/200/entries",
        status=404,
    )


@pytest.fixture
def zone_descendants_mock(st):
    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/zones/80/descendants",
        json=json.load(open("tests/securetrack/json/zones/zone-descendants-80.json")),
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/zones/200/descendants",
        status=404,
    )


@pytest.fixture
def zones_mock(st):
    def zone_callback(request):
        parts = request.url.split("/")
        _id = int(parts[-1])

        try:
            _json = json.load(open(f"tests/securetrack/json/zones/zone-{_id}.json"))
        except FileNotFoundError:
            return (404, {}, "{}")

        return (200, {}, json.dumps(_json))

    responses.add_callback(
        responses.GET,
        re.compile("https://198.18.0.1/securetrack/api/zones/(\\d+)$"),
        callback=zone_callback,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/zones",
        json=json.load(open("tests/securetrack/json/zones/zones.json")),
    )


@pytest.fixture()
def test_post_add_domain_json():
    json.load(open("tests/securetrack/json/domain/post_add_domain.json"))


@pytest.fixture
def domains_mock(st):
    def domain_callback(request):
        parts = request.url.split("/")
        _id = int(parts[-1])

        try:
            _json = json.load(open(f"tests/securetrack/json/domains/domain-{_id}.json"))
        except FileNotFoundError:
            return (404, {}, "{}")

        return (200, {}, json.dumps(_json))

    responses.add_callback(
        responses.GET,
        re.compile("https://198.18.0.1/securetrack/api/domains/(\\d+)$"),
        callback=domain_callback,
    )

    responses.add(
        responses.GET,
        "https://198.18.0.1/securetrack/api/domains",
        json=json.load(open("tests/securetrack/json/domains/domains.json")),
    )

    responses.add(
        responses.POST,
        "https://198.18.0.1/securetrack/api/domains/",
        headers={"Location": "https://198.18.0.1/securetrack/api/domains/7"},
    )
    responses.add(responses.PUT, "https://198.18.0.1/securetrack/api/domains/7")


@pytest.fixture
def generic_interfaces_mock(st):
    def interface_callback(request):
        parts = request.url.split("/")
        _id = int(parts[-1])

        try:
            _json = json.load(
                open(f"tests/securetrack/json/generic_interfaces/int-{_id}.json")
            )
        except FileNotFoundError:
            return (
                404,
                {},
                json.dumps({"result": {"message": "Generic Interface Not Found"}}),
            )

        return (200, {}, json.dumps(_json))

    def management_callback(request):
        parts = request.url.split("/")
        _id = int(parts[-1])

        try:
            _json = json.load(
                open(f"tests/securetrack/json/generic_interfaces/mgmt-{_id}.json")
            )
        except FileNotFoundError:
            return (
                404,
                {},
                json.dumps({"result": {"message": "Management Not Found"}}),
            )

        return (200, {}, json.dumps(_json))

    """Get Interface by ID"""
    responses.add_callback(
        responses.GET,
        re.compile(
            "https://198.18.0.1/securetrack/api/topology/generic/interface/(\\d+)$"
        ),
        callback=interface_callback,
    )

    """Get Interfaces by Management ID"""
    responses.add_callback(
        responses.GET,
        re.compile(
            "https://198.18.0.1/securetrack/api/topology/generic/interface/mgmt/(\\d+)$"
        ),
        callback=management_callback,
    )

    """Delete Interface by ID"""
    responses.add_callback(
        responses.DELETE,
        re.compile(
            "https://198.18.0.1/securetrack/api/topology/generic/interface/(\\d+)$"
        ),
        callback=interface_callback,
    )

    """Delete Interfaces by Management ID"""
    responses.add_callback(
        responses.DELETE,
        re.compile(
            "https://198.18.0.1/securetrack/api/topology/generic/interface/mgmt/(\\d+)$"
        ),
        callback=management_callback,
    )
