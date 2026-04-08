import sys
from pathlib import Path

# Ensure sibling modules (app.py, backend.py) are importable.
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import app
