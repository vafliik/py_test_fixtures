def start_with_circles():
    print('\nInserting sample Circles to Database ... it takes 10 seconds, it is huuuge')


def dump_event_log_to_json():
    print('\nGeting event log ... dumping it into JSON file ... DONE!')


class TestCircles:
    def setup_method(self):
        print('\n> Setting up method')
        start_with_circles()

    def teardown_method(self):
        print('\n< Tearing down method')
        dump_event_log_to_json()

    def test_display_all_circles(self):
        print('\nTEST - Reading Circles from Database ... OK ... I am logging everything')

    def test_display_all_circle_users(self):
        print('\nTEST - Browsing Circles and getting users ... OK ... Of course I am logging the users')

    def test_verify_homepage_title(self):
        print('\nTEST - Quickly checking Circles homepage ... I do not care about Circles in DB at all ... OK ... I do not log anything, why should I?')
