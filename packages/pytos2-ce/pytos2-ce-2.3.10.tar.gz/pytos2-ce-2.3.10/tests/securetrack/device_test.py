import pytest
import json
import responses

from netaddr import IPAddress

from pytos2.securetrack.device import Device
from pytos2.utils import get_api_node


class TestDevice:
    @pytest.fixture
    def device(self):
        j = json.load(open("tests/securetrack/json/devices/devices.json"))
        device_node = get_api_node(j, "devices.device")[0]
        return Device.kwargify(device_node)

    def test_attributes(self, device):
        assert device.id == 1
        assert device.name == "RTR1"
        assert device.vendor == Device.Vendor.CISCO
        assert device.model == Device.Model.ROUTER
        assert isinstance(device.domain_id, int) and device.domain_id == 1
        assert device.domain_name == "Default"
        assert device.module_uid == ""
        assert device.ip == IPAddress("10.100.200.54")
        assert (
            isinstance(device.latest_revision, int) and device.latest_revision == 1674
        )
        assert device.virtual_type == ""

    def test_set_attributes(self, device):
        assert device.ip == IPAddress("10.100.200.54")

        device.ip = "1.2.3.4"
        assert device.ip == IPAddress("1.2.3.4")

    @responses.activate
    def test_properties(self, devices_mock, st):
        device = st.get_device(identifier=60)
        assert device
        assert device.name == "NSX-Edge-01"

        parent_device = device.parent
        assert parent_device.id == 58
        assert parent_device.name == "NSX"

        assert len(parent_device.children) == 4

        grandparent = parent_device.parent
        assert grandparent is None
