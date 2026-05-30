#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

REQUIRED_SKILLS = {
    "app-store-release",
    "google-play-release",
    "mobile-release-coordinator",
}

SENSITIVE_PATTERNS = {
    "Webhook URL": re.compile(
        r"https://open\.[^\"'\s]+/" + r"open-apis/bot/|hooks\.slack\.com",
        re.I,
    ),
    "Service account private key": re.compile("-----BEGIN " + "PRIVATE KEY-----"),
    "Apple private key content": re.compile("-----BEGIN EC " + "PRIVATE KEY-----"),
    "Private key file": re.compile(r"AuthKey_[A-Z0-9]+\.p8"),
    "Keystore password": re.compile(r"(storePassword|keyPassword)\s*[:=]\s*['\"][^'\"]+['\"]"),
    "Non-example bundle id": re.compile(r"\bcom\.(?!example\b)[a-z0-9][a-z0-9_.-]+\b", re.I),
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_skill(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    metadata = skill_dir / "agents" / "openai.yaml"

    if not skill_md.exists():
        fail(f"{skill_dir.relative_to(ROOT)} is missing SKILL.md")
    if not metadata.exists():
        fail(f"{skill_dir.relative_to(ROOT)} is missing agents/openai.yaml")

    body = read(skill_md)
    if not body.startswith("---\n"):
        fail(f"{skill_md.relative_to(ROOT)} is missing YAML frontmatter")
    if not re.search(r"^name:\s*[-a-z0-9]+$", body, re.M):
        fail(f"{skill_md.relative_to(ROOT)} is missing a valid name field")
    if not re.search(r"^description:\s*.+$", body, re.M):
        fail(f"{skill_md.relative_to(ROOT)} is missing a description field")

    metadata_body = read(metadata)
    if "interface:" not in metadata_body:
        fail(f"{metadata.relative_to(ROOT)} is missing interface section")
    if f"${skill_dir.name}" not in metadata_body:
        fail(f"{metadata.relative_to(ROOT)} default_prompt must mention ${skill_dir.name}")


def validate_sensitive_content() -> None:
    checked_suffixes = {".md", ".txt", ".rb", ".py", ".yaml", ".yml", ".json"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in checked_suffixes:
            continue
        text = read(path)
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                fail(f"{label} found in {path.relative_to(ROOT)}")


def main() -> None:
    if not SKILLS.exists():
        fail("skills directory is missing")

    found = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    missing = REQUIRED_SKILLS - found
    if missing:
        fail(f"missing required skills: {', '.join(sorted(missing))}")

    for skill_name in sorted(REQUIRED_SKILLS):
        validate_skill(SKILLS / skill_name)

    validate_sensitive_content()
    print("OK: skills validated")


if __name__ == "__main__":
    main()
