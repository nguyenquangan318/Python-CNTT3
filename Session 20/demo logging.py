import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename='log.txt',
    format="%(filename)s: %(lineno)d - %(asctime)s - %(message)s"
)
log = logging.getLogger(__name__)

def divide(first_num: float, second_num:float) -> float:
    log.debug(f'Ket qua la {first_num / second_num}')
    return first_num / second_num

first = float(input('Nhập số thứ nhất: '))
log.info(f'So vua nhap la {first}')
second = float(input('Nhập số thứ hai: '))
log.info(f'So vua nhap la {second}')
divide(first, second)