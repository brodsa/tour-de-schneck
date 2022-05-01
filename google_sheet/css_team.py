from data_google_sheet import df_team

with open("style_teams.css", "w") as f_team:
    f_team.write(
         f"""
        .team-a::after {{
            content: \" {df_team.loc["Cevedale", "Score"]} \"
        }}
        

        """ )
