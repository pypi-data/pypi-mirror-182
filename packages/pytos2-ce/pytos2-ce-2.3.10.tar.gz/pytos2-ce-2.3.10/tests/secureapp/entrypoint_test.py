import pytest
import responses

from . import conftest  # noqa

from pytos2.secureapp.entrypoint import Sa
from pytos2.secureapp.application_identities import ApplicationIdentity


class TestEntrypoint:
    @responses.activate
    def test_application_identities(self, sa: Sa, application_identities_mock):
        # print(dir(sa))
        identity = sa.application_identities[0]
        assert isinstance(identity, ApplicationIdentity)

    @responses.activate
    def test_application_identites_error(self, sa: Sa, failure_mock):
        with pytest.raises(ValueError):
            sa.application_identities
