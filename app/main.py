import sys, staticfile as sfile
from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QPushButton, QMainWindow, QMenuBar, QMenu, QToolBar, QTableView, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction
import database as db


# window = QWidget()
# window.setWindowTitle('Test PyQT App')
# window.setGeometry(100,100,180,80)
# window.move(60,15)
# helloMsg = QLabel('<h1>Hello PyQT app</h1>',parent=window)
# helloMsg.move(60,15)




class MainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self._initUi()
        self._createActions()
        self._createMenuBar()
        self._createToolBar()

    def _initUi(self):
        self.setGeometry(0,0,800,600)
        self.setWindowTitle('Library Managment System')
        self.setWindowIcon(QIcon(sfile.WINDOW_ICON))
        self.centralWidget = UserTable(DATA)
        #self.centralWidget.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter)
        self.setCentralWidget(self.centralWidget)

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        fileMenu = QMenu("&File",self)
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        editMenu = QMenu("&Edit",self)
        dataMenu = QMenu("&Data",self)
        helpMenu = QMenu("&Help",self) 
        menuBar.addMenu(fileMenu)
        menuBar.addMenu(editMenu)
        menuBar.addMenu(dataMenu)
        menuBar.addMenu(helpMenu)


    def _createToolBar(self):
        NavBar = QToolBar("Nav", self)
        NavBar.addAction(self.users)
        NavBar.addAction(self.books)
        NavBar.addAction(self.borrows)
        
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea,NavBar)

        ToolBar = QToolBar("Tools", self)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea,ToolBar)


    def _createActions(self):
        self.newAction = QAction("&New",self)
        self.openAction = QAction("&Open...",self)
        self.saveAction = QAction("&Save",self)
        self.exitAction = QAction("&Exit",self)

        self.users = QAction(QIcon(sfile.USERS_ICON),"Users",self)
        self.users.triggered.connect(self.clicked_users_btn)

        self.books = QAction(QIcon(sfile.BOOKS_ICON),"Books",self)
        self.books.triggered.connect(self.clicked_books_btn)

        self.borrows = QAction(QIcon(sfile.BORROWS_ICON),"Borrows",self)
        self.borrows.triggered.connect(self.clicked_borrows_btn)

    def clicked_users_btn(self):
        print("Users")
        
    def clicked_books_btn(self):
        print("books")

    def clicked_borrows_btn(self):
        print("borrows")


DATA = {
    f'col{i}': [f'{i * j}' for j in range(1, 10)] for i in range(1, 10)
}


class UserTable(QTableWidget):
    def __init__(self,d):
        print(DATA)
        m = len(d[next(iter(d))])
        n = len(DATA)
        super().__init__(m,n)
        hor_headers = []
        for n, (key, values) in enumerate(DATA.items()):
            hor_headers.append(key)
            for m, item in enumerate(values):
                qtitem = QTableWidgetItem(item)
                self.setItem(m, n, qtitem)
        self.setHorizontalHeaderLabels(hor_headers)
        # the sizeHint works fine if I disable this line
        self.setVerticalHeaderLabels(f'row{i}' for i in range(1, m + 2))
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def sizeHint(self):
        hh = self.horizontalHeader()
        vh = self.verticalHeader()
        fw = self.frameWidth() * 2
        return QSize(
            hh.length() + vh.sizeHint().width() + fw,
            vh.length() + hh.sizeHint().height() + fw)




        


class BooksWindow(QWidget):
    pass

class BorrowWindow(QWidget):
    pass


    
        
        
def main():
    db.deleteDB()
    db.initDB()
    app = QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
