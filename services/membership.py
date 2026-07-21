from datetime import datetime


from services.spreadsheet import get_members





DATE_FORMAT = "%d-%m-%Y"





# ==========================
# CHECK MEMBER
# ==========================


def check_member(
    telegram_id
):


    members = get_members()



    user_rows = []



    for member in members:


        if str(member["Telegram ID"]) == str(telegram_id):


            user_rows.append(
                member
            )



    if not user_rows:


        return {


            "active": False,


            "expired": None,


            "package": None

        }





    # Ambil expired terbaru


    latest = max(

        user_rows,


        key=lambda x:


        datetime.strptime(

            x["Expired"],

            DATE_FORMAT

        )

    )





    expired_date = datetime.strptime(

        latest["Expired"],

        DATE_FORMAT

    )





    now = datetime.now()





    if expired_date >= now:


        return {


            "active": True,


            "expired":

                latest["Expired"],


            "package":

                latest["Paket"],


            "username":

                latest["Username"]


        }





    return {


        "active": False,


        "expired":

            latest["Expired"],


        "package":

            latest["Paket"]

    }







# ==========================
# GET ACTIVE MEMBERS
# ==========================


def get_active_members():


    members = get_members()


    result = []



    checked = {}



    for member in members:


        telegram_id = str(
            member["Telegram ID"]
        )



        expired = datetime.strptime(

            member["Expired"],

            DATE_FORMAT

        )



        # simpan expired terbesar

        if telegram_id not in checked:


            checked[telegram_id] = member



        else:


            old = datetime.strptime(

                checked[telegram_id]["Expired"],

                DATE_FORMAT

            )


            if expired > old:


                checked[telegram_id] = member






    for user in checked.values():


        expired = datetime.strptime(

            user["Expired"],

            DATE_FORMAT

        )



        if expired >= datetime.now():


            result.append(

                user

            )



    return result
