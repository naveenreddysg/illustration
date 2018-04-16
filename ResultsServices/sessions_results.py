from ModelServices.sessions_service import SessionsService

class SessionsResults:

    def __init__(self, current_start_date, current_end_date, previous_start_date, previous_end_date):
        self.current_start_date = current_start_date
        self.current_end_date = current_end_date
        self.previous_start_date = previous_start_date
        self.previous_end_date = previous_end_date

    def main(self):

        current_results = SessionsService(self.current_start_date, self.current_end_date).get_data()
        previous_results = SessionsService(self.previous_start_date, self.previous_end_date).get_data()

        main_result = [
            {'Country': i[0]['country'],
            'Current': i[0]['totalSessions'],
            'Previous': i[1]['totalSessions'],
            'Change': str(round((((float(i[0]['totalSessions'])-float(i[1]['totalSessions']))
                                  /float(i[1]['totalSessions']))*100), 2))+'%'}
            for i in zip(current_results, previous_results)
        ]

        return main_result