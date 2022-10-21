
import gspread
import argparse
import datetime
import sys
import os
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

NOW_DATETIME = datetime.datetime.now()

CUR_MONTH = NOW_DATETIME.strftime('%B')
CUR_DAY = NOW_DATETIME.strftime('%A')
IS_HOLIDAY = True if CUR_DAY == 'Sunday' or CUR_DAY == 'Saturday' else False
CUR_DATE = "%s %s" % (NOW_DATETIME.day, CUR_MONTH)
CUR_TIME = NOW_DATETIME.strftime('%I:%M %p')

CREDS_LOC = "/Users/zubairsoomro/python-workspace/attendance_marker/creds.json"

SHEET_NAME = 'Work From Home attendance Sheet'

EMPLOYEE_NAME = ''

parser = argparse.ArgumentParser(
    'Change name by editing the script or change it by the argument')

parser.add_argument(
    '-n', '--name', help='Provide the name as it is written on the google sheet')

parser.add_argument('-o', '--override',
                    help='To mark attendance even when its a holiday')

args = parser.parse_args()

if args.name:
    EMPLOYEE_NAME = args.name


def connect_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_LOC, scope)

    client = gspread.authorize(creds)

    try:
        sheet = client.open(SHEET_NAME)
    except gspread.SpreadsheetNotFound:
        print('Sheet not found, or you don\'t have the permission to the sheet.')

    worksheet = sheet.worksheet(CUR_MONTH)

    name_cell = worksheet.find(EMPLOYEE_NAME)

    date_Cell = worksheet.find(CUR_DATE)

    cur_cell = worksheet.cell(name_cell.row, date_Cell.col)

    if cur_cell.value != '':

        updated_value = cur_cell.value + ' '+CUR_TIME

        worksheet.update_cell(cur_cell.row, cur_cell.col, updated_value)

    else:

        worksheet.update_cell(cur_cell.row, cur_cell.col, CUR_TIME + ' - ')


    # row = worksheet.row_values(3)
if __name__ == '__main__':
    if not IS_HOLIDAY or args.override:
        if EMPLOYEE_NAME != '':
            connect_sheet()
        else:
            print("Please provide a name as it is mentioned in the sheets.")
    else:
        print('Its holiday today, if you are still working pass argument -o or --override to mark your attendance')