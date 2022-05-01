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


# Data summary for teams and stations
df = df_original[["Team", "Station", "Score", "Originelle_Zusatzpunkte"]].drop_duplicates().dropna()

# teams summary
df_team = df.groupby("Team").sum()  
df_team.sort_values(by=['Score'], inplace=True, ascending=False)
df_team['Order'] = list(range(df_team.shape[0]))
df_team_station = df['Team'].value_counts() 
max_team = len(df['Team'].unique())
max_score= 10 * 13

#station summary
df_station = df["Station"].value_counts()  
max_station = 13


# Example to display
example_score = df_team.loc["Cevedale", "Score"]
example_team_station = df_team_station["Cevedale"]
example_station = df_station["Station A"]
example_order = df_team.loc["Cevedale", "Order"]
print(f"Score: {example_score}/{max_score}")
print(f"Stationen: {example_team_station}/{max_station}")
print(f"Teamsreihnfolge: {example_order}")
print(f"Teams in Stationen: {example_station}/{max_team}")









# from __future__ import print_function
# import gspread
# from oauth2client.client import SignedJwtAssertionCredentials
# import pandas as pd
# import json


# SCOPE = ["https://docs.google.com/spreadsheets/d/1eHuUXIXMmwADt9B6cpSuLWSNGAWvgYTps6rU6FHEZRQ/edit?resourcekey#gid=174414602"]
# SECRETS_FILE = "tour-de-schneck-6c39180b57b4.json"
# SPREADSHEET = "Ergebnisse"


# json_key = json.load(open(SECRETS_FILE))
# # Authenticate using the signed key
# credentials = SignedJwtAssertionCredentials(json_key['client_email'],
#                                             json_key['private_key'], SCOPE)


# gc = gspread.authorize(credentials)


# print("The following sheets are available")
# for sheet in gc.openall():
#     print("{} - {}".format(sheet.title, sheet.id))