# AI Automated Digital Art - Zero-Cost, Faceless, Self-Evolving

This repo runs a zero-cost automation loop on GitHub Actions:
1) Research trending art niches
2) Generate algorithmic PNG art packs (no GPU costs)
3) Publish as draft products to Gumroad
4) Learn & Evolve by updating niche memory for next runs

## Setup (5 minutes)
1. In your repo: Settings -> Secrets and variables -> Actions
   - Secrets: AI (for repo writes), GUMROAD_TOKEN, STORE_HANDLE, (optional) ADMIN_APPROVAL
   - Variables: DEFAULT_PRICE (e.g. 999), PACK_SIZE (e.g. 24)
2. Go to Actions and run: Research -> Generate -> Publish -> Learn

The AI secret is used to push memory updates in 4_learn_and_evolve.yml.
