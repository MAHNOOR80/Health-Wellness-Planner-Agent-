from dataclasses import dataclass
from agents import Agent,RunHooks,RunContextWrapper,AgentHooks,Tool,FunctionTool


# run hooks
@dataclass
class Custom_hooks(RunHooks):
    async def on_agent_start(self,ctx:RunContextWrapper,agent:Agent):
        print(f"🚀 Agent '{agent.name}' has started.")
    
    async def on_agent_end(self,ctx:RunContextWrapper,agent:Agent,output):
        print(f"✅ Agent '{agent.name}' has ended.")

        
    
my_hooks=Custom_hooks()


# agent hooks
@dataclass
class Custom_agent_hooks(AgentHooks):
    async def on_start(self,ctx:RunContextWrapper,agent:Agent):
        print(f"🤖 '{agent.name}' is thinking ..")
    
    async def on_handoff(self,ctx:RunContextWrapper,agent:Agent,source):
        print(f"🤝 Handoff from agent '{source.name}' to agent '{agent.name}'")
    
    async def on_tool_start(self, ctx:RunContextWrapper, agent:Agent, tool:FunctionTool):
        print(f"🛠️ Tool '{tool.name}' is starting....")



my_agent_hooks=Custom_agent_hooks()



