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


        sheet_id = str(
            member.get(
                "telegram_id",
                ""
            )
        )



        if sheet_id == str(telegram_id):


            user_rows.append(
                member
            )





    # user tidak ditemukan


    if not user_rows:


        return {


            "active": False,


            "expired": None,


            "package": None

        }





    valid_rows = []



    for row in user_rows:


        try:


            expired = datetime.strptime(

                row.get(
                    "expired",
                    ""
                ),

                DATE_FORMAT

            )


            valid_rows.append(

                (
                    expired,

                    row

                )

            )


        except:


            continue





    # jika expired kosong semua


    if not valid_rows:


        return {


            "active": False,


            "expired": None,


            "package": None

        }





    # ambil membership dengan expired paling lama


    latest_date, latest = max(

        valid_rows,

        key=lambda x:x[0]

    )





    now = datetime.now()





    status = str(

        latest.get(
            "status",
            ""
        )

    ).upper()





    if latest_date >= now and status == "ACTIVE":


        return {


            "active": True,


            "expired": latest.get(
                "expired"
            ),


            "package": latest.get(
                "paket"
            ),


            "username": latest.get(
                "username",
                ""
            ),


            "data": latest

        }





    return {


        "active": False,


        "expired": latest.get(
            "expired"
        ),


        "package": latest.get(
            "paket"
        ),


        "data": latest

    }









# ==========================
# GET ACTIVE MEMBERS
# ==========================


def get_active_members():


    members = get_members()



    checked = {}





    for member in members:



        telegram_id = str(

            member.get(
                "telegram_id",
                ""
            )

        )



        if not telegram_id:

            continue





        try:


            expired = datetime.strptime(

                member.get(
                    "expired"
                ),

                DATE_FORMAT

            )


        except:


            continue





        # jika user belum ada
        # simpan


        if telegram_id not in checked:


            checked[telegram_id] = (

                expired,

                member

            )



        else:



            old_expired = checked[telegram_id][0]



            # ambil expired terbaru


            if expired > old_expired:


                checked[telegram_id] = (

                    expired,

                    member

                )








    result = []



    now = datetime.now()



    for expired, member in checked.values():



        status = str(

            member.get(
                "status",
                ""
            )

        ).upper()



        if expired >= now and status == "ACTIVE":


            result.append(

                member

            )





    return result
