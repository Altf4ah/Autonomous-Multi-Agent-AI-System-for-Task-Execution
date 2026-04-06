# Autonomous Multi-Agent AI System for Task Execution

A practical MVP where multiple specialized agents collaborate to complete a high-level goal end-to-end.

## What is implemented in this repo

- **Orchestrator service** that plans and executes a 3-step workflow.
- **Three agents** (`research`, `analysis`, `writer`) with structured handoffs.
- **Context memory** and a lightweight semantic-memory stub.
- **Message bus** to capture inter-agent outputs.
- **FastAPI API** with:
  - `GET /health`
  - `POST /api/execute`
- **Tests** for orchestrator flow and API behavior.

## Architecture (MVP)

1. **Planner** creates a task plan from a user goal.
2. **Dispatcher** routes each task to a specialized agent.
3. Agents write/read shared **context memory** and **vector memory**.
4. **Evaluator** checks if output needs refinement.
5. API returns plan, task outputs, message trace, and final report.

## Project structure

```text
backend/
├── app/
│   ├── api/routes.py
│   ├── agents/
│   │   ├── base.py
│   │   ├── research_agent.py
│   │   ├── analysis_agent.py
│   │   └── writer_agent.py
│   ├── comms/message_bus.py
│   ├── memory/
│   │   ├── context_store.py
│   │   └── vector_store.py
│   ├── orchestrator/
│   │   ├── planner.py
│   │   ├── dispatcher.py
│   │   ├── evaluator.py
│   │   └── service.py
│   ├── schemas/
│   │   ├── task.py
│   │   └── message.py
│   └── main.py
├── tests/
│   ├── test_api.py
│   └── test_orchestrator.py
└── requirements.txt
```

## Quickstart

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Example request

```bash
curl -X POST http://127.0.0.1:8000/api/execute \
  -H 'Content-Type: application/json' \
  -d '{"goal":"Research top AI startups in healthcare and create a report"}'
```

## Notes

- `VectorStore` and tool integrations are intentionally stubs for MVP simplicity.
- Replace stubs with FAISS/Pinecone and real web/API tooling as next step.
