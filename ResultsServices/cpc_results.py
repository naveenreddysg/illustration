from ModelServices.cpc_service import CPCService

class CPCResults:

    def __init__(self, current_start_date, current_end_date,previous_start_date,previous_end_date):
        self.current_start_date = current_start_date
        self.current_end_date = current_end_date
        self.previous_start_date = previous_start_date
        self.previous_end_date = previous_end_date

    @staticmethod
    def total(result):
        res_data = {'Paid Source': 'Total', 'Goal Completions': 0, 'Previous': 0}
        for item in result:
            res_data['Goal Completions'] += item['Goal Completions']
            res_data['Previous'] += item['Previous']
        return res_data

    def main(self):

        current_results = CPCService(self.current_start_date, self.current_end_date).get_data()
        previous_results = CPCService(self.previous_start_date,self.previous_end_date).get_data()
        main_result = [
            {'Paid Source': 'Google ads', 'Goal Completions': current_results[0]['google'], 'Previous': previous_results[0]['google']},
            {'Paid Source': 'Bing ads', 'Goal Completions': current_results[0]['Bingads'], 'Previous': previous_results[0]['Bingads']},
            {'Paid Source': 'Facebook ads', 'Goal Completions': current_results[0]['facebookads'], 'Previous': previous_results[0]['facebookads']},
            {'Paid Source': 'Instagram ads', 'Goal Completions': current_results[0]['Instagram'], 'Previous': previous_results[0]['Instagram']}
         ]

        total = self.total(main_result)
        main_result.append(total)
        return main_result