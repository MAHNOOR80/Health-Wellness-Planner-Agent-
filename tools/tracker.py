from agents import function_tool
from typing import TypedDict

class ProgressUpdate(TypedDict):
    date:str
    activity:str
    status:str

@function_tool
def ProgressTrackerTool(update:ProgressUpdate)->str:
     """
    Tracks and updates the user's progress for a specific activity.
    
    Example input:
    {
        "date": "2025-07-25",
        "activity": "Yoga",
        "status": "Completed"
    }
    """
     
     return f"✅ Progress for '{update['activity']}' on {update['date']} marked as '{update['status']}'."