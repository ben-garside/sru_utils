from . import controllers as Ctrl
from aiohttp.web import Response
import logging

log = logging.getLogger(__name__)

async def util(request):
    data = await request.json()
    if "action" in data:
        action = getattr(Ctrl, data["action"])
        data.setdefault("action_param", {})
        result = action(**data["action_param"])
        return result
