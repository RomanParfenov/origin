

import logging


def make_logger(parametr):
    def decor(old_function):
        def function(*args, **kwars):

            logging.basicConfig(filename='myapp.log', filemode='w',
                            format='[%(asctime)s] [%(levelname)s] [%(lineno)d] [%(pathname)s]=> %(message)s',
                            level=logging.DEBUG)
            if args[2] != 0:
                logging.info(f'Started function {old_function.__name__}\nInput data: a = {args}, b = {kwars},'
                             f'path_log ={parametr}')
                result = old_function(*args, **kwars)
                logging.info(f'Finished function {old_function.__name__}\nOutput data: result = {result}')
                return result
            else:
                logging.debug(f'Input data: a = {args}, b = {kwars}\nДеление на ноль, path_log ={parametr}')
                print(f'Деление на ноль')

        return function

    return decor


@make_logger(' C:/users')
def summator(a, b, t):
    return (a + b)/t



if __name__ == '__main__':

  summary = summator(62, 540, 0)
  print('result: ', summary)

