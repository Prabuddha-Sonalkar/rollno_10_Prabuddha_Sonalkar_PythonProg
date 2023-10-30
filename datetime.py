import os
import datetime as dt
print("last accessed time",os.path.getatime("E:/TY_10"))
print("last modified time",os.path.getmtime("E:/Ty_10"))
# access_time=dt.timestamp(os.path.getatime("E:/TY_10"))
