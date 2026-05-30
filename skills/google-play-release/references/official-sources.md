# Google Play Official Sources

Use this reference when Google Play guidance depends on current policy, Play Console behavior, Android platform requirements, signing, privacy declarations, or rollout behavior. Prefer Google Play Console Help and Android Developers over third-party summaries.

## Priority sources

- Play Console Help: https://support.google.com/googleplay/android-developer/
- Google Play Policy Center: https://support.google.com/googleplay/android-developer/topic/9877466
- Target API level requirements: https://support.google.com/googleplay/android-developer/answer/11926878
- Google Play target API level policy: https://support.google.com/googleplay/android-developer/answer/16561298
- Data safety section: https://support.google.com/googleplay/android-developer/answer/10787469
- Play App Signing: https://support.google.com/googleplay/android-developer/answer/9842756
- App bundles and APKs / latest releases and bundles: https://support.google.com/googleplay/android-developer/answer/9844279
- Create and set up your app: https://support.google.com/googleplay/android-developer/answer/9859152
- Internal app sharing: https://support.google.com/googleplay/android-developer/answer/9844679
- Staged rollouts: https://support.google.com/googleplay/android-developer/answer/6346149
- Android app signing: https://developer.android.com/studio/publish/app-signing
- Android App Bundle: https://developer.android.com/guide/app-bundle

## Must re-check official sources

Re-check official sources before final advice when the task involves:

- Target SDK/API level deadlines, app availability, policy exceptions, or extension requests.
- Data safety, data deletion, account deletion, permissions declarations, ads, tracking, SDK behavior, or sensitive permissions.
- App Bundle requirements, APK exceptions, Play App Signing, upload keys, signing key rotation, or release artifact compatibility.
- Internal testing, closed/open testing, production rollout, staged rollout, release status, country targeting, or halted/resumed rollout behavior.
- App access instructions, demo credentials, content rating, health, financial, VPN, background location, SMS/call log, notification, or user-generated content policies.
- Play Console review issues, policy appeals, enforcement, or rejection remediation.

## Local-first rule

Read the repository first. Use local files such as Gradle build files, manifests, signing config, version sources, fastlane lanes, metadata, and changelogs to form the evidence table. Then use official sources to validate policy-sensitive conclusions.
