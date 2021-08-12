from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext(master="local[*]", appName='stream_context')
ssc = StreamingContext(sc, 5)


"""
定义上下文后，您必须执行以下操作。
    通过创建输入DStream定义输入源。
    通过将转换和输出操作应用于DStream来定义流计算。
    开始接收数据并使用进行处理streamingContext.start()。
    等待使用停止处理（手动或由于任何错误）streamingContext.awaitTermination()。
    可以使用手动停止处理streamingContext.stop()。

"""



