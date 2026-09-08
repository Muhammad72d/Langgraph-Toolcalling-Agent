# 🤖 LangGraph Tool-Calling Agent

> An AI agent built with LangGraph that autonomously decides when to use
> external tools to answer user queries.

## 🚀 Live Demo

👉 [Try the Agent Live](YOUR_LIVE_LINK)

## 🎥 Demo

[Add demo GIF / screenshot here]

## ✨ Features

- 🧠 LLM-powered autonomous agent
- 🔧 Tool calling
- 🌤️ Real-time weather information
- 🔎 Web search
- 🧮 Calculator
- 🔄 Multi-step agent/tool execution loop
- 🕸️ LangGraph stateful workflow
- 🎯 Conditional tool routing
- 💬 Streamlit chat interface
- 🐳 Dockerized
- ☁️ Cloud deployed

## 🏗️ Architecture

START
  ↓
Agent
  ↓
tools_condition
  ├── ToolNode
  │     ├── 🔎 Search
  │     ├── 🌤️ Weather
  │     └── 🧮 Calculator
  │
  └── END
        ↑
        └── Agent

## 🛠️ Tech Stack

- Python
- LangGraph
- LangChain
- Gemini
- Streamlit
- Docker
- Open-Meteo
- DuckDuckGo Search

## 📂 Project Structure

```text
Langgraph-Toolcalling-Agent/
│
├── agents/
│   ├── agent.py
│   ├── graph.py
│   ├── llm.py
│   ├── state.py
│   └── tools.py
│
├── GUI.py
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md
