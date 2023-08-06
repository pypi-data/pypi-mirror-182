import json
import base64
import requests


class Progressively:
    flags = {}
    apiUrl = ""

    def __init__(self, apiUrl):
        self.apiUrl = apiUrl

    @staticmethod
    def create(clientKey, apiUrl, fields={}):
        fields["clientKey"] = clientKey
        jsonStr = json.dumps(fields)
        b64Fields = base64.b64encode(jsonStr.encode('utf-8'))
        b64Str = b64Fields.decode("utf-8")
        apiUrlWithParams = apiUrl + "/sdk/" + b64Str

        sdk = Progressively(apiUrlWithParams)
        sdk.loadFlags()

        return sdk

    def loadFlags(self):
        try:
            r = requests.get(self.apiUrl)
            self.flags = r.json()
        except:
            self.flags = {}

    def evaluate(self, flagKey):
        return self.flags[flagKey]
