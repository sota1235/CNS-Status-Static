#!/usr/local/bin/python
# -*- cofing: utf-8 -*-

# Description:
#   Filtering for 'CNS Printer Status' mail to
#   the exclusive folder you made.
#
# Crontab:
#   ex)
#       */10 * * * * /usr/local/bin/python /home/#{your_login_name}/src/move_mail.py /home/{login_name}/Maildir/cur
#       */10 * * * * /usr/local/bin/python /home/#{your_login_name}/src/move_mail.py /home/{login_name}/Maildir/new
#
# Author:
#   @sota1235

import os
import shutil
import sys

login_name = '#{your_login_name}'
path = sys.argv[1]
path_cps = '/home/' + login_name + '/Maildir/.CNS.CNS_Printer/new/'
From = 'yuoka@sfc.keio.ac.jp'

# exit if nothing in new mail box
if len(os.listdir(path)) == 0: exit()

for mail in os.listdir(path)[-100:]:
    f = open(path + mail, 'r')
    if From in f.read().split('\n')[0]:
        shutil.move(path + mail, path_cps)
