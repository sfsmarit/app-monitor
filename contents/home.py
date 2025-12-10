import streamlit as st
import pandas as pd

from common.utils import collect_app_info


first_columns = ["app", "url", "status"]
hidden_columns = ["test", "visible"]


st.title("Streamlit Dashboard")

check_status = st.button("Check Status")

# データの取得
with st.spinner("Loading data..."):
    data = collect_app_info(check_status)

# visible == True のみ抽出
data = [d for d in data if d.get("visible", True)]

unique_keys = []
for d in data:
    for k in d:
        if k not in unique_keys:
            unique_keys.append(k)

columns = first_columns + [col for col in unique_keys if col not in first_columns]
df = pd.DataFrame(data, columns=columns)
df = df.sort_values(by="port")

df1 = df[df["test"] == True].drop(columns=hidden_columns)
st.subheader("Released")
st.table(df1)

df2 = df[df["test"] == False].drop(columns=hidden_columns)
if len(df2):
    st.subheader("Test")
    st.table(df2)
