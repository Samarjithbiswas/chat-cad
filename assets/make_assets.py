"""Regenerate the README graphics.

    python assets/make_assets.py

Every visual property is written as an SVG presentation attribute rather than through
an internal <style> block. Internal CSS is dropped by several SVG rasterisers, so a
stylesheet-driven file looks correct in a browser and comes out half-empty everywhere
else. Attributes render identically in all of them.

Animation uses SMIL (<animate>, <animateMotion>, <animateTransform>), which GitHub
serves through its image proxy and browsers play inside an <img>. GitHub strips
<script>, so there is none here.
"""

from pathlib import Path

OUT = Path(__file__).parent
FONT = "'Segoe UI', system-ui, -apple-system, Helvetica, Arial, sans-serif"

INK = "#e6edf3"
MUTED = "#8b949e"
DIM = "#6e7f91"
CARD = "#151c25"
EDGE = "#263442"
TEAL = "#2dd4bf"
BLUE = "#60a5fa"
AMBER = "#fbbf24"
GREEN = "#34d399"
VIOLET = "#a78bfa"
RED = "#f87171"
CYAN = "#22d3ee"
PINK = "#e879f9"


def txt(x, y, s, size=12, fill=MUTED, weight="400", anchor="start", spacing=None):
    sp = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{sp}>{s}</text>'
    )


def card(x, y, w, h, accent=None, fill=CARD, stroke=EDGE, r=10):
    out = (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="1.1"/>'
    )
    if accent:
        out += (
            f'<rect x="{x}" y="{y}" width="{w}" height="3.2" rx="1.6" fill="{accent}"/>'
        )
    return out


def frame(w, h, top="#0d1117", bot="#0b1620", gid="bg"):
    return (
        f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0%" stop-color="{top}"/><stop offset="100%" stop-color="{bot}"/>'
        f"</linearGradient></defs>"
        f'<rect width="{w}" height="{h}" rx="14" fill="url(#{gid})"/>'
        f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="14" '
        f'fill="none" stroke="#233240" stroke-width="1"/>'
    )


def svg(w, h, body, label):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
        f'width="{w}" height="{h}" role="img" aria-label="{label}">\n'
        + body
        + "\n</svg>\n"
    )


def eyebrow(x, y, s):
    return txt(x, y, s, size=12, fill=DIM, weight="700", spacing="1.4")


# --------------------------------------------------------------------------- hero
def hero():
    w, h = 1200, 340
    p = [frame(w, h, "#0d1117", "#0b1620", "hbg")]

    p.append(
        '<defs>'
        '<linearGradient id="acc" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="{TEAL}"/><stop offset="50%" stop-color="{BLUE}"/>'
        f'<stop offset="100%" stop-color="{AMBER}"/></linearGradient>'
        '<linearGradient id="swp" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="{TEAL}" stop-opacity="0"/>'
        f'<stop offset="50%" stop-color="{TEAL}" stop-opacity="0.9"/>'
        f'<stop offset="100%" stop-color="{TEAL}" stop-opacity="0"/></linearGradient>'
        '</defs>'
    )

    # faint grid
    p.append('<g stroke="#1b2632" stroke-width="1">')
    for y in (85, 170, 255):
        p.append(f'<path d="M0 {y}h1200"/>')
    for x in range(150, 1200, 150):
        p.append(f'<path d="M{x} 0v340"/>')
    p.append("</g>")

    # rotating isometric wireframe
    p.append('<g transform="translate(990 170)">')
    p.append("<g>")
    p.append(
        '<animateTransform attributeName="transform" type="rotate" '
        'from="0" to="360" dur="28s" repeatCount="indefinite"/>'
    )
    for d, op, col in (
        ("M0,-74 L64,-37 L64,37 L0,74 L-64,37 L-64,-37 Z", 0.34, TEAL),
        ("M0,-52 L45,-26 L45,26 L0,52 L-45,26 L-45,-26 Z", 0.26, TEAL),
        (
            "M0,-74 L0,-52 M64,-37 L45,-26 M64,37 L45,26 "
            "M0,74 L0,52 M-64,37 L-45,26 M-64,-37 L-45,-26",
            0.22,
            TEAL,
        ),
        ("M-94 0 H94 M0 -94 V94", 0.16, BLUE),
    ):
        p.append(
            f'<path d="{d}" fill="none" stroke="{col}" '
            f'stroke-opacity="{op}" stroke-width="1.1"/>'
        )
    p.append(
        f'<circle r="22" fill="none" stroke="{BLUE}" '
        f'stroke-opacity="0.24" stroke-width="1.1"/>'
    )
    p.append("</g>")
    p.append(f'<circle r="3" fill="{TEAL}">')
    p.append(
        '<animate attributeName="r" values="2.4;4.4;2.4" dur="2.8s" repeatCount="indefinite"/>'
    )
    p.append("</circle>")
    p.append("</g>")

    p.append(txt(58, 112, "Chat CAD", size=60, fill=INK, weight="700", spacing="-1.2"))
    p.append('<rect x="58" y="128" width="132" height="4" rx="2" fill="url(#acc)"/>')
    p.append(
        txt(
            58,
            178,
            "Describe a part in plain English. Get real CAD out.",
            size=21,
            fill="#93b7c9",
            weight="500",
        )
    )
    p.append(
        txt(
            58,
            209,
            "B-rep kernel &#183; 5-agent design loop &#183; STEP / STL / drawing PDF "
            "&#183; real FEA",
            size=15.5,
            fill="#7d8ea0",
        )
    )

    p.append('<rect x="58" y="232" width="620" height="2" rx="1" fill="#233240"/>')
    p.append(
        '<rect x="58" y="231.2" width="200" height="3.6" rx="1.8" fill="url(#swp)">'
        '<animate attributeName="x" values="58;478;58" dur="5.4s" repeatCount="indefinite"/>'
        "</rect>"
    )

    chips = [
        ("CadQuery", 112, "#132b2a", TEAL, "#5eead4"),
        ("OpenCascade", 130, "#14212f", BLUE, "#93c5fd"),
        ("Three.js", 96, "#2a2415", AMBER, "#fcd34d"),
        ("scikit-fem", 108, "#1c2430", "#8b949e", "#adbac7"),
        ("bring-your-own LLM", 168, "#1c2430", "#8b949e", "#adbac7"),
    ]
    x = 58
    for lab, cw, bg, bd, fg in chips:
        p.append(
            f'<rect x="{x}" y="258" width="{cw}" height="30" rx="15" fill="{bg}" '
            f'stroke="{bd}" stroke-opacity="0.5" stroke-width="1"/>'
        )
        p.append(txt(x + cw / 2, 278, lab, size=13.5, fill=fg, weight="600", anchor="middle"))
        x += cw + 12

    return svg(w, h, "\n".join(p), "Chat CAD: chat-driven mechanical CAD with a real B-rep kernel")


# ----------------------------------------------------------------------- pipeline
def pipeline():
    w, h = 1200, 300
    p = [frame(w, h, "#0d1117", "#0b1620", "pbg")]
    p.append(
        '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0,1 L9,5 L0,9 z" fill="#3d5165"/></marker></defs>'
    )
    p.append(eyebrow(30, 34, "THE LOOP"))

    for a, b in ((148, 302), (450, 524), (672, 746), (894, 968)):
        p.append(
            f'<path d="M{a} 150 H{b}" stroke="#2b3a48" stroke-width="2" '
            f'fill="none" marker-end="url(#ah)"/>'
        )

    for col, r, dur, begin in ((TEAL, 4.2, "4.8s", "0s"), (BLUE, 3.2, "4.8s", "1.6s")):
        p.append(
            f'<circle r="{r}" fill="{col}">'
            f'<animateMotion dur="{dur}" begin="{begin}" repeatCount="indefinite" '
            f'path="M148,150 H968"/>'
            f'<animate attributeName="opacity" values="0;1;1;0" dur="{dur}" '
            f'begin="{begin}" repeatCount="indefinite"/></circle>'
        )

    stages = [
        (24, 104, 124, 92, TEAL, "Chat", ["plain English", "or typed command"]),
        (302, 86, 148, 128, VIOLET, "5-agent loop",
         ["Planner", "Modeler", "Visual critic", "DFM &#183; Standards"]),
        (524, 104, 148, 92, BLUE, "B-rep kernel", ["CadQuery /", "OpenCascade"]),
        (746, 104, 148, 92, AMBER, "Viewport",
         ["feature tree, gizmos", "19 PBR materials"]),
        (968, 86, 208, 128, GREEN, "Ship it",
         ["STEP &#183; STL &#183; 4-view PDF", "linear-elastic FEA",
          "steady-state thermal", "assembly STEP"]),
    ]
    for x, y, cw, ch, accent, title, lines in stages:
        cx = x + cw / 2
        p.append(card(x, y, cw, ch, accent))
        p.append(txt(cx, y + 36, title, size=15, fill=INK, weight="700", anchor="middle"))
        for i, ln in enumerate(lines):
            p.append(txt(cx, y + 56 + i * 17, ln, size=12.5, fill=MUTED, anchor="middle"))

    p.append(
        f'<path d="M376 214 C376 258, 200 258, 148 214" fill="none" stroke="{VIOLET}" '
        f'stroke-opacity="0.5" stroke-width="1.6" stroke-dasharray="5 4" '
        f'marker-end="url(#ah)"/>'
    )
    p.append(
        txt(262, 276, "critic rejects &#8594; re-model before you ship",
            size=12.5, fill=VIOLET, anchor="middle")
    )
    return svg(w, h, "\n".join(p),
               "Pipeline from chat prompt through the agent loop and B-rep kernel to export and simulation")


# ------------------------------------------------------------------------- agents
def agents():
    w, h = 1000, 380
    p = [frame(w, h, "#0d1117", "#100e1a", "abg")]
    p.append(eyebrow(28, 32, "WHO CHECKS THE WORK"))
    p.append(
        '<circle cx="500" cy="200" r="128" fill="none" stroke="#302b46" '
        'stroke-width="1.2" stroke-dasharray="3 5"/>'
    )
    p.append("<g>")
    p.append(
        '<animateTransform attributeName="transform" type="rotate" '
        'from="0 500 200" to="360 500 200" dur="9s" repeatCount="indefinite"/>'
    )
    p.append(f'<circle cx="500" cy="72" r="13" fill="{VIOLET}" opacity="0.18"/>')
    p.append(f'<circle cx="500" cy="72" r="6" fill="{VIOLET}" opacity="0.9"/>')
    p.append("</g>")

    p.append(
        '<circle cx="500" cy="200" r="60" fill="#191428" stroke="#463a6b" stroke-width="1.4"/>'
    )
    p.append(txt(500, 196, "design", size=16, fill="#d8c9ff", weight="700", anchor="middle"))
    p.append(txt(500, 216, "loop", size=16, fill="#d8c9ff", weight="700", anchor="middle"))
    p.append(txt(500, 236, "iterate until clean", size=11.5, fill="#8b7fb0", anchor="middle"))

    p.append('<g stroke="#3a3355" stroke-width="1.2">')
    for d in ("M500 140 L500 96", "M548 178 L636 140", "M548 226 L618 268",
              "M452 226 L382 268", "M452 178 L364 140"):
        p.append(f'<path d="{d}"/>')
    p.append("</g>")

    boxes = [
        (404, 44, TEAL, "1 &#183; Planner", "breaks the prompt into steps"),
        (640, 112, BLUE, "2 &#183; Modeler", "calls the CAD operations"),
        (622, 266, AMBER, "3 &#183; Visual critic", "looks at the render, vision LLM"),
        (186, 266, RED, "4 &#183; DFM critic", "wall too thin, draft, radii"),
        (168, 112, GREEN, "5 &#183; Standards critic", "your saved rules, TF-IDF RAG"),
    ]
    for x, y, col, name, role in boxes:
        p.append(
            f'<rect x="{x}" y="{y}" width="192" height="50" rx="9" fill="#171e28" '
            f'stroke="{col}" stroke-opacity="0.55" stroke-width="1.1"/>'
        )
        p.append(txt(x + 96, y + 22, name, size=14.5, fill=INK, weight="700", anchor="middle"))
        p.append(txt(x + 96, y + 40, role, size=12, fill=MUTED, anchor="middle"))

    p.append(
        txt(500, 360, "the critics run before you export, not after you machine it",
            size=12, fill="#7d6ea8", anchor="middle")
    )
    return svg(w, h, "\n".join(p),
               "The five agents: planner, modeler, visual critic, DFM critic and standards critic")


# ------------------------------------------------------------------- capabilities
def capabilities():
    w, h = 1200, 360
    p = [frame(w, h, "#0d1117", "#0b1620", "cbg")]
    p.append(eyebrow(28, 32, "WHAT IT CAN BUILD"))

    p.append(card(24, 52, 176, 128))
    p.append(txt(112, 112, "140+", size=44, fill="#5eead4", weight="700", anchor="middle"))
    p.append(txt(112, 136, "chat-callable", size=13, fill="#7d8ea0", anchor="middle"))
    p.append(txt(112, 153, "operations", size=13, fill="#7d8ea0", anchor="middle"))
    p.append('<rect x="48" y="164" width="128" height="3" rx="1.5" fill="#233240"/>')
    p.append(
        f'<rect x="48" y="163.4" width="40" height="4.2" rx="2.1" fill="{TEAL}">'
        '<animate attributeName="x" values="48;136;48" dur="4.6s" repeatCount="indefinite"/>'
        "</rect>"
    )

    p.append(card(24, 196, 176, 140))
    p.append(txt(44, 222, "One-command", size=14, fill=INK, weight="700"))
    p.append(txt(44, 240, "assemblies", size=14, fill=INK, weight="700"))
    for i, s in enumerate(["turbojet", "turbofan", "gear_train", "bolt_stack &#183; engine"]):
        p.append(txt(44, 264 + i * 18, s, size=11.8, fill=MUTED))

    cards = [
        (216, 52, 230, 128, TEAL, "Solids &amp; sketches",
         ["primitives, booleans, fillet, chamfer", "shell, draft, revolve, loft, sweep",
          "2D sketcher with a constraint solver", "pattern, mirror, transform gizmos"]),
        (462, 52, 230, 128, BLUE, "Assemblies",
         ["cq.Assembly with mate solving", "joints, alignment, interference",
          "bill of materials", "assembly STEP export"]),
        (708, 52, 230, 128, AMBER, "Sheet metal &amp; profiles",
         ["sheet, L-bend, U-bend, box, flange", "T-slot extrusion, I-beam, angle",
          "tube, C-channel", "structural framing"]),
        (954, 52, 222, 128, GREEN, "Library parts",
         ["M-bolt with real thread, nut", "washer, bearing, hinge",
          "pulley, gear, spring", "drop-in and mate"]),
        (216, 196, 230, 140, VIOLET, "Aerospace mockups",
         ["turbine wheel, compressor stage", "combustor, nozzle, propeller",
          "NACA airfoil", "honeycomb core"]),
        (462, 196, 230, 140, RED, "Simulation",
         ["linear-elastic FEA", "steady-state thermal", "gmsh meshing",
          "scikit-fem solve, subprocess", "on the same B-rep geometry"]),
        (708, 196, 230, 140, CYAN, "Documentation out",
         ["4-view engineering drawing PDF", "dimension arrows, title block",
          "mass-properties summary", "STEP and STL"]),
        (954, 196, 222, 140, PINK, "Your rules, remembered",
         ["save a note once", "&#8220;M4 bolts always&#8221;",
          "&#8220;wall &#8805; 3 mm for FDM&#8221;",
          "retrieved into every", "agent prompt"]),
    ]
    for x, y, cw, ch, accent, title, items in cards:
        p.append(card(x, y, cw, ch, accent))
        p.append(txt(x + 22, y + 28, title, size=14, fill=INK, weight="700"))
        for i, s in enumerate(items):
            p.append(txt(x + 22, y + 52 + i * 18, s, size=11.8, fill=MUTED))

    return svg(w, h, "\n".join(p),
               "Capability map across solids, sketches, assemblies, sheet metal, library parts, "
               "aerospace mockups, simulation and documentation")


if __name__ == "__main__":
    for name, fn in (
        ("hero", hero),
        ("pipeline", pipeline),
        ("agents", agents),
        ("capabilities", capabilities),
    ):
        path = OUT / f"{name}.svg"
        path.write_text(fn(), encoding="utf-8")
        print(f"wrote {path.name}  {path.stat().st_size:,} bytes")
