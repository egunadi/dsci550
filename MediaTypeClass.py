#!/usr/bin/env python
import tika
from tika import config
# print(config.getParsers())
# print(config.getMimeTypes())
# print(config.getDetectors())

import pandas as pd

parsers_json = config.getParsers()
parsers_list = pd.read_json(parsers_json).children.to_list()
parsers_df = pd.DataFrame(parsers_list)

# print(parsers_df.columns)
# print(parsers_df.info())

text_parser = parsers_df[parsers_df.name.str.contains('text', na=False, case=False)]
# print(text_parser.supportedTypes)

# OUTPUT
# [text/csv, text/tsv, text/plain]

mimetypes_json = config.getMimeTypes()
mimetypes_df = pd.read_json(mimetypes_json)

# print(mimetypes_df.columns)

"""
text_columns =  [   column
                    for column in mimetypes_df.columns
                    if 'text/plain' in column ]
print(text_columns)
"""

text_mimetype = mimetypes_df.loc[:, 'text/plain']

# print(text_mimetype)
"""OUTPUT
alias                                                 []
parser       org.apache.tika.parser.csv.TextAndCSVParser
supertype                                            NaN
"""
