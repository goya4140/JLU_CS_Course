# Sayo UI Icons

Custom icon set for the Sayo UI framework. All icons use `stroke="currentColor"` — they inherit text colour via CSS.

## Design principles

- **Monoline** — 1.5px stroke, no fill (except deliberate accent fills)
- **Geometric** — circles, grids, and sharp angles. No organic curves.
- **currentColor** — every icon inherits `color` from its context. Set `color: var(--syo-accent)` on the parent.
- **20×20 viewBox** — consistent coordinate system, scale with `width`/`height` attributes.

## Usage

```html
<!-- Inline (recommended — inherits colour automatically) -->
<svg width="16" height="16" viewBox="0 0 20 20" fill="none">
  <path d="..." stroke="currentColor" stroke-width="1.5"/>
</svg>

<!-- External file -->
<img src="icons/toast-success.svg" width="20" height="20" alt="Success">
```

## Icon index

| File | Size | Category | Description |
|------|------|----------|-------------|
| `sayo-logo.svg` | 24×24 | Logo | Three concentric rings + centre dot. Concentric rings metaphor. Used as favicon. |
| `doc-document.svg` | 20×20 | Sidebar | Document with lines. Getting Started section. |
| `doc-tokens.svg` | 20×20 | Sidebar | Concentric circles + colour dot. Design Tokens section. |
| `doc-components.svg` | 20×20 | Sidebar | 2×2 grid of rounded squares. Components section. |
| `doc-theme.svg` | 20×20 | Sidebar | Circle half-filled. Theme section. |
| `doc-motion.svg` | 20×20 | Sidebar | Lightning bolt. Motion & JS section. |
| `toggle-sun.svg` | 20×20 | Toggle | Sun with rays. Day mode (colour: `#f57c00`). |
| `toggle-moon.svg` | 20×20 | Toggle | Crescent moon. Night mode (colour: `#5c6bc0`). |
| `toast-success.svg` | 20×20 | Toast | Checkmark in circle. `--syo-green`. |
| `toast-error.svg` | 20×20 | Toast | X mark in circle. `--syo-red`. |
| `toast-info.svg` | 20×20 | Toast | "i" in circle. `--syo-blue`. |
| `toast-warning.svg` | 20×20 | Toast | Triangle with "!". `--syo-yellow`. |
| `x-close.svg` | 20×20 | UI | X mark. Close buttons. |
| `hamburger.svg` | 20×20 | UI | Three horizontal lines. Mobile menu. |
| `chevron-right.svg` | 20×20 | UI | Right-pointing chevron. Next, expand. |
| `chevron-left.svg` | 20×20 | UI | Left-pointing chevron. Back, collapse. |
| `chevron-down.svg` | 20×20 | UI | Down-pointing chevron. Dropdown, show more. |
| `chevron-up.svg` | 20×20 | UI | Up-pointing chevron. Collapse, show less. |
| `search.svg` | 20×20 | UI | Magnifying glass. Search. |
| `home.svg` | 20×20 | UI | House. Home page. |
| `star.svg` | 20×20 | UI | Five-pointed star. Favourite, rate. |
| `heart.svg` | 20×20 | UI | Heart shape. Like, love. |
| `user.svg` | 20×20 | UI | Person silhouette. Profile, account. |
| `pencil.svg` | 20×20 | UI | Pencil. Edit, compose. |
| `check.svg` | 20×20 | UI | Simple checkmark. Confirm, done. |
| `plus.svg` | 20×20 | UI | Plus sign. Add, create, new.

## Preview

Open `icons/index.html` in a browser to see all icons at once with their recommended colours.
