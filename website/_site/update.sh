#!/bin/bash

jekyll build

git add ./*
git commit -a -m "updating website"
git push

cd ../../HadoopDiagrams.gh-pages.git
cp -a ../HadoopDiagrams/website/_site/* ./
cp -a ../HadoopDiagrams/website/public/images/* public/images/
git add ./*
git commit -a -m "updating website"
git push

exit 0
