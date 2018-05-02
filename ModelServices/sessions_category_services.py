from DbConnections.Db import db
from models.models import SessionsCategoryModel
from utilities import group

class SessionsCategoryService:

    model = SessionsCategoryModel

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def sort_by(res_data, sort_list):
        new_data = []
        for item in sort_list:
            i = 0
            condition = True
            while condition:
                if res_data[i]['country'] == item:
                    new_data.append(res_data[i])
                    condition = False
                i += 1
        return new_data

    def get_data(self):

        req_data = db.session.query(self.model).filter(self.model.date >= self.start_date, self.model.date <= self.end_date)
        req_data = req_data.all()
        res_data = group(req_data, 'country')
        new_dict = {
            'country': "ROW",
            'paidSearch': res_data[-1]['paidSearch']+res_data[-3]['paidSearch'],
            'direct': res_data[-1]['direct'] + res_data[-3]['direct'],
            'social': res_data[-1]['social'] + res_data[-3]['social'],
            'organicSearch': res_data[-1]['organicSearch'] + res_data[-3]['organicSearch'],
            'referral': res_data[-1]['referral']+res_data[-3]['referral'],
            'email': res_data[-1]['email'] + res_data[-3]['email'],
        }
        del res_data[-1]
        del res_data[-2]
        res_data.append(new_dict)
        sort_list = ['UK', 'US', 'France', 'China', 'India', 'SEA', 'ANZ', 'ROW']
        res_data = self.sort_by(res_data, sort_list)
        return res_data

