from ModelServices.sessions_category_services import SessionsCategoryService

class SessionsCategoryResults:

    def __init__(self, current_start_date, current_end_date, previous_start_date, previous_end_date):
        self.current_start_date = current_start_date
        self.current_end_date = current_end_date
        self.previous_start_date = previous_start_date
        self.previous_end_date = previous_end_date

    @staticmethod
    def total(result, country):
        res_data = {'Country': country, 'Organic Search': 0, 'Direct': 0, 'Paid Search': 0, 'Referral': 0, 'Social': 0, 'Email': 0}
        for item in result:
            res_data['Organic Search'] += item['organicSearch']
            res_data['Direct'] += item['direct']
            res_data['Paid Search'] += item['paidSearch']
            res_data['Referral'] += item['referral']
            res_data['Social'] += item['social']
            res_data['Email'] += item['email']
        return res_data

    @staticmethod
    def change_cal(total1, total2):
        change_dict = {}
        change_dict['Country'] = 'Change'
        for key, value in total1.iteritems():
            try:
                change_dict[key] = str(round(((float(total1[key])-float(total2[key]))/float(total2[key])) * 100, 2)) + '%'
            except Exception as e:
                # print e
                pass
        return change_dict

    @staticmethod
    def result(results):
        main_result = [
            {'Country': i['country'],
             'Direct': i['direct'],
             'Paid Search': i['paidSearch'],
             'Organic Search': i['organicSearch'],
             'Referral': i['referral'],
             'Social': i['social'],
             'Email': i['email']
             }
            for i in results
        ]
        return main_result

    def main(self):
        current_results = SessionsCategoryService(self.current_start_date, self.current_end_date).get_data()
        previous_results = SessionsCategoryService(self.previous_start_date, self.previous_end_date).get_data()
        main_result = self.result(current_results)
        total_current = self.total(current_results, 'Total')
        total_previous = self.total(previous_results, 'Total(Prev)')
        change = self.change_cal(total_current, total_previous)
        main_result.append(total_current)
        main_result.append(total_previous)
        main_result.append(change)
        return main_result

    def mainprev(self):
        previous_results = SessionsCategoryService(self.previous_start_date, self.previous_end_date).get_data()
        main_resultPrev = [
            {'Country': i['country'],
             'Direct': i['direct'],
             'Paid Search': i['paidSearch'],
             'Organic Search': i['organicSearch'],
             'Referral': i['referral'],
             'Social': i['social'],
             'Email':i['email']
             }
            for i in previous_results
        ]
        return main_resultPrev