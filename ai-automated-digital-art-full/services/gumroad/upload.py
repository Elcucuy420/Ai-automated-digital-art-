import os, argparse, json, glob, requests, zipfile

GUMROAD_API = "https://api.gumroad.com/v2/products"

def create_or_update_product(token, pack_path, store_handle, default_price):
    meta = json.load(open(os.path.join(pack_path,"metadata.json")))
    title = f"{meta['theme']} - {meta['pack_size']} Abstracts ({store_handle})"
    desc  = open(os.path.join(pack_path,"description.txt"),encoding="utf-8").read()
    # Zip pack
    zip_name = os.path.join(pack_path, "pack.zip")
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as z:
        for fn in meta["files"]:
            z.write(os.path.join(pack_path, fn), fn)
    price = int(os.environ.get("DEFAULT_PRICE", meta["price_cents"]))
    data = {
        "name": title,
        "description": desc,
        "price": price,
        "published": False,
        "require_shipping": False,
        "max_purchase_count": 0,
    }
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.post(GUMROAD_API, data=data, headers=headers, timeout=60)
    r.raise_for_status()
    pid = r.json()["product"]["id"]
    files_api = f"https://api.gumroad.com/v2/products/{pid}/files"
    with open(zip_name, "rb") as f:
        rr = requests.post(files_api, headers=headers, files={"file":("pack.zip", f, "application/zip")})
        rr.raise_for_status()
    print("[gumroad] created product:", pid, "->", title)
    return pid

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pack_dir", required=True)
    args = ap.parse_args()
    token = os.environ["GUMROAD_TOKEN"]
    store = os.environ.get("STORE_HANDLE","store")
    packs = sorted(glob.glob(os.path.join(args.pack_dir,"*")))
    if not packs:
        print("No packs in", args.pack_dir); return
    create_or_update_product(token, packs[-1], store, os.environ.get("DEFAULT_PRICE"))

if __name__ == "__main__":
    main()
