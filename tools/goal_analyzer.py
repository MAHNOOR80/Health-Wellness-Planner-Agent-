from agents import function_tool, RunContextWrapper
import re
from context import User_info

@function_tool
def GoalAnalyzerTool(ctx: RunContextWrapper[User_info], user_input: str) -> dict:
    pattern = r"(lose|gain)\s+(\d+)\s*(kg|pounds|lbs)\s+in\s+(\d+)\s+(days|weeks|months)"
    match = re.search(pattern, user_input, re.IGNORECASE)

    if not match:
        return {"is_valid_goal": False, "reason": "Invalid format. Use: 'lose 5kg in 2 months'"}

    action, amount, unit, duration_value, duration_unit = match.groups()

    goal_type = "weight_loss" if action.lower() == "lose" else "weight_gain"

    structured_goal = {
        "type": goal_type,
        "amount": f"{amount}{unit}",
        "duration": f"{duration_value} {duration_unit}",
        "original_input": user_input.strip()
    }

    ctx.context.goal = structured_goal

    return {
        "is_valid_goal": True,
        "goal": structured_goal
    }
