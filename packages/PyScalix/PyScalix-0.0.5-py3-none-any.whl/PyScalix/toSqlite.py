import sqlite3
import csv
import os


class CsvToSqlite:

    @staticmethod
    def tosqlite(csvfile):
        flag = False
        try:
            table_name = os.path.basename(csvfile).split('.')[0]
            dbfile = table_name+".sqlite"
            if os.path.exists(dbfile):
                os.remove(dbfile)
            conn = sqlite3.connect(dbfile)
            cursor = conn.cursor()
            with open(csvfile, 'r', encoding='utf-8') as file:
                for n, line in enumerate(file):
                    if n == 0:
                        columns = line.strip().split(',')
                        cursor.execute(
                            f'CREATE TABLE {table_name} ({", ".join(columns)})')
                    else:
                        try:
                            cursor.execute(
                                f"INSERT INTO {table_name} VALUES ({', '.join('?' * len(columns))})", line.strip().split(','))
                        except Exception as e:
                            print(e)
                conn.commit()
                flag = True
        except Exception as e:
            flag = False
        return flag
