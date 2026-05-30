# App Store fastlane Checks

Use this reference only when the repository has `ios/fastlane/Fastfile` or the user asks about fastlane.

## What to inspect

- `default_platform`
- `app_identifier`, `team_id`, and App Store Connect API key usage
- Lane names and descriptions
- Build command and export method
- Version/build-number source
- `upload_to_testflight` options
- `upload_to_app_store` or `deliver` options
- `skip_metadata`, `skip_screenshots`, `submit_for_review`, `automatic_release`, `phased_release`
- `precheck` usage or absence
- Notification hooks and environment variables
- Metadata and screenshots directories

## Safe command guidance

Do not invent lane names. If the lane requires options, preserve the repository's option names.

Example pattern:

```sh
cd ios
bundle exec fastlane ios <lane> key:value key2:value2
```

## Common risks

- The lane uploads metadata but not screenshots.
- The lane submits for review automatically.
- `automatic_release` is true by default, which can release immediately after approval.
- `submit_for_review` is true by default, which turns a build upload into a review submission.
- `skip_screenshots: true` requires manual App Store Connect screenshot confirmation or a separate screenshot lane.
- Build number comes from a file outside Xcode project settings.
- Release notes exist for only one locale.
- API key files are referenced from local paths that CI may not have.
- Production environment flags are implicit or defaulted.

## Risk handling

When a lane can submit or auto-release, recommend an explicit dry-run style command first, for example with `submit:false`, `auto_release:false`, or the repository's equivalent lane options. Preserve the repository's actual option names.

If screenshots are skipped, do not mark screenshots/media as passed from fastlane evidence alone. Mark it `Unknown` or `Fail` until App Store Connect or another screenshot upload path is verified.
