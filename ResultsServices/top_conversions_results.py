from ModelServices.portfolio_service import PortflioService
from ModelServices.agents_service import AgentsService
from ModelServices.side_btn_service import SideBtnService
from ModelServices.top_conversion_service import TopConversionsService

class TopConversionsResults:

    def __init__(self, current_start_date, current_end_date, previous_start_date, previous_end_date):
        self.current_start_date = current_start_date
        self.current_end_date = current_end_date
        self.previous_start_date = previous_start_date
        self.previous_end_date = previous_end_date

    def main(self):
        portfolio_current_results = PortflioService(self.current_start_date, self.current_end_date).get_data()
        portfolio_previous_results = PortflioService(self.previous_start_date, self.previous_end_date).get_data()
        agents_current_results = AgentsService(self.current_start_date, self.current_end_date).get_data()
        agents_previous_results = AgentsService(self.previous_start_date, self.previous_end_date).get_data()
        side_btn_current_results = SideBtnService(self.current_start_date, self.current_end_date).get_data()
        side_btn_previous_results = SideBtnService(self.previous_start_date, self.previous_end_date).get_data()
        top_conversion_current_results = TopConversionsService(self.current_start_date, self.current_end_date).get_data()
        top_conversion_previous_results = TopConversionsService(self.previous_start_date, self.previous_end_date).get_data()
        top_conversion_result = [
            {'Metric': 'Mobile+Tablet',
             'Current': top_conversion_current_results[0]['MobileTablet'],
             'Previous': top_conversion_previous_results[0]['MobileTablet'],
             'Change': str(round((((float(top_conversion_current_results[0]['MobileTablet']) -
                                    float(top_conversion_previous_results[0]['MobileTablet']))
                                  /float(top_conversion_previous_results[0]['MobileTablet']))*100), 2))+'%'
             },
            {'Metric': 'Mobile+Tablet Bounce Rate',
             'Current': top_conversion_current_results[0]['BounceRate'],
             'Previous': top_conversion_previous_results[0]['BounceRate'],
             'Change': str(round((float(top_conversion_current_results[0]['BounceRate']) -
                                    float(top_conversion_previous_results[0]['BounceRate'])), 2)) + '%'
             },
            {'Metric': 'Returning Visitor Conversions',
             'Current': top_conversion_current_results[0]['ReturningConversions'],
             'Previous': top_conversion_previous_results[0]['ReturningConversions'],
             'Change': str(round((float(top_conversion_current_results[0]['ReturningConversions']) -
                                    float(top_conversion_previous_results[0]['ReturningConversions'])), 2)) + '%'
             },
            {'Metric': 'New/Unique Visitor Conversions',
             'Current': top_conversion_current_results[0]['UniqueConversions'],
             'Previous': top_conversion_previous_results[0]['UniqueConversions'],
             'Change': str(round((float(top_conversion_current_results[0]['UniqueConversions']) -
                                    float(top_conversion_previous_results[0]['UniqueConversions'])), 2)) + '%'
             },
            {'Metric': 'Avg. Session Duration',
             'Current': top_conversion_current_results[0]['SessionDuration'],
             'Previous': top_conversion_previous_results[0]['SessionDuration'],
             'Change': str(round((((float(top_conversion_current_results[0]['SessionDuration']) -
                                    float(top_conversion_previous_results[0]['SessionDuration']))
                                   / float(top_conversion_previous_results[0]['SessionDuration'])) * 100), 2)) + '%'
             },
        ]
        agents_result = [
            {'Metric': 'Agent Email Clicks',
             'Current': agents_current_results[0]['click'],
             'Previous': agents_previous_results[0]['click'],
             'Change': str(round((((float(agents_current_results[0]['click']) -
                                    float(agents_previous_results[0]['click']))
                                   / float(agents_previous_results[0]['click'])) * 100), 2)) + '%'
             },
            {'Metric': 'Agent PopUp Email Btn Click',
             'Current': agents_current_results[0]['emailClick'],
             'Previous': agents_previous_results[0]['emailClick'],
             'Change': str(round((((float(agents_current_results[0]['emailClick']) -
                                    float(agents_previous_results[0]['emailClick']))
                                   / float(agents_previous_results[0]['emailClick'])) * 100), 2)) + '%'
             },
            {'Metric': 'Agent PopUp Call Btn Click',
             'Current': agents_current_results[0]['callClick'],
             'Previous': agents_previous_results[0]['callClick'],
             'Change': str(round((((float(agents_current_results[0]['callClick']) -
                                    float(agents_previous_results[0]['callClick']))
                                   / float(agents_previous_results[0]['callClick'])) * 100), 2)) + '%'
             }
        ]
        side_btn_result = [
            {'Metric': 'Side Nav- Recently Viewed Clicks',
             'Current': side_btn_current_results[0]['recentlyViewedPortfolios'],
             'Previous': side_btn_previous_results[0]['recentlyViewedPortfolios'],
             'Change': str(round((((float(side_btn_current_results[0]['recentlyViewedPortfolios']) -
                                    float(side_btn_previous_results[0]['recentlyViewedPortfolios']))
                                   / float(side_btn_previous_results[0]['recentlyViewedPortfolios'])) * 100), 2)) + '%'
             },
            {'Metric': 'Side Nav- Help Clicks',
             'Current': side_btn_current_results[0]['Help'],
             'Previous': side_btn_previous_results[0]['Help'],
             'Change': str(round((((float(side_btn_current_results[0]['Help']) -
                                    float(side_btn_previous_results[0]['Help']))
                                   / float(side_btn_previous_results[0]['Help'])) * 100), 2)) + '%'
             },
        ]
        portfolio_result = [
            {'Metric': 'Artist Portfolio - PDF Downloads',
             'Current': portfolio_current_results[0]['PDFDownloads'],
             'Previous': portfolio_previous_results[0]['PDFDownloads'],
             'Change': str(round((((float(portfolio_current_results[0]['PDFDownloads']) -
                                    float(portfolio_previous_results[0]['PDFDownloads']))
                                   / float(portfolio_previous_results[0]['PDFDownloads'])) * 100), 2)) + '%'
             },
            {'Metric': 'Artist Portfolio - Email Clicks',
             'Current': portfolio_current_results[0]['EmailClicks'],
             'Previous': portfolio_previous_results[0]['EmailClicks'],
             'Change': str(round((((float(portfolio_current_results[0]['EmailClicks']) -
                                    float(portfolio_previous_results[0]['EmailClicks']))
                                   / float(portfolio_previous_results[0]['EmailClicks'])) * 100), 2)) + '%'
             },
            {'Metric': 'Artist Portfolio - Call Clicks',
             'Current': portfolio_current_results[0]['CallClicks'],
             'Previous': portfolio_previous_results[0]['CallClicks'],
             'Change': str(round((((float(portfolio_current_results[0]['CallClicks']) -
                                    float(portfolio_previous_results[0]['CallClicks']))
                                   / float(portfolio_previous_results[0]['CallClicks'])) * 100), 2)) + '%'
             },
            {'Metric': 'Artist Portfolio - Video Image Clicks',
             'Current': portfolio_current_results[0]['VideoImageClicks'],
             'Previous': portfolio_previous_results[0]['VideoImageClicks'],
             'Change': str(round((((float(portfolio_current_results[0]['VideoImageClicks']) -
                                    float(portfolio_previous_results[0]['VideoImageClicks']))
                                   / float(portfolio_previous_results[0]['VideoImageClicks'])) * 100), 2)) + '%'
             },
        ]
        main_result = top_conversion_result+agents_result+side_btn_result+portfolio_result
        return main_result