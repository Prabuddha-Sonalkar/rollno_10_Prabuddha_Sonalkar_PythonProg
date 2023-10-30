import os
import datetime as dt
print("last accessed time",os.path.getatime("E:/Aditi"))
print("last modified time",os.path.getmtime("E:/Aditi"))
# access_time=dt.timestamp(os.path.getatime("E:/Aditi"))
