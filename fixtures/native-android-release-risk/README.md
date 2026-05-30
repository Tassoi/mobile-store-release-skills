# Native Android Release Risk Fixture

This fixture models a native Android app without fastlane.

The skills should detect:

- Gradle/Play Console release path instead of fastlane automation.
- Release signing that must not fall back to debug signing.
- `android:usesCleartextTraffic="true"` as a network security risk.
- Sensitive permissions that affect Play declarations and Data safety.

Do not copy this fixture into an app.
