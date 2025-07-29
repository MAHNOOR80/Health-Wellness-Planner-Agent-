from agents import function_tool
from typing import TypedDict

class CheckinScheduleOutput(TypedDict):
    schedule: str
@function_tool
def CheckinSchedulerTool()->CheckinScheduleOutput:
    """
    Returns a weekly progress check-in schedule.
    """

    return{
        "schedule": "Progress check scheduled every Monday"
    }