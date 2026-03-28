import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs("outputs", exist_ok=True)

df = pd.read_csv("ipl.csv")

print("First 5 rows:\n",df.head())
print("\nColumns\n:",df.columns)

df = df.dropna(subset=["winner"])

wins = df["winner"].value_counts()

plt.figure()
wins.plot(kind="bar")
plt.title("Most Wins By Team")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.xticks(rotation = 90)
plt.savefig("outputs/team_wins.png")
plt.show()

toss_win = df[df["toss_winner"] == df["winner"]]
impact = len(toss_win) / len(df) * 100

print("Toss Impact:",impact)

plt.figure()
plt.pie([impact,100-impact],labels=["Win after Toss","Lose after Toss"],autopct="%1.1f%%")
plt.title("Toss Impact")
plt.savefig("outputs/toss_impact.png")
plt.show()

top_players = df["player_of_match"].value_counts().head(10)

plt.figure()
top_players.plot(kind = "bar")
plt.title("Top Players (Man of the Match)")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.savefig("outputs/top_players.png")
plt.show()


df["win_type"] = df["result"].apply(lambda x: "Bat first" if x == "runs" else ("Field First" if x == "wickets" else "Other"))

win_type = df["win_type"].value_counts()
plt.figure()
win_type.plot(kind = "pie",autopct ="%1.1f%%")
plt.title("Win Type Distribution")
plt.savefig("outputs/win_type.png")
plt.show()

toss_decision = df["toss_decision"].value_counts()

plt.figure()
toss_decision.plot(kind = "bar")
plt.title("Toss Decision")
plt.savefig("outputs/toss_decision.png")
plt.show()