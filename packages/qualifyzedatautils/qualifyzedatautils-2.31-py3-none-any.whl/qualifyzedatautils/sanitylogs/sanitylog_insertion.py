from datetime import datetime
import redshift_connector

def post_sanitylog( redshift_valid_connection, type, source, affected, response="" ):

    insertion_ts = datetime.now()

    print(12345)

    cursor_sanitylog = redshift_valid_connection.cursor()
    cursor_sanitylog.execute('INSERT INTO dev.sanity_logs (type, source, affected, response, log_ts) VALUES (%s, %s, %s, %s, %s)', (type, source, affected, response, insertion_ts))
    cursor_sanitylog.close()
    redshift_valid_connection.commit()

    return print(123456)