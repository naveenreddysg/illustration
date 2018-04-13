from DbConnections.Db import db
class SessionsCategoryModel(db.Model):

    __tablename__ = 'sessions_category'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column('country', db.String(30))
    organicSearch = db.Column('organic_search', db.Integer)
    direct = db.Column('direct', db.Integer)
    referral = db.Column('referral', db.Integer)
    social = db.Column('social', db.Integer)
    paidSearch = db.Column('paid_search', db.Integer)
    email = db.Column('email', db.Integer)
    date = db.Column('date', db.Date)

    def __init__(self, country, organicSearch, direct, referral, social, paidSearch, email, date):
        self.country = country
        self.organicSearch = organicSearch
        self.direct = direct
        self.referral = referral
        self.social = social
        self.paidSearch = paidSearch
        self.email = email
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class SessionsModel(db.Model):

    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column('country', db.String(30))
    totalSessions = db.Column('total', db.String(30))
    date = db.Column('date', db.Date)

    def __init__(self, country, totalSessions, date):
        self.country = country
        self.totalSessions = totalSessions
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class EventsModel(db.Model):

    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column('country', db.String(30))
    HelloBarEvents = db.Column('hello_bar_events', db.String(30))
    date = db.Column('date', db.Date)

    def __init__(self, country, HelloBarEvents, date):
        self.country = country
        self.HelloBarEvents = HelloBarEvents
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class DevicesModel(db.Model):

    __tablename__ = 'devices'

    id = db.Column(db.Integer, primary_key=True)
    mobileTablet = db.Column('mobile_tablet', db.String(30))
    desktop = db.Column('desktop', db.String(30))
    date = db.Column('date', db.Date)

    def __init__(self,mobileTablet, desktop, date):
        self.mobileTablet = mobileTablet
        self.desktop = desktop
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class CPCModel(db.Model):

    __tablename__ = 'cpc'

    id = db.Column(db.Integer, primary_key=True)
    google = db.Column('google', db.String(30))
    Bingads = db.Column('Bingads', db.String(30))
    facebookads = db.Column('facebookads', db.String(30))
    Instagram = db.Column('Instagram', db.String(30))
    date = db.Column('date', db.Date)

    def __init__(self, google, Bingads, facebookads, Instagram, date):
        self.google = google
        self.Bingads = Bingads
        self.facebookads = facebookads
        self.Instagram = Instagram
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class SideBtnModel(db.Model):

    __tablename__ = 'side_btn'

    id = db.Column(db.Integer, primary_key=True)
    recentlyViewedPortfolios = db.Column('recently_viewed_portfolios', db.String(30))
    Help = db.Column('Help', db.String(30))
    date = db.Column('date', db.Date)

    def __init__(self, recentlyViewedPortfolios, Help, date):
        self.recentlyViewedPortfolios = recentlyViewedPortfolios
        self.Help = Help
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class AgentsModel(db.Model):

    __tablename__ = 'agents'

    id = db.Column(db.Integer, primary_key=True)
    click = db.Column('click', db.String(30))
    emailClick = db.Column('email_click', db.String(30))
    callClick = db.Column('call_click', db.String(30))
    date = db.Column('date', db.Date)

    def __init__(self, click, emailClick, callClick, date):
        self.click = click
        self.emailClick = emailClick
        self.callClick = callClick
        self.callClick = callClick
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class PortflioModel(db.Model):

    __tablename__ = 'portfolio'

    id = db.Column(db.Integer, primary_key=True)
    PDFDownloads = db.Column('PDF_downloads', db.String(30))
    EmailClicks = db.Column('email_clicks', db.String(30))
    CallClicks = db.Column('call_clicks', db.String(30))
    VideoImageClicks = db.Column('video_Image_Clicks', db.String(30))
    date = db.Column('date', db.Date)

    def __init__(self, PDFDownloads, EmailClicks, CallClicks, VideoImageClicks, date):
        self.PDFDownloads = PDFDownloads
        self.EmailClicks = EmailClicks
        self.CallClicks = CallClicks
        self.VideoImageClicks = VideoImageClicks
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class TopConversionsModel(db.Model):

    __tablename__ = 'top_conversions'

    id = db.Column(db.Integer, primary_key=True)
    MobileTablet = db.Column('mobile_tablet', db.String(30))
    BounceRate = db.Column('bounce_rate', db.String(30))
    ReturningConversions = db.Column('returning_conversions', db.String(30))
    UniqueConversions = db.Column('unique_conversions', db.String(30))
    SessionDuration = db.Column('session_duration', db.String(30))
    date = db.Column('date', db.Date)

    def __init__(self, MobileTablet, BounceRate, ReturningConversions, UniqueConversions, SessionDuration, date):
        self.MobileTablet = MobileTablet
        self.BounceRate = BounceRate
        self.ReturningConversions = ReturningConversions
        self.UniqueConversions = UniqueConversions
        self.SessionDuration = SessionDuration
        self.date = date

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


