# django-scaffoldx-cli
# 🛠️ Django ScaffoldX CLI

A power tool for Django developers to **bootstrap apps**, **autogenerate boilerplate**, and **wire up project URLs** — all from a single management command.

> ⚙️ `python manage.py scaffold [flags]`

## 🚀 Features

- 🔧 Auto-create Django apps if missing
- 🏗️ Scaffold files like `urls.py`, `views.py`, `serializers.py`, `signals.py`, etc.
- 🧱 Auto-create `templates/<app>/` and `static/<app>/` folders
- 🔗 Update `config/urls.py` to include app URLs
- 💡 Optional dry-run, config overrides, and verbose timing

---

## 📦 Installation

> Requires Django and Python 3.7+  
> Copy or clone this into your Django project as an app named `scaffoldx`, then add it to `INSTALLED_APPS`.

```bash
pip install colorama
⚙️ Usage Examples
# Scaffold all apps listed in settings.py (skipping built-ins)
python manage.py scaffold


# Preview changes only (no writes)
python manage.py scaffold --dry-run


# Only create apps (no files)
python manage.py scaffold --apps-only


# Only scaffold boilerplate (no app creation)
python manage.py scaffold --scaffold-only


# Refresh config/urls.py without modifying anything else
python manage.py scaffold --refresh-urls


# Pass a custom config (e.g. for CI or dev presets)
python manage.py scaffold --config tools/dev-config.json




