# create your main function here
# run the necessary operaitons and return
import json
import requests
import os 

CLIENT_ID = "87bd102858597fc75a11"
CLIENT_SECRET = "8db3bf3b15786dd6f1e61d1c04273682f35d7482"
# should be the current url 
REDIRECT_URI = "https://l3utlequjf.execute-api.us-east-1.amazonaws.com/entropy-default/authorize"


def entropy_main(event, context):
    # the input event is in a json string
    # event = json.loads(event)
    # need to get the code 
    print(event)
    raw_query_string = event['rawQueryString']
    code = raw_query_string.split("=")[1]
    # code = "bfcfa4bad6a8b949ab95"

    headers = {"Accept": "application/json"}
    params = {"client_id": CLIENT_ID,
            "client_secret":CLIENT_SECRET,
            "code": code,  
            "redirect_uri": REDIRECT_URI}
    r = requests.post('https://github.com/login/oauth/access_token',
        headers=headers, params=params)

    resp = json.loads(r.text)
    print(resp)
    access_token = resp['access_token']
    # save the access token to the db 

    # return {"response": "this is my entropy function", "resp":resp}
    return "http://localhost:3000/3be1c6e0-99c9-46f0-be67-7dbde65681e1/function-editor?funcID=0884eb3c-2315-45f3-8c06-a50e42de38e9"