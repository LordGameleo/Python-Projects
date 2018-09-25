import requests,webbrowser

#Query to search
search_query = input("Enter the name of the video you want to search for : ")
search_query = search_query.replace(" ","+")

#Create credentials from Google API Console for Youtube Data API and replace in the below line.
key = {YOUR_YOUTUBE_DATA_API_KEY}

#URL to search through API.
url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q="+ search_query +"&type=video&key=" + key

#Getting response from the API with desired Query
response = requests.get(url)

#Getting JSON from the response to extract data.
json_response = response.json()

#Printing the name of the top match video.
print(json_response['items'][0]['snippet']['title'])

#Extracting data from JSON
song_id = json_response['items'][0]['snippet']['title']

#Placying the video on web browser.
webbrowser.open('https://www.youtube.com/watch?v='+json_response['items'][0]['id']['videoId'])
