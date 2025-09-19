import streamlit as st

st.set_page_config(page_title="Backtest", page_icon="🧪", layout="wide")
st.title("Backtest")

ok = True
err = None
try:
    from app.core.backtest import (
        load_candles, discretize, fit_markov, generate_signals,
        simulate, CostModel, summary_stats
    )
except Exception as e:
    ok = False
    err = e

if not ok:
    st.error("Could not import backtest module: **app.core.backtest**")
    st.code(str(err))
    st.info("Run from repo root, ensure __init__.py exists, set PYTHONPATH.")
else:
    st.success("Imported backtest module successfully.")
    st.caption("Placeholder UI — we’ll wire controls next.")
