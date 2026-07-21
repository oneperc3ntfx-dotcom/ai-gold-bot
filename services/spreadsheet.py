import gspread

from oauth2client.service_account import ServiceAccountCredentials


from config.settings import SPREADSHEET_ID



# ==========================
# GOOGLE SHEET CONNECTION
# ==========================


scope = [

    "https://spreadsheets.google.com/feeds",

    "https://www.googleapis.com/auth/drive"

]



creds = ServiceAccountCredentials.from_json_keyfile_name(

    "credentials/google.json",

    scope

)



client = gspread.authorize(
    creds
)



sheet = client.open_by_key(
    SPREADSHEET_ID
).sheet1





# ==========================
# GET ALL MEMBER
# ==========================


def get_members():

    return sheet.get_all_records()




# ==========================
# ADD MEMBER
# ==========================


def add_member(data):


    sheet.append_row([

        data["telegram_id"],

        data["username"],

        data["nama"],

        data["paket"],

        data["harga"],

        data["register"],

        data["expired"],

        data["status"]

    ])
