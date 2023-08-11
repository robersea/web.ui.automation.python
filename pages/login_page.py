class LoginPage:

    def __init__(self, page):
        self.page = page
        self.user_name = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def login(self, config, env, user_type):
        self.user_name.fill(config['Environments'][f'{env}']['Users'][f'{user_type}']['UserName'])
        self.password.fill(config['Environments'][f'{env}']['Users'][f'{user_type}']['Password'])
        self.login_button.click()
