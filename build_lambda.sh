#!/usr/bin/env bash

# delete old build
rm -R lambdabuild
rm lambdabuild.zip

mkdir lambdabuild

# copy files over
cp -R lambdaenv/lib/python2.7/site-packages/ lambdabuild/
mkdir lambdabuild/lambda
cp lambda/lambda.py lambdabuild

# zip it up
zip -r lambdabuild{.zip,}
