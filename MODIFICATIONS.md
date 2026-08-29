# Stream V19 build fixes

This repository was reviewed from the supplied Stream V19 ZIP.

## Applied fixes

- Kept the app name and package identity on Stream V19.
- Pinned `rtmp_streaming` to exactly `2.0.1`.
- Updated the project Android toolchain to AGP 9.0.1, Kotlin 2.3.20 and Gradle 9.3.1.
- Kept Android built-in Kotlin enabled.
- Added a repository-side patch script for `rtmp_streaming 2.0.1`.
- The patch changes the plugin's internal Kotlin stdlib from 2.4.10 to 2.3.20 so it matches the Flutter/AGP built-in Kotlin compiler used by the project.
- The patch migrates the plugin's legacy `kotlinOptions` block to the AGP 9 `compilerOptions` DSL.
- The GitHub Actions workflow runs `flutter precache --android` before the build.
- The workflow runs `flutter analyze` and `flutter test` before creating the release APK.
- The workflow uploads `Stream-V19-release.apk` as the `Stream-V19-APK` artifact.
- Removed the fragile inline YAML/Python heredoc patching approach; the patch now lives in `tool/patch_rtmp_streaming.py`.

## What was intentionally not changed

- The Dart streaming UI and RTMP flow were not rewritten.
- No stream keys, OAuth secrets, passwords or backend credentials were added.
- The RTMP endpoint remains user-configurable.
