# PySNMP SMI module. Autogenerated from smidump -f python MPLS-LC-ATM-STD-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:04 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( AtmVpIdentifier, ) = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier")
( mplsInterfaceIndex, ) = mibBuilder.importSymbols("MPLS-LSR-STD-MIB", "mplsInterfaceIndex")
( MplsAtmVcIdentifier, mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsAtmVcIdentifier", "mplsStdMIB")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( RowStatus, StorageType, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TruthValue")

# Objects

mplsLcAtmStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 9)).setRevisions(("2006-01-12 00:00",))
if mibBuilder.loadTexts: mplsLcAtmStdMIB.setOrganization("Multiprotocol Label Switching (MPLS) Working Group")
if mibBuilder.loadTexts: mplsLcAtmStdMIB.setContactInfo("        Thomas D. Nadeau\nPostal: Cisco Systems, Inc.\n        250 Apollo Drive\n        Chelmsford, MA 01824\nTel:    +1-978-244-3051\nEmail:  tnadeau@cisco.com\n\n        Subrahmanya Hegde\nPostal: Cisco Systems, Inc.\n        225 East Tazman Drive\nTel:    +1-408-525-6562\nEmail:  subrah@cisco.com\nGeneral comments should be sent to mpls@uu.net")
if mibBuilder.loadTexts: mplsLcAtmStdMIB.setDescription("This MIB module contains managed object definitions for\nMPLS Label-Controlled ATM interfaces as defined in\n[RFC3035].\n\nCopyright (C) The Internet Society (2006).  This\nversion of this MIB module is part of RFC 4368; see\nthe RFC itself for full legal notices.")
mplsLcAtmStdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 0))
mplsLcAtmStdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 1))
mplsLcAtmStdInterfaceConfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1))
if mibBuilder.loadTexts: mplsLcAtmStdInterfaceConfTable.setDescription("This table specifies per-interface MPLS LC-ATM\ncapability and associated information.  In particular,\nthis table sparsely extends the MPLS-LSR-STD-MIB's\nmplsInterfaceConfTable.")
mplsLcAtmStdInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1)).setIndexNames((0, "MPLS-LSR-STD-MIB", "mplsInterfaceIndex"))
if mibBuilder.loadTexts: mplsLcAtmStdInterfaceConfEntry.setDescription("An entry in this table is created by an LSR for\nevery interface capable of supporting MPLS LC-ATM.\nEach entry in this table will exist only if a\ncorresponding entry in ifTable and mplsInterfaceConfTable\nexists.  If the associated entries in ifTable and\nmplsInterfaceConfTable are deleted, the corresponding\nentry in this table must also be deleted shortly\nthereafter.")
mplsLcAtmStdCtrlVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 1), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdCtrlVpi.setDescription("This is the VPI value over which this\nLSR is willing to accept control traffic on\nthis interface.")
mplsLcAtmStdCtrlVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 2), MplsAtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdCtrlVci.setDescription("This is the VCI value over which this\nLSR is willing to accept control traffic\non this interface.")
mplsLcAtmStdUnlabTrafVpi = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 3), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdUnlabTrafVpi.setDescription("This is the VPI value over which this\nLSR is willing to accept unlabeled traffic\non this interface.")
mplsLcAtmStdUnlabTrafVci = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 4), MplsAtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdUnlabTrafVci.setDescription("This is the VCI value over which this\nLSR is willing to accept unlabeled traffic\non this interface.")
mplsLcAtmStdVcMerge = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdVcMerge.setDescription("If set to true(1), indicates that this interface\nis capable of ATM VC merge; otherwise, it MUST\nbe set to false(2).")
mplsLcAtmVcDirectlyConnected = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmVcDirectlyConnected.setDescription("This value indicates whether an LC-ATM is directly\nor indirectly (by means of a VP) connected.  If set to\ntrue(1), indicates that this interface is directly\nconnected LC-ATM; otherwise, it MUST be set to\nfalse(2).  Note that although it can be intimated\nfrom RFC 3057 that multiple VPs may be used,\nin practice only a single one is used, and therefore\nthe authors of this MIB module have chosen to model\nit as such.")
mplsLcAtmLcAtmVPI = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 7), AtmVpIdentifier().clone('0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmLcAtmVPI.setDescription("This is the VPI value used for indirectly\nconnected LC-ATM interfaces.  For these\ninterfaces, the VPI field is not\navailable to MPLS, and the label MUST be\nencoded entirely within the VCI field\n(see [RFC3035]).  If the interface is directly\nconnected, this value MUST be set to zero.")
mplsLcAtmStdIfConfRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdIfConfRowStatus.setDescription("This object is used to create and\ndelete entries in this table.  When configuring\nentries in this table, the corresponding\nifEntry and mplsInterfaceConfEntry\nMUST exist beforehand.  If a manager attempts to\ncreate an entry for a corresponding\nmplsInterfaceConfEntry that does not support LC-ATM,\nthe agent MUST return an inconsistentValue error.\nIf this table is implemented read-only, then the\nagent must set this object to active(1) when this\nrow is made active.  If this table is implemented\nwritable, then an agent MUST not allow modification\nto its objects once this value is set to active(1),\nexcept to mplsLcAtmStdIfConfRowStatus and\nmplsLcAtmStdIfConfStorageType.")
mplsLcAtmStdIfConfStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 9, 1, 1, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsLcAtmStdIfConfStorageType.setDescription("The storage type for this conceptual row.\nConceptual rows having the value 'permanent(4)'\nneed not allow write-access to any columnar\nobjects in the row.")
mplsLcAtmStdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 2))
mplsLcAtmStdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 1))
mplsLcAtmStdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 2))

# Augmentions

# Groups

mplsLcAtmStdIfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 2, 1)).setObjects(*(("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdVcMerge"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdUnlabTrafVci"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfConfStorageType"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfConfRowStatus"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdCtrlVpi"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdUnlabTrafVpi"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmLcAtmVPI"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdCtrlVci"), ("MPLS-LC-ATM-STD-MIB", "mplsLcAtmVcDirectlyConnected"), ) )
if mibBuilder.loadTexts: mplsLcAtmStdIfGroup.setDescription("Collection of objects needed for MPLS LC-ATM\n\n\n\ninterface configuration.")

# Compliances

mplsLcAtmStdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 1, 1)).setObjects(*(("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfGroup"), ) )
if mibBuilder.loadTexts: mplsLcAtmStdModuleFullCompliance.setDescription("Compliance statement for agents that provide\nfull support for MPLS-LC-ATM-STD-MIB.  Such\ndevices can be monitored and also be configured\nusing this MIB module.")
mplsLcAtmStdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 9, 2, 1, 2)).setObjects(*(("MPLS-LC-ATM-STD-MIB", "mplsLcAtmStdIfGroup"), ) )
if mibBuilder.loadTexts: mplsLcAtmStdModuleReadOnlyCompliance.setDescription("Compliance requirement for implementations that only\nprovide read-only support for MPLS-LC-ATM-STD-MIB.\nSuch devices can be monitored but cannot be configured\nusing this MIB module.")

# Exports

# Module identity
mibBuilder.exportSymbols("MPLS-LC-ATM-STD-MIB", PYSNMP_MODULE_ID=mplsLcAtmStdMIB)

# Objects
mibBuilder.exportSymbols("MPLS-LC-ATM-STD-MIB", mplsLcAtmStdMIB=mplsLcAtmStdMIB, mplsLcAtmStdNotifications=mplsLcAtmStdNotifications, mplsLcAtmStdObjects=mplsLcAtmStdObjects, mplsLcAtmStdInterfaceConfTable=mplsLcAtmStdInterfaceConfTable, mplsLcAtmStdInterfaceConfEntry=mplsLcAtmStdInterfaceConfEntry, mplsLcAtmStdCtrlVpi=mplsLcAtmStdCtrlVpi, mplsLcAtmStdCtrlVci=mplsLcAtmStdCtrlVci, mplsLcAtmStdUnlabTrafVpi=mplsLcAtmStdUnlabTrafVpi, mplsLcAtmStdUnlabTrafVci=mplsLcAtmStdUnlabTrafVci, mplsLcAtmStdVcMerge=mplsLcAtmStdVcMerge, mplsLcAtmVcDirectlyConnected=mplsLcAtmVcDirectlyConnected, mplsLcAtmLcAtmVPI=mplsLcAtmLcAtmVPI, mplsLcAtmStdIfConfRowStatus=mplsLcAtmStdIfConfRowStatus, mplsLcAtmStdIfConfStorageType=mplsLcAtmStdIfConfStorageType, mplsLcAtmStdConformance=mplsLcAtmStdConformance, mplsLcAtmStdCompliances=mplsLcAtmStdCompliances, mplsLcAtmStdGroups=mplsLcAtmStdGroups)

# Groups
mibBuilder.exportSymbols("MPLS-LC-ATM-STD-MIB", mplsLcAtmStdIfGroup=mplsLcAtmStdIfGroup)

# Compliances
mibBuilder.exportSymbols("MPLS-LC-ATM-STD-MIB", mplsLcAtmStdModuleFullCompliance=mplsLcAtmStdModuleFullCompliance, mplsLcAtmStdModuleReadOnlyCompliance=mplsLcAtmStdModuleReadOnlyCompliance)
