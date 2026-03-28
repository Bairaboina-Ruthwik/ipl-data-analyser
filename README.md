# 🏏 IPL Data Analysis

## 📌 Overview

This project performs basic data analysis on IPL match data using **Pandas** and **Matplotlib**. It extracts insights like team performance, toss impact, top players, and win patterns.

---

## 📂 Project Structure

```
IPL-Analysis/
│── ipl.csv
│── main.py
│── outputs/
│   ├── team_wins.png
│   ├── toss_impact.png
│   ├── top_players.png
│   ├── win_type.png
│   ├── toss_decision.png
│── README.md
```

---

## ⚙️ Requirements

Install the required libraries:

```bash
pip install pandas matplotlib
```

---

## ▶️ How to Run

1. Place `ipl.csv` in the project folder
2. Run the script:

```bash
python main.py
```

3. Output graphs will be saved in the `outputs/` folder

---

## 📊 Analysis Performed

### 1. 🏆 Most Wins by Team

* Counts total wins for each team
* Displays as a bar chart

### 2. 🎯 Toss Impact

* Calculates how often the toss-winning team also wins the match
* Visualized using a pie chart

### 3. ⭐ Top Players

* Finds top 10 players with most "Player of the Match" awards
* Displayed as a bar chart

### 4. ⚔️ Win Type Distribution

* Categorizes wins into:

  * Bat First (runs)
  * Field First (wickets)
* Shown using a pie chart

### 5. 🪙 Toss Decision

* Shows how often teams choose:

  * Bat
  * Field
* Visualized using a bar chart

---

## 📁 Outputs

All generated graphs are saved in the `outputs/` folder:

* `team_wins.png`
* `toss_impact.png`
* `top_players.png`
* `win_type.png`
* `toss_decision.png`

---

## 📌 Notes

* Matches with no result are removed (`winner` is NaN)
* Missing or inconsistent data is handled before analysis

---

## 🚀 Future Improvements

* Add season-wise analysis
* Compare team performance over years
* Use Seaborn for better visualization
* Build a dashboard

---

## 👨‍💻 Author

Bairaboina Ruthwik
