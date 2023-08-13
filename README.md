# birthdaymanager
A simple program to help you manage birthdays

Currently implemented:
- -l: lists every birthday
- -n: lists every birthday within the next 30days
- -add NAME/DAY/MONTH/{YEAR}: adds a birthday with given name and date. Year is optional.
- -remove INDEX: remove a birthday with index INDEX

Requirments:
- Python 3
- pandas

Getting started:
- Linux: In the terminal, run `git clone https://github.com/Afixll/birthdaymanager.git && mv birthdaymanager ~/.birthdaymanager`. This will clone the repo and hide it in your home folder. Next add an alias to your bash to use the birthdaymanager efficently from the terminal. To do this simply add `alias birthday='python3 ~/.birthdaymanager/main.py'` to the end of `/etc/bash.bashrc` (you'll need sudo permissions to edit the file). Now logout and login again. You should be able to use the birthdaymanager from terminal by simly typing in `birthday -OPTION`
- Windows & Mac: Clone the repo and execute main.py with python3 or later :D. Sorry i have no idea how to do stuff on these platforms, but the program should still work on these (in theory, i didn't try it)
