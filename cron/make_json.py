#!/usr/local/bin/python
# -*- coding: utf-8 -*-

# Description:
#   Make json of 'CNS Printer Status'.
#
# Format:
#   {
#       "date": "Date written in CNS Printer Status mail"
#       "status": [
#           [
#               [ "X%", "Y%", "Z%"],
#               ...
#           ]
#   }
#
# Crontab:
#    */10 * * * * /usr/local/bin/python /home/#{your_login_name}/src/make_json.py

import json
import re
import codecs

# regular expression
r_date = re.compile('\[.*\]')

login_name = '#{your_login_name}'

path_mail = '/home/' + login_name + '/src/mails.txt'
path_log  = '/home/' + login_name + '/src/log.txt'

mails_txt = codecs.open(path_mail, 'r', 'shift-jis').read()

# Date
d = r_date.search(mails_txt)
date = u'{0}年{1}月{2}日 {3}'.format(d[1:5], d[6:8], d[9:11], d[11:-1])

# Printer Status
tmp = []
for l in mails.txt.split('\n')[3:]:
    tmp.append(map(lambda x: x.decode('utf-8'),l.split()[2:5]))

status = [
        tmp[10],tmp[13],tmp[14],tmp[12],
        tmp[11],tmp[8], tmp[9], tmp[7],
        tmp[4], tmp[3], tmp[2], tmp[1],
        tmp[0], tmp[5], tmp[6]
        ]

# make associative array for json
j = {'date': date, 'status': status}

# write to mail.json
f = codecs.open('/home/' + login_name + '/public_html/mail.json', 'w', 'utf-8')
f.write(json.dumps(j, indent=4, ensure_ascii=False))
f.close()

# write to log.txt
log = open(path_log, 'a+')
log.write(date.encode('utf-8') + '\n')
log.close()
