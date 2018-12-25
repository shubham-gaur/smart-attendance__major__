import mysql.connector
import datetime
from time import strftime
from datetime import datetime as date
from os.path import join,basename
from pyfacesgui import *

#global student
#student=basename(matchfile)            

class DatabaseUtility: 
    def __init__(self, database, tableName):
        self.db = database
        self.tableName = tableName

        # Open database connection
        self.cnx = mysql.connector.connect(user = 'root',password = '2406',host = '127.0.0.1')
        # prepare a cursor object using cursor() method
        self.cursor = self.cnx.cursor()

        self.ConnectToDatabase()
        #self.CreateTable()


    def ConnectToDatabase(self):
        try:
            self.cnx.database = self.db
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.CreateDatabase()
                self.cnx.database = self.db
            else:
                print(err.msg)

    def CreateDatabase(self):
        try:
            self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" %self.db)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))

    def Attendence(self, student, dt, dy , t):
                cmd = "replace into attendence(enrollment,date,day,time) values ('%s','%s','%s','%s' );" %(student,dt,dy,t)
                try:
                    self.cursor.execute(cmd);
                    print "done"
                except mysql.connector.Error as err:
                    self.cnx.rollback()
                    print err
                self.cnx.commit()

    def __del__(self):
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()

#===============================================
#===============================================

if __name__ == '__main__':
    db = 'db'
    tableName = 'attendence'
    dbu = DatabaseUtility(db, tableName)
