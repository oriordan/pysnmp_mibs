# PySNMP SMI module. Autogenerated from smidump -f python T11-FC-FSPF-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:15 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( FcDomainIdOrZero, fcmInstanceIndex, fcmSwitchIndex, ) = mibBuilder.importSymbols("FC-MGMT-MIB", "FcDomainIdOrZero", "fcmInstanceIndex", "fcmSwitchIndex")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Gauge32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "TimeTicks", "Unsigned32", "mib-2")
( RowStatus, StorageType, TextualConvention, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention", "TruthValue")
( t11FamConfigDomainId, ) = mibBuilder.importSymbols("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamConfigDomainId")
( T11FabricIndex, ) = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")

# Types

class T11FspfInterfaceState(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,2,3,6,5,4,)
    namedValues = NamedValues(("down", 1), ("init", 2), ("dbExchange", 3), ("dbAckwait", 4), ("dbWait", 5), ("full", 6), )
    
class T11FspfLinkType(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,255)
    
class T11FspfLsrType(Integer32):
    subtypeSpec = Integer32.subtypeSpec+ValueRangeConstraint(0,255)
    
class T11FspfLastCreationTime(TimeTicks):
    pass


# Objects

t11FcFspfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 143)).setRevisions(("2006-08-14 00:00",))
if mibBuilder.loadTexts: t11FcFspfMIB.setOrganization("T11")
if mibBuilder.loadTexts: t11FcFspfMIB.setContactInfo("Claudio DeSanti\nCisco Systems, Inc.\n170 West Tasman Drive\nSan Jose, CA 95134 USA\nEMail: cds@cisco.com\n\n\n\n\nKeith McCloghrie\nCisco Systems, Inc.\n170 West Tasman Drive\nSan Jose, CA USA 95134\nEmail: kzm@cisco.com")
if mibBuilder.loadTexts: t11FcFspfMIB.setDescription("The MIB module for managing the Fabric Shortest Path\nFirst (FSPF) protocol.  FSPF is specified in FC-SW-4.\n\nCopyright (C) The Internet Society (2006).  This version of\nthis MIB module is part of RFC 4626;  see the RFC itself for\nfull legal notices.")
t11FspfNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 143, 0))
t11FspfObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 143, 1))
t11FspfConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 143, 1, 1))
t11FspfTable = MibTable((1, 3, 6, 1, 2, 1, 143, 1, 1, 1))
if mibBuilder.loadTexts: t11FspfTable.setDescription("This table allows the users to configure and monitor FSPF's\nper-Fabric parameters and statistics on all Fabrics known to\nlocally managed switches.\n\nEntries are created/removed by the agent if and when\n(Virtual) Fabrics are created/deleted.")
t11FspfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1)).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FSPF-MIB", "t11FspfFabricIndex"))
if mibBuilder.loadTexts: t11FspfEntry.setDescription("An entry containing FSPF variables, parameters, and\nstatistics on a particular switch (identified by values\nof fcmInstanceIndex and fcmSwitchIndex) for a particular\nFabric (identified by a t11FspfFabricIndex value).\n\n(Note that the local switch's per-fabric Domain-ID is\navailable in t11FamConfigDomainId, which is defined in\nT11-FC-FABRIC-ADDR-MGR-MIB.)")
t11FspfFabricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 1), T11FabricIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: t11FspfFabricIndex.setDescription("A unique index value that uniquely identifies a\nparticular Fabric.\n\nIn a Fabric conformant to FC-SW-4, multiple Virtual Fabrics\ncan operate within one (or more) physical infrastructures.\nIn such a case, index value is used to uniquely identify a\nparticular Fabric within a physical infrastructure.\n\nIn a Fabric that has (can have) only a single Fabric\noperating within the physical infrastructure, the\nvalue of this Fabric Index will always be 1.")
t11FspfMinLsArrival = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FspfMinLsArrival.setDescription("The minimum time after accepting a Link State Record\n(LSR) on this Fabric before accepting another update of\nthe same LSR on the same Fabric.\n\nAn LSR update that is not accepted because of this time\ninterval is discarded.")
t11FspfMinLsInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(5000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FspfMinLsInterval.setDescription("The minimum time after this switch sends an LSR on this\nFabric before it will send another update of the same LSR\non the same Fabric.")
t11FspfLsRefreshTime = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 4), Unsigned32().clone(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLsRefreshTime.setDescription("The interval between transmission of refresh LSRs on this\nFabric.")
t11FspfMaxAge = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 5), Unsigned32().clone(60)).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfMaxAge.setDescription("The maximum age an LSR will be retained in the FSPF\ndatabase on this Fabric.  An LSR is removed from the\ndatabase after MaxAge is reached.")
t11FspfMaxAgeDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfMaxAgeDiscards.setDescription("The number of LSRs discarded due to their age reaching\nt11FspfMaxAge in this Fabric.  The last discontinuity of\nthis counter is indicated by t11FspfCreateTime.")
t11FspfPathComputations = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfPathComputations.setDescription("The number of times that the path computation algorithm\nhas been invoked by this Switch on this Fabric to compute\na set of minimum cost paths for this Fabric.  The last\n\n\n\ndiscontinuity of this counter is indicated by\nt11FspfCreateTime.")
t11FspfChecksumErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfChecksumErrors.setDescription("The number of FSPF checksum errors that were detected\nlocally (and therefore discarded) on this Fabric.\nThe last discontinuity of this counter is indicated by\nt11FspfCreateTime.")
t11FspfLsrs = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLsrs.setDescription("The current number of entries for this Fabric in the\nt11FspfLsrTable.")
t11FspfCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 10), T11FspfLastCreationTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfCreateTime.setDescription("The value of sysUpTime when this entry was last created.")
t11FspfAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 11), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FspfAdminStatus.setDescription("The desired state of FSPF in this Fabric.  If value of\nthis object is set to 'up', then FSPF is enabled in\nthis Fabric.  If set to 'down', then FSPF is disabled\nin this Fabric -- when FSPF is disabled, FSPF provides\n\n\n\nno routes to be included in the T11-FC-ROUTE-MIB module.\n(see the T11-FC-ROUTE-MIB).")
t11FspfOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 12), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfOperStatus.setDescription("State of FSPF in this Fabric.  If 't11FspfAdminStatus' is\n'down', then the 't11FspfOperStatus' should be 'down'.\nIf 't11FspfAdminStatus' is changed to 'up', then\n't11FspfOperStatus' should change to 'up' as and when\nFSPF is active in this Fabric.")
t11FspfNbrStateChangNotifyEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FspfNbrStateChangNotifyEnable.setDescription("Specifies whether or not the local agent should\nissue the notification 't11FspfNbrStateChangNotify'\nwhen the local switch learns of a change of state\nin the FSPF Neighbor Finite State Machine on an\ninterface in this Fabric.\nIf the value of the object is 'true, then the\nnotification is generated.  If the value is 'false',\nnotification is not generated.")
t11FspfSetToDefault = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 14), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("default", 1), ("noOp", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FspfSetToDefault.setDescription("Setting this value to 'default' changes the value of each\nand every writable object in this row to its default\n\n\n\nvalue.\n\nNo action is taken if this object is set to 'noOp'.\nThe value of the object, when read, is always 'noOp'.")
t11FspfStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 1, 1, 15), StorageType().clone('nonVolatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11FspfStorageType.setDescription("The storage type for read-write objects in this\nconceptual row.\n\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
t11FspfIfTable = MibTable((1, 3, 6, 1, 2, 1, 143, 1, 1, 2))
if mibBuilder.loadTexts: t11FspfIfTable.setDescription("This table allows the users to configure and monitor\nthe FSPF parameters that are per-interface (identified\nby a t11FspfIfIndex value), per-Fabric (identified by a\nt11FspfFabricIndex value), and per-switch (identified by\nvalues of fcmInstanceIndex and fcmSwitchIndex).\n\nCreating a row in this table via t11FspfIfRowStatus\nprovides the means to specify non-default parameter value(s)\nfor an interface at a time when the relevant row in this\ntable would not otherwise exist because the interface is\neither down or it is not an E_Port, but the corresponding\nrow in the t11FspfTable must already exist.\n\nAfter the non-default values have been specified for a\nport's parameters, they need to be retained in this table,\neven when the port becomes 'isolated'.  However, having\nunnecessary rows in this table clutters it up and makes\nthose rows that are useful harder for an NMS to find.\nTherefore, when an E_Port becomes isolated, its row gets\ndeleted if and only if all of its parameter values are the\ndefault values; also, when an E_Port becomes non-isolated\n\n\n\nin a particular Fabric, a row in this table needs to exist\nand is automatically created, if necessary.\n\nThe specific conditions for an automated/implicit deletion\nof a row are:\na) if the corresponding interface is no longer an E_Port\n   (e.g., a G_Port which is dynamically determined to be an\n   F_Port), and all configurable parameters have default\n   values; or\nb) if the interface identified by t11FspfIfIndex no longer\n   exists (e.g., because a line-card is physically removed);\n   or\nc) if the corresponding row in the t11FspfTable is deleted.")
t11FspfIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1)).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FSPF-MIB", "t11FspfFabricIndex"), (0, "T11-FC-FSPF-MIB", "t11FspfIfIndex"))
if mibBuilder.loadTexts: t11FspfIfEntry.setDescription("An entry containing FSPF information for the interface\nidentified by t11FspfIfIndex, on the fabric identified\nby t11FspfFabricIndex, on the switch identified by\nfcmSwitchIndex.")
t11FspfIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: t11FspfIfIndex.setDescription("The value of ifIndex that identifies the local\nFibre Channel interface for which this entry\ncontains FSPF information.")
t11FspfIfHelloInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(20)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FspfIfHelloInterval.setDescription("Interval between the periodic HELLO messages sent on this\ninterface in this Fabric to verify the link health.  Note\nthat this value must be same at both ends of a link in\nthis Fabric.")
t11FspfIfDeadInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 65535)).clone(80)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FspfIfDeadInterval.setDescription("Maximum time for which no HELLO messages can be received\non this interface in this Fabric.  After this time, the\ninterface is assumed to be broken and removed from the\ndatabase.  Note that this value must be greater than the\nHELLO interval specified on this interface in this Fabric.")
t11FspfIfRetransmitInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FspfIfRetransmitInterval.setDescription("The time after which an unacknowledged LSR is\nretransmitted on this interface in this Fabric.")
t11FspfIfInLsuPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfInLsuPkts.setDescription("Number of Link State Update (LSU) packets received on\nthis interface in this Fabric.  The last discontinuity\nof this counter is indicated by t11FspfIfCreateTime.")
t11FspfIfInLsaPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfInLsaPkts.setDescription("Number of Link State Acknowledgement (LSA) packets\nreceived on this interface in this Fabric.  The last\ndiscontinuity of this counter is indicated by\nt11FspfIfCreateTime.")
t11FspfIfOutLsuPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfOutLsuPkts.setDescription("Number of Link State Update (LSU) packets transmitted\non this interface in this Fabric.  The last\ndiscontinuity of this counter is indicated by\nt11FspfIfCreateTime.")
t11FspfIfOutLsaPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfOutLsaPkts.setDescription("Number of Link State Acknowledgement (LSA) packets\ntransmitted on this interface in this Fabric.  The\nlast discontinuity of this counter is indicated by\nt11FspfIfCreateTime.")
t11FspfIfOutHelloPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfOutHelloPkts.setDescription("Number of HELLO packets transmitted on this interface in\nthis Fabric.  The last discontinuity of this counter is\nindicated by t11FspfIfCreateTime.")
t11FspfIfInHelloPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfInHelloPkts.setDescription("Number of HELLO packets received on this interface in\nthis Fabric.  The last discontinuity of this counter is\nindicated by t11FspfIfCreateTime.")
t11FspfIfRetransmittedLsuPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfRetransmittedLsuPkts.setDescription("The number of LSU packets that contained one or more\nretransmitted LSRs, and that were transmitted on this\ninterface in this Fabric.  The last discontinuity of\nthis counter is indicated by t11FspfIfCreateTime.")
t11FspfIfInErrorPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfInErrorPkts.setDescription("Number of invalid FSPF control packets received on this\ninterface in this Fabric.  The last discontinuity of\nthis counter is indicated by t11FspfIfCreateTime.")
t11FspfIfNbrState = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 13), T11FspfInterfaceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfNbrState.setDescription("The state of FSPF's 'neighbor state machine', which is\nthe operational state of the interaction with the\n\n\n\nneighbor's interface that is connected to this interface.\n\nIf the 't11FspfIfAdminStatus' is 'down', then this object\nshould be 'down'.  If the 't11FspfIfAdminStatus' is 'up',\nthen this object's value depends on the state of FSPF's\n'neighbor state machine' on this interface in this\nFabric.")
t11FspfIfNbrDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 14), FcDomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfNbrDomainId.setDescription("The Domain Id of the neighbor in this Fabric.")
t11FspfIfNbrPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfNbrPortIndex.setDescription("The index, as known by the neighbor, of the neighbor's\ninterface that is connected to this interface in this\nFabric.")
t11FspfIfAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 16), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("up", 1), ("down", 2), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FspfIfAdminStatus.setDescription("The desired state of FSPF on this interface in this\nFabric, whenever 't11FspfAdminStatus' is 'up'.\nIf the value of this object is set to 'up', then FSPF is\nenabled on this interface in this Fabric.  If set to\n'down', then FSPF is disabled on this interface in this\nFabric.  Note that the operational state of FSPF on an\ninterface is given by t11FspfIfNbrState.")
t11FspfIfCreateTime = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 17), T11FspfLastCreationTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfIfCreateTime.setDescription("The value of sysUpTime when this entry was last\ncreated.")
t11FspfIfSetToDefault = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 18), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("default", 1), ("noOp", 2), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FspfIfSetToDefault.setDescription("Setting this value to 'default' changes the value of each\nand every writable object in this row to its default\nvalue.\n\nIf all the configuration parameters have their default\nvalues, and if the interface is down, then the row is\ndeleted automatically.\n\nNo action is taken if this object is set to 'noOp'.\nThe value of the object, when read, is always 'noOp'.")
t11FspfIfLinkCostFactor = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FspfIfLinkCostFactor.setDescription("The administrative factor used in calculating the cost\nof sending a frame on this interface in this Fabric.\n\nThe formula used to calculate the link cost is:\n\n         Link Cost = S * (1.0625e12 / ifSpeed)\nwhere:\n  S = (the value of this object / 100)\n  ifSpeed = interface speed (as defined in the IF-MIB).")
t11FspfIfStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 20), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FspfIfStorageType.setDescription("The storage type for this conceptual row.\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
t11FspfIfRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 1, 2, 1, 21), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11FspfIfRowStatus.setDescription("The status of the conceptual row.\n\nThis object can be used to create an entry only if there\nis an entry in the t11FspfTable for the corresponding\nFabric, and if the interface is either isolated or is a\nnon-E_port.\n\nSetting this object to 'destroy' will typically fail;\nto reverse the creation process, set the corresponding\ninstance of t11FspfIfSetToDefault to 'default'.")
t11FspfIfPrevNbrState = MibScalar((1, 3, 6, 1, 2, 1, 143, 1, 1, 3), T11FspfInterfaceState()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: t11FspfIfPrevNbrState.setDescription("The previous state of FSPF's Neighbor Finite State\nMachine on an interface.\n\nThis object is only used in the\n't11FspfNbrStateChangNotify' notification.")
t11FspfDatabase = MibIdentifier((1, 3, 6, 1, 2, 1, 143, 1, 2))
t11FspfLsrTable = MibTable((1, 3, 6, 1, 2, 1, 143, 1, 2, 1))
if mibBuilder.loadTexts: t11FspfLsrTable.setDescription("This table is the database of all the latest\nincarnations of the Link State Records (LSRs) that\nare currently contained in the topology database,\nfor all interfaces on all Fabrics known to\nlocally managed switches.\n\nA Fabric's topology database contains the LSRs that\nhave been either issued or received by a local switch on\nthat Fabric, and that have not reached t11FspfMaxAge.")
t11FspfLsrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1)).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FSPF-MIB", "t11FspfFabricIndex"), (0, "T11-FC-FSPF-MIB", "t11FspfLsrDomainId"), (0, "T11-FC-FSPF-MIB", "t11FspfLsrType"))
if mibBuilder.loadTexts: t11FspfLsrEntry.setDescription("This gives information for the most recent update of an\nLSR.  There is one entry for every LSR issued or received\nby a locally managed switch (identified by\nfcmInstanceIndex and fcmSwitchIndex) in a Fabric\n(identified by t11FspfFabricIndex).")
t11FspfLsrDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 1), FcDomainIdOrZero()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: t11FspfLsrDomainId.setDescription("Domain Id of the LSR owner in this Fabric.  It is the\nLink State Id of this LSR.")
t11FspfLsrType = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 2), T11FspfLsrType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: t11FspfLsrType.setDescription("Type of this LSR.")
t11FspfLsrAdvDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 3), FcDomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLsrAdvDomainId.setDescription("Domain Id of the switch that is advertising the LSR on\nthe behalf of the switch owning it.")
t11FspfLsrAge = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLsrAge.setDescription("The time since this LSR was inserted into the database.")
t11FspfLsrIncarnationNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLsrIncarnationNumber.setDescription("The link state incarnation number of this LSR.  This is\nused to identify most recent instance of an LSR while\nupdating the topology database when an LSR is received.\nThe updating of an LSR includes incrementing its\nincarnation number prior to transmission of the updated\nLSR.  So, the most recent LSR is the one with the\nlargest incarnation number.")
t11FspfLsrCheckSum = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLsrCheckSum.setDescription("The checksum of the LSR.")
t11FspfLsrLinks = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65355))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLsrLinks.setDescription("Number of entries in the t11FspfLinkTable associated with\nthis LSR.")
t11FspfLinkNumber = MibScalar((1, 3, 6, 1, 2, 1, 143, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLinkNumber.setDescription("The number of rows in the t11FspfLinkTable.")
t11FspfLinkTable = MibTable((1, 3, 6, 1, 2, 1, 143, 1, 2, 4))
if mibBuilder.loadTexts: t11FspfLinkTable.setDescription("This table contains the list of Inter-Switch Links and\ntheir information that is part of an LSR, either\nreceived or transmitted.")
t11FspfLinkEntry = MibTableRow((1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1)).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "FC-MGMT-MIB", "fcmSwitchIndex"), (0, "T11-FC-FSPF-MIB", "t11FspfFabricIndex"), (0, "T11-FC-FSPF-MIB", "t11FspfLsrDomainId"), (0, "T11-FC-FSPF-MIB", "t11FspfLsrType"), (0, "T11-FC-FSPF-MIB", "t11FspfLinkIndex"))
if mibBuilder.loadTexts: t11FspfLinkEntry.setDescription("An entry that contains information about a link\ncontained in an LSR in this Fabric.  An entry is created\nwhenever a new link appears in an (issued or received)\nLSR.  An entry is deleted when a link no longer appears\nin an (issued or received) LSR.")
t11FspfLinkIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: t11FspfLinkIndex.setDescription("An arbitrary index of this link.")
t11FspfLinkNbrDomainId = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 2), FcDomainIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLinkNbrDomainId.setDescription("The Domain Id of the neighbor on the other end of this\nlink in this Fabric.")
t11FspfLinkPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLinkPortIndex.setDescription("The source E_port of this link, as indicated by the index\nvalue in the LSR received from the switch identified by\n't11FspfLsrDomainId'.")
t11FspfLinkNbrPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLinkNbrPortIndex.setDescription("The destination E_port of this link, as indicated by the\nindex value in the LSR received from the switch identified\nby 't11FspfLinkNbrDomainId'.")
t11FspfLinkType = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 5), T11FspfLinkType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLinkType.setDescription("The type of this link.")
t11FspfLinkCost = MibTableColumn((1, 3, 6, 1, 2, 1, 143, 1, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11FspfLinkCost.setDescription("The cost of sending a frame on this link in this Fabric.\nLink cost is calculated using the formula:\n\n      link cost = S * (1.0625e12 / Signalling Rate)\n\nFor issued LSRs, S is determined by the value of\nt11FspfIfLinkCostFactor for the corresponding interface\n\n\n\nand Fabric.")
t11FspfConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 143, 2))
t11FspfMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 143, 2, 1))
t11FspfMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 143, 2, 2))

# Augmentions

# Notifications

t11FspfNbrStateChangNotify = NotificationType((1, 3, 6, 1, 2, 1, 143, 0, 1)).setObjects(*(("IF-MIB", "ifIndex"), ("T11-FC-FSPF-MIB", "t11FspfIfNbrDomainId"), ("T11-FC-FSPF-MIB", "t11FspfIfNbrState"), ("T11-FC-FSPF-MIB", "t11FspfIfPrevNbrState"), ("T11-FC-FABRIC-ADDR-MGR-MIB", "t11FamConfigDomainId"), ) )
if mibBuilder.loadTexts: t11FspfNbrStateChangNotify.setDescription("This notification signifies that there has been a change in\nthe state of an FSPF neighbor.  This is generated when the\nFSPF state changes to a terminal state, through either\nregression (i.e., goes from Full to Init or Down) or\nprogression (i.e., from any state to Full).  The value of\n't11FspfIfNbrState' is the state of the neighbor after the\nchange.")

# Groups

t11FspfGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 143, 2, 2, 1)).setObjects(*(("T11-FC-FSPF-MIB", "t11FspfAdminStatus"), ("T11-FC-FSPF-MIB", "t11FspfChecksumErrors"), ("T11-FC-FSPF-MIB", "t11FspfPathComputations"), ("T11-FC-FSPF-MIB", "t11FspfLsRefreshTime"), ("T11-FC-FSPF-MIB", "t11FspfOperStatus"), ("T11-FC-FSPF-MIB", "t11FspfCreateTime"), ("T11-FC-FSPF-MIB", "t11FspfLsrs"), ("T11-FC-FSPF-MIB", "t11FspfMaxAge"), ("T11-FC-FSPF-MIB", "t11FspfMinLsArrival"), ("T11-FC-FSPF-MIB", "t11FspfMaxAgeDiscards"), ("T11-FC-FSPF-MIB", "t11FspfSetToDefault"), ("T11-FC-FSPF-MIB", "t11FspfNbrStateChangNotifyEnable"), ("T11-FC-FSPF-MIB", "t11FspfStorageType"), ("T11-FC-FSPF-MIB", "t11FspfMinLsInterval"), ) )
if mibBuilder.loadTexts: t11FspfGeneralGroup.setDescription("A collection of objects for displaying and\nconfiguring FSPF parameters.")
t11FspfIfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 143, 2, 2, 2)).setObjects(*(("T11-FC-FSPF-MIB", "t11FspfIfRowStatus"), ("T11-FC-FSPF-MIB", "t11FspfIfRetransmitInterval"), ("T11-FC-FSPF-MIB", "t11FspfIfNbrState"), ("T11-FC-FSPF-MIB", "t11FspfIfDeadInterval"), ("T11-FC-FSPF-MIB", "t11FspfIfHelloInterval"), ("T11-FC-FSPF-MIB", "t11FspfIfNbrDomainId"), ("T11-FC-FSPF-MIB", "t11FspfIfPrevNbrState"), ("T11-FC-FSPF-MIB", "t11FspfIfNbrPortIndex"), ("T11-FC-FSPF-MIB", "t11FspfIfLinkCostFactor"), ("T11-FC-FSPF-MIB", "t11FspfIfSetToDefault"), ("T11-FC-FSPF-MIB", "t11FspfIfAdminStatus"), ("T11-FC-FSPF-MIB", "t11FspfIfCreateTime"), ("T11-FC-FSPF-MIB", "t11FspfIfStorageType"), ) )
if mibBuilder.loadTexts: t11FspfIfGroup.setDescription("A collection of objects for displaying the FSPF\ninterface information.")
t11FspfIfCounterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 143, 2, 2, 3)).setObjects(*(("T11-FC-FSPF-MIB", "t11FspfIfOutLsuPkts"), ("T11-FC-FSPF-MIB", "t11FspfIfInErrorPkts"), ("T11-FC-FSPF-MIB", "t11FspfIfOutLsaPkts"), ("T11-FC-FSPF-MIB", "t11FspfIfInLsaPkts"), ("T11-FC-FSPF-MIB", "t11FspfIfInHelloPkts"), ("T11-FC-FSPF-MIB", "t11FspfIfInLsuPkts"), ("T11-FC-FSPF-MIB", "t11FspfIfRetransmittedLsuPkts"), ("T11-FC-FSPF-MIB", "t11FspfIfOutHelloPkts"), ) )
if mibBuilder.loadTexts: t11FspfIfCounterGroup.setDescription("A collection of objects for counting particular\nFSPF-packet occurrences on an interface.")
t11FspfDatabaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 143, 2, 2, 4)).setObjects(*(("T11-FC-FSPF-MIB", "t11FspfLinkPortIndex"), ("T11-FC-FSPF-MIB", "t11FspfLinkNumber"), ("T11-FC-FSPF-MIB", "t11FspfLsrCheckSum"), ("T11-FC-FSPF-MIB", "t11FspfLinkNbrPortIndex"), ("T11-FC-FSPF-MIB", "t11FspfLsrAge"), ("T11-FC-FSPF-MIB", "t11FspfLinkNbrDomainId"), ("T11-FC-FSPF-MIB", "t11FspfLsrLinks"), ("T11-FC-FSPF-MIB", "t11FspfLinkCost"), ("T11-FC-FSPF-MIB", "t11FspfLsrIncarnationNumber"), ("T11-FC-FSPF-MIB", "t11FspfLinkType"), ("T11-FC-FSPF-MIB", "t11FspfLsrAdvDomainId"), ) )
if mibBuilder.loadTexts: t11FspfDatabaseGroup.setDescription("A collection of objects for displaying the FSPF\ntopology database information.")
t11FspfNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 143, 2, 2, 5)).setObjects(*(("T11-FC-FSPF-MIB", "t11FspfNbrStateChangNotify"), ) )
if mibBuilder.loadTexts: t11FspfNotificationGroup.setDescription("A collection of notifications for FSPF.")

# Compliances

t11FspfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 143, 2, 1, 1)).setObjects(*(("T11-FC-FSPF-MIB", "t11FspfIfCounterGroup"), ("T11-FC-FSPF-MIB", "t11FspfDatabaseGroup"), ("T11-FC-FSPF-MIB", "t11FspfGeneralGroup"), ("T11-FC-FSPF-MIB", "t11FspfNotificationGroup"), ("T11-FC-FSPF-MIB", "t11FspfIfGroup"), ) )
if mibBuilder.loadTexts: t11FspfMIBCompliance.setDescription("The compliance statement for entities that\nimplement the FSPF.")

# Exports

# Module identity
mibBuilder.exportSymbols("T11-FC-FSPF-MIB", PYSNMP_MODULE_ID=t11FcFspfMIB)

# Types
mibBuilder.exportSymbols("T11-FC-FSPF-MIB", T11FspfInterfaceState=T11FspfInterfaceState, T11FspfLinkType=T11FspfLinkType, T11FspfLsrType=T11FspfLsrType, T11FspfLastCreationTime=T11FspfLastCreationTime)

# Objects
mibBuilder.exportSymbols("T11-FC-FSPF-MIB", t11FcFspfMIB=t11FcFspfMIB, t11FspfNotifications=t11FspfNotifications, t11FspfObjects=t11FspfObjects, t11FspfConfiguration=t11FspfConfiguration, t11FspfTable=t11FspfTable, t11FspfEntry=t11FspfEntry, t11FspfFabricIndex=t11FspfFabricIndex, t11FspfMinLsArrival=t11FspfMinLsArrival, t11FspfMinLsInterval=t11FspfMinLsInterval, t11FspfLsRefreshTime=t11FspfLsRefreshTime, t11FspfMaxAge=t11FspfMaxAge, t11FspfMaxAgeDiscards=t11FspfMaxAgeDiscards, t11FspfPathComputations=t11FspfPathComputations, t11FspfChecksumErrors=t11FspfChecksumErrors, t11FspfLsrs=t11FspfLsrs, t11FspfCreateTime=t11FspfCreateTime, t11FspfAdminStatus=t11FspfAdminStatus, t11FspfOperStatus=t11FspfOperStatus, t11FspfNbrStateChangNotifyEnable=t11FspfNbrStateChangNotifyEnable, t11FspfSetToDefault=t11FspfSetToDefault, t11FspfStorageType=t11FspfStorageType, t11FspfIfTable=t11FspfIfTable, t11FspfIfEntry=t11FspfIfEntry, t11FspfIfIndex=t11FspfIfIndex, t11FspfIfHelloInterval=t11FspfIfHelloInterval, t11FspfIfDeadInterval=t11FspfIfDeadInterval, t11FspfIfRetransmitInterval=t11FspfIfRetransmitInterval, t11FspfIfInLsuPkts=t11FspfIfInLsuPkts, t11FspfIfInLsaPkts=t11FspfIfInLsaPkts, t11FspfIfOutLsuPkts=t11FspfIfOutLsuPkts, t11FspfIfOutLsaPkts=t11FspfIfOutLsaPkts, t11FspfIfOutHelloPkts=t11FspfIfOutHelloPkts, t11FspfIfInHelloPkts=t11FspfIfInHelloPkts, t11FspfIfRetransmittedLsuPkts=t11FspfIfRetransmittedLsuPkts, t11FspfIfInErrorPkts=t11FspfIfInErrorPkts, t11FspfIfNbrState=t11FspfIfNbrState, t11FspfIfNbrDomainId=t11FspfIfNbrDomainId, t11FspfIfNbrPortIndex=t11FspfIfNbrPortIndex, t11FspfIfAdminStatus=t11FspfIfAdminStatus, t11FspfIfCreateTime=t11FspfIfCreateTime, t11FspfIfSetToDefault=t11FspfIfSetToDefault, t11FspfIfLinkCostFactor=t11FspfIfLinkCostFactor, t11FspfIfStorageType=t11FspfIfStorageType, t11FspfIfRowStatus=t11FspfIfRowStatus, t11FspfIfPrevNbrState=t11FspfIfPrevNbrState, t11FspfDatabase=t11FspfDatabase, t11FspfLsrTable=t11FspfLsrTable, t11FspfLsrEntry=t11FspfLsrEntry, t11FspfLsrDomainId=t11FspfLsrDomainId, t11FspfLsrType=t11FspfLsrType, t11FspfLsrAdvDomainId=t11FspfLsrAdvDomainId, t11FspfLsrAge=t11FspfLsrAge, t11FspfLsrIncarnationNumber=t11FspfLsrIncarnationNumber, t11FspfLsrCheckSum=t11FspfLsrCheckSum, t11FspfLsrLinks=t11FspfLsrLinks, t11FspfLinkNumber=t11FspfLinkNumber, t11FspfLinkTable=t11FspfLinkTable, t11FspfLinkEntry=t11FspfLinkEntry, t11FspfLinkIndex=t11FspfLinkIndex, t11FspfLinkNbrDomainId=t11FspfLinkNbrDomainId, t11FspfLinkPortIndex=t11FspfLinkPortIndex, t11FspfLinkNbrPortIndex=t11FspfLinkNbrPortIndex, t11FspfLinkType=t11FspfLinkType, t11FspfLinkCost=t11FspfLinkCost, t11FspfConformance=t11FspfConformance, t11FspfMIBCompliances=t11FspfMIBCompliances, t11FspfMIBGroups=t11FspfMIBGroups)

# Notifications
mibBuilder.exportSymbols("T11-FC-FSPF-MIB", t11FspfNbrStateChangNotify=t11FspfNbrStateChangNotify)

# Groups
mibBuilder.exportSymbols("T11-FC-FSPF-MIB", t11FspfGeneralGroup=t11FspfGeneralGroup, t11FspfIfGroup=t11FspfIfGroup, t11FspfIfCounterGroup=t11FspfIfCounterGroup, t11FspfDatabaseGroup=t11FspfDatabaseGroup, t11FspfNotificationGroup=t11FspfNotificationGroup)

# Compliances
mibBuilder.exportSymbols("T11-FC-FSPF-MIB", t11FspfMIBCompliance=t11FspfMIBCompliance)
