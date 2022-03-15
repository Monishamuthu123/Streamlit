import streamlit as st
from multiapp import MultiApp
from apps import covid_home, covid_india, covid_vaccine, covid_testing
app = MultiApp()

st.markdown("""
# COVID Dashboard India

Here you can find the interactive COVID dashboard which contains covid cases in India, covid vaccination in India and 
covid test results in India
""")

# Add all your application here
app.add_app("covid_home", covid_home.app)
app.add_app("covid_india", covid_india.app)
app.add_app("covid_vaccine", covid_vaccine.app)
app.add_app("covid_testing", covid_testing.app)
# The main app
app.run()
