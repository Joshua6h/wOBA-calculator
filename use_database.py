import sqlite3
import parsestats
import linear_weights_constants

def create_league_table(filename):
    """Uses a csv to create a database table with the same name as that csv"""
    try:
        # Making a connection between sqlite3 database and Python Program
        sqliteConnection = sqlite3.connect('baseball_data.db')
        print("Creating league table")

        cursor_obj = sqliteConnection.cursor()
        cursor_obj.execute(f"DROP TABLE IF EXISTS {filename}")

        table = f"""
        CREATE TABLE {filename} (
        id INT PRIMARY KEY NOT NULL,
        name VARCHAR(255) NOT NULL,
        at_bats INT NOT NULL,
        singles INT NOT NULL,
        doubles INT NOT NULL,
        triples INT NOT NULL,
        hrs INT NOT NULL,
        walks INT NOT NULL,
        RAA REAL,
        wOBA REAL
        );
        """
        cursor_obj.execute(table)
        
        players = parsestats.parse_data(filename + '.csv')
        i = 0
        for player in players:
            insert = f"""
            INSERT INTO rock_2022 (id,name,at_bats,singles,doubles,triples,hrs,walks)
            VALUES ({i}, "{player.name}", {player.at_bats}, {player.singles}, {player.doubles}, {player.triples},
                        {player.home_runs}, {player.walks});
            """

            cursor_obj.execute(insert)
            i += 1
        

        sqliteConnection.commit()

    except sqlite3.Error as error:
        print("Failed to create league table", error)
    finally:
        # Inside Finally Block, If connection is open, we need to close it
        if sqliteConnection:
            # using close() method, we will close the connection
            sqliteConnection.close()


def select_top_5_players(table_name):
        """Helper function to view top five players of a table"""
        sqliteConnection = sqlite3.connect('baseball_data.db')

        cursor_obj = sqliteConnection.cursor()

        select_string = f"""
        SELECT * FROM {table_name}
        """
        cursor_obj.execute(select_string)
        output = cursor_obj.fetchall()
        print(output[0][2])

        if sqliteConnection:
            sqliteConnection.close()


def get_league_stats(table_name):
        """Creates a season environment using all the players in a given table"""
        # Making a connection between sqlite3 database and Python Program
        sqliteConnection = sqlite3.connect('baseball_data.db')
        # If sqlite3 makes a connection with python program then it will print "Connected to SQLite"
        # Otherwise it will show errors
        print("Getting league wide stats")

        cursor_obj = sqliteConnection.cursor()

        select_string = f"""
        SELECT SUM(at_bats), SUM(singles), SUM(doubles), SUM(triples), SUM(hrs), SUM(walks) from {table_name}
        """
        cursor_obj.execute(select_string)

        output = cursor_obj.fetchall()
        probabilities = linear_weights_constants.create_season(output[0][0], output[0][1], output[0][2], output[0][3], output[0][4], output[0][5])

        if sqliteConnection:
            sqliteConnection.close()

        return probabilities


def get_all_players(table_name):
        """Returns player objects for all players in a database"""
        sqliteConnection = sqlite3.connect('baseball_data.db')
        print("Getting players from the database")

        cursor_obj = sqliteConnection.cursor()

        select_string = f"""
        SELECT id, name, at_bats, singles, doubles, triples, hrs, walks, RAA, wOBA from {table_name}
        """
        cursor_obj.execute(select_string)

        output = cursor_obj.fetchall()
        
        players = []

        for row in output:
            player = parsestats.Player(row[1], row[2], row[3] + row[4] + row[5] + row[6], row[4], row[5], row[6], row[7], 0, RAA=row[8], wOBA=row[9], id = row[0])
            players.append(player)


        if sqliteConnection:
            sqliteConnection.close()

        return players
    

if __name__ == "__main__":
    create_league_table("rock_2022")
    select_top_5_players("rock_2022")
    probabilities = get_league_stats("rock_2022")
    print(probabilities)
    players = get_all_players("rock_2022")
    for player in players:
         print(player)
    # name = name.replace("'", "\'")
    # dbeaver community