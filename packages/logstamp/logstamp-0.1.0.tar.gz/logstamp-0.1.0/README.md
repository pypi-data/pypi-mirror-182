# logstamp

Another logger, made for data science and heavy-compute workloads. Logs to timestamped file too.

## Usage

```python3
from logstamp import log
import time
log("doing big thing")
time.sleep(3)
log("did big thing, doing other thing")
time.sleep(5)
log("all done")
```

## logs to file:

```Started script ... is now 2022-12-19 18:05:22.769841 ... last interval 0:00:00.000001
doing big thing ... is now 2022-12-19 18:05:22.769930 ... last interval 0:00:00.000089
did big thing, doing other thing ... is now 2022-12-19 18:05:25.773236 ... last interval 0:00:03.003306
all done ... is now 2022-12-19 18:05:30.778863 ... last interval 0:00:05.005627
```