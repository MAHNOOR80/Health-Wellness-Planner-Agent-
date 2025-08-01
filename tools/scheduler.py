from agents import function_tool, RunContextWrapper
from typing import TypedDict, Literal
from context import User_info
from pydantic import BaseModel


class CheckinInput(BaseModel):
    day_of_week: Literal[
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    time_of_day: str  # e.g. "9am", "18:00", etc.


class CheckinScheduleOutput(TypedDict):
    schedule: str


@function_tool
def CheckinSchedulerTool(
    ctx: RunContextWrapper[User_info],
    input: CheckinInput
) -> CheckinScheduleOutput:
    """Schedule a user check-in time by saving the day and time to the session context.

    Args:
        ctx: Contains the current user session context.
        input: A structured input with the day of the week and time of day.

    Returns:
        CheckinScheduleOutput: A confirmation message indicating the scheduled check-in.

    Side Effects:
        Updates `progress_logs` in the user context with the provided time and day.
    """

    if ctx.context.progress_logs is None:
        ctx.context.progress_logs = []

    ctx.context.progress_logs.append({
        "day": input.day_of_week,
        "time": input.time_of_day
    })

    return CheckinScheduleOutput(
        schedule=f"Check-in scheduled for {input.day_of_week} at {input.time_of_day}."
    )
