import pytest

@pytest.fixture()
def clean_db():
    print('\nDeleting everything from database')

@pytest.fixture()
def start_with_circles():
    print('\nInserting sample Circles to Database ... it takes 10 seconds, it is huuuge')

@pytest.fixture()
def dump_event_log_to_json():
    print('\nEvent log just warming up')
    yield dump_event_log_to_json
    print('\nGeting event log ... dumping it into JSON file ... DONE!')


class TestCircles:

    def test_display_all_circles(self, clean_db, start_with_circles, dump_event_log_to_json):
        print('\nTEST - Reading Circles from Database ... OK ... I am logging everything')

    def test_display_all_circle_users(self, start_with_circles):
        print('\nTEST - Browsing Circles and getting users ... OK ...I do not log users, they do not like it')

    def test_verify_homepage_title(self):
        print('\nTEST - Quickly checking Circles homepage ... I do not care about Circles in DB at all ... OK ... I do not log anything, why should I?')
