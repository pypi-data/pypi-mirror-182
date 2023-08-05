#!/usr/bin/env python3

"""
This CLI gives us the possibility to use the Trackl API via commandline!
"""

import os
import requests
import dateutil.parser
from datetime import timezone


def _handle_error(resp):
    try:
        resp.raise_for_status()
        return resp.json()
    except:
        print(f'Error')
        raise Exception(resp.content.decode('utf8'))


def _parse_date_time(val):
    """
    Timestamps are stored as UTC in the database. The API returns them as UTC (*Z). Ideally we should store the user's timezone in the database and the API should return the timestamps with the timezone information the user has.
    Until this is done, a client needs to convert that timestamp back into it's local timezone
    """

    return dateutil.parser.isoparse(val).replace(tzinfo=timezone.utc).astimezone(tz=None) if val else None


class TracklClient:
    """
    API doc: https://trackl.labsolution.lu/apidoc
    """

    def __init__(self, api_endpoint=None, workspace=None, api_key=None, login_email=None, password=None):
        self.api_endpoint = api_endpoint or os.environ['api_endpoint']
        
        self.api_key = api_key or os.environ['api_key']
        
        # Get API Key with login
        if not self.api_key:
            workspace = workspace or os.environ.get('workspace')
            login_email = login_email or os.environ.get('login_email')
            password = password or os.environ.get('password')

            resp = requests.get(
                f'{self.api_endpoint}/auth/login',
                params={
                    'workspace_name': self.workspace,
                    'email': login_email,
                    'password': password,
                }
            )
            ret = _handle_error(resp)
            self.api_key = ret['access_api_key']

        print(f'Trackl API CLI successfully initialised')

    def session_get(self):
        # Load Session
        resp = requests.get(
            f'{self.api_endpoint}/session',
            headers={'Authorization': f'Bearer {self.api_key}'},
        )
        session_info = _handle_error(resp)
        return session_info

    def teams_list(self):
        # Load Teams
        resp = requests.get(
            f'{self.api_endpoint}/teams',
            headers={'Authorization': f'Bearer {self.api_key}'},
        )
        teams = _handle_error(resp)
        return teams

    def teams_search(self, name=None):
        resp = requests.get(
            f'{self.api_endpoint}/teams/search',
            headers={'Authorization': f'Bearer {self.api_key}'},
            params={
                'name': name,
            }
        )
        teams = _handle_error(resp)
        return teams

    def teams_create(self, active, name):
        resp = requests.post(
            f'{self.api_endpoint}/teams',
            headers={'Authorization': f'Bearer {self.api_key}'},
            json={
                "active": active,
                "name": name,
            },
        )
        team = _handle_error(resp)
        return team

    def users_list(self):
        # Load Users
        resp = requests.get(
            f'{self.api_endpoint}/users',
            headers={'Authorization': f'Bearer {self.api_key}'},
        )
        users = _handle_error(resp)
        return users

    def users_search(self, email=None, name=None):
        resp = requests.get(
            f'{self.api_endpoint}/users/search',
            headers={'Authorization': f'Bearer {self.api_key}'},
            params={
                'email': email,
                'name': name,
            }
        )
        users = _handle_error(resp)
        return users

    def users_create(self, active, email, name, password, permissions):
        resp = requests.post(
            f'{self.api_endpoint}/users',
            headers={'Authorization': f'Bearer {self.api_key}'},
            json={
                "active": active,
                "email": email,
                "name": name,
                "password": password,
                "permissions": permissions.split(',')
            },
        )
        user = _handle_error(resp)
        return user

    def teams_add_user(self, team_id=None, user_id=None, team_name=None, user_email=None):
        # Load Team
        if team_name:
            team_id = self.teams_search(name=team_name)['items'][0]['id']

        # Load user
        if user_email:
            user_id = self.users_search(email=user_email)['items'][0]['id']

        # Do it
        resp = requests.post(
            f'{self.api_endpoint}/teams/{team_id}/users',
            headers={'Authorization': f'Bearer {self.api_key}'},
            json={
                "user_id": user_id,
            },
        )
        teamuser = _handle_error(resp)
        return teamuser

    def teams_remove_user(self, team_id=None, user_id=None, team_name=None, user_email=None):
        # Load Team
        if team_name:
            team_id = self.teams_search(name=team_name)['items'][0]['id']

        # Load user
        if user_email:
            user_id = self.users_search(email=user_email)['items'][0]['id']

        # Do it
        resp = requests.delete(
            f'{self.api_endpoint}/teams/{team_id}/users/{user_id}',
            headers={'Authorization': f'Bearer {self.api_key}'},
        )
        teamuser = _handle_error(resp)
        return teamuser

    def teams_list_users(self, team_id=None, team_name=None):
        # Load Team
        if team_name:
            team_id = self.teams_search(name=team_name)['items'][0]['id']
        
        # Do it
        resp = requests.get(
            f'{self.api_endpoint}/teams/{team_id}/users',
            headers={'Authorization': f'Bearer {self.api_key}'},
        )
        users = _handle_error(resp)
        return users

    def records_search(self, page=None, page_type=None, page_size=None, id=None, user_id=None, team_id=None, reference=None, redmine_issue=None, client=None, project=None, description_like=None, start_date_time_from=None, start_date_time_to=None, end_date_time_is_null=None, include_user_name=None, update_date_time_from=None, tag=None):
        resp = requests.get(
            f'{self.api_endpoint}/records/search',
            headers={'Authorization': f'Bearer {self.api_key}'},
            params={
                'page': page,
                'page_type': page_type,
                'page_size': page_size,
                'id': id,
                'user_id': user_id,
                'team_id': team_id,
                'reference': reference,
                'redmine_issue': redmine_issue,
                'client': client,
                'project': project,
                'description_like': description_like,
                'start_date_time_from': start_date_time_from,
                'start_date_time_to': start_date_time_to,
                'end_date_time_is_null': end_date_time_is_null,
                'include_user_name': include_user_name,
                'update_date_time_from': update_date_time_from,
                'tag': tag,
            }
        )
        records = _handle_error(resp)

        # Parse date times
        for record in records['items']:
            record['start_date_time'] = _parse_date_time(record['start_date_time'])
            record['end_date_time'] = _parse_date_time(record['end_date_time'])
            record['create_date_time'] = _parse_date_time(record['create_date_time'])
            record['update_date_time'] = _parse_date_time(record['update_date_time'])

        return records

    def records_validate(self, id):
        resp = requests.get(
            f'{self.api_endpoint}/records/{id}/validate',
            headers={'Authorization': f'Bearer {self.api_key}'},
        )
        record_validtiy_infos = _handle_error(resp)
        return record_validtiy_infos
