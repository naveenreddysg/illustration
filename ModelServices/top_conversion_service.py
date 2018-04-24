from DbConnections.Db import db
from models.models import TopConversionsModel
from utilities import group


class TopConversionsService:

    model = TopConversionsModel

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):

        req_data = db.session.query(self.model).filter(self.model.date >= self.start_date, self.model.date <= self.end_date)
        req_data = req_data.all()
        res_data1 = group(req_data)
        res_data = []
        keys = res_data1[0].keys()
        new = {}
        length = len(res_data1)
        for key in keys:
            if key != 'country' and key != 'date':
                x = 0
                for data in res_data1:
                    x += float(data[key])
                if key != 'MobileTablet':
                    new[key] = round(float(x/length), 2)
                else:
                    new[key] = int(x)
        res_data.append(new)
        return res_data