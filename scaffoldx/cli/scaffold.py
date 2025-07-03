import re, subprocess, sys
from pathlib import Path
from colorama import Fore, init
import json

init(autoreset=True)

SETTINGS_PATH = Path("config/settings.py")
PROJECT_URLS = Path("config/urls.py")

BUILTINS = {
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
}
def load_config(path=".scaffoldrc.json"):
    cfg_path = Path(path)
    if cfg_path.exists():
        return json.loads(cfg_path.read_text())
    return {}

def get_apps(config):
    excluded = set(config.get("exclude_apps", []))
    settings_text = SETTINGS_PATH.read_text()

    # 👇 Extract just the INSTALLED_APPS list
    match = re.search(r'INSTALLED_APPS\s*=\s*\[([^\]]+)\]', settings_text)
    if not match:
        print(Fore.RED + "🚫 Could not find INSTALLED_APPS in settings.py")
        return []

    apps_raw = match.group(1)

    # 👇 Grab only quoted app names from that list
    apps = re.findall(r"'([^']+)'", apps_raw)

    return [app for app in apps if app not in excluded]

def create_app(app, dry_run=False):
  if not Path(app).exists():
    msg = (
      f"{Fore.YELLOW}[DRY-RUN] Would create app: {app}"
      if dry_run else f"{Fore.YELLOW}📦 Creating app: {app}"
    )
    print(msg)
    if not dry_run:
      subprocess.run([sys.executable, "manage.py", "startapp", app])
  else:
    print(Fore.GREEN + f"✅ App already exists: {app}")

def scaffold(app, dry_run=False):
  app_path = Path(app)
  if not app_path.exists():
    return

  def touch(p, content=""):
    if not p.exists():
      print(
        f"{Fore.YELLOW}[DRY-RUN] Would create {p}"
        if dry_run else f"{Fore.CYAN}📄 Created {p.name}"
      )
      if not dry_run:
        p.write_text(content)

  touch(app_path / "urls.py", "from django.urls import path\n\nurlpatterns = []\n")
  touch(app_path / "serializers.py")
  touch(app_path / "views.py", "from django.shortcuts import render\n")
  touch(app_path / "admin.py")
  touch(app_path / "tests.py")
  touch(app_path / "signals.py")

  for folder in ["templates", "static"]:
    dir_path = app_path / folder / app
    if not dir_path.exists():
      print(
        f"{Fore.YELLOW}[DRY-RUN] Would create {dir_path}"
        if dry_run else f"{Fore.CYAN}📁 Created {dir_path}"
      )
      if not dry_run:
        dir_path.mkdir(parents=True, exist_ok=True)
        (dir_path / "__init__.py").touch()

def update_urls(apps, dry_run=False):
  content = PROJECT_URLS.read_text()
  original = content

  if "include(" not in content:
    content = content.replace(
      "from django.urls import path",
      "from django.urls import path, include"
    )

  for app in apps:
    route = f"path('{app}/', include('{app}.urls'))"
    if route not in content:
      print(Fore.YELLOW + f"🔗 Adding URL for {app}")
      content = content.replace(
        "urlpatterns = [",
        f"urlpatterns = [\n    {route},"
      )
    else:
      print(Fore.GREEN + f"🔗 URL for {app} already exists")

  if dry_run and content != original:
    print(Fore.YELLOW + "[DRY-RUN] Would update urls.py")
  elif not dry_run and content != original:
    PROJECT_URLS.write_text(content)
    print(Fore.CYAN + "🔧 Updated project urls.py")
def main(args):
    """Entry point for scaffold CLI, receives options dict from Django command."""
    config_path = args.get("config") or ".scaffoldrc.json"
    config = load_config(config_path)
    apps = get_apps(config)
    dry = args.get("dry_run")
    print(Fore.BLUE + f"⚙️ Loaded config from {config_path}: {config}")



    if not apps:
        print(Fore.RED + "🚫 No custom apps found in settings.py — nothing to scaffold.")
        return

    if args.get("apps_only"):
        for app in apps:
            create_app(app, dry_run=dry)

    elif args.get("scaffold_only"):
        for app in apps:
            scaffold(app, dry_run=dry)

    elif args.get("refresh_urls"):
        update_urls(apps, dry_run=dry)

    else:
        for app in apps:
            create_app(app, dry_run=dry)
            scaffold(app, dry_run=dry)
        update_urls(apps, dry_run=dry)