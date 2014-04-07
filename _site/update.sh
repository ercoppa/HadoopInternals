#!/bin/bash

jekyll build

git add ./*
git commit -a -m "updating website"
git push

cd ../../HadoopDiagrams.gh-pages.git
cp -a ../HadoopDiagrams/website/_site/* ./
git add ./*
git commit -a -m "updating website"
git push

exit 0
