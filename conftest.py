import pytest
import json
from playwright.sync_api import Playwright, Page


# <editor-fold desc="Load Environments">
@pytest.fixture(scope='session')
def config():
    with open('config.json') as config_file:
        data = json.load(config_file)
    return data
# </editor-fold>

# <editor-fold desc="Environment Selector">
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="Tin",
        help="Options: tin, bronze, drprod, demo, corp, prod"
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
    yield

# </editor-fold>
