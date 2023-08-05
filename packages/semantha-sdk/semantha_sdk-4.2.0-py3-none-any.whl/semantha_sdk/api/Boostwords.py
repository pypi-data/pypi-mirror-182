from semantha_sdk.api import SemanthaAPIEndpoint
from semantha_sdk.response import SemanthaPlatformResponse


class Boostwords(SemanthaAPIEndpoint):
    @property
    def _endpoint(self):
        return self._parent_endpoint + "/boostwords"

    def get_all(self) -> list:
        """ Get all boostwords """
        return self._session.get(self._endpoint).execute().as_list()

    def post(self, id: str, word: str, regex: str, tags: list[str], label: str) -> SemanthaPlatformResponse:
        """ Create a boostword (not yet implemented)"""
        # TODO implement and adapt DocString
        raise NotImplementedError("Boostwords can not be added yet")
        body = locals()
        return self._session.post(self._endpoint, body).execute()

    def delete_all(self):
        """ Delete all boostwords """
        self._session.delete(self._endpoint).execute()

    def get_one(self, id: str) -> dict:
        """ Get a boostword by id """
        return self._session.get(self._endpoint + f"/{id}").execute().as_dict()

    def put(self, id: str) -> SemanthaPlatformResponse:
        """ Update a boostword by id (not yet implemented)"""
        # TODO implement and adapt DocString
        return self._session.put(self._endpoint + f"/{id}").execute()

    def delete_one(self, id: str):
        """ Delete a boostword by id """
        self._session.delete(self._endpoint + f"/{id}").execute()
