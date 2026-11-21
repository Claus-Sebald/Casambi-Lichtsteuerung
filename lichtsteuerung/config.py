"""Konfiguration ausschließlich über Umgebungsvariablen.

Es werden hier bewusst keine Geheimnisse (API-Schlüssel, Passwörter) mit
Standardwerten hinterlegt. Adapter-spezifische Variablen kommen später hinzu,
sobald die Adapter implementiert werden (siehe .env.example).
"""

import os
from dataclasses import dataclass

_TRUE = {"1", "true", "yes", "on", "ja"}
_FALSE = {"0", "false", "no", "off", "nein"}


def _env_bool(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    value = raw.strip().lower()
    if value in _TRUE:
        return True
    if value in _FALSE:
        return False
    raise ValueError(f"Ungültiger Wahrheitswert für {name}: {raw!r}")


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None or raw.strip() == "":
        return default
    try:
        return int(raw)
    except ValueError:
        raise ValueError(f"Ungültige Zahl für {name}: {raw!r}") from None


@dataclass(frozen=True)
class Settings:
    host: str
    port: int
    log_level: str
    # Simulationsmodus: Standardmäßig AN, damit nie versehentlich echte
    # Hardware angesprochen wird.
    simulation: bool
    hue_enabled: bool
    casambi_evolution_enabled: bool
    casambi_classic_enabled: bool


def load_settings() -> Settings:
    return Settings(
        host=os.environ.get("LICHT_HOST", "127.0.0.1"),
        port=_env_int("LICHT_PORT", 8000),
        log_level=os.environ.get("LICHT_LOG_LEVEL", "info").lower(),
        simulation=_env_bool("LICHT_SIMULATION", True),
        hue_enabled=_env_bool("HUE_ENABLED", False),
        casambi_evolution_enabled=_env_bool("CASAMBI_EVOLUTION_ENABLED", False),
        casambi_classic_enabled=_env_bool("CASAMBI_CLASSIC_ENABLED", False),
    )
