VDR is a way of doing arithmetic that keeps answers exact as fractions instead of turning them into rounded decimals.

Most normal computing uses decimal or floating-point numbers. That is fast, but it means numbers get rounded all the time. Usually that is fine, but after enough steps the little rounding errors add up. Two things that should come back to the same value often do not.

VDR takes a different approach. Instead of saying “good enough, round it,” it keeps the number as exact integer relationships all the way through. If the answer is \(1/3\), it stays \(1/3\). If the answer is a more complicated fraction, VDR keeps the exact fraction. If something does not fit neatly into the current form, VDR stores the leftover structure instead of throwing it away.

In plain English, VDR is an exact arithmetic system for people who want:
- exact fractions,
- exact equality,
- no silent rounding drift,
- and clear control over precision.

It is not trying to replace all normal math or all normal computing. It is not meant to be faster than floating-point numbers. It is meant to be honest. Standard decimal arithmetic is fast because it cuts corners. VDR refuses to cut those corners, so it gives exact answers but can cost more time and memory.

That makes it useful in places where exactness matters more than speed:
- rational calculations,
- probability,
- number theory,
- geometry,
- cryptography,
- matrix identities,
- and any long chain of operations where rounding error would otherwise build up.

So the simplest way to think of VDR is this:

Decimal arithmetic is for fast approximate answers.  
VDR is for exact fractional answers.

Introduction

VDR stands for a system of exact arithmetic built from triples of integers. Every value is stored in a structured form that keeps track of both the main fraction and anything that could not be cleanly absorbed into that fraction at that step. Instead of losing information through rounding, VDR preserves it.

This gives VDR a very different personality from ordinary decimal arithmetic. In a normal calculator, repeated operations slowly drift because every step may round. In VDR, the same chain of operations can return exactly to where it started, because nothing was silently discarded.

That is the core idea: keep the structure, keep the fraction exact, and only choose a precision boundary when you deliberately want one.

VDR is best understood as a parallel arithmetic system to decimal. Decimal is built for bounded, approximate computation. VDR is built for exact fractional computation. Each has its place. The point of VDR is to make exactness practical where exactness matters.
