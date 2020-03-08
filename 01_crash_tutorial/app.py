import streamlit as st

# Text/Title
st.title("Streamlit Tutorials")


# Header / Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.text("Hello Streamlit")

# Markdown syntax
st.markdown("# This is a Markdown title")
st.markdown("## This is a Markdown header")
st.markdown("### This is a Markdown subheader")


# Error/Colorful Text
st.success("Successful")
st.info("Information!")
st.warning("This is a warning")
st.error("This is an error!")
st.exception("NameError('name three not defined')")


# Get help info about python (ex)
st.help(range)



# Writing text / Super function
st.write("Text with write")
st.write(range(10))


# Images
from PIL import Image