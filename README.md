# Trader Behavior vs Market Sentiment

## What this project is about 
This project analyzes how market sentiment (Fear/Greed Index) relates to trader behavior and performance. The main goals were to:

- Understand how trader performance differs in Fear vs Greed markets
- See whether traders actually change their behavior when sentiment changes
- Identify what kind of traders tend to perform better

---

## What is inside this repo

trader-sentiment-analysis/
│
├── analysis.ipynb # Main analysis notebook (everything is here)
│
├── data/
│ ├── fear_greed_index.csv
│ └── historical_data.csv
│
├── outputs/
│ └── charts/ # Key plots from the analysis
│
└── app.py # (Optional) Streamlit dashboard

---

## How to run this project

### 1) Install dependencies

Run this in your terminal:

``` bash
pip install pandas numpy matplotlib scikit-learn streamlit
```

### 2) Run the notebook (recommended)

Open Jupyter Notebook:

``` bash
jupyter notebook
```
Then: - Open `analysis.ipynb` - Run all cells from top to bottom.

### 3) Run the Streamlit app (optional)

``` bash
streamlit run app.py
```

Then open the local link shown in your terminal (usually
`http://localhost:8501`).

---

##  Short Write-up (Methodology, Insights, Recommendations)

###  Part A — Data Preparation (What I did)

- Loaded both datasets:
  - Fear/Greed Index  
  - Hyperliquid historical trading data  
- Documented dataset size (number of rows and columns)  
- Checked and handled missing values and duplicate records  
- Converted timestamps to proper datetime format and aligned both datasets at a **daily level**  
- Created key metrics used throughout the analysis:
  - **Daily PnL per trader (per account)**
  - **Win rate**
  - **Average trade size** (used as a leverage proxy)
  - **Leverage distribution** (based on trade size buckets)
  - **Number of trades per day**
  - **Long/Short ratio**

---

###  Part B — Analysis (What I analyzed)

#### 1) Performance vs Sentiment  
I compared performance across Fear vs Greed days using:
- Total PnL  
- Win rate  
- Drawdown proxy (worst trade of the day)  

#### 2) Trader behavior vs Sentiment  
I examined whether traders changed behavior based on sentiment by analyzing:
- Trade frequency (number of trades per day)  
- Leverage / position size (average trade size)  
- Long/Short bias (daily long/short ratio)

#### 3) Trader Segmentation  
I identified three trader segments:
- **High vs Low leverage traders**
- **Frequent vs Infrequent traders**
- **Consistent vs Inconsistent traders (based on win rate)**  

Each segment was compared using total PnL and visualized with bar charts.

#### 4) Three key insights (supported by charts/tables)
1. Fear days tend to have higher average PnL but worse drawdowns, indicating higher risk.  
2. Traders trade more in Extreme Fear, but take larger positions and show more bullish bias in Greed.  
3. High-leverage traders earn higher total PnL on average, but take more risk than low-leverage traders.

---

###  Part C — Actionable Rules (Strategy Recommendations)

**Rule 1 — Risk control in Extreme Fear**  
During Extreme Fear days, high-leverage traders should cap position sizes and avoid excessive trading due to large drawdowns and very high trading activity.

**Rule 2 — Take more Long trades in Greed / Neutral but stay cautious**  
During Greed and Neutral days, frequent traders can favor Long positions and take slightly larger trade sizes, since these periods show higher win rates and lower downside risk.

---

###  Bonus Work (Optional)

#### Simple Predictive Model  
Built a Logistic Regression model to predict whether **next-day total PnL** would fall into **Low, Medium, or High** buckets using:
- Sentiment  
- Number of trades  
- Average trade size  
- Long/Short ratio  

The model achieved ~60% accuracy, which is better than random guessing (~33%).

#### Clustering Traders  
Used **K-Means clustering** to group traders into behavioral archetypes based on:
- Average trade size  
- Total number of trades  
- Win rate  
- Total PnL  

This helped identify different trader profiles (e.g., high-risk/high-reward vs steady traders).

#### Streamlit Dashboard  
A lightweight Streamlit dashboard was built to explore key metrics and visualizations interactively.
---
