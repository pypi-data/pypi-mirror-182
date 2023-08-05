__version__ = '0.1.0'
from datetime import datetime




def log(msg):
    is_now = datetime.now()
    global last
    last_interval = is_now - last
    last = is_now
    output = ' '.join([msg, "... is now", str(is_now),
                      "... last interval", str(last_interval)])
    print(output)
    write(output)


def write(output, filename='log.'+str(datetime.now())):
    f = open(filename, 'a')
    f.write(output+'\n')
    f.close()


last = datetime.now()
log("Started script",)
