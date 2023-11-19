import mysql.connector
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# Importer la classe Ui_MainWindow du fichier demo.py
from tp import Ui_MainWindow

chapitre = 1
livre_id = 1
id_sauvegarde = 1
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # On va créer la fenêtre avec cette commande
        self.setupUi(self)
        
        self.pushButton_creer.clicked.connect(self._creer_personnage)
        self.pushButton_sauvegarder.clicked.connect(self._sauvegarder_personnage)
        self.pushButton_chapitre.clicked.connect(self._changement_chapitre)
        self.pushButton_charger.clicked.connect(self._charger_personnage)

        self._prologue(livre_id)
        self._afficher_arme()
        self._afficher_kai()
        self._les_sauvegarde()

    def _creer_personnage(self):
        try:
            global id_sauvegarde
            global livre_id
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)
            nom = self.lineEdit_nom.text()

            param={'nom': nom}
            requete = "INSERT INTO personnage (nom) VALUES (%(nom)s);"
            print("creer")
            cursor.execute(requete, param)

            requete = "SELECT last_insert_id() as id;"
            cursor.execute(requete)

            
            id_sauvegarde = cursor.fetchone()
            id_sauvegarde = int(id_sauvegarde['id'])

        except mysql.connector.Error as erreur:
            print(erreur)
            
        finally:
            cnx.commit()
            cursor.close()
            cnx.close()
            self._change_arme()
            self._change_kai()
            self._prologue(livre_id)

    def _sauvegarder_personnage(self):
        try:
            global chapitre
            global id_sauvegarde
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)

            nom = self.lineEdit_nom.text()
            argent = self.lineEdit_argent.text()
            
            if argent == '':
                argent =10
            argent = int(argent)

            habil = self.spinBox_habilite.value()
            endure = self.spinBox_endurance.value()
            repas = self.textEdit_repas.toPlainText()
            objet = self.textEdit_speciaux.toPlainText()
            equipe = self.textEdit_equipement.toPlainText()

            if id_sauvegarde != 0:
                param={'id': id_sauvegarde,'nom': nom, 'argent': argent, 'habil': habil, 'endure': endure,
                    'repas': repas, 'objet': objet, 'equipe': equipe, 'chapitre' : chapitre}
                requete = "UPDATE personnage SET nom = %(nom)s, argent = %(argent)s, habilite = %(habil)s, endurance = %(endure)s, repas = %(repas)s, objet_speciaux = %(objet)s, equipement = %(equipe)s, chapitre = %(chapitre)s WHERE id = %(id)s;"

                cursor.execute(requete, param)


        except mysql.connector.Error as erreur:
            print(erreur)
            
        finally:
            cnx.commit()
            cursor.close()
            cnx.close()
            self._les_sauvegarde()
            self._sup_arme()
            self._sup_kai()
            self._change_arme()
            self._change_kai()

    def _charger_personnage(self):
        global chapitre
        global id_sauvegarde
        try:
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)
            
            id_charge = int(self.comboBox_charger.currentText())
            
            param = {'id_personnage': id_charge , 'id_chapitre': chapitre}
            requete = "SELECT * FROM personnage WHERE id = %(id_personnage)s;"
            cursor.execute(requete, param)

            value = cursor.fetchone()

            self.lineEdit_nom.setText(value['nom'])
            self.lineEdit_argent.setText(str(value['argent']))

            self.spinBox_habilite.setValue(value['habilite'])
            self.spinBox_endurance.setValue(value['endurance'])
            self.textEdit_repas.setPlainText(value['repas']) 
            self.textEdit_speciaux.setPlainText(value['objet_speciaux'])
            self.textEdit_equipement.setPlainText(value['equipement'])

            id_sauvegarde = value['id']
            chapitre = value['chapitre']
            print(chapitre)
            param = {'id_personnage': id_charge , 'id_chapitre': chapitre}
            requete = "SELECT * FROM chapitre INNER JOIN chapitre_livre ON id_chapitre = id WHERE id_chapitre = %(id_chapitre)s; "
            cursor.execute(requete, param)
            
            value = cursor.fetchone()

            self.label_chapitre.setText(str(value['no_chapitre']))
            self.plainTextEdit_chapitre.setPlainText(value['texte'])
            self._combox_navigation() 

            requete = "SELECT id FROM arme INNER JOIN arme_personnage ON id_arme = id WHERE id_personnage = %(id_personnage)s;"
            cursor.execute(requete, param)

            id_arme = cursor.fetchall()
            self.comboBox_arme_1.setCurrentIndex(id_arme[0]['id'] -1)
            self.comboBox__arme_2.setCurrentIndex(id_arme[1]['id'] -1)

            requete = "SELECT id FROM discipline INNER JOIN discipline_personnage ON id_discipline = id WHERE id_personnage = %(id_personnage)s;"
            cursor.execute(requete, param)

            id_kai = cursor.fetchall()
            self.comboBox_kai_1.setCurrentIndex(id_kai[0]['id'] -1)
            self.comboBox_kai_2.setCurrentIndex(id_kai[1]['id'] -1)
            self.comboBox_kai_3.setCurrentIndex(id_kai[2]['id'] -1)
            self.comboBox_kai_4.setCurrentIndex(id_kai[3]['id'] -1)
            self.comboBox_kai_5.setCurrentIndex(id_kai[4]['id'] -1)

        except mysql.connector.Error as erreur:
            print(erreur)
            
        finally:
            cursor.close()
            cnx.close()

    def _les_sauvegarde(self):
        self.comboBox_charger.clear()
        try:
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)

            requete = "SELECT id FROM personnage;"

            cursor.execute(requete)

            values = cursor.fetchall()

            for id in values:
                self.comboBox_charger.addItem(str(id['id']))

        except mysql.connector.Error as erreur:
            print(erreur)
            
        finally:
            cursor.close()
            cnx.close()

    def _prologue(self, livre_id):
        try:
            global chapitre
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)
            param= {'id_livre' : livre_id}
            requete = "SELECT * FROM prologue WHERE id_livre = %(id_livre)s;"
            cursor.execute(requete, param)

            value = cursor.fetchone()

            self.label_chapitre.setText(value['titre'])
            self.plainTextEdit_chapitre.setPlainText(value['texte'])

            requete = "SELECT id_chapitre FROM chapitre_livre INNER JOIN chapitre ON id_chapitre = id WHERE id_livre = %(id_livre)s AND no_chapitre = 1;"
            
            cursor.execute(requete, param)
            chapitre = cursor.fetchone()
            chapitre = chapitre['id_chapitre']

            self.comboBox_destination.addItem('1')
        except mysql.connector.Error as erreur:
            print(erreur)
            
        finally:
            
            cursor.close()
            cnx.close()

    def _combox_navigation(self):
        try:
            global chapitre
            self.comboBox_destination.clear()

            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)
            
            param = {'id_chapitre' : chapitre}
            
            requete = "SELECT no_chapitre FROM chapitre INNER JOIN lien_chapitre ON id = id_chapitre_destination WHERE id_chapitre_origine = %(id_chapitre)s ;"
            cursor.execute(requete, param)

            value = cursor.fetchall()
            for chapitres in value:
                self.comboBox_destination.addItem(str(chapitres['no_chapitre']))
        
        except mysql.connector.Error as erreur:
            print(erreur)

        finally:
            cursor.close()
            cnx.close()

    def _changement_chapitre(self):
        try:
            global chapitre
            global id_sauvegarde
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)
            
            
            no_chapitre = int(self.comboBox_destination.currentText())
            self.comboBox_destination.clear()

            param= {'livre' : livre_id, 'no_chapitre': no_chapitre}
            requete = "SELECT * FROM chapitre INNER JOIN chapitre_livre ON id_chapitre = id WHERE id_livre = %(livre)s and id_chapitre = %(no_chapitre)s; "
            cursor.execute(requete, param)

            value = cursor.fetchone()
            
            chapitre = value['id']

            self.label_chapitre.setText(str(value['no_chapitre']))
            self.plainTextEdit_chapitre.setPlainText(value['texte'])
            self._combox_navigation()

        except mysql.connector.Error as erreur:
            print(erreur)

        finally:
            cursor.close()
            cnx.close()

    def _afficher_arme(self):
        try:
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)

            requete = "SELECT nom FROM arme;"

            cursor.execute(requete)
            armes = cursor.fetchall()

            for arme in armes:
                self.comboBox_arme_1.addItem(arme['nom'])
                self.comboBox__arme_2.addItem(arme['nom'])

        except mysql.connector.Error as erreur:
            print(erreur)

        finally:
            cursor.close()
            cnx.close()

    def _sup_arme(self):
        try:
            global id_sauvegarde
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)

            arme_1 = self.comboBox_arme_1.currentIndex() +1
            arme_2 = self.comboBox__arme_2.currentIndex() +1

            print(id_sauvegarde)
            param = {'id_personnage' : id_sauvegarde, 'arme_1': arme_1, 'arme_2': arme_2}

            requete = "DELETE FROM arme_personnage WHERE id_personnage =  %(id_personnage)s;"
            cursor.execute(requete, param)


        except mysql.connector.Error as erreur:
            print(erreur)

        finally:
            cnx.commit()
            cursor.close()
            cnx.close()

    def _change_arme(self):
        try:
            global id_sauvegarde
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)

            arme_1 = self.comboBox_arme_1.currentIndex() +1
            arme_2 = self.comboBox__arme_2.currentIndex() +1

            param = {'id_personnage' : id_sauvegarde, 'arme_1': arme_1, 'arme_2': arme_2}

            requete = "INSERT INTO arme_personnage VALUES ( %(arme_1)s, %(id_personnage)s, 1), ( %(arme_2)s, %(id_personnage)s, 2)"
            cursor.execute(requete, param)

        except mysql.connector.Error as erreur:
            print(erreur)

        finally:
            cnx.commit()
            cursor.close()
            cnx.close()
    
    def _afficher_kai(self):
        try:
            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)

            requete = "SELECT nom FROM discipline;"

            cursor.execute(requete)
            kais = cursor.fetchall()

            for kai in kais:
                self.comboBox_kai_1.addItem(kai['nom'])
                self.comboBox_kai_2.addItem(kai['nom'])
                self.comboBox_kai_3.addItem(kai['nom'])
                self.comboBox_kai_4.addItem(kai['nom'])
                self.comboBox_kai_5.addItem(kai['nom'])


        except mysql.connector.Error as erreur:
            print(erreur)

        finally:
            cursor.close()
            cnx.close()

    def _sup_kai(self):
        try:
            global id_sauvegarde

            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)
            
            kai_1 = self.comboBox_kai_1.currentIndex() +1
            kai_2 = self.comboBox_kai_2.currentIndex() +1
            kai_3 = self.comboBox_kai_3.currentIndex() +1
            kai_4 = self.comboBox_kai_4.currentIndex() +1
            kai_5 = self.comboBox_kai_5.currentIndex() +1

            param = {'id_personnage' : id_sauvegarde, 'kai_1': kai_1, 'kai_2': kai_2, 'kai_3': kai_3, 'kai_4': kai_4, 'kai_5': kai_5}
            requete = "DELETE FROM discipline_personnage WHERE id_personnage =  %(id_personnage)s;"
            cursor.execute(requete, param)

        except mysql.connector.Error as erreur:
            print(erreur)

        finally:
            cnx.commit()
            cursor.close()
            cnx.close()

    def _change_kai(self):
        try:
            global id_sauvegarde

            cnx = mysql.connector.connect(
                user="aventurier",
                password="dnd",
                host="localhost",
                database='tp_livre'
            ) 
            cursor = cnx.cursor(dictionary=True)
            
            kai_1 = self.comboBox_kai_1.currentIndex() +1
            kai_2 = self.comboBox_kai_2.currentIndex() +1
            kai_3 = self.comboBox_kai_3.currentIndex() +1
            kai_4 = self.comboBox_kai_4.currentIndex() +1
            kai_5 = self.comboBox_kai_5.currentIndex() +1

            param = {'id_personnage' : id_sauvegarde, 'kai_1': kai_1, 'kai_2': kai_2, 'kai_3': kai_3, 'kai_4': kai_4, 'kai_5': kai_5}

            requete = "INSERT INTO discipline_personnage VALUES ( %(kai_1)s, %(id_personnage)s, 1), (%(kai_2)s, %(id_personnage)s, 2), (%(kai_3)s, %(id_personnage)s, 3), (%(kai_4)s, %(id_personnage)s, 4), (%(kai_5)s, %(id_personnage)s, 5);"
            cursor.execute(requete, param)

        except mysql.connector.Error as erreur:
            print(erreur)

        finally:
            cnx.commit()
            cursor.close()
            cnx.close()

app = QApplication([])

window = MainWindow()
window.show()
app.exec()