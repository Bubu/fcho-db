import pymysql
import smtplib

class memberEntry:
    def __init__(self, data):
        self.number = data[0]
        self.name = (data[1],data[2])
        self.title = data[3]
        self.industry = data[4]
        self.work = data[5]
        self.homepage = data[10]
        self.phones = (data[11],data[12],data[13])
        self.adresses = ((data[14],data[15],data[16],data[17],data[18],data[19]),(data[20],data[21],data[22],data[23],data[24],data[25]),(data[26],data[27],data[28],data[29],data[30],data[31]))

    def outputPdf(self):
        pass

    def outputHtml(self):
        pass
    


if __name__ == "__main__":
    print('Connecting to DB')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='pyscripts', passwd='*1xwX@eJ1W2L', database='FChO')
    cur = conn.cursor()
    cur.execute("SELECT Mitgliedsnummer, Name, Vorname, Titel, Branche, tätig_bei, Datenfreigabe, Mitgliederpost, nuremail, email, homepage, Telefon_1, Telefon_2, Telefon_3, Adresszusatz_1a, Adresszusatz_1b, Straße_1, PLZ_1, Ort_1, Land_1, Adresszusatz_2a, Adresszusatz_2b, Straße_2, PLZ_2, Ort_2, Land_2, Adresszusatz_3a, Adresszusatz_3b, Straße_3, PLZ_3, Ort_3, Land_3 FROM Mitglieder WHERE 1")
    members = []
    for row in cur:
        members.append(memberEntry(row))
    cur.close()
    conn.close()
