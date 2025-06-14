from utils import load_data
import visualize_data as vd

def main():
    df = load_data("Social Media Analytics.xlsx")
    vd.plot_all_metrics(df)
    vd.plot_one_metric(df, "New Followers")
    
if __name__ == "__main__":
    main()
    
