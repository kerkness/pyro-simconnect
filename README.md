# Pyro SimConnect

Local SimConnect API server for Pyro-EFB. 

Special thanks to Python-SimConnect
https://github.com/odwdinc/Python-SimConnect


## Development install

Python-SimConnect is manually added. So if there are updates to that library, and update here is needed.

## Requirements

Loosly keeping track of python modules required to build the app

`pip install PyQt6 --user`
`pip install flask --user`
`pip install PySide6 --user`
`pip install flask-cors --user`
`pip install pyinstaller --user`
`pip install flask-socketio --user`
`pip install eventlet --user`

# build an exe

Building the exe requires a bunch of dependcies.. see `hidden imports` and `datas` in spec file


Build with options (see spec file for all hidden import dependencies)
`py -m PyInstaller -F --onefile --name="PyroSimConnect" --hidden-import "eventlet.hubs.epolls" --hidden-import "eventlet.hubs.kqueue" --hidden-import "eventlet.hubs.selects" --hidden-import "dns" --hidden-import "dns.asyncbackend" --add-data "SimConnect;SimConnect" --add-data "variables" --windowed app.py`

Build using Spec
`py -m PyInstaller PyroSimConnect.spec`

This example is useful
https://github.com/miguelgrinberg/python-socketio/blob/main/examples/server/wsgi/app.py