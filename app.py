from flask import Flask, render_template, request
from ResultsServices.sessions_results import SessionsResults
from ResultsServices.sessions_category_results import SessionsCategoryResults
from ResultsServices.events_results import EventsResults
from ResultsServices.devices_results import DeviceResults
from ResultsServices.cpc_results import CPCResults
from ResultsServices.top_conversions import TopConversionsResults
from utilities import get_dates, date_converter
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
            cpc = CPCResults(dates['pre_start'], dates['pre_end'])
            Top_conversions = TopConversionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
            result = {
                "sessions": sessions.main(),
                "session_category": session_category.main(),
                "session_category_prev": session_category.mainprev(),
                "Events": events.main(),
                "Devices": devices.main(),
                "CPC": cpc.main(),
                "Top_conversions": Top_conversions.main()
              }

            def change(source):
                present, previous = [], []
                for item in result['session_category']:
                    present.append(item[source])
                for item in result['session_category_prev']:
                    previous.append(item[source])
                Change = [round(((float(present[0]) - float(previous[0])) / float(previous[0])) * 100, 2),
                          round(((float(present[1]) - float(previous[1])) / float(previous[0])) * 100, 2),
                          round(((float(present[2]) - float(previous[2])) / float(previous[0])) * 100, 2),
                          round(((float(present[3]) - float(previous[3])) / float(previous[0])) * 100, 2),
                          round(((float(present[4]) - float(previous[4])) / float(previous[0])) * 100, 2),
                          round(((float(present[5]) - float(previous[5])) / float(previous[0])) * 100, 2),
                          round(((float(present[6]) - float(previous[6])) / float(previous[0])) * 100, 2),
                          round(((float(present[7]) - float(previous[7])) / float(previous[0])) * 100, 2),
                          ]
                print(present)
                print(previous)
                print(Change)
                return Change

            OrganicSearchChange = change(source='Organic Search')
            DirectChange = change(source='Direct')
            ReferralChange = change(source='Referral')
            SocialChange = change(source='Social')
            PaidSearchChange = change(source='Paid Search')
            EmailChange = change(source='Email')
            DevicesPrv, DevicesPre = [], []
            for item in result['Devices']:
                DevicesPrv.append(item['Previous'])
                DevicesPre.append(item['Goal Completions'])
            DevicesDict = {'DevicesPrv': DevicesPrv, 'DevicesPre': DevicesPre}
            OrganicSearch, Direct, Referral, Social, PaidSearch, Email = [], [], [], [], [], []
            for item in result['session_category']:
                OrganicSearch.append(item['Organic Search'])
                Direct.append(item['Direct'])
                Referral.append(item['Referral'])
                Social.append(item['Social'])
                PaidSearch.append(item['Paid Search'])
                Email.append(item['Email'])
            SesCatDict = {'OrganicSearch': OrganicSearch, 'Direct': Direct, 'Referral': Referral, 'Social': Social,
                          'PaidSearch': PaidSearch, 'Email': Email}

            return render_template("index.html",result=result,DevicesDict=DevicesDict,SesCatDict=SesCatDict,
                                   OrganicSearchChange=OrganicSearchChange,
                                   DirectChange=DirectChange,
                                   ReferralChange=ReferralChange,
                                   SocialChange=SocialChange,
                                   PaidSearchChange=PaidSearchChange,
                                   EmailChange=EmailChange)

    except Exception as e:
        # print(e)
        dates = get_dates(30)
        print(dates)
        sessions = SessionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
        session_category = SessionsCategoryResults(dates['pre_start'], dates['pre_end'], dates['prv_start'],
                                                   dates['prv_end'])
        events = EventsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
        devices = DeviceResults(dates['pre_start'], dates['pre_end'], dates['prv_start'], dates['prv_end'])
        cpc = CPCResults(dates['pre_start'], dates['pre_end'])
        Top_conversions = TopConversionsResults(dates['pre_start'], dates['pre_end'], dates['prv_start'],
                                                dates['prv_end'])
        result = {
            "sessions": sessions.main(),
            "session_category": session_category.main(),
            "session_category_prev":session_category.mainprev(),
            "Events": events.main(),
            "Devices": devices.main(),
            "CPC": cpc.main(),
            "Top_conversions": Top_conversions.main()
        }
        def change(source):
            present, previous = [], []
            for item in result['session_category']:
                present.append(item[source])
            for item in result['session_category_prev']:
                previous.append(item[source])
            Change = [ round(((float(present[0]) - float(previous[0])) / float(previous[0])) * 100,2),
                       round(((float(present[1]) - float(previous[1])) / float(previous[0])) * 100,2),
                       round(((float(present[2]) - float(previous[2])) / float(previous[0])) * 100,2),
                       round(((float(present[3]) - float(previous[3])) / float(previous[0])) * 100,2),
                       round(((float(present[4]) - float(previous[4])) / float(previous[0])) * 100,2),
                       round(((float(present[5]) - float(previous[5])) / float(previous[0])) * 100,2),
                       round(((float(present[6]) - float(previous[6])) / float(previous[0])) * 100,2),
                       round(((float(present[7]) - float(previous[7])) / float(previous[0])) * 100,2),
                       ]
            print(present)
            print(previous)
            print(Change)
            return Change
        OrganicSearchChange = change(source='Organic Search')
        DirectChange = change(source='Direct')
        ReferralChange= change(source='Referral')
        SocialChange = change(source='Social')
        PaidSearchChange = change(source='Paid Search')
        EmailChange = change(source='Email')
        DevicesPrv,DevicesPre = [],[]
        for item in result['Devices']:
            DevicesPrv.append(item['Previous'])
            DevicesPre.append(item['Goal Completions'])
        DevicesDict = {'DevicesPrv':DevicesPrv,'DevicesPre':DevicesPre}
        OrganicSearch,Direct,Referral,Social,PaidSearch,Email = [],[],[],[],[],[]
        for item in result['session_category']:
            OrganicSearch.append(item['Organic Search'])
            Direct.append(item['Direct'])
            Referral.append(item['Referral'])
            Social.append(item['Social'])
            PaidSearch.append(item['Paid Search'])
            Email.append(item['Email'])
        SesCatDict = {'OrganicSearch':OrganicSearch,'Direct':Direct,'Referral':Referral,'Social':Social,
                                'PaidSearch':PaidSearch,'Email':Email }

        return render_template("index.html", result=result,DevicesDict=DevicesDict,SesCatDict=SesCatDict,
                               OrganicSearchChange=OrganicSearchChange,
                               DirectChange=DirectChange,
                               ReferralChange=ReferralChange,
                               SocialChange=SocialChange,
                               PaidSearchChange=PaidSearchChange,
                               EmailChange=EmailChange)

if __name__ == '__main__':
    from models.models import db
    db.init_app(app)
    app.run(port=8001, debug=True)

