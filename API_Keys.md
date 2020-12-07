# Twitch API Keys and Usage

## Access Token
```
> import requests
> url = 'https://id.twitch.tv/oauth2/token'
> data = {
    'client_id' : [client id here],
    'client_secret' : [client secret here],
    'grant_type' : 'client_credentials'
}
> r = requests.post(url=url, data=data)
> r.json()
```
##### Access token will be 0th argument given in JSON response. Additionally, the response gives the time, in seconds, that token will expire, which is about 2 months.

# API Call Examples

## Get Streams (General)
```
> import requests
> url = 'https://api.twitch.tv/helix/streams'
> headers = {
    'Client-ID' : [client id here],
    'Authorization' : 'Bearer [access token here]'
}
> r = requests.get(url=url, headers=headers)
> r.json()
```

## Get Streams (Specific User via Username)

### GET Request
```
> import requests
> url = 'https://api.twitch.tv/helix/streams?user_login=[Twitch username here]'
> headers = {
    'Client-ID' : [client id here],
    'Authorization' : 'Bearer [access token here]'
}
> r = requests.get(url=url, headers=headers)
> r.json()
```

### Output Response (if live)
```
{'data': [{'game_id': '509538',
           'id': [~19 digit number string],
           'language': 'en',
           'started_at': '2020-08-10T00:10:19Z',
           'tag_ids': ['6ea6bca4-4712-4ab9-a906-e3336a9d8039'],
           'thumbnail_url': [thumbnail url here],
           'title': [Stream Title Here],
           'type': 'live',
           'user_id': [8 Digit Number String],
           'user_name': [Twitch username],
           'viewer_count': [Int viewer count]}],
 'pagination': {}}
```
##### Some data has been ommited. 
##### Game ID listed is for *Animal Crossing: New Horizons*
##### Format of ```started_at``` variable is ```YYYY-MM-DDTHH:MM:SSZ``` where ```T``` and ```Z``` Don't mean anything.

### Output Response (if not live)
```
{'data': [], 'pagination': {}}
```

## Verify User Exists

### GET Request
```
> import requests
> url = 'https://api.twitch.tv/helix/users?login=[Twitch username here]'
> headers = {
    'Client-ID' : [client id here],
    'Authorization' : 'Bearer [access token here]'
}
> r = requests.get(url=url, headers=headers)
> r.json()
```

### GET Response 200
```
{'data': [{'broadcaster_type': '',
           'description': '',
           'display_name': [Username here],
           'id': [User id here],
           'login': [Username here],
           'offline_image_url': '',
           'profile_image_url': 'https://static-cdn.jtvnw.net/user-default-pictures-uv/de130ab0-def7-11e9-b668-784f43822e80-profile_image-300x300.png',
           'type': '',
           'view_count': 1}]}
```
##### broadcaster_type is either *"partner"*, *"affiliate*", or empty.
##### I'm not sure if display_name and login are the same, always
##### Corresponding docs can be found [here](https://dev.twitch.tv/docs/api/reference#get-users).

### GET Response 400
```
> {'error': 'Bad Request',
 'message': 'Must provide an ID, Login or OAuth Token.',
 'status': 400}
 ```

 ## Check User Follows

 ### GET Request
 ```
> import requests
> url = 'https://api.twitch.tv/helix/follows?from_id=[Twitch user id here]'
> headers = {
    'Client-ID' : [client id here],
    'Authorization' : 'Bearer [access token here]'
}
> r = requests.get(url=url, headers=headers)
> r.json()
 ```
 ##### User ID can be obtained by the Verify User Exists request.

### GET Response 200
```
{'data': [{'followed_at': '2020-08-09T22:44:00Z',
           'from_id': [User id here],
           'from_name': [Username here],
           'to_id': [ID of followed user],
           'to_name': [Username of followed user]},
 'pagination': {'cursor': 'eyJiIjpudWxsLCJhIjp7IkN1cnNvciI6IjE1OTY4MzQ5Mzg4MTEyMDQyMTQifX0'},
 'total': 1}
```
##### ```pagnation``` is a cursor value, to be used in a subsequent request to specify the starting point of the next set of results