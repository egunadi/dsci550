# parser interface

import tika
tika.initVM()
from tika import parser
parsed = parser.from_file('/Users/egunadi/My Drive/dsci550/tika/testQueries.sql')
print(parsed["metadata"])
print(parsed["content"])