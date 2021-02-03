#! python3

from save_data import save_data_base
from web_scraping import web_extract

mysql_host = "localhost"
mysql_user = "root"
mysql_password = "alice1999++"
mysql_database = "soccer"
mysql_table = "matches2"

# Columns of the table
id_column_name         = "id_web"
pais_column_name       = "country"
liga_column_name       = "liga"
tiempo_column_name     = "time"
equipo1_column_name    = "team1"
equipo2_column_name    = "team2"
marcador_column_name   = "score"
cuota1_column_name     = "c1"
cuota2_column_name     = "c2"
cuota3_column_name     = "c3"
fecha_column_name      = "date"

# List of countries to make we scrapig
countries = [
    "ARGENTINA",
    "AUSTRALIA",
    "AUSTRIA",
    "BELARUS",
    "BELGIUM",
    "BOLIVIA",
    "BOSNIA AND HERZEGOVINA",
    "BRAZIL",
    "CHILE",
    "CHINA",
    "COLOMBIA",
    "COSTA RICA",
    "CROATIA",
    "CYPRUS",
    "CZECH REPUBLIC",
    "DENMARK",
    "ECUADOR",
    "EGYPT",
    "ENGLAND",
    "FINLAND",
    "FRANCE",
    "GERMANY",
    "GREECE",
    "ICELAND",
    "IRELAND",
    "ISRAEL",
    "ITALY",
    "JAPAN",
    "MEXICO",
    "NETHERLANDS",
    "PARAGUAY",
    "PERU",
    "POLAND",
    "PORTUGAL",
    "RUSSIA",
    "SAUDI ARABIA",
    "SCOTLAND",
    "SERBIA",
    "SPAIN",
    "SWEDEN",
    "SWITZERLAND",
    "TURKEY",
    "UKRAINE",
    "UNITED ARAB EMIRATES",
    "URUGUAY",
    "USA",
    "VENEZUELA",
    "WALES",
    "AFRICA",
    "ASIA",
    "AUSTRALIA & OCEANIA",
    "EUROPE",
    "NORTH & CENTRAL AMERICA",
    "SOUTH AMERICA",
    "WORLD"
]

ligas = [
    "Premier League",
    "Ligue 1",
    "Serie A",
    "Primer Devision"
]


# Make web scraping to the page
data_scraping = web_extract(countries, ligas)

# Save information in data base
save_data_base ( 
    data = data_scraping, 
    host = mysql_host, 
    user = mysql_user, 
    password = mysql_password, 
    database = mysql_database, 
    table = mysql_table, 
    id = id_column_name, 
    pais = pais_column_name, 
    liga = liga_column_name, 
    tiempo = tiempo_column_name, 
    equipo1 = equipo1_column_name, 
    equipo2 = equipo2_column_name, 
    marcador = marcador_column_name, 
    cuota1 = cuota1_column_name, 
    cuota2 = cuota2_column_name, 
    cuota3 = cuota3_column_name,
    fecha = fecha_column_name
    )