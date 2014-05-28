# PySNMP SMI module. Autogenerated from smidump -f python IP-FORWARD-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:43 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( IANAipRouteProtocol, ) = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol")
( InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
( InetAddress, InetAddressPrefixLength, InetAddressType, InetAutonomousSystemNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength", "InetAddressType", "InetAutonomousSystemNumber")
( ip, ) = mibBuilder.importSymbols("IP-MIB", "ip")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( RowStatus, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus")

# Objects

ipForward = ModuleIdentity((1, 3, 6, 1, 2, 1, 4, 24)).setRevisions(("2006-02-01 00:00","1996-09-19 00:00","1992-07-02 21:56",))
if mibBuilder.loadTexts: ipForward.setOrganization("IETF IPv6 Working Group\nhttp://www.ietf.org/html.charters/ipv6-charter.html")
if mibBuilder.loadTexts: ipForward.setContactInfo("Editor:\nBrian Haberman\nJohns Hopkins University - Applied Physics Laboratory\nMailstop 17-S442\n11100 Johns Hopkins Road\nLaurel MD,  20723-6099  USA\n\nPhone: +1-443-778-1319\nEmail: brian@innovationslab.net\n\nSend comments to <ipv6@ietf.org>")
if mibBuilder.loadTexts: ipForward.setDescription("The MIB module for the management of CIDR multipath IP\nRoutes.\n\nCopyright (C) The Internet Society (2006).  This version\nof this MIB module is a part of RFC 4292; see the RFC\nitself for full legal notices.")
ipForwardNumber = MibScalar((1, 3, 6, 1, 2, 1, 4, 24, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardNumber.setDescription("The number of current ipForwardTable entries that are\nnot invalid.")
ipForwardTable = MibTable((1, 3, 6, 1, 2, 1, 4, 24, 2))
if mibBuilder.loadTexts: ipForwardTable.setDescription("This entity's IP Routing table.")
ipForwardEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 24, 2, 1)).setIndexNames((0, "IP-FORWARD-MIB", "ipForwardDest"), (0, "IP-FORWARD-MIB", "ipForwardProto"), (0, "IP-FORWARD-MIB", "ipForwardPolicy"), (0, "IP-FORWARD-MIB", "ipForwardNextHop"))
if mibBuilder.loadTexts: ipForwardEntry.setDescription("A particular route to a particular destination, under a\nparticular policy.")
ipForwardDest = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardDest.setDescription("The destination IP address of this route.  An entry\nwith a value of 0.0.0.0 is considered a default route.\n\nThis object may not take a Multicast (Class D) address\nvalue.\n\nAny assignment (implicit or otherwise) of an instance\nof this object to a value x must be rejected if the\nbitwise logical-AND of x with the value of the\ncorresponding instance of the ipForwardMask object is\nnot equal to x.")
ipForwardMask = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 2), IpAddress().clone("0.0.0.0")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMask.setDescription("Indicate the mask to be logical-ANDed with the\ndestination address before being compared to the value\nin the ipForwardDest field.  For those systems that do\nnot support arbitrary subnet masks, an agent constructs\nthe value of the ipForwardMask by reference to the IP\nAddress Class.\n\nAny assignment (implicit or otherwise) of an instance\nof this object to a value x must be rejected if the\nbitwise logical-AND of x with the value of the\ncorresponding instance of the ipForwardDest object is\nnot equal to ipForwardDest.")
ipForwardPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardPolicy.setDescription("The general set of conditions that would cause\nthe selection of one multipath route (set of\nnext hops for a given destination) is referred\nto as 'policy'.\n\nUnless the mechanism indicated by ipForwardProto\nspecifies otherwise, the policy specifier is\nthe IP TOS Field.  The encoding of IP TOS is as\nspecified by the following convention.  Zero\nindicates the default path if no more specific\npolicy applies.\n\n+-----+-----+-----+-----+-----+-----+-----+-----+\n|                 |                       |     |\n|   PRECEDENCE    |    TYPE OF SERVICE    |  0  |\n|                 |                       |     |\n+-----+-----+-----+-----+-----+-----+-----+-----+\n\n             IP TOS                IP TOS\n   Field     Policy      Field     Policy\n   Contents    Code      Contents    Code\n   0 0 0 0  ==>   0      0 0 0 1  ==>   2\n   0 0 1 0  ==>   4      0 0 1 1  ==>   6\n   0 1 0 0  ==>   8      0 1 0 1  ==>  10\n   0 1 1 0  ==>  12      0 1 1 1  ==>  14\n   1 0 0 0  ==>  16      1 0 0 1  ==>  18\n   1 0 1 0  ==>  20      1 0 1 1  ==>  22\n   1 1 0 0  ==>  24      1 1 0 1  ==>  26\n   1 1 1 0  ==>  28      1 1 1 1  ==>  30\n\nProtocols defining 'policy' otherwise must either\ndefine a set of values that are valid for\nthis object or must implement an integer-instanced\npolicy table for which this object's\nvalue acts as an index.")
ipForwardNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardNextHop.setDescription("On remote routes, the address of the next system en\nroute; otherwise, 0.0.0.0.")
ipForwardIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 5), Integer32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardIfIndex.setDescription("The ifIndex value that identifies the local interface\nthrough which the next hop of this route should be\nreached.")
ipForwardType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(4,1,3,2,)).subtype(namedValues=NamedValues(("other", 1), ("invalid", 2), ("local", 3), ("remote", 4), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardType.setDescription("The type of route.  Note that local(3) refers to a\nroute for which the next hop is the final destination;\nremote(4) refers to a route for which the next hop is\nnot the final destination.\n\nSetting this object to the value invalid(2) has the\neffect of invalidating the corresponding entry in the\nipForwardTable object.  That is, it effectively\ndisassociates the destination identified with said\nentry from the route identified with said entry.  It is\nan implementation-specific matter as to whether the\nagent removes an invalidated entry from the table.\nAccordingly, management stations must be prepared to\nreceive tabular information from agents that\ncorresponds to entries not currently in use.  Proper\ninterpretation of such entries requires examination of\nthe relevant ipForwardType object.")
ipForwardProto = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(14,12,3,13,5,8,10,15,11,1,9,4,2,7,6,)).subtype(namedValues=NamedValues(("other", 1), ("es-is", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("is-is", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardProto.setDescription("The routing mechanism via which this route was learned.\nInclusion of values for gateway routing protocols is\nnot intended to imply that hosts should support those\nprotocols.")
ipForwardAge = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 8), Integer32().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardAge.setDescription("The number of seconds since this route was last updated\nor otherwise determined to be correct.  Note that no\nsemantics of `too old' can be implied except through\nknowledge of the routing protocol by which the route\nwas learned.")
ipForwardInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 9), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardInfo.setDescription("A reference to MIB definitions specific to the\nparticular routing protocol that is responsible for\nthis route, as determined by the value specified in the\nroute's ipForwardProto value.  If this information is\nnot present, its value should be set to the OBJECT\nIDENTIFIER { 0 0 }, which is a syntactically valid\nobject identifier, and any implementation conforming to\nASN.1 and the Basic Encoding Rules must be able to\ngenerate and recognize this value.")
ipForwardNextHopAS = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 10), Integer32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardNextHopAS.setDescription("The Autonomous System Number of the Next Hop.  When\nthis is unknown or not relevant to the protocol\nindicated by ipForwardProto, zero.")
ipForwardMetric1 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 11), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric1.setDescription("The primary routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipForwardProto value.\nIf this metric is not used, its value should be set to\n-1.")
ipForwardMetric2 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 12), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric2.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipForwardProto value.\nIf this metric is not used, its value should be set to\n-1.")
ipForwardMetric3 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 13), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric3.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipForwardProto value.\nIf this metric is not used, its value should be set to\n-1.")
ipForwardMetric4 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 14), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric4.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipForwardProto value.\nIf this metric is not used, its value should be set to\n-1.")
ipForwardMetric5 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 15), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric5.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipForwardProto value.\nIf this metric is not used, its value should be set to\n-1.")
ipCidrRouteNumber = MibScalar((1, 3, 6, 1, 2, 1, 4, 24, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteNumber.setDescription("The number of current ipCidrRouteTable entries that are\nnot invalid.  This object is deprecated in favor of\ninetCidrRouteNumber and the inetCidrRouteTable.")
ipCidrRouteTable = MibTable((1, 3, 6, 1, 2, 1, 4, 24, 4))
if mibBuilder.loadTexts: ipCidrRouteTable.setDescription("This entity's IP Routing table.  This table has been\ndeprecated in favor of the IP version neutral\ninetCidrRouteTable.")
ipCidrRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 24, 4, 1)).setIndexNames((0, "IP-FORWARD-MIB", "ipCidrRouteDest"), (0, "IP-FORWARD-MIB", "ipCidrRouteMask"), (0, "IP-FORWARD-MIB", "ipCidrRouteTos"), (0, "IP-FORWARD-MIB", "ipCidrRouteNextHop"))
if mibBuilder.loadTexts: ipCidrRouteEntry.setDescription("A particular route to a particular destination, under a\n\nparticular policy.")
ipCidrRouteDest = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteDest.setDescription("The destination IP address of this route.\n\nThis object may not take a Multicast (Class D) address\nvalue.\n\nAny assignment (implicit or otherwise) of an instance\nof this object to a value x must be rejected if the\nbitwise logical-AND of x with the value of the\ncorresponding instance of the ipCidrRouteMask object is\nnot equal to x.")
ipCidrRouteMask = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteMask.setDescription("Indicate the mask to be logical-ANDed with the\ndestination address before being compared to the value\nin the ipCidrRouteDest field.  For those systems that\ndo not support arbitrary subnet masks, an agent\nconstructs the value of the ipCidrRouteMask by\nreference to the IP Address Class.\n\nAny assignment (implicit or otherwise) of an instance\nof this object to a value x must be rejected if the\nbitwise logical-AND of x with the value of the\ncorresponding instance of the ipCidrRouteDest object is\nnot equal to ipCidrRouteDest.")
ipCidrRouteTos = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteTos.setDescription("The policy specifier is the IP TOS Field.  The encoding\nof IP TOS is as specified by the following convention.\nZero indicates the default path if no more specific\npolicy applies.\n\n+-----+-----+-----+-----+-----+-----+-----+-----+\n|                 |                       |     |\n|   PRECEDENCE    |    TYPE OF SERVICE    |  0  |\n|                 |                       |     |\n+-----+-----+-----+-----+-----+-----+-----+-----+\n\n             IP TOS                IP TOS\n   Field     Policy      Field     Policy\n   Contents    Code      Contents    Code\n   0 0 0 0  ==>   0      0 0 0 1  ==>   2\n   0 0 1 0  ==>   4      0 0 1 1  ==>   6\n   0 1 0 0  ==>   8      0 1 0 1  ==>  10\n   0 1 1 0  ==>  12      0 1 1 1  ==>  14\n   1 0 0 0  ==>  16      1 0 0 1  ==>  18\n   1 0 1 0  ==>  20      1 0 1 1  ==>  22\n\n   1 1 0 0  ==>  24      1 1 0 1  ==>  26\n   1 1 1 0  ==>  28      1 1 1 1  ==>  30")
ipCidrRouteNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteNextHop.setDescription("On remote routes, the address of the next system en\nroute; Otherwise, 0.0.0.0.")
ipCidrRouteIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 5), Integer32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteIfIndex.setDescription("The ifIndex value that identifies the local interface\nthrough which the next hop of this route should be\nreached.")
ipCidrRouteType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(4,1,3,2,)).subtype(namedValues=NamedValues(("other", 1), ("reject", 2), ("local", 3), ("remote", 4), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteType.setDescription("The type of route.  Note that local(3) refers to a\nroute for which the next hop is the final destination;\nremote(4) refers to a route for which the next hop is\nnot the final destination.\n\nRoutes that do not result in traffic forwarding or\nrejection should not be displayed, even if the\nimplementation keeps them stored internally.\n\nreject (2) refers to a route that, if matched,\ndiscards the message as unreachable.  This is used in\nsome protocols as a means of correctly aggregating\nroutes.")
ipCidrRouteProto = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(10,9,3,13,16,5,8,14,15,11,1,12,4,2,7,6,)).subtype(namedValues=NamedValues(("other", 1), ("esIs", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("ciscoEigrp", 16), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("isIs", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteProto.setDescription("The routing mechanism via which this route was learned.\nInclusion of values for gateway routing protocols is\nnot intended to imply that hosts should support those\nprotocols.")
ipCidrRouteAge = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 8), Integer32().clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteAge.setDescription("The number of seconds since this route was last updated\nor otherwise determined to be correct.  Note that no\nsemantics of `too old' can be implied, except through\nknowledge of the routing protocol by which the route\nwas learned.")
ipCidrRouteInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 9), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteInfo.setDescription("A reference to MIB definitions specific to the\nparticular routing protocol that is responsible for\nthis route, as determined by the value specified in the\nroute's ipCidrRouteProto value.  If this information is\nnot present, its value should be set to the OBJECT\nIDENTIFIER { 0 0 }, which is a syntactically valid\nobject identifier, and any implementation conforming to\nASN.1 and the Basic Encoding Rules must be able to\ngenerate and recognize this value.")
ipCidrRouteNextHopAS = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 10), Integer32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteNextHopAS.setDescription("The Autonomous System Number of the Next Hop.  The\nsemantics of this object are determined by the routing-\nprotocol specified in the route's ipCidrRouteProto\nvalue.  When this object is unknown or not relevant, its\nvalue should be set to zero.")
ipCidrRouteMetric1 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 11), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric1.setDescription("The primary routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipCidrRouteProto\nvalue.  If this metric is not used, its value should be\nset to -1.")
ipCidrRouteMetric2 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 12), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric2.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipCidrRouteProto\nvalue.  If this metric is not used, its value should be\n\nset to -1.")
ipCidrRouteMetric3 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 13), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric3.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipCidrRouteProto\nvalue.  If this metric is not used, its value should be\nset to -1.")
ipCidrRouteMetric4 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 14), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric4.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipCidrRouteProto\nvalue.  If this metric is not used, its value should be\nset to -1.")
ipCidrRouteMetric5 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 15), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric5.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's ipCidrRouteProto\nvalue.  If this metric is not used, its value should be\nset to -1.")
ipCidrRouteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteStatus.setDescription("The row status variable, used according to row\ninstallation and removal conventions.")
ipForwardConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 24, 5))
ipForwardGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 24, 5, 1))
ipForwardCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 24, 5, 2))
inetCidrRouteNumber = MibScalar((1, 3, 6, 1, 2, 1, 4, 24, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetCidrRouteNumber.setDescription("The number of current inetCidrRouteTable entries that\nare not invalid.")
inetCidrRouteTable = MibTable((1, 3, 6, 1, 2, 1, 4, 24, 7))
if mibBuilder.loadTexts: inetCidrRouteTable.setDescription("This entity's IP Routing table.")
inetCidrRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 24, 7, 1)).setIndexNames((0, "IP-FORWARD-MIB", "inetCidrRouteDestType"), (0, "IP-FORWARD-MIB", "inetCidrRouteDest"), (0, "IP-FORWARD-MIB", "inetCidrRoutePfxLen"), (0, "IP-FORWARD-MIB", "inetCidrRoutePolicy"), (0, "IP-FORWARD-MIB", "inetCidrRouteNextHopType"), (0, "IP-FORWARD-MIB", "inetCidrRouteNextHop"))
if mibBuilder.loadTexts: inetCidrRouteEntry.setDescription("A particular route to a particular destination, under a\nparticular policy (as reflected in the\ninetCidrRoutePolicy object).\n\nDynamically created rows will survive an agent reboot.\n\nImplementers need to be aware that if the total number\nof elements (octets or sub-identifiers) in\ninetCidrRouteDest, inetCidrRoutePolicy, and\ninetCidrRouteNextHop exceeds 111, then OIDs of column\ninstances in this table will have more than 128 sub-\nidentifiers and cannot be accessed using SNMPv1,\nSNMPv2c, or SNMPv3.")
inetCidrRouteDestType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 1), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: inetCidrRouteDestType.setDescription("The type of the inetCidrRouteDest address, as defined\nin the InetAddress MIB.\n\nOnly those address types that may appear in an actual\nrouting table are allowed as values of this object.")
inetCidrRouteDest = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 2), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: inetCidrRouteDest.setDescription("The destination IP address of this route.\n\nThe type of this address is determined by the value of\nthe inetCidrRouteDestType object.\n\nThe values for the index objects inetCidrRouteDest and\ninetCidrRoutePfxLen must be consistent.  When the value\nof inetCidrRouteDest (excluding the zone index, if one\nis present) is x, then the bitwise logical-AND\nof x with the value of the mask formed from the\ncorresponding index object inetCidrRoutePfxLen MUST be\nequal to x.  If not, then the index pair is not\nconsistent and an inconsistentName error must be\nreturned on SET or CREATE requests.")
inetCidrRoutePfxLen = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 3), InetAddressPrefixLength()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: inetCidrRoutePfxLen.setDescription("Indicates the number of leading one bits that form the\nmask to be logical-ANDed with the destination address\nbefore being compared to the value in the\n\ninetCidrRouteDest field.\n\nThe values for the index objects inetCidrRouteDest and\ninetCidrRoutePfxLen must be consistent.  When the value\nof inetCidrRouteDest (excluding the zone index, if one\nis present) is x, then the bitwise logical-AND\nof x with the value of the mask formed from the\ncorresponding index object inetCidrRoutePfxLen MUST be\nequal to x.  If not, then the index pair is not\nconsistent and an inconsistentName error must be\nreturned on SET or CREATE requests.")
inetCidrRoutePolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 4), ObjectIdentifier()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: inetCidrRoutePolicy.setDescription("This object is an opaque object without any defined\nsemantics.  Its purpose is to serve as an additional\nindex that may delineate between multiple entries to\nthe same destination.  The value { 0 0 } shall be used\nas the default value for this object.")
inetCidrRouteNextHopType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 5), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: inetCidrRouteNextHopType.setDescription("The type of the inetCidrRouteNextHop address, as\ndefined in the InetAddress MIB.\n\nValue should be set to unknown(0) for non-remote\nroutes.\n\nOnly those address types that may appear in an actual\nrouting table are allowed as values of this object.")
inetCidrRouteNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 6), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: inetCidrRouteNextHop.setDescription("On remote routes, the address of the next system en\n\nroute.  For non-remote routes, a zero length string.\n\nThe type of this address is determined by the value of\nthe inetCidrRouteNextHopType object.")
inetCidrRouteIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteIfIndex.setDescription("The ifIndex value that identifies the local interface\nthrough which the next hop of this route should be\nreached.  A value of 0 is valid and represents the\nscenario where no interface is specified.")
inetCidrRouteType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(4,5,1,2,3,)).subtype(namedValues=NamedValues(("other", 1), ("reject", 2), ("local", 3), ("remote", 4), ("blackhole", 5), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteType.setDescription("The type of route.  Note that local(3) refers to a\nroute for which the next hop is the final destination;\nremote(4) refers to a route for which the next hop is\nnot the final destination.\n\nRoutes that do not result in traffic forwarding or\nrejection should not be displayed, even if the\nimplementation keeps them stored internally.\n\nreject(2) refers to a route that, if matched, discards\nthe message as unreachable and returns a notification\n(e.g., ICMP error) to the message sender.  This is used\nin some protocols as a means of correctly aggregating\nroutes.\n\nblackhole(5) refers to a route that, if matched,\ndiscards the message silently.")
inetCidrRouteProto = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 9), IANAipRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetCidrRouteProto.setDescription("The routing mechanism via which this route was learned.\nInclusion of values for gateway routing protocols is\nnot intended to imply that hosts should support those\nprotocols.")
inetCidrRouteAge = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetCidrRouteAge.setDescription("The number of seconds since this route was last updated\nor otherwise determined to be correct.  Note that no\nsemantics of 'too old' can be implied, except through\nknowledge of the routing protocol by which the route\nwas learned.")
inetCidrRouteNextHopAS = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 11), InetAutonomousSystemNumber().clone('0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteNextHopAS.setDescription("The Autonomous System Number of the Next Hop.  The\nsemantics of this object are determined by the routing-\nprotocol specified in the route's inetCidrRouteProto\nvalue.  When this object is unknown or not relevant, its\nvalue should be set to zero.")
inetCidrRouteMetric1 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 12), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric1.setDescription("The primary routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's inetCidrRouteProto\nvalue.  If this metric is not used, its value should be\nset to -1.")
inetCidrRouteMetric2 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 13), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric2.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's inetCidrRouteProto\nvalue.  If this metric is not used, its value should be\nset to -1.")
inetCidrRouteMetric3 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 14), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric3.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's inetCidrRouteProto\nvalue.  If this metric is not used, its value should be\nset to -1.")
inetCidrRouteMetric4 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 15), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric4.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\nprotocol specified in the route's inetCidrRouteProto\nvalue.  If this metric is not used, its value should be\nset to -1.")
inetCidrRouteMetric5 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 16), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric5.setDescription("An alternate routing metric for this route.  The\nsemantics of this metric are determined by the routing-\n\nprotocol specified in the route's inetCidrRouteProto\nvalue.  If this metric is not used, its value should be\nset to -1.")
inetCidrRouteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteStatus.setDescription("The row status variable, used according to row\ninstallation and removal conventions.\n\nA row entry cannot be modified when the status is\nmarked as active(1).")
inetCidrRouteDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 24, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetCidrRouteDiscards.setDescription("The number of valid route entries discarded from the\ninetCidrRouteTable.  Discarded route entries do not\nappear in the inetCidrRouteTable.  One possible reason\nfor discarding an entry would be to free-up buffer space\nfor other route table entries.")

# Augmentions

# Groups

ipForwardMultiPathGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 2)).setObjects(*(("IP-FORWARD-MIB", "ipForwardMetric1"), ("IP-FORWARD-MIB", "ipForwardMask"), ("IP-FORWARD-MIB", "ipForwardMetric2"), ("IP-FORWARD-MIB", "ipForwardMetric3"), ("IP-FORWARD-MIB", "ipForwardAge"), ("IP-FORWARD-MIB", "ipForwardInfo"), ("IP-FORWARD-MIB", "ipForwardMetric4"), ("IP-FORWARD-MIB", "ipForwardPolicy"), ("IP-FORWARD-MIB", "ipForwardProto"), ("IP-FORWARD-MIB", "ipForwardIfIndex"), ("IP-FORWARD-MIB", "ipForwardNumber"), ("IP-FORWARD-MIB", "ipForwardType"), ("IP-FORWARD-MIB", "ipForwardNextHop"), ("IP-FORWARD-MIB", "ipForwardMetric5"), ("IP-FORWARD-MIB", "ipForwardNextHopAS"), ("IP-FORWARD-MIB", "ipForwardDest"), ) )
if mibBuilder.loadTexts: ipForwardMultiPathGroup.setDescription("IP Multipath Route Table.")
ipForwardCidrRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 3)).setObjects(*(("IP-FORWARD-MIB", "ipCidrRouteNextHopAS"), ("IP-FORWARD-MIB", "ipCidrRouteMetric5"), ("IP-FORWARD-MIB", "ipCidrRouteNumber"), ("IP-FORWARD-MIB", "ipCidrRouteType"), ("IP-FORWARD-MIB", "ipCidrRouteIfIndex"), ("IP-FORWARD-MIB", "ipCidrRouteMetric2"), ("IP-FORWARD-MIB", "ipCidrRouteProto"), ("IP-FORWARD-MIB", "ipCidrRouteStatus"), ("IP-FORWARD-MIB", "ipCidrRouteAge"), ("IP-FORWARD-MIB", "ipCidrRouteInfo"), ("IP-FORWARD-MIB", "ipCidrRouteNextHop"), ("IP-FORWARD-MIB", "ipCidrRouteMetric1"), ("IP-FORWARD-MIB", "ipCidrRouteMetric4"), ("IP-FORWARD-MIB", "ipCidrRouteDest"), ("IP-FORWARD-MIB", "ipCidrRouteTos"), ("IP-FORWARD-MIB", "ipCidrRouteMetric3"), ("IP-FORWARD-MIB", "ipCidrRouteMask"), ) )
if mibBuilder.loadTexts: ipForwardCidrRouteGroup.setDescription("The CIDR Route Table.\n\nThis group has been deprecated and replaced with\ninetForwardCidrRouteGroup.")
inetForwardCidrRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 4)).setObjects(*(("IP-FORWARD-MIB", "inetCidrRouteAge"), ("IP-FORWARD-MIB", "inetCidrRouteNextHopAS"), ("IP-FORWARD-MIB", "inetCidrRouteType"), ("IP-FORWARD-MIB", "inetCidrRouteMetric5"), ("IP-FORWARD-MIB", "inetCidrRouteMetric4"), ("IP-FORWARD-MIB", "inetCidrRouteNumber"), ("IP-FORWARD-MIB", "inetCidrRouteMetric1"), ("IP-FORWARD-MIB", "inetCidrRouteMetric3"), ("IP-FORWARD-MIB", "inetCidrRouteMetric2"), ("IP-FORWARD-MIB", "inetCidrRouteDiscards"), ("IP-FORWARD-MIB", "inetCidrRouteProto"), ("IP-FORWARD-MIB", "inetCidrRouteStatus"), ("IP-FORWARD-MIB", "inetCidrRouteIfIndex"), ) )
if mibBuilder.loadTexts: inetForwardCidrRouteGroup.setDescription("The IP version-independent CIDR Route Table.")

# Compliances

ipForwardCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 1)).setObjects(*(("IP-FORWARD-MIB", "ipForwardCidrRouteGroup"), ) )
if mibBuilder.loadTexts: ipForwardCompliance.setDescription("The compliance statement for SNMPv2 entities that\nimplement the ipForward MIB.\n\nThis compliance statement has been deprecated and\nreplaced with ipForwardFullCompliance and\nipForwardReadOnlyCompliance.")
ipForwardOldCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 2)).setObjects(*(("IP-FORWARD-MIB", "ipForwardMultiPathGroup"), ) )
if mibBuilder.loadTexts: ipForwardOldCompliance.setDescription("The compliance statement for SNMP entities that\nimplement the ipForward MIB.")
ipForwardFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 3)).setObjects(*(("IP-FORWARD-MIB", "inetForwardCidrRouteGroup"), ) )
if mibBuilder.loadTexts: ipForwardFullCompliance.setDescription("When this MIB is implemented for read-create, the\nimplementation can claim full compliance.\n\nThere are a number of INDEX objects that cannot be\nrepresented in the form of OBJECT clauses in SMIv2,\nbut for which there are compliance requirements,\nexpressed in OBJECT clause form in this description:\n\n-- OBJECT      inetCidrRouteDestType\n-- SYNTAX      InetAddressType (ipv4(1), ipv6(2),\n--                              ipv4z(3), ipv6z(4))\n-- DESCRIPTION\n--     This MIB requires support for global and\n--     non-global ipv4 and ipv6 addresses.\n\n--\n-- OBJECT      inetCidrRouteDest\n-- SYNTAX      InetAddress (SIZE (4 | 8 | 16 | 20))\n-- DESCRIPTION\n--     This MIB requires support for global and\n--     non-global IPv4 and IPv6 addresses.\n--\n-- OBJECT      inetCidrRouteNextHopType\n-- SYNTAX      InetAddressType (unknown(0), ipv4(1),\n--                              ipv6(2), ipv4z(3)\n--                              ipv6z(4))\n-- DESCRIPTION\n--     This MIB requires support for global and\n--     non-global ipv4 and ipv6 addresses.\n--\n-- OBJECT      inetCidrRouteNextHop\n-- SYNTAX      InetAddress (SIZE (0 | 4 | 8 | 16 | 20))\n-- DESCRIPTION\n--     This MIB requires support for global and\n--     non-global IPv4 and IPv6 addresses.")
ipForwardReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 4)).setObjects(*(("IP-FORWARD-MIB", "inetForwardCidrRouteGroup"), ) )
if mibBuilder.loadTexts: ipForwardReadOnlyCompliance.setDescription("When this MIB is implemented without support for read-\ncreate (i.e., in read-only mode), the implementation can\nclaim read-only compliance.")

# Exports

# Module identity
mibBuilder.exportSymbols("IP-FORWARD-MIB", PYSNMP_MODULE_ID=ipForward)

# Objects
mibBuilder.exportSymbols("IP-FORWARD-MIB", ipForward=ipForward, ipForwardNumber=ipForwardNumber, ipForwardTable=ipForwardTable, ipForwardEntry=ipForwardEntry, ipForwardDest=ipForwardDest, ipForwardMask=ipForwardMask, ipForwardPolicy=ipForwardPolicy, ipForwardNextHop=ipForwardNextHop, ipForwardIfIndex=ipForwardIfIndex, ipForwardType=ipForwardType, ipForwardProto=ipForwardProto, ipForwardAge=ipForwardAge, ipForwardInfo=ipForwardInfo, ipForwardNextHopAS=ipForwardNextHopAS, ipForwardMetric1=ipForwardMetric1, ipForwardMetric2=ipForwardMetric2, ipForwardMetric3=ipForwardMetric3, ipForwardMetric4=ipForwardMetric4, ipForwardMetric5=ipForwardMetric5, ipCidrRouteNumber=ipCidrRouteNumber, ipCidrRouteTable=ipCidrRouteTable, ipCidrRouteEntry=ipCidrRouteEntry, ipCidrRouteDest=ipCidrRouteDest, ipCidrRouteMask=ipCidrRouteMask, ipCidrRouteTos=ipCidrRouteTos, ipCidrRouteNextHop=ipCidrRouteNextHop, ipCidrRouteIfIndex=ipCidrRouteIfIndex, ipCidrRouteType=ipCidrRouteType, ipCidrRouteProto=ipCidrRouteProto, ipCidrRouteAge=ipCidrRouteAge, ipCidrRouteInfo=ipCidrRouteInfo, ipCidrRouteNextHopAS=ipCidrRouteNextHopAS, ipCidrRouteMetric1=ipCidrRouteMetric1, ipCidrRouteMetric2=ipCidrRouteMetric2, ipCidrRouteMetric3=ipCidrRouteMetric3, ipCidrRouteMetric4=ipCidrRouteMetric4, ipCidrRouteMetric5=ipCidrRouteMetric5, ipCidrRouteStatus=ipCidrRouteStatus, ipForwardConformance=ipForwardConformance, ipForwardGroups=ipForwardGroups, ipForwardCompliances=ipForwardCompliances, inetCidrRouteNumber=inetCidrRouteNumber, inetCidrRouteTable=inetCidrRouteTable, inetCidrRouteEntry=inetCidrRouteEntry, inetCidrRouteDestType=inetCidrRouteDestType, inetCidrRouteDest=inetCidrRouteDest, inetCidrRoutePfxLen=inetCidrRoutePfxLen, inetCidrRoutePolicy=inetCidrRoutePolicy, inetCidrRouteNextHopType=inetCidrRouteNextHopType, inetCidrRouteNextHop=inetCidrRouteNextHop, inetCidrRouteIfIndex=inetCidrRouteIfIndex, inetCidrRouteType=inetCidrRouteType, inetCidrRouteProto=inetCidrRouteProto, inetCidrRouteAge=inetCidrRouteAge, inetCidrRouteNextHopAS=inetCidrRouteNextHopAS, inetCidrRouteMetric1=inetCidrRouteMetric1, inetCidrRouteMetric2=inetCidrRouteMetric2, inetCidrRouteMetric3=inetCidrRouteMetric3, inetCidrRouteMetric4=inetCidrRouteMetric4, inetCidrRouteMetric5=inetCidrRouteMetric5, inetCidrRouteStatus=inetCidrRouteStatus, inetCidrRouteDiscards=inetCidrRouteDiscards)

# Groups
mibBuilder.exportSymbols("IP-FORWARD-MIB", ipForwardMultiPathGroup=ipForwardMultiPathGroup, ipForwardCidrRouteGroup=ipForwardCidrRouteGroup, inetForwardCidrRouteGroup=inetForwardCidrRouteGroup)

# Compliances
mibBuilder.exportSymbols("IP-FORWARD-MIB", ipForwardCompliance=ipForwardCompliance, ipForwardOldCompliance=ipForwardOldCompliance, ipForwardFullCompliance=ipForwardFullCompliance, ipForwardReadOnlyCompliance=ipForwardReadOnlyCompliance)