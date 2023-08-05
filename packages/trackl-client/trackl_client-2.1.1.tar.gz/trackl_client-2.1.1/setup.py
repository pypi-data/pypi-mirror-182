# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trackl_client']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.5.0,<0.6.0', 'python-dateutil>=2.8.2,<3.0.0']

setup_kwargs = {
    'name': 'trackl-client',
    'version': '2.1.1',
    'description': 'Trackl Python Client',
    'long_description': "# Trackl Python Client\n\n## Install\n\n`python3 -m pip install git+https://gitlab.com/denny.weinberg/trackl-python-client`\nor\n`python3 -m pip install trackl-python-client`\n\n## Python\n\n**Usage/Init**\n\n```python\nfrom trackl_client import TracklClient\n\n\nclient = TracklClient(api_endpoint='http://localhost:8080/api/v1', api_key='ey...')\n\n#\xa0Or with workspace, email and password\nclient = TracklClient(api_endpoint='http://localhost:8080/api/v1', workspace='test' login_email='test@test.com', password='test')\n```\n\n**Examples**\n\n```python\n# Teams: List\nteams = client.teams_list()\n\n# Teams: Search\nteams = client.teams_search(name='Name')\n\n# Teams: Create\nteam = client.teams_create(True, 'Name')\n\n# Users: List\nusers = client.users_list()\n\n# Users: Search\nusers = client.users_search(email='test@test.com')\n\n# Users: Create\nuser = client.users_create(True, 'email', 'Name', 'testPWD123$', ['record.read', 'record.write'])\n\n# Teams: Add User\nclient.teams_add_user(team_name='Name',  user_email='test@test.com')\n\n# Teams: Remove User\nclient.teams_remove_user(team_name='Name', user_email='test@test.com')\n\n# Teams: List Users\nusers = client.teams_list_users(team_name='Office')\n\n# Records: Search\nrecords = client.records_search(page=1, page_type='elements', id='1,2', page_size=200, start_date_time_from='2022-10-01', start_date_time_to='2022-10-05', end_date_time_is_null=False, include_user_name=True)\n\n# Records: Validate\nrecord_validity_infos = client.records_validate(1)\n```\n\n## CLI\n\n**Usage**\n\n```bash\npython3 -m trackl_client.cli\n    --api_endpoint ${api_endpoint} --workspace ${workspace} --api_key ${api_key} --login_email ${login_email} --password ${password} \n    users_create|teams_create|teams_add_user|teams_remove_user\n    [--help]\n    other_arg_1 --other_kwarg_1\n\n# More:\n\n# python3 -m trackl_client.cli --help\n\n# python3 -m trackl_client.cli records_search --help\n```\n\n**Init**\n\n```bash\nexport api_endpoint='http://localhost:8080/api/v1'\n\nexport api_key='ey...'\n\n#\xa0Or with workspace, email and password\n#\xa0export workspace='test'\n#\xa0export login_email='test@test.com'\n#\xa0export password='test'\n```\n\n**Examples**\n\n```bash\n# Teams: List\npython3 -m trackl_client.cli teams_list\n\n# Teams: Search\npython3 -m trackl_client.cli teams_search --name Name\n\n# Teams: Create\npython3 -m trackl_client.cli teams_create True Name\n\n# Users: List\npython3 -m trackl_client.cli users_list\n\n# Users: Search\npython3 -m trackl_client.cli users_search --email test@test.com\n\n# Users: Create\npython3 -m trackl_client.cli users_create True email Name testPWD123$ record.read,record.write\n\n# Teams: Add User\npython3 -m trackl_client.cli teams_add_user --team_name Name --user_email test@test.com\n\n# Teams: Remove User\npython3 -m trackl_client.cli teams_remove_user --team_name Name --user_email test@test.com\n\n# Teams: List Users\npython3 -m trackl_client.cli teams_list_users --team_name Office\n\n# Records: Search\npython3 -m trackl_client.cli records_search --page 1 --page_type elements --id 1,2 --page_size 200 --start_date_time_from 2022-10-01 --start_date_time_to 2022-10-05 --end_date_time_is_null false --include_user_name True\n\n# Records: Validate\npython3 -m trackl_client.cli records_validate 1\n```\n",
    'author': 'Nobody',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
