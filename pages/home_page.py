
class HomePage:

    def __init__(self, page):
        self.page = page
        self.title = page.locator("title_locator")