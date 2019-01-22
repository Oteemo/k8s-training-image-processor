from datetime import datetime

def get():
  retval = { "status":"Service is up","date": str(datetime.utcnow()) }
  return retval, 200