import streamlit as st

from func import Pagination

st.set_page_config(layout='wide')

if __name__ == "__main__":
    st_pagination = Pagination('data/heroes_information.csv')

    selection = st.sidebar.radio(label='select demo type',
                                 options=['pagination', 'image annotation'])

    if selection == 'pagination':
        st_pagination.show_data()
    else: # selection == 'image annotation'
        st.write("Currently Not Implemented")



