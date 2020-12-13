#ŞİFRE REHBERİM ANA PROGRAMI

from PyQt5.Qt import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sqlite3
import sys

class AnaEkran(QWidget): #TÜM EKRANLARDA BU SINIFI KULLANACAĞIZ.
    def __init__(self, baslik, genislik=900, yukseklik=700):
        super().__init__()

        self.setWindowTitle(baslik)
        self.resize(genislik, yukseklik)
        self.setWindowIcon(QIcon("images/uygulama_icon.png"))
        self.arayuzOlustur()
        self.show()


        #dbye baglantıyı sağlıyoruz.

    def databaseBaglan(self):
        db=sqlite3.connect("sifrerehberim.db")
        imlec=db.cursor()
        print("Veritabanına Bağlantı Gerçekleştirildi.")

    def arayuzOlustur(self): #HER EKRANDA BURASI DEĞİŞTİRİLECEKTİR.
        alan=QVBoxLayout(self)
        alan.addStretch()

        logo=QLabel()
        logo.setPixmap(QPixmap("images/uygulama_logo.png"))
        logo.setAlignment(Qt.AlignHCenter)
        alan.addWidget(logo)

        baslik1=QLabel("<h3 style= color:#FF5050>ŞİFRE REHBERİM UYGULAMASINA HOŞ GELDİNİZ</h3>")
        baslik1.setAlignment(Qt.AlignHCenter)
        alan.addWidget(baslik1)

        baslik2=QLabel("<h4>Uygulamayı kullanmaya başlamak giriş yapın / ilk defa kullanıyorsanız kayıt olun.</h4>")
        baslik2.setAlignment(Qt.AlignHCenter)
        alan.addWidget(baslik2)

        bosluk = QLabel("<h4> </h4>")
        alan.addWidget(bosluk)

        login_buton=QPushButton(QIcon("images/login_icon.png"), "GİRİŞ YAP")
        login_buton.setMaximumSize(460, 100)
        alan.addWidget(login_buton)
        login_buton.clicked.connect(lambda:self.loginFonk())

        register_buton=QPushButton(QIcon("images/register_icon.png"), "KAYIT OL")
        register_buton.setMaximumSize(460, 100)
        alan.addWidget(register_buton)
        register_buton.clicked.connect(lambda:self.registerFonk())

        alan.setAlignment(Qt.AlignHCenter)
        alan.addStretch()
        self.setLayout(alan)

    def loginFonk(self):
        print("GİRİŞ YAP butonuna basıldı.")


    def registerFonk(self):
        print("KAYIT OL butonuna basıldı.")
        self.close()
        CreateUser("KAYIT OL @ ŞİFRE REHBERİM-2020", 400, 400)

class CreateUser(QWidget): #TÜM EKRANLARDA BU SINIFI KULLANACAĞIZ.
    def __init__(self, baslik, genislik=900, yukseklik=700):
        super().__init__()

        self.setWindowTitle(baslik)
        self.resize(genislik, yukseklik)
        self.setWindowIcon(QIcon("images/uygulama_icon.png"))
        self.arayuzOlustur()
        self.show()


        self.dbbaglan()




    def dbbaglan(self):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        imlec.execute("CREATE TABLE IF NOT EXISTS kullanicilar (kullaniciadi TEXT,rehbersifresi TEXT)")
        db.commit()
        db.close()
        print("Veritabanına Bağlantı Gerçekleştirildi.")


    def arayuzOlustur(self): #HER EKRANDA BURASI DEĞİŞTİRİLECEKTİR.

        gridalan=QGridLayout(self)


        logo=QLabel()
        logo.setPixmap(QPixmap("images/register_icon.png"))
        logo.setAlignment(Qt.AlignCenter)
        gridalan.addWidget(logo, 0, 0, 1, 0) #0.0 da başlayıp 1.0 da span yapıyor.

        baslik1=QLabel("<h3 style= color:#FF5050>KAYIT OL EKRANI</h3><p></p>")
        baslik1.setAlignment(Qt.AlignCenter)
        gridalan.addWidget(baslik1, 1, 0, 2, 0)

        baslik2=QLabel("<h4>Kayıt olabilmek için lütfen gerekli bilgileri doldurunuz.<p></p></h4>")
        baslik2.setAlignment(Qt.AlignCenter)
        gridalan.addWidget(baslik2, 2, 0, 3, 0)

        kullaniciadi_label=QLabel("<h4>Kullanıcı Adı:</h4>")
        gridalan.addWidget(kullaniciadi_label, 5, 0)

        kullaniciadi_text = QLineEdit()
        kullaniciadi_text.setPlaceholderText("Kullanıcı adınızı yazınız")
        gridalan.addWidget(kullaniciadi_text, 5, 1)
        kullaniciadi_text.textChanged.connect(lambda: self.kullaniciadicalisti(kullaniciadi_text.text()))


        parola_label=QLabel("<h4>Parola:</h4>")
        gridalan.addWidget(parola_label, 6, 0)

        parola_text=QLineEdit()
        parola_text.setPlaceholderText("Parolanızı yazınız")
        parola_text.setEchoMode(QLineEdit.Password)
        gridalan.addWidget(parola_text, 6, 1)
        parola_text.textChanged.connect(lambda: self.parolacalisti(parola_text.text()))

        parola_onay_label=QLabel("<h4>Parola(tekrar):</h4>")
        gridalan.addWidget(parola_onay_label, 7, 0)

        parola_onay_text=QLineEdit()
        parola_onay_text.setPlaceholderText("Parolanızı tekrar yazınız")
        parola_onay_text.setEchoMode(QLineEdit.Password)
        gridalan.addWidget(parola_onay_text, 7, 1)
        parola_onay_text.textChanged.connect(lambda:self.parolaonaycalisti(parola_onay_text.text()))

        bosluk = QLabel("<h4> </h4>")
        gridalan.addWidget(bosluk, 8, 1)

        kaydetbuton = QPushButton(QIcon("images/save_icon.png"), "KAYDET")
        gridalan.addWidget(kaydetbuton, 9, 1)
        kaydetbuton.clicked.connect(lambda: self.kaydetFonk())


        anaekranbuton=QPushButton(QIcon("images/home_icon.png"), "ANA EKRAN")
        gridalan.addWidget(anaekranbuton, 10, 1)
        anaekranbuton.clicked.connect(lambda:self.anaEkranFonk())


        gridalan.setAlignment(Qt.AlignCenter)
        self.setLayout(gridalan)

    def kullaniciadicalisti(self, gelendeger):
        self.kullaniciadivalue=gelendeger

    def parolacalisti(self, gelendeger):
        self.parolavalue=gelendeger

    def parolaonaycalisti(self, gelendeger):
        self.parolaonayvalue=gelendeger



    def kaydetFonk(self):
        print("KAYDET butonuna basıldı.")
        self.verikaydet()

    # burada da dbye bağlantı fonksiyonunu çağırıyoruz.
    def verikaydet(self):
        print("Kullanıcı Adınız:", self.kullaniciadivalue)
        print("Parolanız:", self.parolavalue)
        print("Parola Onayı:", self.parolaonayvalue)

        
        print("KAYIT BAŞARILI...")

    def anaEkranFonk(self):
        print("ANA EKRAN butonuna basıldı.")
        self.close()
        AnaEkran("ANA EKRAN @ ŞİFRE REHBERİM-2020", 600, 600)



app=QApplication(sys.argv)

if __name__ == '__main__':
    AnaEkran("ANA EKRAN @ ŞİFRE REHBERİM-2020", 600, 600)
app.exec_()













