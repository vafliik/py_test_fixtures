import pytest

# SCOPE
# Module = Run once per module
# Class = Run once per class of tests
# Function = Run once per tests
# Session = Run once per session (To properly demonstrate, all tests from the demo/ folder needs to be run at once)

@pytest.fixture(scope='module')
def module_resource():
    print('\n++ Module fixture setup')
    yield module_resource
    print('\n++ Module fixture teardown')

@pytest.fixture(scope='class')
def class_resource():
    print('\n** Class fixture setup')
    yield class_resource
    print('\n** Class fixture teardown')

@pytest.fixture(scope='session')
def session_resource():
    print('\n-- Session fixture setup')
    yield session_resource
    print('\n-- Session fixture teardown')

@pytest.fixture()
def function_resource():
    print('\n// Function (default) fixture setup')
    yield function_resource
    print('\n// Function (default) fixture teardown')


class TestA:

    def test_A1(self, module_resource, class_resource, function_resource, session_resource ):
        print('>>> CLASS A TEST 1')

    def test_A2(self, module_resource, class_resource, function_resource):
        print('>>> CLASS A TEST 2')

class TestB:

    def test_B1(self, module_resource, class_resource, function_resource, session_resource ):
        print('>>> CLASS B TEST 1')

    def test_B2(self, module_resource, class_resource, function_resource):
        print('>>> CLASS B TEST 2')
