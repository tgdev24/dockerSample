import requests
import sys

url = "http://localhost:5000/get_translation"

SENTENCE_TO_TRANSLATE = sys.argv[1]

payload="{\n    \"sentence\": \"%s\"\n}" % SENTENCE_TO_TRANSLATE
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
