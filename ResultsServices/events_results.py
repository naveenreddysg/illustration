from ModelServices.events_service import EventsService

class EventsResults:

    def __init__(self, current_start_date, current_end_date, previous_start_date, previous_end_date):
        self.current_start_date = current_start_date
        self.current_end_date = current_end_date
        self.previous_start_date = previous_start_date
        self.previous_end_date = previous_end_date

    def main(self):

        current_results = EventsService(self.current_start_date, self.current_end_date).get_data()
        previous_results = EventsService(self.previous_start_date, self.previous_end_date).get_data()

        main_result = [
            {'Country': i[0]['country'],
            'Hello Bar Events': i[0]['HelloBarEvents'],
            'Previous': i[1]['HelloBarEvents']
             }
            for i in zip(current_results, previous_results)
        ]

        return main_result