set verdi_home $env(VERDI_HOME)
source $(verdi_home)/share/NPI/L1/TCL/npi_L1.tcl

set target_signal_hier "harness.xx.xx"

# 获取指定信号的驱动信号的层级关系并保存到文件
proc get_driver_save { file_id target_hier_in } {
  set target_hier [string map {" " ""} $target_hier_in];
  set handles {}
  ::npi_L1::npi_trace_driver $target_hier "handles"

  set driver_count [llength $handles]
  # puts $file_id "drive signal number: $driver_count"
  if {$driver_count !=0} {
    foreach handle $handles {
      set handle_info [::npi_L1::npi_ut_get_hdl_info $handle]
      set path [lindex [split $handle_info ","] 2]
      set root_path [lindex [split $path "/"] 1]
      set second_path [lindex [split $path "/"] 2]
      if {($root_path != "proj") || ($second_path == "Digital_DMT")} {
        continue
      }
      # puts $file_id $handle_info
      set next_target [lindex [split $handle_info ","] 1]
      set next_target_hier [string map {" " ""} $next_target];
      puts $file_id "\[$target_hier\] <- \[$next_target_hier\]"
      get_driver_save $file_id $next_target_hier
    }
  }
}

# 调用
set file_path "/xx/xx.log"
set file_w_id [open $file_path w]
get_driver_save $file_w_id $target_signal_hier
close $file_w_id