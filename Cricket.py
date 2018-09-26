import requests
from bs4 import BeautifulSoup
import time
import platform

#Function which will interact with the ESPN Cricket Server and Ubuntu
def get_data_ubuntu(url):
    try:

        #Getting response from the ESPN Server
        response = requests.get(url)
    except:

        #If the entered URL is not of the required form.
        error_message = "Wrong url or Connection Problem"
        ex ="(example url : http://www.espncricinfo.com/series/8052\
/game/1127668/hampshire-vs-lancashire-specsavers-county-\
championship-division-one-2018)"
        print(error_message + ex)
        url = input("Enter URL from live match report of ESPN Cric : ")
        get_data_ubuntu(url)
        return 0

    #Making BeautifulSoap object of the ESPN web page
    soup = BeautifulSoup(response.text, "html5lib")
    match_description = soup.find_all('meta', attrs={"name": "news_keywords"})[0]['content']
    report_old = soup.find_all('meta', attrs={"name": "title"})[0]['content']

    #Initializing notify2 so that it can be used later on
    notify2.init("Cricket Updates")
    notification = notify2.Notification(match_description, report_old)

    #Delaying after notification
    time.sleep(1)
    print(match_description)
    print(report_old)

    #For continious Updates
    while True:

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html5lib")
        report_new = soup.find_all('meta', attrs={"name": "title"})[0]['content']

        #No notification if no changes and if there is then new notification
        if report_new != report_old:
            notification.update("Match Updates:",report_new)
            notification.show()

            report_old = report_new
        else:
            pass
        time.sleep(5)


#Function which will interact with the ESPN Cricket Server and Windows 10
def get_data_win_10(url):
    try:

        #Getting response from the ESPN Server
        response = requests.get(url)
    except:

        #If the entered URL is not of the required form.
        error_message = "Wrong url or Connection Problem"
        ex ="(example url : http://www.espncricinfo.com/series/8052\
/game/1127668/hampshire-vs-lancashire-specsavers-county-\
championship-division-one-2018)"
        print(error_message + ex)
        url = input("Enter URL from live match report of ESPN Cric : ")
        get_data_win_10(url)
        return 0

    #Making BeautifulSoap object of the ESPN web page
    soup = BeautifulSoup(response.text, "html5lib")
    match_description = soup.find_all('meta', attrs={"name": "news_keywords"})[0]['content']
    report_old = soup.find_all('meta', attrs={"name": "title"})[0]['content']
    #Initial Notification of the match
    toaster = ToastNotifier()
    toaster.show_toast(match_description,
                   report_old,
                   duration=4)
    time.sleep(4)
    print(match_description)
    print(report_old)
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html5lib")
        report_new = soup.find_all('meta', attrs={"name": "title"})[0]['content']
        #No notification if no changes and if there is then new notification
        if report_new != report_old:
            toaster2 = ToastNotifier()
            toaster2.show_toast("Match Updates",
                        report_new,
                        duration=4)
            report_old = report_new
        else:
            pass
        time.sleep(5)




#Asking for URL from ESPN Cricket to start notification of match
url = input("Enter URL from live match report of ESPN Cric : ")

#Different notification plugins for different Operating systems
if platform.system()[:5] == 'Linux':
    import notify2
    get_data_ubuntu(url)
elif platform.system()[:3] == 'Win':
    from win10toast import ToastNotifier
    get_data_win_10(url)
