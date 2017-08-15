#!/bin/sh
lambda_name="mysql_test"
zip_file="${lambda_name}.zip"
role_arn="arn:aws:iam::<aws-account-no>:role/lambda-vpc-execution-role"

subnet_ids=`aws ec2 describe-subnets |\
                jq -r '.Subnets|map(.SubnetId)|join(",")'`
sec_group_id=`aws ec2 describe-security-groups --group-name "default" |\
                jq -r '.SecurityGroups[].GroupId'`

files="mysql_test.py rds_config.py"
chmod 755 ${files}
zip -r "${zip_file}" pymysql ${files}

aws lambda create-function \
    --region "us-east-1" \
    --function-name "${lambda_name}"  \
    --zip-file "fileb://${zip_file}" \
    --role "${role_arn}" \
    --handler "${lambda_name}.lambda_handler" \
    --runtime python2.7 \
    --timeout 60 \
    --vpc-config SubnetIds="${subnet_ids}",SecurityGroupIds="${sec_group_id}"