import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("Covid Testing results in India")
    data = pd.concat(
        map(pd.read_csv, ["covid_19_india.csv", "covid_vaccine_statewise.csv", "StatewiseTestingDetails.csv"]),
        ignore_index=True)
    state = st.sidebar.multiselect(
        "Select the state:",
        options=data["State"].unique(),
        default="Tamil Nadu"
    )
    df_selection = data.query(
        "State == @state"
    )
    type_of_cases = st.sidebar.radio(
        "Select the type of cases:",
        options=["Positive", "Negative"]
    )

    if type_of_cases == "Positive":
        box_fig = px.box(df_selection, x="State", y=type_of_cases, points="all",
                         title=type_of_cases + " cases in India")
        st.write(box_fig)
        line_fig = px.line(df_selection, x="Date", y="Positive", title=type_of_cases + "Cases")
        st.write(line_fig)
    elif type_of_cases == "Negative":
        box_fig = px.box(df_selection, x="State", y=type_of_cases, points="all",
                         title=type_of_cases + " cases in India")
        st.write(box_fig)
        line_fig = px.line(df_selection, x="Date", y="Negative", title=type_of_cases + "Cases")
        st.write(line_fig)

