#!/usr/bin/env python3
"""Fail-closed audit for FreeToken: evidence, static SEO, cards and README."""
from __future__ import annotations
import json, re, sys, pathlib, xml.etree.ElementTree as ET
from datetime import date
ROOT = pathlib.Path(__file__).resolve().parents[1]
ledger = json.loads((ROOT / "data/providers.json").read_text(encoding="utf-8"))
items = ledger["providers"]
html = (ROOT / "index.html").read_text(encoding="utf-8")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
errors = []
def require(ok, message):
    if not ok: errors.append(message)
today = date.today()
require(8 <= len(items) <= 200, "resources out of expected range")
ids = [x["id"] for x in items]
require(len(set(ids)) == len(ids), "duplicate IDs")
require(bool(re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', ledger["updated"])), "invalid update date")
require(date.fromisoformat(ledger["updated"]) <= today, "future dated ledger")
for x in items:
    missing = set(("id","name","kind","region","quota","summary","steps","limits","source","portal","verified","checked","tags","model")) - set(x)
    require(not missing, f"{x.get('id')} missing: {sorted(missing)}")
    if missing: continue
    require(x["kind"] in ("free","trial","mixed","paid","check"), f"{x['id']}: unsupported kind")
    require(x["region"] in ("国内","海外","聚合","云服务"), f"{x['id']}: unsupported region")
    require(bool(re.fullmatch(r'[a-z][a-z0-9-]{1,40}',x["id"])), f"{x['id']}: invalid slug")
    require(x["portal"].startswith("https://") and x["source"].startswith("https://"),f"{x['id']}: URL must be HTTPS")
    require(x["name"] in readme, f"{x['id']}: missing in README")
    require(f'id="{x["id"]}"' in html, f"{x['id']}: missing HTML card")
    require(x["quota"].replace("&", "&amp;") in html, f"{x['id']}: HTML quota differs from ledger")
    require(x["source"].replace("&", "&amp;") in html, f"{x['id']}: official source URL missing in HTML")
    require(x["checked"] == ledger["updated"] if x["verified"] else x["checked"] is None, f"{x['id']}: invalid verification date")
    if x["kind"] == "paid": require(x["verified"],f"{x['id']}: paid status without supporting official source")
ids_in_html = re.findall(r'<article class="resource" id="([^"]+)"', html)
require(ids_in_html == ids,"HTML cards must exactly match the dataset order")
require("FREETOKEN_CARDS_START" in html and "FREETOKEN_TABLE_START" in readme,"missing synchronization markers")
require("https://aipmandy.github.io/FreeToken/" in html and 'rel="canonical"' in html,"canonical missing")
require("https://metaver.vip/" in html and "AIPMAndy" in html,"contact missing")
require("Free 用户每月赠送积分为 0" in html, "HF updated policy missing")
require("$0.10/月" not in html and "$0.10 / 月" not in html, "obsolete Hugging Face benefit still in HTML")
root = ET.fromstring(sitemap)
urls=[x.text for x in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
expected={"https://aipmandy.github.io/FreeToken/","https://aipmandy.github.io/FreeToken/ecosystem.html",*("https://aipmandy.github.io/FreeToken/guides/"+n+".html" for n in ("qwen-free-api","openrouter-free-api","huggingface-pricing"))}
require(set(urls)==expected,"sitemap coverage mismatch")
for u in urls:
    if u.endswith("/"): path=ROOT/"index.html"
    else:path=ROOT/u.split("/FreeToken/",1)[1]
    require(path.exists(),f"missing sitemap target: {u}")
for name in ("qwen-free-api","openrouter-free-api","huggingface-pricing"):
    guide=(ROOT/"guides"/(name+".html")).read_text(encoding="utf-8")
    require('rel="canonical"' in guide,f"guide {name} canonical missing")
    require("AIPMAndy" in guide,f"guide {name} contact missing")
    require("<main" in guide and "<h1>" in guide,f"guide {name} semantic tags missing")
for x in re.findall(r'<a[^>]*target="_blank"[^>]*>',html):
    require('rel="noopener noreferrer"' in x,"external _blank anchor missing noreferrer")
require("Sitemap: https://aipmandy.github.io/FreeToken/sitemap.xml" in (ROOT/"robots.txt").read_text(encoding="utf-8"), "robots sitemap missing")
print(f"FreeToken audit: {len(items)} providers; {len(urls)} SEO URLs; {len(errors)} errors")
for err in errors: print("FAIL:",err)
sys.exit(1 if errors else 0)
