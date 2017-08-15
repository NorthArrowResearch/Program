#!/bin/sh
lambda_name="CHaMPMap"
zip_file="${lambda_name}.zip"

cd ..
rm -fr deploy
mkdir deploy
files="handler.py"
chmod 755 ${files}

cp -fr .venv/lib/python2.7/site-packages/pymysql deploy/pymysql
cp ${files} deploy
cd deploy
zip -r "${zip_file}" pymysql ${files}

aws lambda update-function-code \
    --region "us-west-2" \
    --function-name "${lambda_name}"  \
    --zip-file "fileb://${zip_file}" --profile matt

rm -fr deploy