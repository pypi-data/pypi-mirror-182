# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['basecampapi']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'basecampapi',
    'version': '0.1.0',
    'description': '',
    'long_description': '\n# Basecamp API integration\n\n  \n\nThis module allows you to interact with Basecamp through python.\n\n  \n\n## Table of contents\n\n1. [Requirements](https://github.com/markostefanovic1/basecamp_api#1-requirements "Requirements")\n2. [Installation](https://github.com/markostefanovic1/basecamp_api#2-installation "Installation")\n3. [How to use](https://github.com/markostefanovic1/basecamp_api#3--how-to-use "How to use")\n\t- Initial authentication - getting your refresh token\n\t- Generating and using Basecamp sessions\n\t- \n\n\n\n## 1. Requirements\n- Python 3.7 or higher\n- Compatible "requests" library\n\n## 2. Installation\n\n-\n\n  \n\n## 3.  How to use\n\n### Initial authentication - Acquiring your refresh token\n\nTo be able to interact with Basecamp\'s API, you need to provide an access token upon each API request. Basecamp\'s access tokens are set to expire 2 weeks after being generated, which is why you actually need to acquire a refresh token.\n\nRefresh tokens allow us to automate the process of generating an access token. Generating it requires some manual work, but you only have to do it once and after that you can use it to gain access to Basecamp each time you run your script.\n\nTo gain access you need a developer app on Basecamp. App can be created on https://launchpad.37signals.com/integrations, after which you need to use the generated Client ID, Client Secret and the Redirect URI which you provided for initial authentication.\n\nTo begin the authentication process, first you need to create a link for acquiring a short-term verification code and go to that link. Use your Client ID and Redirect URI inside of the link:\n\n```python\n# Enter your credentials\nclient_id = "your-client-id"\nredirect_uri = "your-redirect-uri"\n\nurl = f"https://launchpad.37signals.com/authorization/new?type=web_server&client_id={client_id}&redirect_uri={redirect_uri}"\nprint(url)\n```\n\nOpen the link that you printed, it will take you to the verification page. Click on "Yes, I\'ll allow access":\n\n[![Verification page](https://user-images.githubusercontent.com/105298890/208861486-3faa5a4d-93aa-4523-90d1-632d67334975.png  "Verification page")](https://user-images.githubusercontent.com/105298890/208861486-3faa5a4d-93aa-4523-90d1-632d67334975.png  "Verification page")\n\nIt will redirect you to the link you provided as Redirect URI, but it will have the verification code in the url address. Save that verification code:\n\n[![Verification code](https://user-images.githubusercontent.com/105298890/208861435-012c3328-3c41-4489-b57d-436106886fcf.png  "Verification code")](https://user-images.githubusercontent.com/105298890/208861435-012c3328-3c41-4489-b57d-436106886fcf.png  "Verification code")\n\nUse the verification code together with other credentials to send a POST request to the following link (you will need to use the "requests" library for this):\n\n```python\n# Enter your credentials\nclient_id = "your-client-id"\nclient_secret = "your-client-secret"\nredirect_uri = "your-redirect-uri"\nverification_code = "your-verification-code"\n\nurl = f"https://launchpad.37signals.com/authorization/token?type=web_server&client_id={client_id}&redirect_uri={redirect_uri}&client_secret={client_secret}&code={verification_code}"\nresponse = requests.post(url)\nrefresh_token = response.json()["refresh_token"]\nprint(refresh_token)\n```\n\nOnce you do that you will get your refresh token. Make sure to save it and don\'t share it with anyone because it will grant them access to your basecamp account to do whatever they want while logged in as YOU. You will use this refresh token each time you access the Basecamp API, so make sure you save it somewhere safe.\n\n------------\n\n\n\n### Generating and using Basecamp sessions\nTo interact with objects on Basecamp you have to initialize a session object. This object will generate your access token and allow you to interact with other Basecamp objects. To do this, you need to pass your credentials and account ID to the Basecamp session object.\n\nYour account ID can be found on your Basecamp home page, in the URL address:\n- https:<SPAN></SPAN>//3.basecamp.com/<b>YOUR-ACCOUNT-ID</b>/projects\n\n```python\ncredentials = {\n\t"client_id": "your-client-id",\n\t"client_secret": "your-client-secret",\n\t"redirect_uri": "your-redirect-uri",\n\t"refresh_token": "your-refresh-token"\n}\n\nbasecamp_session = Basecamp(account_id="your-account-id", credentials=credentials)\n```\nAfter that you will be able to use your session object within other Basecamp objects.\n\n```python\nmy_campfire = Campfire(campfire_id=\'your-campfire-id\', project_id=\'your-project-id\', session=basecamp_session)\nmy_campfire.info() # Shows basic information about the campfire\nmy_campfire.write(content="Hello from Python!") # Sends a campfire message with desired content\n```\n\n------------\n\n',
    'author': 'mare011rs',
    'author_email': 'mare011rs@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
