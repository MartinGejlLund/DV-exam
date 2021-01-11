import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

dataframe = pd.read_csv('StudentsPerformance.csv')
fig = make_subplots(
    rows=2,
    cols=2,
    row_heights=[0.2, 0.8],
    column_widths=[0.8, 0.2],
    vertical_spacing=0.07,
    horizontal_spacing=0.07,
    shared_xaxes=True,
    shared_yaxes=True
)

math_score = [0, 0, 0, 0, 0]
reading_score = [0, 0, 0, 0, 0]
writing_score = [0, 0, 0, 0, 0]
data = [math_score, reading_score, writing_score]

dataframe['group A'] = [1 if i == 'group A' else None for i in dataframe['race/ethnicity']]
dataframe['group B'] = [1 if i == 'group B' else None for i in dataframe['race/ethnicity']]
dataframe['group C'] = [1 if i == 'group C' else None for i in dataframe['race/ethnicity']]
dataframe['group D'] = [1 if i == 'group D' else None for i in dataframe['race/ethnicity']]
dataframe['group E'] = [1 if i == 'group E' else None for i in dataframe['race/ethnicity']]

ethnicity = ['group A', 'group B', 'group C', 'group D', 'group E']

for i in range(len(math_score)):
    math_score[i] = dataframe['math score'].loc[dataframe[ethnicity[i]] == 1].mean()
    reading_score[i] = dataframe['reading score'].loc[dataframe[ethnicity[i]] == 1].mean()
    writing_score[i] = dataframe['writing score'].loc[dataframe[ethnicity[i]] == 1].mean()

fig.add_trace(
    go.Heatmap(
        x=dataframe.columns[-5:],
        y=dataframe.columns[-8:-5],
        z=data,
        colorscale='viridis'
    ),
    row=2,
    col=1
)
fig.add_trace(
    go.Histogram(
        x=dataframe['race/ethnicity']
    ),
    row=1,
    col=1
)
fig.add_trace(
    go.Bar(
        x=[dataframe['math score'].mean(), dataframe['reading score'].mean(), dataframe['writing score'].mean()],
        y=dataframe.columns[-8:-5],
        orientation='h'
    ),
    row=2,
    col=2
)

# app = dash.Dash(__name__)
# app.layout = html.Div([
#     dcc.Graph(figure=fig),
# ])
#
# app.run_server(debug=True)

# fig.show()
fig.write_html('hm.html')