#!/usr/bin/env python3
"""Turn the "finds" collection of the Sinchon Archive Finds catalogue into archive/finds.json.

Input: a JSON Lines file, one document per line, as the catalogue's database lists them:
    {"id": "H-TRNS-97527-770", "data": {...}, "updatedAt": "..."}
(an array of such objects also works). Only the fields below are published.

Usage: python3 archive/build_finds.py docs.jsonl archive/finds.json
"""
import json, sys, datetime

FIELDS = ["title", "titleKo", "date", "archive", "recordId", "url", "kind", "place",
          "licence", "imageUrl", "thumbUrl", "imageCredit", "note", "addedAt"]

def load(path):
    text = open(path, encoding="utf-8").read().strip()
    if text.startswith("["):
        return json.loads(text)
    return [json.loads(l) for l in text.splitlines() if l.strip().startswith("{")]

def main(src, out):
    docs = load(src)
    finds = []
    for d in docs:
        data = d.get("data") or {}
        rec = {"id": d.get("id") or data.get("recordId")}
        rec.update({k: data[k] for k in FIELDS if data.get(k) not in (None, "")})
        if not rec.get("url"):
            continue  # never publish an entry without a link back to its source
        finds.append(rec)
    finds.sort(key=lambda r: (r.get("addedAt", ""), r["id"]), reverse=True)
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    payload = {"catalogue": "Sinchon Archive Finds", "project": "Passing Stories (Yonsei UIC, Team 5)",
               "checkedAt": now, "count": len(finds), "finds": finds}
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"wrote {len(finds)} records to {out}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
