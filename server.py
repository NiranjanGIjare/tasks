from datetime import datetime
import logging
import manager
import database
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

logging.info("=====================================")
logging.info("||            WEL-COME             ||")
logging.info("=====================================")
logging.info("initializing")
db_creads=manager.check_and_init_db_creads()
db=database.DB_handler(db_creads['DB_HOST'],db_creads['USER'],db_creads['PASSWORD'])
db.check_version()
