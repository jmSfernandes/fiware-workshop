import requests


def perform_request():
    url = "http://localhost:9000/v2/entities/?options=count,keyValues&orderBy=!timestamp&limit=100"

    headers = {
        'Fiware-Service': 'socialite',
        'Fiware-ServicePath': '/'
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def fiware_test():
    #####
    # Your code here
    ####
    return


# perform_request()
fiware_test()
