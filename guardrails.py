from connection import config
from pydantic import BaseModel
from agents import (
    Agent, Runner,
    input_guardrail, output_guardrail,
    RunContextWrapper, TResponseInputItem,
    GuardrailFunctionOutput, InputGuardrailTripwireTriggered, MessageOutputItem
)
import asyncio
import re

#  1. Output type for structured goal
class GoalOutputType(BaseModel):
    goal: dict

#  2. Input guardrail function with goal parsing logic
@input_guardrail
async def goal_guardrail_function(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    pattern = r"(lose|gain)\s+(\d+)\s*(kg|pounds|lbs)\s+in\s+(\d+)\s+(days|weeks|months)"
    match = re.search(pattern, input.lower())

    if match:
        action = match.group(1)
        amount = match.group(2) + match.group(3)
        duration = match.group(4) + " " + match.group(5)

        goal_type = "weight_loss" if action == "lose" else "weight_gain"
        goal_data = {"goal": {"type": goal_type, "amount": amount, "duration": duration}}

        return GuardrailFunctionOutput(
            output_info=GoalOutputType(goal=goal_data["goal"]),
            tripwire_triggered=False
        )

    return GuardrailFunctionOutput(
        output_info=GoalOutputType(goal={}),
        tripwire_triggered=True
    )

#  3. Final Agent for Goal Validation
GoalValidationAgent = Agent(
    name="Goal Validation Agent",
    instructions="You help users set fitness goals and return structured data.",
    input_guardrails=[goal_guardrail_function],
    output_type=GoalOutputType
)

#  4. Main runner for testing
async def main():
    try:
        response = await Runner.run(GoalValidationAgent, input="I want to lose 5kg in 2 months", run_config=config)
        print("✅ Structured Goal:", response.final_output)
    except InputGuardrailTripwireTriggered:
        print("❌ Invalid goal format! Use format like: 'lose 5kg in 2 months'")

if __name__ == "__main__":
    asyncio.run(main())



# Output Guardrail Section

class MessageOutput(BaseModel):
    response: str

class HealthOutputValidation(BaseModel):
    is_safe: bool
    summary: str

output_check_agent = Agent(
    name="Output Quality Checker",
    instructions="Check if the health assistant's response is safe, non-medical, and appropriate for general wellness advice.",
    output_type=HealthOutputValidation
)

@output_guardrail
async def health_output_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    output: MessageOutput
) -> GuardrailFunctionOutput:
    output_result = await Runner.run(output_check_agent, output, run_config=config)

    return GuardrailFunctionOutput(
        output_info=output_result.final_output,
        tripwire_triggered=not output_result.final_output.is_safe
    )
