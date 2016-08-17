from aiohttp import web
import sru_utils.controllers.util as utilCtrl
import logging


logger = logging.getLogger(__name__)


params = [
    'action',
    'action_params'
]


async def util(request):
    data = await request.json()
    if all(k in params for k in data.keys()):
        data.setdefault('action_params',{}) # set value if non provided
        action = getattr(utilCtrl, data['action'], utilCtrl.not_found)
        res = action(**data['action_params'])
        return res
    else:
        return web.Response(text="an invalid param was found in request")#
