import logging
import sysconf


def logger_config(log_path, logging_name):
    '''
    配置log
    :param log_path: 输出log路径
    :param logging_name: 记录中name，可随意
    :return:
    '''
    '''
    logger是日志对象，handler是流处理器，console是控制台输出（没有console也可以，将不会在控制台输出，会在日志文件中输出）
    '''
    # 获取logger对象,取名
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"
    logging_level = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    if sysconf.LOGGING_LEVEL in logging_level:
        logging.basicConfig(level=logging_level[sysconf.LOGGING_LEVEL], format=LOG_FORMAT, datefmt=DATE_FORMAT)
    else:
        print("日志等级设置错误，启用默认配置！")
        logging.basicConfig(level=logging_level["ERROR"], format=LOG_FORMAT, datefmt=DATE_FORMAT)

    logger = logging.getLogger(logging_name)
    # 输出DEBUG及以上级别的信息，针对所有输出的第一层过滤
    logger.setLevel(level=logging.DEBUG)
    # 获取文件日志句柄并设置日志级别，第二层过滤
    handler = logging.FileHandler(log_path, encoding='UTF-8')
    handler.setLevel(logging.INFO)
    # 生成并设置文件日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # console相当于控制台输出，handler文件输出。获取流句柄并设置日志级别，第二层过滤
    # console = logging.StreamHandler()
    # console.setLevel(logging.DEBUG)
    # 为logger对象添加句柄
    logger.addHandler(handler)
    # logger.addHandler(console)
    return logger
