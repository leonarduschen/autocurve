import os
from autocurve import pipe

cwd = os.path.dirname(__file__)
fpath = os.path.join(cwd, 'example', 'arctic-monkeys-am.png')

pipe(fpath)
