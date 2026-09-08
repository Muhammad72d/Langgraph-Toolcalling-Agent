from agents.llm import llm_with_tools 
from agents.state import state

def agent (state:state) -> dict:
    """ this is the main agent which will take the query form the user and take the decistion to use a too or automatically answer"""
    try:
        response = llm_with_tools.invoke(state["messages"])
        return {"messages":[response.content[0]["text"]]}
    except Exception as e:
        return {"messages":[("ai",f"there is an error while processing the query :{str(e)}")]}

