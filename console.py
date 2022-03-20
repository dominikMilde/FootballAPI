import os.path
from datetime import datetime

import requests

BASE = "http://127.0.0.1:5000/"

print("Welcome to Football API")
user_in = input(
    'Type "all" if you want to fetch list of all players or type player id to fetch data for one player. \n')

try:
    # ------- ALL PLAYERS ------- #
    if user_in.lower() == "all":
        response = requests.get(BASE + user_in.lower())
        f = open('logs/all_players.txt', 'a+')
        if os.stat("logs/all_players.txt").st_size == 0:  # if file empty
            # print("prazna")
            for record in response.json():
                f.write(str(record) + "\n")
            f.write("Data fetched: " + str(datetime.now()) + "\n")
            f.write("-------------------------------------- \n")
        else:
            last_modified_file_ms = os.path.getmtime('logs/all_players.txt')
            last_modified_file_datetime = datetime.fromtimestamp(last_modified_file_ms)
            change = False
            for record in response.json():
                # print(record['last_modified'])
                # probably would be faster if database filtered by datetime, but api controller would be more complicated
                if datetime.strptime(record['last_modified'], "%Y-%m-%dT%H:%M:%S.%f") > last_modified_file_datetime:
                    f.write(str(record) + "\n")
                    change = True
            if change:
                f.write("Data fetched: " + str(datetime.now()) + "\n")
                f.write("-------------------------------------- \n")
        f.close()

    else:
        # ------- CATCH WRONG INPUTS ------- #
        try:
            id_player = int(user_in)
        except ValueError as e:
            print("ILLEGAL INPUT - input 'all' or player id")
            exit(0)

        # ------- FETCH ONE PLAYER ------- #
        response = requests.get(BASE + str(id_player))
        if response.status_code == 404:
            print("Player with id=" + str(id_player) + " doesn't exist.")
            exit(0)

        f = open('logs/player' + str(id_player) + '.txt', 'a+')
        if os.stat('logs/player' + str(id_player) + '.txt').st_size == 0:  # if file empty
            # print("prazna")
            f.write(str(response.json()) + "\n")
            f.write("Data fetched: " + str(datetime.now()) + "\n")
            f.write("-------------------------------------- \n")
        else:
            last_modified_file_ms = os.path.getmtime('logs/player' + str(id_player) + '.txt')
            last_modified_file_datetime = datetime.fromtimestamp(last_modified_file_ms)
            if datetime.strptime(response.json()['last_modified'], "%Y-%m-%dT%H:%M:%S.%f") > last_modified_file_datetime:
                f.write(str(response.json()) + "\n")
                f.write("Data fetched: " + str(datetime.now()) + "\n")
                f.write("-------------------------------------- \n")
        f.close()

except Exception as e:
    print("Something went wrong, maybe server is not live!")
    exit(1)