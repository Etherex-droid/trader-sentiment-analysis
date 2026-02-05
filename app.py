import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Trader Behavior vs Sentiment")
st.subheader("Dashboard")

st.write("""
This dashboard lets you explore:
- Performance vs Sentiment  
- Trader behavior vs Sentiment  
- Simple trader segmentation  
""")


@st.cache_data
def load_data():
    return pd.read_csv("merged_df.csv", parse_dates=["date_only"])

merged_df = load_data()

menu = st.sidebar.selectbox(
    "Choose Analysis",
    ["Performance vs Sentiment",
     "Trade Frequency vs Sentiment",
     "High vs Low Leverage Traders"]
)

if menu == "Performance vs Sentiment":

    st.header("Performance vs Sentiment")

    performance_summary = (
        merged_df
        .groupby("classification")
        .agg(
            avg_daily_pnl=("Closed PnL", "mean"),
            avg_win_rate=("win", "mean"),
            avg_drawdown=("Closed PnL", "min")
        )
        .reset_index()
    )

    st.dataframe(performance_summary)

    fig, ax = plt.subplots()
    performance_summary.set_index("classification")["avg_daily_pnl"].plot(kind="bar", ax=ax)
    ax.set_title("Average Daily PnL by Sentiment")
    ax.set_ylabel("Avg Daily PnL")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    performance_summary.set_index("classification")["avg_win_rate"].plot(kind="bar", ax=ax)
    ax.set_title("Average Win Rate by Sentiment")
    ax.set_ylabel("Avg Win Rate")
    st.pyplot(fig)

    fig, ax = plt.subplots()
    performance_summary.set_index("classification")["avg_drawdown"].plot(kind="bar", ax=ax)
    ax.set_title("Average Drawdown by Sentiment")
    ax.set_ylabel("Avg Drawdown")
    st.pyplot(fig)

elif menu == "Trade Frequency vs Sentiment":

    st.header("Trade Frequency vs Sentiment")

    trade_freq_summary = (
        merged_df
        .groupby("classification")["Trade ID"]
        .count()
        .reset_index(name="num_trades")
    )

    st.dataframe(trade_freq_summary)

    fig, ax = plt.subplots()
    trade_freq_summary.set_index("classification")["num_trades"].plot(kind="bar", ax=ax)
    ax.set_title("Average Trades per Day by Sentiment")
    ax.set_ylabel("Avg Trades per Day")
    st.pyplot(fig)


elif menu == "High vs Low Leverage Traders":

    st.header("High vs Low Leverage Traders")

    leverage_per_trader = (
        merged_df
        .groupby("Account")["Size USD"]
        .mean()
        .reset_index(name="avg_trade_size")
    )

    leverage_per_trader["leverage_segment"] = pd.qcut(
        leverage_per_trader["avg_trade_size"],
        q=2,
        labels=["Low Leverage", "High Leverage"]
    )

    pnl_per_trader = (
        merged_df
        .groupby("Account")["Closed PnL"]
        .sum()
        .reset_index(name="total_pnl")
    )

    leverage_vs_pnl = leverage_per_trader.merge(pnl_per_trader, on="Account")

    summary = (
        leverage_vs_pnl
        .groupby("leverage_segment")["total_pnl"]
        .mean()
        .reset_index()
    )

    st.dataframe(summary)

    fig, ax = plt.subplots()
    summary.set_index("leverage_segment")["total_pnl"].plot(kind="bar", ax=ax)
    ax.set_title("Average Total PnL: High vs Low Leverage Traders")
    ax.set_ylabel("Avg Total PnL")
    st.pyplot(fig)
