# Contributing

Contributions are welcome when they keep the skills generic, safe, and verifiable.

## Rules

- Do not commit real credentials, private key names, service account JSON, webhook URLs, package names from private apps, Apple team IDs, issuer IDs, or bundle IDs.
- Prefer official Apple, Google, Android, fastlane, Flutter, React Native, and Expo documentation for platform facts.
- Keep `SKILL.md` concise. Put detailed platform notes in `references/`.
- Examples must be anonymized and runnable only after replacing placeholders.
- Fixtures must be anonymized and may intentionally contain risky patterns for validation.
- Do not add project-specific company process unless it is clearly marked as a generic pattern.

## Before opening a PR

Run:

```sh
python3 scripts/validate_skills.py
```

If you add a new skill, include:

- `SKILL.md`
- `agents/openai.yaml`
- At least one useful checklist or reference when the workflow has platform-specific details

## Policy updates

Store policy changes are time-sensitive. When changing release policy guidance, include the official source in the PR description and avoid copying long policy text into the repository.
