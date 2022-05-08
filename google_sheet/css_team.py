from data_google_sheet import df_team

with open("./css/style_teams.css", "w") as f_team:
    f_team.write(
         f"""
        .GL .team__points::after {{
            content: \"{df_team.loc["GL","w_score"]}\"
        }}
        .GL .team__stations::after {{
            content: \"{df_team.loc["GL","w_station_done"]}\"
        }}
        .GL .team__additional-points::after {{
            content: \"{df_team.loc["GL","Originelle_Zusatzpunkte"]}\"
        }}
        .GL .team__logo {{
            background-color: {df_team.loc["GL","color"]}
        }}
        .GL {{
            order: {df_team.loc["GL","order"]}
        }}
        
        .O .team__points::after {{
            content: \"{df_team.loc["O","w_score"]}\"
        }}
        .O .team__stations::after {{
            content: \"{df_team.loc["O","w_station_done"]}\"
        }}
        .O .team__additional-points::after {{
            content: \"{df_team.loc["O","Originelle_Zusatzpunkte"]}\"
        }}
        .O .team__logo {{
            background-color: {df_team.loc["O","color"]}
        }}
        .O {{
            order: {df_team.loc["O","order"]}
        }}

        .Z .team__points::after {{
            content: \"{df_team.loc["Z","w_score"]}\"
        }}
        .Z .team__stations::after {{
            content: \"{df_team.loc["Z","w_station_done"]}\"
        }}
        .Z .team__additional-points::after {{
            content: \"{df_team.loc["Z","Originelle_Zusatzpunkte"]}\"
        }}
        .Z .team__logo {{
            background-color: {df_team.loc["Z","color"]}
        }}
        .Z {{
            order: {df_team.loc["Z","order"]}
        }}

        .M .team__points::after {{
            content: \"{df_team.loc["M","w_score"]}\"
        }}
        .M .team__stations::after {{
            content: \"{df_team.loc["M","w_station_done"]}\"
        }}
        .M .team__additional-points::after {{
            content: \"{df_team.loc["M","Originelle_Zusatzpunkte"]}\"
        }}
        .M .team__logo {{
            background-color: {df_team.loc["M","color"]}
        }}
        .M {{
            order: {df_team.loc["M","order"]}
        }}

        .DS .team__points::after {{
            content: \"{df_team.loc["DS","w_score"]}\"
        }}
        .DS .team__stations::after {{
            content: \"{df_team.loc["DS","w_station_done"]}\"
        }}
        .DS .team__additional-points::after {{
            content: \"{df_team.loc["DS","Originelle_Zusatzpunkte"]}\"
        }}
        .DS .team__logo {{
            background-color: {df_team.loc["DS","color"]}
        }}
        .DS {{
            order: {df_team.loc["DS","order"]}
        }}

        .DU .team__points::after {{
            content: \"{df_team.loc["DU","w_score"]}\"
        }}
        .DU .team__stations::after {{
            content: \"{df_team.loc["DU","w_station_done"]}\"
        }}
        .DU .team__additional-points::after {{
            content: \"{df_team.loc["DU","Originelle_Zusatzpunkte"]}\"
        }}
        .DU .team__logo {{
            background-color: {df_team.loc["DU","color"]}
        }}
        .DU {{
            order: {df_team.loc["DU","order"]}
        }}


        .OT .team__points::after {{
            content: \"{df_team.loc["ÖT","w_score"]}\"
        }}
        .OT .team__stations::after {{
            content: \"{df_team.loc["ÖT","w_station_done"]}\"
        }}
        .OT .team__additional-points::after {{
            content: \"{df_team.loc["ÖT","Originelle_Zusatzpunkte"]}\"
        }}
        .OT .team__logo {{
            background-color: {df_team.loc["ÖT","color"]}
        }}
        .OT {{
            order: {df_team.loc["ÖT","order"]}
        }}


        .GG .team__points::after {{
            content: \"{df_team.loc["GG","w_score"]}\"
        }}
        .GG .team__stations::after {{
            content: \"{df_team.loc["GG","w_station_done"]}\"
        }}
        .GG .team__additional-points::after {{
            content: \"{df_team.loc["GG","Originelle_Zusatzpunkte"]}\"
        }}
        .GG .team__logo {{
            background-color: {df_team.loc["GG","color"]}
        }}
        .GG {{
            order: {df_team.loc["GG","order"]}
        }}


        .CH .team__points::after {{
            content: \"{df_team.loc["CH","w_score"]}\"
        }}
        .CH .team__stations::after {{
            content: \"{df_team.loc["CH","w_station_done"]}\"
        }}
        .CH .team__additional-points::after {{
            content: \"{df_team.loc["CH","Originelle_Zusatzpunkte"]}\"
        }}
        .CH .team__logo {{
            background-color: {df_team.loc["CH","color"]}
        }}
        .CH {{
            order: {df_team.loc["CH","order"]}
        }}


        .GO .team__points::after {{
            content: \"{df_team.loc["GÖ","w_score"]}\"
        }}
        .GO .team__stations::after {{
            content: \"{df_team.loc["GÖ","w_station_done"]}\"
        }}
        .GO .team__additional-points::after {{
            content: \"{df_team.loc["GÖ","Originelle_Zusatzpunkte"]}\"
        }}
        .GO .team__logo {{
            background-color: {df_team.loc["GÖ","color"]}
        }}
        .GO {{
            order: {df_team.loc["GÖ","order"]}
        }}

        .GV .team__points::after {{
            content: \"{df_team.loc["GV","w_score"]}\"
        }}
        .GV .team__stations::after {{
            content: \"{df_team.loc["GV","w_station_done"]}\"
        }}
        .GV .team__additional-points::after {{
            content: \"{df_team.loc["GV","Originelle_Zusatzpunkte"]}\"
        }}
        .GV .team__logo {{
            background-color: {df_team.loc["GV","color"]}
        }}
        .GV {{
            order: {df_team.loc["GV","order"]}
        }}


        .SC .team__points::after {{
            content: \"{df_team.loc["SC","w_score"]}\"
        }}
        .SC .team__stations::after {{
            content: \"{df_team.loc["SC","w_station_done"]}\"
        }}
        .SC .team__additional-points::after {{
            content: \"{df_team.loc["SC","Originelle_Zusatzpunkte"]}\"
        }}
        .SC .team__logo {{
            background-color: {df_team.loc["SC","color"]}
        }}
        .SC {{
            order: {df_team.loc["SC","order"]}
        }}

        .V .team__points::after {{
            content: \"{df_team.loc["V","w_score"]}\"
        }}
        .V .team__stations::after {{
            content: \"{df_team.loc["V","w_station_done"]}\"
        }}
        .V .team__additional-points::after {{
            content: \"{df_team.loc["V","Originelle_Zusatzpunkte"]}\"
        }}
        .V .team__logo {{
            background-color: {df_team.loc["V","color"]}
        }}
        .V {{
            order: {df_team.loc["V","order"]}
        }}


        .MK .team__points::after {{
            content: \"{df_team.loc["MK","w_score"]}\"
        }}
        .MK .team__stations::after {{
            content: \"{df_team.loc["MK","w_station_done"]}\"
        }}
        .MK .team__additional-points::after {{
            content: \"{df_team.loc["MK","Originelle_Zusatzpunkte"]}\"
        }}
        .MK .team__logo {{
            background-color: {df_team.loc["MK","color"]}
        }}
        .MK {{
            order: {df_team.loc["MK","order"]}
        }}

        .SA .team__points::after {{
            content: \"{df_team.loc["SA","w_score"]}\"
        }}
        .SA .team__stations::after {{
            content: \"{df_team.loc["SA","w_station_done"]}\"
        }}
        .SA .team__additional-points::after {{
            content: \"{df_team.loc["SA","Originelle_Zusatzpunkte"]}\"
        }}
        .SA .team__logo {{
            background-color: {df_team.loc["SA","color"]}
        }}
        .SA {{
            order: {df_team.loc["SA","order"]}
        }}
        

        .P .team__points::after {{
            content: \"{df_team.loc["P","w_score"]}\"
        }}
        .P .team__stations::after {{
            content: \"{df_team.loc["P","w_station_done"]}\"
        }}
        .P .team__additional-points::after {{
            content: \"{df_team.loc["P","Originelle_Zusatzpunkte"]}\"
        }}
        .P .team__logo {{
            background-color: {df_team.loc["P","color"]}
        }}
        .P {{
            order: {df_team.loc["P","order"]}
        }}


        .R .team__points::after {{
            content: \"{df_team.loc["R","w_score"]}\"
        }}
        .R .team__stations::after {{
            content: \"{df_team.loc["R","w_station_done"]}\"
        }}
        .R .team__additional-points::after {{
            content: \"{df_team.loc["R","Originelle_Zusatzpunkte"]}\"
        }}
        .R .team__logo {{
            background-color: {df_team.loc["R","color"]}
        }}
        .R {{
            order: {df_team.loc["R","order"]}
        }}


        .HS .team__points::after {{
            content: \"{df_team.loc["HS","w_score"]}\"
        }}
        .HS .team__stations::after {{
            content: \"{df_team.loc["HS","w_station_done"]}\"
        }}
        .HS .team__additional-points::after {{
            content: \"{df_team.loc["HS","Originelle_Zusatzpunkte"]}\"
        }}
        .HS .team__logo {{
            background-color: {df_team.loc["HS","color"]}
        }}
        .HS {{
            order: {df_team.loc["HS","order"]}
        }}
        

        .CE .team__points::after {{
            content: \"{df_team.loc["CE","w_score"]}\"
        }}
        .CE .team__stations::after {{
            content: \"{df_team.loc["CE","w_station_done"]}\"
        }}
        .CE .team__additional-points::after {{
            content: \"{df_team.loc["CE","Originelle_Zusatzpunkte"]}\"
        }}
        .CE .team__logo {{
            background-color: {df_team.loc["CE","color"]}
        }}
        .CE {{
            order: {df_team.loc["CE","order"]}
        }}
        

        .PP .team__points::after {{
            content: \"{df_team.loc["PP","w_score"]}\"
        }}
        .PP .team__stations::after {{
            content: \"{df_team.loc["PP","w_station_done"]}\"
        }}
        .PP .team__additional-points::after {{
            content: \"{df_team.loc["PP","Originelle_Zusatzpunkte"]}\"
        }}
        .PP .team__logo {{
            background-color: {df_team.loc["PP","color"]}
        }}
        .PP {{
            order: {df_team.loc["PP","order"]}
        }}

        
        .HW .team__points::after {{
            content: \"{df_team.loc["HW","w_score"]}\"
        }}
        .HW .team__stations::after {{
            content: \"{df_team.loc["HW","w_station_done"]}\"
        }}
        .HW .team__additional-points::after {{
            content: \"{df_team.loc["HW","Originelle_Zusatzpunkte"]}\"
        }}
        .HW .team__logo {{
            background-color: {df_team.loc["HW","color"]}
        }}
        .HW {{
            order: {df_team.loc["HW","order"]}
        }}


        .K .team__points::after {{
            content: \"{df_team.loc["K","w_score"]}\"
        }}
        .K .team__stations::after {{
            content: \"{df_team.loc["K","w_station_done"]}\"
        }}
        .K .team__additional-points::after {{
            content: \"{df_team.loc["K","Originelle_Zusatzpunkte"]}\"
        }}
        .K .team__logo {{
            background-color: {df_team.loc["K","color"]}
        }}
        .K {{
            order: {df_team.loc["K","order"]}
        }}

        
        
        

        
        .C .team__points::after {{
            content: \"{df_team.loc["C","w_score"]}\"
        }}
        .C .team__stations::after {{
            content: \"{df_team.loc["C","w_station_done"]}\"
        }}
        .C .team__additional-points::after {{
            content: \"{df_team.loc["C","Originelle_Zusatzpunkte"]}\"
        }}
        .C .team__logo {{
            background-color: {df_team.loc["C","color"]}
        }}
        .C {{
            order: {df_team.loc["C","order"]}
        }}

        
        """ )


print("Python: style_teams.css compiled")