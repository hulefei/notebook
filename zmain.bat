@echo off

python app.py

git add .
git commit -m "update"

git remote set-url origin https://hulefei:%GH_TOKEN%@github.com/hulefei/notebook.git
git push origin main

timeout /t 60

echo "https://hulefei.github.io/notebook/"
call start https://hulefei.github.io/notebook
PAUSE
