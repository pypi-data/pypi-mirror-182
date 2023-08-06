import sqlite3
import csv


class SqliteToCsv:

    @staticmethod
    def tocsv(databasefile, tablename):
        flag = False
        try:
            conn = sqlite3.connect(databasefile)
            c = conn.cursor()
            c.execute(f"SELECT * FROM {tablename}")
            with open(tablename+".csv", 'w', newline='', encoding='utf8') as f:
                writer = csv.writer(f)
                writer.writerow([d[0] for d in c.description])
                writer.writerows(c)
            c.close()
            conn.close()
            flag = True
        except:
            flag = False
        return flag
