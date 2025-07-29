from agents import Agent
from tools.meal_planner import meal_planner

NutritionExpertAgent =Agent(
    name="NutritionExpertAgent ",
    instructions="You handle complex dietary needs.",
    tools=[meal_planner]
)
