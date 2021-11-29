

import logging


def make_logger(old_function):

    def function(a, b, c):

        logging.basicConfig(filename='myapp.log', filemode='w',
                            format='[%(asctime)s] [%(levelname)s] [%(lineno)d] [%(pathname)s]=> %(message)s',
                            level=logging.DEBUG)
        if c != 0:
            logging.info(f'Started function {old_function.__name__}\nInput data: a = {a}, b = {b}, c = {c} ')
            result = old_function(a, b, c)
            logging.info(f'Finished function {old_function.__name__}\nOutput data: result = {result}')
            return result
        else:

            logging.debug(f'Деление на ноль')

    return function

@make_logger
def summator(a, b, t):
    return (a + b)/t


if __name__ == '__main__':
  summator(62, 75, 65)

