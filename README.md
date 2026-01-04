# dab_project

**A Databricks project for Citibike ETL pipelines and utilities.**  
Includes reusable Python modules, Databricks job/pipeline configs, and notebooks for bronze/silver/gold ETL layers.

> 🔧 Quick summary: Source code lives in `src/`; Databricks job/pipeline configs in `resources/`; unit tests in `tests/`.

### Badges
- Build: `![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci-workflow.yml/badge.svg)`
- Coverage: `![Coverage](https://img.shields.io/codecov/c/github/<OWNER>/<REPO>.svg)`

(Replace `<OWNER>/<REPO>` with the GitHub owner and repo name to enable badges.)

---

## Features
- Databricks-ready project scaffolding with job/pipeline definitions
- Notebooks + Python scripts for ETL: bronze → silver → gold
- Unit tests and fixtures for local testing
- CI configured via `.github/workflows/ci-workflow.yml`

---

## Repository layout
- `src/` — Python package code (`citibike`, `dab_project`, `utils`)
- `resources/` — Databricks job and pipeline YAMLs
- `citibike_etl/` — notebooks and pipeline notebooks
- `tests/` — unit tests and fixtures
- `scripts/` — helper scripts and runbooks

---

## Requirements & setup ⚙️
- Python 3.8+ recommended
- Optionally use a virtual environment:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate   # Windows
  ```
- Install dependencies:
  - Using uv (project recommended in original template):
    ```bash
    uv sync --dev
    ```
  - Or with pip (alternative):
    ```bash
    pip install -e .
    pip install -r requirements-pyspark.txt
    pip install -r requirements-dbc.txt
    ```

---

## Development & testing 🧪
- Run unit tests:
  ```bash
  uv run pytest
  # or
  pytest -q
  ```
- Generate coverage (example with pytest-cov):
  ```bash
  pytest --cov=src tests/
  ```

---

## Running locally / Databricks CLI
- Authenticate to Databricks:
  ```bash
  databricks configure
  ```
- Deploy bundle to `dev`:
  ```bash
  databricks bundle deploy --target dev
  ```
- Deploy to `prod`:
  ```bash
  databricks bundle deploy --target prod
  ```
- Run a job/pipeline:
  ```bash
  databricks bundle run
  ```

---

## Contributing
- Fork, create a feature branch, add tests, and open a PR.
- Follow repository style (black/flake8) and ensure CI passes.

---

## License & contact
- Add your license details here (e.g., MIT).
- Contact: add maintainer email or GitHub handle.

