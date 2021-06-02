import math
import os
import random
import re
import sys
from datetime import datetime as dt
# Complete the time_delta function below.
def time_delta(t1, t2):
    Tformat = '%a %d %b %Y %H:%M:%S %z'
    t1 = dt.strptime(t1, Tformat)
    t2 = dt.strptime(t2, Tformat)
    print(int(abs((t1-t2).total_seconds())))

time_delta('Sun 10 May 2015 13:54:36 -0700','Sun 10 May 2015 13:54:36 -0000')