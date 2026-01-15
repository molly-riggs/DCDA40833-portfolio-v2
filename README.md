# DCDA 40833 Skills Portfolio Template

## About This Template

This template is designed specifically for DCDA 40833 students completing their **Skills Portfolio**. Unlike a traditional assignment submitted once at the end of the course, this portfolio is **built iteratively** — you started the foundation in Lab 1 and added new pages with each subsequent lab.

This final submission asks you to **refine, polish, and unify** your portfolio into a cohesive demonstration of your skills and learning.

---

## Getting Started

**New to this template?** See [EDITING_GUIDE.md](EDITING_GUIDE.md) for a complete walkthrough of the editing workflow.

### Template Workflow

1. Click **"Use this template"** button (green button at top of repository)
2. Name your repository (e.g., `dcda-skills-portfolio`)
3. Make it **Public** (required for GitHub Pages)
4. Clone with GitHub Desktop and open in VS Code
5. Edit `index.html` following the TODO markers
6. Add new pages for each lab assignment

---

## What Your Portfolio Should Include

By this point in the semester, your portfolio should contain:

### Required Pages (from Labs 1-6)

| Page | File | Lab | Description |
|------|------|-----|-------------|
| **Home/Landing** | `index.html` | Lab 1 | Introduction and navigation to all other pages |
| **AI Tool Evaluation** | `ai-evaluation.html` | Lab 2 | Analysis of AI tools (500-750 words) with evidence |
| **Tufte Critique** | `tufte-critique.html` | Lab 3 | Visualization critique (500+ words) with embedded infographic |
| **Tableau Visualization** | `tableau-visualization.html` | Lab 4 | Embedded Tableau Public viz with reflection (500+ words) |
| **[Lab 5 Content]** | TBD | Lab 5 | *Content based on Lab 5 assignment* |
| **Hometown Map** | `hometown-map.html` | Lab 6 | Interactive Folium map with reflection (300+ words) |

---

## What's Included

```
portfolio-template/
├── index.html              ← Home page template with TODO markers
├── css/
│   └── styles.css          ← Professional CSS (TCU colors, responsive)
├── images/                 ← Place your images here
│   └── .gitkeep           ← Placeholder file
├── README.md               ← This file (overview & requirements)
├── EDITING_GUIDE.md        ← Step-by-step editing workflow
└── .gitignore              ← Ignore temporary files
```

---

## Final Polish Requirements

For this final submission, go beyond what you submitted for individual labs:

### 1. Visual Refinement & Consistency

- **Unified design:** Ensure all pages share consistent styling (colors, fonts, layout)
- **Enhanced CSS:** Add polish beyond basic requirements (spacing, hover effects, responsive design)
- **Navigation:** Clear, working navigation on every page
- **Professional appearance:** Clean, readable, well-organized

### 2. Enhanced Content & Context

For each lab page, add:

- **Brief introduction** explaining the assignment's purpose
- **Reflection on learning** — What did you learn? What was challenging?
- **Connection to your skills** — How does this demonstrate your DCDA abilities?

Consider adding:
- An "About" page introducing yourself and your interests
- A reflection on your growth across the semester

### 3. Code Quality & Documentation

**IMPORTANT:** Comment your code thoroughly.

- **HTML comments** (`<!-- comment -->`) explaining structure and purpose of sections
- **CSS comments** (`/* comment */`) explaining styling choices and what each block does
- **Over-comment** at this stage — we want to see your understanding, not just working code

Comments should explain:
- Why you made certain design choices
- What each section of code accomplishes
- How different elements work together

> **Tip:** Comments are visible in VS Code and when viewing page source (right-click → View Page Source), but not to regular site visitors.

### 4. Technical Requirements

- All files organized in your repository (HTML, CSS, images, etc.)
- All links working (internal navigation, external resources)
- All embedded content displaying correctly (Tableau viz, Folium map, images)
- Site deployed and functional on GitHub Pages

---

## Step-by-Step Customization

### Step 1: Edit HTML Content

Open `index.html` in your text editor (VS Code recommended) and look for `<!-- TODO: ... -->` comments. These mark exactly where to add your content.

**Quick Find & Replace:**
- `Your Name` → Your actual name
- `yourusername` → Your GitHub username (in footer)
- `project-name` → Your repository name (in footer)

### Step 2: Create Lab Pages

For each lab assignment, create a new HTML page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab Title - Your Name</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav>
        <!-- Copy navigation from index.html -->
    </nav>

    <main>
        <section>
            <h1>Lab Title</h1>
            <!-- Your lab content here -->
        </section>
    </main>

    <footer>
        <!-- Copy footer from index.html -->
    </footer>
</body>
</html>
```

### Step 3: Add Navigation Links

Update the navigation on **every page** to include links to all your lab pages:

```html
<nav>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="ai-evaluation.html">AI Evaluation</a></li>
        <li><a href="tufte-critique.html">Tufte Critique</a></li>
        <li><a href="tableau-visualization.html">Tableau Viz</a></li>
        <li><a href="hometown-map.html">Hometown Map</a></li>
    </ul>
</nav>
```

### Step 4: Embed External Content

**Embedding a Tableau Visualization:**
```html
<div class='tableauPlaceholder'>
    <iframe src="YOUR-TABLEAU-EMBED-URL"
            width="100%"
            height="600">
    </iframe>
</div>
```

**Embedding a Folium Map:**
```html
<iframe src="map.html"
        width="100%"
        height="500"
        style="border:none;">
</iframe>
```

---

## Deploy to GitHub Pages

Make your portfolio publicly accessible:

1. **Go to repository Settings → Pages** (left sidebar)
2. **Source:** Select "Deploy from a branch"
3. **Branch:** Select `main` (or `master`), folder: `/ (root)`
4. **Click Save**
5. **Wait 1-2 minutes**, then visit: `https://YOUR-USERNAME.github.io/your-repo-name`

**Troubleshooting:**
- Make sure repository is **Public** (Settings → General)
- Check that `index.html` is in the root directory (not in a subfolder)
- Allow 1-2 minutes for first deployment
- Refresh browser cache (Ctrl+Shift+R or Cmd+Shift+R)

---

## Template Features (Already Built In)

### Visual Design
- **TCU Purple color scheme** (customizable in CSS)
- **Responsive design** - Works on desktop, tablet, mobile
- **Sticky navigation** - Menu stays visible while scrolling
- **Smooth scrolling** - Anchor links animate smoothly
- **Professional typography** - System fonts for fast loading

### Technical Features
- **Semantic HTML5** - Proper structure for accessibility
- **Code syntax highlighting** - Dark theme for code blocks
- **Image optimization** - Responsive images with captions
- **Print-friendly** - Portfolio prints nicely for PDF export

### No Configuration Needed
- **CSS is complete** - No styling knowledge required
- **HTML structure is done** - Just fill in content
- **Mobile responsive** - Automatically adapts to screen size
- **Browser compatible** - Works in all modern browsers

---

## Customization (Optional)

### Change Color Scheme

Edit `css/styles.css` at the top:

```css
:root {
    --primary-color: #4d1979;      /* Main color (currently TCU Purple) */
    --secondary-color: #7c3aed;    /* Accent color */
    --accent-color: #ffd700;       /* Highlight color (currently gold) */
}
```

Try these color schemes:
- **Blue Academia:** `#1e3a8a`, `#3b82f6`, `#fbbf24`
- **Green Digital:** `#065f46`, `#10b981`, `#f59e0b`
- **Red Critical:** `#7f1d1d`, `#ef4444`, `#fcd34d`

---

## Connection to Self-Reflection

Your Skills Portfolio will be a key piece of evidence in your **Final Self-Reflection** (submitted separately). Use your portfolio to demonstrate:

- **Digital Culture proficiency** — Web development, design, digital communication
- **Data Analytics proficiency** — Visualization, critique, mapping, data storytelling
- **Project Design and Planning** — Building something iteratively over the semester
- **Self-direction and growth** — How you refined your work beyond minimum requirements

See the `/self-reflections/` folder for the self-reflection template and guidelines.

---

## Grading Considerations

In the spirit of this course's **ungrading approach**, this assignment doesn't receive a numerical score. However, in your self-reflection and grade argument, you should address:

- **Completeness:** Are all required pages present and functional?
- **Polish:** Did you go beyond minimum requirements to create something professional?
- **Understanding:** Do your comments demonstrate understanding of what you built?
- **Growth:** How did your skills develop from Lab 1 to Lab 6?
- **Timeliness:** Did you submit complete work on time throughout the semester?

Your portfolio is evidence of your learning — make it something you're proud to share.

---

## Final Submission Checklist

### Content Completeness
- [ ] Home/Landing page with navigation to all lab pages
- [ ] AI Tool Evaluation page (500-750 words)
- [ ] Tufte Critique page (500+ words) with embedded infographic
- [ ] Tableau Visualization page with embedded viz (500+ words)
- [ ] Lab 5 content page
- [ ] Hometown Map page with embedded Folium map (300+ words)
- [ ] All pages have reflections on learning

### Technical Requirements
- [ ] All pages use consistent styling
- [ ] Navigation works on every page
- [ ] All embedded content displays correctly (Tableau, Folium, images)
- [ ] All external links open correctly
- [ ] Site deployed and functional on GitHub Pages
- [ ] Repository is organized (HTML, CSS, images in proper folders)

### Code Quality
- [ ] HTML comments explain structure and purpose of sections
- [ ] CSS comments explain styling choices
- [ ] Comments demonstrate understanding of code
- [ ] Code is properly indented and readable

### Polish & Professionalism
- [ ] Unified visual design across all pages
- [ ] Clean, readable layout
- [ ] Proofread all text (spelling, grammar)
- [ ] Professional appearance suitable for portfolio

---

## Troubleshooting

### Images Not Showing

**Solutions:**
- Verify image files are in `images/` folder
- Check exact filename match (case-sensitive)
- Use relative paths: `images/chart.png`
- Refresh browser cache: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)

### CSS Not Loading

**Solutions:**
- Verify `styles.css` is in `css/` folder
- Check `<link>` tag in HTML points to `css/styles.css`
- Clear browser cache and hard refresh
- Open browser developer tools (F12) and check Console for errors

### Embedded Content Not Displaying

**Solutions:**
- Verify embed URLs are correct and public
- For Tableau: Ensure visualization is published to Tableau Public
- For Folium: Ensure HTML file is in your repository
- Check for browser security blocking embedded content

### GitHub Pages Not Working

**Solutions:**
- Confirm repository is **Public**
- Verify `index.html` is in root directory
- Wait 1-2 minutes after enabling Pages
- Check Pages settings: Settings → Pages → Source should be "main branch"

---

## Submission

**Due:** See course schedule

Submit to D2L dropbox:
1. Link to your **GitHub repository**
2. Link to your **live GitHub Pages site**

Your instructors will review both your live site and your repository code (including comments).

---

## Resources

### Technical References
- **HTML Reference:** [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)
- **CSS Reference:** [MDN CSS Docs](https://developer.mozilla.org/en-US/docs/Web/CSS)
- **Git Basics:** [GitHub's Git Handbook](https://guides.github.com/introduction/git-handbook/)
- **GitHub Pages:** [Official Pages Documentation](https://docs.github.com/en/pages)

### Tools
- **VS Code** (Recommended editor): [code.visualstudio.com](https://code.visualstudio.com/)
- **GitHub Desktop** (Git GUI): [desktop.github.com](https://desktop.github.com/)
- **Tableau Public:** [public.tableau.com](https://public.tableau.com/)

---

## Support

### Getting Help

1. **Check [EDITING_GUIDE.md](EDITING_GUIDE.md)** - Workflow guide with troubleshooting
2. **Review lab materials** - Revisit instructions from Labs 1-6
3. **Test in browser** - Open Developer Tools (F12) to see errors
4. **Office hours** - Bring specific questions or errors
5. **D2L discussion** - Post screenshots of issues

### Common Questions

**Q: Do I need to know CSS to use this template?**
A: No! The CSS is complete. You only need to edit HTML content.

**Q: What if I want a different color scheme?**
A: Edit the `:root` section in `css/styles.css` (see Customization section above).

**Q: How do I make my repository private after the class?**
A: Settings → General → Change repository visibility → Make private (after grading is complete).

**Q: Can I use this in my professional portfolio?**
A: Absolutely! That's the point. It's yours to keep and showcase.

---

## Credits

**Template created for:**
DCDA 40833 | TCU
Spring 2026

**License:** MIT (you may use, modify, and share freely)

---

**Good luck with your portfolio!**

Your Skills Portfolio represents your growth across the semester — from your first HTML page in Lab 1 to a polished, professional web presence. Make it something you're proud to share.
