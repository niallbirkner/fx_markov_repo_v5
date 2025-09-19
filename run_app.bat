@echo off
setlocal
set REPO=C:\fx_markov_repo_v5
call "%REPO%\.venv\Scripts\activate.bat"
set PYTHONPATH=%REPO%
python -m streamlit run "%REPO%\app\Home.py" --server.port 8525 --server.headless true
endlocal
