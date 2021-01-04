#ŞİFRE REHBERİM ANA PROGRAMI KARADENİZ_PYTHON GRUBU

from PyQt5 import QtGui, QtWidgets, Qt, QtCore
import sqlite3
import sys

class AnaEkran(QtWidgets.QWidget):
    def __init__(self, baslik, genislik=900, yukseklik=700):
        super().__init__()
        self.setWindowTitle(baslik)
        self.resize(genislik, yukseklik)
        self.setWindowIcon(Qt.QIcon("images/uygulama_icon.png"))
        self.arayuzOlustur()
        self.show()

    def keyPressEvent(self,event):  
        if event.key()==16777216:
            self.close()
        elif event.key()==16777220:
            self.loginFonk()               

    def arayuzOlustur(self):
        alan=QtWidgets.QVBoxLayout(self)
        alan.addStretch()

        logo=QtWidgets.QLabel()
        img=QtGui.QPixmap("images/uygulama_logo.png")
        img=img.scaledToWidth(200)
        logo.setPixmap(img)

        logo.setAlignment(QtCore.Qt.AlignCenter)
        alan.addWidget(logo)

        baslik1=QtWidgets.QLabel("<h3 style= color:#FF5050>ŞİFRE REHBERİM UYGULAMASINA HOŞ GELDİNİZ</h3>")
        baslik1.setAlignment(QtCore.Qt.AlignHCenter)
        alan.addWidget(baslik1)

        baslik2=QtWidgets.QLabel("<h4>Uygulamayı kullanmaya başlamak giriş yapın / ilk defa kullanıyorsanız kayıt olun.</h4>")
        baslik2.setAlignment(QtCore.Qt.AlignHCenter)
        alan.addWidget(baslik2)

        bosluk = QtWidgets.QLabel("<h4> </h4>")
        alan.addWidget(bosluk)

        login_buton=QtWidgets.QPushButton(Qt.QIcon("images/login_icon.png"), "GİRİŞ YAP")
        login_buton.setMaximumSize(460, 100)
        alan.addWidget(login_buton)
        login_buton.clicked.connect(lambda:self.loginFonk())

        register_buton=QtWidgets.QPushButton(Qt.QIcon("images/register_icon.png"), "KAYIT OL")
        register_buton.setMaximumSize(460, 100)
        alan.addWidget(register_buton)
        register_buton.clicked.connect(lambda:self.registerFonk())

        alan.setAlignment(QtCore.Qt.AlignHCenter)
        alan.addStretch()
        self.setLayout(alan)

    def loginFonk(self):
        self.close()
        LogIn("GİRİŞ YAP @ ŞİFRE REHBERİM-2020",400,400)
    def registerFonk(self):
        self.close()
        CreateUser("KAYIT OL @ ŞİFRE REHBERİM-2020", 400, 400)
    
#####################################################################################

class CreateUser(QtWidgets.QWidget):
    def __init__(self, baslik, genislik=900, yukseklik=700):
        super().__init__()
        self.setWindowTitle(baslik)
        self.resize(genislik, yukseklik)
        self.setWindowIcon(Qt.QIcon("images/uygulama_icon.png"))
        self.arayuzOlustur()
        self.show()
        self.dbbaglan()

    def keyPressEvent(self,event):        
        if event.key()==16777216:
            self.close()
        elif event.key()==16777220:
            self.kaydetFonk()

    def dbbaglan(self):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="CREATE TABLE IF NOT EXISTS kullanicilar (kullaniciadi TEXT PRIMARY KEY,rehbersifresi TEXT)"
        imlec.execute(sql_q)
        db.commit()
        db.close()

    def arayuzOlustur(self):
        gridalan=Qt.QGridLayout(self)

        logo=QtWidgets.QLabel()
        logo.setPixmap(QtGui.QPixmap("images/register_icon.png"))
        logo.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(logo, 0, 0, 1, 0)

        baslik1=QtWidgets.QLabel("<h3 style= color:#FF5050>KAYIT OL EKRANI</h3><p></p>")
        baslik1.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(baslik1, 1, 0, 2, 0)

        baslik2=QtWidgets.QLabel("<h4>Kayıt olabilmek için lütfen gerekli bilgileri doldurunuz.<p></p></h4>")
        baslik2.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(baslik2, 2, 0, 3, 0)

        kullaniciadi_label=QtWidgets.QLabel("<h4>Kullanıcı Adı:</h4>")
        gridalan.addWidget(kullaniciadi_label, 5, 0)

        kullaniciadi_text = QtWidgets.QLineEdit()
        kullaniciadi_text.setPlaceholderText("Kullanıcı adınızı yazınız")
        gridalan.addWidget(kullaniciadi_text, 5, 1)
        kullaniciadi_text.textChanged.connect(lambda: self.kullaniciadicalisti(kullaniciadi_text.text()))

        parola_label=QtWidgets.QLabel("<h4>Parola:</h4>")
        gridalan.addWidget(parola_label, 6, 0)

        parola_text=QtWidgets.QLineEdit()
        parola_text.setPlaceholderText("Parolanızı yazınız")
        parola_text.setEchoMode(QtWidgets.QLineEdit.Password)
        gridalan.addWidget(parola_text, 6, 1)
        parola_text.textChanged.connect(lambda: self.parolacalisti(parola_text.text()))

        parola_onay_label=QtWidgets.QLabel("<h4>Parola(tekrar):</h4>")
        gridalan.addWidget(parola_onay_label, 7, 0)

        parola_onay_text=QtWidgets.QLineEdit()
        parola_onay_text.setPlaceholderText("Parolanızı tekrar yazınız")
        parola_onay_text.setEchoMode(QtWidgets.QLineEdit.Password)
        gridalan.addWidget(parola_onay_text, 7, 1)
        parola_onay_text.textChanged.connect(lambda:self.parolaonaycalisti(parola_onay_text.text()))

        bosluk = QtWidgets.QLabel("<h4> </h4>")
        gridalan.addWidget(bosluk, 8, 1)

        kaydetbuton = QtWidgets.QPushButton(Qt.QIcon("images/save_icon.png"), "KAYDET")
        gridalan.addWidget(kaydetbuton, 9, 1)
        kaydetbuton.clicked.connect(lambda:self.kaydetFonk())

        anaekranbuton=QtWidgets.QPushButton(Qt.QIcon("images/home_icon.png"), "ANA EKRAN")
        gridalan.addWidget(anaekranbuton, 10, 1)
        anaekranbuton.clicked.connect(lambda:self.anaEkranFonk())

        gridalan.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(gridalan)

    kullaniciadivalue=""
    parolaonayvalue=""
    parolavalue=""

    def kullaniciadicalisti(self, gelendeger):
        self.kullaniciadivalue=gelendeger
    def parolacalisti(self, gelendeger):
        self.parolavalue=gelendeger
    def parolaonaycalisti(self, gelendeger):
        self.parolaonayvalue=gelendeger
    def kaydetFonk(self):
        if self.kullaniciadivalue!="" and self.parolavalue!="" and self.parolaonayvalue!="":
            if len(self.parolaonayvalue)<8:
                QtWidgets.QMessageBox.critical(self,"HATA","Parolanız en az 8 karakterden oluşmalıdır.")
            elif self.parolakontrol()==1:
                self.dbyekaydet()#bu fonksiyon ile kaydı gerçekleştiriyoruz.
            else:
                QtWidgets.QMessageBox.critical(self,"HATA","Parolaların aynı olduğundan emin olunuz.")
        else:
            QtWidgets.QMessageBox.critical(self,"HATA","Lütfen tüm alanları doldurunuz.")

    def parolakontrol(self):
        if self.parolavalue==self.parolaonayvalue:
            return 1
        else:
            return 0

    def dbyekaydet(self):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="INSERT INTO kullanicilar VALUES(?,?)"
        sql_data=(self.kullaniciadivalue, self.parolavalue)
        try:
            imlec.execute(sql_q,sql_data)
            db.commit()
            QtWidgets.QMessageBox.information(self,"BAŞARILI","Kullanıcı kaydınız gerçekleştirilmiştir.")
            self.close()
            LogIn("GİRİŞ YAP @ ŞİFRE REHBERİM-2020",400,400)
        except sqlite3.Error as hata:
            print(hata)
            QtWidgets.QMessageBox.critical(self, "HATA", "Kullanıcı adı olarak {"+self.kullaniciadivalue+"} daha önce kullanılmıştır.\nLütfen başka bir kullanıcı adı belirleyiniz.")
        db.close()

    def anaEkranFonk(self):
        self.close()
        AnaEkran("ANA EKRAN @ ŞİFRE REHBERİM-2020", 500, 500)

####################################################################################

class LogIn(QtWidgets.QWidget):
    def __init__(self, baslik, genislik=900, yukseklik=700):
        super().__init__()
        self.setWindowTitle(baslik)
        self.resize(genislik, yukseklik)
        self.setWindowIcon(Qt.QIcon("images/uygulama_icon.png"))
        self.arayuzOlustur()
        self.show()
        self.dbbaglan()

    def keyPressEvent(self,event):        
        if event.key()==16777216:
            self.close()
        elif event.key()==16777220: 
            self.girisyapFonk()   

    def dbbaglan(self):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="CREATE TABLE IF NOT EXISTS kullanicilar (kullaniciadi TEXT PRIMARY KEY,rehbersifresi TEXT)"
        imlec.execute(sql_q)
        db.commit()
        db.close()

    def arayuzOlustur(self):
        gridalan=QtWidgets.QGridLayout(self)

        logo=QtWidgets.QLabel()
        logo.setPixmap(QtGui.QPixmap("images/login_icon.png"))
        logo.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(logo, 0, 0, 1, 0) #0.0 da başlayıp 1.0 da span yapıyor.

        baslik1=QtWidgets.QLabel("<h3 style= color:#FF5050>GİRİŞ YAP EKRANI</h3><p></p>")
        baslik1.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(baslik1, 1, 0, 2, 0)

        baslik2=QtWidgets.QLabel("<h4>Giriş yapabilmek için lütfen gerekli bilgileri doldurunuz.<p></p></h4>")
        baslik2.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(baslik2, 2, 0, 3, 0)

        kullaniciadi_label=QtWidgets.QLabel("<h4>Kullanıcı Adı:</h4>")
        gridalan.addWidget(kullaniciadi_label, 5, 0)

        kullaniciadi_text = QtWidgets.QLineEdit()
        kullaniciadi_text.setPlaceholderText("Kullanıcı adınızı yazınız")
        gridalan.addWidget(kullaniciadi_text, 5, 1)
        kullaniciadi_text.textChanged.connect(lambda: self.kullaniciadigonder(kullaniciadi_text.text()))

        parola_label=QtWidgets.QLabel("<h4>Parola:</h4>")
        gridalan.addWidget(parola_label, 6, 0)

        parola_text=QtWidgets.QLineEdit()
        parola_text.setPlaceholderText("Parolanızı yazınız")
        parola_text.setEchoMode(QtWidgets.QLineEdit.Password)
        gridalan.addWidget(parola_text, 6, 1)
        parola_text.textChanged.connect(lambda: self.parolagonder(parola_text.text()))

        bosluk =QtWidgets.QLabel("<h4> </h4>")
        gridalan.addWidget(bosluk, 7, 1)

        girisyapbuton=QtWidgets.QPushButton(Qt.QIcon("images/login_icon2.png"), "GİRİŞ YAP")
        gridalan.addWidget(girisyapbuton,8,1)
        girisyapbuton.clicked.connect(lambda: self.girisyapFonk())

        anaekranbuton=QtWidgets.QPushButton(Qt.QIcon("images/home_icon.png"), "ANA EKRAN")
        gridalan.addWidget(anaekranbuton, 9, 1)
        anaekranbuton.clicked.connect(lambda:self.anaEkranFonk())

        gridalan.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(gridalan)

    kullaniciadivalue=""
    parolavalue=""

    def kullaniciadigonder(self,gelen):
        self.kullaniciadivalue=gelen

    def parolagonder(self,gelen):
        self.parolavalue=gelen

    def girisyapFonk(self):
        if self.kullaniciadivalue!="" and self.parolavalue!="":
            self.kullanicikontrol()
        else:
            QtWidgets.QMessageBox.critical(self, "HATA", "Lütfen tüm alanları doldurunuz.")

    def kullanicikontrol(self):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="SELECT * FROM kullanicilar WHERE kullaniciadi=? and rehbersifresi=?"
        sql_data=(self.kullaniciadivalue,self.parolavalue)
        imlec.execute(sql_q,sql_data)
        oku=imlec.fetchall()
        db.close()

        if len(oku)!=0:
            QtWidgets.QMessageBox.information(self, "BAŞARILI", "Kullanıcı girişi başarılı")
            self.close()
            UserView("KULLANICI EKRANI @ ŞİFRE REHBERİM-2020", 400, 400,oku[0][0])

        else:
            QtWidgets.QMessageBox.critical(self, "HATA", "Kullanıcı adınız veya parolanız hatalı. Lütfen tekrar deneyiniz.")

    def anaEkranFonk(self):
        self.close()
        AnaEkran("ANA EKRAN @ ŞİFRE REHBERİM-2020", 500, 500)

#####################################################################################

class UserView(QtWidgets.QWidget):
    def __init__(self, baslik, genislik=900, yukseklik=700, veri=""):
        super().__init__()
        self.setWindowTitle(baslik)
        self.resize(genislik, yukseklik)
        self.setWindowIcon(Qt.QIcon("images/uygulama_icon.png"))
        self.arayuzOlustur(veri)
        self.show()
        self.dbbaglan()

    def keyPressEvent(self,event):        
        if event.key()==16777216:
            self.close()
        elif event.key()==16777220:
            print()

    def dbbaglan(self):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="CREATE TABLE IF NOT EXISTS sites (kullaniciadi TEXT, uygulamaadi TEXT, uygulamasifresi TEXT)"
        imlec.execute(sql_q)
        db.commit()
        db.close()

    def arayuzOlustur(self,veri):        
        gridalan=QtWidgets.QGridLayout()
        gridalan.setVerticalSpacing(10)
        
        logo=QtWidgets.QLabel()
        img=QtGui.QPixmap("images/uygulama_logo.png")
        img=img.scaledToWidth(180)
        logo.setPixmap(img)
        logo.setFixedSize(200,200)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(logo,0,0,alignment=QtCore.Qt.AlignCenter)

        baslik1=QtWidgets.QLabel("<h2 style= color:#FF5050>Merhaba "+veri+"</h2>")
        gridalan.addWidget(baslik1,1,0,alignment=QtCore.Qt.AlignCenter) 

        cikisbuton=QtWidgets.QPushButton(Qt.QIcon("images/logout_icon.png"),"ÇIKIŞ")
        gridalan.addWidget(cikisbuton,2,0,alignment=QtCore.Qt.AlignCenter)
        cikisbuton.clicked.connect(lambda:self.anaEkranFonk())

        baslik2=QtWidgets.QLabel("<h3><p> </p>Rehberinize ister şifre ekleyin, isterseniz şifrelerinizi görüntüleyin</h3>")
        gridalan.addWidget(baslik2,3,0,alignment=QtCore.Qt.AlignCenter)

        sifrekaydetbuton=QtWidgets.QPushButton(Qt.QIcon("images/sifrekaydet_icon.png"), "YENİ ŞİFRE KAYDET")
        sifrekaydetbuton.setFixedWidth(200)
        gridalan.addWidget(sifrekaydetbuton,5,0,alignment=QtCore.Qt.AlignCenter)
        sifrekaydetbuton.clicked.connect(lambda:self.sifreKaydetFonk(veri))      
        
        sifrelerigosterbuton=QtWidgets.QPushButton(Qt.QIcon("images/sifregoster_icon.png"), "ŞİFRELERİMİ GÖSTER")
        sifrelerigosterbuton.setFixedWidth(200)
        gridalan.addWidget(sifrelerigosterbuton,6,0,alignment=QtCore.Qt.AlignCenter)
        sifrelerigosterbuton.clicked.connect(lambda: self.passViewFonk(veri))

        gridalan.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(gridalan) 

    def anaEkranFonk(self):
        self.close()
        AnaEkran("ANA EKRAN @ ŞİFRE REHBERİM-2020", 500, 500)  
        
    def sifreKaydetFonk(self,gelen):
        self.close()
        AddPass("YENİ ŞİFRE KAYDET @ ŞİFRE REHBERİM-2020", 400, 400, gelen )   
        
    def passViewFonk(self,gelen):
        self.close()
        PassView("ŞİFRELERİM @ ŞİFRE REHBERİM-2020", 400, 400, gelen)

#####################################################################################
class PassView(QtWidgets.QWidget):
    def __init__(self, baslik, genislik=900, yukseklik=700, veri=""):
        super().__init__()
        self.setWindowTitle(baslik)
        self.resize(genislik, yukseklik)
        self.setWindowIcon(Qt.QIcon("images/uygulama_icon.png"))
        self.arayuzOlustur(veri)
        self.show()
        self.dbbaglan()

    def keyPressEvent(self,event):        
        if event.key()==16777216:
            print("ESC tuşuna basıldı.")
            self.close()
            print("Program kullanıcı tarafından sonlandırıldı.")
        elif event.key()==16777220:
            print ("ENTER tuşuna basıldı.")  

    def dbbaglan(self):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="CREATE TABLE IF NOT EXISTS sites (kullaniciadi TEXT, uygulamaadi TEXT, uygulamasifresi TEXT)"
        imlec.execute(sql_q)
        db.commit()
        db.close()
        print("Veritabanı ile bağlantı gerçekleştirildi.")
        
    def vericek(self, veri): 
        veri=(veri,) ###SQL SORGUSU ÇALIŞIRKEN DEĞİŞKENİ TUPLE ŞEKLİNDE ALIYOR...
        print(type(veri))       
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="SELECT uygulamaadi, uygulamasifresi FROM sites WHERE kullaniciadi=?"
        sql_d=(veri)
        imlec.execute(sql_q,sql_d)
        oku=imlec.fetchall()
        db.close()
        return oku        

    def arayuzOlustur(self,data): #HER EKRANDA BURASI DEĞİŞTİRİLECEKTİR.        
        
        gridalan=QtWidgets.QGridLayout()
        gridalan.setVerticalSpacing(10)

        #table oluşturma
        gelen2=self.vericek(data)
        print(gelen2)
        tablewidget=QtWidgets.QTableWidget(len(gelen2),2)
        tablewidget.setFont(QtGui.QFont("Times",weight=QtGui.QFont.Bold))
        tablewidget.setFixedWidth(380)
        tablewidget.setColumnWidth(0,180)
        tablewidget.setColumnWidth(1,180)

        #başlık
        tablewidget.setHorizontalHeaderItem(0,QtWidgets.QTableWidgetItem("Uygulama Adı"))
        tablewidget.setHorizontalHeaderItem(1,QtWidgets.QTableWidgetItem("Uygulama Şifresi"))
                
        #verileri
        gelen=self.vericek(data)
        print(len(gelen))

        for i in range(len(gelen)):
            if gelen[i]!="":
                tablewidget.setItem(i,0,QtWidgets.QTableWidgetItem(gelen[i][0]))
                tablewidget.setItem(i,1,QtWidgets.QTableWidgetItem(gelen[i][1]))
            else:
                break   

        gridalan.addWidget(tablewidget,0,0,alignment=QtCore.Qt.AlignCenter)

        #verisilbutonu
        silbuton=QtWidgets.QPushButton("SİL")
        silbuton.setGeometry(0,0,150,50)
        gridalan.addWidget(silbuton,1,0,alignment=QtCore.Qt.AlignLeft)
        silbuton.clicked.connect(lambda : self.silButonFonk(tablewidget.selectedItems(),data))


        #güncellebutonu
        guncellebuton=QtWidgets.QPushButton("GÜNCELLE")
        guncellebuton.setGeometry(120,0,150,50)
        gridalan.addWidget(guncellebuton,1,0,alignment=QtCore.Qt.AlignRight)
        guncellebuton.clicked.connect(lambda: self.guncelleButonFonk())


        baslik1=QtWidgets.QLabel("<h2 style= color:#FF5050>Merhaba "+data+"</h2>")
        gridalan.addWidget(baslik1,2,0,alignment=QtCore.Qt.AlignCenter) 

        geributon=QtWidgets.QPushButton(Qt.QIcon("images/geri_icon.png"),"GERİ")
        gridalan.addWidget(geributon,3,0,alignment=QtCore.Qt.AlignCenter)
        geributon.clicked.connect(lambda:self.userViewFonk(data))

        baslik2=QtWidgets.QLabel("<h3><p> </p>Rehberinizde bulunan uygulama adı ve şifreleri arayabilirsiniz</h3>")
        gridalan.addWidget(baslik2,4,0,alignment=QtCore.Qt.AlignCenter)        
        

        aramatext=QtWidgets.QLineEdit()
        aramatext.setFixedWidth(200)
        aramatext.setPlaceholderText("Aramak istediğiniz uygulama adını yazınız")
        aramatext.textChanged.connect(lambda: self.aramatextgonder(aramatext.text()))
        gridalan.addWidget(aramatext,5,0,alignment=QtCore.Qt.AlignCenter)

        sifrearabuton=QtWidgets.QPushButton(Qt.QIcon("images/sifreara_icon.png"), "ARA")
        sifrearabuton.setFixedWidth(200)
        sifrearabuton.clicked.connect(lambda: self.sifreAraFonk(data))
        gridalan.addWidget(sifrearabuton,6,0,alignment=QtCore.Qt.AlignCenter)


        gridalan.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(gridalan)   
    

    #sil Fonksiyonu
    def silButonFonk(self,secilen,data):        

        for i in secilen:
            print(i.text())

        if secilen!=[]:
            d=secilen[0].text()
            print(d)
            db = sqlite3.connect("sifrerehberim.db")
            imlec = db.cursor()
            sql_q="DELETE FROM sites WHERE uygulamaadi=? and kullaniciadi=?"
            sql_d=(d,data,)
            imlec.execute(sql_q,sql_d)
            db.commit()
            db.close()
            print("SİLME İŞLEMİ BAŞARILI")
            self.close()
            PassView("ŞİFRELERİ GÖSTER @ ŞİFRE REHBERİM-2020", 400, 400, data)
        
        else:
            QtWidgets.QMessageBox.information(self,"DİKKAT","Uygulama adını seçtiğinizden emin olunuz.")

      
    def guncelleButonFonk(self):
        QtWidgets.QMessageBox.information(self,"HATA","'Güncelle' işlevi geliştirilmeye devam edecektir.")

    arananmetin=""
    def aramatextgonder(self,ara):
        print("FONKSİYONDAKİ VERİ ÇALIŞTI", ara)
        self.arananmetin=ara

    def sifreAraFonk(self,kuladi):
        print(self.arananmetin)
        print(kuladi)
        ###SQL SORGUSU ÇALIŞIRKEN DEĞİŞKENİ TUPLE ŞEKLİNDE ALIYOR... 
        self.arananmetin
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q='SELECT * FROM sites WHERE kullaniciadi="' + kuladi + '" and uygulamaadi Like "%' +  self.arananmetin + '%"'
        
        imlec.execute(sql_q)
        oku=imlec.fetchall()
        db.close()
        print(oku)
        print(type(oku))
        self.close()
        SearchView("ARAMA SAYFASI @ ŞİFRE REHBERİM-2020", 400, 400, kuladi, oku)
           
    def userViewFonk(self,data):
        print("GERİ butonuna basıldı.")
        self.close()
        UserView("KULLANICI EKRANI @ ŞİFRE REHBERİM-2020", 400, 400, data)
    
    def passViewFonk(self):
        print("ŞİFRELERİ GÖSTER butonuna basıldı.")
        self.close()
        PassView("ŞİFRELERİ GÖSTER @ ŞİFRE REHBERİM-2020", 400, 400)

#####################################################################################

class AddPass(QtWidgets.QWidget):
    def __init__(self, baslik, genislik=900, yukseklik=700, veri=""):
        super().__init__()
        self.setWindowTitle(baslik)
        self.resize(genislik, yukseklik)
        self.setWindowIcon(Qt.QIcon("images/uygulama_icon.png"))
        self.arayuzOlustur(veri)
        self.show()
        self.dbbaglan()

    def keyPressEvent(self,event):        
        if event.key()==16777216:
            self.close()
        elif event.key()==16777220:
            print()

    def dbbaglan(self):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="CREATE TABLE IF NOT EXISTS kullanicilar (kullaniciadi TEXT PRIMARY KEY,rehbersifresi TEXT)"
        imlec.execute(sql_q)
        db.commit()
        db.close()

    def arayuzOlustur(self,gelen):
        gridalan=Qt.QGridLayout(self)

        logo=QtWidgets.QLabel()
        logo.setPixmap(QtGui.QPixmap("images/sifrekaydet_icon.png"))
        logo.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(logo, 0, 0, 1, 0)

        baslik1=QtWidgets.QLabel("<h3 style= color:#FF5050>REHBERE ŞİFRE KAYDET EKRANI</h3><p></p>")
        baslik1.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(baslik1, 1, 0, 2, 0)

        baslik2=QtWidgets.QLabel("<h4>Şifre kaydı için lütfen gerekli bilgileri doldurunuz.<p></p></h4>")
        baslik2.setAlignment(QtCore.Qt.AlignCenter)
        gridalan.addWidget(baslik2, 2, 0, 3, 0)

        uygulamaadi_label=QtWidgets.QLabel("<h4>Uygulama Adı:</h4>")
        gridalan.addWidget(uygulamaadi_label, 5, 0)

        uygulamaadi_text = QtWidgets.QLineEdit()
        uygulamaadi_text.setPlaceholderText("Yeni uygulama adını yazınız")
        gridalan.addWidget(uygulamaadi_text, 5, 1)
        uygulamaadi_text.textChanged.connect(lambda: self.uygulamaadicalisti(uygulamaadi_text.text()))

        uygulamasifresi_label=QtWidgets.QLabel("<h4>Uygulama Şifresi:</h4>")
        gridalan.addWidget(uygulamasifresi_label, 6, 0)

        uygulamasifresi_text=QtWidgets.QLineEdit()
        uygulamasifresi_text.setPlaceholderText("Yeni uygulama şifresini yazınız")
        uygulamasifresi_text.setEchoMode(QtWidgets.QLineEdit.Password)
        gridalan.addWidget(uygulamasifresi_text, 6, 1)
        uygulamasifresi_text.textChanged.connect(lambda: self.uygulamasifresicalisti(uygulamasifresi_text.text()))

        bosluk = QtWidgets.QLabel("<h4> </h4>")
        gridalan.addWidget(bosluk, 8, 1)

        passkaydetbuton = QtWidgets.QPushButton(Qt.QIcon("images/save_icon.png"), "KAYDET")
        gridalan.addWidget(passkaydetbuton, 9, 1)
        passkaydetbuton.clicked.connect(lambda:self.passKaydetFonk(gelen))

        anaekranbuton=QtWidgets.QPushButton(Qt.QIcon("images/geri_icon.png"), "GERİ")
        gridalan.addWidget(anaekranbuton, 10, 1)
        anaekranbuton.clicked.connect(lambda:self.geriFonk(gelen))

        gridalan.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(gridalan)

    uygulamaadivalue=""
    uygulamasifresivalue=""

    def uygulamaadicalisti(self, gelendeger):
        self.uygulamaadivalue=gelendeger
    def uygulamasifresicalisti(self, gelendeger):
        self.uygulamasifresivalue=gelendeger
    def passKaydetFonk(self,gelen):
        if self.uygulamaadivalue!="" and self.uygulamasifresivalue!="":
            self.dbyekaydet(gelen)
        else:
            QtWidgets.QMessageBox.critical(self,"HATA","Lütfen tüm alanları doldurunuz.")

    def dbyekaydet(self,gelen):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="INSERT INTO sites VALUES(?,?,?)"
        sql_data=(gelen,self.uygulamaadivalue,self.uygulamasifresivalue)
        try:
            imlec.execute(sql_q,sql_data)
            db.commit()
            QtWidgets.QMessageBox.information(self,"BAŞARILI","Yeni uygulama ve şifre kaydınız gerçekleştirilmiştir.")
        except sqlite3.Error as hata:
            print(hata)
        db.close()
        self.close()
        UserView("KULLANICI EKRANI @ ŞİFRE REHBERİM-2020", 400, 400, gelen)

    def geriFonk(self,gelen):
        self.close()
        UserView("KULLANICI EKRANI @ ŞİFRE REHBERİM-2020", 400, 400,gelen)

#######################################################################################

class SearchView(QtWidgets.QWidget):
    def __init__(self, baslik, genislik=900, yukseklik=700, kadi="", aranan=()):
        super().__init__()
        self.setWindowTitle(baslik)
        self.resize(genislik, yukseklik)
        self.setWindowIcon(Qt.QIcon("images/uygulama_icon.png"))
        self.arayuzOlustur(kadi,aranan)
        self.show()
        self.dbbaglan()

    def keyPressEvent(self,event):        
        if event.key()==16777216:
            self.close()
        elif event.key()==16777220:
            print()

    def dbbaglan(self):
        db = sqlite3.connect("sifrerehberim.db")
        imlec = db.cursor()
        sql_q="CREATE TABLE IF NOT EXISTS sites (kullaniciadi TEXT, uygulamaadi TEXT, uygulamasifresi TEXT)"
        imlec.execute(sql_q)
        db.commit()
        db.close()   

    def arayuzOlustur(self,kuladi,aranan):
        gridalan=QtWidgets.QGridLayout()
        gridalan.setVerticalSpacing(10)

        tablewidget=QtWidgets.QTableWidget(len(aranan),2)
        tablewidget.setFont(QtGui.QFont("Times",weight=QtGui.QFont.Bold))
        tablewidget.setFixedWidth(380)
        tablewidget.setColumnWidth(0,180)
        tablewidget.setColumnWidth(1,180)

        tablewidget.setHorizontalHeaderItem(0,QtWidgets.QTableWidgetItem("Uygulama Adı"))
        tablewidget.setHorizontalHeaderItem(1,QtWidgets.QTableWidgetItem("Uygulama Şifresi"))

        for i in range(len(aranan)):
            if aranan[i]!="":
                tablewidget.setItem(i,0,QtWidgets.QTableWidgetItem(aranan[i][1]))
                tablewidget.setItem(i,1,QtWidgets.QTableWidgetItem(aranan[i][2]))
            else:
                break              
    
        gridalan.addWidget(tablewidget,0,0,alignment=QtCore.Qt.AlignCenter)

        geributon=QtWidgets.QPushButton(Qt.QIcon("images/geri_icon.png"),"GERİ")
        gridalan.addWidget(geributon,2,0,alignment=QtCore.Qt.AlignCenter)
        geributon.clicked.connect(lambda:self.passViewFonk(kuladi)) 

        gridalan.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(gridalan)

    def passViewFonk(self,kuladi):
        self.close()
        PassView("ŞİFRELERİ GÖSTER @ ŞİFRE REHBERİM-2020", 400, 400, kuladi)

#######################################################################################

app=QtWidgets.QApplication(sys.argv)
if __name__ == '__main__':
    AnaEkran("ANA EKRAN @ ŞİFRE REHBERİM-2020", 500, 500)
app.exec_()