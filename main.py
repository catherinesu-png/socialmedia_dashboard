from utils import load_data
import visualize_data as vd

def main():
    df = load_data("Instagram Analytics Sample.xlsx")
    vd.plot_all_metrics(df)
    
if __name__ == "__main__":
    main()
    
