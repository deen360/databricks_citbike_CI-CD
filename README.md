# databricks_citbike_CI-CD project

**A Databricks project for Citibike ETL pipelines and utilities.**  
Includes reusable Python modules, Databricks job/pipeline configs, and notebooks for bronze/silver/gold ETL layers.

> 🔧 Quick summary: Source code lives in `src/`; Databricks job/pipeline configs in `resources/`; unit tests in `tests/`.

## Overview

This repository provides a **Citibike ETL example** built around the
common Databricks **medallion architecture** (bronze → silver → gold).
Raw data is ingested to bronze, cleaned/enriched in silver, and business‑
friendly aggregates are computed in gold.  Each layer is implemented using
both notebooks and standalone Python scripts; alternate versions are provided
as DLT pipelines to illustrate two deployment approaches.  All assets are
packaged and deployed with Databricks bundles, so you can manage jobs and
pipelines consistently across environments.



---

## Features
- Citibike ETL example following the medallion architecture (bronze → silver → gold)
- Both notebooks and standalone Python scripts for each ETL layer
- Corresponding DLT pipeline variants for production-ready workflows
- Databricks bundle definitions drive deployment of jobs and pipelines
- Databricks-ready project scaffolding with job/pipeline YAMLs
- Reusable helper functions under `src/citibike` and `src/utils`
- Unit tests and fixtures for local testing (Spark/Databricks Connect)
- CI configured via `.github/workflows/ci-workflow.yml`

---

## Repository layout
- `src/` — Python package code (`citibike`, `dab_project`, `utils`)
- `resources/` — Databricks job and pipeline YAMLs and cluster definitions
- `citibike_etl/` — notebooks and scripts organised by layer (01_bronze,
  02_silver, 03_gold) plus DLT variants
- `tests/` — PyTest tests with a Spark fixture in `conftest.py`
- `scripts/` — helper scripts and runbooks

---

## Python packages & utilities

The project exposes a small set of reusable helpers that are used by the ETL
notebooks and can also be imported in external code.  The two primary
packages are:


## Testing with Spark

Unit tests are located in `tests/` and make use of a pytest fixture defined
in `tests/conftest.py`.  The fixture attempts to create a Spark session
using **Databricks Connect** (`DatabricksSession`) and falls back to a local
`pyspark.sql.SparkSession` if the former isn't available.  This allows the
same tests to run both locally and against a remote Databricks cluster.

---

## Continuous integration

A GitHub Actions workflow (`.github/workflows/ci-workflow.yml`) runs on every
push to `feature/**` branches and on pull requests against `main`.  It sets up
Python 3.11, installs the PySpark dependencies, executes the test suite and
produces a coverage report.  The status of the workflow appears in the badge at
the top of this README.



To run the tests you only need to have either `databricks-connect` or
`pyspark` installed in your development environment (see requirements
sections).  The project ships with `pytest` configuration in
`pytest.ini` and coverage support via `pytest-cov`.


---

## Requirements & setup
- Python 3.8+ recommended (Python 3.11 used in examples)

The project uses two distinct virtual environments:
1. `.venv_dbc` for Databricks Connect development, installing
   `requirements-dbc.txt`.
2. `.venv_pyspark` for local PySpark development, installing
   `requirements-pyspark.txt`.

### Environment setup (Windows example shown)
```powershell
# create/connect env for Databricks Connect
py -3.11 -m venv .venv_dbc
.\.venv_dbc\Scripts\activate
pip install -r requirements-dbc.txt
pip list
deactivate

# create/connect env for local PySpark
python -m venv .venv_pyspark
.\.venv_pyspark\Scripts\Activate.ps1
pip install -r requirements-pyspark.txt
pip list
deactivate
```
---

## Getting started

Before running or deploying this project, make sure your environment is
configured with the required Databricks workspaces, service principal
credentials, and a linked GitHub repository.  You will also need to update
`databricks.yml` with your Workspace URLs and Service Principal details.

Local Python environments for Databricks Connect and local PySpark
development must be created as described above; the requirements files
provide the necessary dependencies.


---


---

## Development & testing 
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

## Architecture

The following diagrams outline the overall project structure and pipeline flow:

![Project Architecture](architecture.jpg)

![Pipeline Flow](PIPELINE.png)

## Running locally / Databricks CLI

1. Install the Databricks CLI if it is not already available:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
   # or on macOS with sudo if needed
   sudo curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sudo sh
   ```
2. Authenticate to Databricks:
   ```bash
   databricks configure
   ```
3. Deploy bundle to `dev` (default target):
   ```bash
   databricks bundle deploy --target dev
   ```
   This creates jobs/pipelines such as `citibike_etl_pipeline_py` and
   `citibike_etl_pipeline_nb` defined in `resources/`.
4. Deploy to `prod`:
   ```bash
   databricks bundle deploy --target prod
   ```
   The default job in the template has a daily schedule; schedules are
   paused in dev mode.
5. Run a job or pipeline:
   ```bash
   databricks bundle run
   ```
6. Optionally, install developer tools such as the Databricks extension for
   Visual Studio Code: https://docs.databricks.com/dev-tools/vscode-ext.html

For more on asset bundles and CI/CD, see
https://docs.databricks.com/dev-tools/bundles/index.html.

