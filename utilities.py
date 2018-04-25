from datetime import timedelta
import calendar
import datetime
from collections import defaultdict


def group(req_data, group_by=None):
    groups = defaultdict(list)
    res_data = [item.__dict__ for item in req_data]
    def del_key(d):
        del d['_sa_instance_state']
        del d['id']
        return d
    res_data = map(del_key, res_data)
    if group_by is not None:
        for obj in res_data:
            groups[obj[group_by]].append(obj)
        res_data1 = groups.values()
        res_data = []
        for item in res_data1:
            keys = item[0].keys()
            new = {}
            for key in keys:
                if key != 'country' and key != 'date':
                    x = 0
                    for data in item:
                        x += int(float(data[key]))
                    new[key] = x
                elif key == 'country':
                    new[key] = item[0][key]
            res_data.append(new)
    return res_data

def date_converter(dates):
    newdates = {}
    for key, value in dates.iteritems():
        date = dates[key].split('/')
        newdates[key] = date[2]+'-'+date[0]+'-'+date[1]
    return newdates

def get_dates(N):

    pre_end = datetime.datetime.now() - timedelta(days=1)
    pre_start = datetime.datetime.now() - timedelta(days=N)
    prv_end = pre_start - timedelta(days=1)
    prv_start = prv_end - timedelta(days=N)
    return {'pre_start': pre_start.strftime('%Y-%m-%d'),
            'pre_end': pre_end.strftime('%Y-%m-%d'),
            'prv_start': prv_start.strftime('%Y-%m-%d'),
            'prv_end': prv_end.strftime('%Y-%m-%d')
            }

def get_two_month_dates():

    prev_month = int(datetime.datetime.now().strftime('%m')) - 1
    year = int((datetime.datetime.now().strftime('%Y-%m')).split('-')[0])
    num_days = calendar.monthrange(year, prev_month)
    pre_start = datetime.date(year, prev_month, 1)
    pre_end = datetime.date(year, prev_month, num_days[1])
    year = year if prev_month != 1 else year - 1
    prev_month = (prev_month - 1) if prev_month != 1 else 12
    num_days = calendar.monthrange(year, prev_month)
    prv_start = datetime.date(year, prev_month, 1)
    prv_end = datetime.date(year, prev_month, num_days[1])

    return {'pre_start': pre_start.strftime('%Y-%m-%d'),
            'pre_end': pre_end.strftime('%Y-%m-%d'),
            'prv_start': prv_start.strftime('%Y-%m-%d'),
            'prv_end': prv_end.strftime('%Y-%m-%d')
            }