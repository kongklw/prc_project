from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName('kong').setMaster('local')

sc = SparkContext(conf=conf)

data = [1, 2, 3, 4, 5, 6, 7]
distData = sc.parallelize(data)
print(distData.reduce(lambda x, y: x + y))
# print('distData', distData)
# aim = distData.reduce(lambda x, y: x + y)
# print('aim', aim)

# a = distData.max()
# print(a)
# b = distData.filter(3)
# print(b)
# vals = distData.values()
# print(vals)
#
# name = distData.name()
# sum = distData.sum()
# count = distData.count()
# cache = distData.cache()
# print(name,sum,count,cache)

distFile = sc.textFile('data.txt')

aim = distFile.map(lambda s: len(s)).reduce(lambda a, b: a + b)
print(aim)


# lines = sc.textFile("data.txt")
# lineLengths = lines.map(lambda s: len(s))
# print(lineLengths)
# totalLength = lineLengths.reduce(lambda a, b: a + b)
# print(totalLength)
