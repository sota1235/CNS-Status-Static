#!/usr/bin/python
# -*- coding: utf-8 -*-

# Description:
#   Make json of 'CNS Printer Status'.
#
# Format:
#   {
#       "date": "メールに記載されてる日付"
#       "status": [
#           [
#               [ "X%", "Y%", "Z%"],
#               ...
#           ]
#   }
#
# Crontab:
#   ex)
#       2 * * * * /usr/local/bin/python /home/#{your_login_name}/src/make_json.py
#
# Author:
#   @sota1235

import glob
import json
import codecs
import os.path
import datetime

login_name = '#{your_login_name}'

path_new = '/home/' + login_name + '/Maildir/.CNS.CNS_Printer/new/'
path_cur = '/home/' + login_name + '/Maildir/.CNS.CNS_Printer/cur/'
path_log = '/home/' + login_name + '/src/log.txt'

log_txt = ''

def get_mail(path):
    mail_list = glob.glob(path + '*.*')
    update_time = 0
    mail = ''
    for m in mail_list:
        if update_time < os.path.getatime(m):
            update_time = os.path.getatime(m)
            mail = m
    global log_txt
    log_txt = str(datetime.datetime.today()) + " : " +  mail.replace(path, '')
    return codecs.open(mail, 'r', 'shift-jis').read().split('\n')[28:]

if len(os.listdir(path_new)) != 0:
    mail_txt = get_mail(path_new)
else:
    mail_txt = get_mail(path_cur)

if '[' in mail_txt[0]:
    f_line = mail_txt[0]
    o_line = mail_txt[3:-1]
else:
    f_line = mail_txt[1]
    o_line = mail_txt[4:-1]

d = f_line.replace(' ','').decode('utf-8')
date = u"{0}年{1}月{2}日 {3}".format(d[1:5], d[6:8], d[9:11], d[11:-1])
tmp = []

for l in o_line:
    tmp.append(map(lambda x: x.decode('utf-8'),l.split()[2:5]))

status = [tmp[10],tmp[13],tmp[14],tmp[12],tmp[11],tmp[8],tmp[9],tmp[7],tmp[4],tmp[3],tmp[2],tmp[1],tmp[0],tmp[5],tmp[6]]

j = {'date': date, 'status': status}

# mail.jsonに書き込み
f = codecs.open("/home/" + login_name + "/public_html/mail.json", "w", "utf-8")
f.write(json.dumps(j,indent=4,ensure_ascii=False))
f.close()

log = open(path_log, 'a+')
log.write(date.encode('utf-8'))
log.write(' : ' + log_txt + '\n')
log.close()
