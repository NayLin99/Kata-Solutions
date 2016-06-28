"""
Kata: IPv4 Parser (6 kyu)

Description:
Problem Statement

Write a function that takes two string parameters, an IP (v4) address and a subnet mask, and returns two strings: the network block, and the host identifier.

The function does not need to support CIDR notation.
Description

A single IP address with subnet mask actually specifies several addresses: a network block, and a host identifier, and a broadcast address. These addresses can be calculated using a bitwise AND operation on each bit.

(The broadcast address is not used in this kata.)
Example

A computer on a simple home network might have the following IP and subnet mask:

IP: 192.168.2.1
Subnet: 255.255.255.0
(CIDR Notation: 192.168.2.1 /24)

In this example, the network block is: 192.168.2.0. And the host identifier is: 0.0.0.1.
bitwise AND

To calculate the network block and host identifier the bits in each octet are ANDed together. When the result of the AND operation is '1', the bit specifies a network address (instead of a host address).

To compare the first octet in our example above, convert both the numbers to binary and perform an AND operation on each bit:

11000000 (192 in binary)
11111111 (255 in binary)
--------------------------- (AND each bit)
11000000 (192 in binary)

So in the first octet, '192' is part of the network address. The host identifier is simply '0'.

For more information see the Subnetwork article on Wikipedia.

URL: https://www.codewars.com/kata/ipv4-parser
"""

# Write a function that takes two string parameters, an IP (v4) address and
# a subnet mask, and returns two strings: the network block,
# and the host identifier.

# For example:
# >>> print ipv4__parser('192.168.50.1', '255.255.255.0')
# ('192.168.50.0', '0.0.0.1')

def ipv4__parser(ip_addr, mask):
    ip_list = ip_addr.split('.')
    mask_list = mask.split('.')
    net_list = []
    host_list = []
    for i in xrange(4):
        net_list.append(str(int(ip_list[i]) & int(mask_list[i])))
        host_list.append(str(int(ip_list[i]) & ~int(mask_list[i])))
    net_addr = '.'.join(net_list)
    host_addr = '.'.join(host_list)
    return net_addr, host_addr