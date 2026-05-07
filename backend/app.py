import sys
from pathlib import Path

UPSTREAM_DIR = Path(__file__).parent.parent / "vendor" / "upstream"
sys.path.insert(1, str(UPSTREAM_DIR))

from sau_backend import app  # noqa: E402

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5409)
