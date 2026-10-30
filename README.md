# 🔬 Sensor Data Validation Framework

[![Sensor Validation Tests](https://github.com/agragab/automatic-validation-framework/actions/workflows/main.yml/badge.svg)](https://github.com/agragab/automatic-validation-framework/actions/workflows/main.yml)
![Python](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Robot Framework](https://img.shields.io/badge/Robot%20Framework-000000?logo=robotframework&logoColor=white)
![Docker](https://img.shields.io/badge/docker-ready-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

Send a batch of sensor readings as JSON to a small HTTP service and get back a **plain-text validation report**: which readings have the wrong type, which are out of range, and which are empty.

The service runs in Docker, is covered by a behaviour-style **Robot Framework** test suite, and is tested automatically by **GitHub Actions** on every push and pull request.

## 📖 About

This project is a hands-on exercise in building and testing a small data-validation service end to end:

- **A validation service** with a typed HTTP API (FastAPI + Pydantic) and rule-based checks on `temperature`, `exposure` and `focus_error`.
- **Readable, behaviour-driven tests** written in Robot Framework's Given / When / Then style, including edge cases at every range boundary.
- **Automation around it**: a container image that refuses to build if the tests fail, and a CI workflow that runs the same tests remotely.

Built by [@agragab](https://github.com/agragab).

## 🧭 How it works

```mermaid
flowchart TD
    client(["<b>Client</b><br/>curl · Postman · browser"])

    subgraph docker["Docker container · python:3.12-slim · host :8000 → container :80"]
        direction TB
        api["<b>FastAPI + Pydantic</b><br/>api.py · models.py<br/><i>POST /json · GET /health</i>"]
        main["<b>Orchestrator</b><br/>main.py"]
        rules["<b>Validation rules</b><br/>validators.py<br/>type · temperature · exposure · focus error"]
        counts["<b>Counters</b><br/>utils.py<br/>total / failed checks"]
        report["<b>Report builder</b><br/>report_generator.py"]

        api --> main
        main --> rules
        main --> counts
        rules --> report
        counts --> report
    end

    out(["<b>Client receives</b><br/>text/plain · HTTP 200"])

    client == "JSON array of readings" ==> api
    report == "validation report" ==> out

    classDef edge fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#e2e8f0;
    classDef core fill:#111827,stroke:#6366f1,stroke-width:2px,color:#e5e7eb;
    classDef res fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ecfdf5;
    class client,out edge
    class api,main,rules,counts core
    class report res
    style docker fill:#0b1220,stroke:#334155,stroke-width:2px,stroke-dasharray:6 4,color:#94a3b8
    linkStyle default stroke:#94a3b8,stroke-width:2px
```

### Request lifecycle

```mermaid
sequenceDiagram
    autonumber
    actor C as Client
    participant A as api.py (FastAPI)
    participant M as main.py
    participant V as validators.py
    participant R as report_generator.py

    C->>A: POST /json (array of readings)
    A->>A: Pydantic checks the shape (every value a string)
    alt wrong shape
        A-->>C: 422 Unprocessable Entity
    else valid shape
        A->>M: main(payload)
        M->>V: type, temperature, exposure, focus error checks
        V-->>M: findings per check
        M->>R: counts + findings
        R-->>M: report text
        M-->>A: report text
        A-->>C: 200 text/plain
    end
```

## 🚀 Quick start

### With Docker

```bash
git clone https://github.com/agragab/automatic-validation-framework
cd automatic-validation-framework
docker compose up --build
```

The image build runs the test suite first, so a failing test stops the build. The service is then available on `http://localhost:8000`, and FastAPI's interactive docs are at `http://localhost:8000/docs`.

### Without Docker

Requires Python 3.12 or newer.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn api:app --reload --port 8000
```

### Send some readings

```bash
curl -X POST http://localhost:8000/json \
     -H "Content-Type: application/json" \
     -d @examples/payload.json
```

The request body is a **JSON array** of readings. `examples/payload.json` contains:

```json
[
  {"m_id": "101", "timestamp": "2026-10-09T08:00:00", "temperature": "25",  "exposure": "15", "focus_error": "3"},
  {"m_id": "102", "timestamp": "2026-10-09T08:05:00", "temperature": "19",  "exposure": "22", "focus_error": "12"},
  {"m_id": "103", "timestamp": "2026-10-09T08:10:00", "temperature": "A0a", "exposure": "",   "focus_error": "5"}
]
```

> **Every value must be a string**, including numbers (`"25"`, not `25`). A JSON number is rejected with `422` before any validation runs. A malformed string such as `"A0a"` is accepted and reported as a finding.

### Example response

```text
Report on JSON: 
--------------------------------------------------
Total tests: 30
Passed tests: 25
Failed tests: 5
--------------------------------------------------
    Incorrect Type:
    Sequence: 2
    Test: temperature
    Value: A0a
    Exception Type: ValueError

    Temperature Error:
    Sequence: 1  Reading: 19    WARNING: Temperature is too low

    Exposure Error:
    Sequence: 1  Reading: 22    WARNING: Subject is overexposed
    Sequence: 2  Reading: Null    Empty Value

    Focus Error:
    Sequence: 1  Reading: 12    WARNING: Focus Error is outside permitted range
```

(Blank lines condensed. `Sequence` is the **zero-based** position of the reading in your array.)

## 📏 Validation rules

| Field | Valid range | Reported when |
| --- | --- | --- |
| `temperature` | 20 – 50 | below 20 (too low), above 50 (too high), or empty |
| `exposure` | 10 – 20 | below 10 (underexposed), above 20 (overexposed), or empty |
| `focus_error` | 10 or below (no lower bound) | above 10, or empty |
| `m_id`, `temperature`, `exposure`, `focus_error` | integer string | the value cannot be converted to an integer (reported as `ValueError`) |

Range limits are inclusive. Empty values are reported as `Null` / `Empty Value`. A value that is not an integer is reported once under *Incorrect Type* and skipped by the range check. `timestamp` is not validated.

**Counting:** every reading counts as 10 checks, so `Total tests = 10 × number of readings`. `Failed tests` is the number of type errors plus range/empty findings.

## 🧪 Tests and CI

The suite has **16 Robot Framework test cases** written in Given / When / Then style, covering each field inside range, outside range, at the exact boundaries, empty, and with an invalid type.

```bash
pip install -r requirements.txt
robot --pythonpath . tests/
```

Robot writes `log.html`, `report.html` and `output.xml` to the current directory (all git-ignored). Open `report.html` for a readable summary.

GitHub Actions runs the same command on every push and pull request.

```mermaid
flowchart LR
    dev(["<b>Developer</b><br/>push · pull request"])

    subgraph gh["GitHub Actions · .github/workflows/main.yml"]
        direction LR
        co["Checkout"] --> py["Set up<br/>Python 3.12"] --> deps["pip install<br/>-r requirements.txt"] --> rf["robot --pythonpath .<br/>tests/"]
    end

    gate{"All tests<br/>pass?"}
    ok["✅ Check passes"]
    bad["❌ Check fails<br/>fix and push again"]

    dev ==> co
    rf --> gate
    gate -- "yes" --> ok
    gate -- "no" --> bad

    classDef edge fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#e2e8f0;
    classDef core fill:#111827,stroke:#6366f1,stroke-width:2px,color:#e5e7eb;
    classDef good fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ecfdf5;
    classDef badc fill:#450a0a,stroke:#f87171,stroke-width:2px,color:#fef2f2;
    class dev edge
    class co,py,deps,rf,gate core
    class ok good
    class bad badc
    style gh fill:#0b1220,stroke:#334155,stroke-width:2px,stroke-dasharray:6 4,color:#94a3b8
    linkStyle default stroke:#94a3b8,stroke-width:2px
```

## 🗂️ Project layout

```text
.
├── api.py                  FastAPI app: GET /health, POST /json
├── models.py               TypedDict model of one reading
├── main.py                 Orchestration: run checks, count, build report
├── validators.py           Validation rules + Robot Framework keywords
├── utils.py                Total / failed check counters
├── report_generator.py     Builds the plain-text report
├── tests/
│   └── validation.robot    Robot Framework test suite (16 cases)
├── examples/
│   ├── payload.json        Small request used in this README
│   └── sample_readings.json  Larger, deliberately messy sample (22 readings)
├── Dockerfile              Image; runs the tests during build
├── compose.yaml            Port mapping 8000 → 80
└── .github/workflows/
    └── main.yml            CI: run the Robot suite on push and PR
```

## 🛣️ Known limitations and next steps

- Range limits are hard-coded in `validators.py`; they are not configurable per request.
- Duplicate `m_id` values are not detected.
- `Total tests` is a fixed 10 checks per reading, not a count of checks actually executed.
- Dependencies in `requirements.txt` are not version-pinned.
- Planned tooling: `ruff`, `mypy`, a coverage threshold in CI, and a `pyproject.toml`.
