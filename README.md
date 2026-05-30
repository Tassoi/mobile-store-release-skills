# Mobile Store Release Skills

Reusable Codex skills for preparing mobile app releases for Apple App Store and Google Play.

The skills are intentionally project-agnostic. They detect local release tooling such as fastlane,
Flutter, React Native, native iOS, or native Android, then adapt the checklist to the repository.

## Install

Clone this repository, then copy the skills you want into your Codex skills directory:

```sh
CODEX_SKILLS_DIR="${CODEX_HOME:-$HOME/.codex}/skills"
mkdir -p "$CODEX_SKILLS_DIR"
cp -R skills/app-store-release "$CODEX_SKILLS_DIR/"
cp -R skills/google-play-release "$CODEX_SKILLS_DIR/"
cp -R skills/mobile-release-coordinator "$CODEX_SKILLS_DIR/"
```

If your Codex installation uses a different skills directory, replace `CODEX_SKILLS_DIR` with that path.

## Skills

- `app-store-release`: App Store Connect, TestFlight, iOS signing, metadata, privacy, and review flow.
- `google-play-release`: Google Play Console, Android signing, testing tracks, Data safety, and release flow.
- `mobile-release-coordinator`: Cross-platform entrypoint that chooses the platform skill and checks shared release state.

## Usage

Example prompts:

```text
Use $mobile-release-coordinator to check whether this Flutter app is ready for both stores.
Use $app-store-release to prepare a TestFlight upload from the current repository.
Use $google-play-release to inspect Android release readiness and find Play Console blockers.
```

The skills do not run production release commands blindly. They first inspect the repository,
identify the real release path, and report the exact command or manual step that matches the project.

## Design

- Do not hard-code bundle IDs, team IDs, issuer IDs, API key paths, webhook URLs, or organization-specific policies.
- Treat platform policy and deadline information as time-sensitive. Verify against official Apple or Google documentation before giving final release advice.
- Prefer the repository's existing release path. If `ios/fastlane/Fastfile` or `android/fastlane/Fastfile` exists, inspect it before suggesting commands.
- Keep public examples anonymized.
- Keep `SKILL.md` concise and move platform details into `references/`.

## Example

`examples/flutter-fastlane/` shows anonymized fastlane lanes for Flutter iOS and Android projects.
They are examples only; copy the structure, not the placeholder values.

## Fixtures

`fixtures/` contains anonymized project slices used by validation. They intentionally include release risks so the skills and validator can catch regressions. Do not copy fixtures into an app; use `examples/` for implementation patterns.

## Validate

Run:

```sh
python3 scripts/validate_skills.py
```

The validator checks required skill files, UI metadata, frontmatter, and common credential or private-identifier patterns that should not appear in public examples.

## Scope

This repository provides agent workflow guidance. It does not replace Apple, Google, Android,
Flutter, React Native, Expo, or fastlane documentation. Store policies change over time, so agents
using these skills should verify current policy facts with official sources before final release advice.
