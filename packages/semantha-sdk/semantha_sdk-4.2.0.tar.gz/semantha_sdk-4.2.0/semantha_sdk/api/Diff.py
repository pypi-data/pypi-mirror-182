from semantha_sdk.api import SemanthaAPIEndpoint
from semantha_sdk.response import SemanthaPlatformResponse


class Diff(SemanthaAPIEndpoint):
    """ Create diffs between two texts. """

    @property
    def _endpoint(self):
        return self._parent_endpoint + "/diff"

    def create_diff(self, left_text: str, right_text: str) -> SemanthaPlatformResponse:
        """ Create a diff between two given texts.

        Args:
            left_text (object): One of the two texts for the diff.
            right_text (object): The other text for the diff.
        """

        return self._session.post(
            self._endpoint,
            {
                "left": left_text,
                "right": right_text
            }
        ).execute()
