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

REQUIRED_CONTENT = {
    "skills/app-store-release/SKILL.md": [
        "PrivacyInfo.xcprivacy",
        "submit_for_review: true",
        "automatic_release: true",
        "skip_screenshots: true",
    ],
    "skills/google-play-release/SKILL.md": [
        "debug signing",
        "android/fastlane/Fastfile",
        "usesCleartextTraffic",
    ],
    "skills/mobile-release-coordinator/SKILL.md": [
        "PrivacyInfo.xcprivacy",
        "debug signing fallback",
    ],
}

FIXTURE_REQUIRED_FILES = [
    "fixtures/flutter-release-risk/README.md",
    "fixtures/flutter-release-risk/pubspec.yaml",
    "fixtures/flutter-release-risk/ios/fastlane/Fastfile",
    "fixtures/flutter-release-risk/ios/fastlane/metadata/en-US/release_notes.txt",
    "fixtures/flutter-release-risk/ios/Runner/Info.plist",
    "fixtures/flutter-release-risk/android/app/build.gradle.kts",
    "fixtures/flutter-release-risk/android/app/src/main/AndroidManifest.xml",
]

FIXTURE_REQUIRED_CONTENT = {
    "fixtures/flutter-release-risk/ios/fastlane/Fastfile": [
        "submit = to_bool(options[:submit], false)",
        "auto_release = to_bool(options[:auto_release], false)",
        "confirm = to_bool(options[:confirm], true)",
        "submit_for_review: submit",
        "automatic_release: auto_release",
        "skip_screenshots: true",
    ],
    "fixtures/flutter-release-risk/ios/Runner/Info.plist": [
        "NSAllowsArbitraryLoads",
        "NSLocationAlwaysAndWhenInUseUsageDescription",
        "UIBackgroundModes",
        "remote-notification",
    ],
    "fixtures/flutter-release-risk/android/app/build.gradle.kts": [
        "hasValidKeystore",
        "signingConfigs.getByName(\"release\")",
        "Release signing is not configured",
    ],
    "fixtures/flutter-release-risk/android/app/src/main/AndroidManifest.xml": [
        "android:usesCleartextTraffic=\"true\"",
        "android.permission.ACCESS_FINE_LOCATION",
        "android.permission.CAMERA",
    ],
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


def validate_required_content() -> None:
    for relative_path, snippets in REQUIRED_CONTENT.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(f"{relative_path} is missing")

        text = read(path)
        for snippet in snippets:
            if snippet not in text:
                fail(f"{relative_path} must mention {snippet!r}")


def validate_fixtures() -> None:
    for relative_path in FIXTURE_REQUIRED_FILES:
        if not (ROOT / relative_path).exists():
            fail(f"{relative_path} is missing")

    forbidden_paths = [
        ROOT / "fixtures/flutter-release-risk/ios/Runner/PrivacyInfo.xcprivacy",
        ROOT / "fixtures/flutter-release-risk/android/fastlane/Fastfile",
    ]
    for path in forbidden_paths:
        if path.exists():
            fail(f"{path.relative_to(ROOT)} must stay absent for this risk fixture")

    for relative_path, snippets in FIXTURE_REQUIRED_CONTENT.items():
        text = read(ROOT / relative_path)
        for snippet in snippets:
            if snippet not in text:
                fail(f"{relative_path} must contain fixture pattern {snippet!r}")


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
    validate_required_content()
    validate_fixtures()
    print("OK: skills validated")


if __name__ == "__main__":
    main()
