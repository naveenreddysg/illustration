from __future__ import print_function
import sys
from googleapiclient.errors import HttpError
from googleapiclient import sample_tools
from oauth2client.client import AccessTokenRefreshError
import os
import glob
import csv
import xlwt
#-------------------------------------------------------


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

#========================================================================================================================

MobileTablet = []
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

def get_top_keywords_2(service, profile_id, startDate2, endDate2):

    # print(profile_id, filters)
    results2 = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate2,
      end_date=endDate2,
      metrics='ga:sessions',
      dimensions='ga:deviceCategory',
      segment='gaid::-11'

    ).execute()
    resultsb2 = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate2,
      end_date=endDate2,
      metrics='ga:bouncerate',
      dimensions='ga:deviceCategory',
      segment='gaid::-11'

    ).execute()
    resultsc2 = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate2,
      end_date=endDate2,
      metrics='ga:goalconversionrateall',
      dimensions='ga:deviceCategory',
      segment='gaid::-3'

    ).execute()
    resultsd2 = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate2,
      end_date=endDate2,
      metrics='ga:goalconversionrateall',
      dimensions='ga:deviceCategory',
      segment='gaid::-2'

    ).execute()
    resultse2 = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=startDate2,
      end_date=endDate2,
      metrics='ga:avgsessionduration',
      dimensions='ga:deviceCategory',
      segment=None

    ).execute()

    return (results2,resultsb2,resultsc2,resultsd2,resultse2)

def get_agents(service, profile_id,pre_startDate,pre_endDate,prv_startDate,prv_endDate):
  pres_month = service.data().ga().get(
    ids='ga:' + profile_id,
    start_date=str(pre_startDate),
    end_date=str(pre_endDate),
    metrics='ga:uniqueEvents',
    dimensions='ga:eventCategory,ga:eventAction',
    filters='ga:eventCategory!=ArtistPortfolio;ga:eventCategory!=Newsletter;ga:eventCategory!=SideButtons;ga:eventCategory!=Social;ga:eventCategory!=YouMightAlsoLike;ga:eventCategory!=Artist Quote;ga:eventAction!=Impressions'
  ).execute()

  prev_month = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=str(prv_startDate),
      end_date=str(prv_endDate),
      metrics='ga:uniqueEvents',
      dimensions='ga:eventCategory,ga:eventAction',
      filters='ga:eventCategory!=ArtistPortfolio;ga:eventCategory!=Newsletter;ga:eventCategory!=SideButtons;ga:eventCategory!=Social;ga:eventCategory!=YouMightAlsoLike;ga:eventCategory!=Artist Quote;ga:eventAction!=Impressions'
  ).execute()
  return pres_month, prev_month


def print_agents(results):

    def dict_conversion(a):
        if len(a) > 2:
            a.pop(0)
        return a
    present_result = dict(map(dict_conversion, results[0].get('rows', [["", ""]])))
    prev_result = dict(map(dict_conversion, results[1].get('rows', [["", ""]])))
    return present_result, prev_result

def get_sidebtn(service, profile_id,pre_startDate,pre_endDate,prv_startDate,prv_endDate):
  pres_month = service.data().ga().get(
    ids='ga:' + profile_id,
    start_date=str(pre_startDate),
    end_date=str(pre_endDate),
    metrics='ga:uniqueEvents',
    dimensions='ga:eventLabel',
    filters='ga:eventCategory==SideButtons'
  ).execute()

  prev_month = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=str(prv_startDate),
      end_date=str(prv_endDate),
      metrics='ga:uniqueEvents',
      dimensions='ga:eventLabel',
      filters='ga:eventCategory==SideButtons'
  ).execute()

  return pres_month, prev_month

def print_sidebtn(results):
    present_result = (dict(results[0].get('rows', [["", ""]])))
    prev_result = (dict(results[1].get('rows', [["", ""]])))
    return present_result, prev_result


def get_portpolio(service, profile_id,pre_startDate,pre_endDate,prv_startDate,prv_endDate):
  pres_month = service.data().ga().get(
    ids='ga:' + profile_id,
    start_date=str(pre_startDate),
    end_date=str(pre_endDate),
    metrics='ga:uniqueEvents',
    dimensions='ga:eventAction',
    filters='ga:eventCategory==ArtistPortfolio'
  ).execute()

  prev_month = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=str(prv_startDate),
      end_date=str(prv_endDate),
      metrics='ga:uniqueEvents',
      dimensions='ga:eventAction',
      filters='ga:eventCategory==ArtistPortfolio'
  ).execute()

  return pres_month, prev_month

def print_portpolio(results):
    present_result = (dict(results[0].get('rows')))
    prev_result = (dict(results[1].get('rows')))
    return present_result, prev_result

#----------------------------------------------------------------------------------------------------------------


def get_sessions(service, profile_id, filters, startDate1, endDate1, startDate2, endDate2):

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

  prev_month = service.data().ga().get(
      ids='ga:' + profile_id,
      start_date=str(startDate2),
      end_date=str(endDate2),
      metrics=metrics,
      dimensions=dimensions,
      filters=filters
  ).execute()

  return pres_month, prev_month

def print_sessions(results, country):

  result1 = (dict(results[0].get('rows')))
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

  result2 = (dict(results[1].get('rows')))
  email = result2.get('(Other)', 0)
  result2['Email'] = email
  try:
    del result2['(Other)']
  except:
      pass
  result2['Country'] = country.split(',')[0]
  result2['Country'] = country.split(',')[0]
  if result2['Country'] == 'United States':
      result2['Country'] = 'US'
  elif result2['Country'] == 'United Kingdom':
      result2['Country'] = 'UK'
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
  d_sessions['Current'] = present = float(results[0].get('totalsForAllResults')['ga:sessions'])
  d_sessions['Previous'] = prev = float(results[1].get('totalsForAllResults')['ga:sessions'])

  change = (present - prev)/prev * 100

  d_sessions['Change'] = str(round(change, 2))+"%"

  print("SESSIONS:\n")
  print(result1, "\n")
  print(result2, "\n")
  print(d_sessions, "\n")

  return result1, result2, d_sessions

#-----------------------------------------------------------------------------

def get_events(service, profile_id, startDate1, endDate1, startDate2, endDate2):

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

    prev_month = service.data().ga().get(
        ids='ga:' + profile_id,
        start_date=str(startDate2),
        end_date=str(endDate2),
        metrics=metrics,
        dimensions=dimensions,
        filters=filters
    ).execute()

    return pres_month, prev_month

def print_events(results, country):
    try:
        # print(country)
        # print(results)
        result1 = (dict(results[0].get('rows')))
    except:
        result1 = {}
    try:
        result2 = (dict(results[1].get('rows')))
    except:
        result2 = {}

    result = {'Country': country.split('Events')[0], 'HelloBar Events': result1.get('HelloBar', 0), 'Previous': result2.get('HelloBar', 0)}
    print("EVENTS:\n")
    print(result)
    return result

#-----------------------------------------------------------------------------

def get_devices(service, profile_id, startDate1, endDate1, startDate2, endDate2):
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

    prev_month = service.data().ga().get(
        ids='ga:' + profile_id,
        start_date=str(startDate2),
        end_date=str(endDate2),
        metrics=metrics,
        dimensions=dimensions,
        filters=filters
    ).execute()
    return pres_month, prev_month

def print_devices(results):

    result1 = (dict(results[0].get('rows')))
    result2 = (dict(results[1].get('rows')))
    result1['Mobile + Tablet'] = int(result1.get('mobile', 0)) + int(result1.get('tablet', 0))
    result2['Mobile + Tablet'] = int(result2.get('mobile', 0)) + int(result2.get('tablet', 0))
    try:
        del result1['mobile']
    except:
        pass
    try:
        del result1['tablet']
    except:
        pass
    try:
        del result2['mobile']
    except:
        pass
    try:
        del result2['tablet']
    except:
        pass


    print("DEVICES:\n")
    print(result1, "\n")
    print(result2, "\n")
    return result1, result2

#-----------------------------------------------------------------------------

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

def print_CPC(results):

    result1 = (dict(results.get('rows')))

    print("CPC:\n")
    print(result1, '\n')
    return result1

#-----------------------------------------------------------------------------

def main(argv, startDate1, endDate1, startDate2, endDate2):
  # Authenticate and construct service
  service, flags = sample_tools.init(
      argv, 'analytics', 'v3', __doc__, __file__,
      scope='https://www.googleapis.com/auth/analytics.readonly')
  # startDate1 = '2018-03-01'
  # endDate1 = '2018-03-31'
  # startDate2 = '2018-02-01'
  # endDate2 = '2018-02-28'

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

      global current, currentb, currentc, currentd, currente

      dict_mobile_tablet = {}
      dict_mobile_tabletb = {}
      dict_mobile_tabletc = {}
      dict_mobile_tabletd = {}
      dict_mobile_tablete = {}
      lst = []
      lstb = []
      lstc = []
      lstd = []
      lste = []

      for profile_id in out:
          results = get_top_keywords(service, profile_id[0], startDate1, endDate1)

          gettingdata = {}
          gettingdata['METRIC'] = results[0].get('totalsForAllResults')['ga:sessions']
          individual = float(gettingdata["METRIC"])
          # print(individual)
          lst.append(individual)

          if profile_id[0] == '88496086':
              dict_mobile_tablet['METRIC'] = 'Mobile+Tablet'
              dict_mobile_tablet['Current'] = current = (lst[0] + lst[1] + lst[2] + lst[3])
              # print(dict_mobile_tablet)

          gettingdatab = {}
          gettingdatab['METRIC'] = results[1].get('totalsForAllResults')['ga:bouncerate']
          individualb = float(gettingdatab["METRIC"])
          # print(individualb)
          lstb.append(individualb)

          if profile_id[0] == '88496086':
              dict_mobile_tabletb['METRIC'] = 'Mobile+Tablet Bounce rate'
              dict_mobile_tabletb['Current'] = currentb = ((lstb[0] + lstb[1] + lstb[2] + lstb[3]) / 4)
              # print(dict_mobile_tabletb)

          gettingdatac = {}
          gettingdatac['METRIC'] = results[2].get('totalsForAllResults')['ga:goalconversionrateall']
          individualc = float(gettingdatac["METRIC"])
          # print(individualc)
          lstc.append(individualc)
          if profile_id[0] == '88496086':
              dict_mobile_tabletc['METRIC'] = 'Returning Visitor Conversions'
              dict_mobile_tabletc['Current'] = currentc = ((lstc[0] + lstc[1] + lstc[2] + lstc[3]) / 4)
              # print(dict_mobile_tabletc)

          gettingdatad = {}
          gettingdatad['METRIC'] = results[3].get('totalsForAllResults')['ga:goalconversionrateall']
          individuald = float(gettingdatad["METRIC"])
          # print(individuald)
          lstd.append(individuald)

          if profile_id[0] == '88496086':
              dict_mobile_tabletd['METRIC'] = 'New/Unique Visitor Conversions'
              dict_mobile_tabletd['Current'] = currentd = ((lstd[0] + lstd[1] + lstd[2] + lstd[3]) / 4)
              # print(dict_mobile_tabletd)

          gettingdatae = {}
          gettingdatae['METRIC'] = results[4].get('totalsForAllResults')['ga:avgsessionduration']
          individuale = float(gettingdatae["METRIC"])
          # print(individuale)
          lste.append(individuale)
          if profile_id[0] == '88496086':
              dict_mobile_tablete['METRIC'] = 'Avg. Session Duration'
              dict_mobile_tablete['Current'] = currente = ((lste[0] + lste[1] + lste[2] + lste[3]) / 4)
              # print(dict_mobile_tablete)

      lst2 = []
      lstb2 = []
      lstc2 = []
      lstd2 = []
      lste2 = []
      for profile_id in out:
          results2 = get_top_keywords_2(service, profile_id[0], startDate2, endDate2)

          gettingdata2 = {}
          gettingdata2['METRIC'] = results2[0].get('totalsForAllResults')['ga:sessions']
          individual2 = float(gettingdata2["METRIC"])
          # print(individual2)
          lst2.append(individual2)
          if profile_id[0] == '88496086':
              dict_mobile_tablet['Previous'] = previous = (lst2[0] + lst2[1] + lst2[2] + lst2[3])
              dict_mobile_tablet['Change'] = (current - previous) / previous * 100
              dict_mobile_tablet['Change'] = str(round(dict_mobile_tablet['Change'], 2)) + '%'
              # print(dict_mobile_tablet)
              dict_mobile_tablet['Current'] = int(dict_mobile_tablet['Current'])
              dict_mobile_tablet['Previous'] = int(dict_mobile_tablet['Previous'])
              MobileTablet.append(dict_mobile_tablet)

          gettingdatab2 = {}
          gettingdatab2['METRIC'] = results2[1].get('totalsForAllResults')['ga:bouncerate']
          individualb2 = float(gettingdatab2["METRIC"])

          # print(individualb2)
          lstb2.append(individualb2)
          if profile_id[0] == '88496086':
              dict_mobile_tabletb['Previous'] = previousb = ((lstb2[0] + lstb2[1] + lstb2[2] + lstb2[3]) / 4)
              dict_mobile_tabletb['Change'] = (currentb - previousb) / previousb * 100
              dict_mobile_tabletb['Change'] = str(round(dict_mobile_tabletb['Change'], 2)) + '%'
              # print(dict_mobile_tabletb)
              dict_mobile_tabletb['Current'] = str(round(dict_mobile_tabletb['Current'], 2)) + '%'
              dict_mobile_tabletb['Previous'] = str(round(dict_mobile_tabletb['Previous'], 2)) + '%'
              MobileTablet.append(dict_mobile_tabletb)

          gettingdatac2 = {}
          gettingdatac2['METRIC'] = results2[2].get('totalsForAllResults')['ga:goalconversionrateall']
          individualc2 = float(gettingdatac2["METRIC"])
          # print(individualc2)
          lstc2.append(individualc2)
          if profile_id[0] == '88496086':
              dict_mobile_tabletc['Previous'] = previousc = ((lstc2[0] + lstc2[1] + lstc2[2] + lstc2[3]) / 4)
              dict_mobile_tabletc['Change'] = (currentc - previousc) / previousc * 100
              dict_mobile_tabletc['Change'] = str(round(dict_mobile_tabletc['Change'], 2)) + '%'
              # print(dict_mobile_tabletc)
              dict_mobile_tabletc['Current'] = str(round(dict_mobile_tabletc['Current'], 2)) + '%'
              dict_mobile_tabletc['Previous'] = str(round(dict_mobile_tabletc['Previous'], 2)) + '%'
              MobileTablet.append(dict_mobile_tabletc)

          gettingdatad2 = {}
          gettingdatad2['METRIC'] = results2[3].get('totalsForAllResults')['ga:goalconversionrateall']
          individuald2 = float(gettingdatad2["METRIC"])
          # print(individuald2)
          lstd2.append(individuald2)

          if profile_id[0] == '88496086':
              dict_mobile_tabletd['Previous'] = previousd = ((lstd2[0] + lstd2[1] + lstd2[2] + lstd2[3]) / 4)
              dict_mobile_tabletd['Change'] = (currentd - previousd) / previousd * 100
              dict_mobile_tabletd['Change'] = str(round(dict_mobile_tabletd['Change'], 2)) + '%'
              # print(dict_mobile_tabletd)
              dict_mobile_tabletd['Current'] = str(round(dict_mobile_tabletd['Current'], 2)) + '%'
              dict_mobile_tabletd['Previous'] = str(round(dict_mobile_tabletd['Previous'], 2)) + '%'
              MobileTablet.append(dict_mobile_tabletd)

          gettingdatae2 = {}
          gettingdatae2['METRIC'] = results2[4].get('totalsForAllResults')['ga:avgsessionduration']
          individuale2 = float(gettingdatae2["METRIC"])
          # print(individuale2)

          lste2.append(individuale2)
          if profile_id[0] == '88496086':
              dict_mobile_tablete['Previous'] = previouse = ((lste2[0] + lste2[1] + lste2[2] + lste2[3]) / 4)
              dict_mobile_tablete['Change'] = (currente - previouse) / previouse * 100
              dict_mobile_tablete['Change'] = str(round(dict_mobile_tablete['Change'], 2)) + '%'
              # print(dict_mobile_tablete)
              dict_mobile_tablete['Current'] = int(dict_mobile_tablete['Current'])
              dict_mobile_tablete['Previous'] = int(dict_mobile_tablete['Previous'])
              MobileTablet.append(dict_mobile_tablete)
              # print('MobileTablet',MobileTablet)
              # print('Ok Done..!')

      out = [
          ('5110029', 'UKPortfolio'),
          ('84906789', 'USAPortfolio'),
          ('85625764', 'FrancePortfolio'),
          ('88496086', 'ChinaPortfolio'),
      ]

      result_present = []

      result_prev = []

      for profile_id in out:
          results = get_agents(service, profile_id[0], startDate1, endDate1, startDate2, endDate2)
          result = print_agents(results)
          result_present.append(result[0])
          result_prev.append(result[1])

      CallClick1 = 0
      EmailClick1 = 0
      EmailbtnClick1 = 0
      # PDFClick1 = 0

      for item in result_present:
          CallClick1 += int(item.get('CallClick', 0))
          EmailClick1 += int(item.get('Click', 0))
          EmailbtnClick1 += int(item.get('EmailClick', 0))
          # VideoImgClick1 += int(item.get('VideoImgClick', 0))

      d1 = {'Click': EmailClick1, 'EmailClick': EmailbtnClick1, 'CallClick': CallClick1}

      CallClick2 = 0
      EmailClick2 = 0
      EmailbtnClick2 = 0
      # PDFClick2 = 0

      for item in result_prev:
          CallClick2 += int(item.get('CallClick', 0))
          EmailClick2 += int(item.get('Click', 0))
          EmailbtnClick2 += int(item.get('EmailClick', 0))
          # VideoImgClick1 += int(item.get('VideoImgClick', 0))

      d2 = {'Click': EmailClick2, 'EmailClick': EmailbtnClick2, 'CallClick': CallClick2}
      keys = list(d2.keys())

      main_out = []

      for key in keys:
          d = {}
          d['METRIC'] = 'Agent {}'.format(key)
          d['Current'] = d1[key]
          d['Previous'] = d2[key]
          change = (float(d1[key]) - float(d2[key])) / float(d2[key]) * 100
          d['Change'] = str(round(change, 2)) + "%"

          main_out.append(d)

      MobileTablet.extend(main_out)

      out = [
          ('5110029', 'UKSideBtn'),
          ('84906789', 'USASideBtn'),
          ('85625764', 'FranceSideBtn'),
          ('88496086', 'ChinaSideBtn'),
      ]

      result_present = []
      result_prev = []

      for profile_id in out:
          results = get_sidebtn(service, profile_id[0], startDate1, endDate1, startDate2, endDate2)
          result = print_sidebtn(results)
          result_present.append(result[0])
          result_prev.append(result[1])

      # EmailClick1 = 0
      # CallClick1 = 0
      # VideoImgClick1 = 0
      # PDFClick1 = 0
      Help1 = 0
      RecentlyViewedPortfolios1 = 0

      for item in result_present:
          # PDFClick1 += int(item.get('PDFClick', 0))
          # EmailClick1 += int(item.get('EmailClick', 0))
          Help1 += int(item.get('Help', 0))
          RecentlyViewedPortfolios1 += int(item.get('RecentlyViewedPortfolios', 0))

      d1 = {'Recently Viewed Clicks': RecentlyViewedPortfolios1, 'Help Clicks': Help1}

      # EmailClick2 = 0
      # CallClick2 = 0
      Help2 = 0
      RecentlyViewedPortfolios2 = 0

      for item in result_prev:
          # PDFClick2 += int(item.get('PDFClick', 0))
          # EmailClick2 += int(item.get('EmailClick', 0))
          Help2 += int(item.get('Help', 0))
          RecentlyViewedPortfolios2 += int(item.get('RecentlyViewedPortfolios', 0))

      d2 = {'Recently Viewed Clicks': RecentlyViewedPortfolios2, 'Help Clicks': Help2}
      keys = list(d1.keys())

      main_out = []
      for key in keys:
          d = {}
          d['METRIC'] = 'Side Nav - {}'.format(key)
          d['Current'] = d1[key]
          d['Previous'] = d2[key]
          change = (float(d1[key]) - float(d2[key])) / float(d2[key]) * 100
          d['Change'] = str(round(change, 2)) + "%"
          main_out.append(d)

      MobileTablet.extend(main_out)

      out = [
          ('5110029', 'UKPortfolio'),
          ('84906789', 'USAPortfolio'),
          ('85625764', 'FrancePortfolio'),
          ('88496086', 'ChinaPortfolio'),
      ]
      result_present = []
      result_prev = []

      for profile_id in out:
          results = get_portpolio(service, profile_id[0], startDate1, endDate1, startDate2, endDate2)
          result = print_portpolio(results)
          result_present.append(result[0])
          result_prev.append(result[1])

      EmailClick1 = 0
      CallClick1 = 0
      VideoImgClick1 = 0
      PDFClick1 = 0

      for item in result_present:
          PDFClick1 += int(item.get('PDFClick', 0))
          EmailClick1 += int(item.get('EmailClick', 0))
          CallClick1 += int(item.get('CallClick', 0))
          VideoImgClick1 += int(item.get('VideoImgClick', 0))

      d1 = {'PDF Downloads': PDFClick1, 'Email Clicks': EmailClick1, 'Call Clicks': CallClick1,
            'Video Image Clicks': VideoImgClick1}

      EmailClick2 = 0
      CallClick2 = 0
      VideoImgClick2 = 0
      PDFClick2 = 0

      for item in result_prev:
          PDFClick2 += int(item.get('PDFClick', 0))
          EmailClick2 += int(item.get('EmailClick', 0))
          CallClick2 += int(item.get('CallClick', 0))
          VideoImgClick2 += int(item.get('VideoImgClick', 0))

      d2 = {'PDF Downloads': PDFClick2, 'Email Clicks': EmailClick2, 'Call Clicks': CallClick2,
            'Video Image Clicks': VideoImgClick2}
      keys = list(d1.keys())

      main_out = []
      for key in keys:
          d = {}
          d['METRIC'] = 'Artist Portfolio - {}'.format(key)
          d['Current'] = d1[key]
          d['Previous'] = d2[key]
          change = (float(d1[key]) - float(d2[key])) / float(d2[key]) * 100
          d['Change'] = str(round(change, 2)) + "%"

          main_out.append(d)

      MobileTablet.extend(main_out)
      MobileTabletSub2 = [
                          MobileTablet[5],
                          MobileTablet[6],
                          MobileTablet[7],
                          MobileTablet[8],
                          MobileTablet[9],
                          MobileTablet[10],
                          MobileTablet[11],
                          MobileTablet[12],
                          MobileTablet[13]
                        ]
      print(MobileTablet)
      print(MobileTabletSub2)

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

      events = [('5110029', 'UKEvents'), ('84906789', 'USAEvents'), ('85625764', 'FranceEvents'), ('88496086', 'ChinaEvents')]

      devices = [('5110029', 'UKDevice'), ('84906789', 'USADevice')]

      cpc = [('5110029', 'UKCPC'), ('84906789', 'USACPC')]

      # startDate1 = str(input("please enter current start date:"))
      # endDate1 = str(input("please enter current end date:"))
      # startDate2 = str(input("please enter previous start date:"))
      # endDate2 = str(input("please enter previous end date:"))

      # startDate1 = '2018-02-26'
      # endDate1 = '2018-03-06'
      # startDate2 = '2018-02-21'
      # endDate2 = '2018-02-25'

      print("******--Sit back and relax this will take sometime--******".upper())
      result_sessions1 = []
      result_sessions2 = []
      sessions = []
      Events = []
      Devices = []
      CPC = []

      for profile_id in events:

          results = get_events(service, profile_id[0], startDate1, endDate1, startDate2, endDate2)
          result = print_events(results, profile_id[1])
          Events.append(result)

      Current_sum = 0
      prev_sum = 0
      for item in Events:
          Current_sum += int(item['HelloBar Events'])
          prev_sum += int(item['Previous'])

      total = {'Country': "Total", 'HelloBar Events': Current_sum, 'Previous': prev_sum}
      Events.append(total)

      for profile_id in devices:

          results = get_devices(service, profile_id[0], startDate1, endDate1, startDate2, endDate2)
          result = print_devices(results)
          Devices.append(result)

      curr_desktop = 0
      curr_mobile = 0
      prev_desktop = 0
      prev_mobile = 0

      for item in Devices:

          curr_desktop += int(item[0].get('desktop', 0))
          curr_mobile += int(item[0].get('Mobile + Tablet', 0))
          prev_desktop += int(item[1].get('desktop', 0))
          prev_mobile += int(item[1].get('Mobile + Tablet', 0))

      Devices = [{'Device': 'Desktop', 'Goal Completions': curr_desktop, 'Previous': prev_desktop},
                 {'Device': 'Mobile + Tablet', 'Goal Completions': curr_mobile, 'Previous': prev_mobile}
                 ]

      for profile_id in cpc:

          results = get_CPC(service, profile_id[0], startDate1, endDate1)
          result = print_CPC(results)
          CPC.append(result)

      keys = []
      for item in CPC:
          key = item.keys()
          key = [item for item in key if item.istitle() or item.title() not in key]
          keys.append(key)
      new_d = {}
      total = 0
      # print(keys)
      for i in keys:

          for j in i:
              new_d[j] = int(CPC[0].get(j, 0)) + int(CPC[1].get(j, 0))
              total += new_d[j]
      f = new_d.items()
      CPC = []
      list1 = ['google', 'Bingads', 'facebookads', 'Instagram']
      i = 0
      while i < 4:
          for k in range(0, len(f)):
              if list1[i]==f[k][0]:
                  new_dict = {}
                  new_dict['Paid Source'] = f[k][0]
                  new_dict['Goal Completions'] = f[k][1]
                  CPC.append(new_dict)
          i += 1
      for item in f:
          if item[0] not in list1:
              new_dict = {}
              new_dict['Paid Source'] = item[0]
              new_dict['Goal Completions'] = item[1]
              CPC.append(new_dict)

      CPC.append({'Paid Source': 'Total', 'Goal Completions': total/2})
      for profile_id in session:

        results = get_sessions(service, profile_id[0], profile_id[1], startDate1, endDate1, startDate2, endDate2)
        result = print_sessions(results, profile_id[1])

        if result[0]['Country'] == 'ROWUSA':
            dict_ROWUSA = result[0]

        elif result[0]['Country'] == 'ROW':
            dict_ROW = result[0]

        else:
            result_sessions1.append(result[0])

        if result[1]['Country'] == 'ROWUSA':
            dict_ROWUSA1 = result[1]
            # print(dict_ROWUSA1)
        elif result[1]['Country'] == 'ROW':
            dict_ROW1 = result[1]
            # print(dict_ROW1)
        else:
            result_sessions2.append(result[1])

        if result[2]['Country'] == 'ROWUSA':
            d_ROWUSA = result[2]
        elif result[2]['Country'] == 'ROW':
            d_ROW = result[2]
        else:
            sessions.append(result[2])

      New_dict = {'Country': "ROW",
                  'Direct': float(dict_ROWUSA.get('Direct', 0)) + float(dict_ROW.get('Direct', 0)),
                  'Email': float(dict_ROWUSA.get('Email', 0)) + float(dict_ROW.get('Email', 0)),
                  'Social': float(dict_ROWUSA.get('Social', 0)) + float(dict_ROW.get('Social', 0)),
                  'Referral': float(dict_ROWUSA.get('Referral', 0)) + float(dict_ROW.get('Referral', 0)),
                  'Paid Search': float(dict_ROWUSA.get('Paid Search', 0)) + float(dict_ROW.get('Paid Search', 0)),
                  'Organic Search': float(dict_ROWUSA.get('Organic Search', 0)) + float(dict_ROW.get('Organic Search', 0))
                  }

      New_dict1 = {'Country': "ROW",
                  'Direct': float(dict_ROWUSA1.get('Direct', 0)) + float(dict_ROW1.get('Direct', 0)),
                  'Email': float(dict_ROWUSA1.get('Email', 0)) + float(dict_ROW1.get('Email', 0)),
                  'Social': float(dict_ROWUSA1.get('Social', 0)) + float(dict_ROW1.get('Social')),
                  'Referral': float(dict_ROWUSA1.get('Referral', 0)) + float(dict_ROW1.get('Referral', 0)),
                  'Paid Search': float(dict_ROWUSA1.get('Paid Search', 0)) + float(dict_ROW1.get('Paid Search', 0)),
                  'Organic Search': float(dict_ROWUSA1.get('Organic Search', 0)) + float(dict_ROW1.get('Organic Search', 0))
                  }
      result_sessions1.append(New_dict)
      result_sessions2.append(New_dict1)

      change = float(d_ROWUSA['Change'].split('%')[0])+float(d_ROW['Change'].split('%')[0])
      New_d = {'Country': "ROW", 'Current': d_ROWUSA['Current']+d_ROW['Current'], 'Previous': d_ROWUSA['Previous']+d_ROW['Previous'], 'Change': str(round(change, 2))+"%"}
      sessions.append(New_d)

      Direct_sum1 = 0
      Email_sum1 = 0
      Social_sum1 = 0
      Referral_sum1 = 0
      Paid_sum1 = 0
      Organic_sum1 = 0

      Direct_sum2 = 0
      Email_sum2 = 0
      Social_sum2 = 0
      Referral_sum2 = 0
      Paid_sum2 = 0
      Organic_sum2 = 0

      out_ = zip(result_sessions1, result_sessions2 )

      for item in out_:
          try:
            Direct_sum1 += float(item[0]['Direct'])
          except:
            Direct_sum1 += 0.0
          try:
            Direct_sum2 += float(item[1]['Direct'])
          except:
            Direct_sum2 += 0.0
          try:
            Email_sum1 += float(item[0]['Email'])
          except:
              Email_sum1 += 0.0
          try:
            Email_sum2 += float(item[1]['Email'])
          except:
              Email_sum2 += 0.0
          try:
            Social_sum1 += float(item[0]['Social'])
          except:
              Social_sum1 += 0.0
          try:
            Social_sum2 += float(item[1]['Social'])
          except:
              Social_sum2 += 0.0
          try:
            Referral_sum1 += float(item[0]['Referral'])
          except:
              Referral_sum1 += 0.0
          try:
            Referral_sum2 += float(item[1]['Referral'])
          except:
              Referral_sum2 += 0.0
          try:
            Paid_sum1 += float(item[0]['Paid Search'])
          except:
              item[0]['Paid Search'] = 0
              Paid_sum1 += 0.0
          try:
            Paid_sum2 += float(item[1]['Paid Search'])
          except:
              Paid_sum2 += 0.0
          try:
            Organic_sum1 += float(item[0]['Organic Search'])
          except:
              Organic_sum1 += 0.0
          try:
            Organic_sum2 += float(item[1]['Organic Search'])
          except:
              Organic_sum2 += 0.0

      total1 = {'Country': 'Total',
                'Direct': Direct_sum1,
                'Email': Email_sum1,
                'Social': Social_sum1,
                'Referral': Referral_sum1,
                'Paid Search': Paid_sum1,
                'Organic Search': Organic_sum1
                }
      total2 = {'Country': 'Total(prev)',
                'Direct': Direct_sum2,
                'Email': Email_sum2,
                'Social': Social_sum2,
                'Referral': Referral_sum2,
                'Paid Search': Paid_sum2,
                'Organic Search': Organic_sum2
                }

      change1 = ((total1['Direct'] - total2['Direct'])/total2['Direct'])*100
      change2 = ((total1['Email'] - total2['Email'])/total2['Email'])*100
      change3 = ((total1['Social'] - total2['Social']) / total2['Social']) * 100
      change4 = ((total1['Referral'] - total2['Referral']) / total2['Referral']) * 100
      change5 = ((total1['Paid Search'] - total2['Paid Search']) / total2['Paid Search']) * 100
      change6 = ((total1['Organic Search'] - total2['Organic Search']) / total2['Organic Search']) * 100

      Change = {'Country': 'Change',
                'Direct': str(round(change1, 2))+"%",
                'Email': str(round(change2, 2))+"%",
                'Social': str(round(change3, 2))+"%",
                'Referral': str(round(change4, 2))+"%",
                'Paid Search': str(round(change5, 2))+"%",
                'Organic Search': str(round(change6, 2))+"%"
                }

      result_sessions1.append(total1)
      result_sessions1.append(total2)
      result_sessions1.append(Change)

      Current_sum = 0
      prev_sum = 0
      for item in sessions:
          Current_sum += item['Current']
          prev_sum += item['Previous']

      change = (Current_sum - prev_sum) / prev_sum * 100
      total = {'Country': "Total", 'Current': Current_sum, 'Previous': prev_sum, 'Change': str(round(change, 2))+"%"}
      sessions.append(total)

      # def writer_empty_lines():
      #
      #     fieldnames = []
      #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      #     writer.writeheader()
      #     writer.writerow([])

      # with open('table1.csv', 'w') as csvfile:
      #     fieldnames = ['Country', 'Current', 'Previous', 'Change']
      #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      #
      #     writer.writeheader()
      #     writer.writerows(sessions)
      #
      #     writer_empty_lines()
      #
      #     fieldnames = ['Country', 'Organic Search', 'Direct', 'Referral', 'Social', 'Paid Search', 'Email']
      #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      #     writer.writeheader()
      #     writer.writerows(result_sessions1)
      #
      #     writer_empty_lines()
      #
      #     fieldnames = ['Country', 'HelloBar Events', 'Previous']
      #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      #
      #     writer.writeheader()
      #     writer.writerows(Events)
      #
      #     writer_empty_lines()
      #
      #     fieldnames = ['Device', 'Goal Completions', 'Previous']
      #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      #
      #     writer.writeheader()
      #     writer.writerows(Devices)
      #
      #     writer_empty_lines()
      #
      #     fieldnames = ['Paid Source', 'Goal Completions']
      #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      #
      #     writer.writeheader()
      #     writer.writerows(CPC)
      #
      # for csvfile in glob.glob(os.path.join('.', '*.csv')):
      #     wb = xlwt.Workbook()
      #     fpath = csvfile.split("/", 1)
      #     fname = fpath[1].split(".", 1)  ## fname[0] should be our worksheet name
      #
      #     ws = wb.add_sheet(fname[0])
      #     with open(csvfile, 'rb') as f:
      #         reader = csv.reader(f)
      #         for r, row in enumerate(reader):
      #             for c, col in enumerate(row):
      #                 ws.write(r, c, col)
      #     wb.save('output.xls')

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

  result = {"MobileTablet": MobileTablet,
            "MobileTabletSub":MobileTabletSub2,
            "sessions": sessions,
            "result_sessions1": result_sessions1,
            "Events": Events,
            "Devices": Devices,
            "CPC": CPC}
  return result

#-------------------------------------------------------------------------------------

if __name__ == '__main__':
    main(sys.argv)