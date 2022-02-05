
from flask import jsonify, request
# from variables import *

class RouteHandler:

    def __init__(self, simvars):
        self.simvars = simvars

    def get_data_endpoint(self, datapoint_name):
        
        ds = request.get_json() if request.is_json else request.form
        index = ds.get('index')

        output = self.simvars.get_datapoint(datapoint_name, index)

        if isinstance(output, bytes):
            output = output.decode('ascii')

        return jsonify(output)

    def set_datapoint_endpoint(self, datapoint_name):

        ds = request.get_json() if request.is_json else request.form
        index = ds.get('index')
        value_to_use = ds.get('value')

        status = self.simvars.set_datapoint (datapoint_name, index, value_to_use)

        return jsonify(status)

    def get_json_dataset(self, dataset_name):
        dataset_map = {}

        # This uses get_dataset() to pull in a bunch of different datapoint names into a dictionary which means they can
        # then be requested from the sim
        data_dictionary = get_dataset(dataset_name)

        for datapoint_name in data_dictionary:
            dataset_map[datapoint_name] = aq.get(datapoint_name)

        return jsonify(dataset_map)
