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
