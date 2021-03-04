import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.express as px

from poker.parsers.pokernow.parser import parse_game

log_file_path = "/mnt/c/Users/Owen Mitchell/Desktop/Files/Poker/Game Logs/poker_now_log_hyrimfOUVowoGt_23GAl7gq65.csv"
game_data = open(log_file_path).read()
game = parse_game(game_data)

d = {}

for hand in game.hands:
    away_players = list(d.keys())
    for (player, stack) in hand.stacks:
        if player.name not in d:
            d[player.name] = []
        else:
            away_players.remove(player.name)
        d[player.name].append((stack, hand.id))

plist = list(d.keys())

options = []
for player in plist:
    options.append({"label": player, "value": player})

df = pd.DataFrame(
    {
        "chips": [],
        "hand": [],
    }
)
figure = px.line(df, x="hand", y="chips")

app = dash.Dash("Pyker")
app.layout = html.Div(
    [
        dcc.Dropdown(id="player", options=options),
        dcc.Graph(id="my-graph", figure=figure),
    ],
    style={"width": "500"},
)


@app.callback(Output("my-graph", "figure"), [Input("player", "value")])
def update_graph(player):
    chips, hands = [], []
    for (chip, hand_id) in d[player]:
        print(chip, hand_id)
        chips.append(chip)
        hands.append(hand_id)

    df = pd.DataFrame(
        {
            "chips": chips,
            "hand": hands,
            "player": player,
        }
    )

    figure = px.line(df, x="hand", y="chips", title=player)
    figure.data[0].update(mode="markers+lines")
    return figure


if __name__ == "__main__":
    app.run_server(debug=True)
