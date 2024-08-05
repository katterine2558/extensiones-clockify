import pandas as pd
import gspread

def f_readUserAPIKEY(token_path,file_key,sheet_name):

    service = gspread.service_account(token_path)
    workbook = service.open_by_key(file_key)
    sheet = workbook.worksheet(sheet_name)
    email_list = sheet.col_values(2)[1:]
    apiKey_list = sheet.col_values(6)[1:]

    dict_users = {
        "Correo": email_list,
        "APIKEY": apiKey_list
    }

    return dict_users