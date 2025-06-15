import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import dates as mpdates 
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from prophet import Prophet

def add_cumulative_followers(df, starting_followers):
    df = df.copy()
    df["Cumulative Followers"] = df["New Followers"].cumsum() + starting_followers #plotting actual followers over time
    return df

def top_growth_weeks(df, n= 5):
    df = df.copy()
    df_top_weeks = df.sort_values(by="New Followers", ascending = False).head(n)[["Week", "New Followers"]]
    df_top_weeks["Week"] = df_top_weeks["Week"].dt.strftime("%b %d, %Y")
    df_top_weeks = df_top_weeks.reset_index(drop=True)
    
    fix, ax = plt.subplots()
    ax.axis("off")
    table = pd.plotting.table(ax, df_top_weeks, loc="center", cellLoc = "center", colWidths = [.4, .4])
    plt.show()


def forecast_followers(df, known_growth = None, periods = 15):
    df_prophet = df[["Week", "Cumulative Followers"]].rename(columns={"Week": "ds", "Cumulative Followers": "y"})

    for date_range, (start_val, end_val) in known_growth.items(): 
        start_date = pd.to_datetime(date_range[0])
        end_date = pd.to_datetime(date_range[1])
        
        approx_data = pd.DataFrame({"ds": [start_date, end_date], "y": [start_val, end_val]})
        
        df_prophet = pd.concat([df_prophet, approx_data], ignore_index = True).sort_values("ds")

    model = Prophet(changepoint_prior_scale=0.5)
    model.fit(df_prophet)
    
    future = model.make_future_dataframe(periods, freq = "W")
    forecast = model.predict(future)
    
    fig = model.plot(forecast)
    min_date = df["Week"].min()
    max_date = forecast["ds"].max()
    
    fig.gca().set_xlim([min_date, max_date])
    plt.tight_layout()
    plt.grid(True)
    plt.show()
    
#TODO : add function for engagement rate