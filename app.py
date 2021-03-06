import sys
import os
import time
import json
import socketio
# import eventlet
from engineio.async_drivers import eventlet
import eventlet.wsgi 
# from gevent import pywsgi
# from geventwebsocket.handler import WebSocketHandler
from datetime import datetime
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
# from flask_socketio import SocketIO, emit, send
from threading import Thread
from SimConnect import *
from PySide6.QtCore import Slot, QSize, Qt, QThreadPool, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout
from simvars import SimVars
from routes import RouteHandler

# Create simconnection
flightsim_is_running = False

# Create flask http
sio = socketio.Server(logger=True, cors_allowed_origins="*", async_mode="eventlet")
http = Flask(__name__)
http.wsgi_app = socketio.WSGIApp(sio, http.wsgi_app)
http.config['SECRET_KEY'] = 'cabeza-polo'
CORS(http)
# socketio = SocketIO(http, cors_allowed_origins="*", engineio_logger=True, async_mode="threading")

try:
    sm = SimConnect()
    ae = AircraftEvents(sm)
    aq = AircraftRequests(sm, _time=10)

    simvars = SimVars(sm, ae, aq, sio)
    http_handler = RouteHandler(simvars)

    flightsim_is_running = True
except (ConnectionError):
    pass

def pollSimConnect(sid):
    print("start sim polling")
    while not sm.quit:
        simvars.polling = True
        dataset_map = simvars.poll_simvars(sid)
        eventlet.sleep(0.33)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

@http.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@http.route('/variables', methods=["GET"])
def get_variables():
    with open(resource_path('variables.json')) as variables_file:
        data = json.load(variables_file)
        return jsonify(data)

@http.route('/data/<dataset_name>', methods=["GET"])
def output_json_dataset(dataset_name):
    return http_handler.get_json_dataset(dataset_name)

# This is the http endpoint wrapper for getting an individual datapoint
@http.route('/get/<datapoint_name>', methods=["GET"])
def get_datapoint_endpoint(datapoint_name):
    return http_handler.get_data_endpoint(datapoint_name)

# This is the http endpoint wrapper for setting a datapoint
@http.route('/set/<datapoint_name>', methods=["POST"])
def set_datapoint_endpoint(datapoint_name):
    return http_handler.set_datapoint_endpoint(datapoint_name)

@sio.event
def handshake(sid, data):
    print("got handshake", data, sid)
    pollSimConnect(sid)

@sio.event
def unsubscribe(sid):
    simvars.unsubscribe()

@sio.event
def get_simvars(sid, data):
    for name in data['variables']:
        simvars.poll_variable(name)

    if not simvars.polling:
        pollSimConnect(sid)

@sio.event
def remove_simvar(sid, data):
    for name in data['variables']:
        simvars.remove_variable(name)

def startFlaskThread():
    eventlet.wsgi.server(eventlet.listen(('', 5000)), http)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.flask = Thread(target = startFlaskThread, args = ())
        self.flask.setDaemon(True)

        self.server_is_started = False
        self.setWindowTitle("Pyro SimConnect")
        self.status_message = QLabel()
        self.status_message.setFixedSize(QSize(400, 40))

        self.button = QPushButton("Connect Pyro")
        self.button.setFixedSize(QSize(400,40))
        self.button.setCheckable(True)
        self.button.clicked.connect(self.open_pyro_app)

        if flightsim_is_running:
            self.status_message.setText("Simulator is running")
            self.start_server()
            
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
    def start_server(self):
        if not self.server_is_started:
            
            self.flask.start()
            self.server_is_started = True
            self.button.setText("Open Pyro EFB")
            self.status_message.setText("Sim is connected: Closing this window will disconnect")

    @Slot()
    def open_pyro_app(self):
        if self.server_is_started:            
            url = QUrl("http://localhost:3000")
            QDesktopServices.openUrl(url)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

if __name__ == "__main__":
    app.exec()