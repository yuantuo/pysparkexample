from pyspark import SparkConf, SparkContext, StorageLevel
from pyspark.sql import SQLContext, Row

from optparse import OptionParser
from datetime import date
import sys
import os
import mysql


def main(args):

    conf = SparkConf().setAppName("S3 Example").set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    todaydate = date.today()

    user_count_path = os.path.join('spark', 'data', 'parquet', '*', '*', '*', 'user_comany_count')
    company_list_path = os.path.join('spark', 'data', 'parquet', '*', '*', '*', 'company')


    output_file = os.path.join('/', 'user', 'tokluo', 'spark', 'data', 'parquet', todaydate.strftime('%Y'),
                                                                                  todaydate.strftime('%m'),
                                                                                  todaydate.strftime('%d'))





    raw_companies_df = mysql.mysql_get_table(sqlContext, args, 'loyalfour_development', 'companies')
    company = raw_companies_df.select('id', 'name', 'created_at')

    raw_users_df = mysql.mysql_get_table(sqlContext, args, 'loyalfour_development', 'users')
    user = raw_users_df.select(raw_users_df.id.alias("users_id"), 'email', 'firstname', 'lastname', 'current_sign_in_at', 'confirmation_sent_at')

    raw_users_companies_df = mysql.mysql_get_table(sqlContext, args, 'loyalfour_development', 'users_companies')
    user_companies = raw_users_companies_df.select('user_id', 'company_id')

    df = company.join(user_companies, company.id == user_companies.company_id).join(user, user_companies.user_id == user.users_id)

    df.write.parquet(os.path.join(os.path.join(output_file, 'company')), mode='overwrite')
    count = df.select('name', 'email').groupby('name').count()
    count.write.parquet(os.path.join(os.path.join(output_file, 'user_comany_count')), mode='overwrite')



    user_count = sqlContext.read.parquet(user_count_path)
    # user_count.show()
    for i in user_companies.collect():
        print i

    company_list = sqlContext.read.parquet(company_list_path)
    for i in company_list.collect():
        print i
    # company_list.show()

    print(company_list[company_list.confirmation_sent_at.isNotNull()].count())

    sc.stop()

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('--mysql_user')
    parser.add_option('--mysql_password')
    (options, args) = parser.parse_args()
    main(options)
