#By JAM

#source of data = wikipedia

#INSTALLING AND IMPORTING MODULES

try:

    import subprocess

    import sys
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
    
    #installation

    install('requests')
    install('beautifulsoup4')
    import requests
    from bs4 import BeautifulSoup as bs

except:
    print("Module installation error...")

#DATA

class Data:
    def __init__(self):
        self.url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Ghana"

    def get_data(self):
        req = requests.get(self.url).text
        soup = bs(req, "html.parser")
        return soup


#PROCESSED_DATA

class ProccessedData:
    info_descr =  ["Disease-Name: ", "Virus strain: ", "Location: ",
    "First outbreak: ", "City(Ghana): ", "Arrival date: ",
    "Confirmed cases: ", "Active cases: ", "Severe cases: ", "Critical cases: ",
    "Recovered: ", "Deaths: "]

    title = "LIVE COVID-19 UPDATE FOR GHANA"

    def __init__(self, data):
        self.data = data.get_data()

    

    def output(self):
        def text(value):
            return value.text


        arr_info_details = list(map(text,self.data.find_all(class_="infobox-data")))
        
        print(self.title)

        print("*"*len(self.title),"\n")

        for index, value in enumerate(self.info_descr):
            if arr_info_details[index].endswith("[1]"):
                arr_info_details[index] = arr_info_details[index].replace("[1]","")
            
            print(value, arr_info_details[index], "\n")
        
    

data = Data()

results = ProccessedData(data)

results.output()





























