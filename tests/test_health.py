from fastapi.testclient import TestClient

from lichtsteuerung.config import load_settings
from lichtsteuerung.main import create_app


def test_health_ok():
    client = TestClient(create_app(load_settings()))
    res = client.get("/api/health")
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "ok"
    assert set(body["adapters"]) == {"hue", "casambi_evolution", "casambi_classic"}


def test_index_served():
    client = TestClient(create_app(load_settings()))
    res = client.get("/")
    assert res.status_code == 200
    assert "Lichtsteuerung" in res.text
