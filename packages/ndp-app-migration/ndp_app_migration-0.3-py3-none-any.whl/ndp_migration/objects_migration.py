import sys
import jaydebeapi
import pandas as pd
from getpass import getpass
import re
import itertools
import warnings
from base64 import b64encode
from base64 import b64decode
import hashlib
import os
import os.path
import yaml
import requests
import json
from sqlalchemy import create_engine
from datetime import datetime
from datetime import *
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
from Cryptodome.Hash import SHA256
from getpass import getpass
import logging
from logging.handlers import RotatingFileHandler
from ndp_deployment.fetch_metastore import object_deployment

# Instantiating a Logger to log info+ data with a 1.5 GB max file size.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
maxByteSize = 1.5*1024*1024
file_handler = RotatingFileHandler('Migration.log', maxBytes=maxByteSize,backupCount=10)
file_format = logging.Formatter('%(asctime)s: %(message)s', datefmt='%d-%m-%Y || %I:%M:%S %p')
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

warnings.filterwarnings("ignore")
dt = datetime.now()
ts = datetime.timestamp(dt)

def decrypt(folder_path,key_decrypt):
    file_path=str(folder_path).strip()+"cred.bin"
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        salt = f.read(32)
        data = f.read()
    key = str(key_decrypt)
    key = PBKDF2(key, salt, dkLen=32, count=1000000,hmac_hash_module=SHA256)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    data = unpad(cipher.decrypt(data), AES.block_size)
    data = bytes.decode(data)
    dec_data = data.split('|||')
    return(dec_data)

def get_encrypted_pass (folder_path,key_decrypt,api_url):
    dec_data = decrypt(folder_path,key_decrypt)
    obj = {
        'target':dec_data[1]
    }
    apiurl='https://'+str(api_url).lower().strip()+':8443/enc'
    response = requests.post(url=apiurl,params=obj)
    return response.text

def get_bearer_token (orgId,folder_path,key_decrypt,api_url):
    org_folder_path=str(folder_path).strip()+str(orgId)+"/"
    dec_data = decrypt(org_folder_path,key_decrypt)
    encrypted_password=get_encrypted_pass(org_folder_path,key_decrypt,api_url)
    username = dec_data[0]
    obj = {
        "password":encrypted_password,
        "username":username,
        "orgId": str(orgId).strip()
    }
    apiurl='https://'+str(api_url).lower().strip()+':8443/login'
    response = requests.post(url=apiurl,data=obj)
    response = json.loads(response.text)
    return response['bearer_token']

def runQuery(query:str,r,api_url,bearer_token):
    try:
        obj={
            "sql":query,
        }
        auth={
            "Authorization": "Bearer " + bearer_token
        }
        apiurl='https://'+str(api_url).lower().strip()+':8443/query'
        response = requests.post(url=apiurl, data=obj, headers=auth)
        response=json.loads(response.text)
        if response.get('data'):
            querytoken=response['data']['query_token']
            close_obj={
                "query_token":querytoken,
                "close_query": "true"
            }
            apiurl='https://'+str(api_url).lower().strip()+':8443/closequery'
            requests.post(url=apiurl, data=close_obj, headers=auth)

        if(r):
            data = response['data']['data']
            return data
    except Exception as e:
        logger.info("Run Query Function Error Logs")
        logger.info(e)


def run_fetch_metastore(orgId_alpha,orgId,folder_path,host,key_decrypt,jar_file_name,option_for_backup,container_name,object_name):
    object_deployment(orgId_alpha,orgId,folder_path,host,key_decrypt,jar_file_name,option_for_backup,container_name,object_name)

def migrate_other_env(folder_path,jar_file_name,target_host,target_user_id,target_password,object_type,con_name,pipe_name,option_type):
    try:
        port = '10000'
        driver_class = "com.zetaris.lightning.jdbc.LightningDriver"
        driver_file = str(folder_path)+str(jar_file_name)
        uid=target_user_id
        pwd=target_password
        host=target_host
        connection_string='jdbc:zetaris:lightning@'+ host +':'+ port
        con = jaydebeapi.connect(driver_class, connection_string, [uid, pwd], driver_file,)
        curs=con.cursor()
        logger.info(con)
        logger.info("Target Host Connection successful")
        if (str(object_type).lower().strip()=='views'):
            filename_to_open=str(folder_path).lower().strip()+'Migration_Data_Objects/'+str(con_name).lower().strip()+'-permanent_view.sql'
        elif (str(object_type).lower().strip()=='pipelines'):
            if (option_type=='2' or option_type=='4'):
                filename_to_open=str(folder_path).lower().strip()+'Migration_Data_Objects/'+str(con_name).lower().strip()+'-'+str(pipe_name).lower().strip()+'-pipeline.sql'
            elif (option_type=='1' or option_type=='3'):
                filename_to_open=str(folder_path).lower().strip()+'Migration_Data_Objects/'+str(con_name).lower().strip()+'-pipeline.sql'
        elif (str(object_type).lower().strip()=='data_marts'):
            if (option_type=='5'):
                filename_to_open=str(folder_path).lower().strip()+'Migration_Data_Objects/'+str(con_name).lower().strip()+'-datamart.sql'
            elif (option_type=='6'):
                filename_to_open=str(folder_path).lower().strip()+'Migration_Data_Objects/'+str(con_name).lower().strip()+'-'+str(pipe_name).lower().strip()+'-datamart.sql'
        logger.info(filename_to_open)
        file_read = open(filename_to_open,'r')
        data_read = file_read.read()
        mylist = data_read.split(';')
        for line in mylist:
            if (line.strip()!=''):
                logger.info(line)
                curs.execute(line.strip())
    except Exception as e:
        logger.info('Migration to Target Environment - Not Successful. Please Check Logs.')
        logger.info(e)


def migration_data_objects(orgId_alpha,host,folder_path,key_decrypt,api_url,jar_file_name,option_for_backup,target_host,target_user_id,target_password,con_name,pipe_name,object_type):
    get_org_id="select id from metastore.organisation where organisation_id='"+str(orgId_alpha).strip()+"'"
    logger.info(get_org_id)
    api_url=str(api_url).lower().strip()
    bearer_token = get_bearer_token(orgId_alpha,folder_path,key_decrypt,api_url)
    org_list = runQuery(get_org_id,True,api_url,bearer_token)
    if isinstance(org_list[0],dict):
        for i in org_list:
            orgId = str(i['id'])
    print(orgId)
    print(option_for_backup)
    logger.info('Running Fetch Metastore')
    print(option_for_backup)
    run_fetch_metastore(str(orgId_alpha).strip(),str(orgId).strip(),str(folder_path).strip(),str(host),str(key_decrypt),str(jar_file_name).strip(),str(option_for_backup).strip(),str(con_name).strip(),str(pipe_name).strip())
    migrate_other_env(str(folder_path).strip(),str(jar_file_name),str(target_host),str(target_user_id),str(target_password),str(object_type).strip(),str(con_name).strip(),str(pipe_name).strip(),str(option_for_backup).strip())
    logger.info('\n Migration Successful')
