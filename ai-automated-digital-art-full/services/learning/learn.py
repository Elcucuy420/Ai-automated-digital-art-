import os, json, argparse
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--memory", required=True)
    args = ap.parse_args()
    niche_file = os.path.join(args.memory, "niche_memory.json")
    perf_file  = os.path.join(args.memory, "performance.json")
    if not os.path.exists(niche_file): open(niche_file,"w").write(json.dumps({"bias":{}}, indent=2))
    if not os.path.exists(perf_file):  open(perf_file,"w").write(json.dumps({"sales":[]}, indent=2))
    with open(niche_file,"r") as f: niche = json.load(f)
    bias = niche.get("bias", {})
    last_theme = os.environ.get("LAST_THEME","")
    if last_theme:
        bias[last_theme] = bias.get(last_theme, 0) + 1
    niche["bias"] = bias
    with open(niche_file,"w") as f: json.dump(niche, f, indent=2)
    print("Updated niche bias memory:", niche)
if __name__ == "__main__":
    main()
