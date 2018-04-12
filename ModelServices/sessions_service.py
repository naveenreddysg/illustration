from models.models import SessionsModel
from Db import db

class SessionsService:

    model = SessionsModel

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):

        req_data = db.session.query(self.model).filter(self.model.date >= self.start_date, self.model.date <= self.end_date)
        req_data = req_data.all()
        res_data = [item.__dict__ for item in req_data]
        def del_key(d):
            del d['_sa_instance_state']
            return d
        res_data = map(del_key, res_data)
        return res_data