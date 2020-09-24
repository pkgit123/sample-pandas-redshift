import pandas_redshift as pr
import pandas as pd

# put secrets.py in .gitignore file to avoid pushing to git by mistake
import secrets    # secrets.py

# Redshift database connection engine
str_dbname = secrets.str_dbname
str_host = secrets.str_host
str_port = secrets.str_port
str_user = secrets.str_user
str_pw = secrets.str_pw

# s3 configurations
str_accesskeyid = secrets.str_accesskeyid
str_secretaccesskey = secrets.str_secretaccesskey
str_s3bucket = secrets.str_s3bucket
str_s3subdirectory = secrets.str_s3subdirectory

# delete secrets.py
del secrets

# create pandas-redshift connection
pr.connect_to_redshift(dbname = str_dbname,
                        host = str_host,
                        port = str_port,
                        user = str_user,
                        password = str_pw)

# create dataframe from redshift query
sql_query = "SELECT * FROM <database>.<schema>.<table>;"
df = pr.redshift_to_pandas(sql_query)

print("Shape of dataframe: ", df.shape)

# create sample dataframe for upload
df_upload = pd.DataFrame({
    'a_col': ['red', 'green', 'blue'],
    'b_col': [1, 2, 3],
    'c_col': [True, False, True],
    'd_col': ['2020-01-01', '2020-02-04', '2020-03-06'],
})

# =============================================================
# Write a pandas DataFrame to redshift. Requires access to an S3 bucket and previously running pr.connect_to_redshift.
# If the table currently exists IT WILL BE DROPPED and then the pandas DataFrame will be put in it's place.
# If you set append = True the table will be appended to (if it exists).
# =============================================================

# Connect to S3
pr.connect_to_s3(aws_access_key_id = str_accesskeyid,
                aws_secret_access_key = str_secretaccesskey,
                bucket = str_s3bucket,
                subdirectory = str_s3subdirectory
                # As of release 1.1.1 you are able to specify an aws_session_token (if necessary):
                # aws_session_token = <aws_session_token>
                )

# Write the DataFrame to S3 and then to redshift
str_schema_table = '<schema>.<table>'
pr.pandas_to_redshift(data_frame = df_upload,
                      redshift_table_name = str_schema_table)

# confirm that the table has been uploaded to Redshift by reading
pr.connect_to_redshift(dbname = str_dbname,
                        host = str_host,
                        port = str_port,
                        user = str_user,
                        password = str_pw)
sql_confirm = "SELECT * FROM <database>.<schema>.<table>;"
df_confirm = pr.redshift_to_pandas(sql_confirm)

print("Shape of dataframe: ", df_confirm.shape)

# close pandas_redshift connection
pr.close_up_shop()
