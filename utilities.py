from datetime import timedelta,date
import calendar
import datetime
from collections import defaultdict
'''hbsytdbufeanjodiyfubaheicuaysdgechuyebcdhyusbdefcuysdhefyedc'''


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

def getweekdates(D):

    prev_month = int(datetime.datetime.now().strftime('%m')) - 1
    year = int((datetime.datetime.now().strftime('%Y-%m')).split('-')[0])
    num_days = calendar.monthrange(year, prev_month)
    pre_monthend = datetime.date(year, prev_month, num_days[1])
    pre_start = datetime.date(year, prev_month, 1)
    pre_end = pre_start.replace(day=D)
    year = year if prev_month != 1 else year - 1
    prev_month = (prev_month - 1) if prev_month != 1 else 12
    num_days = calendar.monthrange(year, prev_month)
    prv_monthend = datetime.date(year, prev_month, num_days[1])
    prv_start = datetime.date(year, prev_month, 1)
    prv_end = prv_start.replace(day=D)

    pre_MonthName= pre_start.strftime('%B')
    prv_MonthName= prv_start.strftime('%B')

    pre_start2 = pre_end.replace(day=D+1)
    pre_end2 = pre_start2.replace(day=pre_start2.day+D-1)
    prv_start2 = prv_end.replace(day=D+1)
    prv_end2 = prv_start2.replace(day=prv_start2.day+D-1)

    pre_start3 = pre_end2.replace(day=pre_end2.day + 1)
    pre_end3 = pre_start3.replace(day=pre_start3.day + D - 1)
    prv_start3 = prv_end2.replace(day=prv_end2.day + 1)
    prv_end3 = prv_start3.replace(day=prv_start3.day + D - 1)

    pre_start4 = pre_end3.replace(day=pre_end3.day + 1)
    pre_end4 = pre_monthend
    prv_start4 = prv_end3.replace(day=prv_end3.day + 1)
    prv_end4 = prv_monthend

    return {'pre_start': pre_start.strftime('%Y-%m-%d'),
            'pre_end': pre_end.strftime('%Y-%m-%d'),
            'prv_start': prv_start.strftime('%Y-%m-%d'),
            'prv_end': prv_end.strftime('%Y-%m-%d'),
            'pre_start2': pre_start2.strftime('%Y-%m-%d'),
            'pre_end2': pre_end2.strftime('%Y-%m-%d'),
            'prv_start2': prv_start2.strftime('%Y-%m-%d'),
            'prv_end2': prv_end2.strftime('%Y-%m-%d'),
            'pre_start3': pre_start3.strftime('%Y-%m-%d'),
            'pre_end3': pre_end3.strftime('%Y-%m-%d'),
            'prv_start3': prv_start3.strftime('%Y-%m-%d'),
            'prv_end3': prv_end3.strftime('%Y-%m-%d'),
            'pre_start4': pre_start4.strftime('%Y-%m-%d'),
            'pre_end4': pre_end4.strftime('%Y-%m-%d'),
            'prv_start4': prv_start4.strftime('%Y-%m-%d'),
            'prv_end4': prv_end4.strftime('%Y-%m-%d'),
            'pre_MonthName': pre_MonthName,
            'prv_MonthName': prv_MonthName,
            }

def get12months():
    # print int(datetime.datetime.now().strftime('%m'))
    prev_month = date.today().month - 1
    year = int((datetime.datetime.now().strftime('%Y-%m')).split('-')[0])
    print(year)
    num_days = calendar.monthrange(year, prev_month)
    # print(num_days)
    pre_start = datetime.date(year, prev_month, 1)
    pre_end = datetime.date(year, prev_month, num_days[1])
    year = year if prev_month != 1 else year - 1
    prev_month = (prev_month - 1) if prev_month != 1 else 12
    num_days = calendar.monthrange(year, prev_month)
    prv_start = datetime.date(year, prev_month, 1)
    prv_end = datetime.date(year, prev_month, num_days[1])

    print pre_start,pre_end,'\n',prv_start,prv_end

def change(source,result):
    present, previous = [], []
    for item in result['session_category']:
        present.append(item[source])
    for item in result['session_category_prev']:
        previous.append(item[source])
    Change = []
    for i in range(len(previous)):
        change = round(((float(present[i]) - float(previous[i])) / float(previous[i])) * 100, 2) if previous[                                                                                             i] != 0 else 100
        Change.append(change)
    return Change

def line_results():
    from ResultsServices.sessions_category_results import SessionsCategoryResults

    linedates = getweekdates(7)

    session_category_line1 = SessionsCategoryResults(linedates['pre_start'], linedates['pre_end'],
                                                     linedates['prv_start'], linedates['prv_end'])
    session_category_line2 = SessionsCategoryResults(linedates['pre_start2'], linedates['pre_end2'],
                                                     linedates['prv_start2'], linedates['prv_end2'])
    session_category_line3 = SessionsCategoryResults(linedates['pre_start3'], linedates['pre_end3'],
                                                     linedates['prv_start3'], linedates['prv_end3'])
    session_category_line4 = SessionsCategoryResults(linedates['pre_start4'], linedates['pre_end4'],
                                                     linedates['prv_start4'], linedates['prv_end4'])
    lineresults = {'session_category_line1': session_category_line1.main()[0][10],
                   'session_category_line2': session_category_line2.main()[0][10],
                   'session_category_line3': session_category_line3.main()[0][10],
                   'session_category_line4': session_category_line4.main()[0][10],
                   }
    return lineresults


def line_results_region():
    from ResultsServices.sessions_results import SessionsResults
    linedatesregion  = getweekdates(7)
    session_line1 = SessionsResults(linedatesregion['pre_start'], linedatesregion['pre_end'],
                                    linedatesregion['prv_start'], linedatesregion['prv_end'])
    session_line2 = SessionsResults(linedatesregion['pre_start2'], linedatesregion['pre_end2'],
                                    linedatesregion['prv_start2'], linedatesregion['prv_end2'])
    session_line3 = SessionsResults(linedatesregion['pre_start3'], linedatesregion['pre_end3'],
                                    linedatesregion['prv_start3'], linedatesregion['prv_end3'])
    session_line4 = SessionsResults(linedatesregion['pre_start4'], linedatesregion['pre_end4'],
                                    linedatesregion['prv_start4'], linedatesregion['prv_end4'])

    lineregionresults = {'session_line1': session_line1.main(),'session_line2': session_line2.main(),
                         'session_line3': session_line3.main(),'session_line4': session_line4.main()}
    return lineregionresults

def get_month_names(date1, date2):

    month1 = calendar.month_name[int(date1.split("-")[1])]
    month2 = calendar.month_name[int(date2.split("-")[1])]
    return(month1, month2)


if __name__ == '__main__':
    line_results()