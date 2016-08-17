from aiohttp.web import Response
from sru.helpers import controller as hc
from sru.conf.settings import SRU_VERSION
import subprocess
import schtasks_shim as schtasks
import logging


logger = logging.getLogger(__name__)


def not_found(**kw):
    msg = {
        "message": "invalid Action requested",
        "code": 404
    }

    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")

def heart_beat(**kw):
    import platform
    from datetime import datetime
    msg = {
        "message": "Host is up and well",
        "code": 200,
        "host": platform.node(),
        "time": datetime.now().__str__(),
        "version": SRU_VERSION
    }

    output = hc.encode(msg, json=True)
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
    output = hc.encode(msg, json=True)
    return Response(body=output, content_type="application/json")


def run(cmd, errMsg=None):
    """ run given commands in a subprocess
    """
    try:
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = proc.communicate()
        if type(output) == bytes:
            output = output.decode(encoding='UTF-8')
        logger.debug("Output: {}".format(output))
        logger.debug("Return Code: {}".format(proc.returncode))
        if "[Error]" in output or proc.returncode != 0:
            logger.debug("errMsg: {}".format(errMsg))
            logger.debug("err: {}".format(err))
            if errMsg:
                return errMsg
            else:
                return "%s\r\n%s" % (output, err.decode("utf-8"))
        return output
    except Exception as e:
        logger.error("Exception running 'run': {}".format(e))
        return None


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
        output = hc.encode(msg, json=True)
    if "raw" in kw and kw["raw"] == True:
        return Response(text=res)
    return Response(body=output, content_type="application/json")
    # return Response(text=res)