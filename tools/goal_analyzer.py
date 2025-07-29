from agents import function_tool
import re

@function_tool
def GoalAnalyzerTool(user_input: str) -> dict:
    pattern = r"(lose|gain)\s+(\d+)\s*(kg|pounds|lbs)\s+in\s+(\d+)\s+(days|weeks|months)"
    match = re.search(pattern, user_input, re.IGNORECASE)

    if not match:
        return {"is_valid_goal": False, "reason": "Invalid format. Use: 'lose 5kg in 2 months'"}

    action, amount, unit, duration_value, duration_unit = match.groups()

    goal_type = "weight_loss" if action.lower() == "lose" else "weight_gain"

    return {
        "is_valid_goal": True,
        "goal": {
            "type": goal_type,
            "amount": f"{amount}{unit}",
            "duration": f"{duration_value} {duration_unit}"
        }
    }
