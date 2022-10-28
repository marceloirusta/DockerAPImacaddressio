import requests
import os

apikey = os.environ['API_KEY']
def main():
    def get_first_google_result(s):
        r = requests.get(f"https://api.macaddress.io/v1?apiKey={apikey}&output=json&search={s}")
        companyNameResponse = r.json()['vendorDetails']['companyName']
        google_formatted_param = companyNameResponse.replace(" ", "+")
        google_url_search = f"https://www.google.com/search?q={google_formatted_param}&btnI"
        print(f"The company name associated with this mac address is: {companyNameResponse}.\nYou can have more info about it by clicking on this link {google_url_search}")
        

    input_mac_address = input('Please insert the mac address you want to query: ')
    get_first_google_result(input_mac_address)

if __name__ == '__main__':
    main()