import requests

print("\nRequests version: " + requests.__version__)

get_request = requests.get("https://www.google.com/")
print("\nRetrieving Google Home Page Contents\n", get_request.content)

print("\nRetrieving Python Script...\n")
get_script = requests.get("https://raw.githubusercontent.com/shearpaladin/CMPUT404-LAB1/main/version.py")

print(get_script.text)
