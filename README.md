# What is this?
This is a simple python script used in linux x64 server for ict network login.

To clone the original repo
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

Replace `YOUR_USERNAME` with your ict login username and `YOUR_PASSWORD` with your password in `login.py`.

```
nohup python login.py > auto_login.log &
```
