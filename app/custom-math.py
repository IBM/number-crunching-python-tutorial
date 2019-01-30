from server import api
from flask import jsonify
from flask_restplus import Resource
from server.services import math_services as ms

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
        new_list = ms.csv_to_list(csv)
        my_list.extend(new_list)
        return jsonify(list=my_list)


@api.route('/list/replace/<string:csv>')
@api.doc(params={'csv': 'Comma-separated integer values.'}, description='Replace current list.')
class ReplaceList(Resource):
    def post(self, csv):
        new_list = ms.csv_to_list(csv)
        my_list.clear()
        my_list.extend(new_list)
        return jsonify(list=my_list)


@api.route('/list/mean')
@api.doc(description='Mean of current list.')
class CalculateMean(Resource):
    def get(self):
        my_mean = ms.calculate_mean(my_list)
        return jsonify(mean=my_mean)
