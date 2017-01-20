import tensorflow as tf

import sys


task_index = int(sys.argv[1])


cluster =  tf.train.ClusterSpec({"worker":
    ["10.200.131.57:12222",
    "10.200.131.57:12223",
    "10.200.131.56:12224"]})

server = tf.train.Server(cluster,job_name="worker",task_index=task_index)
server.join()
