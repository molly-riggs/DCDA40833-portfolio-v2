# Editing Your Portfolio: A Beginner's Guide

**For DCDA 40833 Students**

This guide focuses on the practical, day-to-day workflow of editing your Skills Portfolio template. It covers everything from opening your project to saving changes with GitHub Desktop.

---

## Table of Contents

1. [Opening Your Project](#opening-your-project)
2. [Understanding the Template Structure](#understanding-the-template-structure)
3. [The Editing Workflow](#the-editing-workflow)
4. [Finding Your TODO Markers](#finding-your-todo-markers)
5. [Editing HTML Content](#editing-html-content)
6. [Adding Your Images](#adding-your-images)
7. [Creating New Lab Pages](#creating-new-lab-pages)
8. [Previewing Your Changes](#previewing-your-changes)
9. [Saving with GitHub Desktop](#saving-with-github-desktop)
10. [Common Beginner Mistakes](#common-beginner-mistakes)
11. [Quick Troubleshooting](#quick-troubleshooting)

---

## Opening Your Project

### Step 1: Open in VS Code

1. **Launch VS Code**
2. **File → Open Folder** (NOT Open File!)
3. **Navigate to your portfolio folder** (wherever you cloned it)
4. **Click "Open"**

**You should see** a file tree on the left showing:
```
├── index.html
├── css/
│   └── styles.css
├── images/
├── README.md
└── other files...
```

**Pro Tip:** Always open the **folder**, not individual files. This gives you access to all project files at once.

---

## Understanding the Template Structure

### What Each File Does

| File | What It Is | Do You Need to Edit It? |
|------|-----------|------------------------|
| **index.html** | Your portfolio home page | ✅ **YES - Start here** |
| **ai-evaluation.html** | Lab 2 content | ✅ Create and edit for Lab 2 |
| **tufte-critique.html** | Lab 3 content | ✅ Create and edit for Lab 3 |
| **tableau-visualization.html** | Lab 4 content | ✅ Create and edit for Lab 4 |
| **lab5.html** | Lab 5 content | ✅ Create and edit for Lab 5 |
| **hometown-map.html** | Lab 6 content | ✅ Create and edit for Lab 6 |
| **css/styles.css** | Visual styling (colors, fonts, layout) | ❌ Only if changing colors |
| **images/** folder | Storage for your images and screenshots | ✅ Add your files here |
| **README.md** | Documentation | ❌ No |

**Your main tasks:** Edit `index.html` for the home page, then create separate HTML files for each lab assignment.

---

## The Editing Workflow

Here's the cycle you'll repeat over and over:

```
1. PULL → Get latest changes from GitHub
2. EDIT → Make changes in VS Code
3. SAVE → Save your file (Cmd+S or Ctrl+S)
4. PREVIEW → Check in browser
5. COMMIT → Save changes with GitHub Desktop
6. PUSH → Send changes to GitHub
```

Let's break down each step:

---

## Finding Your TODO Markers

The template has helpful `<!-- TODO: ... -->` comments showing exactly where to add content.

### How to Find TODOs in VS Code

**Method 1: Search for TODO**
1. Press **Cmd+F** (Mac) or **Ctrl+F** (Windows)
2. Type `TODO`
3. Press **Enter** to jump through each one

**Method 2: Use the TODO Tree Extension (Optional)**
1. Install "TODO Tree" extension in VS Code
2. TODOs appear in a special sidebar panel
3. Click to jump to each one

### What a TODO Looks Like

```html
<!-- TODO: Replace this placeholder content with information about yourself -->
<p><strong>Who I am:</strong> [Introduce yourself - your name, major, year, etc.]</p>
```

**Your job:** Replace the placeholder text with YOUR content, then delete the TODO comment.

**Before:**
```html
<!-- TODO: Replace this placeholder content with information about yourself -->
<p><strong>Who I am:</strong> [Introduce yourself - your name, major, year, etc.]</p>
```

**After:**
```html
<p><strong>Who I am:</strong> I'm a junior Strategic Communication major at TCU
   with a minor in Digital Culture and Data Analytics.</p>
```

---

## Editing HTML Content

### Basic HTML You Need to Know

Don't worry - you only need to understand a few patterns!

#### 1. Paragraphs

```html
<p>Your text goes here.</p>
```

**Pro Tip:** You can break long paragraphs across multiple lines in your code - HTML ignores line breaks inside tags.

```html
<p>This is a really long paragraph that I'm breaking
   across multiple lines in my code editor to make it
   easier to read while I'm editing.</p>
```

#### 2. Headings

```html
<h2>Main Section Title</h2>
<h3>Subsection Title</h3>
```

#### 3. Bold and Emphasis

```html
<p><strong>This text is bold</strong> and <em>this is italicized</em>.</p>
```

#### 4. Lists

**Bulleted lists:**
```html
<ul>
    <li>First point</li>
    <li>Second point</li>
    <li>Third point</li>
</ul>
```

**Numbered lists:**
```html
<ol>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>
```

#### 5. Links

```html
<a href="https://github.com/yourusername/your-repo">Link text here</a>
```

**Don't forget to update the footer link to YOUR GitHub repository!**

### Editing Strategy: Copy and Modify

**Don't delete the template structure** - just modify the text inside the tags.

**Keep this:**
```html
<section id="about">
    <h2>About Me</h2>
```

**Change this:**
```html
    <p><strong>Who I am:</strong> [Introduce yourself]</p>
```

**To this:**
```html
    <p><strong>Who I am:</strong> I'm a senior Finance major exploring
       how data analytics can transform business decision-making.</p>
```

---

## Adding Your Images

### Step 1: Prepare Your Images

Save screenshots, charts, or other images as PNG or JPG files.

**For Tableau visualizations:**
1. Export as image from Tableau Public, OR
2. Take a screenshot and crop it

**For Colab notebooks (Lab 6 map):**
1. Save your Folium map as an HTML file
2. Place the HTML file in your repository

### Step 2: Add to Your Project

**Option A: Drag and Drop (Easiest)**
1. Open the `images/` folder on your computer
2. Drag your image files into that folder

**Option B: Using VS Code**
1. In VS Code, **right-click** the `images/` folder (left sidebar)
2. **Reveal in Finder** (Mac) or **Reveal in File Explorer** (Windows)
3. Copy your files into this folder

### Step 3: Reference in HTML

**Add an image to your page:**

```html
<figure class="viz-container">
    <img src="images/your-image.png"
         alt="Description of what the image shows">
    <figcaption>Figure 1: Caption describing the image</figcaption>
</figure>
```

**Update with YOUR filename:**
- Change `your-image.png` to match your actual filename
- Update the `alt` text to describe what the image shows

**Common Mistakes:**
- ❌ `src="my-chart.PNG"` (wrong case)
- ❌ `src="images\my-chart.png"` (wrong slash direction)
- ❌ `src="Downloads/my-chart.png"` (wrong folder)
- ✅ `src="images/my-chart.png"` (CORRECT!)

---

## Creating New Lab Pages

For each lab assignment, you'll create a new HTML file. Here's how:

### Step 1: Create the File

1. In VS Code, **right-click** in the file explorer (left panel)
2. Select **"New File"**
3. Name it according to the lab (e.g., `ai-evaluation.html`)

### Step 2: Use This Template

Copy this starter template into your new file:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab Title - Your Name | DCDA 40833</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <!-- Navigation: Same on every page -->
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="ai-evaluation.html">AI Evaluation</a></li>
            <li><a href="tufte-critique.html">Tufte Critique</a></li>
            <li><a href="tableau-visualization.html">Tableau Viz</a></li>
            <li><a href="lab5.html">Lab 5</a></li>
            <li><a href="hometown-map.html">Hometown Map</a></li>
        </ul>
    </nav>

    <!-- Header -->
    <header>
        <h1>Lab Title</h1>
        <p>Your Name | DCDA 40833</p>
    </header>

    <main>
        <section>
            <h2>Assignment Overview</h2>
            <!-- Brief intro explaining the assignment's purpose -->
            <p>In this lab, I explored...</p>
        </section>

        <section>
            <h2>My Work</h2>
            <!-- Your lab content goes here -->
        </section>

        <section>
            <h2>Reflection</h2>
            <!-- What you learned, what was challenging -->
            <p><strong>What I learned:</strong> ...</p>
            <p><strong>Challenges:</strong> ...</p>
            <p><strong>Connection to DCDA:</strong> ...</p>
        </section>
    </main>

    <!-- Footer: Same on every page -->
    <footer>
        <p><a href="https://github.com/yourusername/your-repo-name">View Repository on GitHub</a></p>
        <p>&copy; 2026 Your Name | DCDA 40833 | TCU</p>
    </footer>
</body>
</html>
```

### Step 3: Customize for Each Lab

**Lab 2 - AI Evaluation:**
- Add your 500-750 word analysis
- Include screenshots of AI tools you tested
- Embed evidence of your exploration

**Lab 3 - Tufte Critique:**
- Embed your chosen infographic (image)
- Include link to original source
- Write your 500+ word critique

**Lab 4 - Tableau Visualization:**
- Embed your Tableau Public visualization (use iframe)
- Write your 500+ word reflection

**Lab 6 - Hometown Map:**
- Embed your Folium map (iframe to HTML file)
- Write your 300+ word reflection
- Link to your Google Colab notebook

### Embedding a Tableau Visualization

```html
<div class="viz-container">
    <iframe src="https://public.tableau.com/views/YOUR-VIZ-URL"
            width="100%"
            height="600"
            style="border:none;">
    </iframe>
</div>
```

### Embedding a Folium Map

First, save your map HTML file to your repository, then:

```html
<div class="viz-container">
    <iframe src="hometown-map-folium.html"
            width="100%"
            height="500"
            style="border:none;">
    </iframe>
</div>
```

---

## Previewing Your Changes

### Method 1: Open in Browser (Simplest)

1. **Save your file** in VS Code (Cmd+S or Ctrl+S)
2. In VS Code's file explorer, **right-click `index.html`**
3. **Reveal in Finder/Explorer**
4. **Double-click `index.html`** → Opens in your default browser
5. **Refresh** the browser after making more changes

### Method 2: Live Server Extension (Recommended)

**One-time setup:**
1. In VS Code, go to **Extensions** (left sidebar, looks like blocks)
2. Search for **"Live Server"**
3. Install it

**Using Live Server:**
1. Right-click **anywhere in `index.html`**
2. Select **"Open with Live Server"**
3. Browser opens automatically
4. **Auto-refreshes when you save** - super convenient!

---

## Saving with GitHub Desktop

This is how you save your progress to GitHub (and share with your team if working in a group).

### The Golden Rule

**ALWAYS do this in order:**

1. **PULL** - Get latest changes from GitHub
2. **EDIT** - Make your changes
3. **COMMIT** - Save with a message
4. **PUSH** - Send to GitHub

### Step-by-Step

#### 1. PULL First (Critical!)

1. Open **GitHub Desktop**
2. Click **"Fetch origin"** (top right)
3. If it says **"Pull origin"**, click that too

**Why?** This gets any changes your teammates made. Always pull BEFORE editing to avoid conflicts.

#### 2. Make Your Edits in VS Code

Edit `index.html`, create lab pages, add images, etc.

#### 3. Check What Changed

Go back to **GitHub Desktop**. You'll see:
- **Left panel:** Files you changed
- **Right panel:** Exactly what changed (red = deleted, green = added)

**Review your changes** to make sure you didn't accidentally delete something important.

#### 4. Commit Your Changes

At the bottom left of GitHub Desktop:

**Summary (required):**
```
Added AI Evaluation page for Lab 2
```

**Description (optional):**
```
- Created ai-evaluation.html
- Added analysis of ChatGPT and Claude
- Included screenshots of testing
```

**Click "Commit to main"**

#### 5. PUSH to GitHub

**Click "Push origin"** (top right button)

**Done!** Your changes are now on GitHub.

### Good Commit Messages

**Good:**
- `Added Tufte critique with embedded infographic`
- `Fixed navigation links on all pages`
- `Updated About Me section with bio`

**Not helpful:**
- `updated stuff`
- `changes`
- `asdfjkl`

**Why it matters:** If you need to undo something later, good messages help you find the right version.

---

## Common Beginner Mistakes

### 1. Forgetting to Save

**Problem:** Made changes, refreshed browser, nothing happened.

**Solution:** Press **Cmd+S** (Mac) or **Ctrl+S** (Windows) to save in VS Code. Look for the **white dot** next to the filename - if you see it, the file isn't saved yet.

### 2. Opening Individual Files Instead of Folder

**Problem:** Can't see other project files in VS Code.

**Solution:** **File → Open Folder**, then select your portfolio folder. NOT "Open File"!

### 3. Wrong Image Paths

**Problem:** Images show as broken icons.

**Solution:**
- ✅ Use `images/filename.png` (lowercase, forward slash)
- ❌ NOT `Images/` or `img/` or `pictures/`
- ✅ Filename must match EXACTLY (case-sensitive!)

### 4. Forgetting to Pull Before Editing (Groups)

**Problem:** "Merge conflict" error when trying to push.

**Solution:**
1. **ALWAYS click "Fetch origin" → "Pull"** in GitHub Desktop BEFORE editing
2. **Communicate with your team:** "I'm editing the Tableau page now"
3. **Wait for teammates to push** before you start editing

### 5. Deleting HTML Tags Accidentally

**Problem:** Page looks broken, styling disappeared.

**Solution:**
- Only edit **text inside** tags, not the tags themselves
- If you deleted `</section>` or `</div>` by accident, undo (Cmd+Z)
- Use VS Code's **auto-indent** feature: Select all (Cmd+A), then Format Document

### 6. Not Testing Before Committing

**Problem:** Pushed broken code to GitHub, entire team affected.

**Solution:**
1. **Always preview in browser** before committing
2. Check that images load
3. Check that navigation links work
4. **THEN** commit and push

### 7. Forgetting Navigation on New Pages

**Problem:** Created a lab page but can't navigate back to home.

**Solution:** Copy the `<nav>` section from `index.html` to every new page you create. Navigation should be identical on all pages.

---

## Quick Troubleshooting

### Images Not Showing

**Checklist:**
- [ ] File is in the `images/` folder (not `Images/`, not root folder)
- [ ] Filename in HTML matches exactly (case-sensitive)
- [ ] Path uses forward slash: `images/chart.png`
- [ ] File is actually a PNG or JPG (not `.pdf`, `.ai`, or other format)
- [ ] You saved the HTML file
- [ ] You refreshed the browser (hard refresh: Cmd+Shift+R or Ctrl+Shift+R)

### CSS Not Loading (Page Looks Plain)

**Checklist:**
- [ ] `styles.css` is in the `css/` folder
- [ ] First line of your HTML has `<link rel="stylesheet" href="css/styles.css">`
- [ ] Hard refresh browser (Cmd+Shift+R or Ctrl+Shift+R)

### Embedded Content Not Displaying

**Checklist:**
- [ ] Tableau visualization is published to Tableau Public (not just saved)
- [ ] Folium map HTML file is in your repository
- [ ] iframe `src` path is correct
- [ ] Check browser console (F12) for security errors

### Can't Push to GitHub

**Error:** "You don't have permission"

**Solution:**
- If working in a group: Make sure repository owner added you as collaborator
- Check that you're logged into GitHub Desktop with the correct account

**Error:** "Need to pull first"

**Solution:**
1. Click **"Fetch origin"**
2. Click **"Pull origin"**
3. If there are conflicts, see next section

### Merge Conflicts (Group Work)

**What it means:** You and a teammate edited the same lines.

**How to fix:**
1. GitHub Desktop will show which file has conflicts
2. **Open that file in VS Code**
3. Look for these markers:
   ```html
   <<<<<<< HEAD
   Your version here
   =======
   Your teammate's version here
   >>>>>>> main
   ```
4. **Delete the markers** and keep the version you want (or combine both)
5. **Save the file**
6. Go back to GitHub Desktop → **Commit** → **Push**

**Prevention:** Coordinate with your team - work on different pages at different times!

---

## Working as a Team: Best Practices

### Communication is Everything

**Before editing:**
> "Hey team, I'm going to work on the Tufte Critique page for the next hour. Don't edit that file!"

**After editing:**
> "Tufte page is done and pushed. Safe to pull now!"

### Divide Pages Clearly

**Example for a 3-person team:**
- **Person A:** index.html (Home) + AI Evaluation
- **Person B:** Tufte Critique + Tableau Visualization
- **Person C:** Lab 5 + Hometown Map

**Everyone:** Pull before editing, push when done, communicate constantly!

### Use Descriptive Commit Messages

Help your team understand what you did:
- `Completed AI Evaluation page - Person A`
- `Fixed typos on Tufte Critique - Person B`
- `Added Folium map to Hometown page - Person C`

---

## Quick Reference: Essential Shortcuts

### VS Code

| Action | Mac | Windows |
|--------|-----|---------|
| Save file | Cmd+S | Ctrl+S |
| Find | Cmd+F | Ctrl+F |
| Find and Replace | Cmd+H | Ctrl+H |
| Undo | Cmd+Z | Ctrl+Z |
| Select All | Cmd+A | Ctrl+A |

### Browser

| Action | Mac | Windows |
|--------|-----|---------|
| Hard Refresh | Cmd+Shift+R | Ctrl+Shift+R |
| Open Developer Tools | Cmd+Option+I | F12 |

---

## Final Checklist Before Submission

### For Each Lab Page

- [ ] Page exists and loads correctly
- [ ] Navigation works (can get to all other pages)
- [ ] Content meets word count requirements
- [ ] Images/embeds display correctly
- [ ] Reflection section is complete
- [ ] No TODO comments remaining

### For the Whole Portfolio

- [ ] All six pages completed (Home + 5 labs)
- [ ] Consistent navigation on every page
- [ ] Footer links to your GitHub repository
- [ ] CSS loads on all pages (styling looks correct)
- [ ] Tested on mobile (resize browser window)
- [ ] Code has comments explaining your work
- [ ] GitHub Pages is enabled and site is live

---

## Remember

- **Save often** (Cmd+S becomes muscle memory)
- **Preview frequently** (catch mistakes early)
- **Pull before editing** (especially in groups)
- **Commit with good messages** (your future self will thank you)
- **Ask for help** when stuck (office hours, classmates, D2L discussion)

**You've got this!** The template does most of the hard work - you just need to add your content for each lab. Focus on demonstrating what you learned, and the technical stuff will fall into place.

---

## Need More Help?

- **Full documentation:** See [README.md](README.md)
- **Stuck?** Come to office hours or post on D2L discussion board!

---

**Good luck with your portfolio!** Remember: every expert was once a beginner. You're learning valuable skills that will serve you beyond this class.
