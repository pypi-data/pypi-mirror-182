#!/bin/sh
#
# Finding ID:	
# Version: mount_option_boot_noexec
# SRG ID:	
# Finding Level:	medium
#
# Rule Summary:
#       The noexec mount option can be used to prevent binaries
#       from being executed out of /boot.
#
# Identifiers:
#   - CCE-81033-3
#
# References:
#   - BP28(R12)
#   - CCI-000366
#   - CIP-003-8 R5.1.1
#   - CIP-003-8 R5.3
#   - CIP-004-6 R2.3
#   - CIP-007-3 R2.1
#   - CIP-007-3 R2.2
#   - CIP-007-3 R2.3
#   - CIP-007-3 R5.1
#   - CIP-007-3 R5.1.1
#   - CIP-007-3 R5.1.2
#   - CM-7(a)
#   - CM-7(b)
#   - CM-6(a)
#   - AC-6
#   - AC-6(1)
#   - MP-7
#   - PR.IP-1
#   - PR.PT-2
#   - PR.PT-3
#   - SRG-OS-000368-GPOS-00154
#   - SRG-OS-000480-GPOS-00227
#   - RHEL-08-010571
#   - SV-230300r743959_rule
#
#################################################################
# Standard outputter function
diag_out() {
   echo "${1}"
}

diag_out "--------------------------------------"
diag_out "STIG Finding ID: mount_options_boot"
diag_out "   Set nosuid mount-options on /boot"
diag_out "   to prevent abuses."
diag_out "--------------------------------------"
