from cryptography.fernet import Fernet
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QMessageBox

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = '. : E P I C R Y P T O R : .'
        self.left = 10
        self.top = 10
        self.width = 500
        self.height = 330
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create menu labels and buttons
        self.label = QLabel('Select an option:', self)
        self.label.move(20, 20)

        self.encrypt_button = QPushButton('Encrypt a File', self)
        self.encrypt_button.move(20, 60)
        self.encrypt_button.clicked.connect(self.encrypt_dialog)

        self.decrypt_button = QPushButton('Decrypt a File', self)
        self.decrypt_button.move(20, 100)
        self.decrypt_button.clicked.connect(self.decrypt_dialog)

        self.exit_button = QPushButton('Exit', self)
        self.exit_button.move(20, 140)
        self.exit_button.clicked.connect(self.exit_app)
        
        self.credit_label = QLabel('Note:\nThis is a File Encryption/Decryption application created by \nChristian Fung and Tomas Tello from EPITA School of Engineering', self)
        self.credit_label.move(20, 250)

        self.show()

    def encrypt_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Select file to encrypt', '/')
        if fname[0]:
            gen_key()
            key = load_key()
            encryption(fname[0], key)
            QMessageBox.information(self, 'Success', 'File encrypted successfully!')

    def decrypt_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Select file to decrypt', '/')
        if fname[0]:
            key = load_key()
            try:
                decryption(fname[0], key)
                QMessageBox.information(self, 'Success', 'File decrypted successfully!')
            except:
                QMessageBox.warning(self, 'Error', 'Invalid file or decryption key!')

    def exit_app(self):
        QApplication.quit()

#Load key
def load_key():
    return open("master.key","rb").read()

#Write and Save Key
def gen_key():
    if not os.path.isfile("master.key"):
        key = Fernet.generate_key()
        with open("master.key","wb") as file_key:
            file_key.write(key)

#Encrypt File
def encryption(file_name,key):
    f = Fernet(key)
    with open(file_name,"rb") as file:
        file_info = file.read()
    encrypted_data = f.encrypt(file_info)
    with open(file_name,"wb") as file:
        file.write(encrypted_data)

#Decrypt File
def decryption(file_name,key):
    f = Fernet(key)
    with open(file_name,"rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name,"wb") as file:
        file.write(decrypted_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
