import streamlit as st

import pandas as pd
import numpy as np
import xlsxwriter
from io import BytesIO
import base64

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def gen_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'

    # href = f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download excel file</a> (right-click and save as `filename.xlsx`)' # decode b'abc' => abc
    href = f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download data as excel file</a> (Right-click and save as `your_file_name.xlsx`)'  # decode b'abc' => abc
    return href


# create dataframe with random integers
df = pd.DataFrame(
    np.random.randint(0, 1000, size=(50, 13)),
    columns=list("ABCDEFGHIJKLM")
)

st.subheader("Dataframe")
st.dataframe(df)

# create download link
st.subheader("Download link")
st.markdown(gen_download_link(df), unsafe_allow_html=True)