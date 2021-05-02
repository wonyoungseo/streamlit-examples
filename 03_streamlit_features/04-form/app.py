import streamlit as st

st.header("Usage of `st.form`")

with st.form(key='my_form'):
    topping = st.selectbox('Select Topping', ['Almonds', 'Sprinkles'], key=2)
    intensity = st.slider(label='Select Intensity', min_value=0, max_value=100, key=3)
    submitted = st.form_submit_button('Submit')


if submitted:
    st.write("Submitted")
    st.write("Topping : {}".format(topping))
    st.write("Intensity : {}".format(intensity))




st.header("Code snippet")
st.markdown("""
```python
import streamlit as st

st.header("Usage of `st.form`")

with st.form(key='your_key'):
    topping = st.selectbox('Select Topping', ['Almonds', 'Sprinkles'], key=2)
    intensity = st.slider(label='Select Intensity', min_value=0, max_value=100, key=3)
    submitted = st.form_submit_button('Submit')

if submitted:
    st.write("Submitted")
    st.write("Topping : {}".format(topping))
    st.write("Intensity : {}".format(intensity))
```
""")



