#! python3
# json_date_time_enc serializes a datetime object for JSON encoding

import datetime
import json

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self,obj)

