# FX Markov App (v5.1)

## Quickstart (Windows)

    cd C:\fx_markov_repo_v5
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -U pip wheel
    pip install -r requirements.txt
    python -m streamlit run app\Home.py --server.port 8525 --server.headless true

If imports fail, run from repo root and ensure PYTHONPATH is set to the repo path.
