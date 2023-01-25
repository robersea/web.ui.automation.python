# python playwright web ui automation template

Example template for web ui automation using Python and Playwright

Guide assumes latest version of Python installed on users machine.

Project structure:

ProjectName
-pages
-tests
-conftest.py
-environments.json
-pytest.ini

After project structure created you can run the following:
pip install pipenv
pipenv install pytest-playwright
pipenv install pytest-reporter-hmtl1 (This is optional if you want easily readable reports)
playwright install (This installs all browsers)

You should now have a pipfile and pipfile.lock


