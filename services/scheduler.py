from datetime import datetime, time


import pytz



from config.constants import (
    START_DAY,
    END_DAY,
    START_TIME,
    END_TIME
)



TIMEZONE = pytz.timezone(
    "Asia/Jakarta"
)





# ==========================
# CHECK TRADING SESSION
# ==========================


def trading_open():


    now = datetime.now(
        TIMEZONE
    )



    day = now.weekday()


    current_time = now.time()





    # Minggu OFF

    if day == 6:

        return False





    # Senin sebelum jam 7

    if day == 0 and current_time < START_TIME:

        return False





    # Sabtu setelah jam 02

    if day == 5 and current_time > END_TIME:

        return False





    return True
