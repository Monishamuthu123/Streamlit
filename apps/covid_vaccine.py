import streamlit as st
import pandas as pd
import plotly.express as px
import json

def app():
    st.title("Covid Vaccination report in India")
    data = pd.concat(
        map(pd.read_csv, ["covid_19_india.csv", "covid_vaccine_statewise.csv", "StatewiseTestingDetails.csv"]),
        ignore_index=True)
    state = st.sidebar.multiselect(
        "Select the state:",
        options=data["State"].unique(),
        default="Tamil Nadu"
    )
    result_bar = st.sidebar.radio(
        "Select the status:",
        options=["Covaxin", "CoviShield", "Sputnik"]
    )

    df_selection = data.query(
        "State == @state"
    )

    covaxin = (
        df_selection.groupby(by=["State"]).sum()[["Covaxin (Doses Administered)"]]
    )
    covishield = (
        df_selection.groupby(by=["State"]).sum()[["CoviShield (Doses Administered)"]]
    )
    sputnik = (
        df_selection.groupby(by=["State"]).sum()[["Sputnik V (Doses Administered)"]]
    )
    if result_bar == "Covaxin":
        fig_covid_case = px.bar(
            covaxin,
            x=covaxin.index,
            y="Covaxin (Doses Administered)",
            orientation="v",
            title="<b>Covaxin results </b>",
            # color_discrete_sequence=["#008388"] * len(covid_in_states),
            color='Covaxin (Doses Administered)',
            template="plotly_white"
        )
        st.plotly_chart(fig_covid_case)

    elif result_bar == "CoviShield":
        fig_covid_case = px.bar(
            covishield,
            x=covishield.index,
            y="CoviShield (Doses Administered)",
            orientation="v",
            title="<b>CoviShield results </b>",
            color='CoviShield (Doses Administered)',
            template="plotly_white"
        )
        st.plotly_chart(fig_covid_case)

    elif result_bar == "Sputnik":
        fig_covid_case = px.bar(
            sputnik,
            x=sputnik.index,
            y="Sputnik V (Doses Administered)",
            orientation="v",
            title="<b>CoviShield results </b>",
            color='Sputnik V (Doses Administered)',
            template="plotly_white"
        )
        st.plotly_chart(fig_covid_case)

    categories = ['18-44 Years (Doses Administered)', '45-60 Years (Doses Administered)',
                  '60+ Years (Doses Administered)', '18-44 Years(Individuals Vaccinated)',
                  '45-60 Years(Individuals Vaccinated)', '60+ Years(Individuals Vaccinated)']

    bar_category_wise = px.bar(df_selection, x='State', y=categories,  # animation_frame='State',
                               labels={'variable': 'category wise ',
                                       'value': 'count of vaccinated people category wise'},
                               barmode='group', title='Covid Vaccination category wise ')
    st.write(bar_category_wise)

    india_states = json.load(open('states_india.geojson'))
    state_id_map = {}
    for feature in india_states['features']:
        feature['id'] = feature['properties']['state_code']
        state_id_map[feature['properties']['st_nm']] = feature['id']
    print(state_id_map)
    df_selection.drop(df_selection[df_selection['State'] == "Ladakh"].index, inplace=True)
    df_selection.drop(df_selection[df_selection['State'] == "Dadra and Nagar Haveli and Daman and Diu"].index,
                      inplace=True)
    df_selection.drop(df_selection[df_selection['State'] == "Cases being reassigned to states"].index, inplace=True)
    df_selection.drop(df_selection[df_selection['State'] == "Dadra and Nagar Haveli"].index, inplace=True)
    df_selection.drop(df_selection[df_selection['State'] == "India"].index, inplace=True)
    df_selection['id'] = df_selection['State'].apply(lambda x: state_id_map[x])

    map_fig = px.choropleth(
        df_selection,
        locations="id",
        geojson=india_states,
        color="Total Doses Administered",
        hover_name="State",
        hover_data=["Total Doses Administered"],
        title="India COVID Vaccination report",
        center={"lat": 24, "lon": 78},
        animation_group="State",
    )
    map_fig.update_geos(fitbounds="locations", visible=True)
    st.write(map_fig)


