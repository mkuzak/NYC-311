NYC 311 data set is a good example of large tabular data file that is difficult to analyse at the first sight.
It will fail to open in Excell. Also opening whole file at once in Python with fail.

The goal is to explore dataset from the command line: checking number of rows, kind of columns etc.
Afterwards using python to load data by chunks into sqlite database and when loaded, use sql queries to explore it and visualise.
