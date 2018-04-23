import datetime
# res_data = [{'ReturningConversions': u'0.540192566055', 'SessionDuration': u'185.502303862', 'BounceRate': u'63.4807256236', 'UniqueConversions': u'0.0', 'MobileTablet': u'495', u'date': datetime.date(2017, 10, 14)}, {'ReturningConversions': u'0.283026898195', 'SessionDuration': u'161.418952909', 'BounceRate': u'67.6568047843', 'UniqueConversions': u'0.149253731343', 'MobileTablet': u'491', u'date': datetime.date(2017, 10, 15)}, {'ReturningConversions': u'0.32449772388', 'SessionDuration': u'179.711127212', 'BounceRate': u'65.5844833951', 'UniqueConversions': u'0.0649756341372', 'MobileTablet': u'617', u'date': datetime.date(2017, 10, 16)}, {'ReturningConversions': u'0.672080238365', 'SessionDuration': u'195.820754336', 'BounceRate': u'72.0737837743', 'UniqueConversions': u'0.214920079064', 'MobileTablet': u'649', u'date': datetime.date(2017, 10, 17)}, {'ReturningConversions': u'0.376976579905', 'SessionDuration': u'182.245943157', 'BounceRate': u'64.6274137367', 'UniqueConversions': u'0.374277791481', 'MobileTablet': u'577', u'date': datetime.date(2017, 10, 18)}]
# lst = []
# keys = res_data[0].keys()
# new = {}
# for key in keys:
#     if key != 'country' and key != 'date':
#         x = 0
#         for data in res_data:
#             x += int(float(data[key]))
#         new[key] = x
# lst.append(new)
# print lst

# dates = {'prv_end': u'04/16/2018', 'pre_end': u'04/16/2018', 'prv_start': u'04/15/2018', 'pre_start': u'04/15/2018'}
# def date_converter(dates):
#     newdates = {}
#     for key, value in dates.iteritems():
#         date = dates[key].split('/')
#         newdates[key] = date[2]+'-'+date[0]+'-'+date[1]
#     return newdates

# res_data = [{'totalSessions': 71129, u'country': u'UK'}, {'totalSessions': 9210, u'country': u'India'}, {'totalSessions': 57473, u'country': u'US'}, {'totalSessions': 14142, u'country': u'France'}, {'totalSessions': 8658, u'country': u'China'}, {'totalSessions': 9554, u'country': u'SEA'}, {'totalSessions': 6951, u'country': u'ANZ'}, {'totalSessions': 54144, 'country': 'ROW'}, {'totalSessions': 231261, 'country': 'Total'}]

# sort_list = ['UK', 'US', 'France', 'China', 'India', 'SEA', 'ANZ', 'ROW', 'Total']
#
# new_data = []
#
# for item in sort_list:
#     i = 0
#     condition = True
#     while condition:
#         if res_data[i]['country']==item:
#             new_data.append(res_data[i])
#             condition = False
#         i += 1
# print(new_data)

# import calendar
# prev_month, year = int(datetime.datetime.now().strftime('%m'))-1, int((datetime.datetime.now().strftime('%Y-%m')).split('-')[0])
# num_days = calendar.monthrange(year, prev_month)
# pre_start = datetime.date(year, prev_month, 1)
# pre_end = datetime.date(year, prev_month, num_days[1])
# year = year if prev_month != 1 else year-1
# prev_month = (prev_month-1) if prev_month != 1 else 12
# num_days = calendar.monthrange(year, prev_month)
# prv_start = datetime.date(year, prev_month, 1)
# prv_end = datetime.date(year, prev_month, num_days[1])
#
# print pre_start.strftime('%Y-%m-%d')
# print pre_end.strftime('%Y-%m-%d')
# print prv_start.strftime('%Y-%m-%d')
# print prv_end.strftime('%Y-%m-%d')


devices = [{'Device': 'Desktop', 'Goal Completions': 68, 'Change': '-33.98%', 'Previous': 103}, {'Device': 'Mobile', 'Goal Completions': 24, 'Change': '33.33%', 'Previous': 18},{'Device': 'Tablet', 'Goal Completions': 3, 'Change': '-50.0%', 'Previous': 6}]

for item in devices:
    print item

print ['Devices', 'Goal Completions']

for item in devices:
    print [item['Device'], item['Goal Completions']]
