#!/usr/bin/env python
#
# v02.11 BETA
#
# by Steven Grove (@sigwo)
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
import os
#from blessings import Terminal

# Going to set up colors for a future project, not completed yet
#term = Terminal()

# Get address string and CIDR string from command line
xaddr = raw_input("IP address: ") # need to validate input of IP address 
xcidr = raw_input("CIDR notation, NO / mark!: ")
addr = xaddr.split('.')
cidr = int(xcidr)

# Initialize the netmask and calculate based on CIDR mask
mask = [0, 0, 0, 0]
for i in range(cidr):
    mask[i/8] = mask[i/8] + (1 << (7 - i % 8)) 

# Initialize net and binary and netmask (net) with addr to get network
net = []
for i in range(4):
    net.append(int(addr[i]) & mask[i])

# Duplicate net into broad array, gather host bits, and generate broadcast
broad = list(net)
brange = 32 - cidr
for i in range(brange):
    broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))

# This gives you usable hosts for the given subnet
xhost = 2 ** brange - 2
host = "{:,}".format(xhost)

# Initialize o for wildcard mask (imask) with broadcast - net 
o = [0, 0, 0, 0]
for i in range(4):
	o[i] = broad[i] - net[i]

# This gives the wildcard mask for the given subnet	
imask = []
for i in range (4):
	imask.append(int(o[i]) & broad[i])

# Print information, mapping integer lists to strings for easy printing
print 'Here are your results:..............'
print "Address: " , xaddr
print "Netmask: " , ".".join(map(str, mask))
print "Wildcard Mask: " , ".".join(map(str, imask))
print "Network: " , ".".join(map(str, net))
print "Usable IPs: " , host
print "Broadcast: " , ".".join(map(str, broad))

raw_input("Press any key to exit...")
