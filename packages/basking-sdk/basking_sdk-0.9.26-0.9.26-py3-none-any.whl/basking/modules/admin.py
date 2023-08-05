# pylint: disable=line-too-long, invalid-name
"""
Basking.io — Python SDK
- Admin Class: handles administrative functionality.
"""
import json
import logging

from .graphql_query import GraphqlQuery


class Admin:
    def __init__(self, basking_obj):
        self.basking = basking_obj
        self._api: GraphqlQuery = basking_obj._graphql_query
        self.log = logging.getLogger(self.__class__.__name__)
        basking_log_level = logging.getLogger(self.basking.__class__.__name__).level
        self.log.setLevel(basking_log_level)

    def remove_user_from_building(self, user_id: str, location_id: str):
        query, variables = self._api.revoke_access(user_id=user_id, location_id=location_id)
        result = self._api.graphql_executor(query=query, variables=variables)
        data = json.loads(result)
        if 'message' in data:
            self.basking.api_timeout_handler(data)
        elif 'errors' in data:
            self.log.error('Error in query:')
            self.log.error(data['errors'])
        return data

    def add_user_to_building(self, email: str, location_id: str, auth_group_id: int):
        query, variables = self._api.grant_access(email=email, location_id=location_id, auth_group_id=auth_group_id)
        result = self._api.graphql_executor(query=query, variables=variables)
        data = json.loads(result)
