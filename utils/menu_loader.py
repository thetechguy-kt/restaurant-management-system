import pandas as pd
import os

MENU_FILE = "data/menu.xlsx"

def load_menu():
    if not os.path.exists(MENU_FILE):
        return []
    df = pd.read_excel(MENU_FILE)
    return df.to_dict(orient="records")
