from datetime import datetime, time
import pytz


TIMEZONE = pytz.timezone(
    "Asia/Jakarta"
)


# ==========================
# TRADING SESSION
# ==========================

START_DAY = 0       # Senin
END_DAY = 5         # Sabtu


START_TIME = time(
    6, 55
)                   # 06:55 WIB


END_TIME = time(
    2, 15
)                   # 02:15 WIB





def trading_open():


    now = datetime.now(
        TIMEZONE
    )


    day = now.weekday()

    current_time = now.time()



    print(
        "CHECK MARKET:",
        now
    )



    # ======================
    # MINGGU OFF
    # ======================

    if day == 6:

        return False



    # ======================
    # SENIN SEBELUM 06:55
    # ======================

    if day == 0 and current_time < START_TIME:

        return False



    # ======================
    # SABTU SETELAH 02:15
    # ======================

    if day == 5 and current_time > END_TIME:

        return False



    return True
