# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-SET-DHCP-MIB
# by libsmi2pysnmp-0.1.3 at Fri May 30 14:12:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenSetting, netscreenSettingMibModule, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

netscreenSetDhcpMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 5)).setRevisions(("2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-10 00:00","2001-12-12 00:00","2001-09-28 00:00","2001-05-27 00:00",))
if mibBuilder.loadTexts: netscreenSetDhcpMibModule.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: netscreenSetDhcpMibModule.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: netscreenSetDhcpMibModule.setDescription("This module defines the object that are used to monitor all\nthe configuration info")
nsSetDHCP = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 5))
nsSetDhcpTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1))
if mibBuilder.loadTexts: nsSetDhcpTable.setDescription("NetScreen ScreenOS can allow dhcp service on each of NetScreen\ndevice's physical interface. This table collects the dhcp\nconfiguration on each physical interface.")
nsSetDhcpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1)).setIndexNames((0, "NETSCREEN-SET-DHCP-MIB", "nsSetDhcpIfIdx"))
if mibBuilder.loadTexts: nsSetDhcpEntry.setDescription("Hold the firewall setting attribute.")
nsSetDhcpIfIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDhcpIfIdx.setDescription("unique interface id.")
nsSetDHCPService = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,0,)).subtype(namedValues=NamedValues(("none", 0), ("dhcp-relay-agent", 1), ("dhcp-server", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDHCPService.setDescription("DHCP service type for trusted network.")
nsSetDHCPRelayServer = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDHCPRelayServer.setDescription("DHCP relay agent server name.")
nsSetDHCPVpnEncryp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDHCPVpnEncryp.setDescription("Secure DHCP relay agent traffic via VPN encryption.")
nsSetDhcpIfInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 7, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetDhcpIfInfo.setDescription("Internal id assigned to this interface. Stays persistent across resets.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-SET-DHCP-MIB", PYSNMP_MODULE_ID=netscreenSetDhcpMibModule)

# Objects
mibBuilder.exportSymbols("NETSCREEN-SET-DHCP-MIB", netscreenSetDhcpMibModule=netscreenSetDhcpMibModule, nsSetDHCP=nsSetDHCP, nsSetDhcpTable=nsSetDhcpTable, nsSetDhcpEntry=nsSetDhcpEntry, nsSetDhcpIfIdx=nsSetDhcpIfIdx, nsSetDHCPService=nsSetDHCPService, nsSetDHCPRelayServer=nsSetDHCPRelayServer, nsSetDHCPVpnEncryp=nsSetDHCPVpnEncryp, nsSetDhcpIfInfo=nsSetDhcpIfInfo)
