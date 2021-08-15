# Import <
import dash
from time import sleep
import dash_table as dt
from Serra import jsonLoad
from os import listdir, getcwd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# >


# Declaration <
app = dash.Dash()
server = app.server
path = getcwd()[:-6]
setting = jsonLoad(f'{path}/Resources/Front')

# >


# Dashboard <
app.layout = html.Div([

    # Header <
    html.Div([

        html.H1(children = 'Serra',
                style = setting['h1Style'])

    ], style = setting['divStyle']),

    # >

    # Dropdown <
    html.Div([

        dcc.Dropdown(id = 'dropdownId',
                     style = setting['dropdownStyle'],
                     options = [{'label' : i,
                                 'value' : i}

                                for i in [i[:-5] for i in listdir(f'{path}/Data')]

        ])

    ], style = setting['divStyle']),

    # >

    # DataTable <
    html.Div(id = 'datatableId',
             style = setting['divStyle']),

    # >

])

# >


@app.callback(Output('datatableId', 'children'),
              Input('dropdownId', 'value'))
def dropdownFunction(arg):
    '''  '''

    print('ok')

    return dt.DataTable(sort_action = 'native',
                        data = jsonLoad(f'{path}/Data/{arg}'),
                        columns = [{'name' : i,
                                    'id' : i}

                                   for i in setting['datatableColumn']])


# Run <
while (True):

    app.run_server(debug = True)
    sleep(3600)

# >
