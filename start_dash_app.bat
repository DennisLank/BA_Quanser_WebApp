@echo off
call conda activate quanser_env
timeout /t 2 >nul
python dash_app.py
