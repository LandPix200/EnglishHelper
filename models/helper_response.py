class HelperResponse:
    def __init__(self, response_map: dict):
        self.score = response_map["score"]
        self.token = response_map["token"]
        self.token_str = response_map["token_str"]
        self.sequence = response_map["sequence"]
