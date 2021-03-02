import snowflake.connector
import subprocess
from pathlib import Path
import re
import sys

# get the DDL from the Snowflake table
ctx = snowflake.connector.connect(
    user='',
    password='',
    account='taa42050.us-east-1'
    )
cs = ctx.cursor()

try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print("Snowflake Version: " + one_row[0])



#git pull
    print('Performing git pull...')
    subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE).stdout

#get the Snowflake DDL for the table
    
    Snowflake_DDL_exec_str = cs.execute("SELECT get_ddl('table','MUSIC_SALES.PUBLIC.TIME');")
    one_row = cs.fetchone()
    Snowflake_formatted_DDL = one_row[0]
    Snowflake_unformatted_DDL = re.sub('\s+','',Snowflake_formatted_DDL)
    print('Unformatted Snowflake DDL: ' + '\n' + '--------------------------' + '\n' + Snowflake_unformatted_DDL + '\n' + '\n')


#get the DDL from the git managed DDL File after the git pull

    local_DDL_file = open("C:\\Users\\philp\\Desktop\\More_dbt\\More_dbt\\LearnMoredbt\\Time.sql","r")
    formatted_local_DDL = local_DDL_file.read()
    unformatted_local_DDL = re.sub('\s+','',formatted_local_DDL)
    print('Unformatted Local Git DDL: ' + '\n' + '--------------------------' + '\n' + unformatted_local_DDL + '\n' + '\n')

    if Snowflake_unformatted_DDL != unformatted_local_DDL:
        DDL_match = 'N'
        print('DDLs Do Not Match. Exiting Program.')
        quit()
    else:
        DDL_match = 'Y'
        print('DDLs Match!')
       

#prompt 
    Continue_To_Snowflake_ALTER = input('Continue to ALTER Snowflake Table And Push To Git? Y/N' + '\n')

    if Continue_To_Snowflake_ALTER == 'N':
        print('You Have Opted Not To Continue')
        quit()
    else:
        print('Continuing...')
    

#prompt user for new attributes
    new_attrs = input('Enter New Attribute(s) With Data Type, Separated By Commas If More Than One' + '\n' + 'e.g., NEW_COL1 VARCHAR(10) NOT NULL, NEW_COL2 VARCHAR(10) NOT NULL' + '\n' + '\n')

#put some checking here to be sure DDL is valid

#drop the ETL columns (to be added back after new attrs)
    print('Dropping ETL Columns')
    Snowflake_DDL_exec_str = cs.execute("ALTER TABLE MUSIC_SALES.PUBLIC.TIME DROP COLUMN ETL_NR, ETL_TS;")

#add the new attribute(s) to the end of the table with the alter statement
    print('Adding New Attributes...')
    Snowflake_DDL_add_new_attrs_str = "ALTER TABLE MUSIC_SALES.PUBLIC.TIME ADD COLUMN " + new_attrs + ";"
    print(Snowflake_DDL_add_new_attrs_str) 
    Snowflake_DDL_exec_str = cs.execute(Snowflake_DDL_add_new_attrs_str) 
    print('New Attributes Successfully Added To Table.')

#add the ETL columns back to table at the end
    print('Adding ETL Columns Back To Table...')
    Snowflake_DDL_exec_str = cs.execute("ALTER TABLE MUSIC_SALES.PUBLIC.TIME ADD COLUMN ETL_NR NUMBER(38,0) NOT NULL,ETL_TS TIMESTAMP_NTZ(9) NOT NULL;")
    print('ETL Columns Successfully Added Back To Table.')

#get DDL from Snowflake now that alterations are done
    print('Getting Altered Snowflake DDL...')
    Snowflake_DDL_exec_str = cs.execute("SELECT get_ddl('table','MUSIC_SALES.PUBLIC.TIME');")
    one_row = cs.fetchone()
    Snowflake_formatted_DDL = one_row[0]


#write the new Snowflake DDL back to local git-managed file
    print('Writing New DDL to Local Git File...')
    local_DDL_file = open("C:\\Users\\philp\\Desktop\\More_dbt\\More_dbt\\LearnMoredbt\\Time.sql","r+")
    local_DDL_file.truncate(0)
    local_DDL_file.write(Snowflake_formatted_DDL)
    local_DDL_file.close
    print('New DDL Successfully Written to Local Git File.')

#now git add, commit and push to remote git repo
    git_commit_message = input('Enter git commit message (no quotes, no -m):' +'\n')
    git_commit_message = "-m " + git_commit_message 

    print('Performing git add...')
    subprocess.run(["git", "add -A"], check=True, stdout=subprocess.PIPE).stdout
    print('git add complete.')    

    print('Performing git commit...')
    subprocess.run(["git", "commit", git_commit_message], check=True, stdout=subprocess.PIPE).stdout
    print('git commit complete.')

    print('Performing git push...')
    subprocess.run(["git", "push", "origin", "master"], check=True, stdout=subprocess.PIPE).stdout
    print('git push complete.')


finally:
    cs.close()
    #ct.close()
ctx.close()
