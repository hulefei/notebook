@echo off

python app.py

git add .
git commit -m "update"

git remote set-url origin https://hulefei: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@github.com/hulefei/notebook.git
git push origin main

timeout /t 60

echo "https://hulefei.github.io/notebook/"
call start https://hulefei.github.io/notebook
PAUSE
