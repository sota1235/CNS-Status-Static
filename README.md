CNS Printer Status
====

View the CNS printer status from Mail data.

(for CNS Consultant)

### Description

You can see the CNS Printer Status on the website.

### Demo

[Printer Status Viewer](http://web.sfc.keio.ac.jp/~t11460ss/printer/index.html)

![demo.png](http://i.gyazo.com/2df1ea5f294b92153f21d501cdf9d1ae.png)

### Requirement

* python2.7

* PHP 5.3.3

* Procmail

(Enviroment of ccx September 28, 2014)

And if you use auto filing for `CNS Printer Status`, you need to stop it.

### Install

First, you need to remote login to webedit.sfc.keio.ac.jp.

Then, enter the commands.

```Shell

$ cd

$ git clone https://github.com/sota1235/CNS-Status-Static.git

$ cd CNS-Static-Status

$ ./install

```

Then, you can access to the URL.

 * [http://web.sfc.keio.ac.jp/~{your CNS login name}/printer/index.html](http://web.sfc.keio.ac.jp/~{your CNS login name}/printer/index.html)

### Author

[@sota1235](https://github.com/sota1235)

@okatooth
