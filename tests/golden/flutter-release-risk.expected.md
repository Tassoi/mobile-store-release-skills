# Expected Output: flutter-release-risk

Fixture: `fixtures/flutter-release-risk`

An agent using `$mobile-release-coordinator` should identify these minimum findings:

## Shared

- Project stack: Flutter.
- Version source: `pubspec.yaml`.
- Store policy and privacy conclusions require official source checks before final advice.

## iOS / App Store

- Release tooling: `ios/fastlane/Fastfile` exists.
- TestFlight lane exists.
- App Store release lane exists.
- The release lane is upload-only by default: `submit:false`, `auto_release:false`, and `confirm:true`.
- `submit_for_review` and `automatic_release` are controlled by lane options and must be treated as high-risk when enabled.
- `skip_screenshots:true` means screenshots/media cannot be marked passed from fastlane evidence alone.
- `PrivacyInfo.xcprivacy` is intentionally absent in this fixture and must be reported as a manual privacy-manifest check.
- `Info.plist` contains `NSAllowsArbitraryLoads`, location permissions, and background modes that require privacy and App Review note checks.

## Android / Google Play

- `android/fastlane/Fastfile` is absent, so the skill must not invent Play upload automation.
- Release path is Gradle/AAB plus manual Play Console or explicit CI.
- Release signing must not fall back to debug signing.
- `android:usesCleartextTraffic="true"` must be reported as a network security risk.
- Location and camera permissions require Data safety and permissions declaration checks.
