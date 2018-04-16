from flask import Flask, render_template
from ResultsServices.sessions_results import SessionsResults
from ResultsServices.sessions_category_result import SessionsCategoryResults
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://webanalytics:PyPrince@123@68.178.217.13/webanalytics'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'p9Bv<3Eid9%$i01'


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    sessions = SessionsResults('2017-10-01', '2017-10-31', '2017-12-1', '2017-12-30')
    session_category = SessionsCategoryResults('2017-10-01', '2017-10-31', '2017-12-1', '2017-12-30')
    return render_template("results.html",
                           sessions=sessions.main(),
                           session_category=session_category.main()
                           )

if __name__ == '__main__':
    from models.models import db
    db.init_app(app)
    app.run(port=8000, debug=True)

