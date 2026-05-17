**Email (SMTP/IMAP/POP3)**

Inbound SMTP: a processor runner listens on port 25. A clone spawns per connection, speaks the SMTP grammar — HELO, MAIL FROM, RCPT TO, DATA, QUIT are a fixed protocol with exact syntax, perfect for a grammar template. The clone parses the envelope, extracts headers and body, asserts the message as facts in the recipient's email KB at root.users.jane.email.inbox. From, To, Subject, Date, Body, Attachments — all facts with provenance showing received timestamp and source IP. The clone dies. Zero LLM prose generation. Pure grammar-driven protocol handling.

Outbound SMTP: a user's application clone composes a message by asserting facts — to, subject, body — into an outbox queue. A processor runner pops from the outbox, opens a connection to the destination MX through a granted network primitive, speaks the SMTP grammar outbound, delivers the message, asserts a delivery receipt fact. The entire SMTP conversation is a grammar template with content slots filled from KB facts.

IMAP4: a processor runner listens on port 143. A clone per connection authenticates the user — credential check against their user KB, grants loaded from their scope chain. The IMAP grammar handles SELECT, FETCH, STORE, SEARCH, COPY. Each command maps to a Prolog rule: FETCH 1:* pulls facts from the user's inbox KB, formats them using the IMAP response grammar, sends them down the socket. STORE sets flags — read, flagged, deleted — as fact modifications on the message KB. SEARCH is a Prolog query against message facts. The entire protocol is templated. The LLM never generates prose — it fills content slots in protocol grammars.

POP3: simpler than IMAP. Same pattern. Grammar-driven protocol. LIST queries message facts, RETR fetches message content from KB, DELE marks for deletion. A polling runner handles actual deletion after the session closes — checking DELE flags and retracting message facts.

---

**Web (HTTP/HTTPS)**

A processor runner listens on port 80/443. Each request spawns a clone. The HTTP request grammar parses method, path, headers, and body into facts. A Prolog rule routes the request based on path — route("/api/users", handle_users), route("/api/orders", handle_orders). Each handler is a Prolog rule chain that queries KBs, processes data, and fills an HTTP response grammar — status code, headers, body. HTML responses use page grammars with content slots. JSON API responses use JSON grammars. Static file requests resolve to file facts and serve content through granted file read primitives.

HTTPS is the same with TLS handshake handled by a granted network primitive. The certificate and key are facts in a security KB with owner-only visibility.

Session management: HTTP cookies map to session clone IDs. A Set-Cookie header carries the session KB path. Subsequent requests from the same client route to the same clone or spawn a clone that mounts the session KB. Session expiration is a counter — increment per request, kill when idle counter exceeds timeout threshold.

WebSockets: a processor runner upgrades the HTTP connection and maintains it. Each frame is parsed by the WebSocket grammar — opcode, payload length, masking key, payload. Inbound messages become facts. Outbound messages are grammar-filled frames pushed through the socket. Ping/pong is automatic — a Prolog rule responds to ping frames with pong frames using the same payload.

---

**DNS**

A processor runner listens on port 53 UDP and TCP. The DNS wire format is a binary grammar — header with ID, flags, counts, then question/answer/authority/additional sections. Each query spawns a lightweight handler. The handler parses the question — QNAME, QTYPE, QCLASS — into facts. A Prolog rule looks up the answer in the zone KB at root.services.dns.zones.example_com. Zone records are facts: a_record("www", "192.168.1.1"), mx_record("@", 10, "mail.example.com"), cname_record("blog", "www"). The response grammar fills the answer section from matching facts. TTL values are VDR integers. Serial numbers for zone transfers are counters.

Recursive resolution: if the zone KB doesn't have the answer, a forwarding rule sends the query upstream through a granted network primitive, caches the response in an LRU with TTL-based expiration, and returns it. The LRU is the DNS cache. Expiration is a counter comparison — current time minus cache timestamp versus TTL.

---

**FTP/SFTP**

A processor runner listens on port 21 (FTP) or 22 (SFTP). Clone per connection, authenticated against user KB. The FTP command grammar handles USER, PASS, CWD, LIST, RETR, STOR, DELE, MKD, RMD. Each command maps to a Prolog rule that invokes granted filesystem primitives. LIST calls list_dir, fills the directory listing grammar. RETR calls file_read and streams content. STOR calls file_write. CWD changes the active path — a working data binding in the session.

The grant system provides file-level access control. A user's FTP grants specify which paths they can read and write. RETR on a file outside their granted path returns permission denied. No application-level ACL code — the grant check is in the primitive layer.

SFTP over SSH adds the SSH handshake and channel management through granted network primitives. The file operations are identical.

---

**IRC**

A processor runner connects to an IRC server through a granted network primitive. The IRC protocol grammar handles NICK, USER, JOIN, PART, PRIVMSG, NOTICE, PING, PONG, MODE, KICK, TOPIC. Each message is a single line with a well-defined format — colon-prefix for source, command, parameters. Perfect for a grammar template.

Inbound messages become facts in channel KBs. root.services.irc.channels.general holds message facts with sender, timestamp, and content. A PRIVMSG to the bot triggers a clone that processes the message — queries against KB state, evaluates Prolog rules, fills a response template, sends a PRIVMSG back. The response grammar ensures IRC protocol compliance — line length limits, proper formatting, correct prefix.

Channel management is Prolog rules. Auto-join on connect. Auto-respond to specific patterns. Moderation rules — if a user exceeds message rate (counter comparison), trigger a mute (MODE command via grammar). Topic updates from KB facts. The entire IRC bot is an LM Software application — developed interactively, snapshot, deployed as a processor runner maintaining the IRC connection.

---

**XMPP/Jabber**

XML-based protocol. The XMPP grammar handles stream negotiation, SASL authentication, stanza types — message, presence, iq. Each stanza is parsed by the XML grammar into facts. Outbound stanzas are grammar-filled XML. Presence management is a set of facts — available, away, do-not-disturb — that update based on user KB state. Message routing uses the same inbox queue pattern as email — messages land as facts in user KBs, clients fetch them via iq stanzas.

Multi-user chat rooms are channel KBs, same as IRC but with XML framing. Room configuration is constraints on the room KB — members-only, moderated, persistent. The XEP extensions — file transfer, message receipts, chat state notifications — are additional grammar templates that activate when the corresponding feature fact is present in the session KB.

---

**Matrix Protocol**

HTTP-based federation protocol. Each Matrix event is a JSON object with a well-defined schema. The JSON grammar parses and generates events. Room state is a KB — membership events are facts, message events are facts with provenance, state events are facts that shadow previous state. The DAG structure of Matrix events maps naturally to the KB tree — each event references parent events through connection facts.

Federation: a processor runner handles inbound federation requests on port 8448. Each request is an HTTP transaction with a signed JSON body. Signature verification uses exact VDR arithmetic on the Ed25519 operations through granted cryptographic primitives. The signing key is a fact in the server's security KB with owner-only visibility.

End-to-end encryption: Olm/Megolm session management is facts in user KBs. Key exchange events are parsed and processed through granted cryptographic primitives. The encrypted message payload is opaque bytes that pass through the system without interpretation — only the recipient's clone has the grants and keys to decrypt.

---

**Twitter/X API**

A processor runner polls the Twitter API through granted network primitives. Timeline fetches land as facts in the user's social KB — tweet ID, author, content, timestamp, engagement metrics. Each metric is a VDR fraction — engagement rate is likes/impressions, exact, not float.

Posting: the user's application clone composes a tweet by asserting a fact to the outbox queue. A processor runner pops from the queue, formats the tweet using the Twitter API grammar, sends it through a granted network POST, records the response tweet ID and timestamp as provenance facts.

DMs are inbox/outbox queues on user KBs. Inbound DMs from the API poller land as facts. Outbound DMs are queue items that the processor sends. The UI — whether web or native — queries the user's DM KB and renders from a template grammar. The LLM never generates the DM content unless asked — it just moves data from KB addresses to grammar templates.

Timeline algorithms: Prolog rules score and rank timeline items. Relevance is computed from engagement metrics (VDR fractions), recency (timestamp comparison), relationship strength (connection facts between user KBs). The ranking is exact — no float sort instability. The user can inspect and modify the ranking rules. "Show me more from accounts I reply to" is a rule modification, not an opaque algorithm.

---

**Reddit API**

Same pattern as Twitter. Subreddits are KBs. Posts are facts with score, comments, author, timestamp. Comments are child facts with parent references. Voting is a counter operation. Moderation rules are Prolog — automod as queryable rules instead of regex config files. Karma is a counter per user. Post filtering and ranking use the same Prolog-based scoring as the Twitter timeline.

---

**Discord**

WebSocket-based. A processor runner maintains the WebSocket connection to Discord's gateway. The gateway events — MESSAGE_CREATE, GUILD_MEMBER_ADD, PRESENCE_UPDATE — are parsed by a JSON grammar into facts. Each guild is a KB. Each channel is a child KB. Messages are facts with author, content, timestamp, attachments.

Bot commands use Prolog pattern matching. A message starting with "!help" matches a rule that queries the command registry KB and fills a response template. Slash commands are registered through the Discord API using granted network primitives and handled by the same rule-matching system.

Voice state tracking is facts — user X is in voice channel Y since timestamp Z. A Prolog rule can implement "if user is in voice channel for more than 2 hours, send a reminder" using counter comparison.

---

**Slack**

HTTP-based event API plus WebSocket for real-time. Events come in as JSON. Each workspace is a KB. Channels are child KBs. Messages are facts. Threads are child KBs of the message KB. Reactions are counter-like facts — emoji, user, timestamp.

Slack blocks — the structured message format — are a perfect grammar case. The block grammar fills section blocks, action blocks, context blocks from KB data. Interactive components — buttons, menus, date pickers — trigger HTTP callbacks that spawn clones to handle the interaction. Each interaction is a Prolog rule evaluation: button "approve" on message M triggers rule approve_request(M) which updates the request KB and sends a confirmation block back.

Workflow Builder replacement: the entire Slack workflow is Prolog rules operating on channel and user KBs, triggered by message events or schedule timers.

---

**ActivityPub/Mastodon**

Federation protocol based on HTTP signatures and JSON-LD. Each actor is a KB with inbox and outbox queues. A Create activity is a JSON object parsed by the ActivityPub grammar. Inbound activities arrive at the actor's inbox endpoint — a processor runner handles the HTTP POST, verifies the HTTP signature through granted cryptographic primitives, parses the activity, asserts the object as a fact in the actor's timeline KB.

Outbound activities: asserting a post to the outbox queue triggers a processor that formats the Create activity using the ActivityPub grammar, signs it, and POSTs it to each follower's inbox through granted network primitives. The follower list is a set of connection facts.

Content addressing: each object has a globally unique ID (the URL). The KB stores objects by their ID as the fact key. Fetching a remote object is a granted network GET followed by compaction into a local fact.

---

**CalDAV/CardDAV**

WebDAV-based protocols for calendars and contacts. The XML grammar handles PROPFIND, REPORT, PUT, DELETE. Calendar events are iCalendar format — another grammar. Each event becomes a KB fact with start time, end time, summary, location, recurrence rules, attendees.

Recurrence rules are Prolog: recurring(Event, daily, until(Date)) generates occurrence facts for each date. A query for "events this week" evaluates recurrence rules and returns both one-time and recurring events. Conflict detection is a Prolog rule that checks for overlapping time ranges using VDR fraction comparison on timestamps.

Free/busy queries: a Prolog query across the user's calendar KB collecting all event time ranges and returning the complement. Shared calendars are mounted KBs — mount a colleague's calendar read-only to see their availability without seeing event details.

Contacts (CardDAV): each contact is a KB fact with name, email, phone, address fields. vCard format is a grammar. Search is Prolog query — find contacts matching partial name, company, or tag.

---

**LDAP**

A processor runner listens on port 389. The LDAP protocol is a binary format (BER/DER encoded ASN.1) parsed by a binary grammar. BIND authenticates against user KBs. SEARCH queries the directory tree — which maps directly to the KB tree. An LDAP DN like "cn=Jane Doe,ou=Engineering,dc=acme,dc=com" maps to root.org.acme.engineering.users.jane_doe. SEARCH with a filter like "(objectClass=person)" is a Prolog query across the subtree.

ADD, MODIFY, DELETE operations map to kb_assert, fact modification, and kb_retract. Schema enforcement is constraints on the directory KB — required attributes, allowed object classes, syntax validation. All existing LDAP-aware applications — email clients, VPN authenticators, SSH key lookups — work against this service without modification.

---

**MQTT**

Lightweight pub/sub for IoT. A processor runner listens on port 1883. The MQTT packet grammar handles CONNECT, PUBLISH, SUBSCRIBE, UNSUBSCRIBE, PINGREQ/PINGRESP. Each topic is a KB path — mqtt/sensors/building_a/floor_3/temperature maps to root.services.mqtt.sensors.building_a.floor_3.temperature.

PUBLISH writes a fact to the topic KB with the payload and QoS level. SUBSCRIBE registers a connection fact between the subscriber's session KB and the topic KB. When a PUBLISH arrives, a Prolog rule finds all subscribers through connection queries and pushes the message to each subscriber's outbound queue. QoS 1 (at least once) uses a counter for message acknowledgment. QoS 2 (exactly once) uses a two-phase commit pattern with locks.

Retained messages are persistent facts on the topic KB. Last Will messages are facts on the client's session KB that fire on disconnect through a Prolog rule.

---

**gRPC**

HTTP/2 based RPC. The protobuf schema compiles to a grammar — each message type is a grammar template with typed fields. Service definitions become Prolog rules mapping RPC method names to handler logic. Streaming RPCs use the queue pattern — server streaming pushes items to an outbound queue that the HTTP/2 framing drains. Client streaming pops items from an inbound queue as frames arrive. Bidirectional streaming uses both queues simultaneously.

Protobuf field types map to VDR types — int32 is an i32 fact, double becomes a VDR fraction at the boundary with the conversion logged, string is an interned string ID, bytes is a raw buffer. Repeated fields are list facts. Nested messages are child KB facts.

---

**GraphQL**

An HTTP endpoint where the request body contains a GraphQL query. The GraphQL grammar parses queries, mutations, and subscriptions into an AST represented as KB facts. Each field resolution is a Prolog rule: resolve(type, field, Args, Result). The schema is a KB of type definitions — each type is a KB, each field is a fact with type, arguments, and resolver rule reference.

Nested resolution is natural — Prolog resolves fields recursively, each level querying the appropriate KB. N+1 query problems are addressed by batching — a Prolog rule collects all IDs at one level and issues a single batch query before resolving children.

Subscriptions use the queue pattern. A mutation that changes data pushes a notification to subscriber queues. A WebSocket handler pops from the queue and sends the update using the GraphQL response grammar.

---

**SSH**

A processor runner listens on port 22. The SSH transport grammar handles key exchange, authentication, channel management. Public key authentication checks the user's authorized_keys facts in their user KB. Password authentication checks against credential facts.

Shell sessions: a clone per connection provides a command-line interface. Commands are parsed by a shell grammar and matched against Prolog rules. The user types a command, the clone evaluates it — ls maps to list_dir, cat maps to file_read, custom commands map to whatever Prolog rules the user has at their scope. The output is formatted by a terminal grammar.

SCP/SFTP subsystems: same file operation primitives as FTP, negotiated through the SSH channel layer.

Port forwarding: TCP connections tunneled through SSH channels. The SSH clone acts as a proxy — accepting a connection on the forwarded port, wrapping traffic in SSH channel frames, unwrapping at the other end. The forwarding authorization is a grant on the user's session.

---

**Telnet**

The simplest case. A processor runner listens on port 23. Raw TCP with optional TELNET negotiation (WILL/WONT/DO/DONT for echo, line mode, terminal type). A clone per connection presents a text interface. Input lines are parsed by a command grammar. Output is a text template. The entire MUD/BBS/text-adventure genre is an LM Software application — rooms are KBs, items are facts, movement is scope change, inventory is a list on the player's session KB, combat is Prolog rule evaluation with VDR arithmetic.

---

**NTP**

A processor runner listens on port 123 UDP. The NTP packet is a 48-byte binary grammar — leap indicator, version, mode, stratum, poll interval, precision, timestamps. The server's reference clock is a fact updated by a hardware clock primitive. Client requests get a response with the server's timestamps filled into the grammar. All timestamps are exact integers — NTP uses 64-bit fixed-point with the integer part in seconds since 1900. VDR represents this losslessly.

---

**DHCP**

A processor runner listens on port 67 UDP. The DHCP packet grammar handles DISCOVER, OFFER, REQUEST, ACK. The IP address pool is a KB of available addresses — each address is a fact, leased addresses have a lease fact with expiration timestamp and client MAC. DISCOVER triggers a Prolog rule that finds an unleased address. OFFER reserves it with a lock. REQUEST confirms the lease — lock released, lease fact asserted. Lease expiration is a counter comparison against current time; a polling runner reclaims expired leases.

---

**RADIUS/TACACS+**

Authentication, authorization, and accounting for network devices. A processor runner listens on port 1812 (auth) and 1813 (accounting). The RADIUS packet grammar handles Access-Request, Access-Accept, Access-Reject, Accounting-Request. User authentication checks credential facts in user KBs. Authorization checks grants — what network segments, what privilege levels. Accounting-Request messages become facts in the user's session KB with timestamps, bytes transferred, session duration as VDR fractions.

---

**SIP/RTP (VoIP)**

SIP: a processor runner listens on port 5060. The SIP grammar handles INVITE, ACK, BYE, REGISTER, OPTIONS. Each call is a session KB with caller, callee, codec negotiation facts, and call state as a finite state machine encoded in Prolog rules — idle to ringing to connected to terminated. SDP (Session Description Protocol) within SIP is a nested grammar with media type, codec, and port facts.

RTP: media streams are raw UDP. A processor runner handles RTP packets — the 12-byte header grammar extracts sequence number, timestamp, SSRC. The audio/video payload passes through without LLM involvement. Jitter buffer is a ring buffer. Packet loss detection is a bitset tracking received sequence numbers. RTCP statistics — jitter, round-trip time, packet loss fraction — are VDR fractions.

---

**SNMP**

A processor runner listens on port 161 UDP. The SNMP packet is BER-encoded ASN.1 — a binary grammar. GET, SET, GETNEXT, GETBULK requests map to KB queries. The MIB (Management Information Base) maps directly to a KB tree — each OID is a path, each value is a fact. OID 1.3.6.1.2.1.1.1 (sysDescr) is a fact at root.services.snmp.mib.system.sysDescr. SNMP walks are scope walks. SET operations are fact assertions with grant checks. TRAP/INFORM notifications are queue pushes that a trap receiver runner processes.

---

**Syslog**

A processor runner listens on port 514 UDP (or 6514 TCP with TLS). The syslog message grammar — RFC 5424 format: priority, version, timestamp, hostname, app-name, procid, msgid, structured data, message. Each message becomes a fact in the source host's log KB. Structured data elements parse into additional facts. Severity is an integer 0-7. Facility is an integer 0-23.

Log analysis rules fire on incoming messages. "If facility=local0 and severity<=3 and message contains 'disk', push to storage_alerts queue." A Prolog rule operating on log facts. Aggregation is counter operations — errors per hour per host. Correlation is Prolog queries across host log KBs — "which hosts reported disk errors within 5 minutes of each other?"

---

**Prometheus/OpenMetrics**

A processor runner serves the /metrics endpoint on port 9090. Each metric is a fact — name, type (counter/gauge/histogram/summary), labels as KB path components, value as VDR fraction. A scrape request triggers a Prolog query that collects all metric facts and fills the OpenMetrics text grammar — metric name, labels in braces, value, timestamp.

Alerting rules are Prolog: alert(high_cpu) :- metric(cpu_usage, Host, Value), Value > 80/100. The alert evaluates exactly — 80/100 is exact, the comparison is exact, the alert either fires or doesn't. No float threshold ambiguity.

---

**SMTP-based Mailing Lists**

A processor runner handles list-addressed email. Inbound message arrives via SMTP, clone matches the recipient against list KBs — root.services.lists.dev_team. The clone checks the sender against the subscriber list (fact lookup), applies moderation rules (Prolog — if sender is not subscribed and list is members-only, push to moderation queue), adds list headers using the email header grammar, and redistributes to all subscribers by pushing to each subscriber's inbox queue. Bounce handling is a Prolog rule that checks bounced addresses against subscriber facts and increments a bounce counter — after N bounces, unsubscribe.

---

**RSS/Atom Feed Generation**

An HTTP endpoint serving XML. The Atom grammar fills the feed envelope — title, updated, author, id — from the blog/news KB facts. Each entry is a recent content fact formatted into the entry grammar — title, link, published, summary, content. A Prolog rule selects the most recent N entries by timestamp comparison. Conditional GET support: the ETag header is a checksum of the feed's fact set, computed by a Prolog rule. If-None-Match comparison returns 304 Not Modified when the feed hasn't changed. Zero LLM tokens for the entire feed generation — it's purely grammar-driven from KB facts.

---

**WebDAV**

HTTP extension for collaborative authoring. The WebDAV grammar handles PROPFIND, PROPPATCH, MKCOL, COPY, MOVE, LOCK, UNLOCK. Each resource is a KB. Properties are facts. Collections are parent KBs with children. LOCK uses the lock primitive — acquire the lock on the resource KB, record the lock token as a fact, release on UNLOCK or timeout. COPY is clone. MOVE is clone plus retract original. Dead properties (arbitrary XML) are stored as facts with the property namespace and name as the key.

---

**OAuth 2.0 / OpenID Connect**

The authorization server is an LM Software application. Authorization endpoint: an HTTP handler that presents a consent grammar template, validates the client_id against registered client facts, generates an authorization code as a random integer stored as a temporary fact with expiration. Token endpoint: exchanges the code for an access token — another integer, stored as a fact on the user's session KB with scope facts listing permitted operations. Token validation: any service receiving a token queries the authorization server's token KB by token value, gets back the scope facts. Refresh tokens are longer-lived facts with rotation — each use retracts the old token and asserts a new one. Grant state transitions are monotonic — issued, used, revoked, never un-revoked.

---

**LDAP-backed SSO**

Combines LDAP directory with SAML or OIDC. The identity provider is an LM Software application. User authenticates via the LDAP service. The IdP clone generates a SAML assertion or OIDC id_token — both are grammar-templated XML or JWT with claims filled from user KB facts. Service providers validate the assertion by checking the signature (granted cryptographic primitive) and extracting claims. Each claim maps to a user KB fact — email, groups, roles. Group membership drives grant inheritance — user in group "engineering" inherits engineering branch grants.

---

**S3-Compatible Object Storage**

An HTTP endpoint implementing the S3 REST API. PUT creates a KB for the object with the content stored via a granted filesystem primitive and metadata as facts — content-type, content-length, ETag (checksum). GET retrieves the content and fills HTTP headers from metadata facts. LIST on a bucket is a Prolog query across child KBs matching the prefix parameter. Multipart upload uses a temporary KB per upload with part facts — each part is a separate file, CompleteMultipartUpload merges parts and retracts the temporary KB. Versioning: each PUT creates a new version KB as a sibling, version ID is the KB's integer ID.

ACLs: bucket and object ACLs are grant facts. Cross-account access is a mount with grants. Pre-signed URLs are temporary facts with expiration — a token in the URL maps to a fact that authorizes one GET/PUT within the time window.

---

**Redis-Compatible Cache**

A processor runner listens on port 6379. The RESP protocol grammar handles the wire format — simple strings, errors, integers, bulk strings, arrays. GET maps to a fact lookup in the cache KB. SET maps to a fact assertion with optional TTL as a counter. DEL retracts the fact. EXPIRE sets a TTL counter on the fact. A polling runner checks TTL counters and retracts expired facts.

Lists are queue primitives. Sets are set primitives on the KB. Sorted sets use facts with score as VDR fraction — ZRANGEBYSCORE is a Prolog query with VDR fraction comparison. Pub/sub uses queue-based channels — SUBSCRIBE registers a connection, PUBLISH pushes to all subscriber queues.

The advantage over actual Redis: every operation has provenance. Every key has an audit trail. TTL expiration is exact integer comparison, not float timer approximation. Sorted set scores are exact fractions, not doubles.

---

**Kafka-Compatible Message Streaming**

A processor runner handles the Kafka wire protocol. Topics are KBs. Partitions are child KBs. Each message is a fact with offset (counter, monotonically incrementing), key, value, timestamp. Producers append facts — the offset counter auto-increments, never reuses. Consumers track their position via a consumer group KB with offset facts per partition.

Fetch requests: a Prolog rule collects facts with offset >= consumer's committed offset, up to the fetch limit. Commit: update the consumer's offset fact. Consumer group rebalancing: Prolog rules assign partitions to consumers based on group membership facts and the partition count.

Retention: a polling runner checks message timestamps against retention policy (a constraint on the topic KB). Messages older than retention period are retracted. Compaction mode: for each key, retain only the latest offset fact, retract older ones.

---

**Video Streaming (HLS/DASH)**

An HTTP endpoint serving manifest files and media segments. The HLS manifest grammar fills the M3U8 template — EXT-X-VERSION, EXT-X-TARGETDURATION, EXTINF per segment. Each segment is a fact — URL, duration as VDR fraction, sequence number as integer. Adaptive bitrate: multiple rendition KBs (720p, 1080p, 4K), master manifest lists all renditions. The client selects based on bandwidth. Segment files are served via granted filesystem primitives.

Live streaming: a processor runner ingests the live feed, segments it (granted media primitive), asserts new segment facts, retracts old ones beyond the sliding window. The manifest is regenerated from current segment facts on each client request. DVR: don't retract old segments, extend the window. The manifest grammar adjusts to include the full range.

---

**WebRTC Signaling**

WebSocket-based signaling. The signaling grammar handles offer/answer SDP exchange and ICE candidate trickling. Each peer connection is a session KB with local and remote SDP facts, ICE candidate facts, connection state as a Prolog state machine. The actual media (audio/video RTP) flows peer-to-peer — the VDR-LLM-Prolog system only handles signaling, not media transport.

TURN relay: if peer-to-peer fails, a processor runner handles TURN allocation requests. Each allocation is a session KB with permissions (facts), channels (facts), and lifetime (counter with expiration). STUN binding requests are handled inline — a grammar-driven response with the client's observed address.

---

**SMTP with Spam Filtering**

Extends the basic SMTP handler. After parsing the message, before delivering to the user's inbox, a Prolog rule cascade evaluates spam indicators. SPF: DNS query for sender's SPF record, evaluate against connecting IP using Prolog rules that implement the SPF macro language. DKIM: parse the DKIM-Signature header, fetch the public key via DNS, verify the signature using granted cryptographic primitives. DMARC: check alignment between SPF/DKIM domains and the From header.

Content analysis: Prolog rules check for known spam patterns in the header and body facts. Bayesian scoring uses VDR fractions — P(spam|word) as exact fractions from training data facts. The spam score is an exact VDR fraction with full provenance showing which rules contributed what score. The user can query "why was this marked as spam" and get an exact answer — not "the model thought it was spam" but "SPF failed (0/1), DKIM passed (1/1), content score 73/100 exceeding threshold 70/100 due to rules R47, R112, R203."

---

**Print Service (IPP)**

A processor runner listens on port 631. The IPP protocol is HTTP POST with binary-encoded attributes. The IPP grammar parses print job attributes — document format, copies, page ranges, finishing options. Each print job is a KB with job state facts — pending, processing, completed, aborted. The printer is a KB with capability facts — supported formats, maximum resolution, paper sizes. A Prolog rule validates the job against printer capabilities before accepting. Job processing invokes granted printer primitives. Job history is persistent facts with provenance.

---

Every one of these follows the same structural pattern. A processor runner or a clone-per-request handler speaks the protocol through a grammar. The grammar handles all structural tokens — protocol framing, field delimiters, encoding rules. Data arrives as facts at integer addresses. Prolog rules process the data using builtins. Results fill response grammars. The LLM provides judgment only when the data requires interpretation that no rule covers. Security is grants on the primitives. Audit is provenance on every operation. The protocol grammar, the Prolog rules, and the builtin primitives replace what would conventionally be thousands of lines of server application code.
