from sqlalchemy import create_engine
from ..connections.redshift_credentials import initialize_redshift_credentials

def bulk_df_insert(df_toinsert, tablename, ifexists_method):

    redshift_credentials = initialize_redshift_credentials()
    session = create_engine('postgresql://'+redshift_credentials['user']+':'+redshift_credentials['password']+'@'+redshift_credentials['host']+'/'+redshift_credentials['database']+'')
    df_toinsert.to_sql(''+tablename+'', session, index=False, if_exists=''+ifexists_method+'')
    return print('Bulk insertion in DB')