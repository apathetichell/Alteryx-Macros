#################################
# List all non-standard packages to be imported by your 
# script here (only missing packages will be installed)
from ayx import Package
Package.installPackages(['pandas','gspread','google-auth-oauthlib','google-auth','google-auth-httplib2'])


#################################
import gspread
from ayx import Alteryx
from google.oauth2 import service_account

datastream1 = Alteryx.read("#1")

jwt_path= datastream1.iloc[0,0]

ghseetfile= datastream1.iloc[0,1]

print(f'the path value is {jwt_path} and the sheet value is {ghseetfile}')


keyfile_path = jwt_path

credentials = service_account.Credentials.from_service_account_file(
    keyfile_path,
    scopes=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
)

gc=gspread.authorize(credentials)

sheet=gc.open_by_url(ghseetfile)

worksheet = sheet.get_worksheet(0)



#################################
datastream2 = Alteryx.read("#2")

row_i = 1

col_index = 65

for col in datastream2.columns:
    worksheet.update(chr(col_index)+'1',col)
    col_index +=1


while row_i <= datastream2.shape[0]:
    col_i =1
    while col_i <=datastream2.shape[1]:
        cell_value = str(datastream2.iloc[row_i-1][col_i-1])
        row_location = str(row_i+1)
        col_location = chr(64+col_i)
        worksheet.update(col_location+row_location,cell_value)
        col_i = col_i+1
    row_i +=1





#################################



#################################
