from oauth2client.service_account import ServiceAccountCredentials


def load_credentials(scopes: list, credentials: dict) -> ServiceAccountCredentials:
    return ServiceAccountCredentials.from_json_keyfile_dict(
        scopes=scopes, keyfile_dict=credentials
    )
