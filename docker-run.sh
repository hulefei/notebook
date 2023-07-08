docker run -e URL=$1 -e CATEGORY=$2 \
-v /data/home/lefeihu/documents/notebook/results:/app/results  \
-v /data/home/lefeihu/documents/notebook:/app  \
hulefei/notebook

git add .
git commit -m "update %1"
git push
