# PySNMP SMI module. Autogenerated from smidump -f python IF-INVERTED-STACK-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:42 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ifStackGroup2, ifStackHigherLayer, ifStackLowerLayer, ) = mibBuilder.importSymbols("IF-MIB", "ifStackGroup2", "ifStackHigherLayer", "ifStackLowerLayer")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "mib-2")
( RowStatus, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus")

# Objects

ifInvertedStackMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 77)).setRevisions(("2000-06-14 00:00",))
if mibBuilder.loadTexts: ifInvertedStackMIB.setOrganization("IETF Interfaces MIB Working Group")
if mibBuilder.loadTexts: ifInvertedStackMIB.setContactInfo("   Keith McCloghrie\nCisco Systems, Inc.\n170 West Tasman Drive\nSan Jose, CA  95134-1706\nUS\n\n408-526-5260\nkzm@cisco.com")
if mibBuilder.loadTexts: ifInvertedStackMIB.setDescription("The MIB module which provides the Inverted Stack Table for\ninterface sub-layers.")
ifInvMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1))
ifInvStackTable = MibTable((1, 3, 6, 1, 2, 1, 77, 1, 1))
if mibBuilder.loadTexts: ifInvStackTable.setDescription("A table containing information on the relationships between\n\nthe multiple sub-layers of network interfaces.  In\nparticular, it contains information on which sub-layers run\n'underneath' which other sub-layers, where each sub-layer\ncorresponds to a conceptual row in the ifTable.  For\nexample, when the sub-layer with ifIndex value x runs\nunderneath the sub-layer with ifIndex value y, then this\ntable contains:\n\n  ifInvStackStatus.x.y=active\n\nFor each ifIndex value, z, which identifies an active\ninterface, there are always at least two instantiated rows\nin this table associated with z.  For one of these rows, z\nis the value of ifStackHigherLayer; for the other, z is the\nvalue of ifStackLowerLayer.  (If z is not involved in\nmultiplexing, then these are the only two rows associated\nwith z.)\n\nFor example, two rows exist even for an interface which has\nno others stacked on top or below it:\n\n  ifInvStackStatus.z.0=active\n  ifInvStackStatus.0.z=active\n\nThis table contains exactly the same number of rows as the\nifStackTable, but the rows appear in a different order.")
ifInvStackEntry = MibTableRow((1, 3, 6, 1, 2, 1, 77, 1, 1, 1)).setIndexNames((0, "IF-MIB", "ifStackLowerLayer"), (0, "IF-MIB", "ifStackHigherLayer"))
if mibBuilder.loadTexts: ifInvStackEntry.setDescription("Information on a particular relationship between two sub-\nlayers, specifying that one sub-layer runs underneath the\nother sub-layer.  Each sub-layer corresponds to a conceptual\nrow in the ifTable.")
ifInvStackStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 77, 1, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInvStackStatus.setDescription("The status of the relationship between two sub-layers.\n\nAn instance of this object exists for each instance of the\nifStackStatus object, and vice versa.  For example, if the\nvariable ifStackStatus.H.L exists, then the variable\nifInvStackStatus.L.H must also exist, and vice versa.  In\naddition, the two variables always have the same value.\n\nHowever, unlike ifStackStatus, the ifInvStackStatus object\nis NOT write-able.  A network management application wishing\nto change a relationship between sub-layers H and L cannot\ndo so by modifying the value of ifInvStackStatus.L.H, but\nmust instead modify the value of ifStackStatus.H.L.  After\nthe ifStackTable is modified, the change will be reflected\nin this table.")
ifInvConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2))
ifInvGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 1))
ifInvCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 77, 1, 2, 2))

# Augmentions

# Groups

ifInvStackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 77, 1, 2, 1, 1)).setObjects(*(("IF-INVERTED-STACK-MIB", "ifInvStackStatus"), ) )
if mibBuilder.loadTexts: ifInvStackGroup.setDescription("A collection of objects providing inverted information on\nthe layering of MIB-II interfaces.")

# Compliances

ifInvCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 77, 1, 2, 2, 1)).setObjects(*(("IF-INVERTED-STACK-MIB", "ifInvStackGroup"), ("IF-MIB", "ifStackGroup2"), ) )
if mibBuilder.loadTexts: ifInvCompliance.setDescription("The compliance statement for SNMP entities which provide\ninverted information on the layering of network interfaces.")

# Exports

# Module identity
mibBuilder.exportSymbols("IF-INVERTED-STACK-MIB", PYSNMP_MODULE_ID=ifInvertedStackMIB)

# Objects
mibBuilder.exportSymbols("IF-INVERTED-STACK-MIB", ifInvertedStackMIB=ifInvertedStackMIB, ifInvMIBObjects=ifInvMIBObjects, ifInvStackTable=ifInvStackTable, ifInvStackEntry=ifInvStackEntry, ifInvStackStatus=ifInvStackStatus, ifInvConformance=ifInvConformance, ifInvGroups=ifInvGroups, ifInvCompliances=ifInvCompliances)

# Groups
mibBuilder.exportSymbols("IF-INVERTED-STACK-MIB", ifInvStackGroup=ifInvStackGroup)

# Compliances
mibBuilder.exportSymbols("IF-INVERTED-STACK-MIB", ifInvCompliance=ifInvCompliance)
