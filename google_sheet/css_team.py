from data_google_sheet import df_team

with open("./css/style_teams.css", "w") as f_team:
    f_team.write(
         f"""
        .GL .team__score::after {{
            content: \"{df_team.loc["GL","w_score"]}\"
        }}
        .GL .team__stations::after {{
            content: \"{df_team.loc["GL","w_station_done"]}\"
        }}
        .GL .team__bonus::after {{
            content: \"{df_team.loc["GL","Originelle_Zusatzpunkte"]}\"
        }}
        .GL .team__logo {{
            background-color: {df_team.loc["GL","color"]}
        }}
        .GL {{
            order: {df_team.loc["GL","order"]}
        }}
        .GL .team__all-points::after{{
            content: \"{df_team.loc["GL","w_points"]}\"
        }}
        
        .O .team__score::after {{
            content: \"{df_team.loc["O","w_score"]}\"
        }}
        .O .team__stations::after {{
            content: \"{df_team.loc["O","w_station_done"]}\"
        }}
        .O .team__bonus::after {{
            content: \"{df_team.loc["O","Originelle_Zusatzpunkte"]}\"
        }}
        .O .team__logo {{
            background-color: {df_team.loc["O","color"]}
        }}
        .O {{
            order: {df_team.loc["O","order"]}
        }}
        .O .team__all-points::after{{ 
            content: \" {df_team.loc["O","w_points"]}\"
        }}


        .Z .team__score::after {{
            content: \"{df_team.loc["Z","w_score"]}\"
        }}
        .Z .team__stations::after {{
            content: \"{df_team.loc["Z","w_station_done"]}\"
        }}
        .Z .team__bonus::after {{
            content: \"{df_team.loc["Z","Originelle_Zusatzpunkte"]}\"
        }}
        .Z .team__logo {{
            background-color: {df_team.loc["Z","color"]}
        }}
        .Z {{
            order: {df_team.loc["Z","order"]}
        }}
        .Z .team__all-points::after{{
            content: \"{df_team.loc["Z","w_points"]}\"
        }}



        .M .team__score::after {{
            content: \"{df_team.loc["M","w_score"]}\"
        }}
        .M .team__stations::after {{
            content: \"{df_team.loc["M","w_station_done"]}\"
        }}
        .M .team__bonus::after {{
            content: \"{df_team.loc["M","Originelle_Zusatzpunkte"]}\"
        }}
        .M .team__logo {{
            background-color: {df_team.loc["M","color"]}
        }}
        .M {{
            order: {df_team.loc["M","order"]}
        }}
        .M .team__all-points::after{{
            content: \"{df_team.loc["M","w_points"]} \"
        }}


        .DS .team__score::after {{
            content: \"{df_team.loc["DS","w_score"]}\"
        }}
        .DS .team__stations::after {{
            content: \"{df_team.loc["DS","w_station_done"]}\"
        }}
        .DS .team__bonus::after {{
            content: \"{df_team.loc["DS","Originelle_Zusatzpunkte"]}\"
        }}
        .DS .team__logo {{
            background-color: {df_team.loc["DS","color"]}
        }}
        .DS {{
            order: {df_team.loc["DS","order"]}
        }}
        .DS .team__all-points::after{{
            content: \"{df_team.loc["DS","w_points"]}\"
        }}
        

        .DU .team__score::after {{
            content: \"{df_team.loc["DU","w_score"]}\"
        }}
        .DU .team__stations::after {{
            content: \"{df_team.loc["DU","w_station_done"]}\"
        }}
        .DU .team__bonus::after {{
            content: \"{df_team.loc["DU","Originelle_Zusatzpunkte"]}\"
        }}
        .DU .team__logo {{
            background-color: {df_team.loc["DU","color"]}
        }}
        .DU {{
            order: {df_team.loc["DU","order"]}
        }}
        .DU .team__all-points::after{{
            content: \"{df_team.loc["DU","w_points"]}\"
        }}



        .OT .team__score::after {{
            content: \"{df_team.loc["ÖT","w_score"]}\"
        }}
        .OT .team__stations::after {{
            content: \"{df_team.loc["ÖT","w_station_done"]}\"
        }}
        .OT .team__bonus::after {{
            content: \"{df_team.loc["ÖT","Originelle_Zusatzpunkte"]}\"
        }}
        .OT .team__logo {{
            background-color: {df_team.loc["ÖT","color"]}
        }}
        .OT {{
            order: {df_team.loc["ÖT","order"]}
        }}
        .OT .team__all-points::after{{
            content: \" {df_team.loc["ÖT","w_points"]}\"
        }}



        .GG .team__score::after {{
            content: \"{df_team.loc["GG","w_score"]}\"
        }}
        .GG .team__stations::after {{
            content: \"{df_team.loc["GG","w_station_done"]}\"
        }}
        .GG .team__bonus::after {{
            content: \"{df_team.loc["GG","Originelle_Zusatzpunkte"]}\"
        }}
        .GG .team__logo {{
            background-color: {df_team.loc["GG","color"]}
        }}
        .GG {{
            order: {df_team.loc["GG","order"]}
        }}
        .GG .team__all-points::after{{
             content: \"{df_team.loc["GG","w_points"]}\"
        }}


        .CH .team__score::after {{
            content: \"{df_team.loc["CH","w_score"]}\"
        }}
        .CH .team__stations::after {{
            content: \"{df_team.loc["CH","w_station_done"]}\"
        }}
        .CH .team__bonus::after {{
            content: \"{df_team.loc["CH","Originelle_Zusatzpunkte"]}\"
        }}
        .CH .team__logo {{
            background-color: {df_team.loc["CH","color"]}
        }}
        .CH {{
            order: {df_team.loc["CH","order"]}
        }}
        .CH .team__all-points::after{{
            content: \"{df_team.loc["CH","w_points"]}\"
        }}


        .GO .team__score::after {{
            content: \"{df_team.loc["GÖ","w_score"]}\"
        }}
        .GO .team__stations::after {{
            content: \"{df_team.loc["GÖ","w_station_done"]}\"
        }}
        .GO .team__bonus::after {{
            content: \"{df_team.loc["GÖ","Originelle_Zusatzpunkte"]}\"
        }}
        .GO .team__logo {{
            background-color: {df_team.loc["GÖ","color"]}
        }}
        .GO {{
            order: {df_team.loc["GÖ","order"]}
        }}
        .GO .team__all-points::after{{
            content: \"{df_team.loc["GÖ","w_points"]}\"
        }}


        .GV .team__score::after {{
            content: \"{df_team.loc["GV","w_score"]}\"
        }}
        .GV .team__stations::after {{
            content: \"{df_team.loc["GV","w_station_done"]}\"
        }}
        .GV .team__bonus::after {{
            content: \"{df_team.loc["GV","Originelle_Zusatzpunkte"]}\"
        }}
        .GV .team__logo {{
            background-color: {df_team.loc["GV","color"]}
        }}
        .GV {{
            order: {df_team.loc["GV","order"]}
        }}
        .GV .team__all-points::after{{
            content: \"{df_team.loc["GV","w_points"]}\"
        }}


        .SC .team__score::after {{
            content: \"{df_team.loc["SC","w_score"]}\"
        }}
        .SC .team__stations::after {{
            content: \"{df_team.loc["SC","w_station_done"]}\"
        }}
        .SC .team__bonus::after {{
            content: \"{df_team.loc["SC","Originelle_Zusatzpunkte"]}\"
        }}
        .SC .team__logo {{
            background-color: {df_team.loc["SC","color"]}
        }}
        .SC {{
            order: {df_team.loc["SC","order"]}
        }}
        .SC .team__all-points::after{{
            content: \"{df_team.loc["SC","w_points"]}\"
        }}


        .V .team__score::after {{
            content: \"{df_team.loc["V","w_score"]}\"
        }}
        .V .team__stations::after {{
            content: \"{df_team.loc["V","w_station_done"]}\"
        }}
        .V .team__bonus::after {{
            content: \"{df_team.loc["V","Originelle_Zusatzpunkte"]}\"
        }}
        .V .team__logo {{
            background-color: {df_team.loc["V","color"]}
        }}
        .V {{
            order: {df_team.loc["V","order"]}
        }}
        .V .team__all-points::after{{
            content: \"{df_team.loc["V","w_points"]}\"
        }}


        .MK .team__score::after {{
            content: \"{df_team.loc["MK","w_score"]}\"
        }}
        .MK .team__stations::after {{
            content: \"{df_team.loc["MK","w_station_done"]}\"
        }}
        .MK .team__bonus::after {{
            content: \"{df_team.loc["MK","Originelle_Zusatzpunkte"]}\"
        }}
        .MK .team__logo {{
            background-color: {df_team.loc["MK","color"]}
        }}
        .MK {{
            order: {df_team.loc["MK","order"]}
        }}
        .MK .team__all-points::after{{
            content: \"{df_team.loc["MK","w_points"]}\"
        }}


        .SA .team__score::after {{
            content: \"{df_team.loc["SA","w_score"]}\"
        }}
        .SA .team__stations::after {{
            content: \"{df_team.loc["SA","w_station_done"]}\"
        }}
        .SA .team__bonus::after {{
            content: \"{df_team.loc["SA","Originelle_Zusatzpunkte"]}\"
        }}
        .SA .team__logo {{
            background-color: {df_team.loc["SA","color"]}
        }}
        .SA {{
            order: {df_team.loc["SA","order"]}
        }}
        .SA .team__all-points::after{{
            content: \"{df_team.loc["SA","w_points"]}\"
        }}
        

        .P .team__score::after {{
            content: \"{df_team.loc["P","w_score"]}\"
        }}
        .P .team__stations::after {{
            content: \"{df_team.loc["P","w_station_done"]}\"
        }}
        .P .team__bonus::after {{
            content: \"{df_team.loc["P","Originelle_Zusatzpunkte"]}\"
        }}
        .P .team__logo {{
            background-color: {df_team.loc["P","color"]}
        }}
        .P {{
            order: {df_team.loc["P","order"]}
        }}
        .P .team__all-points::after{{
            content: \"{df_team.loc["P","w_points"]}\"
        }}


        .R .team__score::after {{
            content: \"{df_team.loc["R","w_score"]}\"
        }}
        .R .team__stations::after {{
            content: \"{df_team.loc["R","w_station_done"]}\"
        }}
        .R .team__bonus::after {{
            content: \"{df_team.loc["R","Originelle_Zusatzpunkte"]}\"
        }}
        .R .team__logo {{
            background-color: {df_team.loc["R","color"]}
        }}
        .R {{
            order: {df_team.loc["R","order"]}
        }}
        .R .team__all-points::after{{
            content: \"{df_team.loc["R","w_points"]}\"
        }}



        .HS .team__score::after {{
            content: \"{df_team.loc["HS","w_score"]}\"
        }}
        .HS .team__stations::after {{
            content: \"{df_team.loc["HS","w_station_done"]}\"
        }}
        .HS .team__bonus::after {{
            content: \"{df_team.loc["HS","Originelle_Zusatzpunkte"]}\"
        }}
        .HS .team__logo {{
            background-color: {df_team.loc["HS","color"]}
        }}
        .HS {{
            order: {df_team.loc["HS","order"]}
        }}
        .HS .team__all-points::after{{
            content: \"{df_team.loc["HS","w_points"]}\"
        }}

        

        .CE .team__score::after {{
            content: \"{df_team.loc["CE","w_score"]}\"
        }}
        .CE .team__stations::after {{
            content: \"{df_team.loc["CE","w_station_done"]}\"
        }}
        .CE .team__bonus::after {{
            content: \"{df_team.loc["CE","Originelle_Zusatzpunkte"]}\"
        }}
        .CE .team__logo {{
            background-color: {df_team.loc["CE","color"]}
        }}
        .CE {{
            order: {df_team.loc["CE","order"]}
        }}
        .CE .team__all-points::after{{
            content: \"{df_team.loc["CE","w_points"]}\"
        }}


        .PP .team__score::after {{
            content: \"{df_team.loc["PP","w_score"]}\"
        }}
        .PP .team__stations::after {{
            content: \"{df_team.loc["PP","w_station_done"]}\"
        }}
        .PP .team__bonus::after {{
            content: \"{df_team.loc["PP","Originelle_Zusatzpunkte"]}\"
        }}
        .PP .team__logo {{
            background-color: {df_team.loc["PP","color"]}
        }}
        .PP {{
            order: {df_team.loc["PP","order"]}
        }}
        .PP .team__all-points::after{{
            content: \"{df_team.loc["PP","w_points"]}\"
        }}

        
        .HW .team__score::after {{
            content: \"{df_team.loc["HW","w_score"]}\"
        }}
        .HW .team__stations::after {{
            content: \"{df_team.loc["HW","w_station_done"]}\"
        }}
        .HW .team__bonus::after {{
            content: \"{df_team.loc["HW","Originelle_Zusatzpunkte"]}\"
        }}
        .HW .team__logo {{
            background-color: {df_team.loc["HW","color"]}
        }}
        .HW {{
            order: {df_team.loc["HW","order"]}
        }}
        .HW .team__all-points::after{{
            content: \"{df_team.loc["HW","w_points"]}\"
        }}


        .K .team__score::after {{
            content: \"{df_team.loc["K","w_score"]}\"
        }}
        .K .team__stations::after {{
            content: \"{df_team.loc["K","w_station_done"]}\"
        }}
        .K .team__bonus::after {{
            content: \"{df_team.loc["K","Originelle_Zusatzpunkte"]}\"
        }}
        .K .team__logo {{
            background-color: {df_team.loc["K","color"]}
        }}
        .K {{
            order: {df_team.loc["K","order"]}
        }}
        .K .team__all-points::after{{
            content: \"{df_team.loc["K","w_points"]}\"
        }}
        
        
        .CO .team__score::after {{
            content: \"{df_team.loc["CO","w_score"]}\"
        }}
        .CO .team__stations::after {{
            content: \"{df_team.loc["CO","w_station_done"]}\"
        }}
        .CO .team__bonus::after {{
            content: \"{df_team.loc["CO","Originelle_Zusatzpunkte"]}\"
        }}
        .CO .team__logo {{
            background-color: {df_team.loc["CO","color"]}
        }}
        .CO {{
            order: {df_team.loc["CO","order"]}
        }}
        .CO .team__all-points::after{{
            content: \"{df_team.loc["CO","w_points"]}\"
        }}

        
        """ )


print("Python: style_teams.css compiled")