import datetime
res_data = [{'ReturningConversions': u'0.540192566055', 'SessionDuration': u'185.502303862', 'BounceRate': u'63.4807256236', 'UniqueConversions': u'0.0', 'MobileTablet': u'495', u'date': datetime.date(2017, 10, 14)}, {'ReturningConversions': u'0.283026898195', 'SessionDuration': u'161.418952909', 'BounceRate': u'67.6568047843', 'UniqueConversions': u'0.149253731343', 'MobileTablet': u'491', u'date': datetime.date(2017, 10, 15)}, {'ReturningConversions': u'0.32449772388', 'SessionDuration': u'179.711127212', 'BounceRate': u'65.5844833951', 'UniqueConversions': u'0.0649756341372', 'MobileTablet': u'617', u'date': datetime.date(2017, 10, 16)}, {'ReturningConversions': u'0.672080238365', 'SessionDuration': u'195.820754336', 'BounceRate': u'72.0737837743', 'UniqueConversions': u'0.214920079064', 'MobileTablet': u'649', u'date': datetime.date(2017, 10, 17)}, {'ReturningConversions': u'0.376976579905', 'SessionDuration': u'182.245943157', 'BounceRate': u'64.6274137367', 'UniqueConversions': u'0.374277791481', 'MobileTablet': u'577', u'date': datetime.date(2017, 10, 18)}]
lst = []
keys = res_data[0].keys()
new = {}
for key in keys:
    if key != 'country' and key != 'date':
        x = 0
        for data in res_data:
            x += int(float(data[key]))
        new[key] = x
lst.append(new)
print lst