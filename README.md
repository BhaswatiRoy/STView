# 📊 ST View – Trading Analytics Dashboard

ST View is an interactive data visualization dashboard built using **Streamlit**, designed to analyze trading performance, risk metrics, and signals across multiple dimensions such as traders, books, and securities.

---

## 📸 Screenshots

### 1. PNL Dashboard

<pre>
<img width="1919" height="1070" alt="image" src="https://github.com/user-attachments/assets/db62fe53-638b-44dc-9275-c79bd55fac4b" />
<img width="1919" height="1069" alt="image" src="https://github.com/user-attachments/assets/707ab0be-a6e3-4312-851b-f3187ad11209" />
<img width="1919" height="1071" alt="image" src="https://github.com/user-attachments/assets/45978421-320f-4acb-adb1-a81fbf9a8edf" />
</pre>

---

### 2. Balance Sheet

<pre>
<img width="1919" height="1063" alt="image" src="https://github.com/user-attachments/assets/4d267d3d-e272-464a-9249-87a532f43048" />
</pre>

---

### 3. Risk Analytics

<pre>
<img width="1919" height="1070" alt="image" src="https://github.com/user-attachments/assets/6b6e9a34-f15f-4b28-947a-76abd8f23d79" />
<img width="1918" height="1060" alt="image" src="https://github.com/user-attachments/assets/5391b651-62f0-468b-8e9a-61ff8d06a85f" />
<img width="1919" height="1071" alt="image" src="https://github.com/user-attachments/assets/62f7c1a9-e888-45d5-8be3-620166a55158" />
<img width="1919" height="1069" alt="image" src="https://github.com/user-attachments/assets/e41ee922-a915-428a-964c-5f23fe227949" />
<img width="1919" height="1071" alt="image" src="https://github.com/user-attachments/assets/e32b70fe-ac99-445b-a9ac-1434a4bee96c" />
<img width="1919" height="1075" alt="image" src="https://github.com/user-attachments/assets/7d73d111-caa7-4413-8c95-8385bc9a39c0" />
</pre>

---

### 4. Signals

<pre>
<img width="1919" height="1066" alt="image" src="https://github.com/user-attachments/assets/1af49548-5593-456d-afbb-9d635d8f5f82" />
</pre>


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

