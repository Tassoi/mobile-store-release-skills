# App Store Official Sources

Use this reference when App Store guidance depends on current Apple policy, App Store Connect behavior, privacy requirements, or review interpretation. Prefer Apple developer documentation and App Store Connect Help over third-party summaries.

## Priority sources

- App Review Guidelines: https://developer.apple.com/app-store/review/guidelines/
- App Review overview: https://developer.apple.com/app-store/review/
- App Store Connect Help: https://developer.apple.com/help/app-store-connect/
- TestFlight overview: https://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview/
- App Store Connect API: https://developer.apple.com/documentation/appstoreconnectapi
- Privacy manifest files: https://developer.apple.com/documentation/bundleresources/privacy-manifest-files
- App privacy details: https://developer.apple.com/app-store/app-privacy-details/
- Manage app privacy in App Store Connect: https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy/
- Upload app previews and screenshots: https://developer.apple.com/help/app-store-connect/manage-app-information/upload-app-previews-and-screenshots
- Screenshot specifications: https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/

## Must re-check official sources

Re-check official sources before final advice when the task involves:

- App Review rejection causes, appeals, review notes, demo accounts, subscriptions, in-app purchases, payments, user-generated content, safety, child-directed apps, AI-generated content, or regulated features.
- TestFlight external testing, beta app review, tester limits, export compliance, or encryption declarations.
- App Store Connect metadata, screenshots, app previews, age rating, privacy policy, support URLs, or release notes.
- App Privacy, privacy manifests, required reason APIs, tracking domains, third-party SDK privacy requirements, or permission purpose strings.
- App Store Connect API, API keys, Transporter, build upload, review submission, phased release, or automatic release behavior.

## Local-first rule

Read the repository first. Use local files such as `Info.plist`, `.xcprivacy`, entitlements, fastlane lanes, screenshots, metadata, and release notes to form the evidence table. Then use official sources to validate policy-sensitive conclusions.
