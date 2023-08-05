import snowflake.connector
import pandas as pd

from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
from pyathena import connect
import mysql.connector

class sql():
    def get_snf_df(snf_q,user_,password_,account_,warehouse_,database_):
        snowflake_con = snowflake.connector.connect(user=user_,
                                            password=password_,
                                            account=account_)
        snowflake_con.cursor().execute(f"USE WAREHOUSE {warehouse_}")
        snowflake_con.cursor().execute(f"USE DATABASE {database_}")

    
            
        if snf_q is None:
            return pd.DataFrame()
        
        snf_df =pd.read_sql_query(snf_q, snowflake_con) 
        
        cols = {}
        
        for each_col in snf_df.columns:
            cols[each_col] = each_col.lower()
            
        snf_df = snf_df.rename(columns=cols)
        return snf_df
    
    def get_dl_df(dl_q,aws_access_key_id_,aws_secret_access_key_,s3_staging_dir_,region_name_):
        
        cursor = connect(aws_access_key_id=aws_access_key_id_,
        aws_secret_access_key=aws_secret_access_key_,
        s3_staging_dir=s3_staging_dir_,
        region_name=region_name_).cursor()
    
            
        if dl_q is None:
            return pd.DataFrame()
        
        dl_df =pd.DataFrame(cursor.execute(dl_q))
        columns = [i[0] for i in cursor.description]
        dl_df.columns = columns
        
        cols = {}
        
        for each_col in dl_df.columns:
            cols[each_col] = each_col.lower()
            
        dl_df = dl_df.rename(columns=cols)
        return dl_df

    def get_rs_df_insto(rs_q, user_, password_, host_,server_=''):
        if rs_q is None:
            return pd.DataFrame()
        if server_ not in ['SAM','TTG']:
            print('wrong server name')
            return pd.DataFrame()
        else:
            if server_ == 'SAM':
                database_='sam_live'
            if server_ == 'TTG':
                database_='ttg_live' 
            try:  
                mydb = mysql.connector.connect(
                host=host_,
                user=user_,
                password=password_,
                database=database_)
                mycursor = mydb.cursor()
                mycursor.execute(rs_q)
                columns = [i[0] for i in mycursor.description]
                result = mycursor.fetchall()
                dl_rs = pd.DataFrame(result)
                dl_rs.columns = columns
                dl_rs['server'] = database_
                
                    

                cols = {}
                
                for each_col in dl_rs.columns:
                    cols[each_col] = each_col.lower()
                    
                dl_rs = dl_rs.rename(columns=cols)
            except:
                return pd.DataFrame()


        return dl_rs

    def get_rs_df(rs_q, user_, password_, host_, num_, server_=''):
        if rs_q is None:
            return pd.DataFrame()

        dl_rs = pd.DataFrame()
        if num_=='':
                print('error: need total number of server')
        else:
            if server_ == '':
                for i in range(1,int(num_)+1):
                    mydb = mysql.connector.connect(
                    host=host_,
                    user=user_,
                    password=password_,
                    database=f"tm_live_" + str(i))
                    mycursor = mydb.cursor()
                    mycursor.execute(rs_q)
                    columns = [i[0] for i in mycursor.description]
                    result = mycursor.fetchall()
                    df = pd.DataFrame(result)
                    try:
                        df.columns = columns
                        df['server'] = f'Live0{i}'
                        dl_rs = pd.concat([dl_rs,df])
                        
                    except:
                        return pd.DataFrame()
                cols = {}
                        
                for each_col in dl_rs.columns:
                    cols[each_col] = each_col.lower()
                    
                dl_rs = dl_rs.rename(columns=cols)
            else:
                try:
                    mydb = mysql.connector.connect(
                    host=host_,
                    user=user_,
                    password=password_,
                    database=f"tm_live_{server_}")
                    mycursor = mydb.cursor()
                    mycursor.execute(rs_q)
                    columns = [i[0] for i in mycursor.description]
                    result = mycursor.fetchall()
                    dl_rs = pd.DataFrame(result)
                    dl_rs.columns = columns
                    dl_rs['server'] = f'Live0{server_}'
                    cols = {}
            
                    for each_col in dl_rs.columns:
                        cols[each_col] = each_col.lower()
                        
                    dl_rs = dl_rs.rename(columns=cols)
                except:
                        return pd.DataFrame()
            
        return dl_rs




