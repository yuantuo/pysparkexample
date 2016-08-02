# To run this code:
#
# % spark-submit \
#    --py-files sparky/dataIO.py,sparkey/features.py \
#    --master local[*] \
#    sparky/example.py

from pyspark import SparkConf, SparkContext, StorageLevel
from pyspark.sql import SQLContext, Row

import sys
import dataIO
import features

# class Foo():
#
#     def print_me(self):
#         print('print from foo class')

def main(dataFile, outputPath):

    conf = SparkConf().setAppName("S3 Example").set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    raw_text = sc.textFile(dataFile).persist(StorageLevel.MEMORY_AND_DISK)

    csv_data = raw_text.map(lambda l: l.split(","))
    row_data = csv_data.map(lambda p: dataIO.dataStruc(p))

    interaction_df = sqlContext.createDataFrame(row_data)

    # features.save_hdfs_parquet(interaction_df, outputPath)
    dataIO.save_hdfs_parquet(interaction_df, outputPath)

    interaction_df.registerTempTable("interactions")

    tcp_interactions = sqlContext.sql( """
        SELECT duration, dst_bytes, protocol_type FROM interactions WHERE protocol_type = 'tcp' AND duration > 1000 AND dst_bytes=0
    """)

    tcp_interactions.show()

    features.print_tcp_interactions(tcp_interactions)
    dataIO.print_from_dataio()
    features.print_from_feature()

    sc.stop()


def read_parquet(input_path):

    conf = SparkConf().setAppName("S3 Example").set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    # df = features.load_hdfs_parguet(sqlContext, input_path)
    df = dataIO.load_hdfs_parguet(sqlContext, input_path)
    df.show()
    # obj = Foo()
    # obj.print_me()

if __name__ == '__main__':

    dataFile = sys.argv[1]
    # outputPath = sys.argv[2]
    # main(dataFile, outputPath)
    read_parquet(dataFile)