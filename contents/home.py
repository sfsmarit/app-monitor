import streamlit as st
import pandas as pd

import config
from common.utils import collect_app_info


first_columns = ["app", "url", "status"]
hidden_columns = ["visible"]


st.title("Streamlit Dashboard")

check_status = st.button("Check Status")

# データの取得
with st.spinner("Loading data..."):
    data = collect_app_info(check_status)

# visible == True のみ抽出
data = [d for d in data if d.get("visible", True)]

columns = first_columns + [col for col in data[0] if col not in first_columns + hidden_columns]
df = pd.DataFrame(data, columns=columns)
df = df.sort_values(by="port")

st.table(df)
