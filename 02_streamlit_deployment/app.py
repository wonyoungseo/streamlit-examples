import streamlit as st
import pandas as pd
from functools import reduce
import plotly_express as px

df_confirmed = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_deaths = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
df_recovered = pd.read_csv(
    'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
id_list = df_confirmed.columns.to_list()[:4]
vars_list = df_confirmed.columns.to_list()[4:]
confirmed_tidy = pd.melt(df_confirmed, id_vars=id_list, \
                         value_vars=vars_list, var_name='Date', value_name='Confirmed')
deaths_tidy = pd.melt(df_deaths, id_vars=id_list, \
                      value_vars=vars_list, var_name='Date', value_name='Deaths')
recovered_tidy = pd.melt(df_recovered, id_vars=id_list, \
                         value_vars=vars_list, var_name='Date', value_name='recovered')
confirmed_tidy.head()

id_list = df_confirmed.columns.to_list()[:4]
vars_list = df_confirmed.columns.to_list()[4:]
confirmed_tidy = pd.melt(df_confirmed, id_vars=id_list, value_vars=vars_list, var_name='Date', value_name='Confirmed')
deaths_tidy = pd.melt(df_deaths, id_vars=id_list, value_vars=vars_list, var_name='Date', value_name='Deaths')
recovered_tidy = pd.melt(df_recovered, id_vars=id_list, value_vars=vars_list, var_name='Date', value_name='recovered')

data_frames = [confirmed_tidy, deaths_tidy, recovered_tidy]
df_corona = reduce(lambda left, right: pd.merge(left, right, on=id_list + ['Date'], how='outer'), data_frames)

id_vars = df_corona.columns[:5]
data_type = ['Confirmed', 'Deaths', 'recovered']
df_corona = pd.melt(df_corona, id_vars=id_vars, value_vars=data_type, var_name='type', value_name='Count')
df_corona['Date'] = pd.to_datetime(df_corona['Date'], format='%m/%d/%y', errors='raise')

tsmap_corona = df_corona[df_corona['type'] == 'Confirmed']
tsmap_corona['Date'] = tsmap_corona['Date'].astype(str)
to_Category = pd.cut(tsmap_corona['Count'], [-1, 0, 105, 361, 760, 1350, 6280, 200000],
                     labels=[0, 1, 8, 25, 40, 60, 100])
tsmap_corona = tsmap_corona.assign(size=to_Category)
tsmap_corona = tsmap_corona[~pd.isnull(tsmap_corona['size'])].reset_index(drop=True)


def write_main_page():
    st.title('COVID-19 시각화 툴 (샘플)')
    st.write("""
이 웹 어플리케이션은 **Streamlit**을 활용하여 간단한 시각화 툴을 만들고 웹 어플리케이션을 배포하는 과정을 안내하기 위한 샘플로 만들어졌습니다.
**Johns Hopkins CSSE**의 Github에 제공된 **COVID-19 데이터([링크](https://github.com/CSSEGISandData/COVID-19))**를 사용하였습니다.

웹 어플리케이션에서는 다음과 같은 기능이 있습니다.

- Raw Data
    - 테이블 형태의 데이터셋을 확인할 수 있습니다.
- Map: Confirmed
    - 1월 22일부터 현재까지 전세계의 확진자 현황을 지도로 확인할 수 있습니다.

## Reference
- [Johns Hopkins CSSE Github Repository](https://github.com/CSSEGISandData/COVID-19)
- [_Mapping the Spread of Coronavirus COVID-19 with python and Plotly_ by. Babak Fard](https://medium.com/analytics-vidhya/mapping-the-spread-of-coronavirus-covid-19-d7830c4282e)

"""
             )


def plot_confirmed(tsmap_corona):
    fig = px.scatter_geo(data_frame=tsmap_corona,
                         lat='Lat', lon='Long',
                         hover_name='Country/Region',
                         hover_data=['Province/State', 'Count'],
                         size='size',
                         animation_frame='Date',
                         size_max=40,
                         width=700, )
    return fig


def create_layout():
    st.sidebar.title("Menu")
    page = st.sidebar.selectbox("Please select a page",
                                ["Main",
                                 "Raw Data",
                                 "Confirmed Map", ])
    if page == 'Main':
        write_main_page()
    elif page == 'Raw Data':
        st.title('COVID19 Raw Data')
        st.dataframe(df_corona)
    elif page == 'Confirmed Map':
        st.title('Confirmed Map')
        fig = plot_confirmed(tsmap_corona)
        st.plotly_chart(fig)


def main():
    create_layout()


if __name__ == "__main__":
    main()