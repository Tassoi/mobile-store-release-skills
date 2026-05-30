# Google Play fastlane Checks

Use this reference only when the repository has `android/fastlane/Fastfile` or the user asks about fastlane.

## What to inspect

- Package name and JSON key/service account configuration
- Lane names and descriptions
- Gradle task, flavor, build type, and artifact path
- Track: `internal`, `alpha`, `beta`, `production`, or custom track
- Rollout percentage and release status
- `upload_to_play_store` options
- Metadata, image, and screenshot upload flags
- Changelog source and locale coverage
- Notification hooks and environment variables

## Safe command guidance

Do not invent lane names. If the lane requires options, preserve the repository's option names.

Example pattern:

```sh
cd android
bundle exec fastlane android <lane> key:value key2:value2
```

## Common risks

- `versionCode` is not incremented.
- The lane uploads to production by default.
- The project has no `android/fastlane/Fastfile`, so Play upload is manual or handled by another CI path.
- Release builds fall back to debug signing when keystore config is missing.
- Service account JSON is only available locally.
- Release status is `completed` when staged rollout was intended.
- Data safety declarations are stale after SDK or feature changes.

## When Android fastlane is absent

Report the absence explicitly. Recommend the repository's existing build command for producing an AAB, then list Play Console manual steps or suggest adding a fastlane/CI lane only if the user wants automation.
