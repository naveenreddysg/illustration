from DbConnections.Db import db
from models.models import PortflioModel
from utilities import group

class PortflioService:

    model = PortflioModel

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):

        req_data = db.session.query(self.model).filter(self.model.date >= self.start_date, self.model.date <= self.end_date)
        req_data = req_data.all()
        res_data = group(req_data)
        return res_data