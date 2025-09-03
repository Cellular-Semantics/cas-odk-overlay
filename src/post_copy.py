import sys
import requests
from pathlib import Path

def download_taxonomy_json(taxonomy_id: str, cas_taxonomy_url: str):
    src_dir = Path("src/dendrograms")
    src_dir.mkdir(parents=True, exist_ok=True)
    json_path = src_dir / f"{taxonomy_id}.json"
    response = requests.get(cas_taxonomy_url)
    response.raise_for_status()
    with open(json_path, "wb") as f:
        f.write(response.content)

def clean_taxonomy_json(taxonomy_id: str):
    src_dir = Path("src/dendrograms")
    json_path = src_dir / f"{taxonomy_id}.json"
    if json_path.exists():
        json_path.unlink()
    try:
        src_dir.rmdir()
    except OSError as e:
        print(f"Cleanup warning: {e}")

if __name__ == "__main__":
    taxonomy_id = "{{ taxonomy_id }}"
    cas_taxonomy_url = "{{ cas_taxonomy_url }}"
    if len(sys.argv) > 1 and sys.argv[1] == "--clean":
        clean_taxonomy_json(taxonomy_id)
    else:
        download_taxonomy_json(taxonomy_id, cas_taxonomy_url)
