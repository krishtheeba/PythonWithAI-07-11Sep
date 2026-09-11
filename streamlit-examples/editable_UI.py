import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Alice"],
    "Age": [25, 30]
})

edited_df = st.data_editor(
    df,
    use_container_width=True,
    num_rows="dynamic"
)

st.write("Updated Data")
st.write(edited_df)