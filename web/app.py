import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.express as px

from poker.parsers.pokernow.parser import parse_game

# You'll have to hardcode this in for now
log_file_path = "/mnt/c/Users/Owen Mitchell/Desktop/Files/Poker/Game Logs/poker_now_log_d3SCENVxPZYrYHLhpKrxi_FBu.csv"
game_data = open(log_file_path).read()

# TODO Implement multiple games
game = parse_game(game_data)

chips_hand_by_player = {}
chips_all_players = {}
chips_all_players["hand"] = []


# test

for hand in game.hands:
    chips_all_players["hand"].append(hand.id)
    away_players = list(chips_hand_by_player.keys())
    for (player, stack) in hand.stacks:
        if player.name not in chips_hand_by_player:
            chips_hand_by_player[player.name] = []
        else:
            away_players.remove(player.name)
        chips_hand_by_player[player.name].append((stack, hand.id))

plist = list(chips_hand_by_player.keys())
options = []
data_by_player = {}
data = []

for player in plist:

    chips = []
    hands = []
    for (c, h) in chips_hand_by_player[player]:
        chips.append(c)
        hands.append(h)

    player_data = {
        "y": chips,
        "x": hands,
        "name": player,
        "type": "line",
    }

    data_by_player[player] = player_data
    data.append(player_data)
    options.append({"label": player, "value": player})


options.append({"label": "all", "value": "all"})

figure = {"data": data, "layout": {"title": "Chips by Hand"}}
app = dash.Dash("Pyker")
app.layout = html.Div(
    [
        dcc.Dropdown(id="player", options=options, value="all"),
        dcc.Graph(id="my-graph", figure=figure),
    ],
    style={"width": "500"},
)


@app.callback(Output("my-graph", "figure"), [Input("player", "value")])
def update_graph(player):
    print(player)
    if player == "all":
        d = data

    else:
        d = [data_by_player[player]]
        print(d)
    figure = {"data": d, "layout": {"title": "Chips by Hand"}}
    return figure


if __name__ == "__main__":
    app.run_server(debug=True)
