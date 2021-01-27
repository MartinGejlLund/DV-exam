import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

dataframe = pd.read_csv('StudentsPerformance.csv')

fig = make_subplots(
    rows=3,
    cols=1,
    vertical_spacing=0.07,
    horizontal_spacing=0.07,
    shared_xaxes=True
)

scores = ['math score', 'reading score', 'writing score']

nn = 1
for ii in scores:
    if ii == 'math score':
        showLegend = True
    else:
        showLegend = False
    fig.add_trace(
        go.Violin(
            x=dataframe['race/ethnicity'],
            y=dataframe[ii],
            box_visible=True,
            meanline_visible=True,
            legendgroup='Total',
            scalegroup='Total',
            name='Total',
            line_color='Green',
            showlegend=showLegend,
            visible=True
        ),
        row=nn,
        col=1
    )
    fig.add_trace(
        go.Violin(
            x=dataframe['race/ethnicity'][dataframe['gender'] == 'male'],
            y=dataframe[ii][dataframe['gender'] == 'male'],
            box_visible=True,
            meanline_visible=True,
            legendgroup='Male',
            scalegroup='Male',
            name='Male',
            side='negative',
            line_color='red',
            showlegend=showLegend,
            visible=False
        ),
        row=nn,
        col=1
    )
    fig.add_trace(
        go.Violin(
            x=dataframe['race/ethnicity'][dataframe['gender'] == 'female'],
            y=dataframe[ii][dataframe['gender'] == 'female'],
            box_visible=True,
            meanline_visible=True,
            legendgroup='Female',
            scalegroup='Female',
            name='Female',
            side='positive',
            line_color='blue',
            showlegend=showLegend,
            visible=False
        ),
        row=nn,
        col=1
    )
    fig.update_yaxes(
        title_text=ii,
        row=nn,
        col=1
    )
    nn += 1

fig.update_layout(
    title='Score distributions of the different ethnic groups',
    yaxis2_matches='y1',
    yaxis3_matches='y2',
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=[{'visible': [True, False, False]}],
                    label='Display total',
                    method='update'
                ),
                dict(
                    args=[{'visible': [False, True, True]}],
                    label='Display by Gender',
                    method='update'
                )
            ]),
            type='buttons',
            direction='right',
            pad={'r': 10, 't': 10},
            showactive=True,
            x=.45,
            xanchor='left',
            y=1.05,
            yanchor='bottom'
        ),
    ]
)

fig.show()
fig.write_html('ViolinPlot.html')
fig.write_image('ViolinPlot.png', width=1200, height=720, scale=1)