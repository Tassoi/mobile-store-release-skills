# Google Play Data Safety Checks

Use this reference for Data safety, permissions, and Play policy review.

## Inspect locally

- `android/app/src/main/AndroidManifest.xml`
- Flavor-specific manifests
- Gradle dependencies and SDKs
- Firebase, analytics, ads, crash reporting, sign-in, push, maps, location, media, contacts, camera, microphone, Bluetooth, photo library, health, financial, and background behavior
- Network and persistence layers that collect or transmit user data

## Compare against Play Console

The local app behavior must match:

- Data collected
- Data shared
- Data processed ephemerally
- Optional versus required data
- Data deletion path
- Encryption in transit
- Account creation and account deletion declarations
- Permissions declaration forms

## Output

Report mismatches as release blockers unless the user explicitly asks for advisory-only review.
