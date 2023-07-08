echo $1
echo $2

docker run -e URL=$1 -e CATEGORY=$2 hulefei/notebook