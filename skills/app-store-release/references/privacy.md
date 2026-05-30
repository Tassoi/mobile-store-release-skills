# App Store Privacy Checks

Use this reference for privacy labels, privacy manifests, permission strings, and App Review notes.

## Inspect locally

- `ios/Runner/Info.plist`
- `ios/Runner/PrivacyInfo.xcprivacy` or other `.xcprivacy` files
- Entitlements files
- Firebase, analytics, ads, crash reporting, sign-in, push, maps, location, media, contacts, camera, microphone, Bluetooth, photo library, tracking, and background modes
- Third-party SDK documentation for data collection and required reason APIs

## Local blockers and warnings

- Missing `.xcprivacy` files are a warning or blocker when the app or SDKs use required reason APIs or declare collected data that needs a privacy manifest.
- Broad App Transport Security exceptions such as `NSAllowsArbitraryLoads` should be called out and matched with a release justification.
- Background modes such as `location`, `fetch`, `processing`, `audio`, or `remote-notification` require feature justification in review notes when their usage is not obvious.
- Location Always, push notifications, Apple Sign In, HealthKit, WeatherKit, maps, camera, photo library, local network, Bluetooth, microphone, contacts, or user-generated content should trigger a privacy/review-note check.

## Compare against App Store Connect

The local app behavior must match:

- App Privacy answers
- Data linked to user
- Data used for tracking
- Data not linked to user
- Required reason API declarations
- Permission purpose strings
- Review notes and demo account details

## Output

Report mismatches as release blockers unless the user explicitly asks for advisory-only review.
