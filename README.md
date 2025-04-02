**Pytest Tutorial Notes**
=========================

### Step 1: Installing Pytest

*   Install Pytest using pip: `pip install pytest`
*   Verify installation: `pytest --version`

### Step 2: Writing Your First Test

*   Create a Python file (e.g., `test_example.py`)
*   Write a simple test using the `assert` statement:
    ```python
def test_example(): assert 1 + 1 == 2
```
*   Run the test using Pytest: `pytest test_example.py`

### Step 3: Understanding Fixtures

*   Fixtures are setup and teardown functions that run before and after tests
*   Use the `@pytest.fixture` decorator to define a fixture
    ```python
@pytest.fixture
def example_fixture():
    return 1 + 1
```
*   Use the fixture in a test:
    ```python
def test_example_fixture(example_fixture):
    assert example_fixture == 2
```

### Step 4: Parameterized Testing

*   Use the `@pytest.mark.parametrize` decorator to run a test with different input values
    ```python
@pytest.mark.parametrize("a, b, expected", [(1, 1, 2), (2, 2, 4)])
def test_example(a, b, expected):
    assert a + b == expected
```

### Step 5: Running Tests

*   Run all tests in a directory using `pytest`
*   Run a specific test using `pytest -k <test_name>`

### Step 6: Advanced Topics

#### Mocking
Use libraries like `pytest-mock` to mock dependencies in your tests.

#### Test Discovery
Use `pytest.ini` or `tox.ini` to configure test discovery.

#### Parallel Testing
Use `pytest-xdist` to run tests in parallel.

If you'd like more information on any of these topics, feel free to ask!
