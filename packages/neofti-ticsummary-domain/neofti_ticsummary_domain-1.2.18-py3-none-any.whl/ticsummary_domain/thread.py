from PyQt6 import QtCore

threadPool = QtCore.QThreadPool.globalInstance()
threadPool.setMaxThreadCount(60)