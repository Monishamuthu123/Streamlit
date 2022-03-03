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
    pie_bar = st.sidebar.radio(
        "Select the status:",
        options=["Cured", "Confirmed", "Deaths"])

    if pie_bar == 'Deaths':
        pie_chart = px.pie(
            data_frame=df_selection,
            values='Deaths',
            names='State',
            color='State',
            # color_discrete_sequence=['pink', 'silver', 'steelblue'],
            hover_name='Deaths',
            # hover_data=['positive'],
            # custom_data=['total'],
            labels={"state": "the State"},
            title=pie_bar + ' cases in India',
            template='presentation',
            # width=800,
            # height=600,
            hole=0.4,
        )
        st.write(pie_chart)

    if pie_bar == 'Cured':
        pie_chart = px.pie(
            data_frame=df_selection,
            values='Cured',
            names='State',
            color='State',
            # color_discrete_sequence=['pink', 'silver', 'steelblue'],
            hover_name='Cured',
            # hover_data=['positive'],
            # custom_data=['total'],
            labels={"state": "the State"},
            title=pie_bar + ' cases in India',
            template='presentation',
            # width=800,
            # height=600,
            hole=0.4,
        )
        st.write(pie_chart)

    if pie_bar == 'Confirmed':
        pie_chart = px.pie(
            data_frame=df_selection,
            values='Confirmed',
            names='State',
            color='State',
            # color_discrete_sequence=['pink', 'silver', 'steelblue'],
            hover_name='Confirmed',
            # hover_data=['positive'],
            # custom_data=['total'],
            labels={"state": "the State"},
            title=pie_bar + ' cases in the India',
            template='presentation',
            # width=800,
            # height=600,
            hole=0.4,
        )
        st.write(pie_chart)
