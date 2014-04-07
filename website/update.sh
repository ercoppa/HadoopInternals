#!/bin/bash

jeckyll build

git add ./*
git commit -a -m "~"
git push

cd ../../HadoopDiagrams.gh-pages.git
cp -a ../HadoopDiagrams/website/_site/* ./
git add ./*
git commit -a -m "~"
git push

exit 0
