import pytest
import json
from pages.login_page import LoginPage


# <editor-fold desc="Load Environments">

# Use this to load environmental URLs and user login credentials
@pytest.fixture(scope='session')
def config():
    with open('environments.json') as environments_file:
        data = json.load(environments_file)
    return data
# </editor-fold>

# <editor-fold desc="Environment Selector">

# Use this to dynamically pass in what environment you want your tests to run against.
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="Test",
        help="Options: Test, Stage, Prod"
    )


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")
# </editor-fold>

# <editor-fold desc="Login Fixtures">
@pytest.fixture()
def login(config, env, request, page):
    user_type = request.node.get_closest_marker("user_type").args[0]
    page.goto(config['Environments'][f'{env}']['LoginUrl'])
    login = LoginPage(page)
    login.login(config, env, user_type)
    yield

# </editor-fold>
