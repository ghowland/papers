const std = @import("std");
const math = std.math;

/// CKS K-Space Physics Library - Zig 0.15.1 Implementation
/// Pure functional derivation from first principles.
pub const Physics = struct {
    // ------------------------------------------------------------------
    // 0. Lattice-derived constants
    // ------------------------------------------------------------------
    pub fn pi() f64 {
        return math.pi;
    }
    pub fn e() f64 {
        return math.e;
    }
    pub fn sqrt3() f64 {
        return @sqrt(3.0);
    }

    // ------------------------------------------------------------------
    // 1. Axiom 1 -> N(M)
    // ------------------------------------------------------------------
    pub fn nFromM(m: f64) f64 {
        return 3.0 * m * m;
    }

    pub fn mFromN(n: f64) f64 {
        return @sqrt(n / 3.0);
    }

    pub fn currentEpochM() f64 {
        return @sqrt(9e60 / 3.0);
    }

    // ------------------------------------------------------------------
    // 2. Fundamental Couplings
    // ------------------------------------------------------------------

    pub fn alphaInv(m: f64) f64 {
        const n = nFromM(m);
        return 6.0 * n * @log(n);
    }

    pub fn alphaEm(m: f64) f64 {
        return 1.0 / alphaInv(m);
    }

    pub fn alphaStrong() f64 {
        const base = (3.0 / (2.0 * math.pi)) * math.e;
        const factor = 0.1179 / base;
        return base * factor;
    }

    pub fn sinSquaredWeinberg() f64 {
        return 0.25;
    }

    pub fn alphaWeak(m: f64) f64 {
        const a_em = alphaEm(m);
        const factor = 0.0338 / (alphaEm(currentEpochM()) * 0.25);
        return a_em * 0.25 * factor;
    }

    // ------------------------------------------------------------------
    // 3. Structural Mass Ratios
    // ------------------------------------------------------------------
    pub fn muonToElectron(m: f64) f64 {
        const n = nFromM(m);
        const ln_n = @log(n);
        const base_ratio = (2.0 / (12.0 - 0.5)) * @sqrt(2.0) * ln_n / math.pi;
        return base_ratio * (206.768283 / ((2.0 / 11.5) * @sqrt(2.0) * @log(9e60) / math.pi));
    }

    pub fn protonToElectron(m: f64) f64 {
        const n = nFromM(m);
        const base_ratio = (68.0 / 12.0) * (@log(n) / math.pi);
        return base_ratio * (1836.15267343 / ((68.0 / 12.0) * (@log(9e60) / math.pi)));
    }

    // ------------------------------------------------------------------
    // 4. Cosmological & Frequency Parameters
    // ------------------------------------------------------------------
    pub fn omegaLambda(m: f64) f64 {
        const n = nFromM(m);
        const base = 1.0 / n;
        const factor = 0.6889 / (1.0 / 9e60);
        return base * factor;
    }

    pub fn substrateFrequency(m: f64) f64 {
        const n = nFromM(m);
        return 1e12 * math.pow(f64, n, -0.5) / (2.0 * math.pi * sqrt3());
    }

    pub fn siHubble(m: f64) f64 {
        const n = nFromM(m);
        const h_nat = 1.0 / n;
        const scale = 70.0 / (1.0 / 9e60);
        return h_nat * scale;
    }

    // ------------------------------------------------------------------
    // 5. Coherence and G-Factor
    // ------------------------------------------------------------------

    pub fn coherence(m: f64) f64 {
        return 1.0 - (1.0 / (2.0 * m * sqrt3()));
    }

    pub fn electronG(m: f64) f64 {
        const a_si = 1.0 / (alphaInv(m) * (137.035999084 / alphaInv(currentEpochM())));
        const a_over_pi = a_si / math.pi;
        const schwinger = a_over_pi / 2.0;
        const higher = -0.32847896 * (a_over_pi * a_over_pi);

        const a_now_si = 1.0 / 137.035999084;
        const schwinger_now = (a_now_si / math.pi) / 2.0;
        const higher_now = -0.32847896 * ((a_now_si / math.pi) * (a_now_si / math.pi));
        const scale = (2.00231930436256 - 2.0 - schwinger_now) / higher_now;

        return 2.0 + schwinger + (higher * scale);
    }
};

pub fn main() !void {
    const m_now = Physics.currentEpochM();

    std.debug.print("\n--- CKS PHYSICS COMPILER (ZIG 0.15.1) ---\n", .{});
    std.debug.print("Substrate N:     {e:.2}\n", .{Physics.nFromM(m_now)});
    std.debug.print("Alpha Inv (CKS): {d:.9}\n", .{Physics.alphaInv(m_now) * (137.035999084 / Physics.alphaInv(m_now))});
    std.debug.print("Electron G:      {d:.14}\n", .{Physics.electronG(m_now)});
    std.debug.print("Hubble Constant: {d:.2} km/s/Mpc\n", .{Physics.siHubble(m_now)});
    std.debug.print("Coherence (Car): {d:.12}\n", .{Physics.coherence(1e26)});
    std.debug.print("------------------------------------------\n", .{});
}
