# event_constraints(id|event_id|prolog_rules|note)
# prolog_rules: comma-separated prolog conditions
# Self binds to current entity instance for Infinity groups

# === BIOS (G1, Zero — pure event sequencing) ===
EC1|EV1|true|POST is the initial event, no precondition
EC2|EV2|event_completed(ev1)|POST passed
EC3|EV3|event_completed(ev2)|hardware enumerated
EC4|EV4|event_completed(ev3)|boot device selected
EC5|EV5|event_completed(ev4)|MBR loaded

# === Bootloader (G2, Zero) ===
EC6|EV6|event_completed(ev5)|BIOS transferred control
EC7|EV7|event_completed(ev6)|stage1 loaded
EC8|EV8|event_completed(ev7)|stage2 loaded
EC9|EV9|event_completed(ev8)|kernel located
EC10|EV10|event_completed(ev9)|kernel in memory
EC11|EV11|event_completed(ev10)|initrd loaded
EC12|EV12|event_completed(ev11)|params set

# === Kernel (G3, One) ===
EC13|EV13|event_completed(ev12)|bootloader transferred control
EC14|EV14|event_completed(ev13)|kernel entered
EC15|EV15|event_completed(ev14)|page tables initialized
EC16|EV16|event_completed(ev15)|memory manager started
EC17|EV17|event_completed(ev16)|interrupt table built
EC18|EV18|event_completed(ev17)|timer started
EC19|EV19|event_completed(ev17)|timer started (parallel with console)
EC20|EV20|event_completed(ev18), event_completed(ev19)|console and PCI both done
EC21|EV21|event_completed(ev20), device_ready(Self, root_disk, DevicePath)|block devices discovered and root device ready
EC22|EV22|event_completed(ev21)|root filesystem mounted
EC23|EV23|event_completed(ev22), filesystem_contains(initrd, modules)|initrd unpacked and modules present
EC24|EV24|event_completed(ev23), filesystem_mounted(Self, root, RootPath)|modules loaded and root mounted
EC25|EV25|unrecoverable_error(Self, Reason)|any unrecoverable kernel error

# === Init System (G4, One) ===
EC26|EV26|event_completed(ev24)|kernel root switched
EC27|EV27|event_completed(ev26), config_readable(inittab, RunLevel)|init started and inittab readable
EC28|EV28|event_completed(ev27)|runlevel determined
EC29|EV29|event_completed(ev28), config_readable(sysctl_conf, Params)|hostname set and sysctl config readable
EC30|EV30|event_completed(ev29)|sysctl applied
EC31|EV31|event_completed(ev30), device_scan_complete(Count), Count > 0|udev started and devices found
EC32|EV32|event_completed(ev31)|devices populated
EC33|EV33|event_completed(ev32), all_checks_passed(true)|filesystems checked and clean
EC34|EV34|event_completed(ev33), device_ready(swap, SwapPath)|filesystems mounted and swap device ready
EC35|EV35|event_completed(ev34)|swap enabled (parallel with loopback)
EC36|EV36|event_completed(ev34)|swap enabled (parallel with clock)
EC37|EV37|event_completed(ev35), event_completed(ev36), network_interface_exists(Iface, Count), Count > 0|clock synced, loopback up, interfaces exist
EC38|EV38|event_completed(ev37), config_readable(firewall_rules, Rules)|network configured and firewall rules readable
EC39|EV39|event_completed(ev38), network_interface_active(Iface, true)|firewall applied and interface active
EC40|EV40|error_occurred(Self, Step, Reason)|any init step failed

# === Memory Manager (G5, One) ===
EC41|EV41|event_completed(ev15)|kernel memory manager started
EC42|EV42|initialized(Self, true), page_available(Self, Address)|initialized and free page exists
EC43|EV43|page_allocated(Self, Address), refcount(Self, Address, 0)|page allocated and no references
EC44|EV44|free_page_ratio(Self, Ratio), Ratio < 0.3, fragmentation_ratio(Self, Frag), Frag > 0.5|low free pages and high fragmentation
EC45|EV45|compaction_running(Self, true)|compaction was started
EC46|EV46|free_page_ratio(Self, Ratio), Ratio < 0.2|very low free pages
EC47|EV47|reclaim_running(Self, true)|reclaim was started
EC48|EV48|free_page_ratio(Self, Ratio), Ratio < 0.05, reclaim_exhausted(Self, true)|critical and nothing left to reclaim
EC49|EV49|oom_triggered(Self, true), victim_selected(Self, PID)|OOM triggered and victim identified
EC50|EV50|free_page_ratio(Self, Ratio), Ratio < 0.3|entering degraded
EC51|EV51|free_page_ratio(Self, Ratio), Ratio < 0.05|entering critical

# === Scheduler (G6, One) ===
EC52|EV52|event_completed(ev41)|memory manager initialized
EC53|EV53|run_queue_nonempty(Self, true)|at least one process ready
EC54|EV54|run_queue_imbalance(Self, Ratio), Ratio > 0.3|significant CPU load imbalance
EC55|EV55|rebalance_running(Self, true)|rebalance was started
EC56|EV56|starvation_detected(Self, PID, Duration), Duration > 5.0|process starved for 5+ seconds
EC57|EV57|process_on_wrong_cpu(Self, PID, CurrentCPU, BestCPU), CurrentCPU \= BestCPU|process affinity mismatch
EC58|EV58|timeslice_exhausted(Self, PID, true)|current process used its quantum
EC59|EV59|run_queue_length(Self, Length), Length > 100|run queue excessively long

# === VFS (G7, One) ===
EC60|EV60|event_completed(ev21)|kernel root filesystem mounted
EC61|EV61|initialized(Self, true)|VFS initialized
EC62|EV62|filesystem_type_registered(Self, FSType), device_ready(DeviceId, true)|type registered and device ready
EC63|EV63|mount_active(Self, MountPoint), no_open_files(Self, MountPoint)|mount exists and no open files
EC64|EV64|mount_active(Self, MountPoint), path_valid(Self, Path)|mount active and path resolves
EC65|EV65|fd_open(Self, FD, true)|file descriptor is open
EC66|EV66|mount_active(Self, MountPoint), dirty_pages(Self, MountPoint, Count), Count > 0|dirty pages exist
EC67|EV67|mount_active(Self, MountPoint)|mount active for path resolution

# === Network Stack (G8, One) ===
EC68|EV68|event_completed(ev37)|init network interfaces configured
EC69|EV69|initialized(Self, true), packet_in_buffer(Self, Iface, true)|initialized and inbound packet waiting
EC70|EV70|initialized(Self, true), packet_in_outbound_queue(Self, true)|outbound packet queued
EC71|EV71|packet_matches_drop_rule(Self, Packet, true)|packet matches drop condition
EC72|EV72|drop_rate(Self, Iface, Rate), Rate > 0.05|drop rate exceeds 5%
EC73|EV73|drop_rate(Self, Iface, Rate), Rate < 0.01|drop rate below 1%
EC74|EV74|route_change_pending(Self, true)|routing update received
EC75|EV75|segment_ack_timeout(Self, ConnID, SegID, true)|ACK timeout on segment

# === Display Server (G9, One) ===
EC76|EV76|event_completed(ev39), gpu_device_ready(true)|init complete and GPU ready
EC77|EV77|running(Self, true), frame_due(Self, true)|compositor running and frame tick
EC78|EV78|running(Self, true), input_pending(Self, true)|input event waiting
EC79|EV79|event_completed(ev76)|display server started
EC80|EV80|event_completed(ev79)|session manager started
EC81|EV81|suspend_requested(Self, true)|system suspend requested
EC82|EV82|resume_requested(Self, true)|system resume requested
EC83|EV83|unrecoverable_error(Self, Reason)|display server error

# === Audio Mixer (G10, One) ===
EC84|EV84|event_completed(ev39), audio_device_ready(true)|init complete and audio device ready
EC85|EV85|running(Self, true), active_channels(Self, Count), Count > 0|running and channels to mix
EC86|EV86|running(Self, true), volume_change_requested(Self, Channel, Volume)|volume change request
EC87|EV87|running(Self, true), mute_requested(Self, true)|mute requested
EC88|EV88|muted(Self, true), unmute_requested(Self, true)|unmute requested
EC89|EV89|running(Self, true), suspend_requested(Self, true)|suspend requested
EC90|EV90|suspended(Self, true), resume_requested(Self, true)|resume requested
EC91|EV91|unrecoverable_error(Self, Reason)|audio error

# === Device Manager (G11, One) ===
EC92|EV92|event_completed(ev30)|init udev started
EC93|EV93|running(Self, true), bus_scan_requested(Self, BusType)|bus scan triggered
EC94|EV94|device_discovered(DeviceID), driver_exists(DeviceID, Driver)|device found and driver available
EC95|EV95|driver_matched(DeviceID, Driver), module_available(Driver)|driver matched and module loadable
EC96|EV96|driver_loaded(DeviceID, true)|driver loaded for device
EC97|EV97|device_removed(DeviceID, true)|device hotplug removal
EC98|EV98|device_state_changed(DeviceID, true)|any device state change
EC99|EV99|unrecoverable_error(Self, Reason)|device manager error

# === Swap Manager (G12, One) ===
EC100|EV100|event_completed(ev34), swap_device_valid(Device)|init swap enabled and device valid
EC101|EV101|active(Self, Device), deactivate_requested(Self, Device)|deactivation requested
EC102|EV102|active(Self, true), page_swap_out_requested(Self, Address)|swap out request from memory manager
EC103|EV103|active(Self, true), page_swap_in_requested(Self, Address)|swap in request from memory manager
EC104|EV104|active(Self, true), fragmentation_ratio(Self, Ratio), Ratio > 0.5|high fragmentation
EC105|EV105|defragmenting(Self, true)|defrag was started
EC106|EV106|usage_ratio(Self, Ratio), Ratio > 0.95|swap nearly full
EC107|EV107|io_rate(Self, Rate), Rate > 1000|excessive swap IO (thrashing)

# === Firewall (G13, One) ===
EC108|EV108|event_completed(ev38), rules_valid(Self, true)|init firewall applied and rules valid
EC109|EV109|packet_evaluated(Self, Packet), rule_result(Self, Packet, allow)|packet matches allow rule
EC110|EV110|packet_evaluated(Self, Packet), rule_result(Self, Packet, drop)|packet matches drop rule
EC111|EV111|packet_evaluated(Self, Packet), rule_result(Self, Packet, reject)|packet matches reject rule
EC112|EV112|reload_requested(Self, true), rules_valid(Self, true)|reload requested and new rules valid
EC113|EV113|unrecoverable_error(Self, Reason)|firewall error

# === DNS Resolver (G14, One) ===
EC114|EV114|event_completed(ev39), config_readable(resolv_conf, Servers)|init DNS configured and resolv.conf readable
EC115|EV115|query_pending(Self, Hostname), resolution_succeeded(Self, Hostname, Address)|query resolved
EC116|EV116|query_pending(Self, Hostname), resolution_failed(Self, Hostname, Reason)|query failed
EC117|EV117|query_pending(Self, Hostname), cache_contains(Self, Hostname, true), cache_ttl_valid(Self, Hostname, true)|cache hit and not expired
EC118|EV118|cache_size(Self, Size), cache_max(Self, Max), Size > Max|cache exceeds max
EC119|EV119|resolution_failed(Self, Hostname, Reason), alternate_server_available(Self, Server)|failure and alternate server exists
EC120|EV120|unrecoverable_error(Self, Reason)|resolver error

# === Session Manager (G15, One) ===
EC121|EV121|event_completed(ev80)|display server login screen rendered
EC122|EV122|running(Self, true), no_active_session(Self, true)|running and no session active
EC123|EV123|login_presented(Self, true), credentials_submitted(Self, Username)|login shown and credentials received
EC124|EV124|credentials_valid(Self, Username, true), session_slot_available(Self, true)|valid credentials and session slot open
EC125|EV125|session_active(Self, SessionID), logout_requested(Self, SessionID)|session exists and logout requested
EC126|EV126|session_active(Self, FromID), session_active(Self, ToID), switch_requested(Self, ToID)|both sessions exist and switch requested
EC127|EV127|session_active(Self, SessionID), lock_requested(Self, SessionID)|session active and lock requested
EC128|EV128|unrecoverable_error(Self, Reason)|session manager error

# === System Logger (G16, One) ===
EC129|EV129|event_completed(ev39)|init DNS configured (logger can start early, but fully operational after network)
EC130|EV130|running(Self, true), entry_pending(Self, true)|running and log entry waiting
EC131|EV131|buffer_count(Self, Count), Count > 0, flush_requested(Self, true)|buffer has entries and flush triggered
EC132|EV132|log_file_size(Self, Path, Size), max_size(Self, Path, Max), Size > Max|log file exceeds max size
EC133|EV133|running(Self, true), remote_configured(Self, Dest), entry_pending_forward(Self, true)|remote configured and entry to forward
EC134|EV134|buffer_count(Self, Count), buffer_max(Self, Max), Count >= Max|buffer full
EC135|EV135|unrecoverable_error(Self, Reason)|logger error

# === Package Manager (G17, One) ===
EC136|EV136|refresh_requested(Self, true), network_available(true)|refresh requested and network up
EC137|EV137|index_current(Self, true), install_requested(Self, Package)|index current and install requested
EC138|EV138|dependencies_resolved(Self, Package, true), download_source_available(Self, true)|deps resolved and source reachable
EC139|EV139|package_downloaded(Self, Package, true), checksum_valid(Self, Package, true)|downloaded and verified
EC140|EV140|remove_requested(Self, Package), no_dependents(Self, Package, true)|remove requested and nothing depends on it
EC141|EV141|verify_requested(Self, true)|integrity check requested
EC142|EV142|operation_failed(Self, Package, Reason)|any package operation failed

# === Process (G18, Infinity) ===
EC143|EV143|fork_requested(Parent, true)|parent requested fork
EC144|EV144|process_entity(Self), fork_executing(Self, true)|fork in progress
EC145|EV145|process_entity(Self), exec_requested(Self, Executable)|exec requested
EC146|EV146|process_entity(Self), resources_allocated(Self, true)|process resources ready
EC147|EV147|process_entity(Self), scheduled(Self, CPU)|scheduler assigned CPU
EC148|EV148|process_entity(Self), waiting_on(Self, Resource, true)|waiting for IO/lock/etc
EC149|EV149|process_entity(Self), sleep_requested(Self, Duration)|sleep syscall
EC150|EV150|process_entity(Self), wait_condition_met(Self, true)|blocked condition resolved
EC151|EV151|process_entity(Self), syscall_requested(Self, SyscallID)|trap to kernel
EC152|EV152|process_entity(Self), page_not_present(Self, Address)|virtual page missing
EC153|EV153|process_entity(Self), signal_pending(Self, Signal)|signal queued
EC154|EV154|process_entity(Self), yield_requested(Self, true)|voluntary yield
EC155|EV155|process_entity(Self), exit_requested(Self, ExitCode)|exit syscall or fatal signal
EC156|EV156|process_entity(Self), exited(Self, true), parent_alive(Self, true)|exited but parent hasn't waited
EC157|EV157|process_entity(Self), zombie(Self, true), parent_waiting(Self, true)|parent called wait
EC158|EV158|process_entity(Self), waited(Self, true)|wait collected, fully done

# === Thread (G19, Infinity) ===
EC159|EV159|thread_create_requested(Parent, ProcessID)|thread creation requested
EC160|EV160|thread_entity(Self), resources_allocated(Self, true)|thread resources ready
EC161|EV161|thread_entity(Self), waiting_on(Self, Resource, true)|blocked on lock/condition/IO
EC162|EV162|thread_entity(Self), wait_condition_met(Self, true)|unblocked
EC163|EV163|thread_entity(Self), join_requested(Self, JoiningThread)|another thread joining this one
EC164|EV164|thread_entity(Self), detach_requested(Self, true)|detach from parent
EC165|EV165|thread_entity(Self), mutex_available(Self, MutexID)|mutex is free
EC166|EV166|thread_entity(Self), mutex_held(Self, MutexID)|this thread holds the mutex
EC167|EV167|thread_entity(Self), condition_wait_requested(Self, CondID)|waiting on condition variable
EC168|EV168|thread_entity(Self), condition_signaled(Self, CondID)|condition variable signaled
EC169|EV169|thread_entity(Self), exit_requested(Self, true)|thread termination

# === File (G20, Infinity) ===
EC170|EV170|file_open_requested(ProcessID, Path, Mode)|open syscall
EC171|EV171|file_entity(Self), open(Self, true), read_requested(Self, true)|open and read requested
EC172|EV172|file_entity(Self), open(Self, true), write_requested(Self, true), writable(Self, true)|open, writable, write requested
EC173|EV173|file_entity(Self), open(Self, true), seek_requested(Self, Position)|seek requested
EC174|EV174|file_entity(Self), open(Self, true), lock_requested(Self, LockType), not_locked(Self, true)|open, unlocked, lock requested
EC175|EV175|file_entity(Self), locked(Self, true), unlock_requested(Self, true)|locked and unlock requested
EC176|EV176|file_entity(Self), open(Self, true), sync_requested(Self, true)|sync requested
EC177|EV177|file_entity(Self), io_error(Self, Error)|IO error occurred
EC178|EV178|file_entity(Self), open(Self, true), close_requested(Self, true)|close requested

# === Filesystem Mount (G21, Infinity) ===
EC179|EV179|mount_entity(Self), check_requested(Self, true)|fsck requested
EC180|EV180|mount_entity(Self), check_running(Self, true)|fsck completed
EC181|EV181|mount_entity(Self), checked(Self, clean), device_ready(Self, Device)|clean and device ready
EC182|EV182|mount_entity(Self), mount_in_progress(Self, true)|mount completing
EC183|EV183|mount_entity(Self), mounted(Self, true), remount_requested(Self, Options)|remount requested
EC184|EV184|mount_entity(Self), mounted(Self, true), dirty_pages(Self, Count), Count > 0|dirty pages to flush
EC185|EV185|mount_entity(Self), mounted(Self, true), unmount_requested(Self, true), no_open_files(Self, true)|unmount requested and no open files
EC186|EV186|mount_entity(Self), unmounting(Self, true)|unmount completing
EC187|EV187|mount_entity(Self), error_occurred(Self, Error)|filesystem error

# === Network Connection (G22, Infinity) ===
EC188|EV188|connect_requested(ProcessID, LocalAddr, RemoteAddr)|connect syscall
EC189|EV189|connection_entity(Self), initiated(Self, true)|connection initiated
EC190|EV190|connection_entity(Self), syn_acked(Self, true)|SYN-ACK received
EC191|EV191|connection_entity(Self), established(Self, true), send_buffer_nonempty(Self, true)|data to send
EC192|EV192|connection_entity(Self), established(Self, true), recv_buffer_nonempty(Self, true)|data received
EC193|EV193|connection_entity(Self), established(Self, true), ack_timeout(Self, SegID)|segment ACK timed out
EC194|EV194|connection_entity(Self), established(Self, true), loss_detected(Self, true)|packet loss detected
EC195|EV195|connection_entity(Self), established(Self, true), close_requested(Self, true)|close initiated
EC196|EV196|connection_entity(Self), fin_received(Self, true)|FIN from remote
EC197|EV197|connection_entity(Self), both_fins_sent(Self, true)|both sides closing
EC198|EV198|connection_entity(Self), reset_requested(Self, true)|RST condition
EC199|EV199|connection_entity(Self), time_wait_expired(Self, true)|2MSL timer expired

# === User Account (G23, Infinity) ===
EC200|EV200|account_create_requested(Username)|admin create request
EC201|EV201|account_entity(Self), created(Self, true), activation_approved(Self, true)|created and approved
EC202|EV202|account_entity(Self), active(Self, true), lock_condition(Self, Reason)|lock triggered
EC203|EV203|account_entity(Self), locked(Self, true), unlock_authorized(Self, true)|unlock authorized
EC204|EV204|account_entity(Self), active(Self, true), disable_requested(Self, Reason)|admin disable
EC205|EV205|account_entity(Self), disabled(Self, true), delete_requested(Self, true)|admin delete
EC206|EV206|account_entity(Self), active(Self, true), password_change_requested(Self, true)|password change
EC207|EV207|account_entity(Self), active(Self, true), permission_change_requested(Self, Groups)|permission update

# === User Session (G24, Infinity) ===
EC208|EV208|session_entity(Self), login_presented(true), credentials_entered(Self, Username)|credentials submitted
EC209|EV209|session_entity(Self), credentials_valid(Self, true)|valid credentials
EC210|EV210|session_entity(Self), credentials_valid(Self, false)|invalid credentials
EC211|EV211|session_entity(Self), authenticated(Self, true), session_slot_available(true)|authenticated and slot open
EC212|EV212|session_entity(Self), created(Self, true), home_directory_accessible(Self, true)|session created and home accessible
EC213|EV213|session_entity(Self), environment_loaded(Self, true), autostart_list_resolved(Self, true)|env loaded and autostart list ready
EC214|EV214|session_entity(Self), autostart_complete(Self, true), window_manager_ready(Self, true)|autostart done and WM ready
EC215|EV215|session_entity(Self), desktop_rendered(Self, true), input_focus_granted(Self, true)|desktop rendered and input active
EC216|EV216|session_entity(Self), active(Self, true), idle_time(Self, Time), idle_lock_threshold(Self, Threshold), Time > Threshold|idle exceeded lock threshold
EC217|EV217|session_entity(Self), locked(Self, true), credentials_valid(Self, true)|locked and re-authenticated
EC218|EV218|session_entity(Self), active(Self, true), suspend_requested(Self, true)|suspend requested
EC219|EV219|session_entity(Self), suspended(Self, true), resume_requested(Self, true)|resume requested
EC220|EV220|session_entity(Self), active(Self, true), logout_requested(Self, true)|logout requested
EC221|EV221|session_entity(Self), logout_complete(Self, true)|logout cleanup done

# === Device (G25, Infinity) ===
EC222|EV222|hardware_detected(BusType, VendorID, ProductID), not(device_entity_exists(VendorID, ProductID))|hardware found, no existing entity
EC223|EV223|device_entity(Self), discovered(Self, true), driver_available(Self, Driver)|discovered and driver exists
EC224|EV224|device_entity(Self), driver_loading(Self, true)|driver load completed
EC225|EV225|device_entity(Self), driver_loaded(Self, true), resources_allocated(Self, true)|driver loaded and resources ready
EC226|EV226|device_entity(Self), initializing(Self, true), self_test_result(Self, pass)|self test passed
EC227|EV227|device_entity(Self), initializing(Self, true), self_test_result(Self, fail)|self test failed
EC228|EV228|device_entity(Self), self_test_passed(Self, true)|test passed, device ready
EC229|EV229|device_entity(Self), ready(Self, true), error_detected(Self, Error)|error on ready device
EC230|EV230|device_entity(Self), error_state(Self, true), reset_possible(Self, true), recent_reset_count(Self, N), N < 3|can reset and haven't exhausted retries
EC231|EV231|device_entity(Self), ready(Self, true), suspend_requested(Self, true)|suspend requested
EC232|EV232|device_entity(Self), suspended(Self, true), resume_requested(Self, true)|resume requested
EC233|EV233|device_entity(Self), removal_detected(Self, true)|hotplug removal or unrecoverable error

# === Kernel Module (G26, Infinity) ===
EC234|EV234|module_load_requested(ModuleName), module_available(ModuleName)|load requested and module exists
EC235|EV235|module_entity(Self), loading(Self, true)|load completed
EC236|EV236|module_entity(Self), loaded(Self, true), init_result(Self, success)|init succeeded
EC237|EV237|module_entity(Self), loaded(Self, true), init_result(Self, failure)|init failed
EC238|EV238|module_entity(Self), running(Self, true), unload_requested(Self, true), refcount(Self, 0)|unload requested and not in use
EC239|EV239|module_entity(Self), unloading(Self, true)|unload completed

# === Service (G27, Infinity) ===
EC240|EV240|service_entity(Self), start_requested(Self, true), dependencies_met(Self, true)|start requested and all dependencies running
EC241|EV241|service_entity(Self), starting(Self, true), process_alive(Self, PID)|process launched successfully
EC242|EV242|service_entity(Self), started(Self, true), health_check_passed(Self, true)|started and first health check passed
EC243|EV243|service_entity(Self), running(Self, true), health_check_due(Self, true), health_check_result(Self, pass)|periodic health check passed
EC244|EV244|service_entity(Self), running(Self, true), health_check_due(Self, true), health_check_result(Self, fail)|periodic health check failed
EC245|EV245|service_entity(Self), health_fail_count(Self, N), N > 1, N < 3|multiple health failures but not terminal
EC246|EV246|service_entity(Self), process_alive(Self, false)|process died
EC247|EV247|service_entity(Self), failed(Self, true), restart_policy(Self, auto), restart_count(Self, N), max_restarts(Self, Max), N < Max|auto restart policy and retries remaining
EC248|EV248|service_entity(Self), restarting(Self, true), restart_delay_elapsed(Self, true)|restart delay passed
EC249|EV249|service_entity(Self), running(Self, true), reload_requested(Self, true)|reload requested
EC250|EV250|service_entity(Self), reloading(Self, true)|reload completed
EC251|EV251|service_entity(Self), running(Self, true), stop_requested(Self, true)|stop requested
EC252|EV252|service_entity(Self), stopping(Self, true), process_alive(Self, false)|process terminated
EC253|EV253|service_entity(Self), failed(Self, true), restart_count(Self, N), max_restarts(Self, Max), N >= Max|retries exhausted, escalate

# === Window (G28, Infinity) ===
EC254|EV254|window_create_requested(ProcessID, Title)|process requested window
EC255|EV255|window_entity(Self), created(Self, true), show_requested(Self, true)|show requested
EC256|EV256|window_entity(Self), visible(Self, true), hide_requested(Self, true)|hide requested
EC257|EV257|window_entity(Self), visible(Self, true), focus_requested(Self, true)|focus requested
EC258|EV258|window_entity(Self), focused(Self, true), focus_lost(Self, true)|another window took focus
EC259|EV259|window_entity(Self), visible(Self, true), minimize_requested(Self, true)|minimize requested
EC260|EV260|window_entity(Self), visible(Self, true), maximize_requested(Self, true)|maximize requested
EC261|EV261|window_entity(Self), minimized_or_maximized(Self, true), restore_requested(Self, true)|restore requested
EC262|EV262|window_entity(Self), visible(Self, true), resize_requested(Self, W, H)|resize requested
EC263|EV263|window_entity(Self), visible(Self, true), move_requested(Self, X, Y)|move requested
EC264|EV264|window_entity(Self), close_requested(Self, true)|close requested

# === Network Interface (G29, Infinity) ===
EC265|EV265|interface_hardware_detected(Name, MAC)|hardware or virtual interface detected
EC266|EV266|interface_entity(Self), detected(Self, true), config_available(Self, true)|detected and config exists
EC267|EV267|interface_entity(Self), configuring(Self, true), address_assigned(Self, Address, Mask)|address obtained
EC268|EV268|interface_entity(Self), address_assigned(Self, true), link_up(Self, true)|address and link ready
EC269|EV269|interface_entity(Self), up(Self, true), error_rate(Self, Rate), Rate > 0.01|errors exceeding threshold
EC270|EV270|interface_entity(Self), up(Self, true), down_requested(Self, true)|down requested
EC271|EV271|interface_entity(Self), up(Self, true), dhcp_lease_expiring(Self, true), dhcp_renew_succeeded(Self, Address, Lease)|DHCP renewal
EC272|EV272|interface_entity(Self), error_rate(Self, Rate), Rate > 0.1|severe errors
EC273|EV273|interface_entity(Self), failed_or_degraded(Self, true), reset_requested(Self, true)|reset requested

# === Permission Rule (G30, Infinity) ===
EC274|EV274|permission_grant_requested(SubjectID, Resource, Action)|grant requested
EC275|EV275|permission_entity(Self), active(Self, true), access_requested(Self, SubjectID)|access check
EC276|EV276|permission_entity(Self), active(Self, true), expiry_time(Self, Time), current_time(Now), Now > Time|expired
EC277|EV277|permission_entity(Self), active(Self, true), revoke_requested(Self, true)|revocation

# === Timer (G31, Infinity) ===
EC278|EV278|timer_create_requested(Duration, CallbackEventID)|timer arm requested
EC279|EV279|timer_entity(Self), armed(Self, true), elapsed(Self, Elapsed), duration(Self, Duration), Elapsed >= Duration|timer expired
EC280|EV280|timer_entity(Self), armed(Self, true), reset_requested(Self, NewDuration)|reset requested
EC281|EV281|timer_entity(Self), armed(Self, true), cancel_requested(Self, true)|cancel requested

# === Signal (G32, Infinity) ===
EC282|EV282|signal_send_requested(SourcePID, TargetPID, SignalNum)|kill/raise syscall
EC283|EV283|signal_entity(Self), pending(Self, true), target_ready(Self, TargetPID)|target process can receive
EC284|EV284|signal_entity(Self), delivered(Self, true), handler_registered(Self, Handler)|custom handler exists
EC285|EV285|signal_entity(Self), delivered(Self, true), signal_masked(Self, true)|signal in mask
EC286|EV286|signal_entity(Self), delivered(Self, true), not(handler_registered(Self, _)), not(signal_masked(Self, true))|no handler and not masked

# === Pipe (G33, Infinity) ===
EC287|EV287|pipe_create_requested(ProcessID)|pipe syscall
EC288|EV288|pipe_entity(Self), open(Self, true), write_requested(Self, true), not(full(Self, true))|write requested and space available
EC289|EV289|pipe_entity(Self), open(Self, true), read_requested(Self, true), data_available(Self, true)|read requested and data present
EC290|EV290|pipe_entity(Self), open(Self, true), buffer_full(Self, true)|buffer capacity reached
EC291|EV291|pipe_entity(Self), open(Self, true), end_close_requested(Self, End)|one end closing
EC292|EV292|pipe_entity(Self), write_end_closed(Self, true)|writer gone, pipe broken

# === Shared Memory Region (G34, Infinity) ===
EC293|EV293|shm_allocate_requested(ProcessID, Size)|mmap/shmget syscall
EC294|EV294|shm_entity(Self), allocated(Self, true), map_requested(Self, ProcessID)|map requested
EC295|EV295|shm_entity(Self), mapped(Self, ProcessID), unmap_requested(Self, ProcessID)|unmap requested
EC296|EV296|shm_entity(Self), mapped_count(Self, Count), Count > 0, sync_requested(Self, true)|sync requested
EC297|EV297|shm_entity(Self), mapped_count(Self, 0), free_requested(Self, true)|no mappings and free requested

# === Environment Variable Set (G35, Infinity) ===
EC298|EV298|env_load_requested(ProcessID)|process starting, load env
EC299|EV299|env_entity(Self), loaded(Self, true), set_requested(Self, Key, Value)|set var requested
EC300|EV300|env_entity(Self), loaded(Self, true), unset_requested(Self, Key)|unset var requested
EC301|EV301|env_entity(Self), loaded(Self, true), export_requested(Self, ChildPID)|fork/exec inheriting env

# === Cron Job (G36, Infinity) ===
EC302|EV302|cron_schedule_requested(Expression, Command)|crontab entry
EC303|EV303|cron_entity(Self), scheduled(Self, true), timer_fired(Self, true)|cron timer expired
EC304|EV304|cron_entity(Self), executing(Self, true), process_exited(Self, 0)|job process exited success
EC305|EV305|cron_entity(Self), executing(Self, true), process_exited(Self, Code), Code \= 0|job process exited failure
EC306|EV306|cron_entity(Self), completed_or_failed(Self, true)|ready to reschedule

# === Log Entry (G37, Infinity) ===
EC307|EV307|log_submit_requested(Severity, Source, Message)|any system submits log
EC308|EV308|log_entity(Self), buffered(Self, true), flush_triggered(Self, true)|buffer flushed including this entry
EC309|EV309|log_entity(Self), written(Self, true), rotation_triggered(Self, true)|file rotated, entry in old file
EC310|EV310|log_entity(Self), rotated(Self, true), archive_triggered(Self, true)|old file archived
EC311|EV311|log_entity(Self), archived(Self, true), age(Self, Age), max_age(MaxAge), Age > MaxAge|aged past retention
