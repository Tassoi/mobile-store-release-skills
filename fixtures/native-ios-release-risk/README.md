# Native iOS Release Risk Fixture

This fixture models a native iOS app without fastlane.

The skills should detect:

- Xcode project release path instead of fastlane automation.
- `Info.plist` permission strings and background modes that require App Review notes.
- `PrivacyInfo.xcprivacy` presence and required-reason API declarations.
- Entitlements that affect review, signing, and App Store Connect setup.

Do not copy this fixture into an app.
