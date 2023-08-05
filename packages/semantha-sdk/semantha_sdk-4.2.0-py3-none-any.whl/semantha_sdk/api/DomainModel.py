from semantha_sdk.api import SemanthaAPIEndpoint
from semantha_sdk.api.Boostwords import Boostwords
from semantha_sdk.rest.RestClient import RestClient


class DomainModel(SemanthaAPIEndpoint):

    def __init__(self, session: RestClient, parent_endpoint: str, domain_name: str):
        super().__init__(session, parent_endpoint)
        self._domain_name = domain_name
        self.__boostwords = Boostwords(session, self._endpoint)

    @property
    def _endpoint(self):
        return self._parent_endpoint + f"/{self._domain_name}"

    @property
    def boostwords(self):
        return self.__boostwords


class Domains:

    def __init__(self, session: RestClient, parent_endpoint: str):
        self._session = session
        self.__endpoint = parent_endpoint + "/domains"

    def get_one(self, domain_name: str) -> DomainModel:
        # Returns a Domain object for the given domainname, throws error if id doesn't exist
        return DomainModel(self._session, self.__endpoint, domain_name)
