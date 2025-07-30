HEAVY WIP

- The `/var/log/dmesg` file stores boot-time information about the kernel ring buffer, including hardware drivers, kernel status, and bootup events. This log file is reset on every boot and can be viewed using the `dmesg` command.1
    
- The `/var/log/kern.log` file contains kernel-related information and events, including output from `dmesg`. It is useful for diagnosing hardware issues or problems during bootup.1
    
- Kernel logs can also be accessed using the `dmesg` command, which displays the kernel ring buffer messages. This is particularly useful for checking hardware events and driver-related issues.2
    
- The `syslog` system, often found in `/var/log/syslog`, logs a wide range of system-level events, including service and user activity, while `dmesg` focuses more on kernel-specific messages related to hardware and drivers.2
    
- For real-time monitoring of kernel logs, the `tail -f` command can be used, allowing users to view logs as they are generated. However, care must be taken when monitoring log files that are subject to rotation, as this can interrupt the stream.6
    
- The kernel log levels determine the severity of messages displayed on the console. These levels range from 0 (emergency) to 7 (debug), and they can be adjusted using the `/proc/sys/kernel/printk` file or by modifying the kernel command-line parameters.4
    
- In some cases, the `earlycon` feature can be used to capture kernel logs before the normal console is initialized, which is particularly useful for debugging issues that occur during early boot stages.