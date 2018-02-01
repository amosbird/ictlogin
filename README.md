# What is this?
This is a simple python script used in linux x64 server for ict network login.

Original Repo address
```
git clone https://github.com/amosbird/ictlogin
```

This repo added connectivity checking functionality  
To clone this repo
```
git clone https://github.com/AveryLiu/ictlogin.git
```

Then  
```
cd ictlogin
pip install ./selenium-3.4.3-py2.py3-none-any.whl --user
```

Copy `phantomjs` to system path such as `/usr/local/bin`.

Create a new conf file under the same directory `account.conf` and set  
the first line to your username and second line to your password

```
nohup python login.py > auto_login.log &
```
