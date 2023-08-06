# xerparser
# xer.py

from xerparser.src.errors import find_xer_errors
from xerparser.src.parser import xer_to_dict
from xerparser.schemas.account import ACCOUNT
from xerparser.schemas.calendars import CALENDAR
from xerparser.schemas.findates import FINDATES
from xerparser.schemas.memotype import MEMOTYPE
from xerparser.schemas.project import PROJECT
from xerparser.schemas.projwbs import PROJWBS
from xerparser.schemas.rsrc import RSRC
from xerparser.schemas.task import TASK, LinkToTask
from xerparser.schemas.taskfin import TASKFIN
from xerparser.schemas.taskmemo import TASKMEMO
from xerparser.schemas.taskpred import TASKPRED
from xerparser.schemas.taskrsrc import TASKRSRC
from xerparser.schemas.trsrcfin import TRSRCFIN
from xerparser.schemas.ermhdr import ERMHDR


class Xer:
    """
    A class to represent the schedule data included in a .xer file.
    """

    # class variables
    CODEC = "cp1252"

    def __init__(self, file: bytes | str) -> None:
        _xer = xer_to_dict(file)

        self.export_info = ERMHDR(*_xer["ERMHDR"])
        self.errors = find_xer_errors(_xer)
        self.accounts = {
            acct["acct_id"]: ACCOUNT(**acct) for acct in _xer.get("ACCOUNT", [])
        }
        self.calendars = {
            clndr["clndr_id"]: CALENDAR(**clndr) for clndr in _xer.get("CALENDAR", [])
        }
        self.financial_periods = {
            fin_per["fin_dates_id"]: FINDATES(**fin_per)
            for fin_per in _xer.get("FINDATES", [])
        }
        self.notebook_topics = {
            topic["memo_type_id"]: MEMOTYPE(**topic)
            for topic in _xer.get("MEMOTYPE", [])
        }
        self.projects = {
            proj["proj_id"]: PROJECT(**proj)
            for proj in _xer.get("PROJECT", [])
            if proj["export_flag"] == "Y"
        }
        self.resources = {
            rsrc["rsrc_id"]: RSRC(**rsrc) for rsrc in _xer.get("RSRC", [])
        }

        self._set_project_attrs(_xer)
        self._set_task_attrs(_xer)

    def _set_project_attrs(self, xer: dict) -> None:
        for wbs in xer.get("PROJWBS", []):
            if proj := self.projects.get(wbs["proj_id"]):
                proj.wbs.update(**self._set_wbs(**wbs))

        for task in xer.get("TASK", []):
            if proj := self.projects.get(task["proj_id"]):
                proj.tasks.update(**self._set_task(**task))

        for rel in xer.get("TASKPRED", []):
            if proj := self.projects.get(rel["proj_id"]):
                proj.relationships.update(self._set_taskpred(**rel))

        for proj in self.projects.values():
            for wbs in proj.wbs.values():
                wbs.parent = proj.wbs.get(wbs.parent_wbs_id)

    def _set_task_attrs(self, xer: dict) -> None:
        for res in xer.get("TASKRSRC", []):
            if proj := self.projects.get(res["proj_id"]):
                proj.tasks[res["task_id"]].resources.update(**self._set_taskrsrc(**res))

        for memo in xer.get("TASKMEMO", []):
            if proj := self.projects.get(memo["proj_id"]):
                proj.tasks[memo["task_id"]].memos.append(self._set_memo(**memo))

        for task_fin in xer.get("TASKFIN", []):
            if proj := self.projects.get(task_fin["proj_id"]):
                proj.tasks[task_fin["task_id"]].periods.append(
                    self._set_taskfin(**task_fin)
                )

        for rsrc_fin in xer.get("TRSRCFIN", []):
            if proj := self.projects.get(rsrc_fin["proj_id"]):
                proj.tasks[rsrc_fin["task_id"]].resources[
                    rsrc_fin["taskrsrc_id"]
                ].periods.append(self._set_taskrsrc_fin(**rsrc_fin))

    def _set_memo(self, **kwargs) -> TASKMEMO:
        topic = self.notebook_topics[kwargs["memo_type_id"]].topic
        task = self.projects[kwargs["proj_id"]].tasks[kwargs["task_id"]]
        return TASKMEMO(task=task, topic=topic, **kwargs)

    def _set_task(self, **kwargs) -> dict[str, TASK]:
        calendar = self.calendars.get(kwargs["clndr_id"])
        if calendar:
            self.projects[kwargs["proj_id"]].calendars.add(calendar)
        wbs = self.projects[kwargs["proj_id"]].wbs[kwargs["wbs_id"]]
        wbs.assignments += 1
        task = TASK(calendar=calendar, wbs=wbs, **kwargs)
        return {task.uid: task}

    def _set_taskpred(self, **kwargs) -> dict[str, TASKPRED]:
        pred = self.projects[kwargs["pred_proj_id"]].tasks[kwargs["pred_task_id"]]
        succ = self.projects[kwargs["proj_id"]].tasks[kwargs["task_id"]]
        task_pred = TASKPRED(predecessor=pred, successor=succ, **kwargs)
        pred.successors.append(LinkToTask(succ, task_pred.link, task_pred.lag))
        succ.predecessors.append(LinkToTask(pred, task_pred.link, task_pred.lag))
        return {task_pred.uid: task_pred}

    def _set_taskrsrc(self, **kwargs) -> dict[str, TASKRSRC]:
        rsrc = self.resources.get(kwargs["rsrc_id"])
        account = self.accounts.get(kwargs["acct_id"])
        task = self.projects[kwargs["proj_id"]].tasks[kwargs["task_id"]]
        taskrsrc = TASKRSRC(task=task, resource=rsrc, account=account, **kwargs)
        return {taskrsrc.uid: taskrsrc}

    def _set_taskfin(self, **kwargs) -> TASKFIN:
        period = self.financial_periods.get(kwargs["fin_dates_id"])
        return TASKFIN(period=period, **kwargs)

    def _set_taskrsrc_fin(self, **kwargs) -> TRSRCFIN:
        period = self.financial_periods.get(kwargs["fin_dates_id"])
        return TRSRCFIN(period=period, **kwargs)

    def _set_wbs(self, **kwargs) -> dict[str, PROJWBS]:
        wbs = PROJWBS(**kwargs)
        if wbs.is_proj_node and (proj := self.projects.get(wbs.proj_id)):
            proj.name = wbs.name
        return {wbs.uid: wbs}
