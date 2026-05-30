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

GOVERNANCE_FILES = [
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/policy_update.yml",
    ".github/ISSUE_TEMPLATE/skill_gap.yml",
    ".github/pull_request_template.md",
    ".github/workflows/validate.yml",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "LICENSE",
    "README.md",
    "README.zh-CN.md",
    "SECURITY.md",
]

GOLDEN_EXPECTED_FILES = [
    "tests/golden/flutter-release-risk.expected.md",
    "tests/golden/native-ios-release-risk.expected.md",
    "tests/golden/native-android-release-risk.expected.md",
]

REQUIRED_CONTENT = {
    "skills/app-store-release/SKILL.md": [
        "PrivacyInfo.xcprivacy",
        "references/official-sources.md",
        "submit_for_review: true",
        "automatic_release: true",
        "skip_screenshots: true",
    ],
    "skills/google-play-release/SKILL.md": [
        "references/official-sources.md",
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
    "fixtures/native-ios-release-risk/README.md",
    "fixtures/native-ios-release-risk/App.xcodeproj/project.pbxproj",
    "fixtures/native-ios-release-risk/App/Info.plist",
    "fixtures/native-ios-release-risk/App/PrivacyInfo.xcprivacy",
    "fixtures/native-ios-release-risk/App/App.entitlements",
    "fixtures/native-android-release-risk/README.md",
    "fixtures/native-android-release-risk/settings.gradle.kts",
    "fixtures/native-android-release-risk/build.gradle.kts",
    "fixtures/native-android-release-risk/app/build.gradle.kts",
    "fixtures/native-android-release-risk/app/src/main/AndroidManifest.xml",
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
    "fixtures/native-ios-release-risk/App/Info.plist": [
        "CFBundleIdentifier",
        "NSCameraUsageDescription",
        "NSLocationWhenInUseUsageDescription",
        "UIBackgroundModes",
    ],
    "fixtures/native-ios-release-risk/App/PrivacyInfo.xcprivacy": [
        "NSPrivacyAccessedAPITypes",
        "NSPrivacyAccessedAPICategoryUserDefaults",
        "NSPrivacyTracking",
    ],
    "fixtures/native-ios-release-risk/App/App.entitlements": [
        "aps-environment",
        "com.apple.developer.applesignin",
        "com.apple.developer.associated-domains",
    ],
    "fixtures/native-android-release-risk/app/build.gradle.kts": [
        "com.android.application",
        "targetSdk = 35",
        "hasValidKeystore",
        "Release signing is not configured",
    ],
    "fixtures/native-android-release-risk/app/src/main/AndroidManifest.xml": [
        "android:usesCleartextTraffic=\"true\"",
        "android.permission.POST_NOTIFICATIONS",
        "android.permission.ACCESS_FINE_LOCATION",
    ],
    "README.md": [
        "| Native iOS | Partial |",
        "| Native Android | Partial |",
        "dedicated fixture coverage exists",
        "tests/golden/",
        "README.zh-CN.md",
        "CHANGELOG.md",
    ],
    "README.zh-CN.md": [
        "快速开始",
        "支持矩阵",
        "安全模型",
        "Fixtures 与 Golden Expectations",
        "python3 scripts/validate_skills.py",
    ],
    "CHANGELOG.md": [
        "## Unreleased",
        "Native iOS release-risk fixture",
        "Native Android release-risk fixture",
        "Official source references",
        "Golden expected outputs",
        "Chinese README",
        "Validator now checks",
    ],
    "skills/app-store-release/references/official-sources.md": [
        "App Review Guidelines",
        "App Store Connect Help",
        "Privacy manifest files",
        "Must re-check official sources",
        "Local-first rule",
    ],
    "skills/google-play-release/references/official-sources.md": [
        "Play Console Help",
        "Google Play Policy Center",
        "Target API level requirements",
        "Data safety section",
        "Play App Signing",
        "Must re-check official sources",
        "Local-first rule",
    ],
}

GOLDEN_REQUIRED_CONTENT = {
    "tests/golden/flutter-release-risk.expected.md": [
        "Fixture: `fixtures/flutter-release-risk`",
        "Project stack: Flutter",
        "ios/fastlane/Fastfile",
        "submit:false",
        "auto_release:false",
        "confirm:true",
        "skip_screenshots:true",
        "PrivacyInfo.xcprivacy",
        "`android/fastlane/Fastfile` is absent",
        "android:usesCleartextTraffic=\"true\"",
        "Data safety",
    ],
    "tests/golden/native-ios-release-risk.expected.md": [
        "Fixture: `fixtures/native-ios-release-risk`",
        "Project stack: native iOS",
        "`ios/fastlane/Fastfile` is absent",
        "Xcode archive/export",
        "`PrivacyInfo.xcprivacy` exists",
        "push notifications",
        "Apple Sign In",
        "official Apple source checks",
    ],
    "tests/golden/native-android-release-risk.expected.md": [
        "Fixture: `fixtures/native-android-release-risk`",
        "Project stack: native Android",
        "`android/fastlane/Fastfile` is absent",
        "targetSdk = 35",
        "must not fall back to debug signing",
        "Release signing is not configured",
        "android:usesCleartextTraffic=\"true\"",
        "Data safety",
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
    "Non-example bundle id": re.compile(
        r"\b"
        + r"com\."
        + r"(?!(example|apple|android|google)\b)[a-z0-9][a-z0-9_.-]+\b",
        re.I,
    ),
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


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


def validate_reference_links(skill_dir: Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    references_dir = skill_dir / "references"
    body = read(skill_md)
    referenced = set(re.findall(r"`(references/[^`]+\.md)`", body))

    for reference in referenced:
        path = skill_dir / reference
        if not path.exists():
            fail(f"{relative(skill_md)} references missing file {reference}")

    if references_dir.exists():
        for reference_path in references_dir.glob("*.md"):
            reference = f"references/{reference_path.name}"
            if reference not in body:
                fail(f"{relative(reference_path)} is not referenced from {relative(skill_md)}")


def validate_governance_files() -> None:
    for relative_path in GOVERNANCE_FILES:
        if not (ROOT / relative_path).exists():
            fail(f"{relative_path} is missing")


def validate_sensitive_content() -> None:
    checked_suffixes = {".md", ".txt", ".rb", ".py", ".yaml", ".yml", ".json"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in checked_suffixes:
            continue
        text = read(path)
        for label, pattern in SENSITIVE_PATTERNS.items():
            if pattern.search(text):
                fail(f"{label} found in {path.relative_to(ROOT)}")


def validate_examples_and_fixtures_contract() -> None:
    examples_dir = ROOT / "examples"
    fixtures_dir = ROOT / "fixtures"

    if not examples_dir.exists():
        fail("examples directory is missing")
    if not fixtures_dir.exists():
        fail("fixtures directory is missing")

    for readme in examples_dir.glob("*/README.md"):
        text = read(readme).lower()
        if "anonymized" not in text or "placeholder" not in text:
            fail(f"{relative(readme)} must explain anonymized placeholders")
        if "do not copy this fixture" in text or "validation fixture" in text:
            fail(f"{relative(readme)} mixes fixture language into an example")

    for readme in fixtures_dir.glob("*/README.md"):
        text = read(readme).lower()
        if "do not copy" not in text:
            fail(f"{relative(readme)} must say fixtures should not be copied into apps")
        if "fixture" not in text:
            fail(f"{relative(readme)} must identify itself as a fixture")


def validate_readme_fixture_matrix() -> None:
    readme = read(ROOT / "README.md")
    matrix_expectations = {
        "flutter-release-risk": "| Flutter + iOS fastlane | Supported |",
        "native-ios-release-risk": "| Native iOS | Partial |",
        "native-android-release-risk": "| Native Android | Partial |",
    }

    for fixture_name, matrix_row in matrix_expectations.items():
        if not (ROOT / "fixtures" / fixture_name).exists():
            fail(f"fixtures/{fixture_name} is missing")
        if matrix_row not in readme:
            fail(f"README support matrix must include {matrix_row!r}")

    for fixture_name in matrix_expectations:
        if f"`{fixture_name}`" not in readme:
            fail(f"README fixtures section must mention `{fixture_name}`")


def validate_golden_outputs() -> None:
    for relative_path in GOLDEN_EXPECTED_FILES:
        if not (ROOT / relative_path).exists():
            fail(f"{relative_path} is missing")

    for relative_path, snippets in GOLDEN_REQUIRED_CONTENT.items():
        text = read(ROOT / relative_path)
        for snippet in snippets:
            if snippet not in text:
                fail(f"{relative_path} must contain golden expectation {snippet!r}")


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
        ROOT / "fixtures/native-ios-release-risk/ios/fastlane/Fastfile",
        ROOT / "fixtures/native-android-release-risk/android/fastlane/Fastfile",
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
        skill_dir = SKILLS / skill_name
        validate_skill(skill_dir)
        validate_reference_links(skill_dir)

    validate_governance_files()
    validate_sensitive_content()
    validate_required_content()
    validate_fixtures()
    validate_examples_and_fixtures_contract()
    validate_readme_fixture_matrix()
    validate_golden_outputs()
    print("OK: skills validated")


if __name__ == "__main__":
    main()
