# 📊 ST View – Trading Analytics Dashboard

ST View is an interactive data visualization dashboard built using **Streamlit**, designed to analyze trading performance, risk metrics, and signals across multiple dimensions such as traders, books, and securities.

---

## 🚀 Features

### 📈 PNL Analytics

* Cumulative PnL tracking by:

  * Trader
  * Book
  * Trade Channel
* Aggregated total PnL across all categories
* Intraday PnL breakdown by components:

  * Accrued
  * Funding
  * Carry
  * Broker Fees
  * Cash Trading PnL
  * And more...

### 📊 Balance Sheet

* Time series visualization of balance sheet exposure by trader

### ⚠️ Risk Monitoring

* Total risk trends over time:

  * Bond Risk
  * ETF Risk
  * Aggregate Risk
* Risk breakdown by:

  * Security ID
  * Maturity
  * Asset Class
  * Issuer
  * Credit Rating

### 📡 Signals

* Time series visualization of signal values by security

---

## 🧰 Tech Stack

* **Python**
* **Streamlit** – UI framework
* **Pandas** – Data manipulation
* **Plotly** – Interactive visualizations

---

## 📁 Project Structure

```
.
├── app.py
├── pnl.csv
├── pnl_intraday.csv
├── positions.csv
├── signals.csv
├── risk.csv
├── balancesheet.csv
├── isins.csv
└── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/st-view.git
cd st-view
```

2. Install dependencies:

```bash
pip install pandas streamlit plotly
```

3. Ensure all required CSV files are in the project root directory.

---

## ▶️ Running the App

Start the Streamlit app with:

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## 🧪 Data Requirements

The app expects the following CSV files with appropriate columns:

* `pnl.csv` → trader, book, tradeChannel, date, estPnl
* `pnl_intraday.csv` → time, securityId, pnl components
* `risk.csv` → time, securityId, bondRisk, etfRisk, totalRisk, maturity, asset, issuer, rating
* `balancesheet.csv` → date, trader, balance_sheet_mm
* `signals.csv` → time, securityId, signal_value
* `securityIds.csv` → securityId

---

