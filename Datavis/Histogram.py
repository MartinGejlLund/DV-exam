import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html

dataframe = pd.read_csv('StudentsPerformance.csv')

dataframe['id'] = [i for i in range(len(dataframe['gender']))]

ethnicity = ['group A', 'group B', 'group C', 'group D', 'group E']
scores = ['math score', 'reading score', 'writing score']

def setLayout(fig):
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=['barmode', 'default'],
                        label='Side by side',
                        method='relayout'
                    ),
                    dict(
                        args=['barmode', 'overlay'],
                        label='Overlay',
                        method='relayout'
                    ),
                    dict(
                        args=['barmode', 'stack'],
                        label='Stacked',
                        method='relayout'
                    )
                ]),
                type='buttons',
                direction='right',
                pad={'r': 10, 't': 10},
                showactive=True,
                x=0,
                xanchor='left',
                y=1.065,
                yanchor='top'
            ),
            dict(
                buttons=list([
                    dict(
                        args=['histnorm', ''],
                        label='Count',
                        method='restyle'
                    ),
                    dict(
                        args=['histnorm', 'percent'],
                        label='Percentage',
                        method='restyle'
                    )
                ]),
                type='buttons',
                direction='right',
                pad={'r': 10, 't': 10},
                showactive=True,
                x=0,
                xanchor='left',
                y=1.1,
                yanchor='top'
            ),
        ]
    )
    fig.update_traces(opacity=0.75)
    return fig

def scoreHistogram():
    df1 = dataframe.copy()
    df1['subject'] = ['mean' for i in df1.gender]
    df1['score'] = dataframe[['math score', 'reading score', 'writing score']].mean(axis=1)

    df2 = dataframe.copy()
    df2['subject'] = ['math' for i in df2.gender]
    df2['score'] = dataframe['math score']

    df3 = dataframe.copy()
    df3['subject'] = ['reading' for i in df3.gender]
    df3['score'] = dataframe['reading score']

    df4 = dataframe.copy()
    df4['subject'] = ['writing' for i in df4.gender]
    df4['score'] = dataframe['writing score']

    df = pd.concat([df1, df2, df3, df4], axis=0, ignore_index=True)
    fig = px.histogram(
        df,
        x='score',
        color='gender',
        facet_col='race/ethnicity',
        facet_row='subject'
    )
    fig = setLayout(fig)
    return fig

def scoreHistogramTotal():
    df = dataframe.copy()
    df['mean score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    fig = px.histogram(
            df,
            x='mean score',
            color='race/ethnicity'
    )
    fig = setLayout(fig)
    return fig

def combinePlots():
    data1 = scoreHistogramTotal()
    data2 = scoreHistogram()
    fig = px.histogram()
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=['type', data1],
                        label='Count',
                        method='update'
                    ),
                    dict(
                        args=['type', data2],
                        label='Percentage',
                        method='update'
                    )
                ]),
                type='buttons',
                direction='right',
                pad={'r': 10, 't': 10},
                showactive=True,
                x=0,
                xanchor='left',
                y=1.135,
                yanchor='top'
            ),
        ]
    )

    return fig

# scoreHistogram().show()
scoreHistogram().write_html('Histogram.html')
# scoreHistogramTotal().show()
# combinePlots().show()