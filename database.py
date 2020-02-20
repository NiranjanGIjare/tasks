import pymysql
import logging

class DB_handler:
	def __init__(self, db_host, user, password, database='tasks'):
		try:
			self.db = pymysql.connect(db_host,user,password,database )
			self.cursor = self.db.cursor()
		except Exception as e:
			logging.error(e)

	def check_version(self):
		self.cursor.execute("SELECT VERSION()")
		data = self.cursor.fetchone()
		print ("Database version : %s " % data)
