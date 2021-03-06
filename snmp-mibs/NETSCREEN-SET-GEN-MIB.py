# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-SET-GEN-MIB
# by libsmi2pysnmp-0.1.3 at Fri May 30 14:12:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenSetting, netscreenSettingMibModule, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
( Bits, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

netscreenSetGenMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 1)).setRevisions(("2005-08-12 00:00","2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-10 00:00","2001-09-28 00:00","2001-05-27 00:00",))
if mibBuilder.loadTexts: netscreenSetGenMibModule.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: netscreenSetGenMibModule.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: netscreenSetGenMibModule.setDescription("obsolete nsSetGenSysIp")
nsSetGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 1))
nsSetGenSysIp = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGenSysIp.setDescription("System Ip address")
nsSetGenHostName = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGenHostName.setDescription("Host name of NetScreen device.")
nsSetGenDomain = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGenDomain.setDescription("Domain name of NetScreen device.")
nsSetGenOpMode = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGenOpMode.setDescription("NetScreen device can work in one of the tree mode:\ntransparent, NAT  and route. This attribute indicates which\noperation mode it use.")
nsSetGenSwVer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGenSwVer.setDescription("NetSceen OS version.")
nsSetGenLicInfo = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGenLicInfo.setDescription("NetScreen OS license information.")
nsSetGenSCSAdminEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGenSCSAdminEnable.setDescription("enable Command Security Shell")
nsSetGenDropSelfLogPac = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("disable", 0), ("enabled", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetGenDropSelfLogPac.setDescription("Log Packets to Self that are dropped")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-SET-GEN-MIB", PYSNMP_MODULE_ID=netscreenSetGenMibModule)

# Objects
mibBuilder.exportSymbols("NETSCREEN-SET-GEN-MIB", netscreenSetGenMibModule=netscreenSetGenMibModule, nsSetGeneral=nsSetGeneral, nsSetGenSysIp=nsSetGenSysIp, nsSetGenHostName=nsSetGenHostName, nsSetGenDomain=nsSetGenDomain, nsSetGenOpMode=nsSetGenOpMode, nsSetGenSwVer=nsSetGenSwVer, nsSetGenLicInfo=nsSetGenLicInfo, nsSetGenSCSAdminEnable=nsSetGenSCSAdminEnable, nsSetGenDropSelfLogPac=nsSetGenDropSelfLogPac)

