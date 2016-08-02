def print_from_feature():
    print('print from features')

def print_tcp_interactions(df):
    tcp_interactions_out = df.map(lambda p: "Duration: {}, Dest, bytes {}, protocol_type {}".format(p.duration, p.dst_bytes, p.protocol_type))
    for out in tcp_interactions_out.collect():
        print out

