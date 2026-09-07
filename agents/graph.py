from langgraph.graph import StateGraph , START,END
from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.checkpoint.memory import MemorySaver
from agents.state import state
from agents.agent import agent
from agents.llm import llm_with_tools , tools


graph=StateGraph(state)

graph.add_node("agent",agent)
graph.add_node("tool_agent",ToolNode(tools))

graph.add_edge(START,"agent")
graph.add_conditional_edges("agent",tools_condition,{'tools':"tool_agent","__end__":END})
graph.add_edge("tool_agent","agent")

app=graph.compile(checkpointer=MemorySaver())