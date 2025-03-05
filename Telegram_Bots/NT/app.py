from random import choice


def main():
    mode = False
    print(" ---  Welcome to my app.  ---")
    manage(mode)
    input(" --- Press enter to exit ---\n")


def manage(mode):
    print(" ----------------------------")
    m = input(" --- Do you want to play (y/n)\n --- Your answer: ")
    while m not in ['y', 'n', 'admin']:
        m = input(" --- Do you want to play (y/n)\n --- Your answer: ")
    else:
        if m == 'admin':
            d = load(data)
            tests = test_reader(d)
            res = input('#: ')
            while res != '-q':
                if res == "":
                    print("# -help:\n# -test <n>: from n, 10 tests.\n# -q : for quit")
                    res = input('#: ')
                elif res[:5] == "-test":
                    try:
                        res = (res.split(' '))[1]
                        res = int(res)
                    except:
                        res = 0
                    test_first_n(tests, res)
                    res = input('#: ')
            else:
                manage(mode)
        elif m == 'y':
            if not mode:
                print(" | Let's start with trial ...")
                print("-----------------------------")
                d = load(data_3)
                tests = test_reader(d)
                test(tests, 3)
                print(" | Trial expired!")
                mode = True
            print("-----------------------------")
            key = input(" | Please enter authorization key: ")
            if key == 'rete':
                print("-----------------------------")
                d = load(data)
                tests = test_reader(d)
                test(tests, 10)
                manage(mode)
            else:
                print(" --- Oops, incorrect key!")


def test(tests, n):
    for i in random_test(tests, n):
        print(f" | {i['question']}")
        i['options'].append(i['correct'])
        count = ord('A')
        op = option_gen(i['options'])
        for j in op:
            if len(j) <= 90:
                print(f" | \t{chr(count)}) {j}")
            else:
                print(f" | \t{chr(count)}) {j[:91]}\n | \t{j[91:]}")
            count += 1
        res = input(" | Your answer: ")
        while res not in ['A', 'B', 'C', 'D']:
            res = input(" | Try again\n | Your answer: ")
        else:
            count = ord('A')
            for j in op:
                if j == i['correct']:
                    if chr(count) == res:
                        if len(j) <= 90:
                            print(f" | Correct!\n | Result: {chr(count)}) {j}\n -----------------------------")
                        else:
                            print(f" | Correct!\n | Result: {chr(count)}) {j[:91]}\n | {j[91:]}\n -----------------------------")
                    else:
                        if len(j) <= 90:
                            print(f" | Correct!\n | Result: {chr(count)}) {j}\n -----------------------------")
                        else:
                            print(f" | Correct!\n | Result: {chr(count)}) {j[:91]}\n | {j[91:]}\n -----------------------------")
                else:
                    count += 1


def random_test(tests, n):
    temp = list()
    for i in range(n):
        temp1 = choice(tests)
        temp.append(temp1)
        tests.remove(temp1)
    return temp


def test_first_n(tests, n):
    for i in tests[n:n + 10]:
        print(f" | {i['question']}")
        i['options'].append(i['correct'])
        count = ord('A')
        op = option_gen(i['options'])
        for j in op:
            print(f" | \t{chr(count)}) {j}")
            count += 1
        res = input(" | Your answer: ")
        while res not in ['A', 'B', 'C', 'D']:
            res = input(" | Try again\n | Your answer: ")
        else:
            count = ord('A')
            for j in op:
                if j == i['correct']:
                    if chr(count) == res:
                        print(f" | Correct!\n | Result: {chr(count)}) {j}\n -----------------------------")
                    else:
                        print(f" | Incorrect!\n | Result: {chr(count)}) {j}\n -----------------------------")
                else:
                    count += 1


def option_gen(options: list):
    temp = list()
    for i in range(len(options)):
        temp1 = choice(options)
        temp.append(temp1)
        options.remove(temp1)
    return temp


def test_reader(data):
    objs = list()
    obj = {'question': "", 'correct': "", 'options': list()}
    for i in data:
        if i[0] == '$':
            obj['question'] = i[1:]
        elif i[0] == '*':
            obj['correct'] = i[1:]
        elif i[-1] == '#':
            obj['options'].append(i[:-1])
            objs.append(obj)
            obj = {'question': "", 'correct': "", 'options': list()}
        else:
            obj['options'].append(i)
    return objs


def load(data):
    data = data.split('\n')
    return data


data_3 = """$In the fully operational OSPF protocol, all routers have in memory:
*The database describing the area to which they belong
The same tree of optimal routes
The same database describing the entire AS
A Distance Vector set of all neighboring routers#
$Filtering table of a VLAN:
*It can be updated manually or automatically with appropriate protocols
It can only be updated manually
Contains only local network Ips#
$The Frequency Reuse in a cellular network refers to
*The reuse of the same frequency in different cells that are sufficiently distant
The reuse of frequencies usually adopted for other services (for example, TV broadcasting)
The reuse of the same frequency to send consecutive text messages (SMS)
The reuse of the same frequency for all the phone calls made by a terminal#"""

data = """$In the fully operational OSPF protocol, all routers have in memory:
*The database describing the area to which they belong
The same tree of optimal routes
The same database describing the entire AS
A Distance Vector set of all neighboring routers#
$Filtering table of a VLAN:
*It can be updated manually or automatically with appropriate protocols
It can only be updated manually
Contains only local network Ips#
$The Frequency Reuse in a cellular network refers to
*The reuse of the same frequency in different cells that are sufficiently distant
The reuse of frequencies usually adopted for other services (for example, TV broadcasting)
The reuse of the same frequency to send consecutive text messages (SMS)
The reuse of the same frequency for all the phone calls made by a terminal#
$When an IP router with complete multicast service support receives a packet related to a given multicast group
*Sends out a copy of the packet on all the ports useful to reach the destinations belonging to the multicast
Discards the packet because it’s not possible to offer multicast services over an IP network
Sends out a copy of the packets on all the ports.
Sends out a copy of the packet on all the ports. except the one through which the packet received#
$The configuration of a switch port in access mode is used for
*Assigning a packet received on that port to a specific VLAN
Allowing the access to the switch only to specific flows that are not considered match
Enabling the access to the network
Assigning a packet sent through that port to a specific VLAN#
$The basic ideal of MPLS (Multi-Protocol Label Switching) consists in
*Associating a label to each packet so that network nodes can use it to determine how to process such packet
Inserting a label in IP packets so that network nodes can use it to determine the path the packet must follow
Inserting a label layer two frames so that network nodes can use it to identify the various higher-layer protocols (multi-protocol) encapsulated in the frame
Association a label to each packet so that the destination can identify the data flow the packet belongs to. Independently of the protocol being used (multi- protocol)#
$An ARP Request that a host with IP address 130.192.10.1/24 sends to learn the MAC address of a host with IP address 130.192.10.200
*Arrives at the destination if the two hosts are connected by means of an Ethernet switch, ignoring possible failures of links and devices involved
Never arrives at the destination
Actually, the ARP Request is not sent because the destination host is outside the IP network of the source
Always arrives at the destination, ignoring possible failures of links and devices involved#
$A network interface with both an IPv4 and an IPv6 address can receive:
*Both IPv4 and IPv6 packets
Only IPv4 packets encapsulated in IPv6, according to the approach called "tunneling"
Only IPv6 packets, since in such kind of configuration the operating system considers IPv4 as obsolete
Only IPv6 packets encapsulated in IPv4, according to the approach called "tunneling"#
$Which of the following choices is not an Adaptive Routing algorithm?
*Selective Flooding
Isolated Routing
Link State
Centralized Routing#
$The Duplicate Address Detection (DAD) procedure
*Is used in IPv6 in order to check that the IPv6 address selected for a host is not already in use
Is used in IPv6 In order to check that a host could also acquire an IPv4 address
Is used in IPv6 in order to check that the MAC address selected for a host is not already in use
Is used in IPv4 in order to check that a host could also acquire an IPv6 address#
$The term handover in cellular networks refers to
*The movement of a mobile terminal from a cell to another without the interruption of an active communication (eg. a call)
The movement of a mobile terminal from a cell to another, even if in that moment there are no active communications
The use of a mobile terminal in the network of a different operator with respect to the one the SIM card installed in the terminal belongs to
The turn-on of the mobile terminal after a long period of inactivity#
$In IEEE 802.11 networks, the -hidden terminal problem- refers to
*the possibility that two or more wireless nodes can interfere with each other without knowing it
a security threat caused by an Intruder in the BSS
a failure in the association to an Access Pont during the passive scanning procedure
the use of the same MAC address by more than one node to the same BSS#
$OSPF-TE and ISIS-TE include enhancements to traditional routing protocols OSPF and ISIS that have been standardized in the context of MPLS in order to
*Enable the distribution of additional information (named constrained data) in support of constraint based routing.
Include adequate fields in routing messages to support explicit routing.
Allow the independence of control plane and data plane in MPLS routers, which ultimately enables traffic engineering.
Ensure faster convergence and enhanced stability.#
$In the LTE core network, packets are routed to/from the Access network by:
*The Serving Gateway (SGW)
The Mobility Management Entity (MME)
The eNodeB
The Packet Data Network Gateway (PGW)#
$The Timing Advance in the GSM is
*The beginning of the transmission at a mobile terminal before the beginning of its assigned time-slot
The capability of a mobile terminal to operate in different time zones
The beginning of the transmission at a mobile terminal after the beginning of its assigned time-slot
The beginning of the transmission at a mobile terminal before the creation of the Stand-alone Dedicated Control Channel (SDCCH)#
$when a MPLS frame has multiple labels, routers:
*only process the next eternal label to decide how to forward the frame
only can swap the next external and the next label to each other
only process the next internal label to decide how to forward the frame
can swap any of the labels#
$The entries of the filtering database of an Ethernet switch
*Have a lifetime, which generally can be set by the switch administrator
Have a lifetime, which varies over time, depending on the number of received frames
Have all an infinite lifetime
Have a lifetime, which is always less than 1 second in order to properly manage device mobility#
$The Layer 3 VPN (virtual private network) solutions based on MPLS are characterized by
*A good level of automation and integration between the public backbone and private networks
Particularly high security thanks to the deployment of cryptographic techniques
A mix of Layer 2 and Layer 3 tunnelling mechanisms
Layer 3 tunneling mechanisms, namely within IP packets#
$VPNs (virtual private networks) are used to
*Transport private traffic through a shared infrastructure while creating the same conditions the traffic would undergo through a private infrastructure
Divide a corporate local area network in a set of separate subnets, each for a different corporate function (e.g., sales, procurement, engineering, marketing)
Partition a private network (for example the one of a parent company with various subsidiaries) in multiple networks virtually separated#
$One of the protocols used in MPLS for label distribution is:
*BGP
L2TP
OSPF
IS-IS#
$An Autonomous System:
*is a subnet configured by leveraging the static routing
is identified by means of a 4 bytes long ID assigned by the CSA
is a set of subnets with a short topological proximity and managed by a single organization unit
is identified by means of a 4 bytes long ID automatically computed by the BGP#
$In MPLS (unlike in IP) support for scalable traffic engineering is specifically enabled by
*The forwarding information in the data plane (e.g., the forwarding table) not being automatically updated when the routing information (e.g., The routing table) changes in the control plane
The availability of efficient label distribution protocols
The deployment of a unified control plane
The deployment of dynamic and distributed routing protocols#
$Select the correct response
*None of the options
End to end VPN is always better than site to site VPN
Firewall and IDS cannot be placed inside a network protected by a VPN gateway
Skewed channel is a type of IPsec tunnel#
$Two stations A and B are interconnected via an Ethernet switch S. The MAC address of the network card of S to which station A is connected is used as the destination MAC address in an ethernet frame
*Sent from A to S, for example for management or configuration purposes
Sent from B to A
Sent from To to a destination outside the network
Sent from A to B#
$One of the reasons that are favoring the spread of the IPv6 protocol is
*The possible inefficiency of the private IPv4 addressing
The more and more widespread need to use multicast applications
The low inclination of network operators to modify the configuration of their own networks
The lack of MAC addresses#
$When an IPv6 host needs to learn the MAC address associated to a given IPv6 address
*
 *It can send a specific ICMPv6 message in multicast over the network
 It can send a specific ICMPv6 message in unicast over the network
 It can send an ARP Request in broadcast over the network
 It can send a specific ICMPv6 message in broadcast over the network#
$The IPv6 Extension Headers are
*Header chains that can be added to the main IPv6 header in order to offer additional features
Header chains that can be added to the main IPv6 header in order to move to the network layer some features that are typically of the transport layer (e.g., the transmission of acknowledges)
Padding techniques adopted to make the IPv6 packet of fixed size equal to 40 bytes
Padding techniques adopted to fix the size of the layer 2 frame containing the IPv6 packet#
$A host A with IP address 130.192.225.79/24 sends an ARP Request on the local network in order to learn the MAC address of a host with IP address 130.192.225.1/26. The corresponding ARP Reply sent from B
*Is sent to the MAC address of A
Is sent to the MAC address of B's default gateway, because A is outside the IP network of B
Is not sent
Arrives to A only if the network is based on a shared medium (e.g., a Ethernet hub)#
$An IPSec-based VPN (Virtual Private Network)
*Deploys tunneling to allow encryption and/or authentication of IP packets exchanged by corporate hosts
Requires that the end points support the IPSec protocol
Requires that the involved Gateway supports the IPsec protocol
The encryption is mandatory, while the authentication is optional#
$When the link between two MPLS routers deploys a layer 2 protocol that supports virtual connections (such as ATM and Frame Relay)
*The most external MPLS label is carried inside the layer 2 header.
Routing protocols specified for the given layer 2 protocol must be deployed (for example, a routing protocol of the ATM standard).
Labels can be bound only to FECs that include layer 2 destination identifiers (e.g., ATM addresses)
It is not possible to use more than one label for each packet.#
$SSL-based VPN (Virtual Private Network) solutions are widely deployed because
*They do not have any problems when packets go through a NAT (Network Address Translation) function on their path to their destination.
They are the only VPN solutions providing a robust packet encryption and authentication functionality.
Allow packets to be encrypted and authenticated without the need of negotiating cryptographic keys.
Allow the layer 3 (network layer) header to be encrypted and authenticated.#
$LSP (Label Switched Path) setup in MPLS (Multi-Protocol Label Switching) implies that
*Routers connected at the ends of a link share which label should be prepended to packets belonging to the LSP.
The hosts sending and receiving packets belonging to the LSP support MPLS.
Routers at the two ends of the LSP (Label Edge Routers) directly exchange routing information.
The upstream router on a link communicates to the downstream router which label should be prepended to packets belonging to the LSP.#
$The Random Access Channel (RACH) in a GSM network is used
*By mobile terminals, for requesting dedicated communication channels to the network
By mobile terminals for sending voice samples by means of a Slotted-Aloha technique for the medium access
By the network, for offering dedicated communication channels to mobile terminals
By mobile terminals for sending voice samples by means of a CSMA technique for the medium access#
$The application of Frequency Hopping (FH) in a GSM network results in
*An increase of the communication quality, but with a reduction of the maximum number of users the cell can serve
An increase of the maximum number of users the cell can serve, but with a reduction of the communication quality
A reduction of both the communication quality and the maximum number of users the cell can serve
An increase of both the communication quality and the maximum number of users the cell can serve#
$In the 6PE solution packets traveling through the MPLS backbone have two labels;
*The external label is used by internal (P) routers to forward packets towards a PE router.
The internal label is used by internal (P) routers to forward packets towards an IPv6 destination.
The external label is used by internal (P) routers to forward packets towards an IPv6 destination.
The internal label is used by internal (P) routers to forward packets towards a PE router.#
$When an IPv6 host needs to learn the MAC address associated to a given IPv6 address
*It can send a specific ICMPv6 message in multicast over the network
It can send a specific ICMPv6 message in unicast over the network
It can send an ARP Request in broadcast over the network
It can send a specific ICMPv6 message in broadcast over the network#
$One of the main strengths of the IPv6 protocol is
*The large size of the addressing space
The possibility to use 10Gb/s channels, a feature not available in IPv4
The possibility to enable a routing mechanism based on names and no longer on addresses
The encryption of the packet payload, available by default for all the packets sent by a host#
$The paging procedure in a cellular network is used for
*Notifying the mobile terminal that it has to be contacted
Notifying the mobile terminal that it is going to change the cell
Forcing the mobile terminal to apply proper memory sharing policies
Sending an SMS#
$The IGMP protocol
*Allows a host to communicate to routers in the network its own interest in receiving the traffic related to a given multicast group
Allows a host to communicate to other hosts belonging to a given multicast group its own interest in entering the group
Allows a router to communicate to other routers in the Internet network its own interest in receiving the traffic related to a given multicast group
Carries the multicast traffic generated by hosts#
$With respect to previous solutions, The Long Term Evolution (LTE) technology is characterized, among the other things, by
*The usage of an "all-IP" network architecture with shared communication channels
The usage of switching technique based on virtual circuits
The usage of a circuit switching technique
The usage of mobile terminals that are able to use the IP protocol for sending data#
$The Integrated Services (IntServ) solution has been standardized to
*Allow applications to request to and receive from the network the quality of service they need.
Mark packets as belonging to a specific class of service so that they can receive the most suitable service.
Integrate within the network traditional IP routers and MPLS (Multi-Protocol Label Switching) Label Switch Routers (LSRs), thanks to the common deployment of RSVP (Resource ReSerVation Protocol).
Enable the integrated deployment of IP routers and Ethernet switches to guarantee network connectivity.#
$Among the four proposed alternatives, which is the smallest valid aggregation that can represent the IP networks 130.192.1.0/24 and 130.192.2.0/24 in a routing table?
*0.0.0.0/0
130.192.1.0/23
130.192.1.0/23
130.192.0.0/23#
$The static routing
*Consists in the network administrator manually configuring routing information in each router
It is an obsolete technology no longer deployed since dynamic routing is preferred over it
Consists in one network node computing routes for other network nodes and providing the computed routes to them
Consists in the automatic learning of routes without exchanging routing information#
$In order to setup a label switched path (LSP)
*MPLS routers on the path must perform a mapping operation
The same layer-two protocol must be deployed on all links on the path
Final destinations of IP packets traveling on the LSP must support MPLS
MPLS routers on the path must deploy the same protocol for label distribution#
$The difference between link state and distance vector routing algorithms can be summarized as follows
*Link state algorithms send local information to all nodes in the network; distance vector algorithms send global information only to neighboring nodes
Link state algorithms send local information only to neighboring nodes; distance vector algorithms send global information to all nodes in the network
Link state algorithms send global information to all nodes in the network; distance vector algorithms send local information only to neighboring nodes#
$The Integrated IS-IS protocol
*Is a protocol based on the link state routing algorithm widely used in large networks
Is a protocol used by Ethernet switches to create a routing tree in the network (spanning tree) removing closed paths (i.e., loops)
Is an obsolete routing protocol no longer used due to its low performanc
Is a protocol derived as an evolution of BGP for the exchange of information between routers belonging to different autonomous systems#
$Which of these techniques is not a solution for the IPv4-IPv6 transition?
*6mix4
Teredo
6to4
6over4#
$The IPv6 address FE80::0201:06FF:FEA5:3A4C is:
*An address that can be used on a host with MAC address 00:01:06:A5:3A:4C for communicating with another host on the same link
An address currently not available in IPv6
An address that can be used by more than one device on the same link
An address that can be used on a server with MAC address 00:01:06:A5:3A:4C to offer a service on the public IPv6 Internet#
$RIP is characterized by
*Frequent instability and inclination to create circular forwarding paths (i.e., routing loops)
The suitability to both interdomain and intradomain routing
The possibility to operate on large networks thank to its capability to function in a hierarchical way
The usage of a link state routing algorithm#
$The ICMPv6 Router Advertisement packet
*Enables device autoconfiguration without a DHCP protocol intervention
Is sent as a reply to an ICMPv6 Neighbor Solicitation packet
Is a broadcast packet
Is sent periodically by a router to all the other routers of the Internet network#
$The Interface ID of an IPv6 address
*Can be arbitrarily selected, sometimes it is derived from the MAC address of the interface
Is the same for all devices within the same link
Is assigned by the ISP according to a hierarchical schema
Is assigned by the network administrator according to a hierarchical schema#
$The main contribution to the latency experienced in the nodes of a heavily loaded packet network is given by
*The time spent in buffers while waiting for resources occupied by other packets to become available (for example, the transmission capacity of a link).
The time needed to process the packet.
The time taken to transmit the packet on an output link (transmission delay).
The time taken to locate, in the routing table or in the forwarding table, the information need to forward the packet.#
$A device equipped with the NAT64 functionality is able to
*Replace the Ipv6 header of a packet with an ipv4 one, and vice versa
Operate on 64-bit ip address
convert an IPv6 packet in an ethernet frame
replace the ipv6 destination address in the ipv6 header of a packet with an ipv4 one, and vice versa#
$The Mapping Address and Port (MAP) technique for the IPv4-IPv6 transition is based on
*The utilization, on the Customer Premises Equipment (CPE), of an IPv6 address derived from the IPv4 address and the Port Set ID assigned by the provider to the customer
The utilization, on the Border Relay, of an IPv6 address derived from the IPv4 address and the Port Set ID assigned by the provider to the various customers
The utilization, on the Customer Premises Equipment (CPE), of an IPv6 address selected among a fixed set of addresses defined by a standard
The utilization, on the Customer Premises Equipment (CPE), of an IPv6 address which varies on the basis of the IPv4 destination address that the user would like to reach#
$Indicate the false claim among the below statements about the Link State algorithm
*
 The Link State algorithm converges faster than the Distance Vector algorithm
 *The RIP (Routing Information Protocol) protocol is based on the Link State algorithm
 The Link State algorithm seldom generates loops
 The Link State algorithm exchanges less information than the Distance Vector algorithm.#
$fixing cell size G and DECREASING radius R
*capacity increase
capacity decrease
capacity remains same#
$LTE uses which channel access?
*ofdma
fdma
cdma
tdma#
$What is a main function of NSS(Network Switching Subsystem)?
*Authentication
Paging
Resource allocation#
$One of the main properties of the new 5G infrastructure is
*
 the use of virtualization techniques on mobile terminals in order to properly support novel applications
 the come back to the secret switching technology in order to guarantee a proper quality of service which is key in a new generation mobile network
 the use of software emulators and simulators for the design of the mobile operators’ network infrastructures which for this reason are usually referred to as software defined networks
 *the joint use of virtualization techniques and flexible solutions for the network control, with the aim of dividing available network resources in an efficient and effective way#
$Two IP networks 130.192.0.0/24 and 130.192.2.0/24 can be aggregated in:
*130.192.0.0/2
130.192.0.0/23
130.192.2.0/23
They cannot be aggregated#
$In an IPv4 network
*A host can be reached by a multicast packet related to a specific group even if it did not join that group before
A host is reached by a multicast packet related to a specific group only if it joined that group, whichever is the layer 2 technology adopted in the network
A host always deliveries to the application layer all the multicast packets received
A host cannot understand a multicast IPv4 packet#
$The ICMPv6 Router Advertisement packet
*Are defined in such a way that they are globally unique with high probability, but they cannot anyway be used on a global level
Enables device autoconfiguration without a DHCP protocol intervention
Is sent as a reply to an ICMPv6 Neighbor Solicitation packet
Is sent periodically by a router to all the other routers of the Internet network
Is a broadcast packet$IPv6 Private addresses
Are used only for on-link communications
Are used only on routers
Are used to interconnect private networks through a public network#
$In the DS-Lite solution for the IPv4-IPv6 transition
*The NAT feature is implemented for all users on proper ISP devices
The NAT feature is implemented on the user CPE
The NAT feature is implemented on both the CPE and the ISP devices
The NAT feature is not available#
$Two hosts connected to an Ethernet switch
*Can communicate even if they belong to different VLANs, it depends on the network configuration
Can communicate only if they belong to the same VLAN, for any network configuration
Must be able to communicate without an intermediate router, always
Cannot communicate through an intermediate router since they are connected to the same switch#
$The metric (cost) used by a routing algorithm
*Expresses the weight assigned to a link (channel) in the path selection
Expresses the probability to use the shortest path
Expresses the complexity of the algorithm in performing the path computation#
$The difference between link state and distance vector routing algorithms can be summarized as follows:
*Link state algorithms send local information to all nodes in the network; distance vector algorithms send global information only to neighboring nodes
Link state algorithms send global information to all nodes in the network; distance vector algorithms send local information only to neighboring nodes
Link state algorithms send local information only to neighboring nodes; distance vector algorithms send global information to all nodes in the network#
$RSVP (Resource Reservation Protocol) allows:
*Routers to know the requirements of an application in terms of quality of service
To limit the delay variation (jitter) experienced by packets in routers
Servers to reserve computing resources in their shared processors
To monitor delay and loss experienced in the network by packets of multimedia applications#
$The importance of MPLS (multi-protocol label switching) in today's and future computer networks stems from the possibility to
*Have a single control plan for different switching technologies
Realize switches with specific support to guarantee quality of service
Realize devices that can operate without needing to be configured
Balance traffic across a server farm#
$The operations that an MPLS router can perform on labels are:
*Add a label in most external position of the MPLS header (PUSH), remove a label from most external position in the MPLS header (POP), change the content of the external label (SWAP)
Add a label in any position of the MPLS header (PUSH), remove a label from any position in the MPLS header (POP), change the content of any label (SWAP)
Add a label only if there are no others in the MPLS header (only one label is allowed) (PUSH), remove the only allowed label from the MPLS header (POP) upon the packet exiting the MPLS network, change the content of the label (SWAP)
Labels cannot be changed by routers#
$The IPsec "Tunnel Mode" encompasses the encryption of
*The IP header, TCP/UDP header, and payload of the internal packet
Only the payload of the internal packet
Only the TCP/UDP header and payload#
$Two hosts A and B belong to the same physical network and have IP addresses 130.192.1.1/25 and 130.192.1.129/24, respectively.
*A can communicate with B only by means of a router
A directly communicates with B and vice versa
A directly communicates with B but not vice versa
A cannot communicate with B#
$Two IP networks 130.192.0.0/24 and 130.192.2.0/24 can be aggregated in:
*130.192.0.0/22
130.192.0.0/23
130.192.2.0/23
They cannot be aggregated#
$The IGMP protocol
*Allows an IPv4 router to discover which multicast groups are present in a directly connected network
Allows an IPv4 host to create a new multicast group
Allows an IPv4 router to discover which multicast groups are active in the Internet network at a given instant of time
Is a new version of the ICMP protocol#
$In an IPv4 network
*A host can be reached by a multicast packet related to a specific group even if it did not join that group before
A host is reached by a multicast packet related to a specific group only if it joined that group, whichever is the layer 2 technology adopted in the network
A host always deliveries to the application layer all the multicast packets received
A host cannot understand a multicast IPv4 packet#
$The Neighbor Discovery procedure in IPv6
*Is based on a multicast ICMPv6 packet
Is based on a broadcast ICMPv6 packet
Is based on ARPv6
Needs the network to support IPv4#
$IPv6 Private addresses
*Are defined in such a way that they are globally unique with high probability, but they cannot anyway be used on a global level
Are used only for on-link communications
Are used only on routers
Are used to interconnect private networks through a public network#
$IPv6 Site Local addresses
*Are deprecated but they can be used in IPv6 networks
Are automatically setup by IPv6 devices for on-link communications
Are assigned by a central authority that guarantees their global uniqueness
Do not exist#
$The IPv6 address FE80::0201:06FF:FEA5:3A4C is:
*An address that can be used on a host with MAC address 00:01:06:A5:3A:4C for communicating with another host on the same link
An address that can be used on a server with MAC address 00:01:06:A5:3A:4C to offer a service on the public IPv6 Internet
An address that can be used by more than one device on the same link
An address currently not available in IPv6#
$Which of these techniques is not a solution for the IPv4-IPv6 transition?
*6mix4
6over4
6to4
Teredo#
$In the DS-Lite solution for the IPv4-IPv6 transition
*The NAT feature is implemented for all users on proper ISP devices
The NAT feature is implemented on the user CPE
The NAT feature is implemented on both the CPE and the ISP devices
The NAT feature is not available#
$The entries of the filtering database of an Ethernet switch
*Have a lifetime, which generally can be set by the switch administrator
Have all an infinite lifetime
Have a lifetime, which is always less than 1 second in order to properly manage device mobility
Have a lifetime, which varies over time, depending on the number of received frames#
$A consequence of the deployment of VLANs in a local area network is:
*The broadcast traffic is bounded to the VLAN where it has been generated
The creation on virtual interfaces on switches, which, since virtual, cannot have failures
The network security increases as frames are encrypted
Users must be authenticated before connecting to the VLAN#
$Two hosts connected to an Ethernet switch
*Can communicate even if they belong to different VLANs, it depends on the network configuration
Can communicate only if they belong to the same VLAN, for any network configuration
Must be able to communicate without an intermediate router, always
Cannot communicate through an intermediate router since they are connected to the same switch#
$Two hosts connected to a Switched Ethernet network through ports configured in Access mode
*If they belong to different VLANs, it is possible that they can communicate even if they are connected to different switches and ports on switches are configured in Access mode
Can communicate only if they belong to the same VLAN
Cannot communicate
If they belong to different VLANs, they can communicate only if they are connected to different switches and the link between the switches is configured in Trunk mode#
$The metric (cost) used by a routing algorithm
*Expresses the weight assigned to a link (channel) in the path selection
Expresses the probability to use the shortest path
Expresses the complexity of the algorithm in performing the path computation#
$BGP is used in the Internet for
*The exchange of routing information between routers belonging to different autonomous systems
Communicating to neighboring routers the state of the links of a router
Discovering neighboring (bordering) routers on a local are network
Find out the geographic position of a host based on its IP address#
$The difference between link state and distance vector routing algorithms can be summarized as follows:
*Link state algorithms send local information to all nodes in the network; distance vector algorithms send global information only to neighboring nodes
Link state algorithms send global information to all nodes in the network; distancevector algorithms send local information only to neighboring nodes
Link state algorithms send local information only to neighboring nodes; distance vector algorithms send global information to all nodes in the network#
$RIP is characterized by
*Frequent instability and inclination to create circular forwarding paths (i.e., routing loops)
The usage of a link state routing algorithm
The suitability to both interdomain and intradomain routing
The possibility to operate on large networks thank to its capability to function in a hierarchical way#
$The IS-IS protocol
*It is a protocol based on the link state routing algorithm widely used in large networks
Is an obsolete routing protocol no longer used due to its low performance
It is a protocol used by Ethernet switches to create a routing tree in the network (spanning tree) removing closed paths (i.e., loops)
It is a protocol derived as an evolution of BGP for the exchange of information between routers belonging to different autonomous systems#
$RSVP (Resource reSerVation Protocol) allows:
*Routers to know the requirements of an application in terms of quality of service
To limit the delay variation (jitter) experienced by packets in routers
Servers to reserve computing resources in their shared processors
To monitor delay and loss experienced in the network by packets of multimedia applications#
$In DiffServ, a "class of service" identifies:
*A set of packets that are handled the same way by routers (for example, all VoIP traffic)
A set of packets that belong to the same VoIP session
A working mode of border routers that have to classify and mark incoming packets#
$The importance of MPLS (multi-protocol label switching) in today's and future computer networks stems from the possibility to
*Have a single control plan for different switching technologies
Realize switches with specific support to guarantee quality of service
Realize devices that can operate without needing to be configured
Balance traffic across a server farm#
$One of the protocols used in MPLS for label distribution is:
*BGP
OSPF
IS-IS
L2TP#
$In the MPLS (multi-protocol label switching) architecture, LSPs (label switched paths)
*Are set up by network nodes that agree on the labels to be used for packets belonging to a specific forwarding equivalence class (FEC)
Represent alternative paths for forwarding packets towards a given destination kept by a router in its routing table
Are exchanged by routers to create a map of the network
Consist in the shortest path towards a given destination#
$The operations that an MPLS router can perform on labels are:
*Add a label in most external position of the MPLS header (PUSH), remove a label from most external position in the MPLS header (POP), change the content of the external label (SWAP)
Add a label in any position of the MPLS header (PUSH), remove a label from any position in the MPLS header (POP), change the content of any label (SWAP)
Add a label only if there are no others in the MPLS header (only one label is allowed) (PUSH), remove the only allowed label from the MPLS header (POP) upon the packet exiting the MPLS network, change the content of the label (SWAP)
Labels cannot be changed by routers#
$Optical networks are specifically and uniquely characterized by devices capable of:
*Switching an optical channel from an input port to an output port
Transmitting optical signals on optical fiber links
Routing packets by processing their header with optical circuits (rather than electronic ones)
Transporting large amounts of data thanks to their capability of switching traffic according to information contained in a label, carried by a special packet header#
$VPNs (virtual private networks) are used to
*Transport private traffic through a shared infrastructure while creating the same conditions the traffic would undergo through a private infrastructure
Divide a corporate local area network in a set of separate subnets, each for a different corporate function (e.g., sales, procurement, engineering, marketing)
Partition a private network (for example the one of a parent company with various subsidiaries) in multiple networks virtually separated#
$The Layer 3 VPN (virtual private network) solutions based on MPLS are characterized by
*A good level of automation and integration between the public backbone and private networks
Particularly high security thanks to the deployment of cryptographic techniques
Layer 3 tunneling mechanisms, namely within IP packets#
$The IPsec "Tunnel Mode" encompasses the encryption of
*The IP header, TCP/UDP header, and payload of the internal packet
Only the payload of the internal packet
Only the TCP/UDP header and payload
The whole external packet, header included#
$To build a VPN using MPLS , at level 3 according to the peer model, you can:
*Use an appropriately modified version of the BGP.
Use a suitably modified version of the TCP.
Use a suitably modified version of the RIP.
Use an appropriately modified version of the RTP.#
$The GRE protocol aims to:
*Manage the encapsulation of packets to be transported through a tunnel.
Protect packets against eavesdropping.
Authenticate the sender of the packets.
Check the integrity of incoming packets.#
$The GRE protocol is used for:
*Encapsulate packets in other IP headers, so they can be sent over a tunnel.
Ensure the confidentiality of communications.
Ensure the authenticity of packages.
Reserve some bandwidth for communication.#
$PPTP protocol is commonly used for:
*Allow to create a tunnel in an access VPN.
Allowing you to tunnel into an overlay-type site-to-site VPN.
Allowing you to tunnel into a peer-type site-to-site VPN.
Allow you to tunnel into a layer 4 VPN.#
$In a packet traveling over a GRE tunnel , how many headers can there be?
*Two headings, without particular limitations.
Only one, otherwise the addressing is ambiguous.
Two headers, but the internal one can only contain private addresses.
Two headers, but the outer one can only contain private addresses.#
$Why is it useful to use GRE encapsulation protocol as opposed to IP
*Because it is possible to encapsulate lower levels protocols (e.g. data link layers) in IP datagrams.
Because it provides encryption mechanism
Because the resulting packet is shorter.
Because is possible to authenticate the sender.#
$In what situation is it possible for a packet to have two IP headers ?
*The packet is in the public network in transit over an IP tunnel connecting two segments ofan IP-based VPN.
The packet went through an inbound firewall.
The packet is in the public network, having passed through a NAT outbound.
The packet is on the public network after passing through a firewall outbound.#
$In a user station connected to a VPN with centralized access , direct messages to stations outside the VPN pass through:
*The site of the VPN to which the user machine is connected
It is not possible to reach stations outside the VPN.
A specialized router for these packets.
They are sent directly from the user station to the external recipient.#
$The feature of a centralized access VPN is that
*Traffic not directed to the VPN is still passed through the VPN gateway.
User authentication for VPN access is delegated to the ISP.
Traffic not directed to the VPN is not forced to go through the VPN gateway.
User authentication is not done by the VPN gateway.#
$Layer 3 virtual private network ( VPN) solutions across an MPLS backbone are characterized by
*Good level of automation and integration between the public backbone and private networks.
Particularly high levels of security thanks to the use of cryptographic techniques.
Layer 3 tunneling mechanisms, ie inside IP packets.
Direct management by the user, without operator intervention.#
$What is a feature of a layer 3 VPN (virtual private network) implemented using an MPLS network?
*High level of scalability.
High security standards.
It does require a NAT (network address translation) when private addresses are used.
QoS guaranteed for a low travelling across the VPN#
$The solutions for the realization of VPN (virtual private network) of level 3 through a dorsal MPLS are characterized by
*High scalability
Particularly high levels of security
Unlike all the other proposed solutions, they do not require the use of NAT (network address translator) when dealing with private addresses.
The provision of a guaranteed quality service to the traffic passing through the VPN.#
$Why IPsec standard is used in some VPN (virtual private network)?
*It is used to setup a secure tunnels between different sites of the same enterprise using a public network
It is used only to verify the authentication credentials of remote users with a data exchange with an authentication server.
It is only used to allow remote user to send username and password to access the VPN
It is used to overcome problems connected with the use of private networks#
$The IPsec standard is used in VPNs for
*The automatic creation of encrypted connections between company offices over a network public, on which communication is therefore intrinsically unsafe
Verify authentication information provided by remote users through a information with an authentication server
Allow the sending of authentication information (user and psw via challenge) by of users of an access VPN
The creation of tunnels through a public IP network through which it is possible carry packets to a private network regardless of the routing plan used on that private network#
$The so-called VPN (virtual private network) access solutions or virtual dial-up VPN currently most common are based on :
*Tunneling through an IP network.
Dial-up connections.
Using an existing cabling infrastructure to provide wide access services band
New line protocols (data-link layer).#
$What is the distinctive feature of a VPN implementing a overlay model
*The network provider does not know that we are implementing a vpn
The user devices at the edge of the vpn may ignore that we are using a VPN
It is not possible to have a secure connection
I cannot be implemented without the intervention network provider#
$What can be done with a VPN (virtual private network) based on SSL (secure socket layer)?
*It is possible for an enterprise to make available in a secure way some applications aver the corporate network
To distribute, in secure way, over several servers the workload related to a web based application
To implement clusters of private networks
To implement a backbone of an internet service provider for providing an interconnection service, in a simple and effective way#
$What is the goal of PPTP
*To implement access VPN
To implement site to site VPNs
To implement VPN with centralized access
To implement VPN with distributed access.#
$What is the role of GRE protocol?
*It allows to encapsulates a layer 2 frame into an IP packet
It allows to increase the addressing space
It introduces air encryption mechanism for the packets
It allows the encapsulation but it is not possible to encapsulate units of lower layers into a layer 3 packet.#
$What is the typical role of IPSec in VPNs?
*To open a managed secure tunnel across the public internet
To distribute in a secure way the key required by other protocols to open a tunnel
To allow the transmission of authentication information (e.g. username and password) by users of access VPN
To verify the user identity to allow other protocols to open tunnels only with authorized parties.#
$Why access virtual Private networks are used?
*They are used to build a private infrastructure by using a public one
They are used to allow access to public internet using a private access network
They are used to allow an existing cabling infrastructure to provide wide-band services
They are used to connect two sites of an organization by using a dedicated line#
$The virtual private networks (VPN) are used for
*Transporting private traffic over a shared infrastructure creating the same conditions that one would have by using a private infrastructure
Dividing a local area network of a company in a set of different subnetworks for different business activities (sales, purchases, engineering, marketing)
Partitioning a private network (for example the network of the main company with anumber of secondary business units) in different network virtually divided#
$The scheduling algorithms are used:
*In routers, to decide the order in which packets should be transmitted in waiting at an interface
On access routers, to ensure that the traffic generated by a user complies with the traffic profile contracted with your service provider.
In firewalls, to delay packets entering a corporate network from the Internet network with the aim of preventing certain types of security attacks
In routers, to properly schedule the list of configuration commandsgiven by the user in order to minimize the disruption caused by the time needed for application of the changes#
$How QoS is managed in SIP?
*Sip does not provide any mechanism for QS
Is natively used managed by sip
the RTCP protocol is used to obtain QoS
It is optional#
$In the DiffServ architecture , the PHB allows to:
*Treat the various classes of service differently
Monitor the maximum traversal time of a single router for each row through it
Provide the end-to-end guarantee of the QoS required by each stream.
Ensuring the QoS required by each stream passing through a router.#
$What is a feature of the DiffServ (Differentiated Services) architecture?
*Possibility to provide guaranteed QoS for packet row explicitly requesting it.
Sophisticated signaling protocols for resource reservation.
A mechanism to provide different type of treatment to packets belonging to different service classes A.
 Sophisticated signaling protocols to make sure that each row will receive a guaranteed QoS.#
$iffServ differs from IntServ because:
*DiffServ tends to guarantee a maximum traversal time, while IntServ tends to provide a guaranteed minimum bandwidth.
DiffServ tends to provide a guarantee on QoS which IntServ does not give
DiffServ introduces new protocols to allow the reservation of resources for the purpose of get a QoS date.
IntServ tends to rpovide a guarantee on QoS which DiffServ does not give.#
$Where queue scheduling policies are used?
*In a router to decide the order of transmission of the packets waiting at each interfaces
In access routers to make sure that the traffic profile generated by a user is conforming with the agreed with the service provider.
In firewall, to delay packets entering the enterprise network from internet in order to prevent some kinds of attacks
In a router to schedule the list of the configuration commands issued by the user in order to minimize the impact on normal operations caused by the applications of configurations changes.#
$Where scheduling algorithms are used?
*They are used in routers to decide the order of transmission of the pending packets
They are used in access routers to check that the traffic generated by the users is according what they negotiated with the provider.
They are used in firewalls to delay packets entering to an enterprise network in order to lessen risk of denial of services attacks.
They are used in routers to sequence correctly the configuration commands.#
$What is the use of policing mechanisms ?
*They are used by the service provider to verify that the traffic entered by the customer is in accordance with the agreements made.
They are used by the user to agree with the supplier on the level of QoS to be obtained.
They are used by the user to verify that the traffic arriving from the provider complies with the agreements made.
They are used in the various routers to guarantee a maximum crossing time for each of them#
$Algorithm RED (Random Early Deletion)
*Manages the internal queues of routers, starting to discard packets with probability growing when the tail reaches a minimum length
Manages the internal queues of routers by transmitting packets from the various queues in rotation.
Allows the inbound marking of traffics belonging to different classes.
Allows control of the maximum burst size.#
$The IPv6 addressing scheme :
*Provides that the first 64 bits of an address are normally identified as the prefix network, at least on the LANs.
It only provides for addresses uniquely assigned by a responsible body.
Provides for each entity (eg company) to be globally assigned a set of addresses, which become his property for an unlimited time.
It does not foresee the existence of multicast addresses.#
$Stateless autoconfiguration in IPv6 requires:
*It is possible even if there is no server or router present
Un server DHCPv6 (Dynamic Host Configuration Protocol version 6).
A server present on the local network.
A server on the corporate network (intranet).#
$A difference of version 4 IP, version 6:
*It has no broadcast addresses
It does not have an associated ICMP version
It does not allow you to discover the MAC address of another station, knowing its address ROPE.
It has no time-to-live (TTL) field equivalent.#
$In IPV6 protocol, IP packet header
*Includes only fixed size fields that carry the required information in each packet
Is always authenticated through the utilization of proper encryption algorithms in order to increase the security of transmissions.
Has a small size with respect to IPV4, in order to increase the bandwidth efficiency byreducing protocols overhead.
Includes some fields available in IPV4 only as options to offer features that turn to be largely used along the time.#
$What are the differences between the transmission types in IPV4 and IPV6
*IPV4 does not include anycast (included in IPV6) and it does include broadcast (not included in IPV6)
No difference
IPV4 does not include multicast included in IPV6
IPV4 does not include anycast and multicast both included in IPv6#
$Does exist a version of DHCP for IPV6?
*It exists a DHCP IPV6
It does not exist because stateless auto configuration alone solves the same problem.
It does not exist because stateless auto configuration and router advertisement solve the same problem.
It Does not exist because it is more secure it the host is configured manually.#
$Is fragmentation allowed in IPV6?
*Datagrams may only be fragmented by the sender and re-assembled at the final destination
The mechanism is similar to the one included in IPv4
It is not possible to fragment datagrams, both for routers and for the sender
Fragmentation is allowed only in routers whenever necessary.#
$A difference of version 4 IP, version 6:
*It has no variable-length header.
It does not allow you to discover the MAC address of another station, knowing its IP address.
It has no time-to-live (TTL) equivalent.
Disallows the use of IPsec.#
$In IPv6 what disappears from the headers , compared to IPv4?
*The checksum of the header.
The life time of the package.
The sender and recipient addresses.
The indication of which heading is next#
$The link-local addresses
*They are usually built automatically by the station starting from the MAC address of your card, which is prefixed with a predefined prefix.
They are valid within an organization that can use them to assign addresses tomachines in the various subnets of your intranet (they are the counterparts of the private addresses of IPv4).
They cannot be assigned to routers.
They are used to identify machines that perform a certain service (for example server DNS).#
$What is the role of link-local IPV6 address
*It can be used to enable the communication between hosts in the same subnetwork when other type of IPV6 addresses are not available
It is used to physically connect 2 host over a local link
It is the only address that can be used to communicate over a LAN
It is the only address to communicate to routers#
$A link-local address:
* It can be used to allow communication between stations on local links (e.g. a LAN) in the absence of other IPv6 addresses.
 It is used to physically connect two stations on a local link.
 It is the address used by stations on a LAN to exchange data.
 It is used in all communications between local stations.#
$What is the function of the "scope" associated with IPv6 addresses?
*Serves to resolve, in particular cases, the ambiguity regarding the sender.
There is no scope associated with IPv6 addresses.
Used to use global addresses.
It is needed in order to use anycast addresses.#
$What is a feature of the IPv6 addressing scheme?
*Addresses are distributed in order to make it easy to aggregate them in the backbone router forwarding tables.
The whole address is assigned by a single authority.
Multicast addresses are not used.
Variable length addresses are used.#
$In the IPv6 protocol :
*There is the possibility for a station on a network segment to configure itself by listening to Router Advertisement messages.
Routing protocols (eg packet format) do not change with respect to IPv4.
The ARP protocol is incorporated into ICMPv6, but maintains exactly the scheme of previous operation (broadcast request, unicast reply).
Like IPv4, IPv6 has no router reconfiguration mechanisms.#
$What is the feature of IPV6 address?
*They keep the same flexible division between subnet and host fields.
They allow communication between host with IPV4 and IPV6 addresses without additional mechanism
They rigidly organized in network, subnetwork and host fields.
They include a unique broadcast address#
$Which mechanism is used to forward IPV6 packets over the LAN?
*The neighbor discovery mechanism is not used for IPV6 multicast packets because an algorithm exist to map those IPV6 address onto MAC address
A neighbor discovery mechanism is not used because there is an algorithm to map any possible address onto a MAC address.
The neighbor discovery is not used for IPv6 multicast and broadcast packets because an algorithm exists to map those IPV6 address onto MAC address
The neighbor discovery mechanism is used for all the possible types of IPV6 address.#
$What is a feature of stateless auto-configuration in IPv6?
*It uses a standard prefix followed by an host number 64 bit long, derived from the MAC address
It is based on DHCPv6 (Dynamic Host Configuration Protocol version 6)
It is mandatory to have a router in the sub-network to get the network prefix (the most significant 64 bits) with a message of router solicitation.
It is mandatory to have a router in the sub-network to get the network prefix (the most significant 64 bits) with a message of router advertisement.#
$An IPv6 host on reboot will acquire the following address:
*As for the link-local address, it will assume the same IPv6 address as owned before the reboot.
It is not possible to know precisely the address itself, since the IPv6 address it is regenerated each time with a random number as regards the reserved part all'Interface ID.
A FE80 :: / 32 address
The address depends entirely on the configuration it will acquire from its default router.#
$What ENUM standard is used for?
*It is used to call a telephone in the public switched telephone network from a computer, using SIP
It is used to call a sip user from a telephone set connected to the public telephone number
It is used to transmit the voice streams of a sip calls
It is used to implement e-presence in SIP#
$The RTP protocol is capable of:
*Encapsulate the audio / video data with headers containing information about them coding
Limit the variations in delay (jitter) experienced by packets in routers.
Let routers know the traffic profile generated by a station.
Reserve compute resources on servers that share their processors.#
$The RTP protocol is able to:
*Encapsulate audio video data with headers containing encoding information
Limit the variations in delay (jitter) experienced by packets in routers.
Gather information on how the transmission is progressing.
Reserve resources in the network to obtain some QoS.#
$What is one of the possible uses of RTP (Real-time Transport Protocol) ?
*To carry a timestamp related to the block of samples transmitted in a packet
To implement real-time application for industrial plant control.
It can be used in multimedia applications to limit the packet transit time across the network
It is possible to distinguish different streams (e.g. audio + video) addressed to the same host, by means of the field PT (Payload Type).#
$In the RTP protocol , when is it possible to change the encoding of the data carried by a stream?
*It is possible to change the encoding for each packet sent.
Once the audio / video stream transmission has started, it is no longer possible to change the coding
It is possible to change the encoding when an appropriate signaling of is made control using RTCP.
It is possible to change the encoding, only if you are using an RTP mixer.#
$What is possible to do with the RTCP protocol?
*It is possible to monitor the number of losses of a specific low of packets.
It is possible to limit the jitter.
It is possible to communicate to other routers the profile of the traffic generated by a transmitter.
It is possible to reserve resources to obtain guaranteed QoS.#
$Which of the following statement applies to sip trapezoid?
*It is a standard mechanism to setup a call
It is mainly used to sends SUBSCRIBE-NOTIFY (e-presence) message
It is an obsolete mechanism of SIP, since manly current SIP implementations use a more efficient mechanism
It is the standard mechanism to send REGISTER Messages#
$The functions of a voice gateway (or VoIP gateway) include:
*Translate voice streams generated over a packet network (such as via SIP or H.323) into telephone calls on a traditional telephone network (plain old telephone system - POTS).
Forward IP packets between a public IP network and an IP corporate network (intranet).
Encrypt a voice signal from a traditional telephone network firstforwarding over the Internet - notoriously insecure - so that this signal does not can be understood if intercepted.
Translate the SS # 7 telephone reporting into SIP reporting.#
$La telefonia su IP prevede :
*The use of voice gateways to allow communication with users connected to networks traditional (POTS).
Upgrading the IP network cabling to connect each telephone user via optical fiber
To equip each user's computer with voice over IP with telephony software for communicate with other IP telephony users, and a traditional telephone to communicate with traditional telephone users.
The SIP protocol.#
$The SIP messages are characterized by:
*Have, in some cases, a payload consisting of session description protocol).
Don't have a payload, there are just commands / responses and headers.
Have a checksum code that allows error detection.
Have base 2 numerical coding.#
$The main reason why a "telephone" operator like Skype is able to provide a telephone service at very low prices:
*It is due to the fact that the phone calls travel on the IP network (for example ADSL), the costs of which they are already paid by the user when he enters into a "?at" contract and therefore the packages vowels travel virtually "free" for most of their journey
It is due to the fact that it has made interconnection agreements with the Telecom Providers that they pay Skype a fee based on the percentage of traffic generated
It is mainly due to the advertising that is offered with the service.
It is due to having only long distance IP infrastructure, leaving the access infrastructure (much more expensive due to the high capillarity) to third parties, with the consequence of greatly reducing costs.#
$What is a feature of the Session Initialization Protocol (SIP)?
*It is possible to use a server to register a User Agent, so that the server know the mapping between the username and its current IP address.
It is necessary that the media stream is established with the help of server called Media relay.
It is not scalable, because it does not specify how to find users in different domain than the caller.
It is necessary that User Agent is always associated to the same IP address#
$Having to carry VoIP traffic with "toll-quality" guarantees :
*You need to create your own IP network and give priority to voice traffic.
It is possible to use the Internet, Skype proves that this approach works definitely good.
You need to create your own IP network and give priority to voice traffic.
It is necessary to create a dedicated IP network, in which there is no data traffic.#
$Using the coin-operated bucket (or laundry bucket) algorithm of capacity B token e filling speed r token / s can be controlled:
*The number of packets per second entered does not exceed r , and the maximum burst does not exceed B.
That the crossing time does not exceed rB seconds.
The number of packets per second entered does not exceed B , and the maximum burst does not exceed r .
The jitter does not exceed B / r .#
$In the coin-operated bucket mechanism you can check:
*The maximum burst size and average data entry rate.
The maximum traversal time of a router.
Internal queue management with WFQ.
The minimum speed of data entry.#
$If we apply to a low of packets the token bucket (or leaky bucket) algorithm with capacity K and inserting token every 1/W sec, what is the final effect?
*The maximum burst size allowed is K
The maximum burst size allowed is W.
All the packets of this low will be routed on the same path (i.e. out of order arrival is eliminated).
It will be possible to implement traffic engineering mechanisms to this low of packets.#
$In the coin bucket algorithm :
*The capacity of the bucket is related to the maximum burst size.
Bucket capacity is related to long-term average speed.
The capacity of the bucket has a direct relationship with the band
Serve per implementare il weighted fair queuing.#
$When it is necessary to design a new network for integrated data and voice traffic, which is the highest priority requirement to fulfill?
*Routing protocols to find alternative paths in order to avoid call interruption, in case of failure
Mechanism to achieve deterministic characteristics for the voice calls
Mechanisms to reduce jitter as much as possible.
Mechanisms to obtain transit time for the voice packets as short as possible#
$What is a feature of the SIP protocol?
*Often, It requires a server for each SIP domain.
It is only implemented in "soft phones", that is software packages that are used for PC to PCcalls.
It is based on ASN.1, it is extremely complex and it is used for implementing signaling operations in IP networks.
It is used to implement the transmission of voice streams over an IP network.#
$Is user mobility covered in the SIP protocol ?
*Yes, as long as the user does not change their IP address during a SIP session .
It is not treated
Yes, no mobility restrictions are imposed on the user.
Yes, as long as the user always reconnects with an internal IP address provider.#
$In a SIP-based VoIP system , what can happen if I make a call to a recipient not connected to the Internet?
*You can ask to be notified when the desired user returns to being known to system
You can only come back and try later.
You can be notified of the appearance of the desired user, only if both are in the same SIP domain (we have the same operator).
You can be notified of the appearance of the desired user, only if he reconnects from one of the IP addresses known to the SIP domain.( MORE INFORMATION : through the Media Server, containing the voice mail boxes that actfrom answering machines, you can leave a message even if the recipient client it is not connected to the internet. He will receive the message as soon as he reconnects)#
$The SIP user is characterized by the fact that
*Has a domain to which it belongs
It has a specific public IP to which it needs to be connected.
It has an IP which can vary, but which cannot be private.
It is always connected to the Internet.#
$What is the reason of diffusion of VoIP among domestic users?
*The reduced cost associated to the possibility of VoIP technologies to compress voice channels, which require much less bandwidth the analog telephony, with a big reduction of bandwidth used in the backbone.
The reduced costs caused by higher costs in maintaining an high quality channel (the twisted pair) that is more expensive that physical lines used for data transmission.
Costs are often comparable with traditional telephony, but it is not necessary to pay an extra fee for each phone call, in addition to the ?at rate tariff of the ADSL line.
Quality of the calls are higher in VoIP, because the providers adopt suitable QoS mechanisms to offer high standards of quality for the phone calls.#
$Which of the following mechanisms apply to SIP?
*A voice gateway may be used to allow the communication between two IP phones connection to different physical networks
It is necessary to update the access network to fiber connection
Signaling protocols are used to setup a call and to negotiate its parameters
It's necessary to provide each user with a computer for sip cells and is normal phone set for calls from/to public switched network#
$Which of the following statement applies to sip protocol?
*It is based on a distributed architecture where each domain should have a server to manage the domestic users
It is based on a centralized architecture with only one server to manage communications
It is based on a hierarchical organization where each level manages a particular area of the network
It is bases on a peer to peer architecture to enable a dynamic behavior for the users#
$Why the combination of a token bucket (or a leaky bucket) and weighted fair queuing (WFQ) is used?
*It is used to obtain a guarantee jitter for packets
It is used to have a maximum guarantee transversal time for a single router
It is used to have a maximum guarantee transversal time for a NAT
It is used to have a maximum guarantee transversal time for a low of packets#
$The combination of token bucket (or laundry bucket) and Weighted Fair mechanisms Queueing (WFQ) serve a garantire:
*A maximum traversal time of a router.
A maximum traversal time of a NAT.
A maximum bandwidth for each packet stream.
A maximum burst of consecutive packets, for each stream.#
$What is the role of NAPTR record in sip?
*They are used which services are available in a domain with their relative priorities
They are used which server are available in a domain with their relative priorities.
They are used to verify the identity of the users during the registration phase.
They are used to possible change the voice encoding when two UAs do not have the same codec.#
$ The SIP protocol :
*It is based on a distributed architecture, in which each domain must have a server that is responsible for its users
It is based on a strictly centralized architecture, with a single server to manage the communications
It is based on a hierarchical architecture in which each level of the hierarchy is responsible for one particular area of the network
It is based on a peer-to-peer architecture to facilitate user dynamism#
$What is the role of Session Description Protocol?
*It is used to negotiate the parameters to setup a call
It is used to select the use of sip or H.323 for the session being open
It is used to Exchange authentication information at the beginning of a session
It is used to select if a record routing should be selected or not, for the current SIP Session#
$If you are using the SIP protocol, what types of information can be stored in the DNS?
*New record types describing the SIP services available in a domain and related server.
No information other than the usual DNS RR records.
Translation for all user names into IP addresses.
Information on the telephone numbers to use to call SIP users.#
$Which function is performed by a voice gateway (or VoIP gateway)?
*It translates packets carrying voice samples into signals understandable in a plain old telephone system (POTS)
It forwards packets between the public internet and a corporate network.
It encrypts voice signals arriving from a classical telephone network, before they are forwarded to internet, so that the signal cannot be understood by an eavesdropper.
It translates SS #7 signaling into SIP signaling messages#
$Which of the following features are part of a voice gateway (or VoIP) Gateway?
*It translates voice streams generated over a packet network (e.g. using SIP or H232) into telephone calls over a traditional telephone network
It forwards packets from a public IP network to a private one
It encrypts a voice signal arriving from a traditional telephone network before forwarding it over to the internet.
It synchronizes different RTP stream (lip synch)#
$What is the SDP role in SIP telephony?
*It is used to carry the description of the main parameters of the conversation that is about to start.
It is used to reserve the required resources to obtain the quality of services needed to call
It is used to locate the IP address of the called user
It is used to encapsulate the audio/video sample during the phone call#
$What is the role of the NAPTR records in SIP?
*They are used to discover the SIP services available in a given domain
They are used to discover the names of the sip servers of a given domain
They are used to translate the name into the IP addresses of the SIP server.
They include the IP address of the called SIP user#
$What is the role played by RTCP?
*It provides control mechanism for RTP
It may be used to reserve the resources required to obtain a certain quality of services
It may be used to change the payload type of an RTP stream without restarting it
It may be used to distinguish between two streams ( e.g. audio and video) with the same destination.#
$What is the role of Enum standard?
*To translate a phone number into a Sip user name
To Locate the sip server in all the inter domains calls
To translate Sip user name into phone number
To register the users with the SIP servers#
$The codec specifically engineered for voice encoding:
*Always add redundancy bits to reduce damage in case of loss of packages. page 64 notes
They tend to create large packets to maximize network efficiency.
They tend to create small packets to minimize end-to-end delay.
I am also able to operate with different VoIP sources (for example modem or FAX).#
$Gli LSP (label switched path) nell'architettura MPLS (multi-protocol label switching)
*They are created (set up) for the transport of packages belonging to a class of forwarding equivalence class (FEC).
They represent alternate routes maintained in a router's table for forwarding packets to a destination.
They are exchanged by routers to build a network map.
They are the shortest path to a destination.#
$The multi-protocol label switching ( MPLS) architecture is characterized by
*Routing protocols that are particularly quick to update routing tables later to topological changes in order to recover faults quickly.
A particularly advanced support to provide guaranteed quality services
A different mechanism (compared to pure IP) to decide the outbound interface to which a package needs to be forwarded.
Intelligent network terminals capable of personalizing the services received from the network#
$Which operations can be performed on a label by a single MPLS router?
*Add an external label (PUSH), drop the external label (POP), change the content of the external (SWAP)
Add a label in any position (PUSH), drop one label in any position (POP), change the value of a label in any position (SWAP).
Add a label if the router is the ingress one (only 1 label is allowed) (PUSH), drop the only label if the router is the egress one (POP), e change the content of the only label present (SWAP).
Labels cannot be manipulated by MPLS routers.#
$Gli LSP (label switched path) nell'architettura MPLS (multi-protocol label switching)
*They are created by the network nodes who agree on the labels to be used for the packets belonging to a forwarding equivalence class(FEC).
They are obtained by reserving resources in the network nodes in order to guarantee appropriate quality of the service to the applications that created them.
They are the shortest route to a destination.
They are created (set up) by applications for transporting packets belonging to a forwarding equivalence class (FEC).#
$The importance of MPLS (multiprotocol label switching) today's networks derives from one of the following features.
*It is possible to transport efficiently IP packet over ATM networks
It is possible to have a high speed connections between servers and their disk units
It is possible to implement efficient and effective traffic engineering operations
It is possible to implement devices that do not need complex configuration operation#
$In a packet traveling on an MPLS network, it is possible to have multiple labelssimultaneously ?
*Yes, but only in the MPLS tunnels used for VPNs.
No, it is not expected.
Yes, but no more than 2.
Yes, but no more than 20.#
$How can MPLS be used to build a VPN ?
*Can provide point-to-point links in overlay networks or the whole mechanism routing in peer networks .
To make an access VPN.
MPLS cannot be used to build VPNs.
Can provide all routing mechanism in overlay or link networks point-to-point in peer networks.#
$Why MPLS is important?
*It is possible to have a single control plane for different switching technologies
In such networks, it is possible to implement routers with a specific support to guarantee the required quality of services.
It is possible to implement devices that should not be configured
It is possible to distribute the traffic among several equivalent servers#
$MPLS (Multiprotocol Label Switching) architecture is characterized by
*A different mechanism (with respect to pure IP) for selecting the output interface toward which packet should be forwarded.
End System that are able to negotiate with the network the label of packets generated
Intelligent terminals that can personalize service received from the network
Routing protocols that are extremely fast in updating routing tables when a topology changes occur in order to ensure fast fault recovery.#
$In a frame relay network the minimum transmission unit is:
*The level 2 transmitting unit.
The 53-byte cell.
The virtual circuit.
The IP packet.#
$ATM networks are often used for:
*Interconnect the terminations of the ADSL channels with the service provider's network chosen by the user
Interconnect several LAN sections within the same campus.
Create VLANs.
Building VoIP systems.#
$The transport of IP packets over ATM networks
*It is currently used, although in danger of "extinction", on the ridges geographical areas of the operators.
It's not possible
It is essential for real-time traffic transport (for example video) water IP
It is considered an optimal solution whose use is growing rapidly.#
$What is a feature of ATM networks?
*They use a fixed size cell, as unit of transmission.
They do not allow fragmentation of long packets
They provide a datagram based packet forwarding.
They allow a unified control plane with IP networks.#
$Where ATM networks are still used today?
*In private networks
In some LANS
In some connections between homes and the closest DSLAMs
In some networks connecting DSLAMs with ISP networks (POP)#
$How popular is the transport of IP over ATM networks
*It is possible and currently used, but this technique is going to disappear
It is not possible
It is only available solution for real time traffic (e.g. video = over IP)
It is considered a good solution and it will become more popular#
$Transmission in SONET / SDH is characterized by:
*Frames whose duration is always 125 microseconds, whatever the speed of the connections
Flexibility in the use of the band
Mechanisms for congestion control.
Equal time on all channel types for the transmission of a single byte, whatever the link speed.#
$What is one of the problems with SONET/SDH networks?
*Bandwidth management is rigid
They are not suitable for an implementation based on optical fibers.
They are not suitable to implement ATM or frame Relay networks.
They cannot achieve high transmission speed.#
$To ensure quality of service in packet-switched networks
*Network nodes must have appropriate mechanisms in place that regulate packet service (for example scheduling algorithms)
Applications must be able to encode the information to be transferred according to levels (layers) of different importance
Packets must be transported over a cell-switched infrastructure (eg ATM)#
$In a Frame Relay network, what is the Committed Information Rate?
*The maximum number of bits that can be sent to the network, in a specified time interval
The minimum bandwidth guaranteed.
The maximum length of a packet that can enter the network.
The maximum transit time.#"""

if __name__ == '__main__':
    main()
