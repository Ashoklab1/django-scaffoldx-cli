from django.core.management.base import BaseCommand
from scaffoldx.cli.scaffold import main

class Command(BaseCommand):
  help = "Generate apps, scaffold files, and update URLs"

  def add_arguments(self, parser):
    parser.add_argument("--apps-only", action="store_true")
    parser.add_argument("--scaffold-only", action="store_true")
    parser.add_argument("--refresh-urls", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--config", type=str, help="Path to custom JSON config file (e.g. tools/dev-config.json)")

  def handle(self, *args, **options):
    main(options)

def handle(self, *args, **options):
  print("✅ Command loaded!")