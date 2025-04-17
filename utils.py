import pandas as pd

def save_to_csv(data):
    df = pd.DataFrame([data.dict()])
    df.to_csv("form_data.csv", mode="a", header=False, index=False)
