#!/bin/sh

echo "Install start"

echo "Make 'src' folder under your home directory"

mkdir ~/src/
cp ./cron/make_json.py ~/src/
cp ./cron/move_mail.py ~/src/

echo "Make webpage files under your 'public_html' folder"

mkdir ~/public_html/printer
cp ./index.html ~/publc_html/printer/
cp -R ./Flat-UI-master ~/public_html/printer/
cp -R ./js ~/public_html/printer
cp ./public_html/json.php ~/public_html/printer/

echo "Installation is completed!!"
echo "You can access to the website."
echo "http://web.sfc.keio.ac.jp/~`echo ~/ | tail -c 10`printer/index.html"
