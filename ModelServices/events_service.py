from DbConnections.Db import db
from models.models import EventsModel
from utilities import group

class EventsService:

    model = EventsModel

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
        sort_list = ['UK', 'USA', 'France', 'China']
        res_data = self.sort_by(res_data, sort_list)
        return res_data