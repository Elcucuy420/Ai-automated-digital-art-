import os, json, argparse, random
HOOKS = [
  "Transform your space with minimalist abstracts.",
  "Print, frame, and elevate your room in minutes.",
  "Designer-grade art you can download instantly.",
  "Clean lines. Bold mood. Zero clutter.",
  "Algorithmic art for modern homes."
]
CTAS = [
  "Link in bio to download.",
  "Grab the full pack now.",
  "Instant digital download.",
  "Print at home or anywhere.",
  "New pack just dropped."
]
HASHTAGS = "#digitalart #printableart #wallart #homedecor #minimalist #abstract #posterdesign #gumroad"
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--out", default="captions.txt")
    args = ap.parse_args()
    meta = json.load(open(args.meta))
    lines = [f"{random.choice(HOOKS)} {random.choice(CTAS)} {HASHTAGS}" for _ in range(8)]
    with open(args.out,"w",encoding="utf-8") as f: f.write("\n".join(lines))
    print("Wrote captions to", args.out)
if __name__ == "__main__":
    main()
