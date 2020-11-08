import dash
covid_df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
covid_df = covid_df[["iso_code",
                    "continent",
                     "location",
                     "date",
                     "total_cases",
                    "new_cases",
                    "new_cases_smoothed",
                    "total_deaths",
                    "new_deaths",
                    "new_deaths_smoothed",]]
covid_df = covid_df[covid_df["total_cases"].notna()]
covid_df['m_date'] = pd.to_datetime(covid_df["date"], format='%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m'))
covid_df1 = covid_df[covid_df["iso_code"] != "OWID_WRL"]
covid_df1 = covid_df1[covid_df1["date"].str.contains("-01")]




# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server
