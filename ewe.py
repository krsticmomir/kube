import requests

def download_xml (url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"XML file download and saved as {file_path}")
    else:
        print("Fail to download XML file")

url = "http://api.ewe.rs/share/backend_231/?user=egroup&secretcode=72252"
file_path = "xml_ewe_lager.xml"

download_xml(url,file_path)
print("gotovo, skinut lager")
