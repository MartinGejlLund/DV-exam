import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

dataframe = pd.read_csv('StudentsPerformance.csv')

colors = [
    '#BB68FE',
    '#7A2BBB',
    '#47166F',
    '#220F33',
    '#030204'
]
# {
#     'group A': '#BB68FE',
#     'group B': '#7A2BBB',
#     'group C': '#47166F',
#     'group D': '#220F33',
#     'group E': '#030204'
# }
fig = make_subplots(
    rows=3,
    cols=1,
    vertical_spacing=0.07,
    horizontal_spacing=0.07,
    shared_xaxes=True
)

fig.add_trace(
    go.Box(
        x=[dataframe['race/ethnicity'],dataframe['gender']],
        y=dataframe['math score']
        # yaxis_title='math score'
    ),
    row=1,
    col=1
)

fig.add_trace(
    go.Box(
        x=[dataframe['race/ethnicity'],dataframe['gender']],
        y=dataframe['reading score']
    ),
    row=2,
    col=1
)

fig.add_trace(
    go.Box(
        x=[dataframe['race/ethnicity'],dataframe['gender']],
        y=dataframe['writing score']
    ),
    row=3,
    col=1
)

fig.update_yaxes(
    title_text="math score",
    row=1,
    col=1
)

fig.update_yaxes(
    title_text="reading score",
    row=2,
    col=1
)

fig.update_yaxes(
    title_text="writing score",
    row=3,
    col=1
)

# fig.show()
fig.write_html('bp.html')