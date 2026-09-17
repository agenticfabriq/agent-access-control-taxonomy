"""Validate taxonomy files and example records. pip install pyyaml jsonschema"""
import glob, json, sys, yaml, jsonschema
ids = set()
for f in glob.glob("taxonomy/*.yaml"):
    d = yaml.safe_load(open(f))
    for t in d["terms"]:
        assert t["id"].startswith(d["id"] + "/"), f"{f}: bad id {t['id']}"
        assert t["id"] not in ids, f"duplicate {t['id']}"
        ids.add(t["id"])
schema = json.load(open("schema/deployment-record.schema.json"))
for f in glob.glob("examples/*.yaml"):
    rec = yaml.safe_load(open(f))
    jsonschema.validate(rec, schema)
    for k, v in rec.items():
        for x in (v if isinstance(v, list) else [v]):
            if isinstance(x, str) and x.startswith("aact:"):
                assert x in ids, f"{f}: unknown term {x}"
print(f"ok: {len(ids)} terms, examples valid")
