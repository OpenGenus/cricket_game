from PyQt5 import QtCore, QtGui, QtWidgets
from Dialog2 import Ui_Dialog
from Dialog import Ui_Dialog1
from Dialog3 import Ui_Dialog3
import sqlite3

myProject = sqlite3.connect('Project.db')
curproject = myProject.cursor()

class Ui_MainWindow(object):
    player=[]
    ctg=[]
    bat=0
    ar=0
    wk=0
    bow=0
    pa=1000
    pu=0
    batsmen=[]
    bowlers=[]
    allrounders=[]
    wicketkeepers=[]
    pts=[]
    value=[]
    team=[]
    name=""
    score=[]

    def selection(self,sel,obj):
        curproject.execute("SELECT * FROM teams;")
        self.team=curproject.fetchall()
        curproject.execute("SELECT Player,Scored FROM match;")
        self.score = curproject.fetchall()
        try:
            total=0
            obj.listWidget.clear()
            obj.listWidget_2.clear()
            obj.lineEdit.setText("")
            for i in range(len(self.team)):
                if sel==self.team[i][0]:
                    obj.listWidget_2.addItem(self.team[i][1])
                    for j in range(len(self.score)):
                        if self.score[j][0]==self.team[i][1]:
                            obj.listWidget.addItem(str(self.score[j][1]))
                            total=total+self.score[j][1]
            obj.pushButton.clicked.connect(lambda:obj.lineEdit.setText(str(total)))
        except:
            print("error6")
            
    def openDialog(self):
        try:
            self.dialog = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self.dialog)
            name=[]
            matches=["match1","match2","match3"]
            for i in range(len(self.team)):
                name.append(self.team[i][0])
            name=list(set(name))
            self.ui.comboBox_2.addItems(name)
            self.ui.comboBox.addItems(matches)
            self.ui.comboBox_2.currentIndexChanged.connect(lambda:self.selection(self.ui.comboBox_2.currentText(),self.ui))
            self.dialog.show()
        except:
            print("error5")

    def net(self,ln):
        self.name=ln

    def openDialog4(self):
        try:
            self.dialog1 = QtWidgets.QMainWindow()
            self.ui = Ui_Dialog1()
            self.ui.setupUi(self.dialog1)
            self.ui.pushButton.clicked.connect(lambda:self.net(self.ui.lineEdit.text()))
            self.ui.pushButton.clicked.connect(self.opening)
            self.dialog1.show()
        except:
            print("error1")
        
    def openDialog3(self,mes):
        self.dialog2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_Dialog3()
        self.ui2.setupUi(self.dialog2)
        self.ui2.lineEdit.setText(mes)
        self.dialog2.show()
            
    def openDialog1(self):
        self.dialog1 = QtWidgets.QMainWindow()
        self.ui1 = Ui_Dialog1()
        self.ui1.setupUi(self.dialog1)
        self.ui1.pushButton.clicked.connect(lambda:self.lineEdit_7.setText(str(self.ui1.lineEdit.text())))
        self.ui1.pushButton.clicked.connect(lambda:self.lineEdit_6.setText(str(self.pu)))
        self.ui1.pushButton.clicked.connect(lambda:self.lineEdit_5.setText(str(self.pa)))
        self.ui1.pushButton.clicked.connect(lambda:self.lineEdit_4.setText(str(self.wk)))
        self.ui1.pushButton.clicked.connect(lambda:self.lineEdit_3.setText(str(self.ar)))
        self.ui1.pushButton.clicked.connect(lambda:self.lineEdit_2.setText(str(self.bow)))
        self.ui1.pushButton.clicked.connect(lambda:self.lineEdit.setText(str(self.bat)))
        self.ui1.pushButton.clicked.connect(self.fetchData)
        self.dialog1.show()
        
    def fetchData(self):
        curproject.execute("SELECT Player FROM match;")
        self.player = curproject.fetchall()
        curproject.execute("SELECT ctg FROM stats;")
        self.ctg = curproject.fetchall()
        curproject.execute("SELECT value,Player FROM stats;")
        self.pts = curproject.fetchall()
        curproject.execute("SELECT * FROM teams;")
        self.team=curproject.fetchall()
        curproject.execute("SELECT Player,Scored FROM match;")
        self.score = curproject.fetchall()
        for i in range(len(self.player)):
            if self.ctg[i][0]=='BAT':
                self.batsmen.append(self.player[i][0])
            elif self.ctg[i][0]=='BOW':
                self.bowlers.append(self.player[i][0])
            elif self.ctg[i][0]=='AR':
                self.allrounders.append(self.player[i][0])
            else:
                self.wicketkeepers.append(self.player[i][0])
        

    def choice(self):
        lst = [i.text() for i in self.listWidget1.findItems("", QtCore.Qt.MatchContains)]
        if self.radioButton.isChecked()==True:
            self.listWidget.clear()
            for i in range(len(self.wicketkeepers)):
                if self.wicketkeepers[i] not in lst:
                    self.listWidget.addItem(self.wicketkeepers[i])
        elif self.radioButton_2.isChecked()==True:
            self.listWidget.clear()
            for i in range(len(self.allrounders)):
                if self.allrounders[i] not in lst:
                    self.listWidget.addItem(self.allrounders[i])
        elif self.radioButton_3.isChecked()==True:
            self.listWidget.clear()
            for i in range(len(self.bowlers)):
                if self.bowlers[i] not in lst:
                    self.listWidget.addItem(self.bowlers[i])
        elif self.radioButton_4.isChecked()==True:
            self.listWidget.clear()
            for i in range(len(self.batsmen)):
                if self.batsmen[i] not in lst:
                    self.listWidget.addItem(self.batsmen[i])
                    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(8, 20, 761, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 100, 761, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 220, 761, 301))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.removelist1)
        self.horizontalLayout_3.addWidget(self.listWidget)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.listWidget1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget1.setObjectName("listWidget1")
        self.listWidget1.itemDoubleClicked.connect(self.removelist2) 
        self.horizontalLayout_3.addWidget(self.listWidget1)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 160, 761, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_4.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_4.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.toggled.connect(self.choice)
        self.radioButton_2.toggled.connect(self.choice)
        self.radioButton_3.toggled.connect(self.choice)
        self.radioButton_4.toggled.connect(self.choice)
        self.horizontalLayout_4.addWidget(self.radioButton)
        spacerItem1 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_4.addWidget(self.lineEdit_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_4.setText(_translate("MainWindow", "Batsmen(BAT) "))
        self.label_3.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.label_5.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.label_2.setText(_translate("MainWindow", "wicket-kepper(WK)"))
        self.label_7.setText(_translate("MainWindow", "Points Available:"))
        self.label_6.setText(_translate("MainWindow", "Points Used:"))
        self.radioButton_4.setText(_translate("MainWindow", "BAT"))
        self.radioButton_3.setText(_translate("MainWindow", "BOW"))
        self.radioButton_2.setText(_translate("MainWindow", "AR"))
        self.radioButton.setText(_translate("MainWindow", "WK"))
        self.label_8.setText(_translate("MainWindow", "Team Name "))
        self.lineEdit_7.setText(_translate("MainWindow", "Displayed Here"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

    def removelist1(self, item):
        if self.ar+self.wk+self.bow+self.bat>=11:
            self.openDialog3("There should be only \neleven palyers in the team")
            return      
        if self.radioButton.isChecked()==True:
            if self.wk>0:
                self.openDialog3("There should be only one wicket-keeper")
                return
            else:
                self.wk = self.wk + 1
                self.lineEdit_4.setText(str(self.wk))
        elif self.radioButton_2.isChecked()==True:
            self.ar = self.ar + 1
            self.lineEdit_3.setText(str(self.ar))
        elif self.radioButton_3.isChecked()==True:
            self.bow = self.bow + 1
            self.lineEdit_2.setText(str(self.bow))
        elif self.radioButton_4.isChecked()==True:
            self.bat = self.bat + 1
            self.lineEdit.setText(str(self.bat))
        for i in range(len(self.pts)):
            if item.text()==self.pts[i][1]:
                if self.pa<0:
                    self.openDialog3("points are not available")
                    return
                else:
                    self.pu+=int(self.pts[i][0])
                    self.pa-=int(self.pts[i][0])
                    self.lineEdit_5.setText(str(self.pa))
                    self.lineEdit_6.setText(str(self.pu))
                    self.value.append(int(self.pts[i][0]))
        self.listWidget.takeItem(self.listWidget.row(item))
        self.listWidget1.addItem(item.text())

    def removelist2(self, item):
        self.listWidget1.takeItem(self.listWidget1.row(item))
        for i in range(len(self.pts)):
            if item.text()==self.pts[i][1]:
                self.pu-=int(self.pts[i][0])
                self.pa+=int(self.pts[i][0])
                self.lineEdit_5.setText(str(self.pa))
                self.lineEdit_6.setText(str(self.pu))
                self.value.remove(self.pts[i][0])
        if item.text() in self.wicketkeepers:
            self.wk = self.wk - 1
            self.lineEdit_4.setText(str(self.wk))
        elif item.text() in self.allrounders:
            self.ar = self.ar - 1
            self.lineEdit_3.setText(str(self.ar))
        elif item.text() in self.bowlers:
            self.bow = self.bow - 1
            self.lineEdit_2.setText(str(self.bow))
        elif item.text() in self.batsmen:
            self.bat = self.bat - 1
            self.lineEdit.setText(str(self.bat))
            
        if self.radioButton.isChecked()==True:
            if item.text() in self.wicketkeepers:
                self.listWidget.addItem(item.text())
        if self.radioButton_2.isChecked()==True:
            if item.text() in self.allrounders:
                self.listWidget.addItem(item.text())
        if self.radioButton_3.isChecked()==True:
            if item.text() in self.bowlers:
                self.listWidget.addItem(item.text())
        if self.radioButton_4.isChecked()==True:
            if item.text() in self.batsmen:
                self.listWidget.addItem(item.text())

    def saving(self):
        lst = [i.text() for i in self.listWidget1.findItems("", QtCore.Qt.MatchContains)]
        if len(lst)<11:
            self.openDialog3("There should be only "+"\n"+"eleven palyers in the team")
            return
        else:
            try:
                for i in range(len(lst)):
                    curproject.execute("INSERT INTO teams (name,players,value) VALUES (?,?,?);",(self.lineEdit_7.text(),lst[i],self.value[i]))
                myProject.commit()
                self.openDialog3("saved successful")
            except:
                self.openDialog3("error in saving")
                
    def opening(self):
        try:
            curproject.execute("SELECT * FROM teams;")
            self.team=curproject.fetchall()
            temp=0
            name=[]
            for i in range(len(self.team)):
                name.append(self.team[i][0])
            if self.name in name:
                for i in range(len(self.team)):
                    if self.name==self.team[i][0]:
                        self.listWidget1.addItem(self.team[i][1])
                        temp=temp+self.team[i][2]
                self.lineEdit_6.setText(str(temp))
            else:
                self.openDailog3("team  does not exsist")
        except:
            print("error2")

    def menufunction(self, action):
        txt = str(action.text())
        if txt =='EVALUATE Team':
            self.openDialog()
        elif txt =='NEW Team':
            self.openDialog1()
            self.listWidget.clear()
            self.listWidget1.clear()
            self.bat=0
            self.bow=0
            self.ar=0
            self.wk=0
            self.lineEdit_7.setText("")
            self.pa=1000
            self.pu=0
        elif txt =='SAVE Team':
            self.saving()
        elif txt=='OPEN Team':
            try:
                self.listWidget.clear()
                self.listWidget1.clear()
                self.lineEdit_7.setText("")
                self.lineEdit_5.setText("")
                self.lineEdit_4.setText("")
                self.lineEdit_3.setText("")
                self.lineEdit_2.setText("")
                self.lineEdit.setText("")
                self.radioButton.setEnabled(False)
                self.radioButton_2.setEnabled(False)
                self.radioButton_3.setEnabled(False)
                self.radioButton_4.setEnabled(False)
                self.openDialog4()
            except:
                print("error")
            
               
                
    
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

