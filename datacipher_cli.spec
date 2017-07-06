# -*- mode: python -*-

block_cipher = None


a = Analysis(['datacipher_cli.py'],
             pathex=['/home/s8a/Programs/datacipher'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='datacipher_cli',
          debug=False,
          strip=False,
          upx=True,
          console=True )
