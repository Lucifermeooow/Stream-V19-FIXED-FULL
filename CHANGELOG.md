# Stream V19

- Rebuilt as a clean GitHub-ready Flutter project.
- Migrated to `rtmp_streaming` 2.0.1.
- Uses `stopStreaming()` and the current camera-switch API contract.
- Compile SDK raised to Android API 37 to satisfy RootEncoder 2.8.0.
- GitHub Actions pinned to Flutter 3.47.2 and Java 17.
- Added format, analyze and test gates before APK build.
- Removed hard-coded stream endpoint / secrets.
- Added live bitrate/FPS/RTT telemetry when supported.

- Patched `rtmp_streaming` 2.0.1 during GitHub Actions to align Kotlin stdlib with the Flutter AGP 9 built-in Kotlin toolchain and migrated its legacy `kotlinOptions` block to `compilerOptions`.
- Pinned the Android build to AGP 9.0.1, Kotlin 2.3.20 and Gradle 9.3.1.
