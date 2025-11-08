import os, json, argparse, math, random
from datetime import datetime
from PIL import Image, ImageDraw
from apps.generate.palette import pick as pick_palette

def ensure_dir(p): os.makedirs(p, exist_ok=True)

def ring_pattern(size, palette):
    W = H = size
    img = Image.new("RGB", (W,H), color=palette[0])
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2
    max_r = min(cx, cy)-10
    steps = 24
    for i in range(steps):
        r = int(max_r * (i+1)/steps)
        color = palette[(i % (len(palette)-1))+1]
        bbox = [cx-r, cy-r, cx+r, cy+r]
        width = max(1, int(6*(1 - i/steps)))
        d.ellipse(bbox, outline=color, width=width)
    return img

def radial_mandala(size, palette):
    W = H = size
    img = Image.new("RGB", (W,H), color=palette[0])
    d = ImageDraw.Draw(img)
    cx, cy = W//2, H//2
    arms = random.choice([8,12,16,24,32])
    layers = random.choice([6,8,10,12])
    max_r = min(cx, cy)-8
    for L in range(layers):
        r = int(max_r * (L+1)/layers)
        for a in range(arms):
            ang = 2*math.pi*a/arms
            x = cx + int(r*math.cos(ang))
            y = cy + int(r*math.sin(ang))
            color = palette[(L % (len(palette)-1))+1]
            d.line([(cx,cy),(x,y)], fill=color, width=1+L//2)
            d.ellipse([x-3,y-3,x+3,y+3], outline=color, width=1)
    return img

def stripes(size, palette):
    W=H=size
    img = Image.new("RGB",(W,H),color=palette[0])
    d = ImageDraw.Draw(img)
    n = random.choice([8,12,16,20])
    for i in range(n):
        x0 = 0
        y0 = int(i*H/n)
        x1 = W
        y1 = int((i+1)*H/n)
        color = palette[(i % (len(palette)-1))+1]
        d.rectangle([x0,y0,x1,y1], fill=color)
    return img

MODES = [ring_pattern, radial_mandala, stripes]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--research", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with open(args.research,"r") as f:
        research = json.load(f)

    top = research["top"][0]
    theme = top["niche"]
    pack_size = int(top.get("pack_size", 24))
    price_cents = int(top.get("price_suggestion", 999))

    stamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    pack_dir = os.path.join(args.out, f"{theme.replace(' ','_')}_{stamp}")
    ensure_dir(pack_dir)

    meta = {"theme": theme, "price_cents": price_cents, "pack_size": pack_size, "files": []}
    for i in range(pack_size):
        palette = pick_palette()
        func = random.choice(MODES)
        img = func(2048, palette)
        fn = f"{theme.replace(' ','_').lower()}_{i+1:03d}.png"
        img.save(os.path.join(pack_dir, fn), "PNG", optimize=True)
        meta["files"].append(fn)

    with open(os.path.join(pack_dir, "metadata.json"), "w") as f:
        json.dump(meta, f, indent=2)

    desc = f"{theme} - Premium Printable Digital Art Pack\n" + \
           f"Includes {pack_size} high-res 2048x2048 PNG artworks.\n" + \
           "• Instant download • Personal & commercial license (see listing)\n" + \
           "• Perfect for posters, wallpapers, POD mockups\n"
    with open(os.path.join(pack_dir, "description.txt"), "w", encoding="utf-8") as f:
        f.write(desc)

    print("Generated pack at:", pack_dir)

if __name__ == "__main__":
    main()
