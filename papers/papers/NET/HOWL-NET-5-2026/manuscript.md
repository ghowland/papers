# NQDP: A Query-Based Diagnostic Protocol for IPv4-64
## Replacing ICMP's diagnostic role with a fixed-size, trust-gated, carrier-controlled query service that reveals nothing to attackers and everything to the operators who are entitled to it

**Registry:** [@HOWL-NET-5-2026]

**Series Path:** [@HOWL-NET-1-2026] → [@HOWL-NET-2-2026] → [@HOWL-NET-3-2026] → [@HOWL-NET-4-2026] → [@HOWL-NET-5-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** October 2026

**Domain:** Network Protocol Design / Diagnostics / Programmable Dataplane Engineering

**Status:** Proposal — Not submitted to any standards body. Published for public review and discussion.

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections and one biographical note were edited by the author. All paper content was LLM-generated using Anthropic's Claude 4.8 Opus. 

**License:** Open specification. No patent claims. Free to implement, extend, and reference.

---

## 1. Purpose

This document specifies NQDP, the Network Query Diagnostic Protocol. NQDP is the diagnostic service for IPv4-64, the protocol defined in the companion documents [@HOWL-NET-1-2026] through [@HOWL-NET-4-2026].

IPv4-64 deliberately removed ICMP's role from the forwarding plane. The forwarding plane answers no questions. It drops malformed, undeliverable, or unrecognized packets in silence. This is a security decision, explained in Section 2. But diagnostics are necessary. Operators must be able to ask whether a destination is reachable, what a route looks like, and which instance of an anycast service they are hitting. NQDP provides that capability as a separate service that runs above the forwarding plane, not inside it.

NQDP is a proposal. It is not a plan, not a mandate, and not a replacement for any deployed system. It exists because IPv6, for all that it advanced the art, is not desirable in many networks, and the diagnostic model built into the IP layer — ICMP — carries costs that a modern design should not accept. NQDP keeps the diagnostic capability operators need while removing the attack surface that capability has always carried.

---

## 2. Background

### 2.1 What ICMP Is

ICMP is the Internet Control Message Protocol. It is the part of IP that generates diagnostic and error messages. When a router drops a packet because its time-to-live reached zero, it sends an ICMP "Time Exceeded" message back to the sender. When a host is asked for a service it does not run, it sends an ICMP "Port Unreachable." The `ping` command works by sending an ICMP "Echo Request" and waiting for an "Echo Reply." The `traceroute` command works by sending packets with increasing time-to-live values and reading the ICMP "Time Exceeded" messages that come back from each hop.

ICMP was designed in 1981, when every host on the network was trusted. It was built into the IP layer so that any router or host could answer a diagnostic query as a side effect of normal forwarding. This made debugging easy.

### 2.2 Why ICMP Is a Problem

The same property that makes ICMP useful to an operator makes it useful to an attacker. Every ICMP response confirms that a host exists. A scanner sends a probe to an address; if an ICMP reply comes back, the scanner knows a live host is there. The content of the reply often reveals which operating system the host runs, because different systems generate different time-to-live values and message formats. This is reconnaissance, and ICMP hands it out for free to anyone who asks.

ICMP also shares a channel with production traffic. It operates at the IP layer, the same layer that forwards real data. There is no clean way to say "answer diagnostic queries from my operations team but not from the internet," because the forwarding plane itself emits the responses. An operator can configure a firewall to suppress some ICMP, but that is a patch applied per host or per network, not a property of the protocol.

The companion documents established the principle that a modern forwarding plane should reveal nothing and answer nothing. A malformed packet is dropped in silence. A scan receives no response. This closes the reconnaissance surface completely. But it also removes `ping`, `traceroute`, and path-MTU discovery, because those tools depend on the forwarding plane answering. NQDP restores the diagnostic capability without restoring the surface.

### 2.3 The Design Inversion

ICMP answers anyone, reveals host existence, shares a channel with production traffic, and generates responses as a side effect of forwarding. NQDP is the opposite on every axis.

NQDP answers only the parties the carrier chooses. It reveals only the facts the carrier chooses to disclose. It runs as its own service, not as a side effect of forwarding. And it generates a response only on an explicit, authenticated request. The capability is the same — tell me about reachability and paths — but the control over who learns what belongs entirely to the carrier.

---

## 3. What NQDP Is

NQDP is an application-layer protocol. It runs as ordinary payload over IPv4-64 UDP, on port 56789. It is not part of the forwarding plane. The forwarding plane carries NQDP packets exactly as it carries any other UDP traffic, through the same seven phases, under the same security gates, with no special handling.

A requester sends one fixed-size request naming a target prefix. A responder sends back one fixed-size response containing every diagnostic fact it is willing to disclose about that target, computed at one instant. One request, one response, both of fixed size, both known in full before a byte moves.

The facts NQDP carries are the ones network operators actually ask for: the cost to reach a target, the origin autonomous system seen for it, the next-hop autonomous system, a summary of the path, whether the route is RPKI-valid, whether the target is reachable, how long its route has been stable, and which instance of an anycast service was reached. Each fact is a single number. None of them is the full network path, because the full path is topology, and disclosing topology is the reconnaissance problem NQDP exists to avoid.

### 3.1 Terms Used in This Document

**Autonomous System (AS).** A network under one administrative control, identified by a number. BGP routes traffic between autonomous systems.

**BGP.** The Border Gateway Protocol, which routers use to exchange reachability information across the internet. A router's BGP table holds the routes it knows and the cost it assigns to each.

**AS_PATH.** The list of autonomous systems a route passes through. It is the standard way to understand where traffic goes and how it gets there.

**RPKI.** Resource Public Key Infrastructure, a system for cryptographically validating that an autonomous system is authorized to originate a route. An RPKI-valid route is trustworthy; an RPKI-invalid route may be a hijack.

**Anycast.** A service deployed at many locations that share one address. Traffic to that address is delivered to whichever instance is nearest. Anycast makes it hard to tell which instance answered.

**SVT.** The Source Validation Token from [@HOWL-NET-1-2026]. It is a cryptographic stamp a router applies that lets a receiver verify the source of a packet. In NQDP, the SVT determines whether a requester is trusted.

**Fixed offset.** A field is at a fixed offset when it always sits at the same byte position in every packet. There is nothing to calculate and nothing to parse wrong.

**Sentinel.** A reserved value that means "no answer here." In NQDP the sentinel is always all-ones for the field's width.

---

## 4. The Core Design Choices

NQDP makes five choices that shape everything else. Each one is explained here before the packet formats, so the formats read as consequences rather than decisions.

### 4.1 Everything Comes Back, Always

A requester cannot ask for a subset of facts. It sends one request and receives the complete record every time. This has three consequences.

First, there is exactly one request shape and one response shape, so there is exactly one implementation. A protocol that let you select fields would have many possible response shapes, and implementations would diverge on how they handle the ones you did not ask for.

Second, the response is a compile-time constant size, identical regardless of what was answered. An observer cannot tell a rich answer from an empty one by looking at the length.

Third, the response drops directly into a time series. Every field is always present at the same offset, so each response is one row with every column populated. Analyzing change over time becomes trivial: compare this row to the last.

### 4.2 Withheld and Unknown Look the Same

A field the carrier chooses not to disclose carries the sentinel. A field the responder genuinely cannot determine also carries the sentinel. On the wire they are identical. This is deliberate. If the packet announced "I am withholding this," an attacker could poll a responder and map exactly what each carrier will and will not disclose. By making withheld and unknown indistinguishable, NQDP keeps the carrier's disclosure policy unprobeable. The requester, who knows its own relationship with the carrier, can interpret a sentinel in context; a stranger cannot.

### 4.3 The Responder Reads Nothing the Requester Claims About Itself

The only requester-supplied values the responder acts on are the target prefix and its address family. The requester sends no timestamp, no sequence number, and no claim about its own identity. Anything an attacker could poison by supplying false data simply does not exist on the wire. The responder supplies its own time, from its own clock, which never moves backward. Trust is not asserted by the requester either; it is established by the SVT layer below NQDP and inherited as a single bit.

### 4.4 The Hard Work Happens in the Background

The responder never computes a diagnostic value when a request arrives. Every value — the cost, the path summary, the stability time — is computed in advance by the control plane, which watches the carrier's BGP table and updates the values whenever a route changes. These pre-computed values are injected into a table that the fast data plane reads. When a request arrives, the data plane does one table lookup and assembles the response. It reads a cached answer; it does not produce one.

This is what lets a diagnostic service run at line rate. The expensive reasoning about routes happens at BGP's pace, which is seconds to minutes, decoupled from any request. The request triggers a lookup, never a computation. An attacker cannot craft an expensive query because no query is expensive — every one costs the same single table read.

### 4.5 The Cost Is the Carrier's Own BGP Cost

NQDP does not define a cost model. The cost a responder returns is taken directly from the carrier's own BGP table. The carrier sets this cost by setting its BGP policy, exactly as it already does. A requester reading the cost is reading the carrier's real routing preference. Lower means the carrier prefers that path. The requester compares costs from different responders and routes toward the lower one. The carrier drives the requester's traffic by publishing a number it fully controls, in its own units, which reveal nothing about how the number was derived.

---

## 5. The Request Packet

The request is 24 bytes, fixed, six 32-bit words. It names a target and carries an identifier the responder will echo.

```
offset  width  field              purpose
──────────────────────────────────────────────────────────────────────
 0      64     request_id         client-chosen identifier, echoed verbatim.
 8      64     target_prefix      the address or prefix being asked about.
16       8     target_prefix_len  significant bits of target_prefix.
17       8     addr_family        0 native, 1 IPv4-compat, 2 IPv6 /64 prefix.
18      16     reserved           zero in v1.
20      32     reserved           zero in v1.
──────────────────────────────────────────────────────────────────────
total: 24 bytes
```

The `request_id` is how a requester matches a response to a request. The responder copies it back unchanged. The requester records when it sent the request and when the matching response arrived, both on its own clock, and the difference is the round-trip time. No time travels on the wire from the requester, because the responder has no reason to read it and every reason not to.

The `addr_family` tells the responder how to read `target_prefix`: as a native IPv4-64 address, as a legacy IPv4 address in the low 32 bits, or as an IPv6 /64 prefix for transit traffic. This matches the address vocabulary of [@HOWL-NET-4-2026].

There is no credential field. Whether the requester is trusted is decided by the SVT layer below NQDP, before NQDP logic runs, and is inherited as one bit.

---

## 6. The Response Packet

The response is 48 bytes, fixed, twelve 32-bit words. Every field is always present. A field that is withheld or unknown carries the all-ones sentinel.

```
offset  width  field               sentinel      meaning
──────────────────────────────────────────────────────────────────────
 0      64     request_id          —             echoed from the request.
 8      32     responder_epoch     —             responder clock at computation.
12      32     reserved            —             zero in v1.
16      32     cost                0xFFFFFFFF    BGP cost to reach target. Lower preferred.
20      32     origin_as_seen      0xFFFFFFFF    origin AS seen. Compare for hijack.
24      32     next_hop_as         0xFFFFFFFF    immediate next-hop AS.
28      32     as_path_hash        0xFFFFFFFF    plain hash of the AS_PATH.
32       8     as_path_len         0xFF          number of AS hops.
33       8     rpki_status         0xFF          0 valid, 1 invalid, 2 not-found.
34       8     reachable           0xFF          0 no, 1 yes, 2 routable, host unconfirmed.
35       8     scrubbing_active    0xFF          0 no, 1 yes. Traffic via scrubbing path.
36      32     stability_epoch     0xFFFFFFFF    time of last route change.
40      16     anycast_modulus     0xFFFF        which instance of the ring reached.
42      16     anycast_count       0xFFFF        ring size N.
44      32     reserved            —             zero in v1.
──────────────────────────────────────────────────────────────────────
total: 48 bytes
```

### 6.1 The Binding Fields

`request_id` is the echo that ties this response to the question that was asked. `responder_epoch` is the responder's clock at the instant it computed the record. It is the timestamp for the requester's time series. It is never checked against anything the requester sent, because the requester sends no time. The responder's clock is monotonic and never goes backward, which is why NQDP needs no sequence number: time alone orders the records.

### 6.2 The Routing Fields

`cost` is the carrier's BGP cost, explained in Section 4.5. `origin_as_seen` is the autonomous system the responder sees as the origin of the target's route; comparing it to the expected origin detects a hijack or route leak. `next_hop_as` is the immediate next autonomous system the responder would hand the traffic to — one hop of the path, not the path.

`as_path_hash` is a plain hash of the full AS_PATH. It is plain, not keyed, so that two responders on the same path produce the same hash. This lets an operator compare answers from two vantage points: the same hash means the same path, a different hash means the paths diverge, which reveals asymmetric routing. A changed hash across two polls from one responder means the path changed. The hash discloses that two paths are the same or different; it never discloses what the path is. `as_path_len` is the number of hops, which allows route comparison without revealing topology.

`rpki_status` reports whether the route is RPKI-valid, invalid, or not found. `reachable` reports whether the target can be reached, with a distinct value for "routable, but host existence not confirmed" so that reachability can be answered without confirming a specific host exists. `scrubbing_active` reports whether traffic to the target currently flows through a DDoS-scrubbing path, which lets an operator confirm that mitigation is in effect.

### 6.3 The Stability Field

`stability_epoch` is the responder's clock value at the last route change for the target. Subtracting it from `responder_epoch` gives how long the route has been stable. NQDP carries no flap count, because a count is a rate, and a rate cannot be known from a single snapshot. An operator polling over time watches `stability_epoch` and `as_path_hash` change and derives the flap frequency in their own time series. The protocol carries single-instant truth; rates are the requester's own discovery.

### 6.4 The Anycast Fields, Which Also Replace Ping

`anycast_modulus` is which instance of an anycast ring the requester reached. `anycast_count` is the size of the ring. Together they say "you reached instance 7 of 8."

This is also the modern replacement for ping. Reaching an instance is the confirmation that the service is alive. A target that is a single host is a ring of one: a response of "1 of 1" means you reached it, which is exactly what a successful ping confirmed. A response of "7 of 8" means you reached a live member of a larger service. The liveness confirmation is the fact that an instance answered, without the host-existence reconnaissance that ICMP Echo leaked, because you learn you reached a member of a known service, not that a specific hidden host exists.

The full ring — every instance and its cost — is never returned in one packet, because a ring of N instances is a variable-length structure and NQDP carries nothing variable. Each response describes only the one instance reached. An operator assembles the full ring picture in their time series, one row per instance as repeated polls land on different members. The time series is the ring table; the packet stays fixed.

### 6.5 Why Numbers Instead of Paths

Every field is a single number. This is the central discipline. A full AS_PATH is topology, and topology in the hands of an attacker is a map of the network. NQDP returns the diagnostic consequences of the path — its length, a hash that detects change and asymmetry, the origin and next-hop autonomous systems — without returning the path. An operator gets the answers they need for hijack detection, asymmetry detection, flap detection, and route comparison, each from a number, and the topology never leaves the responder.

---

## 7. Trust and Disclosure

### 7.1 Trust Is Inherited, Not Carried

NQDP does not authenticate anyone. The forwarding plane's SVT layer already determined whether the source of the packet is validated, and NQDP reads that result as a single bit. A requester presenting a valid SVT is trusted; one that is not is public. There is no credential in the NQDP packet and no authentication step in the NQDP logic, because both already happened below.

### 7.2 Two Audiences, Two Configurations

The carrier defines two disclosure configurations: one for SVT-trusted requesters and one for the public. Each configuration is a bitfield with one bit per response field. A set bit means "replace this field with the sentinel for this audience." The carrier can withhold any field from either audience independently. A carrier might disclose cost to the public but reveal the origin AS only to trusted peers; that is one bit in each configuration.

Both configurations are live data that the control plane can edit without recompiling anything. When a request arrives, the data plane selects the configuration by the trust bit, applies the sentinels it specifies, and emits the response. The disclosure decision is a single bitfield lookup.

### 7.3 Slam-Shut

A configuration can also be set to drop its entire audience. Under attack, a carrier sets the public configuration to drop. Public requesters then receive nothing, while SVT-trusted requesters keep receiving full answers. This is the moment pathing data is most valuable to peers, so the carrier sheds only the untrusted public and keeps answering the operators it trusts. Slam-shut is not a separate mechanism; it is the drop setting on the public configuration. There is no new state and no new code path.

### 7.4 Why There Is No Rate Limiting

A query service normally needs rate limiting because answering is expensive, and an attacker exploits that by making the responder do costly work cheaply. NQDP answering is a single table read, no more expensive than forwarding a packet. A responder built to forward at line rate can answer NQDP queries at line rate. There is no asymmetry to exploit, so there is nothing to rate-limit. The carrier expresses its intent as policy — answer fully, answer with sentinels, or drop — and serves that policy at line rate. A flood of queries is absorbed the same way a flood of data packets is absorbed, by the forwarding plane's own protections, which gate volumetric attacks before they reach the NQDP port at all.

---

## 8. The Responder Lifecycle

The responder runs only for packets on UDP 56789. Every step is fixed and completes in constant time. The data plane reads injected tables; it computes nothing expensive.

```
D1  Parse        Extract the fixed 24-byte request at fixed offsets.
D2  Validate     reserved == 0, size exact. Else silent drop.
D3  Box mode     respond, relay, or drop (Section 9).
D4  Audience     read the inherited SVT bit.
D5  Lookup       one prefix lookup into the injected bundle. Miss → all sentinels.
D6  Policy       select svt or public config; apply its sentinel bitfield;
                 if the config is set to drop this audience, stop.
D7  Assemble     copy the bundle, apply sentinels, echo request_id,
                 stamp responder_epoch from the local monotonic clock.
D8  Emit         serialize the fixed 48-byte response.
```

The data plane holds only the injected tables, the two disclosure bitfields, and its local clock. There is no connection state, no request history, no rate meter, no sequence counter. The expensive values come from the control plane, which watches the carrier's BGP table and, whenever a route changes, recomputes the affected prefix's bundle — cost taken verbatim from the BGP table, origin and next-hop autonomous systems, the path hash and length, the RPKI status, reachability, scrubbing state, and the time of the change — and injects the updated bundle into the table the data plane reads.

This is the same division of labor the forwarding plane already uses: the slow, general-purpose control plane computes and installs; the fast data plane matches and serves; the table is the contract between them. NQDP applies that established pattern to a different question.

---

## 9. Deployment

Every box can run NQDP. Each box is configured, per port, in one of three modes.

**Respond.** The box answers from its own injected table.

**Relay.** The box does not answer but forwards the query toward the next hop on the way to the target. The query follows normal routing until it reaches a box in respond mode, or, if the carrier chooses to be transparent, all the way to the destination.

**Drop.** The box refuses the query, and the requester receives nothing.

This is a basic configuration option present on all devices. A carrier deploys NQDP everywhere and decides, box by box, which ones answer, which ones pass queries along, and which ones refuse. The diagnostic table competes for memory with the forwarding tables on any box set to respond, so a carrier with tight table budgets sets most boxes to relay and concentrates responders where there is room.

Because relay forwards toward the target, a query naturally finds the box responsible for answering about that target without any extra configuration. The requester does not need to know in advance which box will answer; it addresses the target, and the network delivers the query to a responder on the path.

---

## 10. What NQDP Provides

NQDP restores the diagnostic capability that IPv4-64 removed from the forwarding plane, without restoring the attack surface that capability carried in ICMP.

It cannot be used for reconnaissance, because it reveals only the scalar facts a carrier chooses to disclose, and reaching an anycast instance confirms a service is alive without confirming a hidden host exists.

It cannot be amplified, because the request is 24 bytes and the response is 48 bytes, close to one-to-one, with no multiplier.

It cannot be used to probe a carrier's disclosure policy, because withheld and unknown fields are identical on the wire.

It cannot be flooded for advantage, because answering is a single table read at line rate, and a flood is absorbed the same way the forwarding plane absorbs any volumetric traffic.

It cannot be poisoned by attacker-supplied data, because the responder reads nothing the requester claims about itself — no time, no sequence, no identity — and supplies its own monotonic time instead.

And it gives operators the facts they actually need: reachability, cost, origin and next-hop autonomous systems, path length, path-change and asymmetry detection, RPKI validity, route stability, scrubbing confirmation, and anycast instance identity — each as a single number, each dropping directly into a time series, each disclosed only to the parties the carrier has chosen.

The diagnostic function that ICMP built into the forwarding plane, where it served friendlies and attackers alike, becomes a separate service that the carrier tunes to disclose what it wants, to whom it wants, at line rate, revealing nothing to anyone else.

---

## 11. What This Document Changes

Nothing in the companion documents changes. The forwarding plane, the IP header, the TCP and UDP headers, the security model, and the P4 implementation are unchanged. NQDP is a new application-layer service that rides over IPv4-64 UDP and inherits the SVT trust bit. It adds a diagnostic capability; it modifies no existing field, header, or forwarding behavior.

---

## Appendix A — Request Byte Map

```
byte   field
0-7    request_id          (64 bits)
8-15   target_prefix       (64 bits)
16     target_prefix_len   (8 bits)
17     addr_family         (8 bits)
18-19  reserved            (16 bits, zero in v1)
20-23  reserved            (32 bits, zero in v1)
```
Total: 24 bytes, 6 words.

## Appendix B — Response Byte Map

```
byte   field
0-7    request_id          (64 bits)
8-11   responder_epoch     (32 bits)
12-15  reserved            (32 bits, zero in v1)
16-19  cost                (32 bits)
20-23  origin_as_seen      (32 bits)
24-27  next_hop_as         (32 bits)
28-31  as_path_hash        (32 bits)
32     as_path_len         (8 bits)
33     rpki_status         (8 bits)
34     reachable           (8 bits)
35     scrubbing_active    (8 bits)
36-39  stability_epoch     (32 bits)
40-41  anycast_modulus     (16 bits)
42-43  anycast_count       (16 bits)
44-47  reserved            (32 bits, zero in v1)
```
Total: 48 bytes, 12 words.

## Appendix C — Sentinel Values

The not-available value of any field is all-ones for its width. Binding fields (`request_id`, `responder_epoch`) and reserved fields have no sentinel because they are always present and meaningful.

```
field               sentinel
cost                0xFFFFFFFF
origin_as_seen      0xFFFFFFFF
next_hop_as         0xFFFFFFFF
as_path_hash        0xFFFFFFFF
as_path_len         0xFF
rpki_status         0xFF
reachable           0xFF
scrubbing_active    0xFF
stability_epoch     0xFFFFFFFF
anycast_modulus     0xFFFF
anycast_count       0xFFFF
```

## Appendix D — Field Origin

```
field               answers the operator question
cost                which path does the carrier prefer, and how much
origin_as_seen      is this prefix being originated by the right AS (hijack)
next_hop_as         who does the carrier hand my traffic to next
as_path_hash        did the path change, and is routing asymmetric
as_path_len         how long is the path, for comparison
rpki_status         is the route cryptographically valid
reachable           can the target be reached at all
scrubbing_active    is DDoS mitigation currently in the path
stability_epoch     how long has the route been stable (flap)
anycast_modulus     which instance did I reach (and modern ping)
anycast_count       how many instances are in the ring
```

## Appendix E — Config Vocabulary

```
Per box, per NQDP port:
  mode ∈ { respond, relay, drop }

Per responder, two live bitfields:
  svt_config     one bit per response field; set = sentinel for SVT requesters
  public_config  one bit per response field; set = sentinel for public requesters
  each config also has a whole-audience drop flag

  slam-shut under attack = set public_config.drop
```

---

# HOWL-NET-5-2026 — Supporting Appendices

These appendices supply detail the main specification references but does not carry inline: the operator-problem mapping that drove the field set, the full data-plane and control-plane contract, the time-series behavior that fields depend on, the attack-surface accounting, and the connections to the four prior documents. Nothing here restates the packet layout or the lifecycle from the main document; it carries the material those depend on.

---

## Appendix F — Operator Problem → Field Mapping

Each real diagnostic need, the tool operators use today, what that tool leaks, and the NQDP field that answers the same need without the leak.

| Operator need | Today's tool | What today's tool leaks or costs | NQDP field | How NQDP avoids the cost |
|---|---|---|---|---|
| Is the target alive | ICMP Echo (ping) | Confirms host existence to anyone; enables OS fingerprinting | `anycast_modulus` / `anycast_count` | Confirms a service instance answered, not that a hidden host exists |
| What path does traffic take | traceroute | Reveals every hop; shares channel with production | `as_path_hash`, `as_path_len`, `next_hop_as` | Returns path consequences as numbers, never the hop list |
| Is this route a hijack | external looking glass, RPKI lookup | Looking glasses are scraped HTML, no clean API | `origin_as_seen`, `rpki_status` | Machine-readable scalar, one fixed response |
| Is routing asymmetric | traceroute from both ends, manual compare | Requires access to both source nodes | `as_path_hash` from two vantages | Same hash = same path; compared in the requester's series |
| Is the route flapping | BGP monitoring (BMP), route collectors | Firehose to a trusted collector; heavy infrastructure | `stability_epoch` over polls | Single-instant stability time; rate derived in the series |
| Which carrier path is better | BGP cost, hidden inside the AS | Not externally visible at all | `cost` | Carrier's own BGP cost, published as one opaque scalar |
| Who gets my traffic next | BGP table access | Requires the source's BGP table | `next_hop_as` | One AS number, no table access needed |
| Is DDoS mitigation active | manual confirmation with provider | No in-band signal | `scrubbing_active` | One bit the carrier chooses to expose |
| Which anycast instance answered | no standard tool | Anycast is opaque by design | `anycast_modulus` / `anycast_count` | Position-in-ring as a modulus, no instance location |

The mapping shows the field set is not invented. It is the enumerated set of facts operators already extract, by harder means, from looking glasses, BMP collectors, traceroute, and direct BGP access. NQDP collapses that scattered, leak-prone, access-dependent set into one fixed query answered by numbers.

---

## Appendix G — NQDP Lifecycle vs Forwarding-Plane Lifecycle

NQDP reuses the seven-phase shape of the forwarding plane deliberately, so an implementer already fluent in [@HOWL-NET-3-2026] reads NQDP as the same pattern pointed at a different question.

| Forwarding phase (NET-3) | NQDP phase (NET-5) | Shared property |
|---|---|---|
| Parse (fixed offsets) | D1 Parse (fixed 24 bytes) | No variable-length parsing |
| Validate (strict drop) | D2 Validate (reserved, size) | Any failure → silent drop |
| Authenticate (SVT/cookie/token) | D4 Audience (inherit SVT bit) | SVT is the trust root; NQDP reuses it, does not recompute |
| Classify (connection/threat/firewall) | D6 Policy (disclosure bitfield) | A table/config decides treatment at a fixed key |
| Route (LPM on dst_addr) | D5 Lookup (LPM on target_prefix) | One longest-prefix match on a 64-bit key |
| Transform (stamp, meter, track) | D7 Assemble (sentinel, echo, stamp) | Fixed-field write, O(1) |
| Emit (fixed length) | D8 Emit (fixed 48 bytes) | Fixed-length serialize, no padding math |

The one phase NQDP adds and the forwarding plane lacks is D3 Box mode (respond/relay/drop), because a forwarding node always forwards, whereas an NQDP node chooses whether to answer. The one phase the forwarding plane has that NQDP lacks a per-request version of is Authenticate: NQDP does no cryptographic work per request because the SVT check already happened in the forwarding plane that carried the packet to the NQDP port.

---

## Appendix H — Data-Plane / Control-Plane Contract

The table is the contract. The control plane writes; the data plane reads. This appendix lists every shared structure, who writes it, who reads it, and at what rate.

| Structure | Written by | Written at rate | Read by | Read at rate |
|---|---|---|---|---|
| `nqdp_prefix` (the bundle table) | nqdp_bgp_sync | per BGP route change (sec–min) | D5 Lookup | per request (line rate) |
| anycast modulus (this box's position) | nqdp_anycast | once per served prefix | D5 Lookup | per request |
| anycast count (ring size) | nqdp_anycast | per ring membership change | D5 Lookup | per request |
| `svt_config` bitfield | nqdp_disclosure | per policy edit (rare) | D6 Policy | per request |
| `public_config` bitfield | nqdp_disclosure | per policy edit; set-to-drop under attack | D6 Policy | per request |
| per-port mode (respond/relay/drop) | nqdp_mode | per operator config | D3 Box mode | per request |
| local monotonic clock | hardware | continuous | D7 Assemble (responder_epoch) | per request |
| `response_seq` | — | — | — | — (removed; time replaces it) |

The read side is always per-request and constant-time. The write side is always slow and asynchronous. No structure is both written and read on the per-request path, which is why there is no per-request contention and no per-request computation.

---

## Appendix I — The Bundle Injected Per Prefix

The control plane assembles one bundle per prefix and injects it into `nqdp_prefix`. This is the full set of values a single lookup returns, their source, and how often the control plane refreshes each.

| Bundle value | Source | Refreshed when |
|---|---|---|
| cost | carrier BGP RIB, verbatim | the prefix's BGP best-path cost changes |
| origin_as_seen | BGP AS_PATH origin | best path changes |
| next_hop_as | BGP AS_PATH first hop | best path changes |
| as_path_hash | plain hash over BGP AS_PATH | AS_PATH changes |
| as_path_len | BGP AS_PATH length | AS_PATH changes |
| rpki_status | RPKI validator | validation state changes |
| reachable | presence of a usable best path | reachability changes |
| scrubbing_active | mitigation/steering state | scrubbing engaged or disengaged |
| stability_epoch | set to responder clock at each change | any best-path change |
| anycast_modulus | this box's fixed ring position | box joins/leaves the ring |
| anycast_count | ring membership size | membership changes |

A miss on the `nqdp_prefix` lookup — a target the control plane has not populated — returns all sentinels. An unknown target is indistinguishable from a fully-squelched one, consistent with Rule 4.

---

## Appendix J — Time-Series Behavior of Each Field

NQDP returns single-instant truth. Every rate, trend, and change is the requester's own derivation across stored rows. This appendix states what each field yields as a time series and the three-state read every field supports.

Every field has three distinct conditions in the series, none ambiguous:

| Condition | On the wire | Meaning in the series |
|---|---|---|
| real value | a legitimate value | the fact at that instant |
| sentinel | all-ones | not available (withheld or unknown — indistinguishable) |
| no row | no response arrived | the responder dropped, relayed with no answer, or was unreachable |

Per-field series derivations:

| Field | Single-row use | Across-row derivation |
|---|---|---|
| cost | pick lowest among responders | rising cost = drain or congestion; carrier steering |
| origin_as_seen | compare to expected origin | a change = possible hijack onset, timestamped |
| next_hop_as | who handles traffic now | a change = peering or path shift |
| as_path_hash | compare two vantages for asymmetry | a change = path changed; frequency of change = instability |
| as_path_len | compare route lengths | lengthening = detour, possible leak |
| rpki_status | trust the route or not | valid→invalid transition = hijack or ROA problem |
| reachable | reachable now or not | yes→no transition = outage onset, timestamped |
| scrubbing_active | mitigation in path now | off→on = attack detected and mitigated |
| stability_epoch | time stable = epoch − stability_epoch | repeated changes = flap frequency (the removed flap_count) |
| anycast_modulus | which instance now | changing across polls = instance flapping |
| anycast_count | ring size now | shrinking = instances withdrawn, possible outage |

The flap count removed from the packet (Section 6.3) reappears here as a derivation: the requester counts how often `stability_epoch` or `as_path_hash` changes per unit of its own wall-clock. The protocol carries the instant; the series carries the rate.

---

## Appendix K — Attack-Surface Accounting

Every attack NQDP must resist, the mechanism that resists it, and where that mechanism lives.

| Attack | NQDP resistance | Mechanism location |
|---|---|---|
| Reconnaissance (host existence) | reaching an instance ≠ confirming a hidden host; only chosen scalars disclosed | field design + disclosure config |
| OS fingerprinting | no response varies by host stack; one fixed record from a table | fixed response + injected bundle |
| Amplification | request 24 B, response 48 B, ~1:1, no multiplier | packet sizing |
| Resource exhaustion | answering is one table read at line rate | two-sided design (Appendix H) |
| Policy probing | withheld and unknown both = sentinel | sentinel rule |
| Flooding for advantage | flood absorbed as ordinary UDP by the forwarding plane | inherited forwarding-plane protection |
| Spoofed-source queries | SVT invalid → public audience; cannot gain trusted disclosure | inherited SVT (NET-1/NET-2) |
| Poisoning via client data | responder reads no client time, sequence, or identity | Rule 8 |
| Replay / mismatched answers | request_id echoed verbatim; requester matches on equality | identifier rule |
| Clock manipulation | responder supplies own monotonic time; never reads client time | Rule 8 + monotonic clock |
| Parser differential | fixed offsets, no options, one shape | Rules 1–2 |

The table shows NQDP's own additions resist the diagnostic-specific attacks (reconnaissance, probing, poisoning, replay), while the volumetric attacks (flooding, spoofing, exhaustion) are resisted by inheriting the forwarding plane's existing protections. NQDP does not re-implement DDoS defense; it rides on the one already built.

---

## Appendix L — What NQDP Keeps, Drops, and Replaces from ICMP

Each ICMP function, and its disposition under IPv4-64 plus NQDP.

| ICMP function | Disposition | Where it goes |
|---|---|---|
| Echo Request/Reply (ping) | Replaced | `anycast_modulus`/`count` — reaching an instance is liveness |
| Time Exceeded (traceroute) | Dropped from forwarding; replaced at query level | `as_path_len` / `as_path_hash` give path facts without hop exposure |
| Destination Unreachable | Dropped | silent drop in forwarding; `reachable` field answers on authenticated request |
| Port Unreachable | Dropped | silent drop; no service probing surface |
| Redirect | Dropped | routing is control-plane only; no in-band redirect |
| Source Quench (deprecated) | Not carried | ECN in the IP header handles congestion signaling |
| Parameter Problem | Dropped | strict drop; malformed packets vanish silently |
| Fragmentation Needed (PMTUD) | Partially addressed | transit fragmentation (NET-1) reduces need; no ICMP black-hole dependence |

The pattern: ICMP's error-signaling functions are dropped entirely because the forwarding plane reveals nothing, and ICMP's diagnostic functions are replaced by NQDP queries that answer the same operational question under carrier-controlled disclosure. The two roles ICMP fused — silent-drop error behavior and answer-anyone diagnostics — are cleanly separated: errors become silence, diagnostics become authenticated queries.

---

## Appendix M — Connection to the Series Invariants

NQDP is the same design philosophy as the forwarding plane, applied one layer up. This appendix maps each series invariant to its NQDP expression.

| Series invariant | Forwarding-plane form | NQDP form |
|---|---|---|
| Fixed size, no variable length | 36-byte header, fixed TCP/UDP | 24-byte request, 48-byte response |
| Worst case = best case | constant pipeline depth | one table read per query, always |
| Reveal nothing | strict silent drop | sentinels + disclosure config |
| Commensurate cost (parity) | expensive action gated behind proven spend | answering costs a table read, no amplification |
| Trust is bilateral and physical | SVT via meet-me-room secrets | SVT bit inherited; same trust root |
| Slow plane computes, fast plane serves | BGP injects routes, P4 forwards | control plane injects bundles, data plane answers |
| No interpretation of hostile input | fixed-offset reads, no parsing | responder reads no client claim about itself |
| Degrade without going dark | graceful drain via cost | slam-shut sheds public, keeps peers |

The through-line: NQDP does not introduce a new security model, a new trust root, or a new performance model. It inherits all three from the forwarding plane and expresses them in the diagnostic layer. The reason the diagnostic service can be as safe and as fast as the forwarding plane is that it is built from the same parts.

---

## Appendix N — Open Deployment Constants

Values a carrier sets at deployment. None affects the wire layout; all are local policy.

| Constant | Set by | Consideration |
|---|---|---|
| UDP port | fixed at 56789 | unregistered, uncommon; carriers may override by agreement |
| as_path_hash function | carrier, consistent across responders | plain, non-cryptographic; must match across boxes for cross-vantage comparison |
| responder_epoch resolution | carrier | 32-bit; choose seconds or finer against the rollover horizon |
| staleness horizon | requester | how old a cached `responder_epoch` may be before re-polling |
| flap window | requester | wall-clock window over which `stability_epoch` changes are counted |
| per-box mode defaults | carrier | respond where table memory allows, relay elsewhere, drop at untrusted edges |
| disclosure bitfield defaults | carrier | which fields public sees; which SVT-only; drop flag for slam-shut |
| responder placement | carrier | respond-mode boxes need bundle-table memory alongside forwarding tables |
