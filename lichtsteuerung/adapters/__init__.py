"""Adapter für die einzelnen Lichtsysteme.

Jedes Lichtsystem bekommt ein eigenes Unterpaket. Die Steuerung ist noch
NICHT implementiert – es wird keinerlei Verbindung zu echter Hardware
aufgebaut.
"""

ADAPTERS = {
    "hue": {"label": "Philips Hue (Bridge, API v2)", "implemented": False},
    "casambi_evolution": {"label": "Casambi Evolution", "implemented": False},
    "casambi_classic": {"label": "Casambi Classic", "implemented": False},
}
