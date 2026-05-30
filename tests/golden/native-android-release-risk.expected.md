# Expected Output: native-android-release-risk

Fixture: `fixtures/native-android-release-risk`

An agent using `$google-play-release` or `$mobile-release-coordinator` should identify these minimum findings:

## Android / Google Play

- Project stack: native Android.
- Release tooling: Gradle project is present and `android/fastlane/Fastfile` is absent.
- Release path is Gradle AAB/APK plus manual Play Console or explicit CI.
- `targetSdk = 35` and target SDK policy must be checked against official Google Play sources before final advice.
- Release signing must use a real release keystore or Play App Signing flow and must not fall back to debug signing.
- `Release signing is not configured` failure path is present for release artifact tasks.
- `android:usesCleartextTraffic="true"` must be reported as a network security risk.
- Location, camera, and notification permissions require Data safety and permissions declaration checks.

## Expected Manual Checks

- Play Console Data safety, app access, content rating, countries, testing track, staged rollout, and review status remain manual unless local or CI evidence exists.
- Service account / Play API access is unknown because no fastlane or CI upload path exists.
