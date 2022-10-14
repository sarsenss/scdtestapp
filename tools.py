import logging

FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('tcpserver')


def predict(input_model, img_path, save_dir='output_images'):
    logger.info('Started detection ...')
    result = input_model(img_path)
    logger.info('Detection completed')
    text, percent = result.process_text()
    logger.info('Detection text %s', text)
    result.save(save_dir)
    logger.info('Output photo saved')

    return text, percent