#!/usr/bin/env python
# Script by Steven Grove (@sigwo)
#           www.sigwo.com
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Date: 09-01-13

import sys

# Get address string and CIDR string from command line
xaddr = raw_input("IP address: ")
xcidr = raw_input("CIDR notation, NO / mark!: ")
addr = xaddr.split('.')
cidr = int(xcidr)

# Initialize the netmask and calculate based on CIDR mask
mask = [0, 0, 0, 0]
for i in range(cidr):
    mask[i/8] = mask[i/8] + (1 << (7 - i % 8))

# Initialize net and binary and netmask with addr to get network
net = []
for i in range(4):
    net.append(int(addr[i]) & mask[i])

# Duplicate net into broad array, gather host bits, and generate broadcast
broad = list(net)
brange = 32 - cidr
for i in range(brange):
    broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))

#This gives you useable hosts for the given subnet
xhost = 2 ** brange - 2
host = "{:,}".format(xhost)

#o1.o2.o3.o4 is the X.X.X.X makeup of an IP address
o1 = broad[0] - net[0]
o2 = broad[1] - net[1]
o3 = broad[2] - net[2]
o4 = broad[3] - net[3]

#need to build wildcard mask for doing ospf and ACL operations
#need to validate input of IP address (ipaddress module?)
#if there is less than /24, need to * by the power of 2
#how in the fuck do i do that? 

# Print information, mapping integer lists to strings for easy printing
print "Address: " , xaddr
print "Netmask: " , ".".join(map(str, mask))
print "Network: " , ".".join(map(str, net))
print "Usable IPs: " , host
print "Broadcast: " , ".".join(map(str, broad))
