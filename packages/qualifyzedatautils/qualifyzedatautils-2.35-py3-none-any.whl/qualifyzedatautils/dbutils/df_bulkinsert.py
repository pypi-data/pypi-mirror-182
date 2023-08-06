from sqlalchemy import create_engine
from ..connections.redshift_credentials import initialize_redshift_credentials

#def bulk_df_insert(df_toinsert, schema, tablename, ifexists_method):
def bulk_df_insert():
    redshift_credentials = initialize_redshift_credentials()
    print(redshift_credentials['host'])
    #session = create_engine('postgresql://'+redshift_credentials['user']+':'+redshift_credentials['password']+'@'+redshift_credentials['host']+':5439/'+redshift_credentials['database']+'')
    #df_toinsert.to_sql(''+tablename+'', session, index=False, schema=''+schema+'',  if_exists=''+ifexists_method+'')
    return print('Bulk insertion in DB')