import snowflake.connector
from pathlib import Path
import re

# get the DDL from the Snowflake table
ctx = snowflake.connector.connect(
    user='Philpo',
    password='***********',
    account='********.us-east-1'
    )
cs = ctx.cursor()

try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print("Snowflake Version: " + one_row[0])


#get the Snowflake DDL for the table

    #Snowflake_DDL_exec_str = cs.execute("SELECT REGEXP_REPLACE(get_ddl('table','MUSIC_SALES.PUBLIC.TIME'),'[^a-zA-Z0-9()_,;]+' );")
    Snowflake_DDL_exec_str = cs.execute("SELECT get_ddl('table','MUSIC_SALES.PUBLIC.TIME');")
    one_row = cs.fetchone()
    Snowflake_formatted_DDL = one_row[0]
    Snowflake_unformatted_DDL = re.sub('\s+','',Snowflake_formatted_DDL)
    print(Snowflake_unformatted_DDL)


#get the DDL from the git managed DDL File after the git pull

    local_DDL_file = open("C:\\Users\\philp\\Desktop\\More_dbt\\More_dbt\\LearnMoredbt\\Time.sql","r")
    formatted_local_DDL = local_DDL_file.read()
    unformatted_local_DDL = re.sub('\s+','',formatted_local_DDL)
    print(unformatted_local_DDL)

    if Snowflake_unformatted_DDL != unformatted_local_DDL:
        print('DDLs do not match')
    else:
        print('DDLs match!')

#prompt user for new attributes
    new_attrs = input('Enter New Attribute(s) With Data Type, Separated By Commas If More Than One' + '\n' + 'e.g., NEW_COL1 VARCHAR(10) NOT NULL, NEW_COL2 VARCHAR(10) NOT NULL' + '\n' + '\n')

#put some checking here to be sure DDL is valid

#drop the ETL columns (to be added back after new attrs)
    print('Dropping ETL Columns')
    Snowflake_DDL_exec_str = cs.execute("ALTER TABLE MUSIC_SALES.PUBLIC.TIME DROP COLUMN ETL_NR, ETL_TS;")

#add the new attribute(s) to the end of the table with the alter statement
    print('Adding New Attributes')
    Snowflake_DDL_add_new_attrs_str = "ALTER TABLE MUSIC_SALES.PUBLIC.TIME ADD COLUMN " + new_attrs + ";"
    print(Snowflake_DDL_add_new_attrs_str) 
    Snowflake_DDL_exec_str = cs.execute(Snowflake_DDL_add_new_attrs_str) 

#add the ETL columns back to table at the end
    print('Adding ETL Columns Back To Table')
    Snowflake_DDL_exec_str = cs.execute("ALTER TABLE MUSIC_SALES.PUBLIC.TIME ADD COLUMN ETL_NR NUMBER(38,0) NOT NULL,ETL_TS TIMESTAMP_NTZ(9) NOT NULL;")

 
finally:
    cs.close()
    #ct.close()
ctx.close()
