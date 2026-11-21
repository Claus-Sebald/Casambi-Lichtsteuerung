"""GET /api/health – Serverstatus als JSON."""

import platform
import time
from datetime import datetime, timezone

from fastapi import APIRouter, Request

from .. import __version__
from ..adapters import ADAPTERS

router = APIRouter(tags=["system"])

_STARTED = time.monotonic()


@router.get("/health")
def health(request: Request) -> dict:
    settings = request.app.state.settings
    enabled = {
        "hue": settings.hue_enabled,
        "casambi_evolution": settings.casambi_evolution_enabled,
        "casambi_classic": settings.casambi_classic_enabled,
    }
    return {
        "status": "ok",
        "app": "Lichtsteuerung",
        "version": __version__,
        "simulation": settings.simulation,
        "time": datetime.now(timezone.utc).isoformat(),
        "uptime_seconds": round(time.monotonic() - _STARTED, 1),
        "python": platform.python_version(),
        "adapters": {
            name: {
                "label": info["label"],
                "enabled": enabled[name],
                "implemented": info["implemented"],
            }
            for name, info in ADAPTERS.items()
        },
    }
