from pyspark.sql import Row

@staticmethod
def print_from_dataio():
    print('from data io')
    return 'hello123'

@staticmethod
def dataStruc(p):

    """
        some validation of data is usefully here:

        match = re.search(APACHE_ACCESS_LOG_PATTERN, p)

        if match is None:
            raise Error("Invalid logline: %s" % logline)
    """
    return Row(
        duration=int(p[0]),
        protocol_type=p[1],
        service=p[2],
        flag=p[3],
        src_bytes=int(p[4]),
        dst_bytes=int(p[5])
    )

@staticmethod
def save_hdfs_parquet(df, path):
    df.save(path)
    # df.write.format("parquet").save('hdfs:///user/tokluo/spark/data/foo.parquet', mode="append")

@staticmethod
def load_hdfs_parguet(sc, path):
    return sc.read.parquet(path)

