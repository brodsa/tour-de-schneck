import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from data_google_sheet import df_team


# Visualization
df_team["Teamname"] = df_team["short"]
df_team.sort_values(by=["Score"],inplace=True,ascending=False)
colors = df_team["color"]
sns.set_palette(sns.color_palette(colors))

plt.figure(figsize=(20,10), dpi=200)
sns.barplot(y = 'Score', x="Teamname", data = df_team)
plt.xlabel('Team', fontsize=20)
plt.ylabel('Score', fontsize=20)
plt.xticks(fontsize= 18)
plt.yticks(fontsize= 18)
plt.savefig("./img/Score.png" , dpi = 200)

df_team.sort_values(by=["Originelle_Zusatzpunkte"],inplace=True,ascending=False)
colors = df_team["color"]
sns.set_palette(sns.color_palette(colors))

plt.figure(figsize=(20,10), dpi=200)
sns.barplot(y = 'Originelle_Zusatzpunkte', x="Teamname", data = df_team)
plt.xlabel('Team', fontsize=20)
plt.ylabel('Bonuspunkte', fontsize=20)
plt.xticks(fontsize= 18)
plt.yticks(fontsize= 18)
plt.savefig("./img/Bonus.png" , dpi = 200)
print("Python: Plots done")