__author__ = 'raven'

import sqlite3
import time

_connection = None
_TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


def init(db_file):
    global _connection
    _connection = sqlite3.connect(db_file)


def _convert_time(param):
    return time.mktime(param)


def check_image_by_date(dt):
    c = _connection.cursor()
    c.execute('select count(id) from images where entry_time = ?', (dt,))
    result = c.fetchone()[0] > 0
    c.close()
    return result


def store_image(image_data):
    dt = _convert_time(image_data['date'])
    if check_image_by_date(dt):
        return False
    template = "insert into images(title, desc, entry_time, uri, image) values (?, ?, ?, ?, ?)"
    c = _connection.cursor()
    c.execute(template, (image_data['title'],
                         image_data['summary'],
                         dt,
                         image_data['image_uri'],
                         image_data['data']))
    _connection.commit()
    c.close()
    return True


def get_latest_image():
    c = _connection.cursor()
    c.execute('select uri, desc, image from images order by entry_time desc limit 1')
    row = c.fetchone()
    c.close()
    if row is None:
        return None
    else:
        return {'url': row[0],
                'summary': row[1],
                'data': row[2]}


def log_access(time, ip):
    c = _connection.cursor()
    c.execute('insert into access(time, ip) values (?, ?)', (time.strftime(_TIME_FORMAT), ip))
    _connection.commit()
    c.close()