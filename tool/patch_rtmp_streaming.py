#!/usr/bin/env python3
"""Patch rtmp_streaming 2.0.1 for Flutter/AGP 9 built-in Kotlin."""

from pathlib import Path
import re
import sys

if len(sys.argv) != 2:
    print("Usage: patch_rtmp_streaming.py <build.gradle>")
    raise SystemExit(2)

path = Path(sys.argv[1]).expanduser().resolve()
if not path.is_file():
    print(f"ERROR: file not found: {path}")
    raise SystemExit(1)

text = path.read_text(encoding="utf-8")

# rtmp_streaming 2.0.1 declares Kotlin stdlib 2.4.10 internally.
# Flutter's AGP 9 built-in Kotlin compiler used by this project is older,
# so keep the plugin's stdlib aligned with the project's Kotlin toolchain.
text, version_count = re.subn(
    r"ext\.kotlin_version\s*=\s*['\"]2\.4\.10['\"]",
    "ext.kotlin_version = '2.3.20'",
    text,
    count=1,
)

# Migrate the plugin's legacy kotlinOptions block to the AGP 9 compilerOptions DSL.
text, kotlin_options_count = re.subn(
    r"(?ms)^\s*kotlinOptions\s*\{\s*jvmTarget\s*=\s*['\"]17['\"]\s*\}\s*",
    "    kotlin {\n        compilerOptions {\n            jvmTarget = org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17\n        }\n    }\n",
    text,
    count=1,
)

if version_count != 1:
    print("ERROR: rtmp_streaming Kotlin 2.4.10 declaration was not found.")
    raise SystemExit(1)

if kotlin_options_count != 1:
    print("ERROR: rtmp_streaming kotlinOptions block was not found.")
    raise SystemExit(1)

path.write_text(text, encoding="utf-8")

print(f"Patched: {path}")
print("- Kotlin stdlib: 2.4.10 -> 2.3.20")
print("- kotlinOptions -> compilerOptions")
