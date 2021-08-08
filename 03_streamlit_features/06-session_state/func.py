import math

import streamlit as st
import pandas as pd



class Pagination:

    def __init__(self, file_path):
        self.file_path = file_path

    @st.cache
    def load_data(self):
        # From https://www.kaggle.com/claudiodavi/superhero-set/home
        return pd.read_csv(self.file_path)

    def next_page(self):
        st.session_state.page += 1

    def prev_page(self):
        st.session_state.page -= 1

    def set_num_page(self):
        rows_per_page = st.slider("Set rows per page",
                                  min_value=5,
                                  max_value=20,
                                  value=10,
                                  step=5)
        num_page = math.ceil(len(self.df) / rows_per_page)
        return rows_per_page, num_page

    def show_data(self):
        # load data
        self.df = self.load_data()
        rows_count, num_page = self.set_num_page()


        # for placing pagination buttons
        col1, col2, col3, _ = st.columns([0.1, 0.17, 0.1, 0.63])

        if "page" not in st.session_state:
            st.session_state.page = 0

        if st.session_state.page > 0:
            col1.button("<", on_click=self.prev_page)
        else:
            col1.write("")  # this makes the empty column show up on mobile

        if st.session_state.page < (num_page-1):
            col3.button(">", on_click=self.next_page)
        else:
            col3.write("")  # this makes the empty column show up on mobile


        col2.write(f"Page {1 + st.session_state.page} of {num_page}")
        start = rows_count * st.session_state.page
        end = start + rows_count
        st.write("")
        st.table(self.df.iloc[start:end])

