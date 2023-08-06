import requests


token_url = "https://auth.co4.dev/auth/realms/test/protocol/openid-connect/token"


headers_data = {'Content-Type': 'application/x-www-form-urlencoded'}

client_id = "test-client"
grant_type = "password"




def get_token(username, password):

    data = {
        'username':username,
        'password':password,
        'grant_type':grant_type,
        'client_id':client_id,
    }

    send_to_server = requests.post(url = token_url, data=data, headers=headers_data)

    print("hey")

    return send_to_server

