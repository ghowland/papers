const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{
        .default_target = .{},
    });
    // const optimize = b.standardOptimizeOption(.{
    //     .preferred_optimize_mode = .Debug,
    //     // .preferred_optimize_mode = .ReleaseFast,
    // });

    const exe = b.addExecutable(.{
        .name = "toy_llm",
        .root_module = b.createModule(.{
            .root_source_file = b.path("toy_llm.zig"),
            .target = target,
            .optimize = .ReleaseFast,
        }),
    });

    b.installArtifact(exe);
}
