# Scientific Time Series Data: A Proposal for a 21st Century Upgrade to CODATA
## Replacing Averaged Snapshots with Synchronized Observable Measurement

**Registry:** [@HOWL-CULT-13-2026]

**Series Path:** [@HOWL-CULT-1-2026] → [@HOWL-CULT-2-2026] → [@HOWL-CULT-3-2026] → [@HOWL-CULT-4-2026] → [@HOWL-CULT-5-2026] → [@HOWL-CULT-6-2026] → [@HOWL-CULT-7-2026] → [@HOWL-CULT-8-2026] → [@HOWL-CULT-9-2026] → [@HOWL-CULT-12-2026] → [@HOWL-CULT-13-2026]

**Date:** May 2026

**DOI:** 10.5281/zenodo.20181965

**Domain:** Metrology / Data Infrastructure / Philosophy of Science

**Status:** Infrastructure proposal with falsifiable predictions

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## 1. What CODATA Currently Does

The Committee on Data for Science and Technology — CODATA — publishes recommended values for the fundamental physical constants. These values are used worldwide as reference inputs for calculation, engineering, and further scientific work. The publication cycle spans several years. Each cycle produces a new set of recommended values that supersede the previous set.

The process that produces these values operates as follows. Instruments around the world measure physical constants. The instruments differ from each other. They use different sensor mechanisms. They are located at different positions on the Earth's surface, at different altitudes, in different geological and electromagnetic environments. They operate at different times — different days, different seasons, different years. Each instrument produces a measurement: a value for the quantity it was designed to measure.

These measurements are collected by the committee. The committee evaluates them according to criteria that include the experiment's stated uncertainty, the methodology's internal consistency, and the committee's assessment of the measurement's reliability. The committee assigns weights to the measurements. The committee computes a weighted average. The committee publishes the average as the recommended value, accompanied by an uncertainty that reflects the committee's assessment of the combined evidence.

The recommended value is what downstream users receive. A physicist calculating a derived quantity uses the recommended value. An engineer designing a precision instrument uses the recommended value. A textbook reports the recommended value. The recommended value is, for practical purposes, the measurement — the single number that represents what the scientific community knows about the quantity in question.

The individual measurements that went into the average are available in the scientific literature for those who seek them out. But the recommended value is the operational output. It is the number that propagates. It is the number that enters subsequent calculations. It is the number that most users treat as the established fact about the quantity.

---

## 2. What the Average Destroys

The averaging process converts many measurements into one number. This conversion has a cost. Three categories of information that exist in the individual measurements do not exist in the averaged output.

**Disagreement between instruments.** If two instruments measuring the same quantity produce different values, the difference between them is a datum. It tells you that something differs between the two measurement contexts — the device, the location, the time, the operating conditions, or some combination. Under the current process, this disagreement is absorbed. The two values are weighted and averaged. The output is a single number that lies between them. The disagreement still exists implicitly in the uncertainty band — a larger spread among input measurements produces a larger stated uncertainty — but the specific structure of the disagreement is gone. You cannot see from the recommended value that instrument A read high and instrument B read low. You cannot ask whether A and B differ because of their locations, their sensor types, or the dates of their measurements. The information that would let you ask that question has been compressed out.

The gravitational constant G illustrates this precisely. G has been measured by multiple independent experiments using different apparatus. The measurements do not converge. The disagreement between independent determinations is larger than the individual experiments' stated uncertainties. This is an anomaly. Under the current process, the committee publishes a new recommended value each cycle. The value shifts. The uncertainty band is adjusted. The non-convergence is treated as a problem of experimental quality to be resolved by future improvements in measurement technique. What the non-convergence might be telling us — that something about the measurement context affects the result in ways the model does not account for — cannot be investigated through the averaged output because the structure of the disagreement has been removed.

**Temporal structure.** Physical constants are assumed to be constant. This assumption may be correct. But the assumption is built into the measurement process in a way that prevents it from being tested. Instruments that measure a constant over an extended period produce a time series — a sequence of values with timestamps. This time series might be flat, confirming that the quantity does not vary over time. It might show fluctuations correlated with identifiable events. It might show a slow drift. Under the current process, the time series is reduced to a summary statistic before it enters the committee's evaluation. The temporal structure — the shape of the signal over time — is discarded. If the quantity does vary over some timescale, the variation is averaged away. The averaged output cannot reveal it because the averaging was designed to remove it.

**Contextual correlation.** Each measurement occurs in a physical context. The instrument is at a specific location on the Earth's surface. The Earth is at a specific point in its orbit. The Sun is in a specific state of activity. The local geological composition, electromagnetic environment, altitude, and gravitational field are specific to the measurement site. If any of these contextual factors affect the measurement, that effect is present in the raw data as a correlation between the reading and the context. Under the current process, the context is stripped. The measurement enters the average as a number detached from the conditions that produced it. A correlation between the reading and the local gravitational field, or the solar cycle, or the seismic state of the region, would be invisible in the output because the contextual variables were not preserved alongside the reading.

Each of these three losses — disagreement structure, temporal structure, and contextual correlation — is a loss of information that existed in the data as it was collected. The information was generated by the instruments. It was present in the raw output. It was removed during processing. The removal was not an error in the original design. When CODATA's methodology was established, storing and distributing large datasets was expensive and technically difficult. Averaging was a practical necessity. The averaged value was the most useful thing the infrastructure of the time could deliver. The infrastructure of the time no longer constrains us.

---

## 3. What Modern Data Infrastructure Looks Like

In any complex system that must operate reliably — a power grid, a telecommunications network, a financial exchange, a large-scale software deployment — operators monitor many subsystems simultaneously. This practice is well-established and its principles are not domain-specific. The principles transfer directly.

Each subsystem reports its state continuously. A network router reports traffic volume, error rates, and latency. A power generator reports output, temperature, and fuel consumption. A software service reports request rates, response times, error counts, and resource utilization. Each report includes a timestamp. The timestamps are synchronized to a common reference — typically GPS-derived UTC — so that reports from different subsystems can be placed on the same timeline.

The reports are stored in a common format in a database designed for time-ordered data. The format is standardized so that tools can read data from any subsystem without custom parsing. The database is queryable so that an analyst can ask questions across subsystems and across time: "show me network error rates and application response times on the same graph for the last six hours" is a routine query.

When something goes wrong in the system, the analyst uses this infrastructure to locate the problem. The process is mechanical. Pull up the time window where the problem was observed. Display multiple subsystems on the same time axis. Look for the moment where two or more readings changed together. A spike in network errors that coincides with a spike in application response time suggests the network is the cause. A spike in application response time with no corresponding network change suggests the application is the cause. The correlated change — or the absence of correlated change — is the lead that narrows the search.

This practice depends on three properties. First, time synchronization: all reports reference the same clock, so events in different subsystems can be compared. Second, format standardization: all reports use a common structure, so tools work across subsystems without modification. Third, cross-domain queryability: any analyst can correlate any subsystem against any other subsystem across any time window, so patterns that span subsystem boundaries can be found.

The practice is called observability. It is standard in every engineering discipline that operates complex systems. It is not a research frontier. It is a solved problem with commodity implementations. Open-source time series databases, standardized data formats, and cross-domain query tools are freely available. Organizations with hundreds of thousands of monitored subsystems use this infrastructure daily.

The purpose of describing this practice is not to argue that physics should adopt software engineering methods by analogy. The purpose is to establish that the infrastructure for storing, synchronizing, and querying time series data from many sources simultaneously is mature, available, and routine. The infrastructure exists. The question is whether to apply it to scientific measurement data.

---

## 4. The Proposal

Three concrete changes to the way fundamental physical measurements are recorded, stored, and published.

**First: time-synchronize all contributing instruments to a common reference clock.** Every instrument that contributes measurements to the reference dataset records its readings with timestamps derived from a common time standard. GPS provides this capability at nanosecond precision, globally, using existing satellite infrastructure. Many precision instruments already reference GPS time for their own internal purposes. The change is to make this timestamp a required, standardized part of the published output rather than an internal operational detail.

**Second: publish each instrument's readings as a time series with full metadata.** Each contributing instrument publishes its sequence of readings — not a summary, not an average, but the readings themselves with their timestamps. Alongside each time series, the instrument publishes its metadata: device type, sensor mechanism, physical location (latitude, longitude, altitude), local environmental conditions where known (geological composition, electromagnetic environment, temperature, pressure), calibration state, and operating parameters. The time series and its metadata together form a complete record of what the instrument observed, when it observed it, and the conditions under which the observation was made.

**Third: make the unified dataset publicly queryable in a standardized format.** All time series from all contributing instruments are stored in a common database using a standard time series format. The database supports queries across instruments, across quantities, and across time. An analyst can request: all measurements of quantity X from all instruments during time window T. Or: measurements of quantity X from instrument A and measurements of quantity Y from instrument B, aligned on the same time axis. Or: all measurements from all instruments during event E, where E is a solar flare, a seismic event, a geomagnetic storm, or any other identified occurrence with a known time window.

Under this proposal, the committee's role changes. The committee no longer produces the answer. The committee maintains the infrastructure. The committee coordinates synchronization standards. The committee validates instrument metadata. The committee certifies that contributing instruments meet quality criteria for inclusion in the dataset. The committee ensures that the data is trustworthy at the source. The data, once certified, speaks for itself. Any analyst can query it, weight it by their own criteria, and draw their own conclusions. The committee's expertise is applied where it is most valuable — at the point of data quality assurance — rather than at the point of interpretation.

The recommended value can still be computed from the dataset by anyone who wants it. The averaging methodology can still be applied. But the average becomes one view of the data rather than the only view. The raw structure is preserved. The temporal, spatial, and instrumental context is preserved. Nothing is destroyed.

---

## 5. What Becomes Visible

The time series format enables categories of analysis that the averaged format structurally cannot perform. Each category is concrete and each produces findings regardless of outcome — a positive result is a discovery, a null result is a closure.

**Investigation of non-convergence.** The gravitational constant G is the clearest current example. Measurements from independent experiments disagree beyond their stated uncertainties. Under the proposed system, each instrument's time series is visible with its full context. The analyst can test specific hypotheses: does the disagreement correlate with device type? If instruments using torsion balances consistently read differently from instruments using beam balances, the disagreement is located at the sensor mechanism. Does the disagreement correlate with geographic location? With altitude? With local geological density? Each test is a direct comparison on the queryable dataset. Each test either identifies a contributing factor or eliminates one. In either case, the search space narrows. Under the current system, none of these tests can be performed because the data needed to perform them — simultaneous time-stamped readings from multiple instruments with preserved context — does not exist in a queryable form.

**Cross-domain correlation.** This is the category with the largest potential information yield and the category that is most completely invisible under the current system. If every domain publishes its measurements as synchronized time series, then quantities from different domains can be placed on the same time axis for the first time. Measurements of the fine structure constant can be compared against solar activity indices. Particle decay rates can be compared against Earth's orbital parameters. Magnetic moment measurements can be compared against local gravitational field readings. Atomic clock rates at different altitudes can be compared against each other and against geomagnetic field measurements.

The current system cannot discover correlations between quantities in different domains because the quantities are never placed on the same timeline. Each domain averages its own data independently and publishes on its own schedule. If a real correlation exists between two quantities measured by two different fields — if, for instance, a measured quantity shows a periodic variation synchronous with a specific solar cycle — the current system is structurally blind to it. Not because the correlation is too small to measure. Not because the instruments lack precision. Because the temporal structure needed to detect the correlation was destroyed when each domain averaged its data independently. The proposed system preserves the temporal structure. Whether specific correlations exist is an empirical question that the current system cannot ask and the proposed system can.

**Event-driven analysis.** Discrete physical events occur continuously. Solar flares. Coronal mass ejections. Geomagnetic storms. Seismic events. Meteor showers. Gravitational wave detections. Each event has a known time window. Under the proposed system, every synchronized instrument is recording during these events. The analyst can query the dataset for all readings from all instruments during any event window and compare them against the same instruments' baseline readings outside the event window.

If an instrument measuring a physical constant shows a deviation from baseline during a solar flare, that deviation is a discovery — something about the solar flare affected the measurement, and the nature of the effect is a lead. If no instrument shows any deviation during any event, that is also a finding — the measured constants are independent of these events at the achieved measurement precision, which closes a question that the current system leaves permanently open because it never performs the comparison.

**Drift detection.** If a physical constant is truly constant, its time series from every instrument is flat after accounting for instrument noise. If a constant changes slowly over time — over years, over decades, over the period of Earth's orbit — the drift is present in the time series. Under the current system, drift slower than the publication cycle is undetectable because each cycle's average is treated independently. A slow upward trend spanning five publication cycles would appear as five slightly different recommended values, each attributed to improved measurement technique or updated methodology. Under the proposed system, the continuous time series reveals the trend directly. Whether any fundamental quantity drifts is an empirical question. The current system cannot answer it for drifts at timescales below its temporal resolution. The proposed system's temporal resolution is the instrument's own sampling rate, which for precision instruments is typically seconds or better.

---

## 6. The Infrastructure Already Exists

The most common objection to any data infrastructure proposal is impracticality. This section addresses that objection by identifying each required component and its current state of availability.

**Time synchronization.** GPS provides time synchronization to nanosecond precision at any point on Earth's surface with a clear view of the sky. GPS receivers are commodity hardware. Many precision measurement instruments already use GPS-derived time references for internal operation. Network Time Protocol and Precision Time Protocol provide sub-microsecond synchronization over standard network connections. The time synchronization infrastructure required by the proposal is deployed, global, and available at negligible cost relative to the instruments it would synchronize.

**Time series data formats.** Standardized formats for time-stamped measurement data exist and are used at scale across multiple industries. Financial markets record and distribute tick-level transaction data for thousands of instruments simultaneously. Climate science stores decades of continuous measurements from thousands of weather stations and ocean buoys in standardized formats. Industrial monitoring systems collect and store continuous readings from sensors across manufacturing facilities. The data format problem — how to represent a timestamped measurement with associated metadata in a structure that tools can read without custom parsing — is solved. Multiple open standards exist. The choice among them is an engineering decision, not a research problem.

**Queryable time series databases.** Databases designed specifically for time series data are commodity technology. Open-source implementations capable of handling billions of data points with sub-second query times are freely available and actively maintained. Commercial implementations operating at larger scales are available from multiple vendors. The storage and query infrastructure required to hold synchronized time series from every precision measurement instrument in the world is a small deployment by the standards of industries that already use this technology. A single large financial exchange processes more time series data per day than the proposed scientific measurement database would accumulate in a year.

**Cross-domain data federation.** The ability to query data from multiple independent sources as if it were a single dataset — federation — is a solved problem in data engineering. Standard query interfaces, common data models, and federation middleware exist as both open-source and commercial products. Organizations routinely federate data across hundreds of independent subsystems maintained by independent teams. The organizational challenge of getting independent physics laboratories to publish data in a common format is real but it is a coordination problem, not a technology problem. The technology to federate the data once published is mature.

No component of the proposed infrastructure requires new technology. Every component exists, is deployed at scale in other domains, and is available either as open-source software or as commodity services. The total infrastructure cost is small relative to the cost of the instruments that would contribute data to it. A single precision measurement experiment at a national laboratory costs more to build and operate than the entire data infrastructure described in this proposal.

---

## 7. Why This Matters Physically

The preceding sections describe the proposal as a data infrastructure improvement. This section describes why the improvement matters beyond administrative convenience — why the structure of the measurement system has consequences for the structure of physical knowledge.

Physical quantities are not independent of each other. They are produced by a single physical system — the universe — in which every interaction is mechanically connected to every other interaction through the forces and fields that operate at each point in space at each moment in time. The universe does not compute the gravitational constant independently from the fine structure constant. It does not compute particle masses independently from coupling strengths. Every quantity that we measure separately is a partial observation of a single integrated computation that the universe performs continuously.

The Planck time — approximately 5.4 × 10⁻⁴⁴ seconds — is the smallest physically meaningful time interval. Below this interval, the concept of sequential time loses physical meaning. At each Planck interval, the physical state updates. The update is finite — a finite number of operations on a finite state producing a finite result. The update is deterministic at the level of the complete state — given the full state at one tick, the state at the next tick is determined. The update is universal — every point, every quantity, every interaction updates on the same clock.

This structure has a direct consequence for measurement. If all quantities are computed by the same system on the same clock, then any two quantities that share upstream causal structure will show correlated behavior at some timescale. The correlations may be strong or weak. They may operate at timescales accessible to current instruments or at timescales too fast or too slow to detect. But the possibility of correlation between any two measured quantities is a physical consequence of the fact that all quantities are produced by one system. The question of whether specific correlations exist is empirical. It can only be answered by measurement systems that preserve the temporal structure needed to detect them.

The current measurement system destroys temporal structure during processing. Each domain reduces its continuous measurements to summary statistics. The summary statistics from different domains are published on different schedules. Cross-domain correlation — the primary signal that would reveal connections between quantities produced by the same underlying system — is undetectable by construction. Not because the instruments lack precision. Not because the correlations are too small. Because the data processing pipeline removes the temporal alignment that correlation detection requires.

This is not a subtle or debatable point. It is a mechanical fact about information. If you average a signal over a long window, you cannot detect variations shorter than the window. If you average signals from two different sources over different windows, you cannot detect correlations between them at any timescale shorter than the longer window. The current system averages across different windows in every domain independently. Cross-domain correlation at any timescale shorter than the publication cycle is invisible. This is a property of the processing, not of the physics.

The proposed system preserves temporal structure at the instruments' native sampling rates. It synchronizes across domains on a common clock. It enables correlation detection at any timescale the instruments can resolve. Whether the universe's single-system structure produces measurable cross-domain correlations at accessible timescales is unknown. It is unknown because the measurement infrastructure needed to answer the question has never been built. The proposal is to build it.

---

## 8. Falsification Conditions

This proposal commits to testable predictions. Each prediction specifies an observable outcome that would demonstrate the proposal's motivating hypothesis is wrong.

**Prediction 1: Cross-domain correlations exist and are detectable.** If synchronized time series measurement across multiple domains, sustained over a sufficient observation period with sufficient instrument coverage, reveals zero unexpected correlations between quantities in different domains, then the motivating hypothesis — that temporal structure contains discoverable cross-domain information — is wrong. The time-synchronization infrastructure would retain value for transparency and reproducibility, but its primary scientific justification would have failed.

**Prediction 2: The G non-convergence has identifiable contextual structure.** If time series analysis of synchronized G measurements from multiple instruments with full contextual metadata shows no correlation between the inter-instrument disagreement and any available contextual variable — device type, location, altitude, geology, time, solar activity, seismic state, geomagnetic conditions — then the non-convergence is not caused by uncontrolled contextual factors. The search for its cause must look elsewhere, and this proposal's specific prediction about G has failed.

**Prediction 3: Event-driven analysis reveals measurable effects.** If no precision measurement instrument shows any statistically significant deviation from baseline during any category of discrete physical event — solar flares, geomagnetic storms, seismic events, gravitational wave detections — over a sustained observation period, then the hypothesis that these events produce measurable effects on fundamental quantities is wrong. This null result would itself constitute a finding: the measured constants are independent of these event categories at the achieved measurement precision. This is a closure — a question that the current system leaves permanently open, answered definitively by the proposed system.

**Prediction 4: Drift detection produces results within one decade.** If continuous time series monitoring of fundamental quantities over a ten-year period reveals no drift in any measured constant beyond instrument noise, then either the constants do not drift at timescales below a decade, or the instruments' precision is insufficient to detect the drift. In either case, the proposal's implicit suggestion that averaging might mask long-term trends would be unsupported at the achieved precision and timescale.

Each of these predictions is specific. Each is observable. Each could fail. The proposal commits to each and accepts falsification if it comes. The critical point is that every one of these questions is currently unanswerable — not because the questions are unanswerable in principle, but because the measurement infrastructure needed to answer them does not exist. The proposal's minimum contribution, regardless of which predictions survive, is to make these questions answerable for the first time.

---

## 9. Closing

CODATA was designed under 20th century infrastructure constraints. Collecting measurements from worldwide instruments, shipping them to a central committee, and computing a weighted average was the best that the available data infrastructure could do. The constraints shaped the methodology. The methodology became the standard. The standard persists.

The constraints no longer exist. Global time synchronization is available at nanosecond precision. Time series data storage and query systems handle billions of data points routinely. Standardized formats for timestamped measurement data are mature and widely deployed. Cross-domain data federation is a solved engineering problem. Every technical component needed to upgrade from averaged snapshots to synchronized time series is available, tested, and affordable.

The upgrade preserves everything the current system provides. The recommended value can still be computed from the dataset by anyone who wants it. Nothing is taken away. What is added is the raw structure — the temporal, spatial, and instrumental context that the averaging process currently destroys. The structure that would let anyone ask whether two quantities correlate, whether a measurement depends on its context, whether a constant drifts, or whether a discrete physical event affects a precision reading.

The universe produces its measurements continuously, simultaneously, at every point, on a single clock. The proposal is to record them the same way.

---

## References

[1] CODATA Task Group on Fundamental Constants, "CODATA Recommended Values of the Fundamental Physical Constants," *Reviews of Modern Physics*, 2021.

[2] E. Tiesinga et al., "CODATA 2018 values of the fundamental physical constants," *Journal of Physical and Chemical Reference Data*, vol. 50, 2021.

[3] Particle Data Group, "Review of Particle Physics," *Progress of Theoretical and Experimental Physics*, 2022.

[4] T. Quinn et al., "The BIPM measurements of the Newtonian constant of gravitation, G," *Philosophical Transactions of the Royal Society A*, 2014.

---

**Series cross-references (for deeper treatment of concepts introduced in this paper):**

- Why averaging obscures structural information: [@HOWL-CULT-1-2026]
- The institutional gap between measurement domains: [@HOWL-CULT-2-2026]
- What falsification structurally requires of a measurement: [@HOWL-CULT-4-2026]
- Why located errors are the most valuable finding: [@HOWL-CULT-5-2026]
- Working in the space between institutional departments: [@HOWL-CULT-8-2026]
- Institutional structure for cross-domain work: [@HOWL-CULT-9-2026]
- Departmental boundaries preventing recognition of unifying patterns: [@HOWL-CULT-10-2026]
- The structural mechanics of institutional non-commitment: [@HOWL-CULT-12-2026]
