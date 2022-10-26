# import module
import requests

url = "https://www.geeksforgeeks.org/"


# create a function
# pass the url
def url_ok(url):
    # exception block
    try:

        # pass the url into
        # request.hear
        response = requests.head(url)

        # check the status code
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return e

# driven code
