import pandas as pd

def load_data(filepath):
    df = pd.read_excel(filepath, sheet_name = "Weekly Dashboard")
    df["Week"] = pd.to_datetime(df["Week"])
    df.sort_values("Week", inplace = True) # seems like file is sorted but might as well check
    return df
