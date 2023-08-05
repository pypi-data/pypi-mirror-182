import json

import pytest
import responses
import pdb
from requests.exceptions import HTTPError
from . import conftest  # noqa
from pytos2.securechange.ticket import Ticket, TicketStatus, Step, Task
from pytos2.securechange.fields import (
    TextArea,
    TextField,
    Checkbox,
    FieldXsiType,
    MultiAccessRequest,
)


class TestTicketAttributes(object):
    def test_steps(self, all_fields_ticket):
        assert isinstance(all_fields_ticket.steps, list)

    def test_workflow(self, all_fields_ticket):
        workflow = all_fields_ticket.workflow

        assert workflow.name == "AR all fields"

    def test_current_step_props(self, all_fields_ticket):
        assert all_fields_ticket.current_step_index == 3
        assert all_fields_ticket.current_step_name == "No Fields"

        assert all_fields_ticket.previous_step.name == "Duplicate"

        empty_ticket = Ticket.create("test_workflow", "test_step")
        assert empty_ticket.current_step_index is None
        assert empty_ticket.previous_step is None

    @pytest.mark.parametrize(
        "attr, value",
        [
            ("id", 288),
            ("subject", "Better Tests"),
            ("requester", "r"),
            ("requester_id", 4),
            ("priority", Ticket.Priority.NORMAL),
            ("status", TicketStatus.INPROGRESS),
            ("expiration_field_name", "Expiration"),
            ("expiration_date", None),
            ("domain_name", "Default"),
            ("sla_status", Ticket.SlaStatus.NA),
            ("sla_outcome", Ticket.SlaOutcome.NA),
        ],
    )
    def test_values(self, all_fields_ticket, attr, value):
        assert getattr(all_fields_ticket, attr) == value

    def test_last_step(self, all_fields_ticket, scw):
        assert all_fields_ticket.last_step.name == "No Fields"

    def test_current_step(self, all_fields_ticket, closed_group_modify_ticket):
        assert (
            all_fields_ticket.current_step_name
            == all_fields_ticket.last_step.name
            == all_fields_ticket.data["ticket"]["current_step"]["name"]
        )
        assert closed_group_modify_ticket.current_step_name is None

    def test_access_request(
        self, open_access_request_ticket, closed_group_modify_ticket
    ):
        assert open_access_request_ticket.access_request
        assert closed_group_modify_ticket.access_request is None

    def test_group_modify(self, open_group_modify_ticket, closed_group_modify_ticket):
        assert open_group_modify_ticket.group_modify
        assert closed_group_modify_ticket.group_modify is None

    def test_last_task(self, all_fields_ticket):
        assert all_fields_ticket.last_task is all_fields_ticket.steps[-1].tasks[-1]

    def test_current_task(self, all_fields_ticket):
        assert all_fields_ticket.current_task is all_fields_ticket.steps[-1].tasks[-1]

    def test_current_task_dynamic_assignment(self, dynamic_assignment_ticket):
        with pytest.raises(ValueError):
            dynamic_assignment_ticket.current_task

    def test_current_tasks(self, all_fields_ticket):
        assert all_fields_ticket.current_tasks is all_fields_ticket.steps[-1].tasks

    def test_json(self, all_fields_ticket):
        assert isinstance(json.dumps(all_fields_ticket._json), str)

    def test_application_details(self, application_details):
        assert application_details.id == 8


class TestTicketFunctions(object):
    def test_create_ticket(self):
        ticket = Ticket.create("workflow", "test subject")
        assert ticket.subject == "test subject"
        assert ticket.workflow.name == "workflow"

        ticket.create_step("Step Name")
        assert ticket.steps[0].name == "Step Name"
        assert isinstance(ticket.steps[0], Step)

    def test_get_step(self, all_fields_ticket):
        assert (
            all_fields_ticket.get_step("invalid")
            is all_fields_ticket.get_step(100)
            is None
        )
        assert (
            all_fields_ticket.get_step("Open request")
            == all_fields_ticket.get_step(0)
            == all_fields_ticket.steps[0]
        )

    def test_get_step_by_id(self, all_fields_ticket):
        assert all_fields_ticket._get_step(1590).id == 1590

    def test_step_task(self, all_fields_ticket):
        assert (
            all_fields_ticket.get_step_task("invalid", 0)
            is all_fields_ticket.get_step_task("invalid", "invalid")
            is None
        )
        assert all_fields_ticket.get_step_task("invalid", 0) is None

    def test_step_task_fields(self, all_fields_ticket):
        assert all_fields_ticket.get_step_task_fields("invalid", 0) is None
        assert not all_fields_ticket.get_step_task_fields(1)

    @responses.activate
    def test_advance(self, first_step_ticket, redo_ticket, closed_ticket):
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/252/steps/1246/tasks/1258",
        )
        responses.add(
            responses.GET,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/252",
            json=closed_ticket.data,
        )
        res = redo_ticket.advance()
        assert isinstance(res, Ticket)
        first_step_ticket.advance(save=False)
        assert all(t.is_done for t in first_step_ticket.current_step.tasks)

    def test_advance_closed(self, closed_group_modify_ticket):
        with pytest.raises(AssertionError):
            closed_group_modify_ticket.advance()

    def test_save_new(self, all_fields_ticket):
        all_fields_ticket.id = None
        with pytest.raises(AssertionError):
            all_fields_ticket.save()

    @responses.activate
    def test_save_unchanged(self, all_fields_ticket):
        responses.add(
            responses.GET,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/288",
            json={"ticket": {**all_fields_ticket.data["ticket"], "id": 288}},
        )
        assert isinstance(all_fields_ticket.save(), Ticket)

    @responses.activate
    def test_save_field(self, open_access_request_ticket):
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/242/steps/current/tasks/1216/fields",
        )
        responses.add(
            responses.GET,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/242",
            json={"ticket": {**open_access_request_ticket.data["ticket"], "id": 242}},
        )

        open_access_request_ticket.last_task.get_field(
            "Design comment"
        ).text = "new text"
        assert isinstance(open_access_request_ticket.save(), Ticket)

    @responses.activate
    def test_save_task(self, open_access_request_ticket):
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/242/steps/current/tasks/1216",
        )
        responses.add(
            responses.GET,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/242",
            json={"ticket": {**open_access_request_ticket.data["ticket"], "id": 242}},
        )
        open_access_request_ticket.last_task.status = Task.Status.DONE
        open_access_request_ticket.current_step.tasks.append(Task())

        assert isinstance(open_access_request_ticket.save(), Ticket)

    @responses.activate
    def test_save_task_force(self, open_access_request_ticket):
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/242/steps/current/tasks/1216",
        )
        responses.add(
            responses.GET,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/242",
            json={"ticket": {**open_access_request_ticket.data["ticket"], "id": 242}},
        )
        open_access_request_ticket.last_task.status = Task.Status.DONE

        assert isinstance(open_access_request_ticket.save(force=True), Ticket)

    @responses.activate
    def test_redo(self, closed_ticket, first_step_ticket, redo_ticket):
        counter = {"count": 0}

        def ticket_cb(c):
            def _f(request):
                c["count"] += 1
                if c["count"] < 2:
                    return (200, {}, json.dumps(redo_ticket.data))
                else:
                    return (200, {}, json.dumps(first_step_ticket.data))

            return _f

        responses.add(
            responses.PUT,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/252/steps/1246/tasks/1258/redo/1245",
        )
        responses.add_callback(
            responses.GET,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/252",
            callback=ticket_cb(counter),
        )
        res = redo_ticket.redo(0)
        assert len(res.steps) == 1

    @responses.activate
    def test_redo_failed(self, closed_ticket, first_step_ticket, redo_ticket):
        responses.add(
            responses.PUT,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/252/steps/1246/tasks/1258/redo/1245",
            status=400,
        )
        with pytest.raises(HTTPError):
            redo_ticket.redo(0)

    def test_redo_closed(self, closed_ticket):
        with pytest.raises(AssertionError):
            closed_ticket.redo(0)

    def test_redo_missing_step(self, redo_ticket):
        with pytest.raises(IndexError):
            redo_ticket.redo(10000)

    def test_redo_first_step(self, first_step_ticket):
        with pytest.raises(AssertionError):
            first_step_ticket.redo(0)

    def test_redo_no_step_id(self, redo_ticket):
        redo_ticket.steps[0].id = None
        with pytest.raises(AssertionError):
            redo_ticket.redo(0)

    def test_redo_current_step(self, redo_ticket):
        with pytest.raises(AssertionError):
            redo_ticket.redo(1)

    def test_misc_redo_errors(self, redo_ticket):
        redo_ticket.current_task.id = None
        with pytest.raises(AssertionError):
            redo_ticket.redo(0)
        redo_ticket.current_step.id = None
        with pytest.raises(AssertionError):
            redo_ticket.redo(0)
        redo_ticket.id = None
        with pytest.raises(AssertionError):
            redo_ticket.redo(0)

    def test_save_closed(self, closed_group_modify_ticket, scw):
        with pytest.raises(AssertionError):
            closed_group_modify_ticket.save()

    def test_json_override(self, all_fields_ticket):
        all_fields_ticket._json = {}
        assert all_fields_ticket._json == {}

    def test_post_json(self, all_fields_ticket):
        new_json = all_fields_ticket._json
        new_json["ticket"]["steps"]["step"] = [new_json["ticket"]["steps"]["step"][0]]
        assert all_fields_ticket.post_json == new_json

    @responses.activate
    def test_post(self, all_fields_ticket, scw):
        responses.add(
            responses.POST,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets",
            headers={
                "Location": "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/614"
            },
        )
        responses.add(
            responses.GET,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets/614",
            json={"ticket": {**all_fields_ticket.data["ticket"], "id": 614}},
        )

        t = all_fields_ticket.post()
        assert t.id == 614

    @responses.activate
    def test_bad_post(self, all_fields_ticket, scw, post_bad_ticket_json):
        responses.add(
            responses.POST,
            "https://198.18.0.1/securechangeworkflow/api/securechange/tickets",
            status=400,
            json=post_bad_ticket_json,
        )
        with pytest.raises(HTTPError):
            all_fields_ticket.post()

    @responses.activate
    def test_reject(self, all_fields_ticket, scw):
        responses.add(
            responses.PUT,
            f"https://198.18.0.1/securechangeworkflow/api/securechange/tickets/{all_fields_ticket.id}/reject",
        )
        responses.add(
            responses.GET,
            f"https://198.18.0.1/securechangeworkflow/api/securechange/tickets/{all_fields_ticket.id}",
            json=all_fields_ticket.data,
        )
        assert isinstance(all_fields_ticket.reject(), Ticket)
        all_fields_ticket.id = None
        with pytest.raises(ValueError):
            all_fields_ticket.reject()

    @responses.activate
    def test_reject_not_supported(self, all_fields_ticket, scw):
        responses.add(
            responses.PUT,
            f"https://198.18.0.1/securechangeworkflow/api/securechange/tickets/{all_fields_ticket.id}/cancel",
        )
        responses.add(
            responses.PUT,
            f"https://198.18.0.1/securechangeworkflow/api/securechange/tickets/{all_fields_ticket.id}/reject",
            json={
                "result": {
                    "code": "WEB_APPLICATION_ERROR",
                    "message": "HTTP 404 Not Found",
                }
            },
            status=400,
        )
        responses.add(
            responses.PUT,
            f"https://198.18.0.1/securechangeworkflow/api/securechange/tickets/1/reject",
            json={"result": {"code": "WEB_APPLICATION_ERROR"}},
            status=400,
        )
        responses.add(
            responses.PUT,
            f"https://198.18.0.1/securechangeworkflow/api/securechange/tickets/2/reject",
            json={"result": {"code": "WEB_APPLICATION_ERROR", "message": "scarry"}},
            status=400,
        )
        responses.add(
            responses.GET,
            f"https://198.18.0.1/securechangeworkflow/api/securechange/tickets/{all_fields_ticket.id}",
            json=all_fields_ticket.data,
        )
        with pytest.raises(HTTPError):
            all_fields_ticket.reject()
        all_fields_ticket.id = 1
        with pytest.raises(HTTPError):
            all_fields_ticket.reject()
        all_fields_ticket.id = 2
        with pytest.raises(HTTPError):
            all_fields_ticket.reject()


class TestStep(object):
    @pytest.fixture()
    def current_step(self, all_fields_ticket):
        return all_fields_ticket.current_step

    @pytest.fixture()
    def first_step(self, all_fields_ticket):
        return all_fields_ticket.get_step(0)

    @pytest.fixture()
    def all_fields_step(self, all_fields_ticket):
        return all_fields_ticket.get_step(1)

    def test_step_index(self, all_fields_ticket, all_fields_step_json):
        assert (
            all_fields_ticket.get_step(3).name
            == all_fields_ticket.get_step(-1).name
            == all_fields_step_json[-1]
        )

    def test_create_task(self):
        step = Step()

        assert len(step.tasks) == 0
        step.create_task()
        assert len(step.tasks) == 1
        assert isinstance(step.tasks[0], Task)

    def test_task(self, all_fields_step):
        assert all_fields_step.get_task(0).name is None
        assert all_fields_step.get_task(None).name is None
        assert all_fields_step.get_task("missing") is None
        assert all_fields_step.get_task(100) is None

    def test_task_field(self, all_fields_step):
        fields = all_fields_step.get_task_fields(0, TextArea)
        print(fields)

        assert len(fields) == 2
        assert isinstance(fields[0], TextArea)

        fields = all_fields_step.get_task_fields(0, MultiAccessRequest)
        assert len(fields) == 1
        assert isinstance(fields[0], MultiAccessRequest)

        fields = all_fields_step.get_task_fields(0)
        assert len(fields) == 0

    def test_done(self, current_step):
        stat = not all(t.status is Task.Status.DONE for t in current_step.tasks)
        assert stat  # all(t.status is Task.Status.DONE for t in current_step.tasks) is False
        current_step.done()
        assert all(t.status is Task.Status.DONE for t in current_step.tasks)

    def test_is_done(self, first_step):
        assert first_step.is_done


class TestTask(object):
    @pytest.fixture()
    def task(self, all_fields_ticket):
        return all_fields_ticket.get_step_task(1)

    @pytest.fixture()
    def open_task(self, all_fields_ticket):
        return all_fields_ticket.last_task

    def test_create_field(self):
        task = Task()

        assert len(task.fields) == 0
        task.create_field("TestField", TextArea)

        assert len(task.fields) == 1
        assert isinstance(task.fields[0], TextArea)
        assert task.fields[0].name == "TestField"

        task.fields = []
        task.create_field("TestField2", FieldXsiType.TEXT_FIELD)

        assert len(task.fields) == 1
        assert isinstance(task.fields[0], TextField)
        assert task.fields[0].name == "TestField2"

    def test_fields(self, task):
        assert all(
            t.xsi_type
            in (FieldXsiType.TEXT_FIELD, FieldXsiType.TEXT_AREA, FieldXsiType.CHECKBOX)
            for t in task._get_fields(TextField, TextArea, Checkbox)
        )

    def test_get_field(self, task):
        assert task.get_field("Text area")
        assert task.get_field("Text area", TextArea)
        assert isinstance(task.get_field(None, TextArea), TextArea)
        assert task.get_field("Text area", TextField) is None
        assert task.get_field("Text field", TextField, TextArea)

    def test_dirty(self, open_task):
        open_task.done()
        assert open_task._dirty

    def test_dirty_fields(self, task):
        f = task.get_field("Approve / Reject")
        f.approve()
        assert task._dirty_fields


class TestTicketIterator:
    @responses.activate
    def test_iterator(self, scw, tickets_mock):
        # looks like ticket_mock can't differenciate different params, so I changed it to a dummy url
        tickets = scw.get_tickets(TicketStatus.CLOSED)
        assert len(tickets) == 200
        assert isinstance(tickets, list)
        assert isinstance(tickets[0], Ticket)
