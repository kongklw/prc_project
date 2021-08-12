from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# 创建两个线程和1秒批处理的 stream context
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 3)

# 输入数据socket 监听数据作为输入源
lines = ssc.socketTextStream("localhost", 9999)

# flatMap是一对多DStream操作，它通过从源DStream中的每个记录生成多个新记录来创建新的DStream。
# 在这种情况下，每行将拆分为多个单词，单词流表示为 wordsDStream。接下来，我们要计算这些单词。
words = lines.flatMap(lambda line: line.split(" "))
print('************', words)

pairs = words.map(lambda word: (word, 1))
wordCount = pairs.reduceByKey(lambda x, y: x + y)

wordCount.pprint()

ssc.start()
ssc.awaitTermination()
