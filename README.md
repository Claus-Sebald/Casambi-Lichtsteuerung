# Lichtsteuerung

Lokale Lichtsteuerung für **Philips Hue** (Bridge, API v2), **Casambi Evolution**
und **Casambi Classic**, mit einer Weboberfläche für Browser, Tablet und Smartphone.

> **Stand 0.1.0:** Grundgerüst. Es werden **keine** echten Leuchten angesprochen.
> Die Adapter sind nur als leere Pakete vorbereitet.

## Voraussetzungen

- macOS oder Linux
- Python **3.9 oder neuer** (empfohlen: 3.11+; Python 3.9 erhält seit Okt. 2025 keine Sicherheitsupdates mehr)

## Installation

```bash
cd /pfad/zu/Lichtsteuerung
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt          # Betrieb
pip install -r requirements-dev.txt      # zusätzlich für Tests (pytest, httpx)
```

## Starten

```bash
source .venv/bin/activate
python -m lichtsteuerung
```

Danach im Browser öffnen:

| Adresse | Inhalt |
|---|---|
| http://127.0.0.1:8000/ | Startseite |
| http://127.0.0.1:8000/api/health | Serverstatus (JSON) |
| http://127.0.0.1:8000/docs | Automatische API-Dokumentation |

Beenden mit `Ctrl+C`.

### Zugriff von Tablet / Smartphone im Heimnetz

Standardmäßig lauscht der Server nur auf `127.0.0.1` (nur dieser Rechner).
Für den Zugriff aus dem Netz:

```bash
LICHT_HOST=0.0.0.0 python -m lichtsteuerung
```

und dann `http://<IP-des-Rechners>:8000/` aufrufen. macOS fragt evtl. einmalig nach
der Firewall-Freigabe für Python.

## Konfiguration

Ausschließlich über Umgebungsvariablen. Vorlage: [.env.example](.env.example).

```bash
cp .env.example .env        # .env wird nicht eingecheckt (.gitignore)
set -a; source .env; set +a
python -m lichtsteuerung
```

| Variable | Standard | Bedeutung |
|---|---|---|
| `LICHT_HOST` | `127.0.0.1` | Netzwerkadresse des Servers |
| `LICHT_PORT` | `8000` | Port |
| `LICHT_LOG_LEVEL` | `info` | `debug`, `info`, `warning`, `error` |
| `LICHT_SIMULATION` | `true` | Simulationsmodus (keine echte Hardware) |
| `HUE_ENABLED` | `false` | Hue-Adapter aktivieren (noch ohne Funktion) |
| `CASAMBI_EVOLUTION_ENABLED` | `false` | Casambi-Evolution-Adapter (noch ohne Funktion) |
| `CASAMBI_CLASSIC_ENABLED` | `false` | Casambi-Classic-Adapter (noch ohne Funktion) |

API-Schlüssel und Zugangsdaten gehören **nur** in Umgebungsvariablen bzw. die lokale
`.env`, niemals in den Quellcode.

## Tests

```bash
python -m pytest
```

## Projektstruktur

```
.
├── lichtsteuerung/              Python-Paket der Anwendung
│   ├── __init__.py              Versionsnummer
│   ├── __main__.py              Startpunkt (python -m lichtsteuerung)
│   ├── config.py                Einlesen der Umgebungsvariablen
│   ├── main.py                  FastAPI-App, Router, Startseite
│   ├── api/
│   │   └── health.py            GET /api/health
│   ├── adapters/                Ein Unterpaket pro Lichtsystem
│   │   ├── hue/
│   │   ├── casambi_evolution/
│   │   └── casambi_classic/
│   └── web/                     Weboberfläche
│       ├── index.html
│       └── static/style.css
├── tests/                       pytest-Tests
├── requirements.txt             Laufzeit-Abhängigkeiten (fastapi, uvicorn)
├── requirements-dev.txt         Test-Abhängigkeiten
├── .env.example                 Vorlage für die Konfiguration
└── README.md
```
