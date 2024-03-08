import pandas as pd
import numpy as np
import dash 
import dash_html_components as html
import dash_core_components as dcc 
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

from main import *

app = dash.Dash( __name__)
server = app.server
app.title = 'Poetry Data Analysis'
colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}


app.layout = html.Div(
    className = 'main_block',
    #style={'backgroundColor': colors['background']},  
    children = [ #Time-series Analysis
                #Individual Analysis
        html.H1(children = 'Sales Time-Series Analysis',
                style = {
                    'textAlign': 'center',
                    'color': colors['text']}),
        html.P(
            children = "Analyzing the behavior of Poetry books' sales on a monthly "
            "or a weekly basis",
            style = {
                'color': colors['text']
            }
        ),
        html.Div([
            dcc.Dropdown(
            id = 'timeseries_dropdown',
            options = [{"label": x, "value": x}
                    for x in np.arange(2016,2022)],
            value = 2016,
            clearable = False,
        ),
            dcc.RadioItems(
                id='timeseries_radio',
                options = [
                        {'label': 'Weekly', 'value': 'Weekly'},
                        {'label': 'Monthly', 'value': 'Monthly'}
                        ],
                value = 'Monthly'
            ),
            dcc.RadioItems(
                id = 'rupi_kaur_tsa',
                options = [
                        {'label': 'Without Rupi Kaur', 'value': '!rupi_kaur'},
                        {'label': 'With Rupi Kaur', 'value': 'rupi_kaur'}],
                value = 'rupi_kaur'
                
            ),
        dcc.Graph(id = 'time-series'),
    ]),
        #Comparisons on a time-series chart
        html.Div([
            html.H1(children = 'Comparing different monthly sales',
                    style = {
                            'textAlign': 'center',
                            'color': colors['text']
                            }),
            dcc.Checklist(
                        id='year_compare_checklist',
                        options = [
                            {'label': year, 'value': year}
                            for year in np.arange(2016,2022)
                            ],
                        value = [2016]
                        ),
            dcc.RadioItems(
                id = 'rupi_kaur_yc',
                options = [
                        {'label': 'Without Rupi Kaur', 'value': '!rupi_kaur'},
                        {'label': 'With Rupi Kaur', 'value': 'rupi_kaur'}],
                value = 'rupi_kaur'
                
            ),
            dcc.RadioItems(
                id='yc_radio',
                options = [
                        {'label': 'Weekly', 'value': 'Weekly'},
                        {'label': 'Monthly', 'value': 'Monthly'}
                        ],
                value = 'Monthly'
            ),
            dcc.Graph(id='yearly_compare'),
        ]),
        #Market Shares
        html.Div([
            html.H1(children = 'Market shares',
                    style={
                        'textAlign': 'center',
                        'color': colors['text']
                        }),
            dcc.Dropdown(
                id='shares_dropdown',
                options = [
                    {'label': 'Author', 'value': 'Author'},
                    {'label': 'Book', 'value': 'Title'}
                ],
                value = 'Author',
                clearable = False
            ),
            dcc.RadioItems(
                id='shares_radio',
                options = [
                    {'label': year, 'value': year}
                    for year in np.arange(2016,2022)
                ],
                value = 2020
            ),
            dcc.RadioItems(
                id = 'shares_top',
                options = [
                    {'label': 'Top 10', 'value': 'Top 10'},
                    {'label': 'Top 5', 'value': 'Top 5'}
                ],  
                value = 'Top 5'
            ),
            dcc.RadioItems(
                id = 'rupi_kaur_ms',
                options = [
                        {'label': 'Without Rupi Kaur', 'value': '!rupi_kaur'},
                        {'label': 'With Rupi Kaur', 'value': 'rupi_kaur'}],
                value = 'rupi_kaur'
                
            ),
            dcc.Graph(id = 'Market_shares')
        ]),
        html.Div([
            html.H1(children = 'Monthly performance of 2021 against the average',
                    style = {
                        'textAlign': 'center',
                        'color': colors['text']
                    }),
            dcc.RadioItems(
                id = 'rupi_kaur_2021_per',
                options = [
                        {'label': 'Without Rupi Kaur', 'value': '!rupi_kaur'},
                        {'label': 'With Rupi Kaur', 'value': 'rupi_kaur'}],
                value = 'rupi_kaur'
                
            ),
            dcc.Graph(
                id='sales_2021_performance_m'),
        ]),
        html.Div([
            html.H1(children = 'Weekly performance of 2021 against the average',
                    style = {
                        'textAlign': 'center',
                        'color': colors['text']
                    }),
            dcc.RadioItems(
                id = 'rupi_kaur_2021_per_w',
                options = [
                        {'label': 'Without Rupi Kaur', 'value': '!rupi_kaur'},
                        {'label': 'With Rupi Kaur', 'value': 'rupi_kaur'}],
                value = 'rupi_kaur'
                
            ),
            dcc.Graph(id='sales_2021_performance_w'),
    ]
)
]
)


@app.callback(
    Output("time-series", "figure"),
    [Input("timeseries_dropdown", "value"),
    Input("timeseries_radio", "value"),
    Input("rupi_kaur_tsa", "value")
    ]
)

def display_time_series(timeseries_dropdown, timeseries_radio, rupi_kaur_tsa):
        
    if timeseries_radio == 'Weekly':
        fig = px.line(sales[rupi_kaur_tsa][timeseries_radio][timeseries_dropdown], 
                    x=sales[rupi_kaur_tsa][timeseries_radio][timeseries_dropdown].index, 
                    y='Total Sales',
                template = 'plotly_dark',
                )
    if timeseries_radio == 'Monthly':
        if timeseries_dropdown == 2021:
            months_2021 = months[0:sales_2021.index[-1]]
            fig = px.line(sales[rupi_kaur_tsa][timeseries_radio][timeseries_dropdown], x=months_2021, y='Total Sales',
                template = 'plotly_dark',
                labels = {
                    'x': 'Month'
                })
        else:
            #months=months    
            fig = px.line(sales[rupi_kaur_tsa][timeseries_radio][timeseries_dropdown], x=months, y='Total Sales',
                template = 'plotly_dark',
                labels = {
                    'x': 'Month'
                })
    maximum = int(sales[rupi_kaur_tsa][timeseries_radio][timeseries_dropdown].max())
    fig.update_yaxes(range=[0, maximum])
    return fig

@app.callback(
    Output('yearly_compare', 'figure'),
    [Input('year_compare_checklist', 'value'),
    Input('rupi_kaur_yc', 'value'),
    Input('yc_radio', 'value')]
)

def update_graph(year_compare_checklist, rupi_kaur_yc, yc_radio):
    colors = {
    2016: '#FF617A',
    2017: '#9154E3',
    2018: '#68BDFA',
    2019: '#54E38A',
    2020: '#E4FB5D',
    2021: '#D2D6D9',
    #'#ed7391'
}
    if yc_radio == 'Monthly':
        fig = go.Figure()
        fig.update_layout(template = 'plotly_dark', 
                        xaxis_title = "Month")
        for x in year_compare_checklist:  
            df = sales[rupi_kaur_yc]['Monthly'][x]
            fig.add_trace(go.Scatter(x=months, y=df['Total Sales'], mode='lines', 
                                    name=f'Total Sales {x}', line_color=colors[x], showlegend=True))
    elif yc_radio == 'Weekly':
        fig = go.Figure()
        fig.update_layout(template = 'plotly_dark', 
                        xaxis_title = "Week")
        for x in year_compare_checklist:  
            df = sales_weekly_yc[rupi_kaur_yc][x]
            weeks = [f'Week {int(x)}' for x in df.index]
            fig.add_trace(go.Scatter(x=weeks, y=df['Total Sales'], mode='lines', 
                                    name=f'Total Sales {x}', line_color=colors[x], showlegend=True))
    return fig

@app.callback(
    Output('Market_shares', 'figure'),
    [
    Input('shares_dropdown', 'value'),
    Input('shares_top', 'value'),
    Input('shares_radio', 'value'),
    Input('rupi_kaur_ms', 'value')
    ]
)

def market_share(shares_dropdown, shares_top, shares_radio, rupi_kaur_ms):
    df = market_shares[rupi_kaur_ms][shares_dropdown][shares_top][shares_radio]
    fig = px.pie(df, values = 'Total Sales', names = df[shares_dropdown],
                title = f'{shares_top} {shares_dropdown} market shares for {shares_radio}',
                color_discrete_sequence=px.colors.sequential.Mint,
                template = 'plotly_dark')
    fig.update_traces(textposition='inside', textinfo='value+label', sort=False, rotation = -90)
    fig.update_layout(uniformtext_minsize=12, legend_traceorder="normal")
    return fig


@app.callback(
    Output('sales_2021_performance_m', 'figure'),
    Input('rupi_kaur_2021_per', 'value')
)
def sales_2021_avg(rupi_kaur_2021_per):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x = months,
        y = sales_2021_vs_avg[rupi_kaur_2021_per].iloc[0],
        name = 'Average Sales 2016:2020',
        marker_color = '#bd8de3'
    ))
    fig.add_trace(go.Bar(
        x=months,
        y=sales_2021_vs_avg[rupi_kaur_2021_per].iloc[1],
        name = '2021 sales',
        marker_color = '#60b802'
    ))
    fig.update_layout(barmode='group', xaxis_tickangle=-45, template='plotly_dark',
                    xaxis_title = "Month", yaxis_title = "Total Sales")
    return fig

@app.callback(
    Output('sales_2021_performance_w', 'figure'),
    Input('rupi_kaur_2021_per_w', 'value')
)

def sales_2021_avg_w(rupi_kaur_2021_per_w):
    df = sales_2021_vs_avg_weekly[rupi_kaur_2021_per_w]
    df.columns = [f'Week {i}' for i in range(0,54)]
    fig = go.Figure()
    fig.update_layout(template = 'plotly_dark', 
                    xaxis_title = "Week")
    fig.add_trace(go.Scatter(x=df.columns, y=df.iloc[0], mode='lines', name = 'Average Sales',
                            line_color = '#bd8de3'))
    fig.add_trace(go.Scatter(x=df.columns, y=df.iloc[1], mode='lines', name='2021 Sales',
                            line_color = '#60b802'))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)


