import sys
import os
from flask import Flask, jsonify, render_template, request
import _thread
from threading import Thread
from SimConnect import *
from PySide6.QtCore import Slot, QSize, Qt, QThreadPool
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout
from werkzeug.serving import make_server


# Create simconnection

http = Flask(__name__)

sm = SimConnect()
ae = AircraftEvents(sm)
aq = AircraftRequests(sm, _time=10)

# This function actually does the work of getting an individual datapoint from the sim
def get_datapoint(datapoint_name, index=None):

    if index is not None and ':index' in datapoint_name:
        dp = aq.find(datapoint_name)
        if dp is not None:
            dp.setIndex(int(index))

    return aq.get(datapoint_name)


# This is the http endpoint wrapper for getting an individual datapoint
@http.route('/datapoint/<datapoint_name>/get', methods=["GET"])
def get_datapoint_endpoint(datapoint_name):

    ds = request.get_json() if request.is_json else request.form
    index = ds.get('index')

    output = get_datapoint(datapoint_name, index)

    if isinstance(output, bytes):
        output = output.decode('ascii')

    return jsonify(output)


# This function actually does the work of setting an individual datapoint
def set_datapoint(datapoint_name, index=None, value_to_use=None):

    if index is not None and ':index' in datapoint_name:
        clas = aq.find(datapoint_name)
        if clas is not None:
            clas.setIndex(int(index))

    sent = False
    if value_to_use is None:
        sent = aq.set(datapoint_name, 0)
    else:
        sent = aq.set(datapoint_name, int(value_to_use))

    if sent is True:
        status = "success"
    else:
        status = "Error with sending request: %s" % (datapoint_name)

    return status


# This is the http endpoint wrapper for setting a datapoint
@http.route('/datapoint/<datapoint_name>/set', methods=["POST"])
def set_datapoint_endpoint(datapoint_name):

    ds = request.get_json() if request.is_json else request.form
    index = ds.get('index')
    value_to_use = ds.get('value_to_use')

    status = set_datapoint (datapoint_name, index, value_to_use)

    return jsonify(status)


def flaskThread():
    http.run()

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.flask = Thread(target = flaskThread, args = ())
        self.flask.setDaemon(True)

        self.server_is_started = False
        self.setWindowTitle("Pyro SimConnect")
        self.status_message = QLabel()
        self.status_message.setFixedSize(QSize(400, 40))

        self.button = QPushButton("Connect Pyro")
        self.button.setFixedSize(QSize(400,40))
        self.button.setCheckable(True)
        self.button.clicked.connect(self.start_server)

        if sm.ok:
            self.status_message.setText("Simulator is running")
        else:
            self.button.setEnabled(False)
            self.status_message.setText("Close this window and start your simulator first.")

        layout = QVBoxLayout()
        layout.addWidget(self.status_message)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setFixedSize(QSize(420,100))

        self.setCentralWidget(container)

    @Slot()
    def start_server(self, checked):
        if not self.server_is_started:
            
            self.flask.start()
            self.server_is_started = True
            self.button.setText("Pyro is connected")
            self.status_message.setText("Close this window to disconnect")
            self.button.setEnabled(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

if __name__ == "__main__":
    app.exec()