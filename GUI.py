import streamlit as st
from agents.graph import app
from agents.functions import extract_text

st.set_page_config(
    page_title="LangGraph Agent",
      page_icon="🤖"
      )

st.title(" LangGraph tool-calling Agent")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input(" Ask me ...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role":"user",
                                      "content":user_input})
    
    with st.chat_message("assistant"):
        response = app.invoke({"messages":[("human",user_input)]},
                              config={"configurable": {"thread_id": "streamlit_user"}})
        
        assistant_response = extract_text(response["messages"][-1].content)
        st.markdown(assistant_response)

        st.session_state.messages.append({"role":"assistant",
                                          "content":assistant_response})
        