import pymysql
import logging


class DB_handler:	
	def __init__(self,withoutdb=False):
		db_creads=DB_handler.check_and_init_db_creads('/etc/tasksdb.conf')
		if(withoutdb):
			self.create_db_handler(db_creads['DB_HOST'],db_creads['USER'],db_creads['PASSWORD'],"")
			self.initialize_database()
		self.create_db_handler(db_creads['DB_HOST'],db_creads['USER'],db_creads['PASSWORD'],db_creads['DATABASE'])

	def create_db_handler(self, db_host, user, password, database='tasks'):
		try:
			self.db = pymysql.connect(db_host,user,password,database )
			self.cursor = self.db.cursor()
		except Exception as e:
			logging.error(e)
			exit(1)

	def check_version(self):
		self.cursor.execute("SELECT VERSION()")
		data = self.cursor.fetchone()
		print ("Database version : %s " % data)

	def check_and_init_db_creads(conf_file):
		try:
	                file_reader=open(conf_file,'r')
	                creads=file_reader.read()
	                creads=creads.split('\n')
	                if creads[-1]=="":
	                        creads=creads[:-1:]
	                db_creads=dict()
	                for cred in creads:
	                        cred=cred.split(':')
	                        if cred[0] in db_creads:
	                                raise Exception("Repetative element found in conf file")
	                        else:
	                                db_creads[cred[0]]=cred[1]
		except Exception as e:
	                logging.error("Something went wrong with db file")
	                logging.error(e)
		finally:
	                try:
	                        file_reader.close()
	                except:
	                        pass
		return db_creads

	def initialize_database(self, database="tasks"):
		self.cursor.execute("DROP DATABASE IF EXISTS "+database+";")
		data = self.cursor.fetchone()
		print("Data base dropped")
		self.cursor.execute("CREATE DATABASE  "+database+";")
		data = self.cursor.fetchone()
		print("Database created")
		self.cursor.execute("USE " + database +";")
		self.cursor.execute("CREATE TABLE tasks (id  int NOT NULL AUTO_INCREMENT KEY, title VARCHAR(20), status VARCHAR(10), description VARCHAR(20),time_created DATETIME, deadline DATETIME );")
