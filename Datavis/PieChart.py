import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

dataframe = pd.read_csv('StudentsPerformance.csv')

dataframe['id'] = [i for i in range(len(dataframe['gender']))]

ethnicity = ['group A', 'group B', 'group C', 'group D', 'group E']
subjects = ['math score', 'reading score', 'writing score']
gender = ['female', 'male', 'total']

columns = {
    'ethnicity': [np.nan] * 15,
    'gender': [np.nan] * 15,
    'count': [np.nan] * 15,
    'math score': [np.nan] * 15,
    'reading score': [np.nan] * 15,
    'writing score': [np.nan] * 15,
    'overall score': [np.nan] * 15,
}

df = pd.DataFrame(
    columns
)

nn = 0

for ii in range(len(ethnicity)):
    tmpDF1 = dataframe.copy()
    tmpDF1 = tmpDF1.loc[tmpDF1['race/ethnicity'] == ethnicity[ii]]
    for jj in range(len(gender)):
        nn = jj + ii * (len(gender))
        df['ethnicity'][nn] = ethnicity[ii]
        df['gender'][nn] = gender[jj]
        if gender[jj] != 'total':
            tmpDF2 = tmpDF1.copy()
            tmpDF2 = tmpDF2.loc[tmpDF2['gender'] == gender[jj]]
        else:
            tmpDF2 = tmpDF1.copy()
        df['count'][nn] = tmpDF2['gender'].count()
        for kk in subjects:
            df[kk][nn] = tmpDF2[kk].mean()

df['overall score'] = dataframe[subjects].mean(axis=1)


def createPie():
    df2 = df.copy()
    df2 = df2.loc[df2['gender'] == 'male']

    df3 = df.copy()
    df3 = df3.loc[df3['gender'] == 'female']

    fig = make_subplots(
        rows=3,
        cols=2,
        vertical_spacing=0.07,
        horizontal_spacing=0.07,
        specs=[[{'type': 'domain'}, {'type': 'domain'}],
               [{'type': 'domain'}, {'type': 'domain'}],
               [{'type': 'domain'}, {'type': 'domain'}]],
        subplot_titles=['Distribution of student count by ethnicity',
                        'Distribution of student mean of scores by ethnicity',
                        'Distribution of male student count by ethnicity',
                        'Distribution of male mean of scores by ethnicity',
                        'Distribution of female student count by ethnicity',
                        'Distribution of female mean of scores by ethnicity']
    )
    fig.add_trace(
        go.Pie(
            labels=df['ethnicity'],
            values=df['count'],
            name='Count',
            sort=False
        ),
        row=1,
        col=1
    )
    fig.add_trace(
        go.Pie(
            labels=df['ethnicity'],
            values=df['overall score'],
            name='Mean of scores',
            sort=False
        ),
        row=1,
        col=2
    )
    fig.add_trace(
        go.Pie(
            labels=df2['ethnicity'],
            values=df2['count'],
            name='Count',
            sort=False
        ),
        row=2,
        col=1
    )
    fig.add_trace(
        go.Pie(
            labels=df2['ethnicity'],
            values=df2['overall score'],
            name='Mean of scores',
            sort=False
        ),
        row=2,
        col=2
    )
    fig.add_trace(
        go.Pie(
            labels=df3['ethnicity'],
            values=df3['count'],
            name='Count',
            sort=False
        ),
        row=3,
        col=1
    )
    fig.add_trace(
        go.Pie(
            labels=df3['ethnicity'],
            values=df3['overall score'],
            name='Mean of scores',
            sort=False
        ),
        row=3,
        col=2
    )
    return fig


createPie().show()
createPie().write_html('PieChart.html')
createPie().write_image('PieChart.png', width=720, height=720, scale=1)
