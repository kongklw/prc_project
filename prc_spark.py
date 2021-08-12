import sys
from operator import add
from pyspark import SparkContext
from pyspark.shell import spark
from pyspark.sql.functions import *
# sc = SparkContext()
#
# lines = sc.textFile('storm.csv')
# counts = lines.flatMap(lambda x: x.split(',')).map(lambda x: (x, 1)).reduceByKey(add)
# output = counts.collect()
# output = filter(lambda x: not x[0].isnumeric(), sorted(output, key=lambda x: x[1], reverse=True))
#
# for word, count in output[:10]:
#     print(word, count)

# 2
textFile = spark.read.text("README.md")

count = textFile.count()
print(count)



# a = textFile.select(size(split(textFile.value, "\s+")).name("numWords")).agg(max(col("numWords"))).collect()