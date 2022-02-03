# Pyro SimConnect

Local SimConnect API server for Pyro-EFB. 

Special thanks to Python-SimConnect
https://github.com/odwdinc/Python-SimConnect


## Development install

```
cd Python-SimConnect
pip install -e .
```

## Requirements

`pip install PyQt6 --user`
`pip install flask --user`
`pip install PySide6 --user`
`pip install pyinstaller --user`

# build an exe

`rename SimConnect.dll to SimConnect.dllc`
`py -m PyInstaller -F --onefile --name="PyroSimConnect" --windowed pyro-simconnect.py --add-data "Python-SimConnect;SimConnect"`