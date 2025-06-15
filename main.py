from utils import load_data
import visualize_data as vd
from analysis import add_cumulative_followers
from analysis import forecast_followers
from analysis import top_growth_weeks


def main():
    starting_followers = 27020
    df = load_data("Social Media Analytics.xlsx")
    df = add_cumulative_followers(df, starting_followers)
    
    vd.plot_all_metrics(df)
    vd.plot_one_metric(df, "New Followers")
    forecast_followers(df)
    top_growth_weeks(df)
    
    
    
if __name__ == "__main__":
    main()
    
