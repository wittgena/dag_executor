# dsl_loader.py
# Loads DSL spec files from the `dsl/` folder and returns parsed metadata and executable DSL tree.

import os
import yaml
import json

DSL_FOLDER = "dsl"

def load_dsl_manifest():
    path = os.path.join(DSL_FOLDER, "dsl_manifest.yaml")
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_dsl_spec(dsl_name):
    manifest = load_dsl_manifest()
    dsl_entry = next((item for item in manifest['dsls'] if item['name'] == dsl_name), None)
    if not dsl_entry:
        raise ValueError(f"DSL spec '{dsl_name}' not found in manifest.")

    path = os.path.join(DSL_FOLDER, dsl_entry['file'])
    ext = os.path.splitext(path)[-1].lower()

    with open(path, 'r', encoding='utf-8') as f:
        if ext == ".json":
            return json.load(f)
        elif ext in [".yaml", ".yml"]:
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported DSL file format: {ext}")