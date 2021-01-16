import streamlit as st
import re
import os
from pathlib import Path
import pandas as pd

FILE_SAVE_PATH = "data/"



st.subheader("File uploader")

# restrict uploaded file to excel
uploaded_file = st.file_uploader("Choose a file", type="xlsx")



if uploaded_file is not None:

    # accept only allowed file name, otherwise reject
    filename_pattern = r"^Daily-result-\d{8}-upload\.xlsx$"
    if re.search(filename_pattern, uploaded_file.name) is None:
        st.error("File name format incorrect.")
        st.warning("Make sure your file name format is Daily-result-YYYYMMDD-upload.xlsx")

    else:
        # read file to save
        df = pd.read_excel(uploaded_file)

        # preview uploaded file
        st.dataframe(df)


        st.markdown("\n")
        st.markdown("**Click button to save file**")
        if st.button("Save file"):
            with st.spinner("Uploading..."):

                try:
                    os.mkdir(FILE_SAVE_PATH)
                    df.to_excel(FILE_SAVE_PATH + uploaded_file.name, index=False)
                except FileExistsError:
                    df.to_excel(FILE_SAVE_PATH + uploaded_file.name, index=False)

                st.success("File successfully uploaded!")