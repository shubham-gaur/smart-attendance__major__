#!/usr/bin/python
import sys  
#reload(sys)  
#sys.setdefaultencoding('utf8')
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
import PIL
from PIL import Image

##===============================================

class DatabaseUtility: 
	def __init__(self, database, tableName):
		self.db = database
		self.tableName = tableName

		self.cnx = mysql.connector.connect(user = 'root',password = '2406',host = '127.0.0.1')
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

	def CreateTable(self):
		cmd = (" CREATE TABLE IF NOT EXISTS " + self.tableName + " ("
			" `ID` int(5) NOT NULL AUTO_INCREMENT,"
			" `username` char(50) NOT NULL,"
			" `password` char(50) NOT NULL,"
			" PRIMARY KEY (`ID`)"
			") ENGINE=InnoDB;")
		self.RunCommand(cmd)

	def GetTable(self):
		self.CreateTable()
		return self.RunCommand("SELECT * FROM %s;" % self.tableName)

	def GetColumns(self):
		return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName)

	def RunCommand(self, cmd):
		print ("RUNNING COMMAND: " + cmd)
		try:
			self.cursor.execute(cmd)
		except mysql.connector.Error as err:
			print ('ERROR MESSAGE: ' + str(err.msg))
			print ('WITH ' + cmd)
		try:
			msg = self.cursor.fetchall()
		except:
			msg = self.cursor.fetchone()
		return msg

	def AddEntryToAdmin(self, username, password):
		
		cmd = " INSERT INTO " + self.tableName + " (username, password)"
		cmd += " VALUES ('%s','%s');" % (username, password)
		self.RunCommand(cmd)

	def AddEntryToStudent(self, name, enrollment, branch, year):
		cmd = " INSERT INTO " + self.tableName + "(enrollment,StudentName,branch,year)" 
		cmd += "VALUES ('%s','%s','%s','%s');"%(enrollment,name,branch,year)
		self.RunCommand(cmd)

	def AddEntryToFaculty(self, name,subject):
		cmd = " INSERT INTO " + self.tableName + "(name,subject)" 
		cmd += "VALUES ('%s','%s');"%(name,subject)
		self.RunCommand(cmd)

	
	def __del__(self):
		self.cnx.commit()
		self.cnx.close()

##===============================================
##===============================================


if __name__ == '__main__':
	db = 'UsernamePassword_DB'
	tableName = 'masterTable'

	dbu = DatabaseUtility(db, tableName)

	# dbu.AddEntryToTable ('asdf', 'asdf')
	# print (dbu.GetColumns())
	# print (dbu.GetTable())
	
