import pytest
from playwright.sync_api import expect

from pages.home_page import HomePage

@pytest.mark.user_type("TestUser1")
def test_example(login, page):
    home_page = HomePage(page)
    expect(home_page.title).to_have_title("Example title text")

