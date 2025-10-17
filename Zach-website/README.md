# Zach Steinberg — Personal Portfolio

A clean, responsive portfolio website showcasing professional experience and skills. The site is ready to be deployed to GitHub Pages.

## Project Structure

- `index.html` — main page with About, Skills, Work, Contact sections
- `styles.css` — responsive styles
- `assets/` — contains profile images in various formats
- `resume.pdf` — downloadable resume
- `CNAME` — contains the custom domain `zacharysteinberg.com` for GitHub Pages

Quick local preview

Open `index.html` in a browser or run a tiny static server. Example using Python 3 built-in server:

```bash
python3 -m http.server 8000
# then open http://localhost:8000 in your browser
```

Deploying

## Deployment to GitHub Pages

1. Create a new repository named `zachsteinberg.github.io` on GitHub
2. Initialize and push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin git@github.com:zachsteinberg/zachsteinberg.github.io.git
   git push -u origin main
   ```
3. In repository Settings > Pages:
   - Select the "main" branch as source
   - The site will be published at `https://zachsteinberg.github.io`

## DNS Configuration

Add these DNS records at your domain registrar:

```
Type  | Name                  | Value
A     | @                    | 185.199.108.153
A     | @                    | 185.199.109.153
A     | @                    | 185.199.110.153
A     | @                    | 185.199.111.153
CNAME | www                  | zachsteinberg.github.io.
```

Note: DNS propagation may take 24-48 hours. After DNS is configured:
1. Go to repository Settings > Pages
2. Enable "Enforce HTTPS"

For Vercel specifically:
- Add domain `www.zachsteinberg.com` to the project.
- Create the required CNAME or A records shown by Vercel under your domain provider. Vercel will provision HTTPS automatically.

## Local Development

To test the site locally:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000 in your browser
```

## Making Updates

After making changes:
```bash
git add .
git commit -m "Description of changes"
git push
```

Your changes will automatically deploy within a few minutes.

## Optional: Analytics and SEO

- Add Open Graph images and meta tags if you want richer previews.
- Add a small privacy-friendly analytics script (Plausible or Simple Analytics) if desired.

Next steps

- Provide your real profile image and bio copy.
- Add links to live projects or repos in the Work section.
- Upload your `resume.pdf` to the site root and regenerate a QR that points to the final URL.
- If you'd like, I can:
  - Generate a real QR for you once you confirm the resume location.
  - Deploy to Vercel and walk through DNS changes for `www.zachsteinberg.com`.

Replacing your profile image

1. Recommended formats: `webp` (best) or `jpg` for photographs. Keep an SVG for a stylized fallback if desired.
2. Place files in `assets/` with these names (these are used by the site):
  - `assets/profile.webp` (preferred)
  - `assets/profile.jpg` (fallback)
  - `assets/profile.svg` (existing fallback)
3. Optimize the photo before uploading:
  - Resize to ~800px on the longest side for fast load times.
  - Compress with a tool like `squoosh.app` (browser) or `cwebp` for webp.

Quick convert & optimize with `cwebp` (if you have it installed):
```bash
# convert a jpeg to webp at quality 80
cwebp -q 80 assets/profile.jpg -o assets/profile.webp
```

If you'd like, upload the photo here (or tell me the filename) and I will add it to the repo and update the site so it uses the new image.
