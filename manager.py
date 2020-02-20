import logging


def check_and_init_db_creads():
	try:
		file_reader=open('/etc/tasksdb.conf','r')
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
		print(db_creads)
	except Exception as e:
		logging.error("Something went wrong with db file")
		logging.error(e)
	finally:
		try:
			file_reader.close()
		except:
			pass
