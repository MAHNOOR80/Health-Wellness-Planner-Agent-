from agents import Agent
from tools.goal_analyzer import GoalAnalyzerTool

escalation_agent=Agent(
    name="escalation agent",
    instructions="You are a human coach.Handle escalations, complaints, or user issues needing special attention.",
    tools=[GoalAnalyzerTool]

)