# from flask_socketio import emit, send

class SimVars:

    def __init__(self, sm, ae, aq, sio):
        self.sm = sm
        self.ae = ae
        self.aq = aq
        self.connected = True
        self.simvars = {}
        self.polling = False
        self.sio = sio

    def unsubscribe(self):
        self.simvars = {}

    def poll_variable(self, name):
        if name in list(self.simvars):
            pass            
        self.simvars[name] = ''

    def remove_variable(self, name):
        if name in list(self.simvars):
            del self.simvars[name]

    def get_variables(self):
        return list(self.simvars)

    def has_updated(self, name, value):
        if not name in list(self.simvars):
            return True

        return self.simvars[name] != value

    def update_variable(self, name, value):
        self.simvars[name] = value

    def get_datapoint(self, datapoint_name, index=None):

        if index is not None and ':index' in datapoint_name:
            dp = self.aq.find(datapoint_name)
            if dp is not None:
                dp.setIndex(int(index))

        return self.aq.get(datapoint_name)

    # This function actually does the work of setting an individual datapoint
    def set_datapoint(self, datapoint_name, index=None, value_to_use=None):

        if index is not None and ':index' in datapoint_name:
            clas = self.aq.find(datapoint_name)
            if clas is not None:
                clas.setIndex(int(index))

        sent = False
        if value_to_use is None:
            sent = self.aq.set(datapoint_name, 0)
        else:
            sent = self.aq.set(datapoint_name, int(value_to_use))

        if sent is True:
            status = "success"
        else:
            status = "Error with sending request: %s" % (datapoint_name)

        return status

    def poll_simvars(self, sid):
        variables = self.get_variables()
        return self.get_data_map(variables, sid)

    def get_data_map(self, variables_dict, sid):

        dataset_map = {}

        for datapoint_name in variables_dict:
            dataset_map[datapoint_name] = self.aq.get(datapoint_name)
            value = self.aq.get(datapoint_name)
            if self.has_updated(datapoint_name, value):
                updates = {}
                updates[datapoint_name] = value
                self.update_variable(datapoint_name, value)
                self.sio.emit('simVarResponse', updates, room=sid)

        return dataset_map

