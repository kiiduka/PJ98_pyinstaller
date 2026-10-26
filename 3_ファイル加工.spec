# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['3_ファイル加工.py'],
    pathex=[],
    binaries=[],

    datas=[ ('../.img/step_import_1.png', '.'),
            ('../.img/step_import_2.png', '.'),
            ('../.img/step_import_3.png', '.'),
            ('../.img/step_import_4.png', '.'),
            ('../.img/step_import_5.png', '.'),
            ('../.img/step_import_6.png', '.'),
            ('../.img/step_import_7.png', '.')
            ],

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
    name='3_ファイル加工',
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
    icon=['../.ico/python-logo-only.ico'],
)
