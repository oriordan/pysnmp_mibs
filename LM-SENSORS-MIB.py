# PySNMP SMI module. Autogenerated from smidump -f python LM-SENSORS-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:46 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")
( ucdExperimental, ) = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")

# Objects

lmSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 2021, 13, 16))
lmSensorsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 16, 1)).setRevisions(("2000-11-05 00:00",))
if mibBuilder.loadTexts: lmSensorsMIB.setOrganization("AdamsNames Ltd")
if mibBuilder.loadTexts: lmSensorsMIB.setContactInfo("Primary Contact: M J Oldfield\nemail:     m@mail.tc")
if mibBuilder.loadTexts: lmSensorsMIB.setDescription("This MIB module defines objects for lm_sensor derived data.")
lmTempSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2))
if mibBuilder.loadTexts: lmTempSensorsTable.setDescription("Table of temperature sensors and their values.")
lmTempSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1)).setIndexNames((0, "LM-SENSORS-MIB", "lmTempSensorsIndex"))
if mibBuilder.loadTexts: lmTempSensorsEntry.setDescription("An entry containing a device and its statistics.")
lmTempSensorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmTempSensorsIndex.setDescription("Reference index for each observed device.")
lmTempSensorsDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmTempSensorsDevice.setDescription("The name of the temperature sensor we are reading.")
lmTempSensorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmTempSensorsValue.setDescription("The temperature of this sensor in mC.")
lmFanSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3))
if mibBuilder.loadTexts: lmFanSensorsTable.setDescription("Table of fan sensors and their values.")
lmFanSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1)).setIndexNames((0, "LM-SENSORS-MIB", "lmFanSensorsIndex"))
if mibBuilder.loadTexts: lmFanSensorsEntry.setDescription("An entry containing a device and its statistics.")
lmFanSensorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmFanSensorsIndex.setDescription("Reference index for each observed device.")
lmFanSensorsDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmFanSensorsDevice.setDescription("The name of the fan sensor we are reading.")
lmFanSensorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 3, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmFanSensorsValue.setDescription("The rotation speed of the fan in RPM.")
lmVoltSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4))
if mibBuilder.loadTexts: lmVoltSensorsTable.setDescription("Table of voltage sensors and their values.")
lmVoltSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1)).setIndexNames((0, "LM-SENSORS-MIB", "lmVoltSensorsIndex"))
if mibBuilder.loadTexts: lmVoltSensorsEntry.setDescription("An entry containing a device and its statistics.")
lmVoltSensorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmVoltSensorsIndex.setDescription("Reference index for each observed device.")
lmVoltSensorsDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmVoltSensorsDevice.setDescription("The name of the device we are reading.")
lmVoltSensorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmVoltSensorsValue.setDescription("The voltage in mV.")
lmMiscSensorsTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5))
if mibBuilder.loadTexts: lmMiscSensorsTable.setDescription("Table of miscellaneous sensor devices and their values.")
lmMiscSensorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1)).setIndexNames((0, "LM-SENSORS-MIB", "lmMiscSensorsIndex"))
if mibBuilder.loadTexts: lmMiscSensorsEntry.setDescription("An entry containing a device and its statistics.")
lmMiscSensorsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmMiscSensorsIndex.setDescription("Reference index for each observed device.")
lmMiscSensorsDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmMiscSensorsDevice.setDescription("The name of the device we are reading.")
lmMiscSensorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 16, 5, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lmMiscSensorsValue.setDescription("The value of this sensor.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("LM-SENSORS-MIB", PYSNMP_MODULE_ID=lmSensorsMIB)

# Objects
mibBuilder.exportSymbols("LM-SENSORS-MIB", lmSensors=lmSensors, lmSensorsMIB=lmSensorsMIB, lmTempSensorsTable=lmTempSensorsTable, lmTempSensorsEntry=lmTempSensorsEntry, lmTempSensorsIndex=lmTempSensorsIndex, lmTempSensorsDevice=lmTempSensorsDevice, lmTempSensorsValue=lmTempSensorsValue, lmFanSensorsTable=lmFanSensorsTable, lmFanSensorsEntry=lmFanSensorsEntry, lmFanSensorsIndex=lmFanSensorsIndex, lmFanSensorsDevice=lmFanSensorsDevice, lmFanSensorsValue=lmFanSensorsValue, lmVoltSensorsTable=lmVoltSensorsTable, lmVoltSensorsEntry=lmVoltSensorsEntry, lmVoltSensorsIndex=lmVoltSensorsIndex, lmVoltSensorsDevice=lmVoltSensorsDevice, lmVoltSensorsValue=lmVoltSensorsValue, lmMiscSensorsTable=lmMiscSensorsTable, lmMiscSensorsEntry=lmMiscSensorsEntry, lmMiscSensorsIndex=lmMiscSensorsIndex, lmMiscSensorsDevice=lmMiscSensorsDevice, lmMiscSensorsValue=lmMiscSensorsValue)

