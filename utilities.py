from datetime import datetime, timedelta
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

def get_dates(N):

    pre_end = datetime.now() - timedelta(days=1)
    pre_start = datetime.now() - timedelta(days=N)
    prv_end = pre_end - timedelta(days=1)
    prv_start = prv_end - timedelta(days=N)

    return {'pre_start': pre_start.strftime('%Y-%m-%d'),
            'pre_end': pre_end.strftime('%Y-%m-%d'),
            'prv_start': prv_start.strftime('%Y-%m-%d'),
            'prv_end': prv_end.strftime('%Y-%m-%d')
            }

def date_converter(dates):
    newdates = {}
    for key, value in dates.iteritems():
        date = dates[key].split('/')
        newdates[key] = date[2]+'-'+date[0]+'-'+date[1]
    return newdates