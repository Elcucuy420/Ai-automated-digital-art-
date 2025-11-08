import json, argparse, random
from datetime import datetime

CANDIDATE_THEMES = [
  {"niche":"Minimalist Abstracts","tags":["minimal","modern","beige","neutral"]},
  {"niche":"Geometric Mandalas","tags":["mandala","sacred geometry","pattern"]},
  {"niche":"Boho Line Art","tags":["boho","line art","feminine","warm"]},
  {"niche":"Retro Vaporwave","tags":["neon","80s","vaporwave","synth"]},
  {"niche":"Nordic Landscapes","tags":["nordic","mountain","fjord","snow"]},
  {"niche":"Pet Silhouette Packs","tags":["dog","cat","pet","silhouette"]},
  {"niche":"Zen Ink Textures","tags":["zen","ink","wash","texture"]},
]

def score_theme(theme):
    base = 0.6
    trend = random.uniform(0.0, 0.4)
    return round(base + trend, 3)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    ranked = [{
        **t,
        "score": score_theme(t),
        "price_suggestion": random.choice([699, 999, 1299, 1499]),
        "pack_size": random.choice([16, 24, 32, 40])
    } for t in CANDIDATE_THEMES]
    ranked.sort(key=lambda x: x["score"], reverse=True)
    payload = {
        "generated_at": datetime.utcnow().isoformat()+"Z",
        "top": ranked[:3],
        "all": ranked
    }
    with open(args.out, "w") as f:
        json.dump(payload, f, indent=2)
    print("Wrote", args.out, "top:", payload["top"][0]["niche"])

if __name__ == "__main__":
    main()
