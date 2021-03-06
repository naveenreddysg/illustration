from flask import Flask, render_template, request
from ResultsServices.sessions_results import SessionsResults
from ResultsServices.sessions_category_results import SessionsCategoryResults
from ResultsServices.events_results import EventsResults
from ResultsServices.devices_results import DeviceResults
from ResultsServices.cpc_results import CPCResults
from ResultsServices.top_conversions_results import TopConversionsResults
from ResultsServices.device_sessions_results import DeviceSessionsResults
from utilities import get_dates, date_converter, change, line_results, line_results_region, getweekdates, get_two_month_dates, get_month_names
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
        dates = date_converter(dates)
        print(dates)
        if dates['pre_start'] != "":
            sessions = SessionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            session_category = SessionsCategoryResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            events = EventsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            devices = DeviceResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            devices_sessions = DeviceSessionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'],dates['prv_end'])
            cpc = CPCResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            Top_conversions = TopConversionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])

            result = {
                "sessions": sessions.main(),
                "session_category": session_category.main(),
                "Events": events.main(),
                "Devices": devices.main(),
                'Device_sessions': devices_sessions.main(),
                "CPC": cpc.main(),
                "Top_conversions": Top_conversions.main()
            }

            MonthNames = get_month_names(dates['pre_start'], dates['prv_start'])
            MonthNames2 = [getweekdates(7)['pre_MonthName'], getweekdates(7)['prv_MonthName']]

            keys = (result['session_category']['present'][0].keys())
            keys = [x for x in keys if x != 'Country']
            Change = {
                i: change(source=i, result=result['session_category']) for i in keys
            }

            return render_template("index.html",
                                   result=result, Change=Change, lineresults=line_results(),
                                   lineregionresults=line_results_region(), MonthNames=MonthNames, MonthNames2=MonthNames2, dates=dates)
    except Exception as e:
        print(e)
        dates = get_two_month_dates()
        print(dates)
        sessions = SessionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
        session_category = SessionsCategoryResults(dates['pre_start'], dates['pre_end'], dates['prv_start'],
                                                   dates['prv_end'])
        events = EventsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
        devices = DeviceResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
        devices_sessions = DeviceSessionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
        cpc = CPCResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
        Top_conversions = TopConversionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'],
                                                dates['prv_end'])
        result = {
            "sessions": sessions.main(),
            "session_category": session_category.main(),
            "Events": events.main(),
            "Devices": devices.main(),
            "Device_sessions": devices_sessions.main(),
            "CPC": cpc.main(),
            "Top_conversions": Top_conversions.main()
            }

        MonthNames = get_month_names(dates['pre_start'], dates['prv_start'])
        MonthNames2 = [getweekdates(7)['pre_MonthName'], getweekdates(7)['prv_MonthName']]

        print result['session_category']
        keys = (result['session_category']['present'][0].keys())
        keys = [x for x in keys if x != 'Country']
        Change = {
            i: change(source=i, result=result['session_category']) for i in keys
        }

        return render_template("index.html",
                               result=result, Change=Change, lineresults=line_results(),
                               lineregionresults=line_results_region(), MonthNames=MonthNames, MonthNames2=MonthNames2,
                               dates=dates)
if __name__ == '__main__':

    from models.models import db
    db.init_app(app)
    app.run(port=8001, debug=True)