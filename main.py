import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(massage)s')
logging.debug("debug")
logging.info("info")
logging.error("погано написав програму error")
logging.warning("warning")
logging.critical("critical")

try:
    print(10/0)
except Exception:
    logging.exception("Kkk")
#факторіал числа

def factorial(n):
    logging.info('Розпочато обчислення факторіалу числа')
    result=1
    for i in range(1,n+1):
        result*=i
    logging.info(f"Обчислення факторіалу {n} числа завершено.Результат виконання: {result}")
factorial(5)