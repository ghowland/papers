#!/bin/bash -e

ZIG=/mnt/c/zig/zig-x86_64-windows-0.15.1/zig.exe

reset ; $ZIG build -freference-trace --prefix build/ && \
  ./build/bin/toy_llm.exe

