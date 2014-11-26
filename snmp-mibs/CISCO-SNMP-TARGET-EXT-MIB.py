# PySNMP SMI module. Autogenerated from smidump -f python CISCO-SNMP-TARGET-EXT-MIB
# by libsmi2pysnmp-0.1.3 at Fri Aug  1 20:54:45 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ciscoMgmt, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
( InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
( InetAddress, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( snmpTargetAddrEntry, snmpTargetAddrName, ) = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry", "snmpTargetAddrName")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( RowStatus, StorageType, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TruthValue")

# Objects

ciscoSnmpTargetExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 412)).setRevisions(("2008-11-07 00:00","2007-08-20 00:00","2004-04-01 00:00",))
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIB.setOrganization("Cisco Systems, Inc.")
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIB.setContactInfo("Cisco Systems\nCustomer Service\n\nPostal: 170 W. Tasman Drive\nSan Jose, CA 95134\nUSA\n\nTel: +1 800 553-NETS\n\nE-mail: cs-snmp@cisco.com")
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIB.setDescription("This MIB is an extension of the SNMP-TARGET-MIB\nspecified in RFC3413.\n\nThis MIB module contains  Cisco-defined  extension\nto the snmpTargetAddrTable to represent information\nrequired for IPv6 Address. \n\nWhen Target has Link local or Multicast IPv6 address,\nthe information of the interface on which the\nnotification has to be sent is required. This\nadditional information is provided by this extension\nMIB.\n\nThis module also contains definition for set of new\nvariable to hold the address of the host that had\nsent an unauthentic SNMP message to agent.\n\nGlossary of the terms used in this MIB:\n--------------------------------------\n\nVRF - Virtual Routing and Forwarding. An IP technology  that \n      allows multiple instances of routing table to exist\n      in a system and work simultaneously. A VRF consists of \n      an IP routing table, a forwarding table, a set of \n      interfaces that use the forwarding table, and a set of \n      rules and routing protocol parameters that control \n      the information that is included into the routing \n      table.")
ciscoSnmpTargetExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 1))
cExtSnmpTargetAuthAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1))
cExtSnmpTargetAuthInetType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cExtSnmpTargetAuthInetType.setDescription("This contains the type of address\ncExtSnmpTargetAuthInetAddr holds when a host sends an\nunauthentic SNMP message.")
cExtSnmpTargetAuthInetAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cExtSnmpTargetAuthInetAddr.setDescription("This contains the address of the host from which\nsnmp-agent has received a SNMP message that is not\nauthentic.")
cExtSnmpTargetAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2))
if mibBuilder.loadTexts: cExtSnmpTargetAddrTable.setDescription("The cExtSnmpTargetAddrTable extends\nthe SNMP-TARGET-MIB's snmpTargetAddrTable for providing\ninfo on the type of interface for Link Local or Multicast\nIPv6 Target Address.")
cExtSnmpTargetAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2, 1))
if mibBuilder.loadTexts: cExtSnmpTargetAddrEntry.setDescription("A cExtSnmpTargetAddrTable entry extends\nsnmpTargetAddrTable to provide a new variable\nto hold the value of interface type.\n\nA target which has a link local or a multicast\naddress the variable of this table is valid.\nEntries are removed when the corresponding entry in the\nsnmpTargetAddrTable is removed.")
cExtSnmpTargetAddrIntIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 2, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cExtSnmpTargetAddrIntIfIndex.setDescription("Holds valid ifIndex value of the interface through\nwhich the notifications for the target with\nMulticast/Link local address specified in the\nsnmpTargetAddrTAddress, is sent.  \n\nIf snmpTargetAddrTAddress doesn't hold a Linklocal or\na Multicast target address then the value of this\nobject will be zero.\n\nFor the entries with snmpTargetAddrTAddress having\nLink Local or Multicast address the\nsnmpTargetAddrStatus cannot be set to valid unless the\nvalue for this object holds a valid ifIndex value.")
cExtSnmpTargetVrfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3))
if mibBuilder.loadTexts: cExtSnmpTargetVrfTable.setDescription("The cExtSnmpTargetVrfTable extends the snmpTargetAddrTable\nof the SNMP-TARGET-MIB for providing:\n\n   - VRF reachability criterion for the SNMP target\n   - VRF filtering criterion for the SNMP target\n\nThis table is indexed by the target entity \nsnmpTargetAddrName and the associated VRF name \ncExtSnmpTargetVrfName. Each entry of this table forms a \ntuple of target and VRF name for which all the VRF related\nconfiguration parameters can be specified by corresponding\ninstances of the columnar objects.\n\nThe reachability of the SNMP target is qualified by the \nrouting context by way of associating VRF Name(s) with it.\nRestricting only those SNMP notifications that are generated \nwithin the context of a VRF to a specific SNMP target is \nVRF based filtering of notifications.\n\nA row in this table cannot be created prior to the creation\nof row it extends.")
cExtSnmpTargetVrfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1)).setIndexNames((0, "SNMP-TARGET-MIB", "snmpTargetAddrName"), (0, "CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfName"))
if mibBuilder.loadTexts: cExtSnmpTargetVrfEntry.setDescription("An entry (conceptual row) in the cExtSnmpTargetVrfTable.\n\nWhen an entry in the snmpTargetAddrTable is deleted the \ncorresponding entries in this table are also deleted.\n\nA row needs to exist in the cExtSnmpTargetVrfTable for\neach VRF for which SNMP notifications are to be sent to\na particular target address, so that when the same \ntarget address is the destination for multiple VRFs, \nthen multiple rows in this table will reference the same \ntarget address. However, only one of such multiple rows\ncan be used for routing the SNMP notifications to that\ntarget address, i.e., only one of them can have an\ninstance of cExtSnmpTargetVrfRoute with the value 'true'.\nThus, any management operation which sets an instance of\ncExtSnmpTargetVrfRoute to 'true' must also have the\neffect of setting any other instance of  \ncExtSnmpTargetVrfRoute for the same target address to\n'false'.")
cExtSnmpTargetVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cExtSnmpTargetVrfName.setDescription("This object identifies a human readable string representing\nthe name of the VRF.")
cExtSnmpTargetVrfRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfRoute.setDescription("This object specifies whether this VRF (identified by the\ncorresponding instance identifier of cExtSnmpTargetVrfName)\nshould be used for routing the SNMP notifications \nsent to this target address specified in the value of \nthe corresponding instance of snmpTargetAddrTAddress.\n\nThe value 'true' indicates that this VRF should be used.\n\nThe value 'false' indicates that this VRF should not be\nused.")
cExtSnmpTargetVrfFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfFilter.setDescription("This object specifies whether SNMP notifications generated\nin this VRF (identified by the corresponding instance \nidentifier of cExtSnmpTargetVrfName) context should be sent\nto this target address specified in the value of the \ncorresponding instance of snmpTargetAddrTAddress.\n\nBy default, the notifications generated in any of the VRFs \nare allowed to be sent to the configured targets. Setting \nthe value of this object to 'true' defines 'inclusive' \nfiltering policy to allow notifications of a specific VRF \nwhile excluding notifications of all other VRFs.\n\nThe value 'true' indicates that the notifications of this\nVRF should be sent.\n\nThe value 'false' indicates that the notifications of this\nVRF should not be sent.")
cExtSnmpTargetVrfStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfStorage.setDescription("The storage type for this conceptual row.\n\nWhen the value of an instance of this object is 'permanent',\nthe value of the corresponding instance of all the other\nobjects of this table except cExtSnmpTargetVrfStatus are \nread-writable. The 'permanent' rows can not be deleted by\nsetting value of the corresponding instance of \ncExtSnmpTargetVrfStatus to 'destroy'.")
cExtSnmpTargetVrfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cExtSnmpTargetVrfStatus.setDescription("The status of this conceptual row.\n\nThere are no specific restrictions for setting the value\nof this object to 'active'. Once the value of this object\nis set to 'active', the value of the corresponding instance\nof all other objects of this table can still be modified.")
cExtSnmpNotifGblTrapSrcIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cExtSnmpNotifGblTrapSrcIfIndex.setDescription("This object specifies the ifIdex value of the source \ninterface to be used for sending TRAP notifications.\n\nThe value of this object should be a valid 'ifIndex' value.\n\nThis is a global configuration applied for all TRAP \nnotifications sent by this agent to all the targets. If the \nsource interface is configured for a specific target using \nthe value of corresponding instance of \n'cExtSnmpTargetAddrIntIfIndex', then that value takes \nprecedence and will be used for sending the notification.\n\nThe value of this object being 'zero' implies that there is \nno source interface configuration for the TRAP\nnotifications at a global level.")
cExtSnmpNotifGblInformSrcIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 412, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cExtSnmpNotifGblInformSrcIfIndex.setDescription("This object specifies the ifIdex value of the source \ninterface to be used for sending INFORM notifications.\n\nThe value of this object should be a valid 'ifIndex' value.\n\nThis is a global configuration applied for all INFORM\nnotifications sent by this agent to all the targets. If the \nsource interface is configured for a specific target using \nthe value of corresponding instance of \n'cExtSnmpTargetAddrIntIfIndex', then that value takes \nprecedence and will be used for sending the notification.\n\nThe value of this object being 'zero' implies that there is \nno source interface configuration for the INFORM\nnotifications at a global level.")
ciscoSnmpTargetExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 2))
ciscoSnmpTargetExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1))
ciscoSnmpTargetExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2))

# Augmentions
snmpTargetAddrEntry, = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
snmpTargetAddrEntry.registerAugmentions(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAddrEntry"))
cExtSnmpTargetAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Groups

ciscoSnmpTargetAuthFailureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 1)).setObjects(*(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAuthInetAddr"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAuthInetType"), ) )
if mibBuilder.loadTexts: ciscoSnmpTargetAuthFailureGroup.setDescription("The collection of objects which gives information about\nthe recent host that has sent a SNMP message to the agent \nthat is not authentic.")
ciscoSnmpTargetExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 2)).setObjects(*(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetAddrIntIfIndex"), ) )
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIBGroup.setDescription("The collection of objects which give information about\nthe interface through which the notifications are sent\nout for IPv6 Link-local and Multicast Target address.")
ciscoSnmpTargetExtVrfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 3)).setObjects(*(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfRoute"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfStorage"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfFilter"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpTargetVrfStatus"), ) )
if mibBuilder.loadTexts: ciscoSnmpTargetExtVrfMIBGroup.setDescription("The collection of objects for supporting VRF based\nconfiguration for the SNMP targets.")
ciscoSnmpTargetNotifSrcIntGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 2, 4)).setObjects(*(("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpNotifGblInformSrcIfIndex"), ("CISCO-SNMP-TARGET-EXT-MIB", "cExtSnmpNotifGblTrapSrcIfIndex"), ) )
if mibBuilder.loadTexts: ciscoSnmpTargetNotifSrcIntGroup.setDescription("The collection of objects which give information about\nthe interface through which SNMP TRAP and INFORM \nnotifications are sent for all target addresses globally.")

# Compliances

ciscoSnmpTargetExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 1)).setObjects(*(("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetAuthFailureGroup"), ) )
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIBCompliance.setDescription("Compliance for IPv6 address supported by\nsnmpTargetAddrTAddress for Link-Local or Multicast and\nfor holding the recent host address that sent an\nunauthentic SNMP message in cExtSnmpTargetAuthInetAddr\nand cExtSnmpTargetAuthInetType.")
ciscoSnmpTargetExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 2)).setObjects(*(("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetAuthFailureGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtVrfMIBGroup"), ) )
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIBComplianceRev1.setDescription("The compliance statement for entities which implement\nthe CISCO-SNMP-TARGET-EXT-MIB.")
ciscoSnmpTargetExtMIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 412, 2, 1, 3)).setObjects(*(("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtMIBGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetAuthFailureGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetNotifSrcIntGroup"), ("CISCO-SNMP-TARGET-EXT-MIB", "ciscoSnmpTargetExtVrfMIBGroup"), ) )
if mibBuilder.loadTexts: ciscoSnmpTargetExtMIBComplianceRev2.setDescription("The compliance statement for entities which implement\nthe CISCO-SNMP-TARGET-EXT-MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-EXT-MIB", PYSNMP_MODULE_ID=ciscoSnmpTargetExtMIB)

# Objects
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-EXT-MIB", ciscoSnmpTargetExtMIB=ciscoSnmpTargetExtMIB, ciscoSnmpTargetExtMIBObjects=ciscoSnmpTargetExtMIBObjects, cExtSnmpTargetAuthAddr=cExtSnmpTargetAuthAddr, cExtSnmpTargetAuthInetType=cExtSnmpTargetAuthInetType, cExtSnmpTargetAuthInetAddr=cExtSnmpTargetAuthInetAddr, cExtSnmpTargetAddrTable=cExtSnmpTargetAddrTable, cExtSnmpTargetAddrEntry=cExtSnmpTargetAddrEntry, cExtSnmpTargetAddrIntIfIndex=cExtSnmpTargetAddrIntIfIndex, cExtSnmpTargetVrfTable=cExtSnmpTargetVrfTable, cExtSnmpTargetVrfEntry=cExtSnmpTargetVrfEntry, cExtSnmpTargetVrfName=cExtSnmpTargetVrfName, cExtSnmpTargetVrfRoute=cExtSnmpTargetVrfRoute, cExtSnmpTargetVrfFilter=cExtSnmpTargetVrfFilter, cExtSnmpTargetVrfStorage=cExtSnmpTargetVrfStorage, cExtSnmpTargetVrfStatus=cExtSnmpTargetVrfStatus, cExtSnmpNotifGblTrapSrcIfIndex=cExtSnmpNotifGblTrapSrcIfIndex, cExtSnmpNotifGblInformSrcIfIndex=cExtSnmpNotifGblInformSrcIfIndex, ciscoSnmpTargetExtMIBConformance=ciscoSnmpTargetExtMIBConformance, ciscoSnmpTargetExtMIBCompliances=ciscoSnmpTargetExtMIBCompliances, ciscoSnmpTargetExtMIBGroups=ciscoSnmpTargetExtMIBGroups)

# Groups
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-EXT-MIB", ciscoSnmpTargetAuthFailureGroup=ciscoSnmpTargetAuthFailureGroup, ciscoSnmpTargetExtMIBGroup=ciscoSnmpTargetExtMIBGroup, ciscoSnmpTargetExtVrfMIBGroup=ciscoSnmpTargetExtVrfMIBGroup, ciscoSnmpTargetNotifSrcIntGroup=ciscoSnmpTargetNotifSrcIntGroup)

# Compliances
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-EXT-MIB", ciscoSnmpTargetExtMIBCompliance=ciscoSnmpTargetExtMIBCompliance, ciscoSnmpTargetExtMIBComplianceRev1=ciscoSnmpTargetExtMIBComplianceRev1, ciscoSnmpTargetExtMIBComplianceRev2=ciscoSnmpTargetExtMIBComplianceRev2)
