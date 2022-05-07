import gspread
import pandas as pd


# Connect to google sheet
gc = gspread.service_account(filename='forms-tour-de-schneck-7a82ceba1539.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1eHuUXIXMmwADt9B6cpSuLWSNGAWvgYTps6rU6FHEZRQ/edit?resourcekey#gid=174414602')
print("Connected to google sheet")


# Get the data
worksheet = sh.worksheet("Ergebnisse")
list_of_dicts = worksheet.get_all_records()
df_original = pd.DataFrame(list_of_dicts)

worksheet_color = sh.worksheet("Stationsübersicht")
color_list = worksheet_color.get_all_records()
color_df = pd.DataFrame(color_list)
stations_df = color_df[["Stationen","Bezeichnung"]].iloc[0:13]
stations_df["Station"] = stations_df["Stationen"]

# Data summary for teams and stations
df = df_original[["Team", "Station", "Score", "Originelle_Zusatzpunkte"]].drop_duplicates().dropna()
df_color = color_df[["Gruppennamen","short","color"]].dropna().iloc[0:25]
df_color["Gruppe"] = df_color["Gruppennamen"]
all_teams = df_color["Gruppe"]

# teams summary
df_team_tmp = df.groupby("Team").sum()
df_team_tmp.sort_values(by=['Score'], inplace=True, ascending=False)
df_team_tmp['order'] = list(range(df_team_tmp.shape[0]))
df_team_tmp["Gruppe"] = df_team_tmp.index
df_team_tmp= pd.merge(df_color,df_team_tmp,on=["Gruppe"],how="outer")
df_team_tmp['order'].fillna(100,inplace=True)
df_team_tmp.fillna(0,inplace=True)
df_team_tmp["max_score"]= 10 * 13
df_team_tmp["order"] = df_team_tmp.apply(lambda x: int(x["order"]), axis=1)
df_team_tmp["Score"] = df_team_tmp.apply(lambda x: int(x["Score"]), axis=1)
df_team_tmp["Originelle_Zusatzpunkte"] = df_team_tmp.apply(lambda x: int(x["Originelle_Zusatzpunkte"]), axis=1)
df_team_tmp["w_score"] = df_team_tmp.apply(lambda x: str(x["Score"]) + "/" + str(x["max_score"]),axis=1)


df_team_station = pd.DataFrame(df['Team'].value_counts())
df_team_station["station_max"] = 13 
df_team_station["station_done"] = df_team_station["Team"] 
df_team_station["Gruppe"] = df_team_station.index
df_team_station["w_station_done"] = df_team_station.apply(lambda x: str(x["station_done"]) + '/' + str( x["station_max"]),axis=1)

df_team = pd.merge(df_team_tmp,df_team_station,on="Gruppe",how='outer')
df_team.index = df_team["short"]


df_station = pd.DataFrame(df["Station"].value_counts())
df_station["teams_max"] = len(df['Team'].unique())
df_station["teams_done"] = df_station["Station"]
df_station["Station"] = df_station.index 
df_station = pd.merge(df_station,stations_df,on="Station", how="outer")
df_station["teams_max"].fillna(20,inplace=True)
df_station["teams_done"].fillna(0,inplace=True)
df_station["teams_max"] = df_station.apply(lambda x: int(x["teams_max"]), axis=1)
df_station["teams_done"] = df_station.apply(lambda x: int(x["teams_done"]), axis=1)
df_station["w_teams_done"] = df_station.apply(lambda x: str(x["teams_done"]) + '/' + str(x["teams_max"]),axis=1)

df_station["station"] = df_station.apply(lambda x: str(x["Station"])[-1],axis=1)
df_station.index = df_station["station"]
print(df_station)


# Example to display
print("Score {}".format(df_team.loc["CE","w_score"]))
print("Stationen: {}".format(df_team.loc["CE","w_station_done"]))
print("Teamsreihnfolge: {}".format(df_team.loc["CE","order"]))
print("Teams in Stationen: {}".format(df_station.loc["A","w_teams_done"]))
print("Farbe: {}".format(df_team.loc["CE","color"]))
print("Abbkürzung: {}".format(df_team.loc["CE","short"]))


# Visualization
