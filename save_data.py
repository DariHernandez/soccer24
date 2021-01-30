#! python3

import pymysql.cursors, time, pprint

def save_data_base (data, host, user, password, database, table, id, pais, liga, tiempo, equipo1, equipo2, marcador, cuota1, cuota2, cuota3): 
    """
    save the information in the MYSQl data base
    """

    # Connect to the database
    connection = pymysql.connect(host = host,
                                user = user,
                                password = password,
                                database = database,
                                cursorclass = pymysql.cursors.DictCursor)


    print ("Updating data base...")

    # Make conextion to sata base
    with connection:
        with connection.cursor() as cursor:

            # loop for row value in the data
            for row in data: 

                # Values to insert in the data base
                id_value       = row["id"]
                time_value     = row["tiempo/hora"]
                team1_value    = row["equipo 1"]
                team2_value    = row["equipo 2"]
                score_value    = row["marcador"]
                c1_value       = row["cuota 1"]
                c2_value       = row["cuota 2"]
                c3_value       = row["cuota 3"]
                country_value  = row["pais"]
                liga_value     = row["liga"]

                # Seach the current row in the data base
                sql = "SELECT * FROM `{}` WHERE `{}`='{}';".format(table, id, id_value)
                cursor.execute(sql)
                
                # Verify if register already exist in the data base
                if cursor.fetchall(): 

                    # update register
                    sql = "UPDATE `{}` SET `{}` = '{}', `{}` = '{}', `{}` = '{}', `{}` = '{}', `{}` = '{}', `{}` = '{}', `{}` = '{}', `{}` = '{}', `{}` = '{}', `{}` = '{}' WHERE `{}` = '{}';".format (table, id, id_value, pais, country_value, liga, liga_value, tiempo, time_value, equipo1, team1_value, equipo2, team2_value, marcador, score_value, cuota1, c1_value, cuota2, c2_value, cuota3, c3_value, id, id_value)

                    cursor.execute(sql)

                    connection.commit()
                
                else: 
                    
                    # Insert register
                    sql = "INSERT INTO `{}` (`{}`, `{}`, `{}`, `{}`, `{}`, `{}`, `{}`, `{}`, `{}`, `{}`) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format (table, id, pais, liga, tiempo, equipo1, equipo2, marcador, cuota1, cuota2, cuota3, id_value, country_value, liga_value, time_value, team1_value, team2_value, score_value, c1_value, c2_value, c3_value)

                    cursor.execute(sql)
        
                    connection.commit()

    print ("Done")