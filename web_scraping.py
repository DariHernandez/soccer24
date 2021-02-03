#! python3

import time as t
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def web_extract (list_countries, list_ligas): 
    """ 
    Main function for web scraping. Extract information from the web page https://www.soccer24.com/
    """

    print ("Running web scraping...")

    # List of all data from web scraping
    return_data = []
    
    web_page = "https://www.soccer24.com/"

    # OIpen page with chrome
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get (web_page)

    # Loop for wait the page to load
    while True: 

        # Save all rows of the table 
        selector = "#live-table > div.event > div > div > div"
        rows = browser.find_elements_by_css_selector (selector)
        
        if rows: 
            # Re-select rows
            t.sleep (3)
            rows = browser.find_elements_by_css_selector (selector)
            break

    #  Accept cokies
    selector = "#onetrust-accept-btn-handler"
    accept_button = browser.find_element_by_css_selector (selector)
    accept_button.click()   


    # Variables to save the current country and liga
    country = ""
    liga = ""

    # Loop for each row
    for index_row in range (1, len(rows)+1):

        # Dictionary to save the information of the event
        data_row = {}

        # Try to get the header row of events. 
        # If error happend, the current row is an event
        try: 

            # Save the header information of the events
            selector_country = "#live-table > div.event > div > div > div:nth-child({}) div.icon--flag div span:nth-child(1)".format (index_row)
            selector_liga = "#live-table > div.event > div > div > div:nth-child({}) div.icon--flag div span:nth-child(2)".format (index_row)

            country = browser.find_element_by_css_selector (selector_country).text
            liga = browser.find_element_by_css_selector (selector_liga).text

            # Filter countries to showe message
            if str(country).strip().upper() in list_countries and str(liga).strip() in list_ligas:  
                print ("Scraping events from {}, {}...".format (country, liga))
            else: 
                print ("Skipping row...")


        # Get the information of the events
        except: 

            # Filter countries to skip
            if not str(country).strip().upper() in list_countries:  
                continue

            if not str(liga).strip() in list_ligas:  
                continue


            id = ""
            time = ""
            team1 = ""
            team2 = ""
            score = ""
            c1 = ""
            c2 = ""
            c3 = ""            

            # Get the coutes
            selector_c1 = "#live-table > div.event > div > div > div:nth-child({}) div:nth-child(6)".format (index_row)
            selector_c2 = "#live-table > div.event > div > div > div:nth-child({}) div:nth-child(7)".format (index_row)
            selector_c3 = "#live-table > div.event > div > div > div:nth-child({}) div:nth-child(8)".format (index_row)
            c1 = browser.find_element_by_css_selector (selector_c1).text   
            c2 = browser.find_element_by_css_selector (selector_c2).text   
            c3 = browser.find_element_by_css_selector (selector_c3).text  

            # Skip matches without cuotes
            if c1.strip() == "-" or c2.strip() == "-" or c3.strip() == "-": 
                continue


            # Get the id
            id = rows[index_row-1].get_attribute ("id")            


            # Get the time
            # Try to get the time or the status of the event
            try: 
                selector_time = "#live-table > div.event > div > div > div:nth-child({}) div.event__time".format (index_row)
                time = browser.find_element_by_css_selector (selector_time).text
            except: 
                selector_time = "#live-table > div.event > div > div > div:nth-child({}) div.event__stage > div".format (index_row)
                time = browser.find_element_by_css_selector (selector_time).text
            
            # Delete extra text in time
            if "fro" in str(time).lower(): 
                time = str(time).lower().strip().replace("fro", "").replace("\n", "")


            # Get teams
            selector_team1 = "#live-table > div.event > div > div > div:nth-child({}) div:nth-child(3)".format (index_row)
            selector_team2 = "#live-table > div.event > div > div > div:nth-child({}) div:nth-child(4)".format (index_row)
            team1 = browser.find_element_by_css_selector (selector_team1).text
            team2 = browser.find_element_by_css_selector (selector_team2).text

            # Remove quotes in teams names
            team1 = str(team1).replace ("\'", " ")
            team2 = str(team2).replace ("\'", " ")


            # Get the match of the event
            selector_score = "#live-table > div.event > div > div > div:nth-child({}) div:nth-child(5)".format (index_row)
            score = browser.find_element_by_css_selector (selector_score).text

            # delete extra text in score
            score = str(score).lower().strip().replace("\n", "")
            
            # Replace empty scores
            if not score or score.strip() == "-": 
                score = "none"
 

            # Delate quotes in country and liga
            country = str(country).replace ("\'", " ")
            liga = str(liga).replace ("\'", " ")

            # Save data in dictionary of row
            data_row["id"] = id
            data_row["tiempo/hora"] = time
            data_row["equipo 1"] = team1
            data_row["equipo 2"] = team2
            data_row["marcador"] = score
            data_row["cuota 1"] = c1
            data_row["cuota 2"] = c2
            data_row["cuota 3"] = c3 
            data_row["pais"] = country
            data_row["liga"] = liga

            # Get date and time of the match


            # Save the current data to return list
            return_data.append (data_row)    

    return return_data