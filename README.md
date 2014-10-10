CNS Printer Status
====

View the CNS printer status from Mail data.

(for CNS Consultant)

### Description

You can see the CNS printer status on the website.

### Demo

[Printer Status Viewer](http://printer.sota1235.net)

![demo.png](http://i.gyazo.com/6062cbadf9f8328c8579828159219836.png)

### Requirement

* python2.7

* PHP 5.3.3

(Enviroment of ccx September 28, 2014)

### Install

First, you need to remote login to webedit.sfc.keio.ac.jp.

Then, enter the commands.

```Shell

$ cd

$ git clone https://github.com/sota1235/CNS-Status-Static.git

$ cd CNS-Static-Status

$ ./install

```

Then, edit crontab.

You need to enter the command to edit crontab.

```Shell

$ crontab -e

```

Then, please add the following statement.

```
# m h dom mon dow command
*/10 * * * * /usr/local/bin/python /home/{your_login_name}/src/make_json.py
*/10 * * * * /usr/local/bin/python /home/{your_login_name}/src/move_mail.py /home/{your_login_name}/Maildir/cur/
*/10 * * * * /usr/local/bin/python /home/{your_login_name}/src/move_mail.py /home/{your_login_name}/Maildir/new/
```

The installation completes	.

You can access to the URL.

 * [http://web.sfc.keio.ac.jp/~{your CNS login name}/printer/index.html](http://web.sfc.keio.ac.jp/~{your CNS login name}/printer/index.html)

### Author

[@sota1235](https://github.com/sota1235)
