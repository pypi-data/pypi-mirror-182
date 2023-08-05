import pytest
import json
import responses

from pytos2.securetrack.generic_interface import GenericInterface
from pytos2.utils import get_api_node


class TestGenericInterface:

    mgmt = json.load(open("tests/securetrack/json/generic_interfaces/mgmt-1.json"))
    ipv4Interfaces = mgmt["GenericInterfaces"]

    interface1 = json.load(open("tests/securetrack/json/generic_interfaces/int-1.json"))
    int1 = interface1["GenericInterface"]

    @responses.activate
    def test_add_generic_interfaces_201(self, st):
        """Add one or multiple interfaces"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/interface",
            status=201,
        )

        """Add single interface"""
        newInt1 = st.add_generic_interface(self.int1)
        assert newInt1 == None

        """Add multiple interfaces"""
        newInts1 = st.add_generic_interfaces(self.ipv4Interfaces)
        assert newInts1 == None

        mgmt5 = json.load(open("tests/securetrack/json/generic_interfaces/mgmt-5.json"))
        ipv6Interfaces = mgmt5["GenericInterfaces"]
        newInts2 = st.add_generic_interfaces(ipv6Interfaces)
        assert newInts2 == None

    @responses.activate
    def test_add_generic_interfaces_400(self, st):
        """POST bad request"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/interface",
            status=400,
        )

        with pytest.raises(ValueError) as exception:
            st.add_generic_interface(self.int1)
        assert "Bad Request" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.add_generic_interfaces(self.ipv4Interfaces)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_add_generic_interfaces_404(self, st):
        """POST mgmt id not found"""
        responses.add(
            responses.POST,
            "https://198.18.0.1/securetrack/api/topology/generic/interface",
            status=404,
            json={"result": {"message": "Management Not Found"}},
        )

        with pytest.raises(ValueError) as exception:
            st.add_generic_interface(self.int1)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.add_generic_interfaces(self.ipv4Interfaces)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_get_generic_interface(self, st, generic_interfaces_mock):
        """Get interface by id"""
        mockRes = get_api_node(self.interface1, "GenericInterface")
        interface = GenericInterface.kwargify(mockRes)
        intByInt = st.get_generic_interface(1)
        intByStr = st.get_generic_interface("1")
        assert intByInt == interface
        assert intByStr == interface

        with pytest.raises(ValueError) as exception:
            st.get_generic_interface(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.get_generic_interface("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_get_generic_interfaces(self, st, generic_interfaces_mock):
        """Get all interfaces associated with management id"""
        interfaces = [
            GenericInterface.kwargify(d)
            for d in get_api_node(self.mgmt, "GenericInterfaces", listify=True)
        ]
        intsByInt = st.get_generic_interfaces(1)
        intsByStr = st.get_generic_interfaces("1")
        assert intsByInt == interfaces
        assert intsByStr == interfaces

        with pytest.raises(ValueError) as exception:
            st.get_generic_interfaces(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.get_generic_interfaces("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_update_generic_interfaces_200(self, st):
        """Update one or multiple interfaces"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/interface",
            status=200,
        )

        """Update single interface"""
        newInterface = st.update_generic_interface(self.int1)
        assert newInterface == None

        """Update multiple interfaces"""
        newInterfaces = st.update_generic_interfaces(self.ipv4Interfaces)
        assert newInterfaces == None

        mgmt5 = json.load(open("tests/securetrack/json/generic_interfaces/mgmt-5.json"))
        ipv6Interfaces = mgmt5["GenericInterfaces"]
        newInterfaces = st.update_generic_interfaces(ipv6Interfaces)
        assert newInterfaces == None

    @responses.activate
    def test_update_generic_interfaces_400(self, st):
        """PUT bad request"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/interface",
            status=400,
        )

        with pytest.raises(ValueError) as exception:
            st.update_generic_interface(self.int1)
        assert "Bad Request" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.update_generic_interfaces(self.ipv4Interfaces)
        assert "Bad Request" in str(exception.value)

    @responses.activate
    def test_update_generic_interfaces_404(self, st):
        """PUT mgmt id not found"""
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securetrack/api/topology/generic/interface",
            status=404,
        )

        with pytest.raises(ValueError) as exception:
            st.update_generic_interface(self.int1)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.update_generic_interfaces(self.ipv4Interfaces)
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_delete_generic_interface(self, st, generic_interfaces_mock):
        """Delete interface by interface id"""
        intByInt = st.delete_generic_interface(1)
        intByStr = st.delete_generic_interface("1")
        assert intByInt == None
        assert intByStr == None

        with pytest.raises(ValueError) as exception:
            st.delete_generic_interface(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_generic_interface("404")
        assert "Not Found" in str(exception.value)

    @responses.activate
    def test_delete_generic_interfaces(self, st, generic_interfaces_mock):
        """Delete all interfaces associated with management id"""
        intsByInt = st.delete_generic_interfaces(1)
        intsByStr = st.delete_generic_interfaces("1")
        assert intsByInt == None
        assert intsByStr == None

        with pytest.raises(ValueError) as exception:
            st.delete_generic_interfaces(404)
        assert "Not Found" in str(exception.value)

        with pytest.raises(ValueError) as exception:
            st.delete_generic_interfaces("404")
        assert "Not Found" in str(exception.value)
