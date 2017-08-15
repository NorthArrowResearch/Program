#!/usr/bin/env bash
virtualenv --no-site-packages ../.venv
source ../.venv/bin/activate
pip install pymysql
deactivate