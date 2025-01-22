# H2H Tennis Analysis Dashboard 🎾

## Overview
This repository provides an interactive dashboard that showcases players with a favorable Head-to-Head (H2H) record against tennis legends Roger Federer, Novak Djokovic, and Rafael Nadal. The visualization enables easy exploration of the data, highlighting opponents who have managed to outperform these iconic players in their careers.

## Features
- **Interactive Visualizations:** Bar charts displaying players with a favorable H2H against each member of the "Big Three."
- **Dynamic Analysis:** Filter and compare data across Federer, Nadal, and Djokovic in a single view.
- **Streamlit Integration:** Hosted dashboard for easy sharing and interactivity.

## Dataset
The dataset used in this analysis was compiled from [Ultimate Tennis Statistics](https://ultimatetennisstatistics.com/headsToHeads). It includes:
- Total matches played
- Matches won and lost by each player
- Calculated win rates

### Files
- `dashboard.py`: Main Python script that builds and runs the Streamlit dashboard.
- `big_three_h2h.xlsx`: Dataset containing H2H records for the "Big Three" players.

## Requirements
To run the dashboard, ensure the following dependencies are installed:

```bash
pip install pandas plotly streamlit
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/h2h-tennis-dashboard.git
   cd h2h-tennis-dashboard
   ```

2. Ensure the dataset (`big_three_h2h.xlsx`) is in the same directory as `dashboard.py`.

3. Run the Streamlit app:
   ```bash
   streamlit run dashboard.py
   ```

4. Open the provided URL in your browser to view the dashboard.

## Tools and Technologies
- **Python:** Data analysis and visualization
- **Pandas:** Data manipulation and transformation
- **Plotly:** Interactive chart creation
- **Streamlit:** Dashboard deployment

## Why This Analysis?
While global H2H statistics for these players are widely discussed, there is limited focus on summarizing opponents who have achieved favorable H2H records against them. This analysis provides a fresh perspective, presenting the data in a concise and visually appealing manner.


