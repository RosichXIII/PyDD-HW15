# - Добавьте возможность запуска из командной строки.
# - При этом значение любого параметра можно опустить.
#       В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# - Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

from calendar_base import str_to_date
import argparse
from datetime import datetime

if __name__ == '__main__':
    months = { 1: 'янв',  2: 'фев' ,  3: 'мар',  4:  'апр', 5: 'май', 6: 'июн' ,  7: 'июл',  8: 'авг',  9: 'сен',  10: 'окт',
               11: 'ноя',  12: 'дек'}
    weekdays = {'по': 1, 'вт': 2,'ср': 3,'че': 4,'пя': 5,'су': 6,'во': 7}

    parser = argparse.ArgumentParser()
    parser.add_argument('-ordinal_day', type=str, default='1')
    parser.add_argument('-weekday', type=str, default='по')
    parser.add_argument('-month', type=str, default=months[datetime.now().month])

    args = parser.parse_args()

    weekday = weekdays[int(args.weekday)] if args.weekday.isdigit() and int(args.weekday) in weekdays else args.weekday
    month = months[int(args.month)] if args.month.isdigit() and int(args.month) in months else args.month

    print(f'{args.ordinal_day} {weekday} {month}: ', str_to_date(f'{args.ordinal_day} {weekday} {month}'))

    # запуск из командной строки:
    # python calendar_cmd.py -ordinal_day='2-й' -weekday='понедельник'
    # python calendar_cmd.py -ordinal_day='3-я' -weekday=6 - month=6