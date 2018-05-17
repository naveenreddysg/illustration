from __future__ import print_function
import sys
from googleapiclient import sample_tools
from googleapiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError
from DbConnections.db_connection import Db


#----------------------------------------------------------------------------------------------------

def get_profile_id(service):

  accounts = service.management().accounts().list().execute()

  if accounts.get('items'):
    firstAccountId = accounts.get('items')[0].get('id')
    # print(firstAccountId)
    webproperties = service.management().webproperties().list(
        accountId=firstAccountId).execute()

    if webproperties.get('items'):
      profileIds = []
      try:
          for i in range(0, webproperties['totalResults']):
              # print(i)
              firstWebpropertyId = webproperties.get('items')[i].get('id')
              profiles = service.management().profiles().list(
                  accountId=firstAccountId,
                  webPropertyId=firstWebpropertyId).execute()
              profileIds.append(profiles)
              # print(profiles)
          profiles_id = []
          for profiles in profileIds:
            if profiles.get('items'):
                profiles_id.append((profiles.get('items')[0].get('id')))
          # print(profiles_id)
          return profiles_id
      except Exception as e:
          print(e)
          pass

  return None

#-----------------------------------------------------------------------------------------------------------------------

def get_top_keywords(service, profile_id, startDate1, endDate1):

    # print(profile_id, filters)
    results = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate1,
      end_date=endDate1,
      metrics='ga:sessions',
      dimensions='ga:deviceCategory',
      segment='gaid::-11'
    ).execute()

    resultsb = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate1,
      end_date=endDate1,
      metrics='ga:bouncerate',
      dimensions='ga:deviceCategory',
      segment='gaid::-11'
    ).execute()

    resultsc = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate1,
      end_date=endDate1,
      metrics='ga:goalconversionrateall',
      dimensions='ga:deviceCategory',
      segment='gaid::-3'
    ).execute()

    resultsd = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate1,
      end_date=endDate1,
      metrics='ga:goalconversionrateall',
      dimensions='ga:deviceCategory',
      segment='gaid::-2'
    ).execute()

    resultse = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate1,
      end_date=endDate1,
      metrics='ga:avgsessionduration',
      dimensions='ga:deviceCategory',
      segment=None
    ).execute()

    return (results,resultsb,resultsc,resultsd,resultse)

def print_top_keywords(results, startDate1):

    # query = "INSERT INTO top_conversions (mobile_tablet, bounce_rate, returning_conversions, unique_conversions, session_duration, date)\
    #       VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format \
    #     (sum(results[0]), sum(results[1])/4, sum(results[2])/4, sum(results[3])/4, sum(results[4])/4, startDate1)
    # db = Db()
    # db.execute(query)
    # db.commit()
    # topConversions = TopConversionsModel(sum(results[0]), sum(results[1])/4, sum(results[2])/4, sum(results[3])/4, sum(results[4])/4, startDate1)
    # topConversions.save_to_db()
    print('TopConversions')

#-----------------------------------------------------------------------------------------------------------------------

def get_agents(service, profile_id,pre_startDate,pre_endDate):
  pres_month = service.data().ga().get(
    ids='ga:' + profile_id,
    start_date=str(pre_startDate),
    end_date=str(pre_endDate),
    metrics='ga:uniqueEvents',
    dimensions='ga:eventCategory,ga:eventAction',
    filters='ga:eventCategory!=ArtistPortfolio;ga:eventCategory!=Newsletter;ga:eventCategory!=SideButtons;ga:eventCategory!=Social;ga:eventCategory!=YouMightAlsoLike;ga:eventCategory!=Artist Quote;ga:eventAction!=Impressions'
  ).execute()
  return pres_month


def print_agents(results, date):

    def dict_conversion(a):
        if len(a) > 2:
            a.pop(0)
        return a
    present_result = dict(map(dict_conversion, results.get('rows', [["", ""]])))
    print('print_agents')

    # query = "INSERT INTO agents (click, email_click, call_click, date)\
    #   VALUES ('{}', '{}', '{}', '{}');".format \
    #     (present_result.get('Click', '0'), present_result.get('EmailClick', '0'), present_result.get('EmailClick','0'), date)
    # db = Db()
    # db.execute(query)
    # db.commit()

    # agents = AgentsModel(present_result.get('Click', '0'), present_result.get('EmailClick','0'), present_result.get('EmailClick','0'), date)
    # agents.save_to_db()
    return present_result

def get_sidebtn(service, profile_id,pre_startDate,pre_endDate):
  pres_month = service.data().ga().get(
    ids='ga:' + profile_id,
    start_date=str(pre_startDate),
    end_date=str(pre_endDate),
    metrics='ga:uniqueEvents',
    dimensions='ga:eventLabel',
    filters='ga:eventCategory==SideButtons'
  ).execute()

  return pres_month

def print_sidebtn(results, date):
    present_result = (dict(results.get('rows', [["", ""]])))

    # query = "INSERT INTO side_btn (recently_viewed_portfolios, Help, date)\
    #       VALUES ('{}', '{}', '{}');".format \
    #     (present_result.get('RecentlyViewedPortfolios', '0'), present_result.get('Help', '0'), date)
    # db = Db()
    # db.execute(query)
    # db.commit()
    # print('side_btn')
    # agents = SideBtnModel(present_result.get('RecentlyViewedPortfolios', '0'), present_result.get('Help', '0'), date)
    # agents.save_to_db()
    return present_result

def get_portpolio(service, profile_id,pre_startDate,pre_endDate):
  pres_month = service.data().ga().get(
    ids='ga:' + profile_id,
    start_date=str(pre_startDate),
    end_date=str(pre_endDate),
    metrics='ga:uniqueEvents',
    dimensions='ga:eventAction',
    filters='ga:eventCategory==ArtistPortfolio'
  ).execute()

  return pres_month

def print_portpolio(results, date):
    print('portfolio')
    present_result = (dict(results.get('rows', [["", ""]])))
    # query = "INSERT INTO portfolio (PDF_downloads, email_clicks, call_clicks, video_Image_Clicks, date)\
    #           VALUES ('{}', '{}', '{}', '{}', '{}');".format \
    #     (present_result.get('PDFClick', '0'), present_result.get('EmailClick', '0'), present_result.get('CallClick', '0'), present_result.get('VideoImgClick', '0'), date)
    # db = Db()
    # db.execute(query)
    # db.commit()

    # agents = PortflioModel(present_result.get('PDFClick', '0'), present_result.get('EmailClick', '0'), present_result.get('CallClick', '0'), present_result.get('VideoImgClick', '0'), date)
    # agents.save_to_db()
    return present_result

#----------------------------------------------------------------------------------------------------------------

def get_sessions(service, profile_id, filters, startDate1, endDate1):

  try:
      if filters == 'SEA':
          filters = 'ga:subContinent==Southeast Asia'
          metrics = 'ga:sessions'
          dimensions = 'ga:channelGrouping'
      elif filters == 'ROW':
          filters = 'ga:country!=United Kingdom;ga:country!=India;ga:subContinent!=Southeast Asia;ga:continent!=Oceania'
          metrics = 'ga:sessions'
          dimensions = 'ga:channelGrouping'
      elif filters == 'ANZ':
          filters = 'ga:continent==Oceania'
          metrics = 'ga:sessions'
          dimensions = 'ga:channelGrouping'
      elif filters == 'ROWUSA':
          filters = 'ga:country!=United States;ga:country!=Canada'
          metrics = 'ga:sessions'
          dimensions = 'ga:channelGrouping'
      elif filters == 'France' or filters == 'China':
          filters = None
          metrics = 'ga:sessions'
          dimensions = 'ga:channelGrouping'
      else:
          metrics = 'ga:sessions'
          dimensions = 'ga:channelGrouping'
          filters = 'ga:country=={}'.format(filters)
  except Exception as e:
      print(e)
      pass

  pres_month = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=str(startDate1),
      end_date=str(endDate1),
      metrics=metrics,
      dimensions=dimensions,
      filters=filters
    ).execute()

  return pres_month

def print_sessions(results, country, date):

  try:
    result1 = (dict(results.get('rows')))
  except:
      result1 = {}

  email = result1.get('(Other)', 0)
  result1['Email'] = email
  try:
    del result1['(Other)']
  except:
      pass

  result1['Country'] = country.split(',')[0]
  if result1['Country'] == 'United States':
      result1['Country'] = 'US'
  elif result1['Country'] == 'United Kingdom':
      result1['Country'] = 'UK'
  else:
      pass

  d_sessions = {}
  d_sessions['Country'] = country.split(',')[0]
  if d_sessions['Country'] == 'United States':
      d_sessions['Country'] = 'US'
  elif d_sessions['Country'] == 'United Kingdom':
      d_sessions['Country'] = 'UK'
  else:
      pass
  d_sessions['TotalSessions'] = float(results.get('totalsForAllResults')['ga:sessions'])

  print("SESSIONS:\n")
  print(result1, "\n")
  print(d_sessions, "\n")

  # query = "INSERT INTO sessions_category (country, organic_search, direct, referral, social, paid_search, email, date)\
  # VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format\
  #     (result1['Country'], result1.get('Organic Search', '0'), result1.get('Direct', '0'), result1.get('Social', '0'), result1.get('Referral', '0'), result1.get('Paid Search', '0'), result1.get('Email', '0'), date)
  # db = Db()
  # db.execute(query)
  # db.commit()
  #
  # query = "INSERT INTO sessions (country, total, date)VALUES ('{}', '{}', '{}');".format(d_sessions['Country'], d_sessions.get('TotalSessions', '0'), date)
  # db = Db()
  # db.execute(query)
  # db.commit()
  # db.close()

  # sessions_category = SessionsCategoryModel(result1['Country'], result1.get('Organic Search', '0'), result1.get('Direct', '0'), result1.get('Social', '0'), result1.get('Referral', '0'), result1.get('Paid Search', '0'), result1.get('Email', '0'), date)
  # sessions_category.save_to_db()

  # sessions = SessionsModel(d_sessions['Country'], d_sessions.get('TotalSessions', '0'), date)
  # sessions.save_to_db()
  return result1, d_sessions

#-----------------------------------------------------------------------------

def get_events(service, profile_id, startDate1, endDate1):

    metrics = 'ga:uniqueEvents'
    dimensions = 'ga:eventLabel'
    filters = 'ga:eventLabel==HelloBar'
    pres_month = service.data().ga().get(
        ids='ga:' + profile_id,
        start_date=str(startDate1),
        end_date=str(endDate1),
        metrics=metrics,
        dimensions=dimensions,
        filters=filters
    ).execute()

    return pres_month

def print_events(results, country, date):
    try:
        result1 = (dict(results.get('rows')))
    except:
        result1 = {}

    result = {'Country': country.split('Events')[0], 'HelloBar Events': result1.get('HelloBar', '0')}
    #
    # query = "INSERT INTO events (country, hello_bar_events, date)VALUES ('{}', '{}', '{}');".format(country.split('Events')[0], result1.get('HelloBar', '0'), date)
    # db = Db()
    # db.execute(query)
    # db.commit()
    # db.close()

    # events = EventsModel(country.split('Events')[0], result1.get('HelloBar', '0'), date)
    # events.save_to_db()

    print("EVENTS:\n")
    print(result)
    return result

#-----------------------------------------------------------------------------

def get_devices(service, profile_id, startDate1, endDate1):
    metrics = 'ga:uniqueEvents'
    dimensions = 'ga:deviceCategory'
    filters = 'ga:eventLabel=~Job Quote'
    pres_month = service.data().ga().get(
        ids='ga:' + profile_id,
        start_date=str(startDate1),
        end_date=str(endDate1),
        metrics=metrics,
        dimensions=dimensions,
        filters=filters
    ).execute()

    return pres_month

def print_devices(results, date):

    try:
        result1 = (dict(results.get('rows')))
    except:
        result1 = {}

    # query = "INSERT INTO devices (mobile, tablet, desktop, date) VALUES ('{}', '{}', '{}', '{}');".format(result1.get('mobile', 0), result1.get('tablet', '0'), result1.get('desktop', '0'), date)
    # db = Db()
    # db.execute(query)
    # db.commit()
    # db.close()

    # devices = DevicesModel(result1.get('Mobile', 0), result1.get('Tablet', '0'), result1.get('desktop', '0'), date)
    # devices.save_to_db()

    print("DEVICES:\n")
    print(result1, "\n")
    return result1

#-----------------------------------------------------------------------------------------------------------------------

def get_devices_sessions(service, profile_id, startDate1, endDate1):

    metrics = 'ga:sessions'
    dimensions = 'ga:deviceCategory'
    pres_month = service.data().ga().get(
        ids='ga:' + profile_id,
        start_date=str(startDate1),
        end_date=str(endDate1),
        metrics=metrics,
        dimensions=dimensions,
    ).execute()
    return pres_month

def print_devices_sessions(results, country, date):
    try:
        result1 = (dict(results.get('rows')))
    except:
        result1 = {}

    # query = "INSERT INTO devices_sessions (country, mobile, tablet, desktop, total, date) " \
    #         "VALUES ('{}', '{}', '{}', '{}', '{}', '{}');".format(country, result1.get('mobile', 0),
    #         result1.get('tablet', '0'), result1.get('desktop', '0'),
    #         results.get('totalsForAllResults').get('ga:sessions', 0), date)
    # db = Db()
    # db.execute(query)
    # db.commit()
    # db.close()

    # devices = DevicesSessionsModel(country, result1.get('mobile', 0),
    #             result1.get('tablet', '0'), result1.get('desktop', '0'),
    #             results.get('totalsForAllResults').get('ga:sessions', 0), date)
    # devices.save_to_db()

    print("DEVICES SESSIONS:\n", country)
    print(result1, "\n")
    return result1



#-----------------------------------------------------------------------------------------------------------------------

def get_CPC(service, profile_id, startDate1, endDate1):

    metrics = 'ga:goalCompletionsAll'
    dimensions = 'ga:source'
    filters = 'ga:medium==cpc'
    pres_month = service.data().ga().get(
        ids='ga:' + profile_id,
        start_date=str(startDate1),
        end_date=str(endDate1),
        metrics=metrics,
        dimensions=dimensions,
        filters=filters
    ).execute()

    return pres_month

def print_CPC(results, date):

    try:
        result1 = (dict(results.get('rows')))
    except:
        result1 = {}

    # query = "INSERT INTO cpc (google, Bingads, facebookads, Instagram, date)VALUES ('{}', '{}', '{}', '{}', '{}');".format(result1.get('google', '0'), result1.get('Bingads', '0'), result1.get('facebookads', '0'), result1.get('Instagram', '0'), date)
    # db = Db()
    # db.execute(query)
    # db.commit()
    # db.close()

    # cpc = CPCModel(result1.get('google', '0'), result1.get('Bingads', '0'), result1.get('facebookads', '0'), result1.get('Instagram', '0'), date)
    # cpc.save_to_db()

    print("CPC:\n")
    print(result1, '\n')
    return result1

#-----------------------------------------------------------------------------

def main(argv):
  # Authenticate and construct service
  service, flags = sample_tools.init(
      argv, 'analytics', 'v3', __doc__, __file__,
      scope='https://www.googleapis.com/auth/analytics.readonly')

  # Try to make a request to the API. Print the results or handle errors.
  try:
    profile_ids = get_profile_id(service)
    if not profile_ids:
      print('Could not find a valid profile for this user.')
    else:
      # countries = ['United Kingdom', 'United States,ga:country==Canada', 'France', 'China']
      # out = zip(profile_ids, countries)

      ReportName = ['UK', 'USA', 'France', 'China']
      out = zip(profile_ids, ReportName)

      session = [
          ('5110029', 'United Kingdom'),
          ('84906789', 'United States,ga:country==Canada'),
          ('85625764', 'France'),
          ('88496086', 'China'),
          ('5110029', 'India'),
          ('5110029', 'SEA'),
          ('5110029', 'ROW'),
          ('5110029', 'ANZ'),
          ('84906789', 'ROWUSA')
      ]

      events = [('5110029', 'UKEvents'), ('84906789', 'USAEvents'), ('85625764', 'FranceEvents'),
                ('88496086', 'ChinaEvents')]

      devices = [('5110029', 'UKDevice'), ('84906789', 'USADevice')]

      devices_sessions = [('5110029', 'UK'), ('84906789', 'USA'), ('85625764', 'France'),
                          ('88496086', 'China')]

      cpc = [('5110029', 'UKCPC'), ('84906789', 'USACPC')]

      agents = [
          ('5110029', 'UKPortfolio'),
          ('84906789', 'USAPortfolio'),
          ('85625764', 'FrancePortfolio'),
          ('88496086', 'ChinaPortfolio'),
      ]

      sidebtn = [
          ('5110029', 'UKSideBtn'),
          ('84906789', 'USASideBtn'),
          ('85625764', 'FranceSideBtn'),
          ('88496086', 'ChinaSideBtn'),
      ]

      portpolio = [
          ('5110029', 'UKPortfolio'),
          ('84906789', 'USAPortfolio'),
          ('85625764', 'FrancePortfolio'),
          ('88496086', 'ChinaPortfolio'),
      ]

      from datetime import timedelta, date

      def daterange(start_date, end_date):
          for n in range(int((end_date - start_date).days)):
              yield start_date + timedelta(n)

      start_date = date(2018, 5, 15)
      end_date = date(2018, 5, 16)

      print("******--Sit back and relax this will take sometime--******".upper())

      for single_date in daterange(start_date, end_date):
          startDate1 = endDate1 = single_date.strftime("%Y-%m-%d")
          print(single_date.strftime("%Y-%m-%d"))

          lst = [[], [], [], [], []]
          for profile_id in out:
              results = get_top_keywords(service, profile_id[0], startDate1, endDate1)
              lst[0].append(int(results[0].get('totalsForAllResults')['ga:sessions']))
              lst[1].append(float(results[1].get('totalsForAllResults')['ga:bouncerate']))
              lst[2].append(float(results[2].get('totalsForAllResults')['ga:goalconversionrateall']))
              lst[3].append(float(results[3].get('totalsForAllResults')['ga:goalconversionrateall']))
              lst[4].append(float(results[4].get('totalsForAllResults')['ga:avgsessionduration']))

          print_top_keywords(lst, startDate1)


          for profile_id in agents:
              results = get_agents(service, profile_id[0], startDate1, endDate1)
              # print(results)
              print_agents(results, startDate1)

          for profile_id in sidebtn:
              results = get_sidebtn(service, profile_id[0], startDate1, endDate1)
              # print(results)
              print_sidebtn(results, startDate1)

          for profile_id in portpolio:
              results = get_portpolio(service, profile_id[0], startDate1, endDate1)
              # print(results)
              print_portpolio(results, startDate1)

          for profile_id in events:

              results = get_events(service, profile_id[0], startDate1, endDate1)

              print_events(results, profile_id[1], startDate1)

          for profile_id in devices:

              results = get_devices(service, profile_id[0], startDate1, endDate1)
              print_devices(results, startDate1)

          for profile_id in devices_sessions:
              results = get_devices_sessions(service, profile_id[0], startDate1, endDate1)
              print_devices_sessions(results, profile_id[1], startDate1)

          for profile_id in cpc:

              results = get_CPC(service, profile_id[0], startDate1, endDate1)
              print_CPC(results, startDate1)

          for profile_id in session:

            results = get_sessions(service, profile_id[0], profile_id[1], startDate1, endDate1)
            print_sessions(results, profile_id[1], startDate1)

      print("Done...!")

  except TypeError as error:
    # Handle errors in constructing a query.
    print(('There was an error in constructing your query : %s' % error))

  except HttpError as error:
    # Handle API errors.
    print(('Arg, there was an API error : %s : %s' %
           (error.resp.status, error._get_reason())))

  except AccessTokenRefreshError:
    # Handle Auth errors.
    print ('The credentials have been revoked or expired, please re-run '
           'the application to re-authorize')

#-------------------------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)