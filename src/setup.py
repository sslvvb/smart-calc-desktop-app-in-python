"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['app/main.py']
DATA_FILES = [
    ('config', ['app/config/config.yml']),
    ('data', ['app/data/history.txt']),
    ('logs', ['app/logs/logs_15-08-2023-18-50-31.log']),
    ('model/cpp_dynamic_lib', ['app/model/cpp_dynamic_lib/model.so'])
]
OPTIONS = {
    'argv_emulation': False,
    'includes': ['src', 'app', 'model', 'presenter', 'view']
    # 'packages': ['model', 'presenter', 'view'],  # Add your package names
    #     'excludes': ['PyInstaller.hooks.hook-gi.repository.GstMpegts']
    #     # 'PyInstaller.hooks.hook-pandas.plotting', 'PyInstaller.hooks.hook-PyQt6.QtGui',
    #     #              'PyInstaller.hooks.hook-PyQt5.QtScript', ' PyInstaller.hooks.hook-PySide2.QtLocation',
    #     #              'PyInstaller.hooks.hook-PyQt5.QtNfc', ' PyInstaller.hooks.hook-PyQt6.QtTest',
    #     #              'PyInstaller.hooks.hook-gi.repository.GstVulkan', 'PyInstaller.hooks.hook-PySide6.QtLocation']
    #     # 'iconfile': 'path/to/your/app_icon.icns',  # Optional: Path to your app icon
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

# python3 setup.py py2app
