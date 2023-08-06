import sqlite3
import csv
import os


class CsvToSqlite:

    @staticmethod
    def tosqlite(csvfile):
        flag = False
        try:
            flag = True
            table_name = os.path.basename(csvfile).split('.')[0]
            dbfile = table_name+".sqlite"
            if os.path.exists(dbfile):
                os.remove(dbfile)
            conn = sqlite3.connect(dbfile)
            cursor = conn.cursor()
            with open(csvfile, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                column_names = next(reader)
                columns = ["?" for i in range(len(column_names))]
                cursor.execute(
                    f'CREATE TABLE {table_name} ({", ".join(column_names)})')
                cursor.executemany(
                    f'INSERT INTO {table_name} VALUES ({", ".join(columns)})', reader)
            conn.commit()
            conn.close()
        except:
            flag = False
        return flag
