from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

address = "/home/konglingwen/Desktop/pracSpace/prc_project/"
# df = spark.read.json("/home/konglingwen/Desktop/pracSpace/prc_project/examples/src/main/resources/people.json")
# # Displays the content of the DataFrame to stdout
# df.show()
#
# df.printSchema()
# df.select(df['name'], df['age'] + 1).show()


from pyspark.sql import Row

sc = spark.sparkContext

# Load a text file and convert each line to a Row.
lines = sc.textFile(address + "examples/src/main/resources/people.txt")
parts = lines.map(lambda l: l.split(","))
print('********', parts)

people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

# Infer the schema, and register the DataFrame as a table.
schemaPeople = spark.createDataFrame(people)
schemaPeople.createOrReplaceTempView("people")

# SQL can be run over DataFrames that have been registered as a table.
teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# The results of SQL queries are Dataframe objects.
# rdd returns the content as an :class:`pyspark.RDD` of :class:`Row`.
teenNames = teenagers.rdd.map(lambda p: "Name: " + p.name).collect()
for name in teenNames:
    print(name)
# Name: Justin
