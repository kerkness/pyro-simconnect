# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['app.py'],
             pathex=[],
             binaries=[],
             datas=[('SimConnect', 'SimConnect'), ('variables.json', '.')],
             hiddenimports=[
                 'engineio.async_eventlet',
                 'eventlet.hubs.epolls',
                 'eventlet.hubs.kqueue',
                 'eventlet.hubs.selects',
                 'dns', 
                 'dns.asyncbackend', 
                 'dns.asyncquery', 
                 'dns.asyncresolver', 
                 'dns.e164', 
                 'dns.hash',
                 'dns.namedict', 
                 'dns.tsigkeyring',
                 'dns.update', 
                 'dns.version',
                 'dns.zone', 
                 'dns.versioned',
                 ],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='PyroSimConnect',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
