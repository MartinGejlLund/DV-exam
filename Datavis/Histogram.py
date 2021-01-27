import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
                        args=['barmode', 'stack'],
                        label='Barmode: stacked',
                        method='relayout'
                    ),
                    dict(
                        args=['barmode', 'overlay'],
                        label='Barmode: sverlay',
                        method='relayout'
                    ),
                    dict(
                        args=['barmode', 'default'],
                        label='Barmode: side by side',
                        method='relayout'
                    )
                ]),
                type='buttons',
                direction='right',
                pad={'r': 10, 't': 10},
                showactive=True,
                x=.7,
                xanchor='right',
                y=1.05,
                yanchor='bottom'
            ),
            dict(
                buttons=list([
                    dict(
                        args=[{'histnorm': '', 'labels': {'percentage': 'count'}}],
                        label='Switch y to count',
                        method='restyle'
                    ),
                    dict(
                        args=[{'histnorm': 'percent', 'labels': {'count': 'percentage'}}],
                        label='Switch y to percentage',
                        method='restyle'
                    )
                ]),
                type='buttons',
                direction='right',
                pad={'r': 10, 't': 10},
                showactive=True,
                x=.7,
                xanchor='left',
                y=1.05,
                yanchor='bottom'
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
        facet_row='subject',
        title='Histogram of score distributions'
    )
    fig = setLayout(fig)
    return fig


def scoreHistogramTotal():
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
        color='blue',
        facet_col='race/ethnicity',
        facet_row='subject'
    )
    fig = setLayout(fig)
    return fig


def combinePlots():
    data1 = scoreHistogramTotal()
    data2 = scoreHistogram()
    fig = go.Figure()
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=['visible', data1],
                        label='Count',
                        method='update'
                    ),
                    dict(
                        args=['visible', data2],
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


scoreHistogram().show()
scoreHistogram().write_html('Histogram.html')
scoreHistogram().write_image('Histogram.png', width=1200, height=720, scale=1)
# scoreHistogramTotal().show()
# scoreHistogramTotal().write_html('HistogramTotal.html')
# combinePlots().show()
