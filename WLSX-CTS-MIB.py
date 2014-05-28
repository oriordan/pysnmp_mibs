# PySNMP SMI module. Autogenerated from smidump -f python WLSX-CTS-MIB
# by libsmi2pysnmp-0.1.3 at Tue May 27 09:00:43 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( wlsxEnterpriseMibModules, ) = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "snmpModules")
( DisplayString, MacAddress, PhysAddress, RowStatus, StorageType, TAddress, TDomain, TextualConvention, TestAndIncr, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "PhysAddress", "RowStatus", "StorageType", "TAddress", "TDomain", "TextualConvention", "TestAndIncr", "TimeInterval", "TruthValue")

# Objects

wlsxCtsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11)).setRevisions(("1907-08-06 05:18",))
if mibBuilder.loadTexts: wlsxCtsMIB.setOrganization("Aruba Wireless Networks")
if mibBuilder.loadTexts: wlsxCtsMIB.setContactInfo("Postal:    1322 Crossman Avenue\nSunnyvale, CA 94089	\nE-mail:     dl-support@arubanetworks.com\nPhone:      +1 408 227 4500")
if mibBuilder.loadTexts: wlsxCtsMIB.setDescription("This MIB module defines MIB objects which provide\ninformation about the Controller Transport Service (Cts) in the \n		Aruba controller.")
wlsxCtsOpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1))
wlsxCtsRequestTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1))
if mibBuilder.loadTexts: wlsxCtsRequestTable.setDescription("")
wlsxCtsRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1)).setIndexNames((0, "WLSX-CTS-MIB", "wlsxCtsIndex"))
if mibBuilder.loadTexts: wlsxCtsRequestEntry.setDescription("")
wlsxCtsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 1), Integer32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: wlsxCtsIndex.setDescription("\nCTS transport index \n0 - Config Sync\n1 - Counters Sync\n2 - RF Plan Sync")
wlsxCtsOpcode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxCtsOpcode.setDescription("\nCTS operation opcode")
wlsxCtsCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxCtsCookie.setDescription("\nCookie for the config sync operation")
wlsxCtsURL = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxCtsURL.setDescription("\nURL for the config sync operation")
wlsxCtsFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 5), Bits().subtype(namedValues=NamedValues(("wlsxCtsFlagForce", 0), ("wlsxCtsFlagUseCert", 1), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxCtsFlags.setDescription("\nOperational flags to be sent via CTS")
wlsxCtsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 11, 1, 1, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wlsxCtsStatus.setDescription("\nCTS row status")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("WLSX-CTS-MIB", PYSNMP_MODULE_ID=wlsxCtsMIB)

# Objects
mibBuilder.exportSymbols("WLSX-CTS-MIB", wlsxCtsMIB=wlsxCtsMIB, wlsxCtsOpGroup=wlsxCtsOpGroup, wlsxCtsRequestTable=wlsxCtsRequestTable, wlsxCtsRequestEntry=wlsxCtsRequestEntry, wlsxCtsIndex=wlsxCtsIndex, wlsxCtsOpcode=wlsxCtsOpcode, wlsxCtsCookie=wlsxCtsCookie, wlsxCtsURL=wlsxCtsURL, wlsxCtsFlags=wlsxCtsFlags, wlsxCtsStatus=wlsxCtsStatus)

