from PyQt5 import QtCore, QtGui, QtWidgets
import random
import datetime
import keyboard
import time
import pyautogui

pins =          ["4",
                 "6",
                 "9", 
                 "12", 
                 "16"]

advancedpins =  ["4", 
                 "5", 
                 "6", 
                 "7", 
                 "8", 
                 "9", 
                 "10", 
                 "11", 
                 "12", 
                 "13", 
                 "14", 
                 "15", 
                 "16", 
                 "17", 
                 "18", 
                 "19", 
                 "20", 
                 "21",
                 "22", 
                 "23",
                 "24",
                 "25",
                 "26",
                 "27",
                 "28",
                 "29",
                 "30",
                 "31",
                 "32",
                 "All PIN Bruteforce",
                 "1-3 PIN Bruteforce"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 231)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.label.setObjectName("label")
        self.pinlength = QtWidgets.QComboBox(self.centralwidget)
        self.pinlength.setGeometry(QtCore.QRect(40, 10, 241, 21))
        self.pinlength.setObjectName("pinlength")
        self.pinlength.addItems(pins)
        self.pinlength.currentIndexChanged.connect(self.chk_pin)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 271, 71))
        self.groupBox.setObjectName("groupBox")
        self.pgt_rndm_black = QtWidgets.QRadioButton(self.groupBox)
        self.pgt_rndm_black.setGeometry(QtCore.QRect(130, 20, 131, 17))
        self.pgt_rndm_black.setObjectName("pgt_rndm_black")
        self.pgt_random = QtWidgets.QRadioButton(self.groupBox)
        self.pgt_random.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.pgt_random.setChecked(True)
        self.pgt_random.setAutoRepeat(False)
        self.pgt_random.setObjectName("pgt_random")
        self.pgt_add = QtWidgets.QRadioButton(self.groupBox)
        self.pgt_add.setGeometry(QtCore.QRect(10, 40, 121, 21))
        self.pgt_add.setObjectName("pgt_add")
        self.info = QtWidgets.QGroupBox(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(10, 120, 271, 101))
        self.info.setObjectName("info")
        self.tp_lb = QtWidgets.QLabel(self.info)
        self.tp_lb.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.tp_lb.setObjectName("tp_lb")
        self.btu_lb = QtWidgets.QLabel(self.info)
        self.btu_lb.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.btu_lb.setObjectName("btu_lb")
        self.triedpins = QtWidgets.QLabel(self.info)
        self.triedpins.setGeometry(QtCore.QRect(110, 50, 151, 21))
        self.triedpins.setObjectName("triedpins")
        self.btuptime = QtWidgets.QLabel(self.info)
        self.btuptime.setGeometry(QtCore.QRect(110, 20, 151, 21))
        self.btuptime.setObjectName("btuptime")
        self.cp_lb = QtWidgets.QLabel(self.info)
        self.cp_lb.setGeometry(QtCore.QRect(10, 70, 91, 21))
        self.cp_lb.setObjectName("cp_lb")
        self.currentpin = QtWidgets.QLabel(self.info)
        self.currentpin.setGeometry(QtCore.QRect(110, 70, 151, 21))
        self.currentpin.setObjectName("currentpin")
        self.startbruteforce = QtWidgets.QPushButton(self.centralwidget)
        self.startbruteforce.setGeometry(QtCore.QRect(289, 9, 133, 23))
        self.startbruteforce.setObjectName("startbruteforce")
        self.startbruteforce.clicked.connect(self.start)
        self.avoid_rl = QtWidgets.QCheckBox(self.centralwidget)
        self.avoid_rl.setGeometry(QtCore.QRect(290, 40, 131, 17))
        self.avoid_rl.setObjectName("avoid_rl")
        self.avoid_rl.clicked.connect(self.rl_warn)
        self.erasepin = QtWidgets.QCheckBox(self.centralwidget)
        self.erasepin.setGeometry(QtCore.QRect(290, 60, 131, 17))
        self.erasepin.setObjectName("erasepin")
        self.keyinterval = QtWidgets.QCheckBox(self.centralwidget)
        self.keyinterval.setGeometry(QtCore.QRect(290, 80, 131, 17))
        self.keyinterval.setObjectName("keyinterval")
        self.advancedpins = QtWidgets.QCheckBox(self.centralwidget)
        self.advancedpins.setGeometry(QtCore.QRect(290, 120, 131, 17))
        self.advancedpins.setObjectName("advancedpins")
        self.advancedpins.clicked.connect(self.chpins)
        self.d_opacity = QtWidgets.QCheckBox(self.centralwidget)
        self.d_opacity.setGeometry(QtCore.QRect(290, 100, 131, 17))
        self.d_opacity.setObjectName("d_opacity")
        self.d_opacity.clicked.connect(self.opacity)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def rl_warn(self):
        if self.avoid_rl.isChecked():
            pyautogui.alert('Enabling "Avoid Ratelimit" Can cause the Bruteforce GUI to stop responding.\n\nPlease take note that the Bruteforce GUI did not crash.\nAfter 30 seconds the Bruteforce GUI will start responding\nYou can hold Q to stop while waiting.', "PIN Bruteforcer - Warning", "OK")
    
    def chpins(self):
        self.pinlength.clear()
        if self.advancedpins.isChecked():
            self.pinlength.addItems(advancedpins)
        if not self.advancedpins.isChecked():
            self.pinlength.addItems(pins)

    def opacity(self):
        if self.d_opacity.isChecked():
            MainWindow.setWindowOpacity(0.6)
        if not self.d_opacity.isChecked():
            MainWindow.setWindowOpacity(1.0)
    
    def chk_pin(self):
        pin = self.pinlength.currentText()

        if pin == "All PIN Bruteforce":
            self.pgt_random.setEnabled(False)
            self.pgt_rndm_black.setEnabled(False)
            self.pgt_add.setChecked(True)
        
        if not pin == "All PIN Bruteforce":
            self.pgt_random.setEnabled(True)
            self.pgt_rndm_black.setEnabled(True)

    def start(self):
        self.startbruteforce.setText("Starting in 5...")
        QtWidgets.QApplication.processEvents()
        time.sleep(1)
        self.startbruteforce.setText("Starting in 4...")
        QtWidgets.QApplication.processEvents()
        time.sleep(1)
        self.startbruteforce.setText("Starting in 3...")
        QtWidgets.QApplication.processEvents()
        time.sleep(1)
        self.startbruteforce.setText("Starting in 2...")
        QtWidgets.QApplication.processEvents()
        time.sleep(1)
        self.startbruteforce.setText("Starting in 1...")
        QtWidgets.QApplication.processEvents()
        time.sleep(1)
        self.startbruteforce.setText("Hold Q to Stop")
        self.btuptime.setText("0:00:00")
        self.triedpins.setText("0")
        global startTime
        startTime = time.time()
        QtWidgets.QApplication.processEvents()
        self.startbruteforce.setEnabled(False)
        self.pinlength.setEnabled(False)
        self.groupBox.setEnabled(False)
        tried = 0
        blacklisted = []
        while 1:
            if self.pinlength.currentText() == "4":
                min = 0
                max = 9999
            
            if self.pinlength.currentText() == "5":
                min = 0
                max = 99999
            
            if self.pinlength.currentText() == "6":
                min = 0
                max = 999999
            
            if self.pinlength.currentText() == "7":
                min = 0
                max = 9999999
            
            if self.pinlength.currentText() == "8":
                min = 0
                max = 99999999
            
            if self.pinlength.currentText() == "9":
                min = 0
                max = 999999999
            
            if self.pinlength.currentText() == "10":
                min = 0
                max = 9999999999
            
            if self.pinlength.currentText() == "11":
                min = 0
                max = 99999999999
    
            if self.pinlength.currentText() == "12":
                min = 0
                max = 999999999999
            
            if self.pinlength.currentText() == "13":
                min = 0
                max = 9999999999999
            
            if self.pinlength.currentText() == "14":
                min = 0
                max = 99999999999999
            
            if self.pinlength.currentText() == "15":
                min = 0
                max = 999999999999999
            
            if self.pinlength.currentText() == "16":
                min = 0
                max = 9999999999999999
            
            if self.pinlength.currentText() == "17":
                min = 0
                max = 99999999999999999
            
            if self.pinlength.currentText() == "18":
                min = 0
                max = 999999999999999999
            
            if self.pinlength.currentText() == "19":
                min = 0
                max = 9999999999999999999
            
            if self.pinlength.currentText() == "20":
                min = 0
                max = 99999999999999999999
            
            if self.pinlength.currentText() == "21":
                min = 0
                max = 999999999999999999999
            
            if self.pinlength.currentText() == "22":
                min = 0
                max = 9999999999999999999999
            
            if self.pinlength.currentText() == "23":
                min = 0
                max = 99999999999999999999999
            
            if self.pinlength.currentText() == "24":
                min = 0
                max = 999999999999999999999999
    
            if self.pinlength.currentText() == "25":
                min = 0
                max = 9999999999999999999999999
            
            if self.pinlength.currentText() == "26":
                min = 0
                max = 99999999999999999999999999
            
            if self.pinlength.currentText() == "27":
                min = 0
                max = 999999999999999999999999999
            
            if self.pinlength.currentText() == "28":
                min = 0
                max = 9999999999999999999999999999
            
            if self.pinlength.currentText() == "29":
                min = 0
                max = 99999999999999999999999999999
            
            if self.pinlength.currentText() == "30":
                min = 0
                max = 999999999999999999999999999999
            
            if self.pinlength.currentText() == "31":
                min = 0
                max = 9999999999999999999999999999999
            
            if self.pinlength.currentText() == "32":
                min = 0
                max = 99999999999999999999999999999999
            
            if self.pinlength.currentText() == "All PIN Bruteforce":
                min = 0
                max = 99999999999999999999999999999999
            
            if self.pinlength.currentText() == "1-3 PIN Bruteforce":
                min = 0
                max = 999

            global x
            if self.pgt_random.isChecked():
                if self.pinlength.currentText() == "4":
                    x = format(random.randint(min, max), '04d')
                if self.pinlength.currentText() == "5":
                    x = format(random.randint(min, max), '05d')
                if self.pinlength.currentText() == "6":
                    x = format(random.randint(min, max), '06d')
                if self.pinlength.currentText() == "7":
                    x = format(random.randint(min, max), '07d')
                if self.pinlength.currentText() == "8":
                    x = format(random.randint(min, max), '08d')
                if self.pinlength.currentText() == "9":
                    x = format(random.randint(min, max), '09d')
                if self.pinlength.currentText() == "10":
                    x = format(random.randint(min, max), '010d')
                if self.pinlength.currentText() == "11":
                    x = format(random.randint(min, max), '011d')
                if self.pinlength.currentText() == "12":
                    x = format(random.randint(min, max), '012d')
                if self.pinlength.currentText() == "13":
                    x = format(random.randint(min, max), '013d')
                if self.pinlength.currentText() == "14":
                    x = format(random.randint(min, max), '014d')
                if self.pinlength.currentText() == "15":
                    x = format(random.randint(min, max), '015d')
                if self.pinlength.currentText() == "16":
                    x = format(random.randint(min, max), '016d')
                if self.pinlength.currentText() == "17":
                    x = format(random.randint(min, max), '017d')
                if self.pinlength.currentText() == "18":
                    x = format(random.randint(min, max), '018d')
                if self.pinlength.currentText() == "19":
                    x = format(random.randint(min, max), '019d')
                if self.pinlength.currentText() == "20":
                    x = format(random.randint(min, max), '020d')
                if self.pinlength.currentText() == "21":
                    x = format(random.randint(min, max), '021d')
                if self.pinlength.currentText() == "22":
                    x = format(random.randint(min, max), '022d')
                if self.pinlength.currentText() == "23":
                    x = format(random.randint(min, max), '023d')
                if self.pinlength.currentText() == "24":
                    x = format(random.randint(min, max), '024d')
                if self.pinlength.currentText() == "25":
                    x = format(random.randint(min, max), '025d')
                if self.pinlength.currentText() == "26":
                    x = format(random.randint(min, max), '026d')
                if self.pinlength.currentText() == "27":
                    x = format(random.randint(min, max), '027d')
                if self.pinlength.currentText() == "28":
                    x = format(random.randint(min, max), '028d')
                if self.pinlength.currentText() == "29":
                    x = format(random.randint(min, max), '029d')
                if self.pinlength.currentText() == "30":
                    x = format(random.randint(min, max), '030d')
                if self.pinlength.currentText() == "31":
                    x = format(random.randint(min, max), '031d')
                if self.pinlength.currentText() == "32":
                    x = format(random.randint(min, max), '032d')
                if self.pinlength.currentText() == "All PIN Bruteforce":
                    x = format(random.randint(min, max), '04d')
                if self.pinlength.currentText() == "1-3 PIN Bruteforce":
                    x = format(random.randint(min, max), '01d')

                self.currentpin.setText(x)
                for numbers in x:
                    keyboard.press(numbers)
                    QtWidgets.QApplication.processEvents()

                    if keyboard.is_pressed("q"):
                        self.startbruteforce.setEnabled(True)
                        self.pinlength.setEnabled(True)
                        self.groupBox.setEnabled(True)
                        self.startbruteforce.setText("Start PIN Bruteforce")
                        return
                    
                    if self.keyinterval.isChecked():
                        time.sleep(0.2)

                pyautogui.press("enter")
                if self.erasepin.isChecked():
                    pyautogui.hotkey("ctrl", "a")
                    pyautogui.hotkey("delete")

                QtWidgets.QApplication.processEvents()
                if self.avoid_rl.isChecked():
                    time.sleep(30)
            
            if self.pgt_rndm_black.isChecked():
                if self.pinlength.currentText() == "4":
                    x = format(random.randint(min, max), '04d')
                if self.pinlength.currentText() == "5":
                    x = format(random.randint(min, max), '05d')
                if self.pinlength.currentText() == "6":
                    x = format(random.randint(min, max), '06d')
                if self.pinlength.currentText() == "7":
                    x = format(random.randint(min, max), '07d')
                if self.pinlength.currentText() == "8":
                    x = format(random.randint(min, max), '08d')
                if self.pinlength.currentText() == "9":
                    x = format(random.randint(min, max), '09d')
                if self.pinlength.currentText() == "10":
                    x = format(random.randint(min, max), '010d')
                if self.pinlength.currentText() == "11":
                    x = format(random.randint(min, max), '011d')
                if self.pinlength.currentText() == "12":
                    x = format(random.randint(min, max), '012d')
                if self.pinlength.currentText() == "13":
                    x = format(random.randint(min, max), '013d')
                if self.pinlength.currentText() == "14":
                    x = format(random.randint(min, max), '014d')
                if self.pinlength.currentText() == "15":
                    x = format(random.randint(min, max), '015d')
                if self.pinlength.currentText() == "16":
                    x = format(random.randint(min, max), '016d')
                if self.pinlength.currentText() == "17":
                    x = format(random.randint(min, max), '017d')
                if self.pinlength.currentText() == "18":
                    x = format(random.randint(min, max), '018d')
                if self.pinlength.currentText() == "19":
                    x = format(random.randint(min, max), '019d')
                if self.pinlength.currentText() == "20":
                    x = format(random.randint(min, max), '020d')
                if self.pinlength.currentText() == "21":
                    x = format(random.randint(min, max), '021d')
                if self.pinlength.currentText() == "22":
                    x = format(random.randint(min, max), '022d')
                if self.pinlength.currentText() == "23":
                    x = format(random.randint(min, max), '023d')
                if self.pinlength.currentText() == "24":
                    x = format(random.randint(min, max), '024d')
                if self.pinlength.currentText() == "25":
                    x = format(random.randint(min, max), '025d')
                if self.pinlength.currentText() == "26":
                    x = format(random.randint(min, max), '026d')
                if self.pinlength.currentText() == "27":
                    x = format(random.randint(min, max), '027d')
                if self.pinlength.currentText() == "28":
                    x = format(random.randint(min, max), '028d')
                if self.pinlength.currentText() == "29":
                    x = format(random.randint(min, max), '029d')
                if self.pinlength.currentText() == "30":
                    x = format(random.randint(min, max), '030d')
                if self.pinlength.currentText() == "31":
                    x = format(random.randint(min, max), '031d')
                if self.pinlength.currentText() == "32":
                    x = format(random.randint(min, max), '032d')
                if self.pinlength.currentText() == "All PIN Bruteforce":
                    x = format(random.randint(min, max), '04d')
                if self.pinlength.currentText() == "1-3 PIN Bruteforce":
                    x = format(random.randint(min, max), '01d')

                self.currentpin.setText(x)
                for numbers in x:
                    blacklist = [w for w in blacklisted if numbers in w]
                    if blacklist:
                        print("Number Blacklisted - Already Placed")
                        break
                    
                    if not blacklist:
                        keyboard.press(numbers)
                        QtWidgets.QApplication.processEvents()

                    if keyboard.is_pressed("q"):
                        self.startbruteforce.setEnabled(True)
                        self.pinlength.setEnabled(True)
                        self.groupBox.setEnabled(True)
                        self.startbruteforce.setText("Start PIN Bruteforce")
                        return
                    
                    if self.keyinterval.isChecked():
                        time.sleep(0.2)

                pyautogui.press("enter")
                if self.erasepin.isChecked():
                    pyautogui.hotkey("ctrl", "a")
                    pyautogui.hotkey("delete")

                QtWidgets.QApplication.processEvents()
                if self.avoid_rl.isChecked():
                    time.sleep(30)

            if self.pgt_add.isChecked():
                for i in range(max+1):
                    if self.pinlength.currentText() == "4":
                        x = format(i, '04d')
                    if self.pinlength.currentText() == "5":
                        x = format(i, '05d')
                    if self.pinlength.currentText() == "6":
                        x = format(i, '06d')
                    if self.pinlength.currentText() == "7":
                        x = format(i, '07d')
                    if self.pinlength.currentText() == "8":
                        x = format(i, '08d')
                    if self.pinlength.currentText() == "9":
                        x = format(i, '09d')
                    if self.pinlength.currentText() == "10":
                        x = format(i, '010d')
                    if self.pinlength.currentText() == "11":
                        x = format(i, '011d')
                    if self.pinlength.currentText() == "12":
                        x = format(i, '012d')
                    if self.pinlength.currentText() == "13":
                        x = format(i, '013d')
                    if self.pinlength.currentText() == "14":
                        x = format(i, '014d')
                    if self.pinlength.currentText() == "15":
                        x = format(i, '015d')
                    if self.pinlength.currentText() == "16":
                        x = format(i, '016d')
                    if self.pinlength.currentText() == "17":
                        x = format(i, '017d')
                    if self.pinlength.currentText() == "18":
                        x = format(i, '018d')
                    if self.pinlength.currentText() == "19":
                        x = format(i, '019d')
                    if self.pinlength.currentText() == "20":
                        x = format(i, '020d')
                    if self.pinlength.currentText() == "21":
                        x = format(i, '021d')
                    if self.pinlength.currentText() == "22":
                        x = format(i, '022d')
                    if self.pinlength.currentText() == "23":
                        x = format(i, '023d')
                    if self.pinlength.currentText() == "24":
                        x = format(i, '024d')
                    if self.pinlength.currentText() == "25":
                        x = format(i, '025d')
                    if self.pinlength.currentText() == "26":
                        x = format(i, '026d')
                    if self.pinlength.currentText() == "27":
                        x = format(i, '027d')
                    if self.pinlength.currentText() == "28":
                        x = format(i, '028d')
                    if self.pinlength.currentText() == "29":
                        x = format(i, '029d')
                    if self.pinlength.currentText() == "30":
                        x = format(i, '030d')
                    if self.pinlength.currentText() == "31":
                        x = format(i, '031d')
                    if self.pinlength.currentText() == "32":
                        x = format(i, '032d')
                    if self.pinlength.currentText() == "All PIN Bruteforce":
                        x = format(i, '04d')
                    if self.pinlength.currentText() == "1-3 PIN Bruteforce":
                        x = format(i, '01d')

                    QtWidgets.QApplication.processEvents()
                    self.currentpin.setText(x)
                    for numbers in x:
                        keyboard.press(numbers)
                        QtWidgets.QApplication.processEvents()

                        if keyboard.is_pressed("q"):
                            self.startbruteforce.setEnabled(True)
                            self.pinlength.setEnabled(True)
                            self.groupBox.setEnabled(True)
                            self.startbruteforce.setText("Start PIN Bruteforce")
                            return
                        
                        self.btuptime.setText(str(datetime.timedelta(seconds=int(round(time.time()-startTime)))))

                        if self.keyinterval.isChecked():
                            time.sleep(0.2)

                    pyautogui.press("enter")
                    if self.erasepin.isChecked():
                        pyautogui.hotkey("ctrl", "a")
                        pyautogui.hotkey("delete")
                    

                    if i == max:
                        self.startbruteforce.setEnabled(True)
                        self.pinlength.setEnabled(True)
                        self.groupBox.setEnabled(True)
                        self.startbruteforce.setText("Start PIN Bruteforce")
                        return
                
                if self.avoid_rl.isChecked():
                    time.sleep(30)

            tried += 1
            self.btuptime.setText(str(datetime.timedelta(seconds=int(round(time.time()-startTime)))))
            self.triedpins.setText(str(tried))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PIN Bruteforcer"))
        self.label.setText(_translate("MainWindow", "PIN"))
        self.groupBox.setTitle(_translate("MainWindow", "PIN Generation Type"))
        self.pgt_rndm_black.setText(_translate("MainWindow", "Random (with Blacklist)"))
        self.pgt_random.setText(_translate("MainWindow", "Random"))
        self.pgt_add.setText(_translate("MainWindow", "Additional"))
        self.info.setTitle(_translate("MainWindow", "Bruteforce Info"))
        self.tp_lb.setText(_translate("MainWindow", "Tried Pins"))
        self.btu_lb.setText(_translate("MainWindow", "Bruteforce Uptime"))
        self.triedpins.setText(_translate("MainWindow", "0"))
        self.btuptime.setText(_translate("MainWindow", "0:00:00"))
        self.cp_lb.setText(_translate("MainWindow", "Current Pin"))
        self.currentpin.setText(_translate("MainWindow", "0"))
        self.startbruteforce.setText(_translate("MainWindow", "Start PIN Bruteforce"))
        self.avoid_rl.setText(_translate("MainWindow", "Avoid Ratelimit"))
        self.erasepin.setText(_translate("MainWindow", "Erase PIN on Enter"))
        self.keyinterval.setText(_translate("MainWindow", "Enable Key Interval"))
        self.advancedpins.setText(_translate("MainWindow", "Advanced PINs Mode"))
        self.d_opacity.setText(_translate("MainWindow", "Decrease Opacity"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    print("PIN Bruteforcer made by Xavee#7951")
    print("Github Repo: xacvwe/PINBruteforcer")
    sys.exit(app.exec_())

# PIN Bruteforcer made by Xavee#7951
#
# GUI Main Code
# Github Repo : xacvwe/PINBruteforcer
