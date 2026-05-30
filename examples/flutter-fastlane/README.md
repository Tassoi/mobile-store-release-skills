# Flutter fastlane Example

This is an anonymized example showing how the skills expect to reason about a Flutter project that uses fastlane.

It intentionally uses placeholder identifiers and fake key paths. Do not copy credentials or organization-specific values into public repositories.

## iOS examples

```sh
cd ios
bundle exec fastlane ios beta env:prod confirm:true
bundle exec fastlane ios release env:prod submit:true auto_release:false confirm:true
```

## Android examples

```sh
cd android
bundle exec fastlane android internal env:prod
bundle exec fastlane android production env:prod rollout:0.1
```
