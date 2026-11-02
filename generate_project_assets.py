"""
Generate high-fidelity, cohesive mockups for Lunex Presents portfolio projects.
Creates 4 gallery images and 1 thumbnail per project with consistent theme and high visual polish.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

# Ensure directories exist
MEDIA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'portfolio')
GALLERY_DIR = os.path.join(MEDIA_DIR, 'gallery')
os.makedirs(GALLERY_DIR, exist_ok=True)

# Font helper
def get_font(size, bold=False):
    font_names = [
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\calibrib.ttf" if bold else "C:\\Windows\\Fonts\\calibri.ttf",
    ]
    for fn in font_names:
        if os.path.exists(fn):
            try:
                return ImageFont.truetype(fn, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_header_bar(draw, w, title, url, bg_color=(25, 29, 36), text_color=(160, 170, 185)):
    # Browser / App top bar
    draw.rectangle([0, 0, w, 44], fill=bg_color)
    # Window controls
    draw.ellipse([18, 16, 30, 28], fill=(239, 68, 68))
    draw.ellipse([36, 16, 48, 28], fill=(245, 158, 11))
    draw.ellipse([54, 16, 66, 28], fill=(34, 197, 94))
    
    # URL Pill
    draw.rounded_rectangle([120, 10, w - 120, 34], radius=6, fill=(35, 41, 52))
    f_url = get_font(12)
    draw.text((140, 14), f"🔒 {url}", fill=text_color, font=f_url)

def draw_card(draw, box, fill, border=None, radius=12):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=border, width=1 if border else 0)

# ==========================================
# 1. NOVATECH SOLUTIONS (4 Images + Thumb)
# ==========================================
def make_novatech_images():
    print("Generating NovaTech Solutions images...")
    primary_navy = (10, 14, 23)
    card_navy = (18, 24, 38)
    cyan_accent = (0, 210, 255)
    blue_accent = (59, 130, 246)
    white = (255, 255, 255)
    muted = (148, 163, 184)
    
    # --- Image 1: Corporate Identity & Brand Suite ---
    img1 = Image.new("RGB", (1200, 800), primary_navy)
    d1 = ImageDraw.Draw(img1)
    
    # Background subtle grid
    for x in range(0, 1200, 60):
        d1.line([(x, 0), (x, 800)], fill=(16, 22, 35), width=1)
    for y in range(0, 800, 60):
        d1.line([(0, y), (1200, y)], fill=(16, 22, 35), width=1)
    
    # Title badge
    draw_card(d1, [80, 60, 360, 100], fill=(20, 30, 48), border=cyan_accent, radius=8)
    d1.text((100, 72), "BRAND IDENTITY SYSTEM", fill=cyan_accent, font=get_font(14, bold=True))
    
    d1.text((80, 120), "NovaTech Solutions", fill=white, font=get_font(38, bold=True))
    d1.text((80, 175), "Complete B2B Corporate Identity & Stationery Architecture", fill=muted, font=get_font(18))
    
    # Large Letterhead mockup card
    draw_card(d1, [80, 240, 560, 720], fill=card_navy, border=(40, 55, 80), radius=16)
    # Header logo
    d1.rounded_rectangle([120, 280, 160, 320], radius=8, fill=cyan_accent)
    d1.text((130, 287), "N", fill=primary_navy, font=get_font(24, bold=True))
    d1.text((175, 290), "NOVATECH", fill=white, font=get_font(20, bold=True))
    d1.text((175, 312), "SOLUTIONS CORP.", fill=cyan_accent, font=get_font(11))
    
    d1.line([(120, 350), (520, 350)], fill=(30, 42, 62), width=1)
    d1.text((120, 380), "CONFIDENTIAL & PROPRIETARY", fill=(100, 116, 139), font=get_font(12, bold=True))
    d1.text((120, 410), "Enterprise Cloud & AI Advisory", fill=white, font=get_font(20, bold=True))
    
    # Simulated lines of text
    for i, w in enumerate([360, 380, 340, 390, 280, 370, 350, 300]):
        d1.rounded_rectangle([120, 450 + i*24, 120 + w, 458 + i*24], radius=4, fill=(35, 48, 70))
    
    d1.line([(120, 660), (520, 660)], fill=(30, 42, 62), width=1)
    d1.text((120, 675), "San Francisco • London • Singapore", fill=muted, font=get_font(12))
    
    # Overlapping Business Cards Mockup
    # Card 1 (Front - Dark)
    draw_card(d1, [620, 250, 1120, 460], fill=(14, 18, 27), border=cyan_accent, radius=14)
    d1.rounded_rectangle([660, 300, 710, 350], radius=10, fill=cyan_accent)
    d1.text((675, 310), "N", fill=primary_navy, font=get_font(30, bold=True))
    d1.text((730, 305), "NOVATECH", fill=white, font=get_font(26, bold=True))
    d1.text((730, 335), "ENTERPRISE INTELLIGENCE", fill=cyan_accent, font=get_font(12, bold=True))
    d1.text((660, 395), "www.novatech-solutions.io", fill=(148, 163, 184), font=get_font(14))
    
    # Card 2 (Back - Silver & Navy Details)
    draw_card(d1, [660, 490, 1120, 700], fill=(24, 32, 48), border=(60, 80, 110), radius=14)
    d1.text((700, 525), "Alexander Vance", fill=white, font=get_font(22, bold=True))
    d1.text((700, 555), "Chief Technology Architect", fill=cyan_accent, font=get_font(14))
    d1.text((700, 600), "alex.vance@novatech-solutions.io", fill=muted, font=get_font(14))
    d1.text((700, 630), "+1 (555) 849-2041", fill=muted, font=get_font(14))
    d1.text((700, 660), "101 California St, Suite 4400, SF", fill=muted, font=get_font(14))
    
    # QR badge
    draw_card(d1, [1010, 525, 1080, 595], fill=(35, 48, 72), border=cyan_accent, radius=8)
    d1.text((1025, 555), "[QR]", fill=cyan_accent, font=get_font(12, bold=True))
    
    img1.save(os.path.join(GALLERY_DIR, "novatech-solutions-1.jpg"), quality=92)
    # Also save as main thumbnail
    img1.resize((800, 600), Image.Resampling.LANCZOS).save(os.path.join(MEDIA_DIR, "novatech-solutions-thumb.jpg"), quality=90)
    
    # --- Image 2: Enterprise Cloud Portal & Dashboard ---
    img2 = Image.new("RGB", (1200, 800), (12, 16, 24))
    d2 = ImageDraw.Draw(img2)
    draw_header_bar(d2, 1200, "NovaTech Cloud Console", "console.novatech-solutions.io/clusters")
    
    # Sidebar
    draw_card(d2, [20, 65, 220, 780], fill=card_navy, border=(35, 46, 68), radius=10)
    d2.text((45, 90), "NOVATECH", fill=cyan_accent, font=get_font(16, bold=True))
    nav_items = ["Overview", "Deployments", "Telemetry", "Kubernetes", "API Gateways", "Security Vault", "Settings"]
    for idx, item in enumerate(nav_items):
        active = (idx == 0)
        y = 140 + idx * 46
        if active:
            draw_card(d2, [32, y - 6, 208, y + 26], fill=(0, 210, 255, 30), border=cyan_accent, radius=6)
        d2.text((50, y), item, fill=white if active else muted, font=get_font(14, bold=active))
    
    # Top stats row
    stats = [
        ("GLOBAL UPTIME", "99.998%", cyan_accent),
        ("LIVE REQUESTS", "42.8k /sec", white),
        ("ACTIVE PODS", "1,842 Nodes", (52, 211, 153)),
        ("SYSTEM LATENCY", "12 ms", blue_accent),
    ]
    for idx, (label, val, col) in enumerate(stats):
        x = 240 + idx * 235
        draw_card(d2, [x, 65, x + 220, 160], fill=card_navy, border=(35, 46, 68), radius=10)
        d2.text((x + 20, 85), label, fill=muted, font=get_font(11, bold=True))
        d2.text((x + 20, 110), val, fill=col, font=get_font(26, bold=True))
    
    # Central Chart Card (Spline area chart)
    draw_card(d2, [240, 180, 1175, 480], fill=card_navy, border=(35, 46, 68), radius=12)
    d2.text((270, 205), "Real-Time Traffic & Node Throughput", fill=white, font=get_font(18, bold=True))
    d2.text((270, 235), "Continuous stream from 14 edge locations", fill=muted, font=get_font(13))
    
    # Grid lines in chart
    for y_line in [280, 330, 380, 430]:
        d2.line([(270, y_line), (1145, y_line)], fill=(26, 34, 50), width=1)
    
    # Line spline graph
    points = [
        (280, 420), (360, 390), (440, 340), (520, 360), (600, 310),
        (680, 330), (760, 280), (840, 300), (920, 260), (1000, 290), (1080, 250), (1140, 270)
    ]
    for i in range(len(points) - 1):
        d2.line([points[i], points[i+1]], fill=cyan_accent, width=3)
        d2.ellipse([points[i][0]-4, points[i][1]-4, points[i][0]+4, points[i][1]+4], fill=white, outline=cyan_accent)
    d2.ellipse([points[-1][0]-4, points[-1][1]-4, points[-1][0]+4, points[-1][1]+4], fill=white, outline=cyan_accent)
    
    # Bottom Table: Cluster Health
    draw_card(d2, [240, 500, 1175, 780], fill=card_navy, border=(35, 46, 68), radius=12)
    d2.text((270, 525), "Active Production Clusters", fill=white, font=get_font(18, bold=True))
    
    headers = ["Cluster Name", "Region", "Nodes", "CPU Load", "Status"]
    h_x = [270, 470, 650, 810, 990]
    for h, x in zip(headers, h_x):
        d2.text((x, 565), h, fill=(100, 116, 139), font=get_font(12, bold=True))
    d2.line([(270, 590), (1145, 590)], fill=(30, 40, 60), width=1)
    
    rows = [
        ("cluster-us-east-prod", "us-east-1 (N. Virginia)", "48 Nodes", "42%", "HEALTHY ✓"),
        ("cluster-eu-west-prod", "eu-west-1 (Frankfurt)", "32 Nodes", "36%", "HEALTHY ✓"),
        ("cluster-ap-se-prod", "ap-southeast-1 (Singapore)", "24 Nodes", "29%", "HEALTHY ✓"),
        ("cluster-edge-ingress", "Global Anycast Edge", "128 Nodes", "58%", "OPTIMAL ✓"),
    ]
    for r_idx, (cname, reg, nds, cpu, st) in enumerate(rows):
        y_r = 610 + r_idx * 40
        d2.text((270, y_r), cname, fill=white, font=get_font(14, bold=True))
        d2.text((470, y_r), reg, fill=muted, font=get_font(13))
        d2.text((650, y_r), nds, fill=white, font=get_font(13))
        d2.text((810, y_r), cpu, fill=cyan_accent, font=get_font(13))
        d2.text((990, y_r), st, fill=(52, 211, 153), font=get_font(13, bold=True))
    
    img2.save(os.path.join(GALLERY_DIR, "novatech-solutions-2.jpg"), quality=92)
    
    # --- Image 3: Mobile App & Real-Time Monitor ---
    img3 = Image.new("RGB", (1200, 800), (8, 12, 19))
    d3 = ImageDraw.Draw(img3)
    
    # Background glow
    d3.text((80, 70), "NOVATECH MOBILE PLATFORM", fill=cyan_accent, font=get_font(14, bold=True))
    d3.text((80, 105), "Executive Monitoring & Incident Control", fill=white, font=get_font(34, bold=True))
    d3.text((80, 155), "Native iOS and Android operations cockpit for C-suite and DevOps leads.", fill=muted, font=get_font(16))
    
    # Phone Frame 1 (Overview)
    draw_card(d3, [140, 220, 520, 770], fill=(18, 24, 38), border=(50, 70, 100), radius=36)
    # Notch
    d3.rounded_rectangle([280, 232, 380, 252], radius=10, fill=(10, 14, 23))
    # Screen contents
    d3.text((180, 280), "NovaTech Monitor", fill=white, font=get_font(18, bold=True))
    d3.text((180, 310), "Production Status: Normal", fill=(52, 211, 153), font=get_font(12, bold=True))
    
    draw_card(d3, [170, 345, 490, 455], fill=(26, 35, 54), border=cyan_accent, radius=12)
    d3.text((190, 365), "System Health", fill=muted, font=get_font(12))
    d3.text((190, 390), "99.998%", fill=cyan_accent, font=get_font(30, bold=True))
    d3.text((190, 430), "Zero critical incidents last 90 days", fill=(148, 163, 184), font=get_font(11))
    
    # Mini stats
    draw_card(d3, [170, 475, 320, 565], fill=(26, 35, 54), radius=10)
    d3.text((185, 490), "Avg Ping", fill=muted, font=get_font(11))
    d3.text((185, 515), "14ms", fill=white, font=get_font(20, bold=True))
    
    draw_card(d3, [340, 475, 490, 565], fill=(26, 35, 54), radius=10)
    d3.text((355, 490), "Active Pods", fill=muted, font=get_font(11))
    d3.text((355, 515), "1,842", fill=blue_accent, font=get_font(20, bold=True))
    
    # Push alert card
    draw_card(d3, [170, 585, 490, 680], fill=(30, 42, 65), border=(45, 60, 90), radius=10)
    d3.text((190, 600), "🔔 System Alert", fill=cyan_accent, font=get_font(12, bold=True))
    d3.text((190, 625), "Auto-scaled Frankfurt cluster +8 nodes", fill=white, font=get_font(12))
    d3.text((190, 650), "Traffic spike absorbed with 0% dropped packets", fill=muted, font=get_font(10))
    
    # Phone Frame 2 (Metrics screen)
    draw_card(d3, [580, 220, 960, 770], fill=(18, 24, 38), border=(50, 70, 100), radius=36)
    d3.rounded_rectangle([720, 232, 820, 252], radius=10, fill=(10, 14, 23))
    d3.text((620, 280), "Live Metrics", fill=white, font=get_font(18, bold=True))
    d3.text((620, 310), "API Gateways • Global", fill=cyan_accent, font=get_font(12))
    
    # Graph inside phone
    draw_card(d3, [610, 345, 930, 520], fill=(26, 35, 54), radius=12)
    d3.text((630, 365), "Request Velocity", fill=white, font=get_font(14, bold=True))
    m_pts = [(640, 470), (690, 440), (740, 460), (790, 400), (840, 420), (900, 380)]
    for i in range(len(m_pts)-1):
        d3.line([m_pts[i], m_pts[i+1]], fill=cyan_accent, width=3)
    
    # Action buttons
    draw_card(d3, [610, 550, 930, 610], fill=cyan_accent, radius=10)
    d3.text((720, 570), "RUN DIAGNOSTICS", fill=primary_navy, font=get_font(14, bold=True))
    draw_card(d3, [610, 630, 930, 690], fill=(30, 42, 65), border=(50, 70, 100), radius=10)
    d3.text((710, 650), "EXPORT AUDIT LOG", fill=white, font=get_font(14, bold=True))
    
    # Feature Callouts on right
    callouts = [
        ("Real-time Push Alerts", "Immediate escalation for DevOps on duty."),
        ("One-Tap Mitigation", "Drain nodes or route traffic away from compromised regions."),
        ("Biometric Security", "FaceID & hardware security key authentication."),
    ]
    for idx, (title, desc) in enumerate(callouts):
        y_c = 340 + idx * 110
        d3.text((1000, y_c), title, fill=cyan_accent, font=get_font(16, bold=True))
        d3.text((1000, y_c + 28), desc, fill=muted, font=get_font(13))
    
    img3.save(os.path.join(GALLERY_DIR, "novatech-solutions-3.jpg"), quality=92)
    
    # --- Image 4: Brand Guidelines & Design Tokens ---
    img4 = Image.new("RGB", (1200, 800), primary_navy)
    d4 = ImageDraw.Draw(img4)
    
    d4.text((80, 60), "NOVATECH SOLUTIONS", fill=cyan_accent, font=get_font(14, bold=True))
    d4.text((80, 95), "Brand System & Visual Guidelines", fill=white, font=get_font(34, bold=True))
    d4.text((80, 145), "Design tokens, color harmony, typography hierarchy, and geometry.", fill=muted, font=get_font(16))
    
    # Color Tokens Row
    colors = [
        ("Primary Deep Navy", "#0A0E17", primary_navy),
        ("Surface Card Navy", "#121826", card_navy),
        ("Vibrant Cyan Accent", "#00D2FF", cyan_accent),
        ("Tech Blue", "#3B82F6", blue_accent),
        ("Emerald Health", "#34D399", (52, 211, 153)),
    ]
    for idx, (name, hex_code, rgb) in enumerate(colors):
        x = 80 + idx * 215
        draw_card(d4, [x, 210, x + 195, 360], fill=card_navy, border=(40, 55, 80), radius=10)
        draw_card(d4, [x + 15, 225, x + 180, 285], fill=rgb, radius=6)
        text_color = white if rgb != cyan_accent else primary_navy
        d4.text((x + 15, 300), name, fill=white, font=get_font(12, bold=True))
        d4.text((x + 15, 325), hex_code, fill=cyan_accent, font=get_font(12))
    
    # Typography & Grid System
    draw_card(d4, [80, 390, 610, 740], fill=card_navy, border=(40, 55, 80), radius=12)
    d4.text((110, 420), "TYPOGRAPHY SYSTEM", fill=cyan_accent, font=get_font(13, bold=True))
    d4.text((110, 455), "Aa Inter Sans Display", fill=white, font=get_font(28, bold=True))
    d4.text((110, 500), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", fill=muted, font=get_font(14))
    d4.text((110, 525), "abcdefghijklmnopqrstuvwxyz 0123456789", fill=muted, font=get_font(14))
    d4.text((110, 570), "H1 Headline — 48px / Bold / -0.02em", fill=white, font=get_font(14, bold=True))
    d4.text((110, 605), "H2 Subtitle — 24px / SemiBold / Normal", fill=white, font=get_font(14))
    d4.text((110, 640), "Body Copy — 16px / Regular / 1.65 Line Height", fill=muted, font=get_font(14))
    d4.text((110, 675), "Code Mono — 13px / JetBrains Mono", fill=cyan_accent, font=get_font(13))
    
    # Geometric Grid & Logomark Construction
    draw_card(d4, [650, 390, 1120, 740], fill=card_navy, border=(40, 55, 80), radius=12)
    d4.text((680, 420), "GEOMETRIC LOGOMARK CONSTRUCTION", fill=cyan_accent, font=get_font(13, bold=True))
    
    # Construction grid drawing
    center_x, center_y = 885, 570
    for r in [40, 80, 120]:
        d4.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], outline=(40, 60, 90), width=1)
    d4.line([(center_x - 140, center_y), (center_x + 140, center_y)], fill=(40, 60, 90), width=1)
    d4.line([(center_x, center_y - 140), (center_x, center_y + 140)], fill=(40, 60, 90), width=1)
    
    # Logo in center
    draw_card(d4, [center_x - 45, center_y - 45, center_x + 45, center_y + 45], fill=cyan_accent, radius=12)
    d4.text((center_x - 14, center_y - 22), "N", fill=primary_navy, font=get_font(38, bold=True))
    d4.text((780, 700), "Strict 45° angle symmetry • Golden Ratio", fill=muted, font=get_font(13))
    
    img4.save(os.path.join(GALLERY_DIR, "novatech-solutions-4.jpg"), quality=92)
    print("NovaTech images created successfully!")

# ==========================================
# 2. BLOOM BAKERY (4 Images + Thumb)
# ==========================================
def make_bloom_images():
    print("Generating Bloom Bakery images...")
    bg_warm = (248, 245, 238)
    card_cream = (255, 255, 255)
    terracotta = (194, 109, 74)
    brown_dark = (45, 30, 22)
    sage = (107, 142, 109)
    muted_cream = (130, 115, 105)
    
    # --- Image 1: Artisan Storefront & Hero ---
    img1 = Image.new("RGB", (1200, 800), bg_warm)
    d1 = ImageDraw.Draw(img1)
    draw_header_bar(d1, 1200, "Bloom Bakery", "bloombakery.com", bg_color=(235, 228, 218), text_color=brown_dark)
    
    # Hero Navbar
    d1.text((80, 75), "BLOOM BAKERY", fill=terracotta, font=get_font(20, bold=True))
    for idx, nav in enumerate(["Our Story", "Bake Schedule", "Order Online", "Catering", "Locations"]):
        d1.text((550 + idx * 110, 78), nav, fill=brown_dark, font=get_font(13, bold=True))
    draw_card(d1, [1040, 65, 1120, 105], fill=terracotta, radius=6)
    d1.text((1055, 76), "Order Now", fill=(255, 255, 255), font=get_font(12, bold=True))
    
    # Hero Headline
    d1.text((80, 180), "NATURAL SOURDOUGH & ARTISAN PASTRY", fill=terracotta, font=get_font(14, bold=True))
    d1.text((80, 215), "Baked Fresh Everyday.\nCrafted with Intention.", fill=brown_dark, font=get_font(44, bold=True))
    d1.text((80, 335), "Small-batch slow fermentation using 100% stoneground organic flour\nand pure wild yeasts. Good bread takes time.", fill=muted_cream, font=get_font(16))
    
    draw_card(d1, [80, 410, 260, 465], fill=terracotta, radius=8)
    d1.text((115, 428), "Explore Today's Menu", fill=(255, 255, 255), font=get_font(14, bold=True))
    
    draw_card(d1, [280, 410, 440, 465], fill=(255, 255, 255), border=terracotta, radius=8)
    d1.text((310, 428), "Find Our Bakery", fill=terracotta, font=get_font(14, bold=True))
    
    # Store highlights
    draw_card(d1, [80, 520, 500, 720], fill=card_cream, border=(230, 220, 210), radius=16)
    d1.text((110, 550), "TODAY'S SPECIAL OVENS", fill=sage, font=get_font(13, bold=True))
    d1.text((110, 580), "Cranberry & Walnut Country Loaf", fill=brown_dark, font=get_font(20, bold=True))
    d1.text((110, 615), "Out of oven at 8:00 AM • Only 30 loaves baked daily", fill=muted_cream, font=get_font(14))
    d1.text((110, 660), "Price: $8.50  |  Vegan  |  48h Ferment", fill=terracotta, font=get_font(14, bold=True))
    
    # Big visual showcase card on right
    draw_card(d1, [560, 180, 1120, 720], fill=(240, 230, 218), border=(220, 205, 190), radius=20)
    d1.text((620, 260), "🌾 Stoneground Flour", fill=terracotta, font=get_font(24, bold=True))
    d1.text((620, 310), "Every single morning our bakers shape\neach sourdough boule by hand.", fill=brown_dark, font=get_font(18))
    
    # Feature badges
    draw_card(d1, [620, 420, 820, 520], fill=card_cream, radius=12)
    d1.text((645, 445), "48-Hour Ferment", fill=brown_dark, font=get_font(15, bold=True))
    d1.text((645, 475), "Easier digestion & crisp crust", fill=muted_cream, font=get_font(12))
    
    draw_card(d1, [860, 420, 1060, 520], fill=card_cream, radius=12)
    d1.text((885, 445), "Zero Additives", fill=brown_dark, font=get_font(15, bold=True))
    d1.text((885, 475), "Flour, water, sea salt & starter", fill=muted_cream, font=get_font(12))
    
    img1.save(os.path.join(GALLERY_DIR, "bloom-bakery-1.jpg"), quality=92)
    img1.resize((800, 600), Image.Resampling.LANCZOS).save(os.path.join(MEDIA_DIR, "bloom-bakery-thumb.jpg"), quality=90)
    
    # --- Image 2: Daily Fresh Bakes & Pastry Catalog ---
    img2 = Image.new("RGB", (1200, 800), bg_warm)
    d2 = ImageDraw.Draw(img2)
    draw_header_bar(d2, 1200, "Bloom Bakery - Menu", "bloombakery.com/menu", bg_color=(235, 228, 218), text_color=brown_dark)
    
    d2.text((80, 70), "DAILY BAKE SELECTION", fill=terracotta, font=get_font(14, bold=True))
    d2.text((80, 100), "Artisanal Loaves & Morning Pastries", fill=brown_dark, font=get_font(32, bold=True))
    
    items = [
        ("San Francisco Sourdough", "$7.50", "Signature sourdough with blistered blister crust and airy crumb.", "Loaf • 800g"),
        ("Almond Double Croissant", "$5.25", "Twice-baked butter croissant with rich frangipane and toasted almonds.", "Pastry • Fresh 7AM"),
        ("Cardamom Morning Bun", "$4.75", "Laminated brioche rolled in Ceylon cinnamon, crushed cardamom & sugar.", "Pastry • Warm"),
        ("Seeded Multigrain Batard", "$8.00", "Flax, pumpkin, sesame, and sunflower seeds toasted before shaping.", "Loaf • 850g"),
        ("Pain au Chocolat", "$4.95", "French Valrhona 70% dark chocolate batons wrapped in 36 butter layers.", "Pastry • Crisp"),
        ("Rosemary Olive Focaccia", "$6.50", "Extra virgin olive oil dough topped with fresh rosemary & Kalamata olives.", "Slab • 400g"),
    ]
    for idx, (title, price, desc, meta) in enumerate(items):
        row = idx // 3
        col = idx % 3
        x = 80 + col * 360
        y = 170 + row * 280
        draw_card(d2, [x, y, x + 330, y + 250], fill=card_cream, border=(230, 220, 210), radius=14)
        # Category strip
        draw_card(d2, [x + 20, y + 20, x + 160, y + 46], fill=(245, 235, 225), radius=6)
        d2.text((x + 30, y + 26), meta, fill=terracotta, font=get_font(11, bold=True))
        
        d2.text((x + 20, y + 65), title, fill=brown_dark, font=get_font(18, bold=True))
        d2.text((x + 20, y + 95), desc, fill=muted_cream, font=get_font(13))
        d2.text((x + 20, y + 195), price, fill=terracotta, font=get_font(22, bold=True))
        draw_card(d2, [x + 210, y + 185, x + 310, y + 225], fill=brown_dark, radius=6)
        d2.text((x + 230, y + 197), "+ Add", fill=(255, 255, 255), font=get_font(13, bold=True))
    
    img2.save(os.path.join(GALLERY_DIR, "bloom-bakery-2.jpg"), quality=92)
    
    # --- Image 3: Packaging & Cup Mockups ---
    img3 = Image.new("RGB", (1200, 800), (238, 230, 218))
    d3 = ImageDraw.Draw(img3)
    d3.text((80, 60), "BLOOM BAKERY BRAND PACKAGING", fill=terracotta, font=get_font(14, bold=True))
    d3.text((80, 95), "Sustainable Kraft Paper & Cafe Collateral", fill=brown_dark, font=get_font(32, bold=True))
    
    # Bread Bag Mockup (Kraft paper color)
    draw_card(d3, [80, 180, 480, 720], fill=(210, 180, 145), border=(180, 150, 120), radius=16)
    d3.text((140, 260), "BLOOM BAKERY", fill=brown_dark, font=get_font(28, bold=True))
    d3.text((140, 305), "ESTD. 2024 • ARTISAN BAKERY", fill=terracotta, font=get_font(12, bold=True))
    d3.line([(140, 340), (420, 340)], fill=(170, 140, 110), width=1)
    d3.text((140, 370), "Freshly Stoneground\nNatural Wild Sourdough", fill=brown_dark, font=get_font(18))
    d3.text((140, 470), "Recyclable Unbleached Kraft Paper\nSoy-Based Inks Only", fill=(120, 95, 75), font=get_font(13))
    
    # Coffee Cup Mockup
    draw_card(d3, [540, 180, 820, 560], fill=(245, 240, 230), border=(215, 205, 195), radius=24)
    draw_card(d3, [540, 320, 820, 420], fill=(200, 170, 135), radius=0)
    d3.text((610, 355), "BLOOM CAFE", fill=brown_dark, font=get_font(20, bold=True))
    d3.text((600, 480), "Specialty Roasts & Bakes", fill=terracotta, font=get_font(14, bold=True))
    
    # Sticker labels mockup
    draw_card(d3, [880, 180, 1120, 420], fill=card_cream, border=(220, 210, 200), radius=16)
    d3.ellipse([940, 230, 1060, 350], fill=terracotta)
    d3.text((970, 280), "BLOOM", fill=(255, 255, 255), font=get_font(18, bold=True))
    d3.text((965, 370), "Die-cut jar seals", fill=muted_cream, font=get_font(12))
    
    # Menu board card
    draw_card(d3, [540, 600, 1120, 720], fill=brown_dark, radius=12)
    d3.text((580, 630), "CAFE SPECIALTY DRINKS", fill=terracotta, font=get_font(14, bold=True))
    d3.text((580, 665), "Oat Flat White $4.50  •  Filter Batch $3.75  •  Cardamom Chai $5.00", fill=(255, 255, 255), font=get_font(15))
    
    img3.save(os.path.join(GALLERY_DIR, "bloom-bakery-3.jpg"), quality=92)
    
    # --- Image 4: Mobile Ordering Screen ---
    img4 = Image.new("RGB", (1200, 800), bg_warm)
    d4 = ImageDraw.Draw(img4)
    d4.text((80, 60), "BLOOM MOBILE EXPERIENCE", fill=terracotta, font=get_font(14, bold=True))
    d4.text((80, 95), "Frictionless Pickup & Bakery Order Ahead", fill=brown_dark, font=get_font(32, bold=True))
    
    # Phone frame
    draw_card(d4, [400, 170, 800, 760], fill=card_cream, border=(215, 205, 195), radius=36)
    d4.rounded_rectangle([550, 182, 650, 202], radius=8, fill=(230, 220, 210))
    d4.text((440, 230), "Bloom Sourdough Order", fill=brown_dark, font=get_font(18, bold=True))
    
    draw_card(d4, [430, 275, 770, 360], fill=(248, 245, 238), radius=12)
    d4.text((450, 295), "Pickup Location", fill=terracotta, font=get_font(11, bold=True))
    d4.text((450, 320), "Downtown Bakery • Today, 8:30 AM", fill=brown_dark, font=get_font(14, bold=True))
    
    # Cart items
    cart = [
        ("1x Country Sourdough Loaf", "$7.50"),
        ("2x Warm Almond Croissant", "$10.50"),
        ("1x Oat Cortado Coffee", "$4.25"),
    ]
    for idx, (item, cost) in enumerate(cart):
        y_cart = 385 + idx * 60
        draw_card(d4, [430, y_cart, 770, y_cart + 50], fill=(255, 255, 255), border=(235, 225, 215), radius=8)
        d4.text((445, y_cart + 15), item, fill=brown_dark, font=get_font(13))
        d4.text((700, y_cart + 15), cost, fill=terracotta, font=get_font(13, bold=True))
    
    # Total & Checkout button
    d4.text((440, 585), "Total Due:", fill=brown_dark, font=get_font(16, bold=True))
    d4.text((710, 585), "$22.25", fill=terracotta, font=get_font(18, bold=True))
    draw_card(d4, [430, 630, 770, 690], fill=terracotta, radius=10)
    d4.text((540, 650), "PLACE ORDER", fill=(255, 255, 255), font=get_font(14, bold=True))
    
    img4.save(os.path.join(GALLERY_DIR, "bloom-bakery-4.jpg"), quality=92)
    print("Bloom Bakery images created successfully!")

# ==========================================
# 3. VELOCITY GYM (4 Images + Thumb)
# ==========================================
def make_velocity_images():
    print("Generating Velocity Gym images...")
    dark_bg = (13, 15, 18)
    card_bg = (22, 26, 32)
    neon_lime = (180, 255, 50)
    white = (255, 255, 255)
    muted = (150, 160, 175)
    
    # --- Image 1: Gym Web Portal ---
    img1 = Image.new("RGB", (1200, 800), dark_bg)
    d1 = ImageDraw.Draw(img1)
    draw_header_bar(d1, 1200, "Velocity Gym", "velocitygym.club")
    
    d1.text((80, 75), "VELOCITY // ATHLETICS", fill=neon_lime, font=get_font(20, bold=True))
    d1.text((80, 180), "PERFORMANCE FIRST.", fill=neon_lime, font=get_font(16, bold=True))
    d1.text((80, 220), "BREAK YOUR LIMITS.\nBUILD YOUR ENGINE.", fill=white, font=get_font(46, bold=True))
    d1.text((80, 350), "High-performance strength, conditioning, and recovery club.\nOlympic lifting zones, sprint turf, and infrared saunas.", fill=muted, font=get_font(16))
    
    draw_card(d1, [80, 430, 310, 490], fill=neon_lime, radius=8)
    d1.text((120, 450), "CLAIM 7-DAY PASS", fill=dark_bg, font=get_font(15, bold=True))
    
    draw_card(d1, [330, 430, 520, 490], fill=card_bg, border=neon_lime, radius=8)
    d1.text((360, 450), "CLASS TIMETABLE", fill=white, font=get_font(14, bold=True))
    
    # Big stat meters
    stats = [("450+", "Active Members"), ("32", "Weekly Classes"), ("12", "Pro Coaches"), ("04", "Recovery Zones")]
    for idx, (num, lbl) in enumerate(stats):
        x = 80 + idx * 260
        y = 570
        draw_card(d1, [x, y, x + 235, y + 140], fill=card_bg, border=(40, 48, 60), radius=12)
        d1.text((x + 25, y + 25), num, fill=neon_lime, font=get_font(36, bold=True))
        d1.text((x + 25, y + 85), lbl, fill=white, font=get_font(14))
        
    img1.save(os.path.join(GALLERY_DIR, "velocity-gym-1.jpg"), quality=92)
    img1.resize((800, 600), Image.Resampling.LANCZOS).save(os.path.join(MEDIA_DIR, "velocity-gym-thumb.jpg"), quality=90)
    
    # --- Image 2: Social Media Kit ---
    img2 = Image.new("RGB", (1200, 800), dark_bg)
    d2 = ImageDraw.Draw(img2)
    d2.text((80, 60), "VELOCITY GYM SOCIAL MEDIA KIT", fill=neon_lime, font=get_font(14, bold=True))
    d2.text((80, 95), "High-Impact Instagram Carousel & Story Templates", fill=white, font=get_font(32, bold=True))
    
    # 4 Mockup Post Cards
    posts = [
        ("WOD // HYROX 01", "5 Rounds for Time:\n• 1000m Row\n• 50 Sled Push\n• 40 Wall Balls\n• 20 Burpee Box Jumps"),
        ("COACH SPOTLIGHT", "Marcus Vance\nHead of Olympic Lifting\n'Form precedes weight. Always.'"),
        ("MEMBER GAINS", "Sarah K. — 12 Weeks\n+15kg Deadlift\n-6% Body Fat\n100% Commitment"),
        ("JOIN THE TRIBE", "Summer Season Passes\nUnlimited Classes\nSauna & Ice Plunge Access"),
    ]
    for idx, (p_title, p_desc) in enumerate(posts):
        x = 80 + idx * 265
        draw_card(d2, [x, 180, x + 245, 680], fill=card_bg, border=neon_lime if idx == 0 else (45, 55, 70), radius=16)
        draw_card(d2, [x + 20, 210, x + 225, 380], fill=(30, 36, 46), radius=10)
        d2.text((x + 40, 290), "VELOCITY", fill=neon_lime, font=get_font(20, bold=True))
        d2.text((x + 20, 410), p_title, fill=white, font=get_font(16, bold=True))
        d2.text((x + 20, 450), p_desc, fill=muted, font=get_font(13))
        draw_card(d2, [x + 20, 610, x + 225, 650], fill=neon_lime if idx == 0 else (40, 50, 65), radius=6)
        d2.text((x + 65, 622), "VIEW POST", fill=dark_bg if idx == 0 else white, font=get_font(12, bold=True))
        
    img2.save(os.path.join(GALLERY_DIR, "velocity-gym-2.jpg"), quality=92)
    
    # --- Image 3: Class Schedule ---
    img3 = Image.new("RGB", (1200, 800), dark_bg)
    d3 = ImageDraw.Draw(img3)
    draw_header_bar(d3, 1200, "Velocity - Timetable", "velocitygym.club/classes")
    d3.text((80, 70), "SCHEDULE & SESSIONS", fill=neon_lime, font=get_font(14, bold=True))
    d3.text((80, 100), "Daily Performance Schedule", fill=white, font=get_font(32, bold=True))
    
    classes = [
        ("06:00 AM", "HYROX Conditioning", "Coach Marcus", "Turf Zone 1", "Full"),
        ("07:30 AM", "Olympic Barbell Club", "Coach Elena", "Lifting Bay", "3 Spots Left"),
        ("12:00 PM", "MetCon Express (45m)", "Coach Dave", "Main Studio", "8 Spots Left"),
        ("05:30 PM", "Powerlifting Squad", "Coach Marcus", "Lifting Bay", "Full"),
        ("07:00 PM", "Cold Plunge & Breathwork", "Coach Maya", "Recovery Lab", "5 Spots Left"),
    ]
    for idx, (t, c_name, coach, loc, cap) in enumerate(classes):
        y = 170 + idx * 110
        draw_card(d3, [80, y, 1120, y + 85], fill=card_bg, border=(40, 50, 65), radius=10)
        d3.text((110, y + 28), t, fill=neon_lime, font=get_font(18, bold=True))
        d3.text((280, y + 20), c_name, fill=white, font=get_font(18, bold=True))
        d3.text((280, y + 48), f"{coach} • {loc}", fill=muted, font=get_font(13))
        d3.text((780, y + 30), cap, fill=(239, 68, 68) if cap == "Full" else neon_lime, font=get_font(14, bold=True))
        draw_card(d3, [960, y + 20, 1080, y + 65], fill=neon_lime if cap != "Full" else (40, 48, 60), radius=6)
        d3.text((990, y + 32), "BOOK" if cap != "Full" else "WAITLIST", fill=dark_bg if cap != "Full" else muted, font=get_font(12, bold=True))
        
    img3.save(os.path.join(GALLERY_DIR, "velocity-gym-3.jpg"), quality=92)
    
    # --- Image 4: Mobile Workout Tracker ---
    img4 = Image.new("RGB", (1200, 800), dark_bg)
    d4 = ImageDraw.Draw(img4)
    d4.text((80, 60), "VELOCITY COMPANION APP", fill=neon_lime, font=get_font(14, bold=True))
    d4.text((80, 95), "Member Digital Key & Real-Time Performance Analytics", fill=white, font=get_font(32, bold=True))
    
    # Phone frame
    draw_card(d4, [400, 170, 800, 760], fill=card_bg, border=(50, 65, 85), radius=36)
    d4.rounded_rectangle([550, 182, 650, 202], radius=8, fill=(13, 15, 18))
    d4.text((440, 230), "Today's Session", fill=white, font=get_font(20, bold=True))
    
    # Ring score
    draw_card(d4, [430, 280, 770, 420], fill=(28, 34, 44), border=neon_lime, radius=14)
    d4.text((455, 305), "Active Calorie Burn", fill=muted, font=get_font(13))
    d4.text((455, 335), "842 kcal", fill=neon_lime, font=get_font(34, bold=True))
    d4.text((455, 385), "Heart Rate: 164 bpm  •  Zone 4", fill=white, font=get_font(12))
    
    # Exercise log
    draw_card(d4, [430, 440, 770, 520], fill=(28, 34, 44), radius=10)
    d4.text((455, 455), "Back Squat", fill=white, font=get_font(15, bold=True))
    d4.text((455, 485), "4 Sets x 6 Reps @ 120kg ✓ Complete", fill=neon_lime, font=get_font(12))
    
    draw_card(d4, [430, 540, 770, 620], fill=(28, 34, 44), radius=10)
    d4.text((455, 555), "Sled Push Intervals", fill=white, font=get_font(15, bold=True))
    d4.text((455, 585), "6 Sets x 30m @ 80kg ✓ Complete", fill=neon_lime, font=get_font(12))
    
    # QR check-in
    draw_card(d4, [430, 645, 770, 715], fill=neon_lime, radius=10)
    d4.text((535, 668), "TAP FOR GYM BARCODE", fill=dark_bg, font=get_font(13, bold=True))
    
    img4.save(os.path.join(GALLERY_DIR, "velocity-gym-4.jpg"), quality=92)
    print("Velocity Gym images created successfully!")

# ==========================================
# 4. GRIND COFFEE CO. (4 Images + Thumb)
# ==========================================
def make_grind_images():
    print("Generating Grind Coffee Co. images...")
    bg_coffee = (24, 18, 15)
    card_coffee = (36, 28, 24)
    copper = (212, 145, 90)
    cream = (245, 238, 230)
    muted = (160, 145, 135)
    
    # --- Image 1: Specialty Roasters Hero ---
    img1 = Image.new("RGB", (1200, 800), bg_coffee)
    d1 = ImageDraw.Draw(img1)
    draw_header_bar(d1, 1200, "Grind Coffee Co.", "grindcoffeeco.com", bg_color=(20, 15, 12), text_color=copper)
    
    d1.text((80, 75), "GRIND COFFEE CO. // ROASTERY", fill=copper, font=get_font(20, bold=True))
    d1.text((80, 180), "SINGLE ORIGIN. DIRECT TRADE.", fill=copper, font=get_font(14, bold=True))
    d1.text((80, 215), "Coffee Sourced at Origin.\nRoasted with Precision.", fill=cream, font=get_font(44, bold=True))
    d1.text((80, 340), "Ethically sourced from high-altitude micro-lots in Ethiopia, Colombia, and Kenya.\nFreshly roasted every Tuesday and shipped within 24 hours.", fill=muted, font=get_font(16))
    
    draw_card(d1, [80, 420, 280, 480], fill=copper, radius=8)
    d1.text((115, 440), "Shop Fresh Roasts", fill=bg_coffee, font=get_font(15, bold=True))
    
    # Feature Roasts
    roasts = [
        ("ETHIOPIA GUJI", "Light Roast • Heirloom", "Jasmine, Wild Honey, Bergamot"),
        ("COLOMBIA HUILA", "Medium Roast • Castillo", "Brown Sugar, Red Apple, Cocoa"),
        ("KENYA NYERI", "Light Roast • SL28/SL34", "Blackcurrant, Grapefruit, Cane Sugar"),
    ]
    for idx, (r_name, r_meta, r_notes) in enumerate(roasts):
        x = 80 + idx * 360
        y = 540
        draw_card(d1, [x, y, x + 330, y + 190], fill=card_coffee, border=(60, 48, 40), radius=12)
        d1.text((x + 25, y + 25), r_name, fill=cream, font=get_font(18, bold=True))
        d1.text((x + 25, y + 55), r_meta, fill=copper, font=get_font(13, bold=True))
        d1.text((x + 25, y + 95), f"Tasting Notes:\n{r_notes}", fill=muted, font=get_font(13))
        
    img1.save(os.path.join(GALLERY_DIR, "grind-coffee-co-1.jpg"), quality=92)
    img1.resize((800, 600), Image.Resampling.LANCZOS).save(os.path.join(MEDIA_DIR, "grind-coffee-co-thumb.jpg"), quality=90)
    
    # --- Image 2: Matte Coffee Bag Packaging ---
    img2 = Image.new("RGB", (1200, 800), (20, 15, 12))
    d2 = ImageDraw.Draw(img2)
    d2.text((80, 60), "PACKAGING SYSTEM & LABELS", fill=copper, font=get_font(14, bold=True))
    d2.text((80, 95), "Matte Charcoal & Copper Foil Bag Mockups", fill=cream, font=get_font(32, bold=True))
    
    # Coffee Bag 1 (Ethiopia)
    draw_card(d2, [140, 180, 580, 720], fill=(28, 22, 18), border=copper, radius=18)
    draw_card(d2, [180, 220, 540, 360], fill=(38, 30, 25), radius=10)
    d2.text((220, 250), "GRIND COFFEE CO.", fill=copper, font=get_font(24, bold=True))
    d2.text((220, 290), "SPECIALTY COFFEE ROASTERS", fill=muted, font=get_font(12, bold=True))
    
    draw_card(d2, [180, 390, 540, 640], fill=cream, radius=10)
    d2.text((210, 420), "ETHIOPIA GUJI", fill=bg_coffee, font=get_font(24, bold=True))
    d2.text((210, 460), "Washed Process • 2,100 MASL", fill=copper, font=get_font(13, bold=True))
    d2.text((210, 500), "Flavour Profile: Peach, Jasmine blossom,\nraw honey & citrus sweetness.", fill=(80, 65, 55), font=get_font(14))
    d2.text((210, 570), "Net Wt: 250g  |  Whole Bean", fill=bg_coffee, font=get_font(13, bold=True))
    
    # Coffee Bag 2 (Colombia)
    draw_card(d2, [640, 180, 1080, 720], fill=(28, 22, 18), border=(65, 52, 44), radius=18)
    draw_card(d2, [680, 220, 1040, 360], fill=(38, 30, 25), radius=10)
    d2.text((720, 250), "GRIND COFFEE CO.", fill=copper, font=get_font(24, bold=True))
    d2.text((720, 290), "SPECIALTY COFFEE ROASTERS", fill=muted, font=get_font(12, bold=True))
    
    draw_card(d2, [680, 390, 1040, 640], fill=(42, 34, 28), border=copper, radius=10)
    d2.text((710, 420), "COLOMBIA HUILA", fill=cream, font=get_font(24, bold=True))
    d2.text((710, 460), "Anaerobic Ferment • 1,850 MASL", fill=copper, font=get_font(13, bold=True))
    d2.text((710, 500), "Flavour Profile: Milk chocolate, toffee,\nbaked red apple & caramel.", fill=muted, font=get_font(14))
    d2.text((710, 570), "Net Wt: 250g  |  Whole Bean", fill=cream, font=get_font(13, bold=True))
    
    img2.save(os.path.join(GALLERY_DIR, "grind-coffee-co-2.jpg"), quality=92)
    
    # --- Image 3: Subscription & Online Shop ---
    img3 = Image.new("RGB", (1200, 800), bg_coffee)
    d3 = ImageDraw.Draw(img3)
    draw_header_bar(d3, 1200, "Grind Coffee Co. - Subscription", "grindcoffeeco.com/subscribe", bg_color=(20, 15, 12), text_color=copper)
    
    d3.text((80, 70), "ROASTER SUBSCRIPTIONS", fill=copper, font=get_font(14, bold=True))
    d3.text((80, 100), "Never Run Out of Exceptional Coffee", fill=cream, font=get_font(32, bold=True))
    
    plans = [
        ("The Explorer", "$18 / bag", "Fortnightly", "A curated rotation of rare single origins from Africa & Latin America.", True),
        ("The House Reserve", "$16 / bag", "Weekly", "Our balanced, versatile espresso blend designed for milk drinks & stove.", False),
        ("Cold Brew Box", "$28 / pack", "Monthly", "Coarse ground steep pouches with ultra-low acidity and chocolate notes.", False),
    ]
    for idx, (p_name, p_price, freq, desc, featured) in enumerate(plans):
        x = 80 + idx * 360
        draw_card(d3, [x, 180, x + 330, y + 490], fill=card_coffee, border=copper if featured else (55, 42, 34), radius=14)
        if featured:
            draw_card(d3, [x + 20, 200, x + 180, 230], fill=copper, radius=6)
            d3.text((x + 35, 208), "MOST POPULAR", fill=bg_coffee, font=get_font(11, bold=True))
        d3.text((x + 25, 250), p_name, fill=cream, font=get_font(22, bold=True))
        d3.text((x + 25, 290), p_price, fill=copper, font=get_font(26, bold=True))
        d3.text((x + 25, 330), f"Delivered {freq}", fill=muted, font=get_font(13))
        d3.text((x + 25, 380), desc, fill=muted, font=get_font(14))
        draw_card(d3, [x + 25, 550, x + 305, 610], fill=copper if featured else (50, 38, 30), radius=8)
        d3.text((x + 95, 568), "SELECT PLAN", fill=bg_coffee if featured else cream, font=get_font(14, bold=True))
        
    img3.save(os.path.join(GALLERY_DIR, "grind-coffee-co-3.jpg"), quality=92)
    
    # --- Image 4: Brand Identity & Emblem ---
    img4 = Image.new("RGB", (1200, 800), bg_coffee)
    d4 = ImageDraw.Draw(img4)
    d4.text((80, 60), "VISUAL IDENTITY & CRAFT EMBLEMS", fill=copper, font=get_font(14, bold=True))
    d4.text((80, 95), "Typography, Monograms & Cafe Environmental Signage", fill=cream, font=get_font(32, bold=True))
    
    # Emblem Card
    draw_card(d4, [80, 180, 580, 720], fill=card_coffee, border=(60, 48, 40), radius=16)
    d4.ellipse([230, 260, 430, 460], outline=copper, width=3)
    d4.ellipse([245, 275, 415, 445], outline=(80, 60, 50), width=1)
    d4.text((290, 330), "GRIND", fill=cream, font=get_font(24, bold=True))
    d4.text((300, 365), "COFFEE CO.", fill=copper, font=get_font(12, bold=True))
    d4.text((315, 395), "100%", fill=muted, font=get_font(10))
    
    d4.text((140, 520), "Primary Circular Seal", fill=cream, font=get_font(18, bold=True))
    d4.text((140, 555), "Used for rubber stamps, cup sleeves, and exterior cast brass signage.", fill=muted, font=get_font(14))
    
    # Collateral cards on right
    draw_card(d4, [640, 180, 1120, 420], fill=(30, 24, 20), border=copper, radius=14)
    d4.text((680, 220), "Cafe Menu Board Specification", fill=copper, font=get_font(16, bold=True))
    d4.text((680, 260), "Hand-routed walnut timber rails with matte magnetic\noff-white acrylic type glyphs.", fill=cream, font=get_font(14))
    
    draw_card(d4, [640, 460, 1120, 720], fill=(30, 24, 20), border=(60, 48, 40), radius=14)
    d4.text((680, 500), "Tasting Cards & Roaster Log", fill=copper, font=get_font(16, bold=True))
    d4.text((680, 540), "FSC-certified heavyweight cotton cardstock included\nin every coffee shipment with brew recipes.", fill=cream, font=get_font(14))
    
    img4.save(os.path.join(GALLERY_DIR, "grind-coffee-co-4.jpg"), quality=92)
    print("Grind Coffee images created successfully!")

# ==========================================
# 5. APEX REAL ESTATE (4 Images + Thumb)
# ==========================================
def make_apex_images():
    print("Generating Apex Real Estate images...")
    dark_slate = (15, 18, 23)
    card_slate = (24, 29, 38)
    gold = (212, 175, 55)
    white = (255, 255, 255)
    muted = (155, 165, 180)
    
    # --- Image 1: Luxury Showcase Landing Page ---
    img1 = Image.new("RGB", (1200, 800), dark_slate)
    d1 = ImageDraw.Draw(img1)
    draw_header_bar(d1, 1200, "Apex Luxury Real Estate", "apexestates.luxury/penthouse")
    
    d1.text((80, 75), "APEX // PRIVATE CLIENTS", fill=gold, font=get_font(20, bold=True))
    d1.text((80, 180), "EXCLUSIVE LISTING • THE PACIFIC HEIGHTS TOWER", fill=gold, font=get_font(14, bold=True))
    d1.text((80, 215), "The Sky Residence.\nPanoramic Ocean Views.", fill=white, font=get_font(44, bold=True))
    d1.text((80, 340), "5,200 sq.ft private penthouse with 360° floor-to-ceiling glass,\nprivate lift, infinity plunge pool, and 4 dedicated garage suites.", fill=muted, font=get_font(16))
    
    d1.text((80, 430), "$4,850,000 USD", fill=gold, font=get_font(34, bold=True))
    draw_card(d1, [420, 420, 660, 480], fill=gold, radius=8)
    d1.text((455, 442), "REQUEST PRIVATE VIEWING", fill=dark_slate, font=get_font(13, bold=True))
    
    # Key property specs
    specs = [("5,200", "Interior Sq. Ft."), ("4 / 4.5", "Beds & Baths"), ("360°", "Panorama Terrace"), ("04", "Enclosed Parking")]
    for idx, (val, lbl) in enumerate(specs):
        x = 80 + idx * 260
        y = 560
        draw_card(d1, [x, y, x + 235, y + 150], fill=card_slate, border=(45, 55, 72), radius=12)
        d1.text((x + 25, y + 30), val, fill=gold, font=get_font(30, bold=True))
        d1.text((x + 25, y + 90), lbl, fill=white, font=get_font(14))
        
    img1.save(os.path.join(GALLERY_DIR, "apex-real-estate-1.jpg"), quality=92)
    img1.resize((800, 600), Image.Resampling.LANCZOS).save(os.path.join(MEDIA_DIR, "apex-real-estate-thumb.jpg"), quality=90)
    
    # --- Image 2: Interactive Listing & Floor Plan ---
    img2 = Image.new("RGB", (1200, 800), dark_slate)
    d2 = ImageDraw.Draw(img2)
    draw_header_bar(d2, 1200, "Apex - Floorplan", "apexestates.luxury/residence-plan")
    
    d2.text((80, 70), "ARCHITECTURAL BLUEPRINT & LEVEL 42 SPEC", fill=gold, font=get_font(14, bold=True))
    d2.text((80, 100), "Level 42 Penthouse Floor Plan & Specs", fill=white, font=get_font(32, bold=True))
    
    # Blueprint box
    draw_card(d2, [80, 170, 720, 720], fill=(20, 25, 34), border=(45, 60, 80), radius=16)
    # Floorplan lines
    d2.rectangle([130, 220, 670, 670], outline=gold, width=2)
    d2.line([(400, 220), (400, 670)], fill=(50, 70, 95), width=2)
    d2.line([(130, 445), (670, 445)], fill=(50, 70, 95), width=2)
    d2.text((150, 240), "MASTER SUITE (28' x 20')", fill=white, font=get_font(14, bold=True))
    d2.text((420, 240), "GRAND SALON & DINING (34' x 24')", fill=white, font=get_font(14, bold=True))
    d2.text((150, 465), "CHEF'S KITCHEN & PANTRY", fill=white, font=get_font(14, bold=True))
    d2.text((420, 465), "OCEANFRONT TERRACE (40' x 16')", fill=gold, font=get_font(14, bold=True))
    
    # Detail specs card on right
    draw_card(d2, [760, 170, 1120, 720], fill=card_slate, border=(45, 55, 72), radius=16)
    d2.text((800, 210), "FINISHES & AMENITIES", fill=gold, font=get_font(16, bold=True))
    amenities = [
        "Calacatta Oro Italian marble slab islands",
        "Sub-Zero & Wolf integrated appliances",
        "European white oak herringbone flooring",
        "Smart home Lutron automated solar shades",
        "24/7 White-glove concierge and valet",
        "Private wine tasting room with lockbox",
    ]
    for idx, am in enumerate(amenities):
        d2.text((800, 260 + idx * 55), f"• {am}", fill=white, font=get_font(13))
        
    img2.save(os.path.join(GALLERY_DIR, "apex-real-estate-2.jpg"), quality=92)
    
    # --- Image 3: Mobile Property App & Tour ---
    img3 = Image.new("RGB", (1200, 800), dark_slate)
    d3 = ImageDraw.Draw(img3)
    d3.text((80, 60), "APEX MOBILE PORTFOLIO", fill=gold, font=get_font(14, bold=True))
    d3.text((80, 95), "Ultra-Luxury Property Discovery on Mobile", fill=white, font=get_font(32, bold=True))
    
    # Phone frame
    draw_card(d3, [400, 170, 800, 760], fill=card_slate, border=(60, 75, 95), radius=36)
    d3.rounded_rectangle([550, 182, 650, 202], radius=8, fill=(15, 18, 23))
    d3.text((440, 230), "Apex Portfolio", fill=white, font=get_font(20, bold=True))
    
    # Listing preview
    draw_card(d3, [430, 275, 770, 480], fill=(18, 22, 28), border=gold, radius=14)
    d3.text((450, 300), "The Pacific Penthouse", fill=white, font=get_font(18, bold=True))
    d3.text((450, 330), "$4,850,000 USD", fill=gold, font=get_font(22, bold=True))
    d3.text((450, 370), "San Francisco • Pacific Heights", fill=muted, font=get_font(12))
    d3.text((450, 400), "5,200 sq.ft • 4 Beds • 4.5 Baths", fill=white, font=get_font(12))
    
    # Agent card
    draw_card(d3, [430, 505, 770, 610], fill=(30, 36, 48), radius=12)
    d3.text((450, 525), "Listing Director", fill=gold, font=get_font(11, bold=True))
    d3.text((450, 550), "Julian Sterling, Private Client Adv.", fill=white, font=get_font(14, bold=True))
    d3.text((450, 575), "+1 (415) 890-4421 • Direct WhatsApp", fill=muted, font=get_font(12))
    
    # Booking CTA
    draw_card(d3, [430, 635, 770, 700], fill=gold, radius=10)
    d3.text((515, 658), "SCHEDULE PRIVATE VIP TOUR", fill=dark_slate, font=get_font(12, bold=True))
    
    img3.save(os.path.join(GALLERY_DIR, "apex-real-estate-3.jpg"), quality=92)
    
    # --- Image 4: Presentation Deck & Collateral ---
    img4 = Image.new("RGB", (1200, 800), dark_slate)
    d4 = ImageDraw.Draw(img4)
    d4.text((80, 60), "INVESTOR & BUYER COLLATERAL", fill=gold, font=get_font(14, bold=True))
    d4.text((80, 95), "Embossed Lookbooks & Private Client Collateral", fill=white, font=get_font(32, bold=True))
    
    # Presentation folder
    draw_card(d4, [80, 180, 580, 720], fill=(22, 26, 34), border=gold, radius=16)
    d4.text((140, 260), "APEX", fill=gold, font=get_font(36, bold=True))
    d4.text((140, 310), "PRIVATE ESTATES PORTFOLIO", fill=white, font=get_font(14, bold=True))
    d4.line([(140, 350), (520, 350)], fill=(50, 60, 75), width=1)
    d4.text((140, 390), "Exclusive Offering Memorandum\nStrictly Confidential", fill=muted, font=get_font(16))
    
    # Hardcover lookbook on right
    draw_card(d4, [640, 180, 1120, 720], fill=(28, 33, 44), border=(60, 75, 95), radius=16)
    d4.text((680, 220), "Bespoke Bound Property Monograph", fill=gold, font=get_font(18, bold=True))
    d4.text((680, 260), "Hardcover linen binding with debossed gold foil monogram.\nDelivered by courier to accredited high-net-worth buyers.", fill=white, font=get_font(14))
    
    # Card mockup
    draw_card(d4, [680, 380, 1080, 650], fill=(16, 20, 27), border=gold, radius=12)
    d4.text((720, 430), "Julian Sterling", fill=white, font=get_font(22, bold=True))
    d4.text((720, 465), "Principal Broker & Partner", fill=gold, font=get_font(14))
    d4.text((720, 520), "julian@apexestates.luxury", fill=muted, font=get_font(14))
    d4.text((720, 550), "San Francisco • Pebble Beach • Aspen", fill=muted, font=get_font(13))
    
    img4.save(os.path.join(GALLERY_DIR, "apex-real-estate-4.jpg"), quality=92)
    print("Apex Real Estate images created successfully!")

if __name__ == '__main__':
    make_novatech_images()
    make_bloom_images()
    make_velocity_images()
    make_grind_images()
    make_apex_images()
    print("All project images successfully generated!")
