from typing import List

from gcptool.inventory.cache import Cache, parse_model_cache, with_cache

from . import api
from .types import BackendService


@with_cache("compute", "backend_services")
def __all(project_id: str):
    return api.backend_services.list(project=project_id).execute().get("items", [])


def all(project_id: str, cache: Cache) -> List[BackendService]:
    return [
        parse_model_cache(backend_service, BackendService)
        for backend_service in __all(cache, project_id)
    ]
