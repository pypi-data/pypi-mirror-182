import pytest
import responses

from . import conftest  # noqa

# from pytos2.securechange.entrypoint import Scw
from pytos2.securechange.ticket import Ticket, TicketStatus, Task, Comment, Attachment

from pytos2.securechange.user import SCWParty, UserXsiType


class TestEntrypoint:
    @responses.activate
    def test_ticket_search(self, scw, ticket_search_mock):
        arr = scw.ticket_search(status=Task.Status.ASSIGNED)
        # first = next(arr)
        first = arr[0]
        assert first is not None

        # assert first.duration == 2180
        assert first.priority == Ticket.Priority.CRITICAL
        # assert first.workflow_name == "Reg Workflow"
        assert first.id == 8
        assert first.status == TicketStatus.INPROGRESS
        assert first.requester_name == "Smith"
        assert first.subject == "new 1401234982542"
        assert first.sla_status == Ticket.SlaStatus.ESCALATION
        assert first.current_step == "verifier"

    @responses.activate
    def test_get_users(self, scw, users_mock):
        users = scw.get_users(user_name="r", exact_name=True)

        # user = next(users)
        user = users[0]
        assert user is not None

        assert user.display_name == "r"
        assert user.origin_type == SCWParty.OriginType.LOCAL
        assert user.member_of[0].name == "Regi's Grp"
        assert user.roles[0].name == "Role with WorkFlow"
        assert user.id == 289
        assert user.xsi_type == UserXsiType.USER

    @responses.activate
    def test_get_user(self, scw, users_mock, user_mock):
        user = scw.get_user(45)

        assert user is not None

        assert user.display_name == "Johnny_Smith"
        assert user.origin_type == SCWParty.OriginType.LDAP
        assert user.member_of[0].name == "Advertising"
        assert user.roles[0].name == "Role with WorkFlow"
        assert user.id == 45
        assert user.xsi_type == UserXsiType.USER

        user = scw.get_user(45, expand=True)

        assert user is not None

        assert user.display_name == "johnny_smith"
        assert user.origin_type == SCWParty.OriginType.LDAP
        assert user.member_of[0].name == "Advertising"
        assert user.roles[0].name == "Role with WorkFlow"
        assert user.id == 45
        assert user.xsi_type == UserXsiType.USER

    @responses.activate
    def test_get_attachment(self, scw, all_fields_ticket):
        responses.add(
            responses.GET,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/288",
            json={"ticket": {**all_fields_ticket.data["ticket"], "id": 288}},
        )

        comment = all_fields_ticket.comments[0]
        assert isinstance(comment, Comment)
        attachment = comment.attachments[0]
        assert isinstance(attachment, Attachment)
        assert attachment.uid == "b5672678-d9c5-46ee-87cc-d8fa7fce1a43"
        responses.add(
            responses.GET,
            f"https://198.18.0.1/securechangeworkflow/api/securechange/attachments/{attachment.uid}",
        )
        attachment_content = scw.get_attachment(attachment.uid)
        assert isinstance(attachment_content, bytes)
