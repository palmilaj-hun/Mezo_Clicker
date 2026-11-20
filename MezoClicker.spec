# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['clicker_windows.py'],
    pathex=[],
    binaries=[],
    datas=[('bgp.webp', '.'), ('mezoegypedo.wav', '.'), ('mezodeafult.jpg', '.'), ('mezo2.jpg', '.'), ('mezo3.jpg', '.'), ('mezo4.webp', '.'), ('mezo5.jpg', '.'), ('mezo6.jpg', '.'), ('mezo7.jpg', '.'), ('mezo8.png', '.'), ('mezo9.png', '.'), ('mezo10.png', '.'), ('mezo11.png', '.'), ('mezo12.gif', '.'), ('mezo13.png', '.'), ('click_sound.wav', '.')],
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
    a.binaries,
    a.datas,
    [],
    name='MezoClicker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
