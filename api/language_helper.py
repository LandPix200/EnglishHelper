import os

import requests


class LanguageHelper:

    @staticmethod
    def get_language(text) -> str:
        api_url = 'https://api.api-ninjas.com/v1/textlanguage?text={}'.format(text)
        response = requests.get(api_url, headers={'X-Api-Key': os.getenv("NINJA_API_KEY")})
        if response.status_code == requests.codes.ok:
            return response.json()['iso']
        else:
            return 'en'


