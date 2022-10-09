@echo off
set /p MYNAME="Name: "

py manage.py startapp %MYNAME%