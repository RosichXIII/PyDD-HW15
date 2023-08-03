# Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
# - Преобразуйте его в дату в текущем году.
# - Логируйте ошибки, если текст не соответсвует формату.

import logging
from datetime import datetime, date

logging.basicConfig(filename='Calendar.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

months = {'янв': 1, 'фев': 2,'мар': 3,'апр': 4,'май': 5,'июн': 6,'июл': 7,'авг': 8,'сен': 9,'окт': 10,'ноя': 11,'дек': 12}
weekdays = {'по': 1, 'вт': 2,'ср': 3,'че': 4,'пя': 5,'су': 6,'во': 7}

def str_to_date(text: str):
    try:
        year = datetime.now().year
        ordinal_day, weekday_value, month_value = text.split()        
        month = months[month_value[:3]]
        weekday = weekdays[weekday_value[:2]] - 1
        ordinal_day = int(ordinal_day[0])
    except Exception as exc:
        logger.info(f'{ordinal_day}-й  {weekday_value}  {month_value} {year} =  ошибка: {exc}')

    ordinal_week = 0
    for day in range (1, 31 + 1):
        result = date(year=year, month=month, day=day)
        if result.weekday() == weekday:
            ordinal_week += 1
            if ordinal_week == ordinal_day:
                logger.info(f'{ordinal_day}-й {weekday_value} {month_value} {year} = {result} ')
                return result

if __name__ == '__main__':
    print('4-й вторник апреля:', str_to_date('4-й вторник апреля'))
    print('2-я суббота июля:', str_to_date('2-я суббота июля'))
    print('3-й четверг сентября:', str_to_date('3-й четверг сентября'))