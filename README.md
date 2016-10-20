# py_test_fixtures
Demo of py.test fixtures

https://en.wikipedia.org/wiki/Test_fixture#Software

http://doc.pytest.org/en/latest/fixture.html

A software test fixture sets up the system for the testing process by providing it with all the necessary code to initialize it.

The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute.

## xunit style
http://doc.pytest.org/en/latest/xunit_setup.html#xunitsetup
* Module level setup/teardown
* Class level setup/teardown
* Method and function level setup/teardown

[Demo](demo/test_xunit_style.py)

### problem with xunit
Sometimes you setup / teardown resources that you do not need for the test - it can cost resources and time

[Demo](demo/test_xunit_problem.py)

The problem can still be solvable by separating the tests to different classes, modules, etc.

But with py.test fixtures it is not necessary

## py.test fixtures
Use anotations to specify fixture functions (import pytest first)

```python
import pytest

@pytest.fixture()
def clean_db():
```

Then use your fixtures as parameters of your test methods - order matters!
```python
def test_display_all_circles(self, clean_db, start_with_circles, dump_event_log_to_json):
    pass
```

### But what about the setup vs teardown?
Is is simple with methods that should be run **before** the test.

If a code needs to be run **after** the test (cleanup etc.), it there are two ways

*Note that one fixture can contain code to execute BEFORE and AFTER test* - at it will get even better

#### Use 'request' and finalizer
```python
@pytest.fixture()
def cleanup(request):
    # any code here will be executed BEFORE test, as any other fixture
    def cleanup_code():
        # this will be executed AFTER test
        print('Cleaning after test')
    request.addfinalizer(cleanup_code)
```

[Demo](demo/test_pytest_problem_solution1.py)

#### Use yield
```python
@pytest.fixture()
def cleanup():
    # any code here will be executed BEFORE test, as any other fixture
    yield cleanup
    # this will be executed AFTER test
    print('Cleaning after test')
```

[Demo](demo/test_pytest_problem_solution2.py)


pytest and xunit can mix together


