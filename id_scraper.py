from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
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
ids=[]

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFD', input_str)
    return ''.join(char for char in nfkd_form if not unicodedata.combining(char))

def get_player_id():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get('https://www.transfermarkt.us')
        print("Opened Transfermarkt website")

        player_test = ["Alan Shearer",
            "Ronaldo",
            "Predrag Mijatović",
            "Zinedine Zidane"]

        for player in players:
            
            search_box = driver.find_element(By.NAME, 'query')
            search_box.send_keys(Keys.CONTROL + 'a')
            search_box.send_keys(Keys.BACKSPACE)
            search_box.send_keys(player)
            search_box.send_keys(Keys.RETURN)
            print(f"Searching for: {player}")

            wait = WebDriverWait(driver, 10)

            player_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, "/profil/spieler/")]')))
            for link in player_links:
                if remove_accents(link.text)==remove_accents(player):
                    print("Player link found")
                    break
                else:
                    print(f"Incorrect player found, player found: {link.text}")
            player_link = link

            player_url = player_link.get_attribute('href')
            print(player_url)
            player_id = player_url.split('/')[6]
            if player_id:
                ids.append(player_id)
            else:
                id.append(player)


        return ids
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":

    get_player_id()
    