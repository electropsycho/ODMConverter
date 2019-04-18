# -*- mode: python -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Users\\hakan\\PycharmProjects\\ODMConverter'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('filter.ico', 'C:\\Users\\hakan\\PycharmProjects\\ODMConverter\\images\\filter.ico', 'DATA'),
                    ('settings.ico', 'C:\\Users\\hakan\\PycharmProjects\\ODMConverter\\images\\settings.ico', 'DATA'),
                    ('warning.ico', 'C:\\Users\\hakan\\PycharmProjects\\ODMConverter\\images\\warning.ico', 'DATA')]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ODM Donusturucu',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False,
          icon='C:\\Users\\hakan\\PycharmProjects\\ODMConverter\\images\\filter.ico')
