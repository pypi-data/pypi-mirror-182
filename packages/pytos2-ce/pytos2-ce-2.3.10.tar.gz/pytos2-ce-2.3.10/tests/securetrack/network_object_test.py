import json
from pathlib import Path

from netaddr import IPAddress
import responses
import pytest
from netaddr import IPAddress, IPNetwork, IPRange

from pytos2.securetrack.network_object import classify_network_object
from pytos2.utils import get_api_node


class TestDevice:
    @pytest.fixture
    def device(self):
        j = json.load(open("tests/securetrack/json/devices/devices.json"))
        device_node = get_api_node(j, "devices.device")[0]
        return classify_network_object(device_node)


class TestLoadNetworkObjects:
    def test_all_objects(self):
        for path in Path("tests/securetrack/json/network_objects/").glob("*.json"):
            device_id = str(path).split("/")[-1].split(".")[0]
            if device_id.isdigit():
                network_objects_node = get_api_node(
                    json.load(path.open()), "network_objects.network_object"
                )
                for network_object in network_objects_node:
                    classify_network_object(network_object)


class TestCheckpointObject:
    @responses.activate
    def test_nat_object(self, st, network_objects_mock):
        # this should be refactored when get_network_object returns an object
        obj = st.get_network_object(
            device=20, name="CP_default_Office_Mode_addresses_pool"
        )
        assert obj.nat_info.mapped_to_ip == "Hide Behind Gateway"
        obj = st.get_network_object(device=20, name="Net_172.16.40.0")
        assert isinstance(obj.nat_info.mapped_to_ip, IPAddress)


class TestFortigateObject:
    @responses.activate
    def test_nat_object(self, st, network_objects_mock):
        # this should be refactored when get_network_object returns an object
        obj = st.get_network_object(device=157, name="VIP to HQ")
        assert isinstance(obj.nat_info.mapped_ip, IPAddress)
        assert isinstance(obj.nat_info.mapped_ip_max, IPAddress)


class TestHostObject:
    # this class covers host object with interfaces as well
    @responses.activate
    def test_host_object(self, st, network_objects_mock):
        # this should be refactored when get_network_object returns an object
        obj = st.get_network_object(device=184, name="SGW_200.237")
        assert isinstance(obj.ip, IPAddress)
        assert isinstance(obj.interfaces[0].interface_ips[0].ip, IPAddress)


class TestSubnetObject:
    @responses.activate
    def test_subnet_object(self, st, network_objects_mock):
        # this should be refactored when get_network_object returns an object
        obj = st.get_network_object(device=184, name="Sales_1")
        assert isinstance(obj.subnet, IPNetwork)


class TestRangeObject:
    @responses.activate
    def test_range_object(self, st, network_objects_mock):
        # this should be refactored when get_network_object returns an object
        obj = st.get_network_object(device=184, name="my_range")
        assert isinstance(obj.range, IPRange)
