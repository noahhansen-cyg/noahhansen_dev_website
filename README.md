# noahhansen.dev

Personal portfolio website for Noah Hansen — software engineer, drummer, and outdoor enthusiast.

Built with Python and Flask. Content is driven by YAML files so updates never require touching HTML or Python. Tested with pytest, linted with flake8, and auto-deployed to Render from the `main` branch.

## Stack

- **Backend:** Flask 3.x + Jinja2 templates
- **Content:** YAML files loaded at startup (`app/data/`)
- **Testing:** pytest + pytest-cov
- **CI:** GitHub Actions (runs on pull requests to `main` and `dev`)
- **Deployment:** Render (auto-deploy from `main`)

## Project Structure

```
app/
├── __init__.py          # Flask app factory
├── routes.py            # GET /, /resume, /health
├── data/
│   ├── loader.py        # YAML loading utilities
│   ├── work.yaml        # Title, skills, experience
│   ├── projects.yaml    # Personal projects
│   ├── life.yaml        # Hobbies and outside-work content
│   └── links.yaml       # Name, GitHub, LinkedIn, email, resume
├── templates/
│   ├── base.html        # Layout shell (nav, footer)
│   ├── index.html       # Single-page home
│   └── partials/        # hero, work, projects, life, links
└── static/
    ├── css/main.css
    ├── js/main.js
    └── assets/          # resume.pdf goes here
tests/
├── conftest.py          # pytest fixtures
├── test_routes.py       # HTTP status code tests
├── test_data.py         # YAML schema and content tests
└── test_templates.py    # Rendered HTML content tests
```

## Local Development

**First-time setup:**
```bash
make install
```

**Start the dev server:**
```bash
make run
```

Then open `http://127.0.0.1:5000`.

## Testing

```bash
make test   # pytest with coverage (85% minimum enforced)
make lint   # flake8
```

## Updating Content

All site content lives in `app/data/`. Edit the YAML files directly — no Python or HTML changes needed.

| File | Controls |
|---|---|
| `work.yaml` | Job title, skills by category, work experience |
| `projects.yaml` | Personal projects (name, description, tech, URL, status) |
| `life.yaml` | Hobbies and outside-work content |
| `links.yaml` | Name, GitHub, LinkedIn, email, resume filename |

## Branching

- `main` — production. Auto-deploys to Render on push. Never commit directly.
- `dev` — integration branch. All work lands here first.
- Feature branches off `dev` → PR into `dev` → promote `dev → main` to ship.

## Deployment

The site deploys automatically to Render when `main` is updated. To promote `dev` to production:

```bash
git checkout main
git merge dev --no-ff
git push origin main
```
