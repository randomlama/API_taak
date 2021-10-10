import requests
from tabulate import tabulate

#voeg hier uw client ID en Secret in
client_id = 'xxxx'
client_secret = 'xxxx'

#Client credentials flow
auth_url = 'https://accounts.spotify.com/api/token'
data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}
auth_response = requests.post(auth_url, data=data)
access_token = auth_response.json().get('access_token')

#basis van de api call URL en headers met bearertoken uit client credentials flow
base_url = 'https://api.spotify.com/v1/search?'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

#opvragen artiest
artist_in = input("Geef naam van artiest: ")
#samenstellen API call URL en API call
request = base_url + 'q=' + artist_in + '=&type=artist'
response = requests.get(request,headers=headers)
json_resp = response.json()

#verwerking response
count = 0
output = []
for item in json_resp['artists']['items']:
    
    name =  json_resp['artists']['items'][count]['name']
    genres = json_resp['artists']['items'][count]['genres']
    popularity = json_resp['artists']['items'][count]['popularity']
    artist = [name, genres, popularity]
    output.insert(count, artist)
    count+=1

#tabuleren en printen van resultaat
print (tabulate(output, headers=["Name", "Genres", "popularity"]))
