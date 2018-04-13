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
        return res_data

