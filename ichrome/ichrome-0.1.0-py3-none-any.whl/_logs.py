import logging


def init_logger():
    logger = logging.getLogger("ichrome")
    logger.setLevel(logging.INFO)
    hd = logging.StreamHandler()
    formatter_str = (
        "%(asctime)s %(levelname)-5s [%(name)s] %(filename)s(%(lineno)s): %(message)s"
    )
    formatter = logging.Formatter(formatter_str, datefmt="%Y-%m-%d %H:%M:%S")
    hd.setLevel(logging.DEBUG)
    hd.setFormatter(formatter)
    logger.addHandler(hd)
    return logger


ichrome_logger = init_logger()

if __name__ == "__main__":
    # logger.setLevel(logging.INFO)
    logger.debug(1)
    logger.info(1)
