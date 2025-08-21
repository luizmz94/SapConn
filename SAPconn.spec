# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Colete só assets do QDarkStyle (remova se não usar)
qdark_datas = collect_data_files('qdarkstyle')

# Exclua módulos pesados que você não usa (apenas Widgets)
EXCLUDES = [
    'PyQt5.QtQuick', 'PyQt5.QtQml',
    'PyQt5.Qt3DCore', 'PyQt5.Qt3DRender', 'PyQt5.Qt3DInput', 'PyQt5.Qt3DAnimation',
    'PyQt5.QtWebEngineCore', 'PyQt5.QtWebEngineWidgets', 'PyQt5.QtWebEngine',
    'PyQt5.QtGamepad',
]

a = Analysis(
    ['kutapada-desktop/main.py'],
    pathex=['.'],
    binaries=[],               # deixe vazio; hooks do PyInstaller cuidam dos plugins
    datas=qdark_datas,         # se não usa QDarkStyle, pode deixar []
    hiddenimports=[],          # idem: deixe os hooks resolverem
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=EXCLUDES,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SAPconn',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,        # mantenha OFF no macOS
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='SAPconn',
)

app = BUNDLE(
    coll,
    name='SAP Conn.app',
    icon='logo.icns',
    bundle_identifier='io.redware.sapconn',
    info_plist={
        "CFBundleDisplayName": "SAP Conn",
        "NSHighResolutionCapable": True,
    },
)
