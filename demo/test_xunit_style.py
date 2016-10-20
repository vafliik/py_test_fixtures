def setup_module(module):
    print('\n========== Setting up module: {}'.format(module))


def teardown_module(module):
    print('\n========== Tearing down module: {}'.format(module))


def setup_function(function):
    print('\n===== Setting up function: {}'.format(function))


def teardown_function(function):
    print('\n===== Tearing down function: {}'.format(function))


def test_1():
    print('>>> TEST 1 - Actually doing some testing ')
    assert 1 == 1


def test_2():
    print('>>> TEST 2 - Testing something else ')
    assert 2 > 0

class TestClass:
    @classmethod
    def setup_class(cls):
        print('\n======= Setting up class: {}'.format(cls))

    @classmethod
    def teardown_class(cls):
        print('\n======= Tearing down class: {}'.format(cls))

    def setup_method(self, method):
        print('\n===== Setting up method: {}'.format(method))

    def teardown_method(self, method):
        print('\n===== Tearing down up method: {}'.format(method))

    def test_3(self):
        print('>>> TEST 3 - Testing in class ')
        assert "This" == "This"

    def test_4(self):
        print('>>> TEST 4 - Me like testing in class ')
        assert "This" != "That"
