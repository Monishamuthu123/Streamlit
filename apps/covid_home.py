import streamlit as st
import pandas as pd

def app():
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

    df_selection["Negative"] = pd.to_numeric(df_selection["Negative"])

    # KPI Visuals
    positive_cases = df_selection["Positive"].sum()
    negative_cases = df_selection["Negative"].sum()
    vaccinated = df_selection["Total Individuals Vaccinated"].sum()

    left_col, mid_col, right_col = st.columns(3)
    with left_col:
        st.subheader("Positive Cases:")
        st.subheader(f"{positive_cases:,}")
    with mid_col:
        st.subheader("Negative Cases:")
        st.subheader(f"{negative_cases:,}")
    with right_col:
        st.subheader("Vaccinated:")
        st.subheader(f"{vaccinated:,}")

    # positive_map = (
    #     df_selection.groupby(by=["State"]).sum()[["Positive"]]
    # )

