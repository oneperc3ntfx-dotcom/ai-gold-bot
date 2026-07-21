import json

import os

from datetime import datetime



FILE = "database/cache.json"





def load_cache():


    if not os.path.exists(FILE):


        return {

            "date": "",

            "signal": 0

        }



    with open(FILE,"r") as f:

        return json.load(f)







def save_cache(data):


    with open(FILE,"w") as f:


        json.dump(
            data,
            f,
            indent=4
        )







# ==========================
# SIGNAL NUMBER
# ==========================


def get_signal_number():


    data = load_cache()



    today = datetime.now().strftime(
        "%Y-%m-%d"
    )



    if data["date"] != today:


        data = {

            "date":today,

            "signal":1

        }


        save_cache(data)



        return 1




    return data["signal"]







def increase_signal_number():


    data = load_cache()



    today = datetime.now().strftime(
        "%Y-%m-%d"
    )



    if data["date"] != today:


        data = {

            "date":today,

            "signal":2

        }



    else:


        data["signal"] += 1




    save_cache(data)
