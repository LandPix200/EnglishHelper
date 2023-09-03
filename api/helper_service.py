import os

import requests
from translate import Translator


class HelperService:
    def __init__(self, sentence: str):
        self.sentence = sentence

    def generate_response(self) -> str:
        API_URL = "https://api-inference.huggingface.co/models/xlm-roberta-base"
        headers = {"Authorization": "Bearer {}".format(os.getenv("HUGGING_FACE_API_KEY"))}

        mask_count = self.arrange_sentence()

        translater = Translator(to_lang="en")
        self.sentence = translater.translate(self.sentence)

        if mask_count == 1:
            response = requests.post(API_URL, headers=headers, json={"inputs": self.sentence})
            token_str = response.json()[0]["token_str"]
            return self.sentence.replace("<mask>", token_str)

        if mask_count > 1:
            response = requests.post(API_URL, headers=headers, json={"inputs": self.sentence})
            token_str_list = [token[0]["token_str"] for token in response.json()]
            for token_str in token_str_list:
                self.sentence = self.sentence.replace("<mask>", token_str, 1)
            return self.sentence

    def arrange_sentence(self):
        # change ... to <mask> in sentence
        self.sentence = self.sentence.replace("...", "<mask>")
        return self.sentence.count("<mask>")
