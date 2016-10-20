import pytest

# just showing that fixtures can be imported ...
from test_pytest_scope import class_resource, function_resource, session_resource, module_resource

@pytest.mark.usefixtures("function_resource", "class_resource")
class TestA:

    def test_A1(self, module_resource, session_resource ):
        print('>>> CLASS A TEST 1')

    def test_A2(self):
        print('>>> CLASS A TEST 2')

class TestB:

    def test_B1(self, module_resource, class_resource, function_resource, session_resource ):
        print('>>> CLASS B TEST 1')

    def test_B2(self, module_resource, class_resource, function_resource):
        print('>>> CLASS B TEST 2')