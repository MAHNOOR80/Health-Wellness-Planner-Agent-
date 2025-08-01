from connection import config
from dataclasses import dataclass
from typing import Optional, List, Dict
from pydantic import BaseModel


class User_info(BaseModel):
    name: str
    uid: int
    goal: Optional[Dict[str, str]] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[Dict[str, str]] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: Optional[List[str]] = None
    progress_logs: Optional[List[Dict[str, str]]] = None
