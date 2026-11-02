#!/usr/bin/env python3
"""Verify a reviewed fork revision and optionally configure the user proto plugin."""
import argparse
import datetime
import hashlib
import re
import shutil
import subprocess
import urllib.request
from pathlib import Path

APPROVED_SHA256 = "769673f5163e639c4e05886f77ce4c2791e952c5c5f37044e21d47f5e04166b6"
BASE = "https://raw.githubusercontent.com/austinyuch/proto-dotnet-plugin"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("commit", help="Reviewed full 40-character Git commit SHA")
    parser.add_argument("--apply", action="store_true", help="Back up and update ~/.prototools")
    args = parser.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.commit):
        parser.error("A full lowercase commit SHA is required; branches and tags are rejected")
    url = f"{BASE}/{args.commit}/plugin.toml"
    with urllib.request.urlopen(url, timeout=30) as response:
        if response.geturl() != url:
            raise SystemExit("Unexpected redirect; refusing plugin source")
        content = response.read(65537)
    if len(content) > 65536 or hashlib.sha256(content).hexdigest() != APPROVED_SHA256:
        raise SystemExit("Plugin differs from reviewed SHA-256; review before updating wrapper")
    print(f"Verified plugin: {url}")
    print(f"SHA-256: {APPROVED_SHA256}")
    if not args.apply:
        print("Dry run. Add --apply to configure the user-level plugin.")
        return
    proto = Path.home() / ".proto/bin/proto"
    if not proto.is_file():
        raise SystemExit("Expected proto executable at ~/.proto/bin/proto")
    config = Path.home() / ".prototools"
    if config.is_symlink():
        raise SystemExit("Refusing symlinked user configuration")
    if config.exists():
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        backup = config.with_name(f".prototools.backup-{stamp}")
        shutil.copy2(config, backup)
        print(f"Backup: {backup}")
    subprocess.run([str(proto), "plugin", "add", "dotnet", url, "--to", "user"], check=True)
    print("Configured pinned plugin. No SDK was installed.")


if __name__ == "__main__":
    main()
