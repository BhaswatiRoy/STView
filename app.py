import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("ST View")

sidebarOptions = st.sidebar.selectbox(
    label = "ST Options",
    options = ['Home','PNL','Balance Sheet','Risk','Signals']
)

securityIds = pd.read_csv("isins.csv")["securityId"]
pnl = pd.read_csv("pnl.csv")
pnl_intraday = pd.read_csv("pnl_intraday.csv")
positions = pd.read_csv("positions.csv")
signals = pd.read_csv("signals.csv")
risk = pd.read_csv("risk.csv")
balancesheet = pd.read_csv("balancesheet.csv")

if sidebarOptions == 'PNL':

    st.header("PNL Report")

    # PNL BY trader LEVEL + TOTAL PNL BY trader
    pnl_by_trader = pnl.sort_values(["trader","date"])
    pnl_by_trader["cumEstPnl"] = pnl_by_trader.groupby(["trader"])["estPnl"].cumsum()

    pnl_by_trader_agg = pnl_by_trader.groupby("date")["estPnl"].sum().reset_index()
    pnl_by_trader_agg["cumEstPnlAlltraders"] = pnl_by_trader_agg["estPnl"].cumsum()

    pnl_by_trader_timeseries = px.line(pnl_by_trader, x = "date", y = "cumEstPnl", color = "trader", title = "PNL by trader")
    pnl_by_trader_timeseries.add_scatter(x = pnl_by_trader_agg["date"], y = pnl_by_trader_agg["cumEstPnlAlltraders"], mode = "lines", name = "Total Pnl - All traders")
    st.plotly_chart(pnl_by_trader_timeseries)

    # PNL BY BOOK LEVEL + TOTAL PNL BY BOOK
    pnl_by_book = pnl.sort_values(["book", "date"])
    pnl_by_book["cumEstPnl"] = pnl_by_book.groupby(["book"])["estPnl"].cumsum()

    pnl_by_book_agg = pnl_by_book.groupby("date")["estPnl"].sum().reset_index()
    pnl_by_book_agg["cumEstPnlAllBooks"] = pnl_by_book_agg["estPnl"].cumsum()

    pnl_by_book_timeseries = px.line(pnl_by_book, x = "date", y = "cumEstPnl", color = "book", title = "PNL by Book")
    pnl_by_book_timeseries.add_scatter(x = pnl_by_book_agg["date"], y = pnl_by_book_agg["cumEstPnlAllBooks"], mode = "lines", name = "Total Pnl - All Books")
    st.plotly_chart(pnl_by_book_timeseries)

    # PNL BY tradeChannel + TOTAL PNL BY Trade Channel
    pnl_by_tradeChannel = pnl.sort_values(["tradeChannel", "date"])
    pnl_by_tradeChannel["cumEstPnl"] = pnl_by_tradeChannel.groupby(["tradeChannel"])["estPnl"].cumsum()

    pnl_by_tradeChannel_agg = pnl_by_tradeChannel.groupby("date")["estPnl"].sum().reset_index()
    pnl_by_tradeChannel_agg["cumEstPnlAlltradeChannels"] = pnl_by_tradeChannel_agg["estPnl"].cumsum()

    pnl_by_tradeChannel_timeseries = px.line(pnl_by_tradeChannel, x = "date", y = "cumEstPnl", color = "tradeChannel", title = "Pnl by Trade Channel")
    pnl_by_tradeChannel_timeseries.add_scatter(x = pnl_by_tradeChannel_agg["date"], y = pnl_by_tradeChannel_agg["cumEstPnlAlltradeChannels"], mode = "lines", name = "Total Pnl - All Trade Channels")
    st.plotly_chart(pnl_by_tradeChannel_timeseries)

    # PNL BREAKDOWN BY SECURITY ID LEVEL
    securityId_selection = st.selectbox("Select a Security Id", securityIds)
    pnl_by_securityId_filtered = pnl_intraday[pnl_intraday["securityId"] == securityId_selection]
    pnl_components = ["accrued","funding","pullToPar","carry","brokerFeePnl","cashTradingPnl","cashDelta","newBiz"]
    pnl_by_securityId_timeseries = px.line(pnl_by_securityId_filtered, x = "time", y = pnl_components, title = f"Pnl Breakdown - {securityId_selection}")
    st.plotly_chart(pnl_by_securityId_timeseries)


if sidebarOptions == 'Balance Sheet':
    st.header("Balance Sheet by trader")
    balancesheet_timeseries = px.area(balancesheet, x = "date", y = "balance_sheet_mm", color = "trader")
    st.plotly_chart(balancesheet_timeseries)


if sidebarOptions == 'Risk':

    st.header("Risk Factors")

    risk_total = risk.groupby("time")[["bondRisk", "etfRisk", "totalRisk"]].sum().reset_index()
    risk_total_timeseries = px.line(risk_total, x = "time", y = ["bondRisk", "etfRisk", "totalRisk"], title = "Overall Risk")
    st.plotly_chart(risk_total_timeseries)

    securityId_selection = st.selectbox("Select a Security Id", securityIds)
    risk_filtered = risk[risk["securityId"] == securityId_selection]
    risk_by_securityId_timeseries = px.line(risk_filtered, x = "time", y =["bondRisk", "etfRisk", "totalRisk"], title = "Risk by Security Id")
    st.plotly_chart(risk_by_securityId_timeseries)

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

    st.header("Signal by Security Id")
    securityId_selection = st.selectbox("Select an Security Id", securityIds)
    signals_filtered = signals[signals["securityId"] == securityId_selection]
    signal_timeseries = px.line(signals_filtered, x="time", y= "signal_value")
    st.plotly_chart(signal_timeseries)
