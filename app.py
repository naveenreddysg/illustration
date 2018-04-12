from flask import Flask, render_template
from data_to_models import *
from ModelServices.sessions_category_services import SessionsCategoryService
from ModelServices.agents_service import AgentsService
from ModelServices.cpc_service import CPCService
from ModelServices.devices_service import DevicesService
from ModelServices.events_service import EventsService
from ModelServices.portfolio_service import PortflioService
from ModelServices.sessions_service import SessionsService
from ModelServices.side_btn_service import SideBtnService
from ModelServices.top_conversion_service import TopConversionsService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://webanalytics:PyPrince@123@68.178.217.13/webanalytics'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'p9Bv<3Eid9%$i01'


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():

    sessions_category = SessionsCategoryService('2017-10-14', '2017-10-14')
    # sessions = SessionsService('2017-10-14', '2017-10-14')
    # agents = AgentsService('2017-10-14', '2017-10-14')
    # devices = DevicesService('2017-10-14', '2017-10-14')
    # events = EventsService('2017-10-14', '2017-10-14')
    # portfolio = PortflioService('2017-10-14', '2017-10-14')
    # cpc = CPCService('2017-10-14', '2017-10-14')
    # side_btn = SideBtnService('2017-10-14', '2017-10-14')
    # top_conversions = TopConversionsService('2017-10-14', '2017-10-14')
    #
    # print sessions_category.get_data()
    # print sessions.get_data()
    # print agents.get_data()
    # print devices.get_data()
    # print events.get_data()
    # print portfolio.get_data()
    # print cpc.get_data()
    # print side_btn.get_data()
    # print top_conversions.get_data()
    # return render_template("index.html")

if __name__ == '__main__':
    from models.models import db
    db.init_app(app)
    app.run(port=5000, debug=True)

