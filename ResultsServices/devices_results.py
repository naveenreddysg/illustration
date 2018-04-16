from ModelServices.devices_service import DevicesService

class DeviceResults:

    def __init__(self, current_start_date, current_end_date, previous_start_date, previous_end_date):
        self.current_start_date = current_start_date
        self.current_end_date = current_end_date
        self.previous_start_date = previous_start_date
        self.previous_end_date = previous_end_date

    def main(self):

        current_results = DevicesService(self.current_start_date, self.current_end_date).get_data()
        previous_results = DevicesService(self.previous_start_date, self.previous_end_date).get_data()

        main_result = [
            {
            'Device': 'Desktop',
            'Goal Completions': current_results[0]['desktop'],
            'Previous': previous_results[0]['desktop'],
            'Change': str(round(((float(current_results[0]['desktop'])-float(previous_results[0]['desktop'])) /
                                 float(previous_results[0]['desktop'])) * 100, 2)) + '%'
            },
            {
            'Device': 'Mobile + Tablet',
            'Goal Completions': current_results[0]['mobileTablet'],
            'Previous': previous_results[0]['mobileTablet'],
            'Change': str(round(((float(current_results[0]['mobileTablet']) - float(previous_results[0]['mobileTablet'])) /
                              float(previous_results[0]['mobileTablet'])) * 100, 2)) + '%'
            }
         ]
        print(main_result)
        return main_result