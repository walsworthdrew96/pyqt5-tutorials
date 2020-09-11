from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

# application
app = QApplication([])
# view
view = QQuickView()
# url
url = QUrl("view.qml")

# change the view's source to the QUrl object
view.setSource(url)
# show the view.
view.show()
# execute the application
app.exec_()