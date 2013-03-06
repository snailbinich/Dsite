#! /bin/sh
# Author : Zhaoyan

baseDir=`pwd`
targetDir="${baseDir}/output"

if [ ! -d $targetDir ]; then
  echo "output dir doesn't exist"
  mkdir  $targetDir
else 
  cd $targetDir && rm -rf *
  echo "output dir exist"
fi 

cp -r $baseDir/css $targetDir/
cp -r $baseDir/img $targetDir/
cp -r $baseDir/js $targetDir/


#Generate files
pandoc -s --template=$baseDir/template/template.html -o $targetDir/index.html $baseDir/source/index.md

#build tutorial
for f in `find ./ -name *.md`; 
do 
  echo $f;
done

