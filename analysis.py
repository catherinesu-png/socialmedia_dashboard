import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import dates as mpdates 
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def add_cumulative_followers(df, starting_followers):
    df = df.copy()
    df["Cumulative Followers"] = df["New Followers"].cumsum() + starting_followers #plotting actual followers over time
    return df

def forecast_followers(df, periods = 25):

    model = ExponentialSmoothing(df["Cumulative Followers"], trend="add", seasonal=None)
    fit = model.fit()
    forecast = fit.forecast(periods)
    
    plt.figure(figsize = (12,6))
    plt.plot(df["Week"], df["Cumulative Followers"], label = "Actual")
    future_dates = pd.date_range(df["Week"].iloc[-1] + pd.Timedelta(weeks=1), periods=periods, freq="W")
    plt.plot(future_dates, forecast, label="Forecast", linestyle="--")
    plt.title("Follower Forecast")
    plt.xlabel("Week")
    plt.ylabel("Total Followers")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    return forecast

def top_growth_weeks(df, n= 5):
    df = df.copy()
    df_top_weeks = df.sort_values(by="New Followers", ascending = False).head(n)[["Week", "New Followers"]]
    df_top_weeks["Week"] = df_top_weeks["Week"].dt.strftime("%b %d, %Y")
    df_top_weeks = df_top_weeks.reset_index(drop=True)
    
    fix, ax = plt.subplots()
    ax.axis("off")
    table = pd.plotting.table(ax, df_top_weeks, loc="center", cellLoc = "center", colWidths = [.4, .4])
    plt.show()
    
#TODO : add function for engagement rate
