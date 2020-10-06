from dash_elasticsearch_autosuggest import ESAutosuggest
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

# fields=["original", "normalized"]

app.layout = html.Div([
    ESAutosuggest(
        id='input',
        value='',
        endpoint='http://localhost:9200/_search',
        # fields=fields,
        defaultField="autocomplete",
        additionalField=None,
        sort=["_score"],
        placeholder='',
        # suggestions=[], 
        # authUser='user',
        # authPass='pass',
        searchField="autocomplete",
        inputType="textarea",

    ),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=False)

