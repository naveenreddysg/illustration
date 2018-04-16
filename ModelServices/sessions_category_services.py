from DbConnections.Db import db
from models.models import SessionsCategoryModel
from utilities import group

class SessionsCategoryService:

    model = SessionsCategoryModel

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):

        req_data = db.session.query(self.model).filter(self.model.date >= self.start_date, self.model.date <= self.end_date)
        req_data = req_data.all()
        res_data = group(req_data, 'country')
        new_dict = {}
        for data in res_data:
            new_dict['paidSearch'] = 0
            new_dict['direct'] = 0
            new_dict['social'] = 0
            new_dict['organicSearch'] = 0
            new_dict['referral'] = 0
            new_dict['email'] = 0
            new_dict['country'] = 'ROW'
            if data['country'] == 'ROW':
                new_dict['paidSearch'] += data['paidSearch']
                new_dict['direct'] += data['direct']
                new_dict['social'] += data['social']
                new_dict['organicSearch'] += data['organicSearch']
                new_dict['referral'] += data['referral']
                new_dict['email'] += data['email']
                res_data.remove(data)
            elif data['country'] == 'ROWUSA':
                new_dict['paidSearch'] += (data['paidSearch'])
                new_dict['direct'] += data['direct']
                new_dict['social'] += data['social']
                new_dict['organicSearch'] += data['organicSearch']
                new_dict['referral'] += data['referral']
                new_dict['email'] += data['email']
                res_data.remove(data)
        res_data.append(new_dict)
        return res_data

