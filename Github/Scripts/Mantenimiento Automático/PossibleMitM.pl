#!/usr/bin/perl

use strict;
use warnings;

my $arp_table = `arp -a`;

if ($arp_table =~ /([0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2}/) {
    print "Possible MITM attack detected.\n";
} else {
    print "No MITM attack detected.\n";
}