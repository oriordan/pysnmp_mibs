# PySNMP SMI module. Autogenerated from smidump -f python WLSX-MOBILITY-MIB
# by libsmi2pysnmp-0.1.3 at Tue May 27 09:00:43 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( wlsxEnterpriseMibModules, ) = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
( ArubaActiveState, ArubaAuthenticationMethods, ArubaEnableValue, ArubaEncryptionMethods, ArubaEncryptionMethods, ArubaFrameType, ArubaPhyType, ArubaRogueApType, ) = mibBuilder.importSymbols("ARUBA-TC", "ArubaActiveState", "ArubaAuthenticationMethods", "ArubaEnableValue", "ArubaEncryptionMethods", "ArubaEncryptionMethods", "ArubaFrameType", "ArubaPhyType", "ArubaRogueApType")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "snmpModules")
( DisplayString, MacAddress, PhysAddress, RowStatus, StorageType, TAddress, TDomain, TextualConvention, TestAndIncr, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "PhysAddress", "RowStatus", "StorageType", "TAddress", "TDomain", "TextualConvention", "TestAndIncr", "TimeInterval", "TruthValue")

# Objects

wlsxMobilityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9)).setRevisions(("1908-04-16 02:06",))
if mibBuilder.loadTexts: wlsxMobilityMIB.setOrganization("Aruba Wireless Networks")
if mibBuilder.loadTexts: wlsxMobilityMIB.setContactInfo("Postal:    1322 Crossman Avenue\nSunnyvale, CA 94089	\nE-mail:     dl-support@arubanetworks.com\nPhone:      +1 408 227 4500")
if mibBuilder.loadTexts: wlsxMobilityMIB.setDescription("This MIB module defines MIB objects which provide\ninformation about the mobility subsystem in the\n		Aruba controller.")
wlsxMobilityConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1))
wlsxMobilityDomainTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1))
if mibBuilder.loadTexts: wlsxMobilityDomainTable.setDescription("\nThis table lists all mobility domains configured on the controller.")
wlsxMobilityDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1, 1)).setIndexNames((0, "WLSX-MOBILITY-MIB", "mobilityDomainName"))
if mibBuilder.loadTexts: wlsxMobilityDomainEntry.setDescription("Mobility Domain Entry")
mobilityDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1, 1, 1), DisplayString()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: mobilityDomainName.setDescription("The name of the active mobility domain(s) this controller belongs to")
mobilityDomainIsExclusive = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1, 1, 2), ArubaEnableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityDomainIsExclusive.setDescription("Indicates whether this mobility domain is exclusive or not.")
mobilityDomainStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mobilityDomainStatus.setDescription("Row status object used to indicate the status of the row")
wlsxMobilityHomeAgentTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3))
if mibBuilder.loadTexts: wlsxMobilityHomeAgentTable.setDescription("\nThis table lists all Home Agents visible to the controller.")
wlsxMobilityHomeAgentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1)).setIndexNames((0, "WLSX-MOBILITY-MIB", "mobilityHomeAgentSubnet"), (0, "WLSX-MOBILITY-MIB", "mobilityHomeAgentMask"), (0, "WLSX-MOBILITY-MIB", "mobilityHomeAgentIp"))
if mibBuilder.loadTexts: wlsxMobilityHomeAgentEntry.setDescription("Mobility Home Agent Entry")
mobilityHomeAgentSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHomeAgentSubnet.setDescription("Subnet of the home agent")
mobilityHomeAgentMask = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHomeAgentMask.setDescription("Subnet mask of the home agent")
mobilityHomeAgentIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1, 3), IpAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: mobilityHomeAgentIp.setDescription("IP address of the home agent")
mobilityHomeAgentVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHomeAgentVlan.setDescription("Vlan of the home agent")
wlsxMobilityHostTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4))
if mibBuilder.loadTexts: wlsxMobilityHostTable.setDescription("\nThis table lists all mobile hosts on the controller.")
wlsxMobilityHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1)).setIndexNames((0, "WLSX-MOBILITY-MIB", "mobilityHostMac"))
if mibBuilder.loadTexts: wlsxMobilityHostEntry.setDescription("Mobility Host Home Agent Entry")
mobilityHostMac = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 1), MacAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: mobilityHostMac.setDescription("MAC address of the mobile host")
mobilityHostIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHostIp.setDescription("IP address of the mobile host")
mobilityHostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHostStatus.setDescription("Roaming status of the mobile host")
mobilityHostServiceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHostServiceTime.setDescription("Time in seconds mobility service is provided to the mobile host")
mobilityHostHomeVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHostHomeVlan.setDescription("Home VLAN of the mobile host")
mobilityHostHomeNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHostHomeNetwork.setDescription("Home network of the mobile host")
mobilityHostHomeMask = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHostHomeMask.setDescription("Home network mask of the mobile host")
mobilityHostDhcpInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 1, 4, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHostDhcpInfo.setDescription("DHCP details of the mobile host")
wlsxMobilityProxyStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2))
mobilityProxyPktRx = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyPktRx.setDescription("\nThis describes the number of packet Proxy State machine Received")
mobilityProxyPktHandled = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyPktHandled.setDescription("\nThis describes the number of packet Proxy State machine Processed")
mobilityProxyPktFwd = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyPktFwd.setDescription("\nThis describes the number of packet Proxy State machine Forwarded back to Datapath")
mobilityProxyPktDrop = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyPktDrop.setDescription("\nThis describes the number of packet Proxy State machine Dropped")
mobilityProxyBusy = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyBusy.setDescription("\nThis describes the number of mobility events Proxy State machine ignored as it is busy.")
mobilityProxyNoMobility = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyNoMobility.setDescription("\nThis describes the number of mobility clients with <No Mobility Service>")
mobilityProxyClientIPChg = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyClientIPChg.setDescription("\nThis describes the number of times mobility detected client IP change")
mobilityProxyClientEssidChg = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyClientEssidChg.setDescription("\nThis describes the number of times mobility detected client ESSID change")
wlsxMobilityProxyDHCPStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3))
mobilityProxyDhcpBootpRx = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyDhcpBootpRx.setDescription("\nThis describes the number of DHCP Bootp messages received")
mobilityProxyDhcpPktProc = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyDhcpPktProc.setDescription("\nThis describes the number of DHCP messages Processed")
mobilityProxyDhcpPktFwd = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyDhcpPktFwd.setDescription("\nThis describes the number of DHCP messages forwarded")
mobilityProxyDhcpPktDrop = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyDhcpPktDrop.setDescription("\nThis describes the number of DHCP messages Dropped")
mobilityProxyDHCPNak = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyDHCPNak.setDescription("\nThis describes the number of DHCP NAK received from the server.")
mobilityProxyBadDHCPPkt = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyBadDHCPPkt.setDescription("\nThis describes the number of DHCP packets marked invalid by mobility")
mobilityProxyNotDHCP = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyNotDHCP.setDescription("\nThis describes the number of Non-DHCP frames received by DHCP state machine")
mobilityProxyDHCPNoHomeVlan = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyDHCPNoHomeVlan.setDescription("\nThis describes the number of DHCP requested IP for which home vlan does not exist.")
mobilityProxyDHCPUnexpFrame = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyDHCPUnexpFrame.setDescription("\nThis describes the number of unexpected DHCP frames received from client")
mobilityProxyDHCPUnexpRemote = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 3, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityProxyDHCPUnexpRemote.setDescription("\nThis describes the number of unexpected DHCP frames received from remote HA/FA.")
wlsxMobilityHAStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4))
mobilityHARxRRQ = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHARxRRQ.setDescription("\nThis describes the number of Registration request received by HA")
mobilityHASentRRP = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHASentRRP.setDescription("\nThis describes the number of Registration request reply sent by HA")
mobilityHARRQAccept = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHARRQAccept.setDescription("\nThis describes the number of Registration request accepted by HA")
mobilityHARRQDenied = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHARRQDenied.setDescription("\nThis describes the number of Registration request denied by HA")
mobilityHARRQIgnore = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHARRQIgnore.setDescription("\nThis describes the number of Registration request Ignored by HA")
mobilityHARRQAdminDeny = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHARRQAdminDeny.setDescription("\nThis describes the number of Registration request denied for Administrative reasons by HA")
mobilityHARRQNoResource = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHARRQNoResource.setDescription("\nThis describes the number of Registration request denied due to lack of resources by HA")
mobilityHAMNauthFail = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHAMNauthFail.setDescription("\nThis describes the number of times MN-HA authentication failed")
mobilityHAFAauthFail = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHAFAauthFail.setDescription("\nThis describes the number of HA-FA authentication failed")
mobilityHABadID = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHABadID.setDescription("\nThis describes the number of mobileIP messages rejected by HA due to bad identification")
mobilityHAMalform = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHAMalform.setDescription("\nThis describes the number of mobileIP messages rejected by HA as they are poorly formed")
mobilityHATooManyBnd = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHATooManyBnd.setDescription("\nThis describes the number of Registration Request rejected due to too many bindings at HA")
mobilityHABndExpire = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 4, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityHABndExpire.setDescription("\nThis describes the number of times binding expired")
wlsxMobilityFAStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5))
mobilityFASentRRQ = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityFASentRRQ.setDescription("\nThis describes the number of Registration request sent by FA")
mobilityFARcvRRP = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityFARcvRRP.setDescription("\nThis describes the number of Registration request reply received by FA")
mobilityFARRQAccept = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityFARRQAccept.setDescription("\nThis describes the number of Registration request accepted by HA")
mobilityFARRQReject = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityFARRQReject.setDescription("\nThis describes the number of Registration request rejected by HA")
mobilityMNHAauthFAIL = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityMNHAauthFAIL.setDescription("\nThis describes the number of times MN-HA authentication failed")
mobilityFAHAauthFAIL = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityFAHAauthFAIL.setDescription("\nThis describes the number of FA-HA authentication failed")
mobilityFABadID = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityFABadID.setDescription("\nThis describes the number of mobileIP messages rejected by FA due to bad identification")
mobilityFAMalform = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 5, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityFAMalform.setDescription("\nThis describes the number of mobileIP messages rejected by FA as they are poorly formed")
wlsxMobilityHAFARevocationStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6))
mobilitySentRRVRQ = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilitySentRRVRQ.setDescription("\nThis describes the number of Registration revocation request sent ")
mobilityRcvRRVAck = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityRcvRRVAck.setDescription("\nThis describes the number of Registration revocation ack received")
mobilityRcvRRV = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityRcvRRV.setDescription("\nThis describes the number of Registration revocation request received")
mobilitySentRRVAck = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilitySentRRVAck.setDescription("\nThis describes the number of received Registration revocation request ack sent")
mobilityRRVRQIgnore = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityRRVRQIgnore.setDescription("\nThis describes the number of Registration revocation request ignored")
mobilityRRVAckIgnore = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 9, 6, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mobilityRRVAckIgnore.setDescription("\nThis describes the number of Registration revocation ack Ignored")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("WLSX-MOBILITY-MIB", PYSNMP_MODULE_ID=wlsxMobilityMIB)

# Objects
mibBuilder.exportSymbols("WLSX-MOBILITY-MIB", wlsxMobilityMIB=wlsxMobilityMIB, wlsxMobilityConfigGroup=wlsxMobilityConfigGroup, wlsxMobilityDomainTable=wlsxMobilityDomainTable, wlsxMobilityDomainEntry=wlsxMobilityDomainEntry, mobilityDomainName=mobilityDomainName, mobilityDomainIsExclusive=mobilityDomainIsExclusive, mobilityDomainStatus=mobilityDomainStatus, wlsxMobilityHomeAgentTable=wlsxMobilityHomeAgentTable, wlsxMobilityHomeAgentEntry=wlsxMobilityHomeAgentEntry, mobilityHomeAgentSubnet=mobilityHomeAgentSubnet, mobilityHomeAgentMask=mobilityHomeAgentMask, mobilityHomeAgentIp=mobilityHomeAgentIp, mobilityHomeAgentVlan=mobilityHomeAgentVlan, wlsxMobilityHostTable=wlsxMobilityHostTable, wlsxMobilityHostEntry=wlsxMobilityHostEntry, mobilityHostMac=mobilityHostMac, mobilityHostIp=mobilityHostIp, mobilityHostStatus=mobilityHostStatus, mobilityHostServiceTime=mobilityHostServiceTime, mobilityHostHomeVlan=mobilityHostHomeVlan, mobilityHostHomeNetwork=mobilityHostHomeNetwork, mobilityHostHomeMask=mobilityHostHomeMask, mobilityHostDhcpInfo=mobilityHostDhcpInfo, wlsxMobilityProxyStatsGroup=wlsxMobilityProxyStatsGroup, mobilityProxyPktRx=mobilityProxyPktRx, mobilityProxyPktHandled=mobilityProxyPktHandled, mobilityProxyPktFwd=mobilityProxyPktFwd, mobilityProxyPktDrop=mobilityProxyPktDrop, mobilityProxyBusy=mobilityProxyBusy, mobilityProxyNoMobility=mobilityProxyNoMobility, mobilityProxyClientIPChg=mobilityProxyClientIPChg, mobilityProxyClientEssidChg=mobilityProxyClientEssidChg, wlsxMobilityProxyDHCPStatsGroup=wlsxMobilityProxyDHCPStatsGroup, mobilityProxyDhcpBootpRx=mobilityProxyDhcpBootpRx, mobilityProxyDhcpPktProc=mobilityProxyDhcpPktProc, mobilityProxyDhcpPktFwd=mobilityProxyDhcpPktFwd, mobilityProxyDhcpPktDrop=mobilityProxyDhcpPktDrop, mobilityProxyDHCPNak=mobilityProxyDHCPNak, mobilityProxyBadDHCPPkt=mobilityProxyBadDHCPPkt, mobilityProxyNotDHCP=mobilityProxyNotDHCP, mobilityProxyDHCPNoHomeVlan=mobilityProxyDHCPNoHomeVlan, mobilityProxyDHCPUnexpFrame=mobilityProxyDHCPUnexpFrame, mobilityProxyDHCPUnexpRemote=mobilityProxyDHCPUnexpRemote, wlsxMobilityHAStatsGroup=wlsxMobilityHAStatsGroup, mobilityHARxRRQ=mobilityHARxRRQ, mobilityHASentRRP=mobilityHASentRRP, mobilityHARRQAccept=mobilityHARRQAccept, mobilityHARRQDenied=mobilityHARRQDenied, mobilityHARRQIgnore=mobilityHARRQIgnore, mobilityHARRQAdminDeny=mobilityHARRQAdminDeny, mobilityHARRQNoResource=mobilityHARRQNoResource, mobilityHAMNauthFail=mobilityHAMNauthFail, mobilityHAFAauthFail=mobilityHAFAauthFail, mobilityHABadID=mobilityHABadID, mobilityHAMalform=mobilityHAMalform, mobilityHATooManyBnd=mobilityHATooManyBnd, mobilityHABndExpire=mobilityHABndExpire, wlsxMobilityFAStatsGroup=wlsxMobilityFAStatsGroup, mobilityFASentRRQ=mobilityFASentRRQ, mobilityFARcvRRP=mobilityFARcvRRP, mobilityFARRQAccept=mobilityFARRQAccept, mobilityFARRQReject=mobilityFARRQReject, mobilityMNHAauthFAIL=mobilityMNHAauthFAIL, mobilityFAHAauthFAIL=mobilityFAHAauthFAIL, mobilityFABadID=mobilityFABadID, mobilityFAMalform=mobilityFAMalform, wlsxMobilityHAFARevocationStatsGroup=wlsxMobilityHAFARevocationStatsGroup, mobilitySentRRVRQ=mobilitySentRRVRQ, mobilityRcvRRVAck=mobilityRcvRRVAck, mobilityRcvRRV=mobilityRcvRRV, mobilitySentRRVAck=mobilitySentRRVAck, mobilityRRVRQIgnore=mobilityRRVRQIgnore, mobilityRRVAckIgnore=mobilityRRVAckIgnore)

