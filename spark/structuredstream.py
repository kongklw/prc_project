from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, window
from pyspark.sql.functions import split
from pyspark.sql.types import StructType

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

sc = spark.sparkContext
#
# lines = spark \
#     .readStream \
#     .format("socket") \
#     .option("host", "localhost") \
#     .option("port", 9999) \
#     .load()
#
# # lines = spark.readStream.format("socket").option("host", "localhost").option("port", 3000).load()
# print('************************', lines)
# # Split the lines into words
# words = lines.select(
#     explode(
#         split(lines.value, " ")
#     ).alias("word")
# )
#
# wordCounts = words.groupby("word").count()
# print('************************', wordCounts)
#
# query = wordCounts \
#     .writeStream \
#     .outputMode('complete') \
#     .format('console') \
#     .start()
# print(query)
# query.awaitTermination()


# Read text from socket
socketDF = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

socketDF.isStreaming()  # Returns True for DataFrames that have streaming sources

socketDF.printSchema()

# Read all the csv files written atomically in a directory
userSchema = StructType().add("name", "string").add("age", "integer")
csvDF = spark \
    .readStream \
    .option("sep", ";") \
    .schema(userSchema) \
    .csv("/path/to/directory")  # Equivalent to format("csv").load("/path/to/directory")

# 事件时间窗口操作。
words = ...  # streaming DataFrame of schema { timestamp: Timestamp, word: String }

# Group the data by window and word and compute the count of each group
windowedCounts = words.groupBy(
    window(words.timestamp, "10 minutes", "5 minutes"),
    words.word
).count()
