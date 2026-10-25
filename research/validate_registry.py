#!/usr/bin/env python3
"""Offline stdlib-only schema smoke check for public research API registry.

Not a live provider, ethics, licensing, or scientific-validity check.
Run: python3 research/validate_registry.py
"""
import json
import re
from pathlib import Path

REGISTRY = Path(__file__).resolve().with_name("api_registry.json")
ALLOWED = {"planned", "prototype-or-reference", "verified-live", "deprecated"}
def validate(path=REGISTRY):
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    assert raw["schema_version"] == "0.1.0"
    providers = raw["providers"]
    assert isinstance(providers, list) and len(providers) == 14, "expected 14 selected candidate sources"
    ids = set()
    for p in providers:
        assert re.fullmatch(r"[a-z][a-z0-9-]*", p["id"]), p
        assert p["id"] not in ids, "duplicate provider ID"
        ids.add(p["id"])
        assert p["base_url"].startswith("https://"), "HTTPS source required"
        assert isinstance(p["projects"], list) and p["projects"], "orphan provider"
        assert p["implementation_status"] in ALLOWED
        assert isinstance(p["verified_live"], bool)
        assert isinstance(p["policy_recheck_required"], bool)
        assert isinstance(p.get("use_gate"), str) and len(p["use_gate"]) > 8
        if p["verified_live"]:
            raise AssertionError("offline candidate catalogue cannot claim live verification")
    assert "api_key" not in json.dumps(raw).lower(), "secret-shaped inline content"
    return {"schema":raw["schema_version"], "providers":len(providers), "offline_validation":"PASS","live_providers_verified":0}

if __name__ == "__main__":
    print(json.dumps(validate(),ensure_ascii=False,sort_keys=True))
