# Trackl Python Client

## Install

`python3 -m pip install git+https://gitlab.com/denny.weinberg/trackl-python-client`
or
`python3 -m pip install trackl-python-client`

## Python

**Usage/Init**

```python
from trackl_client import TracklClient


client = TracklClient(api_endpoint='http://localhost:8080/api/v1', api_key='ey...')

# Or with workspace, email and password
client = TracklClient(api_endpoint='http://localhost:8080/api/v1', workspace='test' login_email='test@test.com', password='test')
```

**Examples**

```python
# Teams: List
teams = client.teams_list()

# Teams: Search
teams = client.teams_search(name='Name')

# Teams: Create
team = client.teams_create(True, 'Name')

# Users: List
users = client.users_list()

# Users: Search
users = client.users_search(email='test@test.com')

# Users: Create
user = client.users_create(True, 'email', 'Name', 'testPWD123$', ['record.read', 'record.write'])

# Teams: Add User
client.teams_add_user(team_name='Name',  user_email='test@test.com')

# Teams: Remove User
client.teams_remove_user(team_name='Name', user_email='test@test.com')

# Teams: List Users
users = client.teams_list_users(team_name='Office')

# Records: Search
records = client.records_search(page=1, page_type='elements', id='1,2', page_size=200, start_date_time_from='2022-10-01', start_date_time_to='2022-10-05', end_date_time_is_null=False, include_user_name=True)

# Records: Validate
record_validity_infos = client.records_validate(1)
```

## CLI

**Usage**

```bash
python3 -m trackl_client.cli
    --api_endpoint ${api_endpoint} --workspace ${workspace} --api_key ${api_key} --login_email ${login_email} --password ${password} 
    users_create|teams_create|teams_add_user|teams_remove_user
    [--help]
    other_arg_1 --other_kwarg_1

# More:

# python3 -m trackl_client.cli --help

# python3 -m trackl_client.cli records_search --help
```

**Init**

```bash
export api_endpoint='http://localhost:8080/api/v1'

export api_key='ey...'

# Or with workspace, email and password
# export workspace='test'
# export login_email='test@test.com'
# export password='test'
```

**Examples**

```bash
# Teams: List
python3 -m trackl_client.cli teams_list

# Teams: Search
python3 -m trackl_client.cli teams_search --name Name

# Teams: Create
python3 -m trackl_client.cli teams_create True Name

# Users: List
python3 -m trackl_client.cli users_list

# Users: Search
python3 -m trackl_client.cli users_search --email test@test.com

# Users: Create
python3 -m trackl_client.cli users_create True email Name testPWD123$ record.read,record.write

# Teams: Add User
python3 -m trackl_client.cli teams_add_user --team_name Name --user_email test@test.com

# Teams: Remove User
python3 -m trackl_client.cli teams_remove_user --team_name Name --user_email test@test.com

# Teams: List Users
python3 -m trackl_client.cli teams_list_users --team_name Office

# Records: Search
python3 -m trackl_client.cli records_search --page 1 --page_type elements --id 1,2 --page_size 200 --start_date_time_from 2022-10-01 --start_date_time_to 2022-10-05 --end_date_time_is_null false --include_user_name True

# Records: Validate
python3 -m trackl_client.cli records_validate 1
```
