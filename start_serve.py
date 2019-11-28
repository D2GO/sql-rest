from flask import Flask
from flask_restful import Api
from App.config import get_port, get_loc
import App.views as ve


port = get_port()
loc = get_loc()

app = Flask(import_name=__name__, template_folder=loc)
api = Api(app)

api.add_resource(ve.index, '/index')
api.add_resource(ve.rest_sql, '/_QUERIES/<folder_>/<file_>')
api.add_resource(ve.rest_uri, '/<database_>/<schema_>/<table_>')

if __name__ == '__main__':
    app.run(debug=True, port=port)