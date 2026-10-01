# Toolkit README banner convention

Use a **3:1 image canvas (2172 × 724 pixels)** for a toolkit README banner. Put it immediately
below the `# Toolkit Name` heading and render it at the available width:

```html
# Example Toolkit

<img src="docs/assets/banner.png" alt="Describe the scene" width="100%">
```

The common aspect ratio makes banners the same displayed height at the same README width:
displayed height is one third of the available width. The height remains responsive as the
reader's window changes. Do not add a fixed HTML `height` alongside `width="100%"`; that can
stretch artwork when the README width changes. GitHub README rendering removes inline CSS, so
a shared stylesheet is not a reliable way to control these images there.

Keep each banner asset in its own repository. Prepare a 3:1 canvas before adding it to the
README, framing the original artwork without stretching it. Use concise scene-specific alt text.
This is a presentation convention, not a scientific data-product contract.
