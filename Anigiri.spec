# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['codigo.py'],
    pathex=[],
    binaries=[],
    datas=[('Resources/*', 'Resources'), ('Model/*', 'Model'), ('Repository/*', 'Repository'), ('Screens/*', 'Screens'), ('Ui/*', 'Ui'), ('Utils/*', 'Utils'), ('default.db', '.'), ('SQL/*', 'SQL'), ('Config/*', 'Config')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Anigiri',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Resources\\logoAnigiri.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Anigiri',
)
