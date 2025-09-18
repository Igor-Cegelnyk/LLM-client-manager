# FastAPI LLM Client Manager

![Python](https://img.shields.io/badge/python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.0.116.2-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A **FastAPI** service that manages multiple LLM (Large Language Model) clients and provides a unified REST API to generate responses from various LLMs.

---

## 🚀 Features

- REST API endpoint `/generate` for LLM prompts.
- Built-in clients:
  - `mock` — returns mock responses for testing.
  - `openai` — interacts with OpenAI API.
  - `ollama` — interacts with a local Ollama API.

---

## ⚡ Getting Started

### 1️⃣ Clone the repository

```bash
    git clone https://github.com/Igor-Cegelnyk/LLM-client-manager.git
    cd llm-client-manager
```

### ▶️ Build and run docker compose

```bash
    docker compose up -d --build
```

### 📘 API Documentation

Interactive API documentation is available at:

👉 http://localhost:8000/docs



### 🔑 Open AI

- To use the OpenAI client, you must provide your personal API token in the environment variables:

```
    APP_CONFIG__OPENAI_CLIENT_CONFIG__KEY=your_openai_api_key_here
```

- To use free Ollama client, you must `Uncomment the Ollama service section in docker-compose.yml.`
Be aware: the Ollama image will take ~3.8 GB of disk space.


### 📡 API Usage
- Endpoint: /generate 
  - Method: POST
  - Request Body:

```
{
  "client": "mock",       // one of: "mock", "openai", "ollama"
  "prompt": "Hello LLM!"
}
```

- Response:

```
"Generated text..."
```


### 🧩 Extending with New Clients

- Adding a new LLM client is simple:
  - Create a new file in app/clients/ (e.g., my_custom_client.py).
  - Implement a class inheriting from BaseLLMClient.
  - Register the client in app/clients/__init__.py.
  - Add configuration in app/config/.
  - This makes it easy to integrate any additional APIs without touching existing code.