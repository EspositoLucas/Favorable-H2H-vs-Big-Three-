import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Load the data file
file_path = 'big_three_h2h.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load all sheets from the file
df_djokovic = excel_data.parse('h2h_djokovic')
df_nadal = excel_data.parse('h2h_nadal')
df_federer = excel_data.parse('h2h_federer')

# Filter players with a favorable H2H against each one
def get_h2h_favorable(df, player_name):
    df['win_rate'] = df['won'] / df['matches']  # Calculate win percentage
    favorable_h2h = df[df['lost'] > df['won']]  # Opponent won more matches than the player
    favorable_h2h['player'] = player_name  # Add a column to identify the player
    return favorable_h2h[['name', 'matches', 'won', 'lost', 'win_rate', 'player']]

# Get results for each player
df_favorable_djokovic = get_h2h_favorable(df_djokovic, "Djokovic")
df_favorable_nadal = get_h2h_favorable(df_nadal, "Nadal")
df_favorable_federer = get_h2h_favorable(df_federer, "Federer")

# Combine the data into a single DataFrame
df_combined = pd.concat([df_favorable_djokovic, df_favorable_nadal, df_favorable_federer], ignore_index=True)

# Create an interactive dashboard
def create_dashboard(data):
    fig = go.Figure()

    # Add bars for each Big Three player
    for player in data['player'].unique():
        player_data = data[data['player'] == player]
        fig.add_trace(go.Bar(
            x=player_data['name'],
            y=player_data['lost'],
            name=player,
            text=['Total Matches Played: ' + str(m) for m in player_data['matches']],
            texttemplate='%{text}',
            textposition='outside',
            marker=dict(line=dict(color='white', width=1.5))
        ))

    # Configure chart layout
    fig.update_layout(
        title='Players with Favorable H2H vs Big Three',
        template='plotly_dark',
        xaxis=dict(title='Opponent', categoryorder='total descending'),
        yaxis=dict(title='Matches Lost'),
        barmode='group',
        legend=dict(title='Big Three Player'),
        uniformtext_minsize=8,
        uniformtext_mode='hide'
    )

    return fig

# Generate and display the dashboard
fig_dashboard = create_dashboard(df_combined)

# Use Streamlit to share the dashboard
st.title('Favorable H2H vs Big Three 🎾')
st.plotly_chart(fig_dashboard)

st.markdown("### Analysis Summary")
st.write(
    "This dashboard highlights players who have had a favorable record against tennis legends Roger Federer, Novak Djokovic, and Rafael Nadal. The data was sourced from [Ultimate Tennis Statistics](https://ultimatetennisstatistics.com/headsToHeads)."
)
st.write(
    "Using Python, Excel, and libraries like Pandas and Plotly, it was possible to transform a complex dataset into a clear and interactive visualization."
)
