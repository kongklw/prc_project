import pandas as pd
import numpy as np

# df = pd.DataFrame(np.random.randn(10, 4))
# print(df)
#
# pieces = [df[:3], df[5:7], df[7:]]

# print(pieces)
# print(df[:3])
# print(df[3:7])
# print(df[7:])

# df2 = pd.concat(pieces)
# print(df2)

# df = pd.DataFrame({"Let": ["A", "B", "C"], "Num": [1, 2, 3]})
#
# ser = pd.Series(["a", "b", "c", "d", "e", "f"],
#                 index=pd.MultiIndex.from_arrays([["A", "B", "C"] * 2, [1, 2, 3, 4, 5, 6]], names=["Let", "Num"]), )
# print(df)
# print(ser)
#
# # df2 = pd.merge(df,ser,how='left'
# print(ser.reset_index())


df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})

# print(df)
# grouped = df.groupby('A')
# print(grouped.sum())
# grouped = df.groupby(['A', 'B'])
# print(grouped.sum())


df2 = df.set_index(['A', 'B'])
print(df2)
print(df2.index)

grouped = df2.groupby(level=df2.index.names.difference(['B']))
print(grouped.sum())


def get_letter_type(letter):
    if letter.lower() in 'aeiou':
        return 'vowel'
    else:
        return 'consonant'


grouped = df.groupby(get_letter_type, axis=1)
print(grouped.boxplot)
print(grouped.sum())
