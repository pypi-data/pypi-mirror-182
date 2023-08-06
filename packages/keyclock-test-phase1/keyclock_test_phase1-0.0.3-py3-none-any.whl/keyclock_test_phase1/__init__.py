import requests


token_url = "https://auth.co4.dev/auth/realms/test/protocol/openid-connect/token"

auth_url = "https://auth.co4.dev/auth/realms/test/protocol/openid-connect/userinfo"

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


    return send_to_server



def authenticate_user(request):
    token = request.headers['Authorization'].split(' ')[1]

    headers_token = {'Content-Type' : 'application/json','Authorization': f'Bearer {token}'}


    auth_user = requests.get(url = auth_url, headers=headers_token)


    if auth_user.status_code == 200:

        user = auth_user.json()

        data={
            'username':user['preferred_username']
        }

        return data
    else:

        data = {
            'Bad Credentials':401
        }

        return data  
    

    



