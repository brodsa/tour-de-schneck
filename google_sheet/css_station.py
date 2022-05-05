from data_google_sheet import df_station

with open("./css/style_station.css", "w") as f_station:
    f_station.write(
        f"""
        .station-a::after {{
            content: \"{df_station.loc["A","w_teams_done"]}\"
        }}
        

        """ )

