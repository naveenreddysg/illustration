from flask import Flask, render_template, request
from ResultsServices.sessions_results import SessionsResults
from ResultsServices.sessions_category_results import SessionsCategoryResults
from ResultsServices.events_results import EventsResults
from ResultsServices.devices_results import DeviceResults
from ResultsServices.cpc_results import CPCResults
#=======================================================================================================================
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://webanalytics:PyPrince@123@68.178.217.13/webanalytics'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'p9Bv<3Eid9%$i01'


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        dates = request.form.to_dict()
        if dates['pre_start'] != "":
            sessions = SessionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            session_category = SessionsCategoryResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            events = EventsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            devices = DeviceResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            cpc = CPCResults(dates['pre_start'], dates['pre_end'])
            result = {"sessions": sessions.main(),
                      "session_category": session_category.main(),
                      "Events": events.main(),
                      "Devices": devices.main(),
                      "CPC": cpc.main()}

            return render_template("index.html",
                                   result=result
                               )
    except Exception as e:
            # print(e)
            return (render_template('index.html'))

if __name__ == '__main__':
    from models.models import db
    db.init_app(app)
    app.run(debug=True)

