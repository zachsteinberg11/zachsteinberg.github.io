#!/usr/bin/env python3
"""
Generate a QR code (SVG + PNG) for your resume URL.

Usage:
  python3 scripts/generate_qr.py "https://www.zachsteinberg.com/resume.pdf"

Installs:
  python3 -m pip install --user "qrcode[pil]"
"""
import sys
from pathlib import Path
import qrcode
import qrcode.image.svg

data = sys.argv[1] if len(sys.argv) > 1 else 'https://www.zachsteinberg.com/resume.pdf'
out_svg = Path('assets/resume-qr.svg')
out_png = Path('assets/resume-qr.png')

out_svg.parent.mkdir(parents=True, exist_ok=True)

# SVG
factory = qrcode.image.svg.SvgImage
qr_svg = qrcode.make(data, image_factory=factory)
qr_svg.save(out_svg)

# PNG (small fallback)
qr_png = qrcode.make(data)
qr_png.save(out_png)

print(f'Wrote {out_svg} and {out_png} (data={data})')
