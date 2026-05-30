# App Store Privacy Checks

Use this reference for privacy labels, privacy manifests, permission strings, and App Review notes.

## Inspect locally

- `ios/Runner/Info.plist`
- `ios/Runner/PrivacyInfo.xcprivacy` or other `.xcprivacy` files
- Entitlements files
- Firebase, analytics, ads, crash reporting, sign-in, push, maps, location, media, contacts, camera, microphone, Bluetooth, photo library, tracking, and background modes
- Third-party SDK documentation for data collection and required reason APIs

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
