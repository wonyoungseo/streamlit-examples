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


# Show images
from PIL import Image
img = Image.open("sources/example.jpeg")
st.image(img, width=300, caption="Image example: Cat")


# # Show videos
# vid_file = open("example.mp4", "rb").read()
# st.video(vid_file)


# # Audio
# aud_file = open("example_music.mp3", "rb").read()
# st.audio(audio_file, format='audio/mp3')


### Widget
# Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# Radio button
status = st.radio("What is your status?", ("Active", "Inactive"))
if status == "Active":
    st.success("You're now Active!")
else:
    st.warning("Inactive")


# Select Box (ex)
occupation = st.selectbox("Your Occuapation",
                          ["Backend Developer",
                           "Frontend Developer",
                           "Data Engineer",
                           "Database Administrator",
                           "Data Analyst",
                           "Security Engineer"])
st.write("You selected your occupation as ", occupation)


# MultiSelect
location = st.multiselect("Where do you work?",
                          ("Seoul", "London", "New York", "Paris", "Berlin", "Other City"))
st.write("You selected ", len(location), " locations")


# Slider
level = st.slider("What is your level?", 1, 5)


# Buttons
st.button("Simple Button")

if st.button("About"):
    st.text("This is streamlit tutorial")

# Text Input
first_name = st.text_input("Enter Your First Name", "Type Here ...")
if st.button("Submit", key='first_name'):
    result = first_name.title()
    st.success(result)


# Text Area
message = st.text_area("Enter Your message", "Type Here ...")
if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)


# Date Input
import datetime
today = st.date_input("Today is ", datetime.datetime.now())


# Time
the_time = st.time_input("The time is ", datetime.time())


# Displaying JSON
st.text("Display JSON")
st.json({'name':'Jesse', 'gender':'male'})


# Display Raw Code - one line
st.text("Display Raw Code")
st.code("import numpy as np")

# Display Raw Code - snippet
with st.echo():
    # This will also show  as a comment
    import pandas as pd
    df = pd.DataFrame()


# Progress Bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+1)


# # Spinner
# with st.spinner("Waiting ..."):
#     time.sleep(5)
# st.success("Finished!")


# # Ballons
# st.balloons()


# Sidebars
st.sidebar.header("About")
st.sidebar.text("This is sidebar")



# Functions
@st.cache
def run_function():
    return [i for i in range(0, 100, 5)]

st.text("Run python function")
st.write(run_function())


# Table and plotting
import pandas as pd
from sklearn.datasets import load_iris
data = load_iris()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['target'] = data['target']

# DataFrames
st.text("Displaying dataframe")
st.dataframe(df)

# Tables
st.text("Displaying table")
st.table(df)

# Plot
st.text("Plotting with matplotlib")
df['sepal length (cm)'].hist()
st.pyplot()