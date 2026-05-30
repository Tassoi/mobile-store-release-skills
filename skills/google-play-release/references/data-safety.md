# Google Play Data Safety Checks

Use this reference for Data safety, permissions, and Play policy review.

## Inspect locally

- `android/app/src/main/AndroidManifest.xml`
- Flavor-specific manifests
- Gradle dependencies and SDKs
- Release signing configuration in Gradle and `key.properties`/CI secrets references
- `android:usesCleartextTraffic` and any network security config
- Firebase, analytics, ads, crash reporting, sign-in, push, maps, location, media, contacts, camera, microphone, Bluetooth, photo library, health, financial, and background behavior
- Network and persistence layers that collect or transmit user data

## Local blockers and warnings

- Release builds signed with the debug signing config are a Play production blocker.
- Missing or local-only keystore configuration is a blocker for local release uploads and a CI setup risk.
- `android:usesCleartextTraffic="true"` should be reported as a warning or blocker unless scoped and justified.
- Sensitive permissions such as location, camera, accounts, storage, SMS, contacts, health, Bluetooth, or background behavior must align with Play declarations.
- Third-party SDKs can change Data safety answers even when app code does not directly collect the data.

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
