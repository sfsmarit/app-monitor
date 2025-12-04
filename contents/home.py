import streamlit as st
import os
import pandas as pd

from utils import collect_app_info


if os.name == "nt":
    root_dir = r"C:\Users\marit\Documents\python"
else:
    root_dir = "/home"

first_columns = ["app", "url", "status"]
hidden_columns = ["visible"]


# ---------------------------------------------------

st.title("Streamlit Web Apps")
st.set_page_config(page_title="Streamlit Server", page_icon=":signal_strength:", layout="wide")


data = collect_app_info(root_dir)
data = [d for d in data if d.get("visible", True)]

columns = first_columns + [col for col in data[0] if col not in first_columns + hidden_columns]
df = pd.DataFrame(data, columns=columns)
df = df.sort_values(by="port")

st.table(df)
