from ModelServices.cpc_service import CPCService

class CPCResults:

    def __init__(self, current_start_date, current_end_date):
        self.current_start_date = current_start_date
        self.current_end_date = current_end_date

    def main(self):

        current_results = CPCService(self.current_start_date, self.current_end_date).get_data()
        main_result = [
            {'Paid Source': 'Google ads', 'Goal Completions': current_results[0]['google']},
            {'Paid Source': 'Bing ads', 'Goal Completions': current_results[0]['Bingads']},
            {'Paid Source': 'Facebook ads', 'Goal Completions': current_results[0]['facebookads']},
            {'Paid Source': 'Instagram ads', 'Goal Completions': current_results[0]['Instagram']}
         ]
        return main_result