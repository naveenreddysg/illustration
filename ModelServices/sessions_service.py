from DbConnections.Db import db
from models.models import SessionsModel
from utilities import group

class SessionsService:

    model = SessionsModel

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):

        req_data = db.session.query(self.model).filter(self.model.date >= self.start_date, self.model.date <= self.end_date)
        req_data = req_data.all()
        res_data = group(req_data, 'country')
        new_dict = {}
        for data in res_data:
            new_dict['totalSessions'] = 0
            new_dict['country'] = 'ROW'
            if data['country'] == 'ROW':
                new_dict['totalSessions'] += data['totalSessions']
                res_data.remove(data)
            elif data['country'] == 'ROWUSA':
                new_dict['totalSessions'] += data['totalSessions']
                res_data.remove(data)
        res_data.append(new_dict)
        total = 0
        for data in res_data:
            total += data['totalSessions']
        res_data.append({'country': 'Total', 'totalSessions': total})

        return res_data