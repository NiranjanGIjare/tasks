from datetime import datetime
import logging
import manager
#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
#logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

logging.info("=====================================")
logging.info("||            WEL-COME             ||")
logging.info("=====================================")
logging.info("initializing")
manager.check_and_init_db_creads()
