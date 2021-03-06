# PySNMP SMI module. Autogenerated from smidump -f python LLDP-MIB
# by libsmi2pysnmp-0.0.7-alpha at Wed Jun 22 13:58:11 2011,
# Python version (2, 6, 6, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pyasn1.type import constraint, namedval

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( AddressFamilyNumbers, ) = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
( TimeFilter, ZeroBasedCounter32, ) = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter", "ZeroBasedCounter32")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "TruthValue")

# Types

class LldpChassisId(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,255)
    pass

class LldpChassisIdSubtype(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(2,5,6,4,1,7,3,)
    namedValues = namedval.NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7), )
    pass

class LldpManAddrIfSubtype(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,3,2,)
    namedValues = namedval.NamedValues(("unknown", 1), ("ifIndex", 2), ("systemPortNumber", 3), )
    pass

class LldpManAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,31)
    pass

class LldpPortId(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(1,255)
    pass

class LldpPortIdSubtype(Integer):
    subtypeSpec = Integer.subtypeSpec+constraint.SingleValueConstraint(1,4,5,3,6,7,2,)
    namedValues = namedval.NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7), )
    pass

class LldpPortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec+constraint.ValueSizeConstraint(0,512)
    pass

class LldpPortNumber(TextualConvention, Integer32):
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec+constraint.ValueRangeConstraint(1,4096)
    pass

class LldpSystemCapabilitiesMap(Bits):
    namedValues = namedval.NamedValues(("other", 0), ("repeater", 1), ("bridge", 2), ("wlanAccessPoint", 3), ("router", 4), ("telephone", 5), ("docsisCableDevice", 6), ("stationOnly", 7), )
    pass


# Objects

lldpMIB = ModuleIdentity((1, 0, 8802, 1, 1, 2)).setRevisions(("2005-05-06 00:00",))
lldpNotifications = MibIdentifier((1, 0, 8802, 1, 1, 2, 0))
lldpNotificationPrefix = MibIdentifier((1, 0, 8802, 1, 1, 2, 0, 0))
lldpObjects = MibIdentifier((1, 0, 8802, 1, 1, 2, 1))
lldpConfiguration = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 1))
lldpMessageTxInterval = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(5, 32768)).clone(30)).setMaxAccess("readwrite").setUnits("seconds")
lldpMessageTxHoldMultiplier = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
lldpReinitDelay = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite").setUnits("seconds")
lldpTxDelay = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 8192)).clone(2)).setMaxAccess("readwrite").setUnits("seconds")
lldpNotificationInterval = MibScalar((1, 0, 8802, 1, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(5, 3600)).clone(5)).setMaxAccess("readwrite").setUnits("seconds")
lldpPortConfigTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 1, 6))
lldpPortConfigEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1)).setIndexNames((0, "LLDP-MIB", "lldpPortConfigPortNum"))
lldpPortConfigPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 1), LldpPortNumber()).setMaxAccess("noaccess")
lldpPortConfigAdminStatus = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 2), Integer().subtype(subtypeSpec=constraint.SingleValueConstraint(4,2,1,3,)).subtype(namedValues=namedval.NamedValues(("txOnly", 1), ("rxOnly", 2), ("txAndRx", 3), ("disabled", 4), )).clone(3)).setMaxAccess("readwrite")
lldpPortConfigNotificationEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
lldpPortConfigTLVsTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 6, 1, 4), Bits().subtype(namedValues=namedval.NamedValues(("portDesc", 0), ("sysName", 1), ("sysDesc", 2), ("sysCap", 3), )).clone(())).setMaxAccess("readwrite")
lldpConfigManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 1, 7))
lldpConfigManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 1, 7, 1))
lldpConfigManAddrPortsTxEnable = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 1, 7, 1, 1), LldpPortList().clone('')).setMaxAccess("readwrite")
lldpStatistics = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 2))
lldpStatsRemTablesLastChangeTime = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
lldpStatsRemTablesInserts = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 2), ZeroBasedCounter32()).setMaxAccess("readonly").setUnits("table entries")
lldpStatsRemTablesDeletes = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 3), ZeroBasedCounter32()).setMaxAccess("readonly").setUnits("table entries")
lldpStatsRemTablesDrops = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 4), ZeroBasedCounter32()).setMaxAccess("readonly").setUnits("table entries")
lldpStatsRemTablesAgeouts = MibScalar((1, 0, 8802, 1, 1, 2, 1, 2, 5), ZeroBasedCounter32()).setMaxAccess("readonly")
lldpStatsTxPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 2, 6))
lldpStatsTxPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1)).setIndexNames((0, "LLDP-MIB", "lldpStatsTxPortNum"))
lldpStatsTxPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 1), LldpPortNumber()).setMaxAccess("noaccess")
lldpStatsTxPortFramesTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 2, 7))
lldpStatsRxPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1)).setIndexNames((0, "LLDP-MIB", "lldpStatsRxPortNum"))
lldpStatsRxPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 1), LldpPortNumber()).setMaxAccess("noaccess")
lldpStatsRxPortFramesDiscardedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 2), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortFramesErrors = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 3), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortFramesTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 4), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortTLVsDiscardedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 5), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortTLVsUnrecognizedTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 6), Counter32()).setMaxAccess("readonly")
lldpStatsRxPortAgeoutsTotal = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 2, 7, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
lldpLocalSystemData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 3))
lldpLocChassisIdSubtype = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 1), LldpChassisIdSubtype()).setMaxAccess("readonly")
lldpLocChassisId = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 2), LldpChassisId()).setMaxAccess("readonly")
lldpLocSysName = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 3), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
lldpLocSysDesc = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 4), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
lldpLocSysCapSupported = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 5), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
lldpLocSysCapEnabled = MibScalar((1, 0, 8802, 1, 1, 2, 1, 3, 6), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
lldpLocPortTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 3, 7))
lldpLocPortEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1)).setIndexNames((0, "LLDP-MIB", "lldpLocPortNum"))
lldpLocPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 1), LldpPortNumber()).setMaxAccess("noaccess")
lldpLocPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 2), LldpPortIdSubtype()).setMaxAccess("readonly")
lldpLocPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 3), LldpPortId()).setMaxAccess("readonly")
lldpLocPortDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 7, 1, 4), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
lldpLocManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 3, 8))
lldpLocManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1)).setIndexNames((0, "LLDP-MIB", "lldpLocManAddrSubtype"), (0, "LLDP-MIB", "lldpLocManAddr"))
lldpLocManAddrSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 1), AddressFamilyNumbers()).setMaxAccess("noaccess")
lldpLocManAddr = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 2), LldpManAddress()).setMaxAccess("noaccess")
lldpLocManAddrLen = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 3), Integer32()).setMaxAccess("readonly")
lldpLocManAddrIfSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 4), LldpManAddrIfSubtype()).setMaxAccess("readonly")
lldpLocManAddrIfId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 5), Integer32()).setMaxAccess("readonly")
lldpLocManAddrOID = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 3, 8, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
lldpRemoteSystemsData = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 4))
lldpRemTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 1))
lldpRemEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1)).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
lldpRemTimeMark = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 1), TimeFilter()).setMaxAccess("noaccess")
lldpRemLocalPortNum = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 2), LldpPortNumber()).setMaxAccess("noaccess")
lldpRemIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
lldpRemChassisIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 4), LldpChassisIdSubtype()).setMaxAccess("readonly")
lldpRemChassisId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 5), LldpChassisId()).setMaxAccess("readonly")
lldpRemPortIdSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 6), LldpPortIdSubtype()).setMaxAccess("readonly")
lldpRemPortId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 7), LldpPortId()).setMaxAccess("readonly")
lldpRemPortDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
lldpRemSysName = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 9), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
lldpRemSysDesc = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
lldpRemSysCapSupported = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 11), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
lldpRemSysCapEnabled = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 1, 1, 12), LldpSystemCapabilitiesMap()).setMaxAccess("readonly")
lldpRemManAddrTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 2))
lldpRemManAddrEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1)).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemManAddrSubtype"), (0, "LLDP-MIB", "lldpRemManAddr"))
lldpRemManAddrSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 1), AddressFamilyNumbers()).setMaxAccess("noaccess")
lldpRemManAddr = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 2), LldpManAddress()).setMaxAccess("noaccess")
lldpRemManAddrIfSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 3), LldpManAddrIfSubtype()).setMaxAccess("readonly")
lldpRemManAddrIfId = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
lldpRemManAddrOID = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 2, 1, 5), ObjectIdentifier()).setMaxAccess("readonly")
lldpRemUnknownTLVTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 3))
lldpRemUnknownTLVEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1)).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemUnknownTLVType"))
lldpRemUnknownTLVType = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(9, 126))).setMaxAccess("noaccess")
lldpRemUnknownTLVInfo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 3, 1, 2), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 511))).setMaxAccess("readonly")
lldpRemOrgDefInfoTable = MibTable((1, 0, 8802, 1, 1, 2, 1, 4, 4))
lldpRemOrgDefInfoEntry = MibTableRow((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1)).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"), (0, "LLDP-MIB", "lldpRemOrgDefInfoOUI"), (0, "LLDP-MIB", "lldpRemOrgDefInfoSubtype"), (0, "LLDP-MIB", "lldpRemOrgDefInfoIndex"))
lldpRemOrgDefInfoOUI = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 1), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("noaccess")
lldpRemOrgDefInfoSubtype = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 2), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 255))).setMaxAccess("noaccess")
lldpRemOrgDefInfoIndex = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 2147483647L))).setMaxAccess("noaccess")
lldpRemOrgDefInfo = MibTableColumn((1, 0, 8802, 1, 1, 2, 1, 4, 4, 1, 4), OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(0, 507))).setMaxAccess("readonly")
lldpExtensions = MibIdentifier((1, 0, 8802, 1, 1, 2, 1, 5))
lldpConformance = MibIdentifier((1, 0, 8802, 1, 1, 2, 2))
lldpCompliances = MibIdentifier((1, 0, 8802, 1, 1, 2, 2, 1))
lldpGroups = MibIdentifier((1, 0, 8802, 1, 1, 2, 2, 2))

# Augmentions
lldpLocManAddrEntry.registerAugmentions(("LLDP-MIB", "lldpConfigManAddrEntry"))
apply(lldpConfigManAddrEntry.setIndexNames, lldpLocManAddrEntry.getIndexNames())

# Notifications

lldpRemTablesChange = NotificationType((1, 0, 8802, 1, 1, 2, 0, 0, 1)).setObjects(("LLDP-MIB", "lldpStatsRemTablesDeletes"), ("LLDP-MIB", "lldpStatsRemTablesAgeouts"), ("LLDP-MIB", "lldpStatsRemTablesDrops"), ("LLDP-MIB", "lldpStatsRemTablesInserts"), )

# Groups

lldpConfigGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 1)).setObjects(("LLDP-MIB", "lldpPortConfigAdminStatus"), )
lldpConfigRxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 2)).setObjects(("LLDP-MIB", "lldpNotificationInterval"), ("LLDP-MIB", "lldpPortConfigNotificationEnable"), )
lldpConfigTxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 3)).setObjects(("LLDP-MIB", "lldpConfigManAddrPortsTxEnable"), ("LLDP-MIB", "lldpMessageTxHoldMultiplier"), ("LLDP-MIB", "lldpTxDelay"), ("LLDP-MIB", "lldpReinitDelay"), ("LLDP-MIB", "lldpPortConfigTLVsTxEnable"), ("LLDP-MIB", "lldpMessageTxInterval"), )
lldpStatsRxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 4)).setObjects(("LLDP-MIB", "lldpStatsRxPortFramesTotal"), ("LLDP-MIB", "lldpStatsRemTablesAgeouts"), ("LLDP-MIB", "lldpStatsRemTablesDrops"), ("LLDP-MIB", "lldpStatsRxPortTLVsDiscardedTotal"), ("LLDP-MIB", "lldpStatsRxPortFramesDiscardedTotal"), ("LLDP-MIB", "lldpStatsRemTablesDeletes"), ("LLDP-MIB", "lldpStatsRxPortTLVsUnrecognizedTotal"), ("LLDP-MIB", "lldpStatsRemTablesLastChangeTime"), ("LLDP-MIB", "lldpStatsRxPortFramesErrors"), ("LLDP-MIB", "lldpStatsRxPortAgeoutsTotal"), ("LLDP-MIB", "lldpStatsRemTablesInserts"), )
lldpNotificationsGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 8)).setObjects(("LLDP-MIB", "lldpRemTablesChange"), )
lldpLocSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 6)).setObjects(("LLDP-MIB", "lldpLocManAddrOID"), ("LLDP-MIB", "lldpLocSysName"), ("LLDP-MIB", "lldpLocSysCapSupported"), ("LLDP-MIB", "lldpLocSysDesc"), ("LLDP-MIB", "lldpLocChassisIdSubtype"), ("LLDP-MIB", "lldpLocPortId"), ("LLDP-MIB", "lldpLocPortDesc"), ("LLDP-MIB", "lldpLocSysCapEnabled"), ("LLDP-MIB", "lldpLocManAddrIfId"), ("LLDP-MIB", "lldpLocChassisId"), ("LLDP-MIB", "lldpLocPortIdSubtype"), ("LLDP-MIB", "lldpLocManAddrIfSubtype"), ("LLDP-MIB", "lldpLocManAddrLen"), )
lldpStatsTxGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 5)).setObjects(("LLDP-MIB", "lldpStatsTxPortFramesTotal"), )
lldpRemSysGroup = ObjectGroup((1, 0, 8802, 1, 1, 2, 2, 2, 7)).setObjects(("LLDP-MIB", "lldpRemManAddrIfSubtype"), ("LLDP-MIB", "lldpRemManAddrIfId"), ("LLDP-MIB", "lldpRemPortIdSubtype"), ("LLDP-MIB", "lldpRemSysDesc"), ("LLDP-MIB", "lldpRemChassisIdSubtype"), ("LLDP-MIB", "lldpRemUnknownTLVInfo"), ("LLDP-MIB", "lldpRemSysName"), ("LLDP-MIB", "lldpRemChassisId"), ("LLDP-MIB", "lldpRemPortId"), ("LLDP-MIB", "lldpRemSysCapEnabled"), ("LLDP-MIB", "lldpRemOrgDefInfo"), ("LLDP-MIB", "lldpRemManAddrOID"), ("LLDP-MIB", "lldpRemSysCapSupported"), ("LLDP-MIB", "lldpRemPortDesc"), )

# Exports

# Module identity
mibBuilder.exportSymbols("LLDP-MIB", PYSNMP_MODULE_ID=lldpMIB)

# Types
mibBuilder.exportSymbols("LLDP-MIB", LldpChassisId=LldpChassisId, LldpChassisIdSubtype=LldpChassisIdSubtype, LldpManAddrIfSubtype=LldpManAddrIfSubtype, LldpManAddress=LldpManAddress, LldpPortId=LldpPortId, LldpPortIdSubtype=LldpPortIdSubtype, LldpPortList=LldpPortList, LldpPortNumber=LldpPortNumber, LldpSystemCapabilitiesMap=LldpSystemCapabilitiesMap)

# Objects
mibBuilder.exportSymbols("LLDP-MIB", lldpMIB=lldpMIB, lldpNotifications=lldpNotifications, lldpNotificationPrefix=lldpNotificationPrefix, lldpObjects=lldpObjects, lldpConfiguration=lldpConfiguration, lldpMessageTxInterval=lldpMessageTxInterval, lldpMessageTxHoldMultiplier=lldpMessageTxHoldMultiplier, lldpReinitDelay=lldpReinitDelay, lldpTxDelay=lldpTxDelay, lldpNotificationInterval=lldpNotificationInterval, lldpPortConfigTable=lldpPortConfigTable, lldpPortConfigEntry=lldpPortConfigEntry, lldpPortConfigPortNum=lldpPortConfigPortNum, lldpPortConfigAdminStatus=lldpPortConfigAdminStatus, lldpPortConfigNotificationEnable=lldpPortConfigNotificationEnable, lldpPortConfigTLVsTxEnable=lldpPortConfigTLVsTxEnable, lldpConfigManAddrTable=lldpConfigManAddrTable, lldpConfigManAddrEntry=lldpConfigManAddrEntry, lldpConfigManAddrPortsTxEnable=lldpConfigManAddrPortsTxEnable, lldpStatistics=lldpStatistics, lldpStatsRemTablesLastChangeTime=lldpStatsRemTablesLastChangeTime, lldpStatsRemTablesInserts=lldpStatsRemTablesInserts, lldpStatsRemTablesDeletes=lldpStatsRemTablesDeletes, lldpStatsRemTablesDrops=lldpStatsRemTablesDrops, lldpStatsRemTablesAgeouts=lldpStatsRemTablesAgeouts, lldpStatsTxPortTable=lldpStatsTxPortTable, lldpStatsTxPortEntry=lldpStatsTxPortEntry, lldpStatsTxPortNum=lldpStatsTxPortNum, lldpStatsTxPortFramesTotal=lldpStatsTxPortFramesTotal, lldpStatsRxPortTable=lldpStatsRxPortTable, lldpStatsRxPortEntry=lldpStatsRxPortEntry, lldpStatsRxPortNum=lldpStatsRxPortNum, lldpStatsRxPortFramesDiscardedTotal=lldpStatsRxPortFramesDiscardedTotal, lldpStatsRxPortFramesErrors=lldpStatsRxPortFramesErrors, lldpStatsRxPortFramesTotal=lldpStatsRxPortFramesTotal, lldpStatsRxPortTLVsDiscardedTotal=lldpStatsRxPortTLVsDiscardedTotal, lldpStatsRxPortTLVsUnrecognizedTotal=lldpStatsRxPortTLVsUnrecognizedTotal, lldpStatsRxPortAgeoutsTotal=lldpStatsRxPortAgeoutsTotal, lldpLocalSystemData=lldpLocalSystemData, lldpLocChassisIdSubtype=lldpLocChassisIdSubtype, lldpLocChassisId=lldpLocChassisId, lldpLocSysName=lldpLocSysName, lldpLocSysDesc=lldpLocSysDesc, lldpLocSysCapSupported=lldpLocSysCapSupported, lldpLocSysCapEnabled=lldpLocSysCapEnabled, lldpLocPortTable=lldpLocPortTable, lldpLocPortEntry=lldpLocPortEntry, lldpLocPortNum=lldpLocPortNum, lldpLocPortIdSubtype=lldpLocPortIdSubtype, lldpLocPortId=lldpLocPortId, lldpLocPortDesc=lldpLocPortDesc, lldpLocManAddrTable=lldpLocManAddrTable, lldpLocManAddrEntry=lldpLocManAddrEntry, lldpLocManAddrSubtype=lldpLocManAddrSubtype, lldpLocManAddr=lldpLocManAddr, lldpLocManAddrLen=lldpLocManAddrLen, lldpLocManAddrIfSubtype=lldpLocManAddrIfSubtype, lldpLocManAddrIfId=lldpLocManAddrIfId, lldpLocManAddrOID=lldpLocManAddrOID, lldpRemoteSystemsData=lldpRemoteSystemsData, lldpRemTable=lldpRemTable, lldpRemEntry=lldpRemEntry, lldpRemTimeMark=lldpRemTimeMark, lldpRemLocalPortNum=lldpRemLocalPortNum, lldpRemIndex=lldpRemIndex, lldpRemChassisIdSubtype=lldpRemChassisIdSubtype, lldpRemChassisId=lldpRemChassisId, lldpRemPortIdSubtype=lldpRemPortIdSubtype, lldpRemPortId=lldpRemPortId, lldpRemPortDesc=lldpRemPortDesc, lldpRemSysName=lldpRemSysName, lldpRemSysDesc=lldpRemSysDesc, lldpRemSysCapSupported=lldpRemSysCapSupported, lldpRemSysCapEnabled=lldpRemSysCapEnabled, lldpRemManAddrTable=lldpRemManAddrTable, lldpRemManAddrEntry=lldpRemManAddrEntry, lldpRemManAddrSubtype=lldpRemManAddrSubtype, lldpRemManAddr=lldpRemManAddr, lldpRemManAddrIfSubtype=lldpRemManAddrIfSubtype, lldpRemManAddrIfId=lldpRemManAddrIfId, lldpRemManAddrOID=lldpRemManAddrOID, lldpRemUnknownTLVTable=lldpRemUnknownTLVTable, lldpRemUnknownTLVEntry=lldpRemUnknownTLVEntry, lldpRemUnknownTLVType=lldpRemUnknownTLVType, lldpRemUnknownTLVInfo=lldpRemUnknownTLVInfo, lldpRemOrgDefInfoTable=lldpRemOrgDefInfoTable, lldpRemOrgDefInfoEntry=lldpRemOrgDefInfoEntry, lldpRemOrgDefInfoOUI=lldpRemOrgDefInfoOUI, lldpRemOrgDefInfoSubtype=lldpRemOrgDefInfoSubtype, lldpRemOrgDefInfoIndex=lldpRemOrgDefInfoIndex, lldpRemOrgDefInfo=lldpRemOrgDefInfo, lldpExtensions=lldpExtensions, lldpConformance=lldpConformance, lldpCompliances=lldpCompliances, lldpGroups=lldpGroups)

# Notifications
mibBuilder.exportSymbols("LLDP-MIB", lldpRemTablesChange=lldpRemTablesChange)

# Groups
mibBuilder.exportSymbols("LLDP-MIB", lldpConfigGroup=lldpConfigGroup, lldpConfigRxGroup=lldpConfigRxGroup, lldpConfigTxGroup=lldpConfigTxGroup, lldpStatsRxGroup=lldpStatsRxGroup, lldpNotificationsGroup=lldpNotificationsGroup, lldpLocSysGroup=lldpLocSysGroup, lldpStatsTxGroup=lldpStatsTxGroup, lldpRemSysGroup=lldpRemSysGroup)
