from utils import load_data
import visualize_data as vd
from analysis import add_cumulative_followers
from analysis import forecast_followers
from analysis import top_growth_weeks


def main():
    starting_followers = 1008
    known_growth = {("2023-07-01", "2023-09-01"): (430, 516), ("2024-07-01", "2024-09-01"): (988, 1161) }
    
    df = load_data("Instagram Analytics Sample.xlsx")
    df = add_cumulative_followers(df, starting_followers)
    
    vd.plot_all_metrics(df)
    vd.plot_one_metric(df, "New Followers")

    forecast_followers(df, known_growth, periods = 15)
    top_growth_weeks(df)
    
    
    
if __name__ == "__main__":
    main()
    
