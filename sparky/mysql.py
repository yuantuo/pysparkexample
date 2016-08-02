"""
    mysql connector to retrieve table data
"""
def mysql_get_table(sqlContext, args, database, tablename):

    return sqlContext.read.format('jdbc') \
                .option('url', 'jdbc:mysql://localhost/' + database) \
                .option("driver", "com.mysql.jdbc.Driver") \
                .option('dbtable', tablename) \
                .option('user', args.mysql_user) \
                .option('password', args.mysql_password) \
                .load(encoding='utf-8')

