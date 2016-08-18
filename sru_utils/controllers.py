from aiohttp.web import Response
from .helper import encode
import platform
from datetime import datetime

def not_found(**kw):
    msg = {
        "message": "invalid Action requested",
        "code": 404
    }

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def heart_beat(**kw):
    msg = {
        "message": "Host is up and well",
        "code": 200,
        "host": platform.node(),
        "time": datetime.now().__str__(),
        # "version": SRU_VERSION
    }

    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def functions(**kw):
    msg = {
        "message": "All available actions to this machine",
        "code": 200,
        "actions": {
            "util": [
                "heart_beat",
                "functions"
            ]
        }
    }
    output = encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def cmd(**kw):
    output = {}
    if "cmd" in kw.keys():
        logger.debug(kw["cmd"])
        res = run(kw['cmd'])
        if res:
            msg = {
                "code": 200,
                "output": res
            }
        else:
            msg = {
                "code": 500,
                "output": "ERROR"
            }
        output = encode(msg, json=True)
    if "raw" in kw and kw["raw"] == True:
        return Response(text=res)
    return Response(body=output, content_type="application/json")