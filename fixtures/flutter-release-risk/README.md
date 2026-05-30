# Flutter Release Risk Fixture

This fixture is an anonymized project slice used by CI validation.

It models release risks that the skills must recognize:

- iOS fastlane uploads metadata but skips screenshots.
- iOS release defaults are conservative: upload only, no review submission, no auto-release, confirmation enabled.
- iOS `Info.plist` includes permissions/background modes that require privacy and review checks.
- `PrivacyInfo.xcprivacy` is intentionally absent, so the skill should report a manual privacy-manifest check.
- Android has no `android/fastlane/Fastfile`, so the skill must not invent Play upload automation.
- Android release signing fails when a real release keystore is unavailable instead of falling back to debug signing.
- Android cleartext traffic is enabled and must be reported as a risk.

Do not copy this fixture into an app. Use `examples/` for copyable patterns.
