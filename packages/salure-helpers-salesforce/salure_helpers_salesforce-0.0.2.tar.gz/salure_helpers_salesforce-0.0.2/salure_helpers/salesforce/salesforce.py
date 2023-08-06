import urllib.parse
import requests
from typing import Union, List
from salure_helpers.salureconnect import SalureConnect


class Salesforce(SalureConnect):
    """
    This class is meant to be a simple wrapper around the Salesforce API. In order to start using it, authorize your application is Salureconnect.
    You will receive a code which you can use to obtain a refresh token using the get_refresh_token method. Use this refresh token to refresh your access token always before you make a data call.
    """
    def __init__(self, label: Union[str, List], debug: bool = False):
        super().__init__()
        self.credentials = self.get_system_credential(system='salesforce', label=label)
        self.credential_id = self.credentials['id']
        self.customer_url = self.credentials['instance_url']
        self.debug = debug

    def __get_headers(self) -> dict:
        credentials = self.refresh_system_credential(system='salesforce', system_id=self.credential_id)
        headers = {"Authorization": f"Bearer {credentials['access_token']}"}
        if self.debug:
            print(f"Headers: {headers}")
        return headers

    def query_data(self, query: str) -> requests.Response:
        """
        This method is used to send raw queries to Salesforce.
        :param query: Querystring. Something like: 'select+Name,Id+from+Account'
        :return: data or error
        """
        params = {
            "q": query
        }
        if self.debug:
            print(f"Query: {query}")
        params_str = urllib.parse.urlencode(params, safe=':+')
        response = requests.request(method="GET", url=f"{self.customer_url}services/data/v37.0/query/?", params=params_str, headers=self.__get_headers())

        return response

    def get_data(self, fields: Union[str, List], object_name: str, filter: str = None) -> requests.Response:
        """
        This method is used to send queries in a somewhat userfriendly wayt to Salesforce.
        :param fields: fields you want to get
        :param object_name: table or object name that the fields need to be retrieved from
        :param filter: statement that evaluates to True or False
        :return: data or error
        """
        fields = ",".join(fields) if isinstance(fields, List) else fields
        params = {
            "q": f"SELECT {fields} FROM {object_name}{' WHERE ' + filter if filter is not None else ''}"
        }
        if self.debug:
            print(f"Query: {params['q']}")
        params_str = urllib.parse.urlencode(params, safe=':+')
        response = requests.get(url=f"{self.customer_url}services/data/v37.0/query/?", params=params_str, headers=self.__get_headers())

        return response
