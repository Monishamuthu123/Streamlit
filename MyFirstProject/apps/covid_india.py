import streamlit as st
import plotly.express as px
import pandas as pd

def app():
    st.title("Covid cases in India")
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
    st.sidebar.header("View the results of Covid cases!")
    covid_bar = st.sidebar.radio(
        "Select the status:",
        options=["Cured", "Confirmed", "Deaths"])

    if covid_bar == 'Deaths':
        bar_graph = px.bar(df_selection, x="Deaths", y="State", color="Deaths",
                     hover_data=['Deaths'], barmode='stack', title=covid_bar + ' cases in India')
        st.write(bar_graph)

    if covid_bar == 'Cured':
        bar_graph = px.bar(df_selection, x="Cured", y="State", color="Cured",
                           hover_data=['Cured'], barmode='stack', title=covid_bar + ' cases in India')
        st.write(bar_graph)

    if covid_bar == 'Confirmed':
        bar_graph = px.bar(df_selection, x="Confirmed", y="State", color="Confirmed",
                           hover_data=['Confirmed'], barmode='stack', title=covid_bar + ' cases in India')
        st.write(bar_graph)
        