# Ink & Insight — GitHub Pages article website

A fully editable, mobile-friendly article publication built with **Jekyll (GitHub Pages)**. Includes working article search, six original example articles, and **8 clearly labeled advertising spaces on the homepage**. No database, server, or paid hosting required.

## 1 — Publish on GitHub

1. Sign into [GitHub](https://github.com), select **New repository**.
2. Repository name: `article-reader`. Choose **Public** and **do not add another README**.
3. Extract this ZIP on your computer, then open **Git Bash** inside the `article-reader-starter` folder.
4. Run these commands, replacing `YOUR-GITHUB-USERNAME` with your GitHub username:

```bash
git init
git branch -M main
git add .
git commit -m "Launch article reading website"
git remote add origin https://github.com/YOUR-GITHUB-USERNAME/article-reader.git
git push -u origin main
```

5. In your GitHub repository, open **Settings → Pages → Build and deployment**.
6. Choose **Deploy from a branch**, then **main** and **/(root)**, and **Save**.
7. Your website address will be `https://YOUR-GITHUB-USERNAME.github.io/article-reader/`.

> Important: In `_config.yml`, replace the value of `url` with your actual `https://YOUR-GITHUB-USERNAME.github.io`. The `baseurl` is set for the repository name `article-reader`. If your repository is named differently, update `baseurl` to `/<repo-name>`. If using a root repository `YOUR-GITHUB-USERNAME.github.io`, set `baseurl: ""`.

## 2 — Add a new article

1. In `_posts`, create a Markdown file like `2026-11-17-my-first-article.md`.
2. Paste this example (replace the title, description, category, and content):

```markdown
---
layout: post
title: "My First Article"
description: "A short description for the homepage and search engines."
category: Ideas
author: Your Publication
reading_time: "3 min read"
---

Write an introduction here.

## First heading

Write a few paragraphs of your original article here.

## Second heading

Continue writing your article.
```

3. Save and push:

```bash
git add .
git commit -m "Publish new article"
git push
```

You can also create and edit posts directly in GitHub's website: **Add file → Create new file → `_posts/YYYY-MM-DD-your-title.md`** and commit.

## 3 — Eight homepage advertising placements

The homepage includes exactly **8 reserved positions**:

| ID | Location |
| --- | --- |
| 01 | Below the top hero banner |
| 02 | After the featured article |
| 03 | Between article cards, after #2 |
| 04 | Between article cards, after #4 |
| 05 | After the article list |
| 06 | Upper sidebar |
| 07 | Lower sidebar |
| 08 | Above the footer |

The article-reading layout reuses #06 (sidebar) and #08 (bottom) to keep articles less cluttered. On mobile, sidebar placements move below the article feed. Placeholder labels are shown until ads are enabled.

## 4 — Set up Google AdSense (AFTER you have real content and approval)

1. Add your real site/domain in [Google AdSense](https://adsense.google.com/start/).
2. Enter your `ca-pub-...` value in `_config.yml` under `adsense_client` (keep `ads_enabled: false` during ownership verification/site review).
3. Once your site is **Ready** and approved to show ads, create the ad units in AdSense.
4. Put their **numeric** ad slot IDs into the `ad_units` values for placement IDs 01–08. The label `01` is just the website position; it is NOT the AdSense slot ID.
5. Set `ads_enabled: true` and `show_ad_placeholders: false`, then push the changes.

**For the site review:** set `show_ad_placeholders: false` so empty demo boxes are hidden; this does not affect the reserved positions in your template. For Google AdSense, plan to use a **custom domain**. AdSense does not accept a full GitHub project URL with a path as a site entry, and it restricts subdomain submissions outside host-partner sites.

**Important:** Eight reserved placements do not imply that eight live ads on every page comply with AdSense policies. Avoid showing more advertising than content; only activate as many placements as are appropriate for the content on that page. You can leave some `ad_units` empty, which keeps those spaces as placeholders, or remove unused `{% include ad-slot.html ... %}` calls. Ads must be distinct from navigation and editorial content.

This starter is **not** already monetized and does not promise AdSense approval.

## 5 — Customize the website

- Site name and description: `_config.yml`.
- Colors, typography, and layout: `assets/css/style.css`.
- Homepage content/layout: `index.html`.
- Header, footer, and AdSense ownership script: `_layouts/default.html`.
- Individual article layout: `_layouts/post.html`.
- Ad placement logic: `_includes/ad-slot.html`.
- About, Privacy, Contact: `about.md`, `privacy.md`, `contact.md`.

**Before launching:** replace the demo articles with your original published content; update the contact details, privacy notice, and relevant cookie consent practices. If you use an advertising network, review its policies for your visitor locations.

## 6 — Useful notes

- GitHub Pages hosts public static files and Jekyll articles; it does not provide server-side login, a CMS dashboard, or a database.
- You can use GitHub's browser editor to add new posts without installing Ruby/Jekyll locally.
- If you want a custom domain, configure it in **Settings → Pages**. Follow GitHub's DNS instructions, and set the appropriate `url` / `baseurl` in `_config.yml`.
- GitHub Pages is fine for an article-based hobby/personal publication, but GitHub says it is not for operating a primarily commercial online business. For a commercial publishing business, assess a dedicated web host.
- The page uses Google Fonts. To remove that external request, delete the `@import` at the top of `assets/css/style.css` and use system fonts instead.

## References

- [GitHub Pages: publishing from a branch](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub Pages: posts and Markdown content](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll)
- [Google AdSense: placement guidance](https://support.google.com/adsense/answer/1282097)
