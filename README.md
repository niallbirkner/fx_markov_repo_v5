# FX Markov App (v5.1)

A Streamlit app scaffold for running and iterating on a Markov-chain–based FX backtest.  
This repo currently includes:
- app/Home.py – landing page
- app/pages/1_Backtest.py – import check & placeholder UI (wire-up next)
- run_app.bat, run_backtest.bat – handy launchers
- requirements.txt, .gitignore, README.md

---

## 1) Prerequisites (Windows 11)
- Python 3.10+ (recommend 3.11) — check with: py --version
- Git (optional but recommended) — git --version
- Internet access to install Python packages

If Activate.ps1 is blocked by PowerShell policy, use this per-session:
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

---

## 2) Get the code
Using Git:
    git clone https://github.com/niallbirkner/fx_markov_repo_v5.git
    cd fx_markov_repo_v5
Or copy the folder to C:\fx_markov_repo_v5.

---

## 3) Create & activate a virtual environment
    cd C:\fx_markov_repo_v5
    py -3 -m venv .venv
    .\.venv\Scripts\Activate.ps1

Upgrade pip & install deps:
    pip install -U pip wheel
    pip install -r requirements.txt

---

## 4) First run (Streamlit)
From the repo root:
    python -m streamlit run app\Home.py --server.port 8525 --server.headless true
Open the printed Local URL (e.g., http://localhost:8525).

Note on External URL: Your ISP public IP shown by Streamlit is not exposed unless you deliberately open/forward port 8525 and allow it through your firewall.

---

## 5) Recommended config files
Create a Streamlit config to pin the port:

    .streamlit\config.toml
        [server]
        port = 8525
        headless = true

If you later add API keys (e.g., OANDA, TradingEconomics), prefer a dotenv or TOML:

    app\config\app.toml
        [oanda]
        api_key = ""
        [trading_economics]
        api_key = ""
        [collector]
        schedule_cron = "*/5 * * * *"  # every 5 minutes; adjust later

And/or .env (do not commit your real keys):
    OANDA_API_KEY=
    TE_API_KEY=

---

## 6) Using the current pages
- Home: simple landing page
- Backtest: currently validates imports from app.core.backtest
  - If you see “Imported backtest module successfully.” your package layout & PYTHONPATH are good.
  - UI wiring for parameters/results is the next task.

---

## 7) Troubleshooting
ModuleNotFoundError: No module named 'app'
- Run commands from repo root (C:\fx_markov_repo_v5)
- Ensure these exist (even empty): app\__init__.py, app\core\__init__.py
- In the same PowerShell session:
       = (Get-Location).Path

Port already in use
      netstat -ano | Select-String ":8525"
      taskkill /PID <pid> /F
Or change the port:
      python -m streamlit run app\Home.py --server.port 8600 --server.headless true

Firewall blocks from other devices
- Local access always works via http://localhost:<port>
- LAN access may require allowing app through Windows Defender Firewall

Streamlit not found
      pip install streamlit

Activation script blocked
      Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

---

## 8) Handy launchers
Double-click in Explorer or run in PowerShell:

run_app.bat
      @echo off
      setlocal
      set REPO=C:\fx_markov_repo_v5
      call "%REPO%\.venv\Scripts\activate.bat"
      set PYTHONPATH=%REPO%
      python -m streamlit run "%REPO%\app\Home.py" --server.port 8525 --server.headless true
      endlocal

run_backtest.bat
      @echo off
      setlocal
      set REPO=C:\fx_markov_repo_v5
      call "%REPO%\.venv\Scripts\activate.bat"
      set PYTHONPATH=%REPO%
      python -m streamlit run "%REPO%\app\pages\1_Backtest.py" --server.port 8525 --server.headless true
      endlocal

---

## 9) Versioning (optional)
Initialize (once):
      git init
      git add .
      git commit -m "v5.1 bootstrap"
      git branch -M main
      git remote add origin https://github.com/USERNAME/fx_markov_repo_v5.git
      git push -u origin main

---

## 10) Next planned work
- Wire Backtest page UI (symbol, date range, candle file, params)
- Compute & display stats (summary_stats) + plots
- Add Config page for OANDA / TradingEconomics & a simple scheduler
- Provide sample data and a documented CSV schema
