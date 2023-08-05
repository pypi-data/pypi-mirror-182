#Import Libraries
import sys
import jaydebeapi
import pandas as pd
from getpass import getpass
import re
from datetime import datetime
import itertools
import warnings
from base64 import b64encode
from base64 import b64decode
from Cryptodome.Cipher import AES
import hashlib
from datetime import datetime
import os
import yaml
from sqlalchemy import create_engine
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Util.Padding import unpad
from Cryptodome.Hash import SHA256
import logging
from logging.handlers import RotatingFileHandler
warnings.filterwarnings("ignore")
dt = datetime.now()
ts = datetime.timestamp(dt)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
maxByteSize = 1.5*1024*1024
file_handler = RotatingFileHandler('backup_versioncontrol.log', maxBytes=maxByteSize,backupCount=10)
file_format = logging.Formatter('%(asctime)s: %(message)s', datefmt='%d-%m-%Y || %I:%M:%S %p')
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

def decrypt(orgId_alpha,orgId,folder_path,key_decrypt):
    logger.info("Decrypting the encoded email id and password")
    file_path=str(folder_path).strip()+str(orgId_alpha).strip()+"/cred.bin"
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

def serverDetails(orgId_alpha,orgId,folder_path,host,key_decrypt,jar_file_name):
    try:
        jar_loc=str(folder_path).strip()+str(jar_file_name).strip()
        dec_data = decrypt(orgId_alpha,orgId,str(folder_path).strip(),str(key_decrypt))
        uid = dec_data[0]
        pwd = dec_data[1]
        driver_class = "com.zetaris.lightning.jdbc.LightningDriver"
        driver_file= jar_loc
        host = str(host).strip()
        port = "10000"
        connection_string='jdbc:zetaris:lightning@'+ host +':'+ port
        con = jaydebeapi.connect(driver_class, connection_string, [uid, pwd], driver_file,)
        curs = con.cursor()
        print("connection Done using JDBC")
        return con
    except:
        logger.info("\nEntered details are incorrect.Cannot connect to database server.\n")
        logger.info("Please try again.\n")
        serverDetails(orgId_alpha,orgId,folder_path,host,key_decrypt,jar_file_name)
            
    
def mainMenu(orgId,con,option,arg1,arg2,arg3):
    if option != 10000:
        print("\n Select the following option to migrate: \n")
        print("1. Data Pipeline container")
        print("2. Individual Data Pipeline")
        print("3. Data Quality container")
        print("4. Individual Data Quality Pipeline")
        print("5. Data Mart")
        print("6. Individual Table/View in the existing Datamart")
        print("7. Permanent Views")
        print("8. View the list of Container/Pipeline Name")
        print("9. Exit")
        try:
            option = int(str(arg1).lower().strip())
            if option == 1:
                DataPipelineContainer_InsertQueries(orgId,con,option,arg1,arg2,arg3)
            elif option == 2:
                IndivdualDataPipeline_InsertQueries(orgId,con,option,arg1,arg2,arg3)
            elif option == 3:
                DataPipelineContainer_InsertQueries(orgId,con,option,arg1,arg2,arg3)
            elif option == 4:
                IndivdualDataPipeline_InsertQueries(orgId,con,option,arg1,arg2,arg3)
            elif option == 5:
                DataMart_InsertQueries(orgId,con,arg1,arg2,arg3)
            elif option == 6:
                DataMart_IndTable_InsertQueries(orgId,con,arg1,arg2,arg3)
            elif option == 7:
                PermanentViews_InsertQueries(orgId,con,arg1,arg2,arg3)
            elif option == 9:
                print("\nThanks for using the system")
                exit
            else:
                print("\n invalid option\n")
                print("\n Thanks for using the system")
                exit
        except:
            logger.info("\nIndvalid selection. Please select between 1-8.\n")
    else:
        print("\n Thanks for using the system")
        exit
 
def checkcontainername(orgId,container_name,con,option):
    logger.info("OrgId "+str(orgId))
    logger.info("Container Name "+str(container_name))
    try:
        sql_containername_check="""select 'INSERT INTO pipeline_container (id, case_sensitive_name,description, name, fk_organisation_id)  VALUES (' || id || ',''' || CHAR(39)||COALESCE(case_sensitive_name, '')||CHAR(39)|| ''',''' ||CHAR(39)||COALESCE(description, '')||CHAR(39) || ''',''' ||CHAR(39)||COALESCE(name,'')||CHAR(39) || ''',' || COALESCE(fk_organisation_id, 0) ||''');'  from metastore.pipeline_container where name='%s' and fk_organisation_id=%s"""%(container_name,orgId)
        curs = con.cursor()
        curs.execute(sql_containername_check)
        res = curs.fetchall()
        if len(res)>0:
            return True
        else:
            return False
    except Exception as e:
        logger.info("Checking Container Name")
        logger.info(e)
    
def checkcontainer_pipeline_name(orgId,container_name,pipeline_name, con):
    logger.info("OrgId "+str(orgId))
    logger.info("Container Name "+str(container_name))
    logger.info("Pipeline Name "+str(pipeline_name))
    try:
        sql_container_pipeline_chk="""select 'INSERT INTO pipeline_relation (id, case_sensitive_name,description, name, fk_pipeline_container_id)VALUES(' || id || ',''' ||CHAR(39)|| COALESCE(case_sensitive_name, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(description, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(name, '')||CHAR(39) || ''',' || COALESCE(fk_pipeline_container_id, 0) || ');'     from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name = '%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'"""%(container_name,orgId,pipeline_name)
        curs = con.cursor()
        curs.execute(sql_container_pipeline_chk)
        res_con_pipe = curs.fetchall()
        if len(res_con_pipe)>0:
            return True
        else:
            return False
    except Exception as e:
        logger.info("Checking Pipeline Name")
        logger.info(e)

    
def chk_datamart_name(orgId,datamart_name,con):
    logger.info("OrgId "+str(orgId))
    logger.info("Data Mart Name "+str(datamart_name))
    try:
        sql_data_mart_ck = """SELECT 'INSERT INTO data_mart (id, case_sensitive_name ,default_view , name , fk_organisation_id ) VALUES (' || id || ',''' || CHAR(39)|| COALESCE(case_sensitive_name, '') ||CHAR(39)|| ''',''' ||CHAR(39)|| COALESCE(default_view, '')||CHAR(39)||''',''' ||CHAR(39)|| COALESCE(name,'')||CHAR(39) ||''','|| COALESCE(fk_organisation_id,'') ||');' FROM metastore.data_mart where name= '%s' and fk_organisation_id=%s;"""%(datamart_name,orgId)
        curs = con.cursor()
        curs.execute(sql_data_mart_ck)
        res_dm_chk = curs.fetchall()
        if len(res_dm_chk)>0:
            return True
        else:
            return False
    except Exception as e:
        logger.info("Checking DataMart Name")
        logger.info(e)
        
    
def chk_datamart_table_name(orgId,datamart_name,table_name, con):
    logger.info("OrgId "+str(orgId))
    logger.info("Data Mart Name "+str(datamart_name))
    logger.info("Table Name "+str(table_name))
    try:
        sql_data_mart_ck = """SELECT 'INSERT INTO data_mart_table (id, case_sensitive_name , name , source_table  ,fk_data_mart_id  )  VALUES (' || id || ',''' || CHAR(39) || COALESCE(case_sensitive_name, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(name, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(source_table, '') || CHAR(39) || ''',' || COALESCE(fk_data_mart_id, 0) || ');' FROM metastore.data_mart_table where fk_data_mart_id in ( select id from metastore.data_mart where name = '%s' and fk_organisation_id=%s) and name='%s';"""%(datamart_name,orgId,table_name) 
        curs = con.cursor()
        curs.execute(sql_data_mart_ck)
        res_dm_chk = curs.fetchall()
        if len(res_dm_chk)>0:
            return True
        else:
            return False
    except Exception as e:
        logger.info("Checking Data Mart Table Name")
        logger.info(e)  
    
def chk_view_name(orgId,View_name,con):
    logger.info("OrgId "+str(orgId))
    logger.info("View Name "+str(View_name))
    try:
        sql_view_name_ck = """select 'INSERT INTO schema_store_view (id, description ,generator, materialized_table,name,query,fk_organisation_id   )  VALUES (' || id || ',''' || CHAR(39) || COALESCE(description, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(generator, '') || char(39) || ''',''' || CHAR(39) || COALESCE(materialized_table, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(name, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(query, '') || CHAR(39) || ''',' || COALESCE(fk_organisation_id, 0) || ');' FROM metastore.schema_store_view where name = '%s' and fk_organisation_id=%s"""%(View_name,orgId)
        curs = con.cursor()
        curs.execute(sql_view_name_ck)
        res_view_chk = curs.fetchall()
        if len(res_view_chk)>0:
            return True
        else:
            return False
    except Exception as e:
        logger.info("Checking View Name")
        logger.info(e)   
    
def DataPipelineContainer_InsertQueries(orgId,con,option,arg1,arg2,arg3):
    try:
        container_name = str(arg2).strip()
        container_name = container_name.lower()
        chk_container_name= checkcontainername(orgId,container_name,con,option)
        if chk_container_name == False:
            logger.info("\nIncorrect container name. Please check the container name & try again.")
        else:
            curs = con.cursor()
            list_queries = []
            print("\nGenerating script...")
            
            sql_pipeline_container = """select 'INSERT INTO metastore.pipeline_container  (id, case_sensitive_name,description, name, fk_organisation_id)  VALUES (' || id || ',''' || CHAR(39)||COALESCE(case_sensitive_name, '')||CHAR(39)|| ''',''' ||CHAR(39)||COALESCE(description, '')||CHAR(39) || ''',''' ||CHAR(39)||COALESCE(name,'')||CHAR(39) || ''',' || COALESCE(fk_organisation_id, 0) ||''');'  from metastore.pipeline_container where  name='%s' and fk_organisation_id=%s"""%(container_name,orgId)
            curs.execute(sql_pipeline_container)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
            
            sql_pipeline_relation = """select 'INSERT INTO metastore.pipeline_relation (id, case_sensitive_name,description, name, fk_pipeline_container_id) VALUES (' || id || ',''' || CHAR(39)||COALESCE(case_sensitive_name, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(description, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(name, '')||CHAR(39) || ''',' || COALESCE(fk_pipeline_container_id, 0) || ');' from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name = '%s' and fk_organisation_id=%s)"""%(container_name,orgId)
            curs.execute(sql_pipeline_relation)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
                
            sql_pipeline_node="""select 'INSERT INTO metastore.pipeline_node (id, case_sensitive_name,description, name, fk_pipeline_relation_id, pipeline_type)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(case_sensitive_name, '')||CHAR(39) || ''',''' ||CHAR(39)||COALESCE(description, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(name,'')||CHAR(39) || ''',' || COALESCE(fk_pipeline_relation_id, 0) ||',''' ||char(39)|| COALESCE(pipeline_type,'')||char(39) ||''');'  from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s))"""%(container_name,orgId)
            curs.execute(sql_pipeline_node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
            
            sql_pipeline_node_schema="""select 'INSERT INTO metastore.pipeline_node_schema (id, column_alias,column_name, data_type, sql_expression, fk_pipeline_node_id)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(column_alias, '')||CHAR(39)|| ''',''' ||CHAR(39)|| COALESCE(column_name, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(data_type,'')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(sql_expression, '')||CHAR(39) ||''',' || COALESCE(fk_pipeline_node_id, 0) ||');'  FROM metastore.pipeline_node_schema where fk_pipeline_node_id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s)))"""%(container_name,orgId)
            curs.execute(sql_pipeline_node_schema)
            res = curs.fetchall()
            for i in range(len(res)):
                temp_str=res[i][0].replace("'",'"')
                temp_str_list=list(temp_str)
                result_comma = [_.start() for _ in re.finditer(",", temp_str)]
                if("decimal(38" not in temp_str):
                    temp_str_list[result_comma[8]+1] = "'"
                    temp_str_list[result_comma[-1]-1] = "'"
                temp_str_1 = "".join(temp_str_list)
                list_queries.append(temp_str_1)
            
            sql_pipeline_node_property="""select 'INSERT INTO metastore.pipeline_node_property (id, property_key,property_value, fk_pipeline_node_id)  VALUES (' || id || ',''' ||CHAR(39)||COALESCE(property_key, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(property_value, '')||CHAR(39) ||''',' || COALESCE(fk_pipeline_node_id, 0) ||');'  FROM metastore.pipeline_node_property  where fk_pipeline_node_id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s)))"""%(container_name,orgId)
            curs.execute(sql_pipeline_node_property)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])


            sql_datasource_Node="""select 'INSERT INTO metastore.pipeline_datasource(id, datasource,datasource_table) VALUES(' || id || ',''' ||CHAR(39)|| COALESCE(datasource, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(datasource_table, '')||CHAR(39) || ''');' FROM metastore.pipeline_datasource where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name = '%s' and fk_organisation_id=%s)))"""%(container_name,orgId) 
            curs.execute(sql_datasource_Node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_sql_table="""select 'INSERT INTO metastore.pipeline_sqltable (id, sql_query,source_tables)
            VALUES(' || id || ',''' ||CHAR(39)||COALESCE(sql_query, '')||CHAR(39) || ''',''' ||CHAR(39)|| 
            COALESCE(source_tables, '')||CHAR(39) || ''');' FROM metastore.pipeline_sqltable where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name = '%s' and fk_organisation_id=%s)))"""%(container_name,orgId)
            curs.execute(sql_sql_table)
            to_substitute = "''"
            res = curs.fetchall()
            for i in range(len(res)):
                temp_str=res[i][0].replace("'",'"')
                temp_str_list=list(temp_str)
                result_comma = [_.start() for _ in re.finditer(",", temp_str)]
                temp_str_list[result_comma[2]+1] = "'"
                temp_str_list[result_comma[-1]-1] = "'"
                temp_str_1 = "".join(temp_str_list)
                list_queries.append(temp_str_1)
        
            sql_projection_node="""select 'INSERT INTO metastore.pipeline_projection (id, filter_expression,order_by, windows_spec)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(filter_expression, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(order_by, '')||CHAR(39) ||''',''' ||CHAR(39)|| COALESCE(windows_spec,'')||CHAR(39)||''');'  FROM metastore.pipeline_projection where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s)))"""%(container_name,orgId)
            curs.execute(sql_projection_node)
            res = curs.fetchall()
            for i in range(len(res)):
                temp_str=res[i][0].replace("'",'"')
                temp_str_list=list(temp_str)
                result_comma = [_.start() for _ in re.finditer(",", temp_str)]
                temp_str_list[result_comma[3]+1] = "'"
                result_comma = [_.start() for _ in re.finditer("\"", temp_str)]
                temp_str_list[result_comma[-5]] = "'"
                temp_str_1 = "".join(temp_str_list)
                list_queries.append(temp_str_1)

            sql_join_node="""select 'INSERT INTO metastore.pipeline_join (id, filter_expression,join_predicate, join_tables, order_by)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(filter_expression, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(join_predicate, '')||CHAR(39) ||''',''' ||CHAR(39)|| COALESCE(join_tables,'')||CHAR(39) ||''',''' || CHAR(39)||COALESCE(order_by,'')||CHAR(39) ||''');'  FROM metastore.pipeline_join where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name='%s' and fk_organisation_id=%s)))"""%(container_name,orgId)
            curs.execute(sql_join_node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_aggregation_node="""select 'INSERT INTO metastore.pipeline_aggregation (id, filter_expression,group_expression, having_expression, order_by)  VALUES (' || id || ',''' ||CHAR(39)||COALESCE(filter_expression, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(group_expression, '')||CHAR(39) ||''',''' ||CHAR(39)|| COALESCE(having_expression,'')||CHAR(39) ||''',''' ||CHAR(39)|| COALESCE(order_by,'')||CHAR(39) ||''');'  FROM metastore.pipeline_aggregation where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s)))"""%(container_name,orgId)
            curs.execute(sql_aggregation_node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_aggregation_node="""select 'INSERT INTO metastore.pipeline_sink (id, sink_type)  VALUES (' || id || ',''' ||char(39)|| COALESCE(sink_type, '')||char(39) ||''');'  FROM metastore.pipeline_sink where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s)))"""%(container_name,orgId)
            curs.execute(sql_aggregation_node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_DQ_pipeline = """select 'INSERT INTO metastore.pipeline_simple_dq (id) VALUES ('||id||');' FROM metastore.pipeline_simple_dq where id in (select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name='%s' and fk_organisation_id=%s)))"""%(container_name,orgId)
            curs.execute(sql_DQ_pipeline)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
                
            sql_pipeline_simple_dq_rule = """SELECT 'INSERT INTO metastore.pipeline_simple_dq_rule (id, columns ,expression , filter , name,fk_pipeline_simple_dq_id  ) VALUES (' || id || ',''' ||CHAR(39)||COALESCE(columns, '')||CHAR(39) || ''',''' ||CHAR(34)|| COALESCE(expression, '')||CHAR(34) || ''',''' ||CHAR(34)|| COALESCE(filter, '')||CHAR(34) || ''',''' ||CHAR(39)|| COALESCE(name, '')||CHAR(39) || ''',' || COALESCE(fk_pipeline_simple_dq_id, 0) || ');' FROM metastore.pipeline_simple_dq_rule where fk_pipeline_simple_dq_id in (select id from metastore.pipeline_simple_dq where id in (select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name = '%s' and fk_organisation_id=%s))))"""%(container_name,orgId)
            curs.execute(sql_pipeline_simple_dq_rule)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            generateSQLfile(list_queries,container_name,'pipeline','')
    except Exception as e:
        logger.info("Inside Full Pipeline container backup function")
        logger.info(e)

def IndivdualDataPipeline_InsertQueries(orgId,con,option,arg1,arg2,arg3):
    try:
        container_name = str(arg2).strip()
        print(container_name)
        container_name = container_name.lower()
        pipeline_name=str(arg3).strip()
        print(pipeline_name)
        pipeline_name=pipeline_name.lower()
        chk_con_pipe_name= checkcontainer_pipeline_name(orgId,container_name,pipeline_name, con)
        if chk_con_pipe_name == False:
            print("\n Incorrect container or pipeline name. Please check the container/pipeline name & try again")  
        else:
            curs = con.cursor()
            list_queries = []
            print("\nGenerating script....")
            
            sql_pipeline_relation = """select 'INSERT INTO metastore.pipeline_relation (id, case_sensitive_name,description, name, fk_pipeline_container_id)VALUES(' || id || ',''' ||CHAR(39)|| COALESCE(case_sensitive_name, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(description, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(name, '')||CHAR(39) || ''',' || COALESCE(fk_pipeline_container_id, 0) || ');'     from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name = '%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_pipeline_relation)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
                
            sql_pipeline_node="""select 'INSERT INTO metastore.pipeline_node (id, case_sensitive_name,description, name, fk_pipeline_relation_id, pipeline_type)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(case_sensitive_name, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(description, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(name,'')||CHAR(39) || ''',' || COALESCE(fk_pipeline_relation_id, 0) ||',''' ||CHAR(39)|| COALESCE(pipeline_type,'')||CHAR(39) ||''');'  from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s) and case_sensitive_name = '%s')"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_pipeline_node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
                
            sql_pipeline_node_schema="""select 'INSERT INTO metastore.pipeline_node_schema (id, column_alias,column_name, data_type, sql_expression, fk_pipeline_node_id)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(column_alias, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(column_name, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(data_type,'')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(sql_expression, '')||CHAR(39) ||''',' || COALESCE(fk_pipeline_node_id, 0) ||');'  FROM metastore.pipeline_node_schema where fk_pipeline_node_id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_pipeline_node_schema)
            res = curs.fetchall()
            for i in range(len(res)):
                temp_str=res[i][0].replace("'",'"')
                temp_str_list=list(temp_str)
                result_comma = [_.start() for _ in re.finditer(",", temp_str)]
                temp_str_list[result_comma[8]+1] = "'"
                temp_str_list[result_comma[-1]-1] = "'"
                temp_str_1 = "".join(temp_str_list)
                list_queries.append(temp_str_1)
            
            sql_pipeline_node_property="""select 'INSERT INTO metastore.pipeline_node_property (id, property_key,property_value, fk_pipeline_node_id)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(property_key, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(property_value, '')||CHAR(39) ||''',' || COALESCE(fk_pipeline_node_id, 0) ||');'  FROM metastore.pipeline_node_property  where fk_pipeline_node_id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_pipeline_node_property)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
                
            sql_datasource_Node="""select 'INSERT INTO metastore.pipeline_datasource(id, datasource,datasource_table) VALUES(' || id || ',''' ||CHAR(39)|| COALESCE(datasource, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(datasource_table, '')||CHAR(39) || ''');' FROM metastore.pipeline_datasource where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name = '%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_datasource_Node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
                
            sql_sql_table="""select 'INSERT INTO metastore.pipeline_sqltable (id, sql_query,source_tables) VALUES(' || id || ',''' ||CHAR(39)||COALESCE(sql_query, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(source_tables, '')||CHAR(39) || ''');' FROM metastore.pipeline_sqltable where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name = '%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_sql_table)
            to_substitute = "''"
            res = curs.fetchall()
            for i in range(len(res)):
                temp_str=res[i][0].replace("'",'"')
                temp_str_list=list(temp_str)
                result_comma = [_.start() for _ in re.finditer(",", temp_str)]
                temp_str_list[result_comma[2]+1] = "'"
                temp_str_list[result_comma[-1]-1] = "'"
                temp_str_1 = "".join(temp_str_list)
                list_queries.append(temp_str_1)

            sql_projection_node="""select 'INSERT INTO metastore.pipeline_projection (id, filter_expression,order_by, windows_spec)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(filter_expression, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(order_by, '')||CHAR(39) ||''',''' || CHAR(39)||COALESCE(windows_spec,'')||CHAR(39) ||''');'  FROM metastore.pipeline_projection where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_projection_node)
            res = curs.fetchall()
            for i in range(len(res)):
                temp_str=res[i][0].replace("'",'"')
                temp_str_list=list(temp_str)
                result_comma = [_.start() for _ in re.finditer(",", temp_str)]
                temp_str_list[result_comma[3]+1] = "'"
                result_comma = [_.start() for _ in re.finditer("\"", temp_str)]
                temp_str_list[result_comma[-5]] = "'"
                temp_str_1 = "".join(temp_str_list)
                list_queries.append(temp_str_1)

            sql_join_node="""select 'INSERT INTO metastore.pipeline_join (id, filter_expression,join_predicate, join_tables, order_by)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(filter_expression, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(join_predicate, '')||CHAR(39) ||''',''' ||CHAR(39)|| COALESCE(join_tables,'')||CHAR(39) ||''',''' ||CHAR(39)|| COALESCE(order_by,'')||CHAR(39) ||''');'  FROM metastore.pipeline_join where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name='%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_join_node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_aggregation_node="""select 'INSERT INTO metastore.pipeline_aggregation (id, filter_expression,group_expression, having_expression, order_by)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(filter_expression, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(group_expression, '')||CHAR(39) ||''',''' ||CHAR(39)|| COALESCE(having_expression,'')||CHAR(39) ||''',''' ||CHAR(39)|| COALESCE(order_by,'')||CHAR(39) ||''');'  FROM metastore.pipeline_aggregation where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_aggregation_node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_sink_node="""select 'INSERT INTO metastore.pipeline_sink (id, sink_type)  VALUES (' || id || ',''' ||char(39)|| COALESCE(sink_type, '')||char(39) ||''');'  FROM metastore.pipeline_sink where id in(select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from  metastore.pipeline_container where name='%s' and fk_organisation_id=%s) and case_sensitive_name = '%s'))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_sink_node)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_DQ_pipeline = """select 'INSERT INTO metastore.pipeline_simple_dq (id) VALUES ('||id||');' FROM metastore.pipeline_simple_dq where id in (select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name='%s' and fk_organisation_id=%s) and name = '%s'))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_DQ_pipeline)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_pipeline_simple_dq_rule = """SELECT 'INSERT INTO metastore.pipeline_simple_dq_rule (id, columns ,expression , filter , name,fk_pipeline_simple_dq_id  ) VALUES (' || id || ',''' ||CHAR(39)||COALESCE(columns, '')||CHAR(39)|| ''',''' ||CHAR(34)||COALESCE(expression, '')||CHAR(34) || ''',''' ||CHAR(34)|| COALESCE(filter, '')||CHAR(34) || ''',''' ||CHAR(39)||COALESCE(name, '')||CHAR(39)|| ''',' || COALESCE(fk_pipeline_simple_dq_id, 0) || ');' FROM metastore.pipeline_simple_dq_rule where fk_pipeline_simple_dq_id in (select id from metastore.pipeline_simple_dq where id in (select id from metastore.pipeline_node where fk_pipeline_relation_id in (select id from metastore.pipeline_relation where fk_pipeline_container_id in (select id from metastore.pipeline_container where name = '%s' and fk_organisation_id=%s)and name='%s')))"""%(container_name,orgId,pipeline_name)
            curs.execute(sql_pipeline_simple_dq_rule)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
            
            generateSQLfile(list_queries,container_name,pipeline_name,'Pipeline')
    except Exception as e:
        logger.info("Inside Individual Pipeline Backup Function")
        logger.info(e)
        
def PermanentViews_InsertQueries(orgId,con,arg1,arg2,arg3):
    try:
        View_name=str(arg2).strip()
        View_name = View_name.upper().strip()
        chk_viewname= chk_view_name(orgId,View_name,con)
        if chk_viewname == False:
            print("\n Incorrect view name.")  
        else:
            curs = con.cursor()
            list_queries = []

            print("\nGenerating script.....")
            sql_Permanent_View = """select 'INSERT INTO metastore.schema_store_view (id, description ,generator, materialized_table,name,query,fk_organisation_id   )  VALUES (' || id || ',''' || CHAR(39) || COALESCE(description, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(generator, '') || char(39) || ''',''' || CHAR(39) || COALESCE(materialized_table, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(name, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(query, '') || CHAR(39) || ''',' || COALESCE(fk_organisation_id, 0) || ');' FROM metastore.schema_store_view where name = '%s' and fk_organisation_id=%s"""%(View_name,orgId)
            curs.execute(sql_Permanent_View)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_schema_store_view_schema = """select  'INSERT INTO metastore.schema_store_view_schema  (id, column_name  ,data_type , fk_schema_store_view_id) VALUES (' || id || ',''' || CHAR(39) || COALESCE(column_name, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(data_type, '') || char(39) || ''',' || COALESCE(fk_schema_store_view_id, 0) || ');' FROM metastore.schema_store_view_schema where fk_schema_store_view_id in (select id from metastore.schema_store_view where name = '%s' and fk_organisation_id=%s)"""%(View_name,orgId)
            curs.execute(sql_schema_store_view_schema)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            generateSQLfile(list_queries,View_name,'Permanent_View','')
    except Exception as e:
        logger.info("Inside Permanent View Backup Function")
        logger.info(e)

def DataMart_InsertQueries(orgId,con,arg1,arg2,arg3):
    try:
        datamart_name=str(arg2).strip()
        datamart_name = datamart_name.upper().strip()
        chk_dm_name= chk_datamart_name(orgId,datamart_name,con)
        if chk_dm_name == False:
            print("\n Incorrect data mart name.")  
        else:
            curs = con.cursor()
            list_queries = []

            sql_data_mart = """SELECT 'INSERT INTO metastore.data_mart (id, case_sensitive_name ,default_view,description, name , fk_organisation_id ) VALUES (' || id || ',''' || CHAR(39)|| COALESCE(case_sensitive_name, '') ||CHAR(39)|| ''',''' ||CHAR(39)|| COALESCE(default_view, '')||CHAR(39)||''',''' ||CHAR(39)|| COALESCE(description, '')||char(39)||''','''||char(39)||COALESCE(name,'')||CHAR(39) ||''','|| COALESCE(fk_organisation_id,'') ||');' FROM metastore.data_mart where name= '%s' and fk_organisation_id=%s;"""%(datamart_name,orgId)
            curs.execute(sql_data_mart)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            print("\nGenerating Script....")

            sql_data_mart_table = """SELECT 'INSERT INTO metastore.data_mart_table (id, case_sensitive_name , name , source_table  ,fk_data_mart_id  )  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(case_sensitive_name, '')||CHAR(39)|| ''',''' ||CHAR(39)|| COALESCE(name, '')||CHAR(39)||''',''' ||CHAR(39)||COALESCE(source_table ,'')||CHAR(39) ||''','|| COALESCE(fk_data_mart_id,0) ||');'  FROM metastore.data_mart_table where fk_data_mart_id in (select id from  metastore.data_mart where name = '%s' and fk_organisation_id=%s);"""%(datamart_name,orgId)
            curs.execute(sql_data_mart_table)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])

            sql_data_mart_table_schema = """select  'INSERT INTO metastore.data_mart_table_schema (id, real_column_name , virtual_name, fk_data_mart_table_id)  VALUES (' || id || ',''' ||CHAR(39)||COALESCE(real_column_name, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(virtual_name, '')||CHAR(39) ||''','|| COALESCE(fk_data_mart_table_id,0) ||');' from metastore.data_mart_table_schema where fk_data_mart_table_id in (select id from metastore.data_mart_table where fk_data_mart_id in (select id from  metastore.data_mart where name = '%s' and fk_organisation_id=%s));"""%(datamart_name,orgId)
            curs.execute(sql_data_mart_table_schema)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
            
            generateSQLfile(list_queries,datamart_name,'DataMart','')
    except Exception as e:
        logger.info("Inside Data Mart backup fucntion")
        logger.info(e)
        
def DataMart_IndTable_InsertQueries(orgId,con,arg1,arg2,arg3):
    try:
        datamart_name=str(arg2).strip()
        datamart_name = datamart_name.upper().strip()
        table_name=str(arg3).strip()
        table_name = table_name.upper().strip()
        chk_dm_name= chk_datamart_table_name(orgId,datamart_name,table_name,con)
        if chk_dm_name == False:
            print("\n Incorrect data mart name.")
        else:
            curs = con.cursor()
            list_queries = []

            print("\nGenerating Script....")
        
            sql_data_mart_table = """SELECT 'INSERT INTO metastore.data_mart_table (id, case_sensitive_name , name , source_table  ,fk_data_mart_id  )  VALUES (' || id || ',''' || CHAR(39) || COALESCE(case_sensitive_name, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(name, '') || CHAR(39) || ''',''' || CHAR(39) || COALESCE(source_table, '') || CHAR(39) || ''',' || COALESCE(fk_data_mart_id, 0) || ');' FROM metastore.data_mart_table where fk_data_mart_id in ( select id from metastore.data_mart where name = '%s' and fk_organisation_id=%s) and name='%s';"""%(datamart_name,orgId,table_name)
            curs.execute(sql_data_mart_table)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
            
            sql_data_mart_table_schema = """select  'INSERT INTO metastore.data_mart_table_schema (id, real_column_name , virtual_name, fk_data_mart_table_id)  VALUES (' || id || ',''' ||CHAR(39)|| COALESCE(real_column_name, '')||CHAR(39) || ''',''' ||CHAR(39)|| COALESCE(virtual_name, '')||CHAR(39) ||''','|| COALESCE(fk_data_mart_table_id,0) ||');' from metastore.data_mart_table_schema where fk_data_mart_table_id in (select id from metastore.data_mart_table where fk_data_mart_id in (select id from  metastore.data_mart where name = '%s' and fk_organisation_id=%s)and name='%s');"""%(datamart_name,orgId,table_name)
            curs.execute(sql_data_mart_table_schema)
            res = curs.fetchall()
            for i in range(len(res)):
                list_queries.append(res[i][0])
            
            generateSQLfile(list_queries,datamart_name,table_name,'DataMart')
    except Exception as e:
        logger.info("Inside Data Mart Individual Tables Backup Function")
        logger.info(e)
    
def generateSQLfile(list_queries,filename1,filename2,filename3):
    try:
        filename1=filename1.lower()
        filename2=filename2.lower()
        filename3=filename3.lower()
        if (len(filename3)>1):
            output_filename =filename1+'-'+filename2+ '-'+ filename3 +'.sql'
        else:
            output_filename=filename1+'-'+filename2+'.sql'
        df = open(output_filename, 'w+')
        for i in range(len(list_queries)):
            df.write(list_queries[i])
            df.write('\n')
        df.close()
    except Exception as e:
        logger.info("Inside Generating Files with SQL Queries Function")
        logger.info(e)

def object_deployment(orgId_alpha,orgId,folder_path,host,key_decrypt,jar_file_name,arg1,arg2,arg3):
    try:
        con = serverDetails(orgId_alpha,orgId,folder_path,host,key_decrypt,jar_file_name)
        mainMenu(orgId,con,'',arg1,arg2,arg3)
    except Exception as e:
        logger.info("Inside Main Object Deployment / Backup of Metastore Main Function")
        logger.info(e)