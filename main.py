from agents.graph import app

config={"configurable": {"thread_id": "1"}}

while True:
    user_input = input("you: ")
    if user_input.lower() in[ "exit","quit"]:
        break
    response = app.invoke({"messages":[("human",user_input)]},config)
    print( response["messages"][-1].content)

