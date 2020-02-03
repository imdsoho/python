from collections import ChainMap

import builtins
#pylookup = ChainMap(locals(), globals(), vars(builtins))
pylookup = ChainMap(vars())

for data in pylookup:
    print(data, " : ", pylookup[data])