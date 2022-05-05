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

# Data summary for teams and stations
df = df_original[["Team", "Station", "Score", "Originelle_Zusatzpunkte"]].drop_duplicates().dropna()
df_color = color_df[["Gruppennamen","short","color"]].dropna().iloc[0:25]
df_color["Gruppe"] = df_color["Gruppennamen"]

# teams summary
df_team = df.groupby("Team").sum()
df_team.sort_values(by=['Score'], inplace=True, ascending=False)
df_team['Order'] = list(range(df_team.shape[0]))
df_team["Gruppe"] = df_team.index
df_team = pd.merge(df_team,df_color,on=["Gruppe"])

df_team_station = df['Team'].value_counts()
max_team = len(df['Team'].unique())
max_score= 10 * 13

#station summary
df_station = df["Station"].value_counts()  
max_station = 13


# Example to display
example_score = int(df_team[df_team["Gruppe"] == "Cevedale"]["Score"])
example_bonus_score = int(df_team[df_team["Gruppe"] == "Cevedale"]["Originelle_Zusatzpunkte"])
example_team_station = df_team_station["Cevedale"]
example_station = df_station["Station A"]
example_order = int(df_team[df_team["Gruppe"] == "Cevedale"]["Order"])
example_color = list(df_team[df_team["Gruppe"] == "Cevedale"]["color"])[0]
example_short = list(df_team[df_team["Gruppe"] == "Cevedale"]["short"])[0]
print(f"Score: {example_score}/{max_score}")
print(f"Stationen: {example_team_station}/{max_station}")
print(f"Teamsreihnfolge: {example_order}")
print(f"Teams in Stationen: {example_station}/{max_team}")
print(f"Farbe: {example_color}")
print(f"Abbkürzung: {example_short}")

print(df_team[df_team["Gruppe"] == "Cevedale"])