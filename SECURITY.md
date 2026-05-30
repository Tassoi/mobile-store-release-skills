# Security Policy

This repository contains release workflow guidance for App Store and Google Play publishing. It must not contain real credentials or private app identifiers.

## Do not submit

- App Store Connect private keys, key IDs, issuer IDs, team IDs, or real bundle IDs.
- Google Play service account JSON, keystores, keystore passwords, package names from private apps, or signing certificates.
- Webhook URLs, API tokens, CI secrets, production API hosts, screenshots from private consoles, or organization-specific release notes.
- Any example copied from a private repository without anonymization.

## Reporting security issues

If you find exposed credentials or private identifiers in this repository, open a private security advisory on GitHub when available. If private advisories are not enabled, open a minimal public issue that says a sensitive-content report is needed, but do not include the secret value.

## Supported security checks

The validator performs basic static checks for common credential patterns:

```sh
python3 scripts/validate_skills.py
```

These checks are not exhaustive. Contributors are responsible for reviewing examples, fixtures, screenshots, logs, and copied snippets before submitting changes.

## Maintainer response

Sensitive content should be removed from the repository history when practical. If a real credential was committed, rotate or revoke it at the provider immediately; deleting it from GitHub is not enough.
