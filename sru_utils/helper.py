import subprocess
import json

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

def jsonify(data, **kw):
    """ takes dictionary and converts to json, can add values to dict using kw
    """
    try:
        if len(kw.keys()) > 0:
            data.update(kw)
        return json.dumps(data)
    except Exception as e:
        print('we have Exception in jsonify', str(e))


def encode(data, encode="utf-8", json=False, **kw):
    if json:
        output = jsonify(data, **kw).encode(encode)
    else:
        output = data.encode(encode)
    return output