from data_google_sheet import df_station, max_station

with open("style_station.css", "w") as f_station:
    f_station.write(
        f"""
        .station-a::after {{
            content: \"{df_station["Station A"]}\"
        }}
        

        """ )

