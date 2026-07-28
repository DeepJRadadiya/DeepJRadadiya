# OBSIDIAN // AETHER — Minimalist Engineering Design System

This document establishes the architecture and visual rules for **Deep Radadiya's** GitHub Profile Repository. The system, titled **Obsidian // Aether**, is engineered to prioritize timeless minimalism, ultra-clean glassmorphism, and zero visual noise while offering **seamless multi-theme adaptability**.

---

## 1. Core Brand Philosophy

A modern software engineering profile should feel like a high-precision digital artifact. Every visual treatment, badge, and vector line is designed to communicate mastery, structured organization, and technical depth.

- **Zero-Noise Precision:** Remove superfluous decorative noise. Let content, whitespace, and sharp typography speak for themselves.
- **Luminescent Glassmorphism:** Rely on deep obsidian backgrounds with razor-thin translucent borders and localized glow physics.
- **Dynamic Adaptability:** Design every asset from day one to be color-theme modular, enabling effortless switching across visual aesthetics without breaking component hierarchy.

---

## 2. Multi-Theme Color Palettes

The architecture uses fixed dark structural tokens combined with **four swappable luminescent accent profiles**.

### Fixed Structural Tokens
| Token Name | Hex Value | Role & Usage |
| :--- | :--- | :--- |
| `obsidian-bg` | `#050505` | Primary repository canvas background |
| `obsidian-surface` | `#0D0E12` | Main card and panel background layer |
| `obsidian-raised` | `#14161C` | Interactive widgets, hover states, and headers |
| `obsidian-border` | `#222630` | Hairline structural dividers and glass edges |
| `text-primary` | `#F8FAFC` | High-contrast body text and headers |
| `text-muted` | `#8B94A0` | Supporting metadata, language tags, and sub-labels |

---

### Swappable Luminescent Accents (The 4 Themes)

You can transition your profile across these four distinct themes instantaneously using our built-in switching utility.

#### 1. 🔵 Quantum Teal (`teal`) *[Default]*
*A cyber-minimalist aesthetic evoking high-performance computing, real-time networking, and clean cloud systems.*
- **Primary Accent:** `#00F0FF` (Active badges, key text highlights, graph charts)
- **Secondary Accent:** `#00A3FF` (Subtle gradients, background grid glow)
- **Status Online:** `#00FFA3`
- **GitHub Stats Theme:** `tokyonight` (customized via parameters)

#### 2. 🟣 Electric Violet (`violet`)
*A sophisticated, deep engineering style celebrating architectural elegance, advanced algorithms, and creative engineering.*
- **Primary Accent:** `#A78BFA`
- **Secondary Accent:** `#8B5CF6`
- **Status Online:** `#34D399`
- **GitHub Stats Theme:** `radical` or `tokyonight` with purer purple shifts

#### 3. 🟢 Emerald Matrix (`emerald`)
*An homage to the core developer terminal, bash automation, and rigorous systems logic.*
- **Primary Accent:** `#10B981`
- **Secondary Accent:** `#34D399`
- **Status Online:** `#22C55E`
- **GitHub Stats Theme:** `merky` / emerald tailored

#### 4. 🟡 Minimal Gold (`gold`)
*A timeless monochrome & prestigious gold finish symbolizing executive craftsmanship, fintech security, and luxury minimalism.*
- **Primary Accent:** `#FACC15`
- **Secondary Accent:** `#EAB308`
- **Status Online:** `#38BDF8`
- **GitHub Stats Theme:** `vision-friendly-dark` / monochrome gold tailored

---

## 3. How to Switch Themes In Real-Time

To make theme switching effortless over time, a Python utility (`switch_theme.py`) is included directly inside the profile root directory. It executes regex-based token swapping across all vector assets (`assets/**/*.svg`) and markdown configuration widgets in `README.md`.

### Usage Command:
Open your terminal inside this repository folder and execute:
```bash
# To apply Quantum Teal:
python switch_theme.py teal

# To apply Electric Violet:
python switch_theme.py violet

# To apply Emerald Matrix:
python switch_theme.py emerald

# To apply Minimal Gold:
python switch_theme.py gold
```
After executing the script, simple commit and push your changes to GitHub to instantly transform your entire profile aesthetic!

---

## 4. Typography System

To ensure zero external font dependencies and ultra-crisp rendering on GitHub's SVG server, the design system utilizes high-performance modern font stacks:

- **Primary Display & Interface Font Stack:**
  ```css
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  ```
- **Code & Terminal Font Stack:**
  ```css
  font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', Consolas, ui-monospace, monospace;
  ```

### Scale & Hierarchy:
| Element | Size | Weight | Tracking (Letter Spacing) |
| :--- | :--- | :--- | :--- |
| **Hero Name Display** | `38–46px` | `800 (ExtraBold)` | `-1.2px` |
| **Hero Sub-Headline** | `15–18px` | `500 (Medium)` | `-0.2px` |
| **Section Card Title** | `18–20px` | `700 (Bold)` | `-0.4px` |
| **Project Name** | `16px` | `700 (Bold)` | `0px` |
| **Tech Tag Pill** | `11px` | `600 (SemiBold)` | `0.4px (Uppercase)` |
| **Body / Description**| `13px` | `400 (Regular)` | `0.2px` |

---

## 5. Component Geometry & Spacing

- **Base Unit:** `4px` grid scale (`4`, `8`, `12`, `16`, `24`, `32`, `48`).
- **Standard Corner Radius:**
  - Major Banners & Hero shells: `20px`
  - Modular Project Cards: `14px`
  - Tech Pills & Status Badges: `6px` or half-height (`999px` for capsules)
- **Stroke Widths:** Keep standard panel boundaries at exactly `1px`. Active accents and progress curves use `2px`. Never exceed `3px` stroke width to preserve zero-noise minimalism.
- **Glassmorphism Spec:** Use localized dark background rects with stroke borders and slight Gaussian blurs (`<feGaussianBlur stdDeviation="12" />`) beneath accent points to simulate deep space luminescence.

---

## 6. Directory Structure

```text
DeepRadadiya/
├── .github/
│   └── workflows/
│       └── snake.yml         # Automated half-daily contribution grid snake generator
├── assets/
│   ├── banners/
│   │   ├── hero.svg          # Minimalist hero greeting & availability indicator
│   │   └── footer.svg        # Clean session sign-off banner
│   ├── cards/
│   │   └── projects-showcase.svg # Interactive-style MERN/Django engineering grid
│   ├── components/
│   │   └── tech-dna.svg      # Visual architecture of languages, frameworks & tools
│   └── dividers/
│       └── minimal-line.svg  # Hairline glowing gradient divider
├── DESIGN.md                 # Design system guidelines and theme architecture (this file)
├── README.md                 # Primary profile presentation window
└── switch_theme.py           # Instant theme toggling command line tool
```

---

## 7. Accessibility & Mobile Optimization

- **ViewBox Rules:** Every custom SVG asset declares an exact proportional `viewBox` (e.g. `viewBox="0 0 900 280"` for banners) with `width="100%"` in README inclusions. This guarantees smooth responsive scaling across desktop displays and narrower mobile screens.
- **Color Contrast:** All reading text stays at high contrast (`#F8FAFC` against `#050505` background), meeting AAA accessibility guidelines.
- **Light/Dark Mode Handling:** Because GitHub profile backgrounds differ across users, all bespoke vector graphics encapsulate their own self-contained obsidian canvas (`<rect width="100%" height="100%" fill="#050505" rx="20"/>`), ensuring consistent presentation regardless of user theme settings.
