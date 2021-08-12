from pyflink.dataset import ExecutionEnvironment
from pyflink.table import TableConfig, DataTypes, BatchTableEnvironment
from pyflink.table.descriptors import Schema, OldCsv, FileSystem

# input_path = '/home/konglingwen/Desktop/pracSpace/prc_project/wordcount.input'
# output_path = '/home/konglingwen/Desktop/pracSpace/prc_project/output'

input_path = '/home/konglingwen/Desktop/pracSpace/prc_project/wordcount.csv'
output_path = '/home/konglingwen/Desktop/pracSpace/prc_project/output.csv'

exec_env = ExecutionEnvironment.get_execution_environment()
exec_env.set_parallelism(1)
t_config = TableConfig()
t_env = BatchTableEnvironment.create(exec_env, t_config)

t_env.connect(FileSystem().path(input_path)) \
    .with_format(OldCsv()
                 .line_delimiter(',')
                 .field('word', DataTypes.STRING())) \
    .with_schema(Schema()
                 .field('word', DataTypes.STRING())) \
    .create_temporary_table('mySource')

t_env.connect(FileSystem().path(output_path)) \
    .with_format(OldCsv()
                 .field_delimiter(',')
                 .field('word', DataTypes.STRING())
                 .field('count', DataTypes.BIGINT())) \
    .with_schema(Schema()
                 .field('word', DataTypes.STRING())
                 .field('count', DataTypes.BIGINT())) \
    .create_temporary_table('mySink')

t_env.from_path('mySource') \
    .group_by('word') \
    .select('word, count(1)') \
    .insert_into('mySink')

t_env.execute("tutorial_job")
