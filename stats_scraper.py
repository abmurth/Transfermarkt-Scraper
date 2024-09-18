from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import unicodedata

players = [
            "Lothar Matthäus",
            "Salvatore Schillaci",
            "Andreas Brehme",
            "Jean-Pierre Papin",
            "Darko Pančev",
            "Lothar Matthäus",
            "Marco van Basten",
            "Hristo Stoichkov",
            "Dennis Bergkamp",
            "Roberto Baggio",
            "Dennis Bergkamp",
            "Eric Cantona",
            "Hristo Stoichkov",
            "Roberto Baggio",
            "Paolo Maldini",
            "George Weah",
            "Jürgen Klinsmann",
            "Jari Litmanen",
            "Matthias Sammer",
            "Ronaldo",
            "Alan Shearer",
            "Ronaldo",
            "Predrag Mijatović",
            "Zinedine Zidane",
            "Zinedine Zidane",
            "Davor Šuker",
            "Ronaldo",
            "Rivaldo",
            "David Beckham",
            "Andriy Shevchenko",
            "Luís Figo",
            "Zinedine Zidane",
            "Andriy Shevchenko",
            "Michael Owen",
            "Raúl",
            "Oliver Kahn",
            "Ronaldo",
            "Roberto Carlos",
            "Oliver Kahn",
            "Pavel Nedvěd",
            "Thierry Henry",
            "Paolo Maldini",
            "Andriy Shevchenko",
            "DECO",
            "Ronaldinho",
            "Ronaldinho",
            "Frank Lampard",
            "Steven Gerrard",
            "Fabio Cannavaro",
            "Gianluigi Buffon",
            "Thierry Henry",
            "Kaká",
            "Cristiano Ronaldo",
            "Lionel Messi",
            "Cristiano Ronaldo",
            "Lionel Messi",
            "Fernando Torres",
            "Lionel Messi",
            "Cristiano Ronaldo",
            "Xavi",
            "Lionel Messi",
            "Andres Iniesta",
            "Xavi",
            "Lionel Messi",
            "Cristiano Ronaldo",
            "Xavi",
            "Lionel Messi",
            "Cristiano Ronaldo",
            "Andres Iniesta",
            "Cristiano Ronaldo",
            "Lionel Messi",
            "Franck Ribery",
            "Cristiano Ronaldo",
            "Lionel Messi",
            "Manuel Neuer",
            "Lionel Messi",
            "Cristiano Ronaldo",
            "Neymar",
            "Cristiano Ronaldo",
            "Lionel Messi",
            "Antoine Griezmann",
            "Cristiano Ronaldo",
            "Lionel Messi",
            "Neymar",
            "Luka Modrić",
            "Cristiano Ronaldo",
            "Antoine Griezmann",
            "Lionel Messi",
            "Virgil van Dijk",
            "Cristiano Ronaldo"
]
ids = [
    "1527",
    "90513",
    "16056",
    "17168",
    "100098",
    "1527",
    "74471",
    "7938",
    "3187",
    "4153",
    "3187",
    "12000",
    "7938",
    "4153",
    "5803",
    "8542",
    "16980",
    "4675",
    "77010",
    "3140",
    "3110",
    "3140",
    "24481",
    "3111",
    "3111",
    "1407",
    "3140",
    "3372",
    "3139",
    "3522",
    "3446",
    "3111",
    "3522",
    "1397",
    "7349",
    "206",
    "3140",
    "7518",
    "206",
    "3603",
    "3207",
    "5803",
    "3522",
    "8564",
    "3373",
    "3373",
    "3163",
    "3109",
    "5775",
    "5023",
    "3207",
    "3366",
    "8198",
    "28003",
    "8198",
    "28003",
    "7767",
    "28003",
    "8198",
    "7607",
    "28003",
    "7600",
    "7607",
    "28003",
    "8198",
    "7607",
    "28003",
    "8198",
    "7600",
    "8198",
    "28003",
    "22068",
    "8198",
    "28003",
    "17259",
    "28003",
    "8198",
    "68290",
    "8198",
    "28003",
    "125781",
    "8198",
    "28003",
    "68290",
    "27992",
    "8198",
    "125781",
    "28003",
    "139208",
    "8198"
]
years = ['1989',
 '1989',
 '1989',
 '1990',
 '1990',
 '1990',
 '1991',
 '1991',
 '1991',
 '1992',
 '1992',
 '1992',
 '1993',
 '1993',
 '1993',
 '1994',
 '1994',
 '1994',
 '1995',
 '1995',
 '1995',
 '1996',
 '1996',
 '1996',
 '1997',
 '1997',
 '1997',
 '1998',
 '1998',
 '1998',
 '1999',
 '1999',
 '1999',
 '2000',
 '2000',
 '2000',
 '2001',
 '2001',
 '2001',
 '2002',
 '2002',
 '2002',
 '2003',
 '2003',
 '2003',
 '2004',
 '2004',
 '2004',
 '2005',
 '2005',
 '2005',
 '2006',
 '2006',
 '2006',
 '2007',
 '2007',
 '2007',
 '2008',
 '2008',
 '2008',
 '2009',
 '2009',
 '2009',
 '2010',
 '2010',
 '2010',
 '2011',
 '2011',
 '2011',
 '2012',
 '2012',
 '2012',
 '2013',
 '2013',
 '2013',
 '2014',
 '2014',
 '2014',
 '2015',
 '2015',
 '2015',
 '2016',
 '2016',
 '2016',
 '2017',
 '2017',
 '2017',
 '2018',
 '2018',
 '2018']

players_test = ["Lothar Matthäus",
    "Salvatore Schillaci",
    "Andreas Brehme",
    "Jean-Pierre Papin"]
ids_test = ['1527', '90513', '16056', '17168']
years_test= ["1989", "1989", "1989", "1990"]

appearances = []
goals = []
assists = []
yellows = []
red = []
minutes = []

def get_player_stats():

    
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)

    try:

        for index, player in enumerate(players):
            stats = []
            driver.get(f'https://www.transfermarkt.us/player/leistungsdaten/spieler/{ids[index]}/saison/{years[index]}')
            print("Opened Transfermarkt website")
            
          
            wait = WebDriverWait(driver, 20)
            print("Waiting for the tfoot element")

           
            tfoot = wait.until(EC.presence_of_element_located((By.TAG_NAME, "tfoot")))
            print("Got tfoot element")

            
            td_elements = tfoot.find_elements(By.TAG_NAME, "td")
   

            
            for i, td_e in enumerate(td_elements):
                stats.append(driver.execute_script("return arguments[0].innerText;", td_e))


            appearances.append(stats[2])
            goals.append(stats[3])
            assists.append(stats[4])
            yellows.append(stats[5])
            red.append(stats[7])
            minutes.append(stats[8])
            print(f"{index}: {player}")

            




    
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        print("Closing the browser")
        print(f"players: {players}")
        print(f"apearances: {appearances}")
        print(f"goals: {goals}")
        print(f"assists: {assists}")
        print(f"yellows: {yellows}")
        print(f"reds: {red}")
        print(f"mins: {minutes}")
        driver.quit()





if __name__ == "__main__":
    get_player_stats()

    