import requests
from bs4 import BeautifulSoup

def get_data():
    url = "https://www.iplocation.net/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html5lib")
    ip = soup.find_all('table')[0].find_all('td')[0].text
    country = soup.find_all('table')[0].find_all('td')[1].text
    state = soup.find_all('table')[0].find_all('td')[3].text
    place  = soup.find_all('table')[0].find_all('td')[2].text
    approx_place = state + "," + place

    return ip,country,approx_place

data = get_data()
print("IP :", data[0], "\nCountry :", data[1], "\nApprox Place :", data[2])
