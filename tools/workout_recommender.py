from agents import function_tool
from typing import TypedDict


class WorkoutGoal(TypedDict):
    goal:str


class WorkoutPlan(TypedDict):
    workout_plan:str


@function_tool
def WorkoutRecommenderTool(goal:WorkoutGoal)->WorkoutPlan:
    """
    Recommends a 7-day workout plan based on the user's fitness goal.
    
    Example input: {"goal": "strength training"}
    """

    user_goal=goal.get("goal", "").lower()

    if "strength" in user_goal:
        plan = {
            "workout_plan": "7-day strength training program:\n"
                            "Day 1: Upper Body Strength\n"
                            "Day 2: Lower Body Strength\n"
                            "Day 3: Core & Flexibility\n"
                            "Day 4: Rest or Active Recovery\n"
                            "Day 5: Full Body Strength\n"
                            "Day 6: HIIT + Core\n"
                            "Day 7: Light Cardio & Stretching"
        }

    else:
        plan = {"workout_plan": "Currently, only strength training plans are supported."}

    return plan