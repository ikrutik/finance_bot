from typing import List, Dict

from oauth2client.service_account import ServiceAccountCredentials


def load_credentials(scopes: List[str], credentials: Dict[str, str]) -> ServiceAccountCredentials:
    """
    Load credentials for authorization to GoogleServices
    :param scopes: Available scopes
    :param credentials: Credentials
    """

    return ServiceAccountCredentials.from_json_keyfile_dict(
        scopes=scopes, keyfile_dict=credentials
    )
