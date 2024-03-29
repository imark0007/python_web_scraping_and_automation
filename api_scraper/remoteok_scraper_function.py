import requests
import xlwt
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

BASE_URL = 'https://remoteok.com/api/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
     'Accept-Language': 'en-US, en;q=0.5',
    
}

def get_Job_postings():
    res = requests.get(url=BASE_URL,headers=REQUEST_HEADER)
    return res.json()
clear

def output_jobs_to_xls(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())
    print(headers)
    
    
if __name__ == "__main__":
    json = get_Job_postings()[1:]
    output_jobs_to_xls(json)