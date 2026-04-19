import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("ST View")

sidebarOptions = st.sidebar.selectbox(
    label = "ST Options",
    options = ['Home','PNL','Balance Sheet','Risk','Signals']
)

isins = pd.read_csv("isins.csv")["isin"]
pnl = pd.read_csv("pnl.csv")
pnl_intraday = pd.read_csv("pnl_intraday.csv")
positions = pd.read_csv("positions.csv")
signals = pd.read_csv("signals.csv")
risk = pd.read_csv("risk.csv")
balancesheet = pd.read_csv("balancesheet.csv")

if sidebarOptions == 'PNL':

    st.header("PNL Report")

    # PNL BY DESIG LEVEL + TOTAL PNL BY DESIG
    pnl_by_desig = pnl.sort_values(["desig","date"])
    pnl_by_desig["cumEstPnl"] = pnl_by_desig.groupby(["desig"])["estPnl"].cumsum()

    pnl_by_desig_agg = pnl_by_desig.groupby("date")["estPnl"].sum().reset_index()
    pnl_by_desig_agg["cumEstPnlAllDesigs"] = pnl_by_desig_agg["estPnl"].cumsum()

    pnl_by_desig_timeseries = px.line(pnl_by_desig, x = "date", y = "cumEstPnl", color = "desig", title = "PNL by Desig")
    pnl_by_desig_timeseries.add_scatter(x = pnl_by_desig_agg["date"], y = pnl_by_desig_agg["cumEstPnlAllDesigs"], mode = "lines", name = "Total Pnl - All Desigs")
    st.plotly_chart(pnl_by_desig_timeseries)

    # PNL BY BOOK LEVEL + TOTAL PNL BY BOOK
    pnl_by_book = pnl.sort_values(["book", "date"])
    pnl_by_book["cumEstPnl"] = pnl_by_book.groupby(["book"])["estPnl"].cumsum()

    pnl_by_book_agg = pnl_by_book.groupby("date")["estPnl"].sum().reset_index()
    pnl_by_book_agg["cumEstPnlAllBooks"] = pnl_by_book_agg["estPnl"].cumsum()

    pnl_by_book_timeseries = px.line(pnl_by_book, x = "date", y = "cumEstPnl", color = "book", title = "PNL by Book")
    pnl_by_book_timeseries.add_scatter(x = pnl_by_book_agg["date"], y = pnl_by_book_agg["cumEstPnlAllBooks"], mode = "lines", name = "Total Pnl - All Books")
    st.plotly_chart(pnl_by_book_timeseries)

    # PNL BY SOURCE + TOTAL PNL BY SOURCE
    pnl_by_source = pnl.sort_values(["source", "date"])
    pnl_by_source["cumEstPnl"] = pnl_by_source.groupby(["source"])["estPnl"].cumsum()

    pnl_by_source_agg = pnl_by_source.groupby("date")["estPnl"].sum().reset_index()
    pnl_by_source_agg["cumEstPnlAllSources"] = pnl_by_source_agg["estPnl"].cumsum()

    pnl_by_source_timeseries = px.line(pnl_by_source, x = "date", y = "cumEstPnl", color = "source", title = "Pnl by Source")
    pnl_by_source_timeseries.add_scatter(x = pnl_by_source_agg["date"], y = pnl_by_source_agg["cumEstPnlAllSources"], mode = "lines", name = "Total Pnl - All Sources")
    st.plotly_chart(pnl_by_source_timeseries)

    # PNL BREAKDOWN BY ISIN LEVEL
    isin_selection = st.selectbox("Select an Isin", isins)
    pnl_by_isin_filtered = pnl_intraday[pnl_intraday["isin"] == isin_selection]
    pnl_components = ["accrued","funding","pullToPar","carry","brokerFeePnl","cashTradingPnl","cashDelta","newBiz"]
    pnl_by_isin_timeseries = px.line(pnl_by_isin_filtered, x = "time", y = pnl_components, title = f"Pnl Breakdown - {isin_selection}")
    st.plotly_chart(pnl_by_isin_timeseries)


if sidebarOptions == 'Balance Sheet':
    st.header("Balance Sheet by Desig")
    balancesheet_timeseries = px.area(balancesheet, x = "date", y = "balance_sheet_mm", color = "desig")
    st.plotly_chart(balancesheet_timeseries)


if sidebarOptions == 'Risk':

    st.header("Risk Factors")

    risk_total = risk.groupby("time")[["bondRisk", "etfRisk", "totalRisk"]].sum().reset_index()
    risk_total_timeseries = px.line(risk_total, x = "time", y = ["bondRisk", "etfRisk", "totalRisk"], title = "Overall Risk")
    st.plotly_chart(risk_total_timeseries)

    isin_selection = st.selectbox("Select an Isin", isins)
    risk_filtered = risk[risk["isin"] == isin_selection]
    risk_by_isin_timeseries = px.line(risk_filtered, x = "time", y =["bondRisk", "etfRisk", "totalRisk"], title = "Risk by Isin")
    st.plotly_chart(risk_by_isin_timeseries)

    risk_aggregated_maturity = risk.groupby("maturity")["totalRisk"].sum().reset_index()
    risk_maturity_bar = go.Figure()
    risk_maturity_bar.add_trace(go.Bar(y = risk_aggregated_maturity["maturity"], x = risk["totalRisk"], name = "Total Risk by Maturity", orientation="h"))
    st.plotly_chart(risk_maturity_bar.update_layout(title="Risk by Maturity"))

    risk_aggregated_asset = risk.groupby("asset")["totalRisk"].sum().reset_index()
    risk_asset_bar = go.Figure()
    risk_asset_bar.add_trace(go.Bar(y = risk_aggregated_asset["asset"], x = risk["totalRisk"], name = "Total Risk by Maturity", orientation="h"))
    st.plotly_chart(risk_asset_bar.update_layout(title = "Risk by Asset"))
    
    risk_aggregated_issuer = risk.groupby("issuer")["totalRisk"].sum().reset_index()
    risk_issuer_bar = go.Figure()
    risk_issuer_bar.add_trace(go.Bar(y = risk_aggregated_issuer["issuer"], x = risk["totalRisk"], name = "Total Risk by Maturity", orientation="h"))
    st.plotly_chart(risk_issuer_bar.update_layout(title = "Risk by Issuer"))

    risk_aggregated_rating = risk.groupby("rating")["totalRisk"].sum().reset_index()
    risk_rating_bar = go.Figure()
    risk_rating_bar.add_trace(go.Bar(y = risk_aggregated_rating["rating"], x = risk["totalRisk"], name = "Total Risk by Maturity", orientation="h"))
    st.plotly_chart(risk_rating_bar.update_layout(title = "Risk by Rating"))


if sidebarOptions == 'Signals':

    st.header("Signal by Isin")
    isin_selection = st.selectbox("Select an Isin", isins)
    signals_filtered = signals[signals["isin"] == isin_selection]
    signal_timeseries = px.line(signals_filtered, x="time", y= "signal_value")
    st.plotly_chart(signal_timeseries)
