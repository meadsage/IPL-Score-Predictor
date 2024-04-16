import ipywidgets as widgets
from IPython.display import display, clear_output

# GUI
venue_dropdown = widgets.Dropdown(options=df['venue'].unique(), description='Venue:')
batting_team_dropdown = widgets.Dropdown(options=df['bat_team'].unique(), description='Batting Team:')
bowling_team_dropdown = widgets.Dropdown(options=df['bowl_team'].unique(), description='Bowling Team:')
striker_dropdown = widgets.Dropdown(options=df['batsman'].unique(), description='Striker:')
bowler_dropdown = widgets.Dropdown(options=df['bowler'].unique(), description='Bowler:')

predict_button = widgets.Button(description="Predict Score")
output = widgets.Output()

def on_predict_button_clicked(b):
    with output:
        clear_output()
        predict_score(venue_dropdown.value, batting_team_dropdown.value, bowling_team_dropdown.value, striker_dropdown.value, bowler_dropdown.value)

predict_button.on_click(on_predict_button_clicked)

display(venue_dropdown, batting_team_dropdown, bowling_team_dropdown, striker_dropdown, bowler_dropdown, predict_button, output)
