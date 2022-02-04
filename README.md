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

# build an exe

Notes on building the .exe 

`rename SimConnect.dll to SimConnect.dllc`
`py -m PyInstaller -F --onefile --name="PyroSimConnect" --add-data "SimConnect;SimConnect" --windowed app.py`