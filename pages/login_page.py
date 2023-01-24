
class LoginPage:

    def __init__(self, page):
        self.page = page
        self.user_name = page.locator("example_user_name_locator")
        self.password = page.locator("example_password_locator")
        self.login_button = page.locator("example_login_button_locator")

    def login(self, config, env, user_type):
        self.user_name.fill(config['Environments'][f'{env}']['Users'][f'{user_type}']['UserName'])
        self.password.fill(config['Environments'][f'{env}']['Users'][f'{user_type}']['Password'])
        self.login_button.click()

