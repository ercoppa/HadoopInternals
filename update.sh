#!/bin/bash

cp -a ../HadoopDiagrams/website/_site/* ./
git add ./*
git commit -a -m "~"
git push

exit 0
