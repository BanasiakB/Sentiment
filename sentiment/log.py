import logging

def setup_log():
    logging.basicConfig(level=logging.INFO, filename=f'log.log', 
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler('log.log')
    handler.setFormatter(formatter)
    logging.getLogger().handlers = [handler]