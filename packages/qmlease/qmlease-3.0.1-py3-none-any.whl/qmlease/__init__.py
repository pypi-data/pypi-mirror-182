if 1:  # step1: setup lk_logger
    import lk_logger
    lk_logger.setup(quiet=True)

if 2:  # step2: select qt api
    # this should be defined before importing qtpy.
    # refer: [lib:qtpy/__init__.py : docstring]
    import os
    import sys
    from importlib.util import find_spec
    
    api = ''
    if not os.getenv('QT_API'):
        for pkg, api in {
            'PySide6'     : 'pyside6',
            'PyQt6'       : 'pyqt6',
            'PySide2'     : 'pyside2',
            'PyQt5'       : 'pyqt5',
            'pyside6_lite': 'pyside6'
        }.items():
            if find_spec(pkg):
                if pkg == 'pyside6_lite':
                    # see `sidework/pyside_package_tailor/dist/pyside6_lite`.
                    from pyside6_lite import init_paths  # noqa
                    for p in init_paths:
                        sys.path.insert(0, p)
                print(':v2', 'Auto detected Qt API: ' + api)
                os.environ['QT_API'] = api
                break
        else:
            raise ModuleNotFoundError('No Qt bindings found!')
    
    if api == 'pyside2':
        # try to repair pyside2 highdpi issue
        #   https://www.hwang.top/post/pyside2pyqt-zai-windows-zhong-tian-jia
        #   -dui-gao-fen-ping-de-zhi-chi/
        # warning: this must be called before QCoreApplication is created.
        from PySide2 import QtCore  # noqa
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

# -----------------------------------------------------------------------------

from .application import Application
from .application import app
from .pyside import pyside
from .pyside import register
from .qmlside import Model
from .qmlside import eval_js
from .qmlside import pyassets
from .qmlside import qlogger
from .qmlside import qml_eval
from .qmlside.widgets_backend import util
from .qtcore import AutoProp
from .qtcore import QObject
from .qtcore import bind
from .qtcore import bind_signal
from .qtcore import signal
from .qtcore import slot
from .style import pystyle

__version__ = '3.0.0'
