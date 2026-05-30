# Expected Output: native-ios-release-risk

Fixture: `fixtures/native-ios-release-risk`

An agent using `$app-store-release` or `$mobile-release-coordinator` should identify these minimum findings:

## iOS / App Store

- Project stack: native iOS.
- Release tooling: Xcode project is present and `ios/fastlane/Fastfile` is absent.
- Release path is Xcode archive/export plus App Store Connect or Transporter unless another CI path is discovered.
- `Info.plist` contains camera, location, and background mode declarations that require privacy and review-note checks.
- `PrivacyInfo.xcprivacy` exists and should be checked against collected data, tracking, and required reason APIs.
- Entitlements include push notifications, Apple Sign In, and associated domains; signing, capabilities, App Store Connect setup, and review notes must be checked.
- Store policy and privacy conclusions require official Apple source checks before final advice.

## Expected Manual Checks

- App Store Connect metadata, screenshots, app previews, support URL, privacy policy, age rating, and review details remain manual unless local evidence exists.
- Signing certificates, provisioning profiles, and export method are unknown from this minimal fixture and must not be marked passed.
