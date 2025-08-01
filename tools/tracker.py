from agents import function_tool, RunContextWrapper
from typing import TypedDict
from context import User_info

class ProgressUpdate(TypedDict):
    date: str
    activity: str
    status: str

@function_tool
def ProgressTrackerTool(ctx: RunContextWrapper[User_info], update: ProgressUpdate) -> str:
    """
    Tracks and updates the user's progress for a specific activity.
    
    Example input:
    {
        "date": "2025-07-25",
        "activity": "Yoga",
        "status": "Completed"
    }
    """
    print("🛠️ ProgressTrackerTool was called with:", update) 

    # Ensure the progress_logs list exists
    if ctx.context.progress_logs is None:
        ctx.context.progress_logs = []

    # Add the progress update
    ctx.context.progress_logs.append({
        "date": update["date"],
        "activity": update["activity"],
        "status": update["status"]
    })

    print(f"🔄 Updating progress: ✅ {update['activity']} on 📅 {update['date']} as '{update['status']}'")



    return f"✅ Progress for '{update['activity']}' on {update['date']} marked as '{update['status']}'."
