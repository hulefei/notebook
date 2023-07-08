docker run -e URL=$1 -e CATEGORY=$2 \
-v /data/home/lefeihu/documents/notebook:/app  \
hulefei/notebook

git add .
git commit -m "update %1"
#git remote set-url origin https://<你的用户名>:<你的token>@github.com/<你的用户名>/<你的仓库名>.git
#git push origin main
