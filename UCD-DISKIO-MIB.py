# PySNMP SMI module. Autogenerated from smidump -f python UCD-DISKIO-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:17 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Counter32, Counter64, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")
( ucdExperimental, ) = mibBuilder.importSymbols("UCD-SNMP-MIB", "ucdExperimental")

# Objects

ucdDiskIOMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2021, 13, 15)).setRevisions(("2005-04-20 00:00","2000-01-26 00:00","2000-01-26 00:00",))
if mibBuilder.loadTexts: ucdDiskIOMIB.setOrganization("University of California, Davis")
if mibBuilder.loadTexts: ucdDiskIOMIB.setContactInfo("This mib is no longer being maintained by the University of\nCalifornia and is now in life-support-mode and being\nmaintained by the net-snmp project.  The best place to write\nfor public questions about the net-snmp-coders mailing list\nat net-snmp-coders@lists.sourceforge.net.\n\npostal:   Wes Hardaker\n         P.O. Box 382\n         Davis CA  95617\n\nemail:    net-snmp-coders@lists.sourceforge.net")
if mibBuilder.loadTexts: ucdDiskIOMIB.setDescription("This MIB module defines objects for disk IO statistics.")
diskIOTable = MibTable((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1))
if mibBuilder.loadTexts: diskIOTable.setDescription("Table of IO devices and how much data they have read/written.")
diskIOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1)).setIndexNames((0, "UCD-DISKIO-MIB", "diskIOIndex"))
if mibBuilder.loadTexts: diskIOEntry.setDescription("An entry containing a device and its statistics.")
diskIOIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOIndex.setDescription("Reference index for each observed device.")
diskIODevice = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIODevice.setDescription("The name of the device we are counting/checking.")
diskIONRead = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONRead.setDescription("The number of bytes read from this device since boot.")
diskIONWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONWritten.setDescription("The number of bytes written to this device since boot.")
diskIOReads = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOReads.setDescription("The number of read accesses from this device since boot.")
diskIOWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOWrites.setDescription("The number of write accesses to this device since boot.")
diskIOLA1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOLA1.setDescription("The 1 minute average load of disk (%)")
diskIOLA5 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOLA5.setDescription("The 5 minute average load of disk (%)")
diskIOLA15 = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIOLA15.setDescription("The 15 minute average load of disk (%)")
diskIONReadX = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONReadX.setDescription("The number of bytes read from this device since boot.")
diskIONWrittenX = MibTableColumn((1, 3, 6, 1, 4, 1, 2021, 13, 15, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: diskIONWrittenX.setDescription("The number of bytes written to this device since boot.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("UCD-DISKIO-MIB", PYSNMP_MODULE_ID=ucdDiskIOMIB)

# Objects
mibBuilder.exportSymbols("UCD-DISKIO-MIB", ucdDiskIOMIB=ucdDiskIOMIB, diskIOTable=diskIOTable, diskIOEntry=diskIOEntry, diskIOIndex=diskIOIndex, diskIODevice=diskIODevice, diskIONRead=diskIONRead, diskIONWritten=diskIONWritten, diskIOReads=diskIOReads, diskIOWrites=diskIOWrites, diskIOLA1=diskIOLA1, diskIOLA5=diskIOLA5, diskIOLA15=diskIOLA15, diskIONReadX=diskIONReadX, diskIONWrittenX=diskIONWrittenX)

