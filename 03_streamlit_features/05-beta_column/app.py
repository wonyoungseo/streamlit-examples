import streamlit as st
import numpy as np



col1, col2, col3 = st.beta_columns([0.50, 0.25, 0.25])
# the list inside the element indicates the ratio of each column



data = np.random.randn(10, 1)
col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)

col3.subheader("Empty column")
col3.markdown("")