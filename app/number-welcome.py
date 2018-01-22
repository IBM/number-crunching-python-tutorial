import os

from flask import Flask, jsonify
from flask_restplus import Api, Resource

from src import functions

app = Flask(__name__)
api = Api(app, title='My first Python API', version='1.0', doc='/apidocs/',
          description='A number-crunching API')
my_list = list()


@api.route('/list/print')
@api.doc(description='Print current list.')
class PrintList(Resource):
    def get(self):
        return jsonify(list=my_list)


@api.route('/list/reset')
@api.doc(description='Reset current list.')
class ResetList(Resource):
    def delete(self):
        my_list.clear()
        return jsonify(list=my_list)


@api.route('/list/reverse')
@api.doc(description='Reverse current list.')
class ReverseList(Resource):
    def put(self):
        my_list.reverse()
        return jsonify(list=my_list)


@api.route('/list/sort')
@api.doc(description='Sort current list.')
class SortList(Resource):
    def put(self):
        my_list.sort()
        return jsonify(list=my_list)


@api.route('/list/extend/<string:csv>')
@api.doc(params={'csv': 'Comma-separated integer values.'}, description='Extend current list.')
class ExtendList(Resource):
    def put(self, csv):
        new_list = functions.csv_to_list(csv)
        my_list.extend(new_list)
        return jsonify(list=my_list)


@api.route('/list/replace/<string:csv>')
@api.doc(params={'csv': 'Comma-separated integer values.'}, description='Replace current list.')
class ReplaceList(Resource):
    def post(self, csv):
        new_list = functions.csv_to_list(csv)
        my_list.clear()
        my_list.extend(new_list)
        return jsonify(list=my_list)


@api.route('/list/mean')
@api.doc(description='Mean of current list.')
class CalculateMean(Resource):
    def get(self):
        my_mean = functions.calculate_mean(my_list)
        return jsonify(mean=my_mean)


@api.route('/list/histogram')
@api.doc(description='Histogram of current list.')
class CalculateHistogram(Resource):
    def get(self):
        my_url = functions.plot_histogram(my_list)
        return jsonify(URL=my_url)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
