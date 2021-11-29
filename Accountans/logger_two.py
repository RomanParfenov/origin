
import logging


def make_logger_two(old_function):

    def function(*args, **kwargs):
        logging.basicConfig(filename='myapp.log', filemode='w',
                            format='[%(asctime)s] [%(levelname)s] [%(lineno)d] [%(pathname)s]=> %(message)s',
                            level=logging.INFO)
        logging.info(f'Started function {old_function.__name__}\nInput data: a = {args} and b = {kwargs}')
        result = old_function(*args, **kwargs)
        logging.info(f'Finished function {old_function.__name__}\nOutput data: result = {result}')
        return result

    return function


# @make_logger_two




