# PySNMP SMI module. Autogenerated from smidump -f python CISCO-DIAL-CONTROL-MIB
# by libsmi2pysnmp-0.1.3 at Mon May 26 11:58:35 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ciscoExperiment, ) = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
( AbsoluteCounter32, ) = mibBuilder.importSymbols("DIAL-CONTROL-MIB", "AbsoluteCounter32")
( InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp")

# Objects

ciscoDialControlMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 25)).setRevisions(("2005-05-26 00:00","2003-07-10 00:01","2002-08-21 00:01","2002-05-24 00:01","2002-02-20 15:46","2001-12-13 15:46","1998-01-16 15:46",))
if mibBuilder.loadTexts: ciscoDialControlMib.setOrganization("Cisco systems, Inc.")
if mibBuilder.loadTexts: ciscoDialControlMib.setContactInfo("        Bibek Das\nPostal: cisco Systems\n        170 West Tasman Drive\n        San Jose, CA 95134\n        U.S.A.\nPhone:  +1 408 526 5225\nE-mail: cs-isdn@cisco.com")
if mibBuilder.loadTexts: ciscoDialControlMib.setDescription("The MIB module to describe call history information for\ndemand access and possibly other kinds of interfaces.")
ciscoDialControlMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 25, 1))
cCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4))
cCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3))
if mibBuilder.loadTexts: cCallHistoryTable.setDescription("A table containing information about specific\ncalls to a specific destination.")
cCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1)).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cCallHistoryEntry.setDescription("The information regarding a single Connection.")
cCallHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cCallHistoryIndex.setDescription("A monotonically increasing integer for the sole purpose of\nindexing call disconnection events.  When it reaches the \nmaximum value, an extremely unlikely event, the agent wraps \nthe value back to 1 and may flush existing entries.")
cCallHistorySetupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistorySetupTime.setDescription("The value of sysUpTime when the call setup was started.\nThis will be useful for an NMS to sort the call history\nentry with call setup time. Also, this object\ncan be useful in finding large delays between the time the\ncall was started and the time the call was connected.\nFor ISDN media, this will be the time when the setup\nmessage was received from or sent to the network.\nThe value of this object is the same as callActiveSetupTime\nin the callActiveTable")
cCallHistoryPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryPeerAddress.setDescription("The number this call was connected to. If the number is\nnot available, then it will have a length of zero.")
cCallHistoryPeerSubAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryPeerSubAddress.setDescription("The subaddress this call was connected to. If the subaddress\nis undefined or not available, this will be a zero length\nstring.")
cCallHistoryPeerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryPeerId.setDescription("This is the Id value of the peer table entry\nto which this call was made. If a peer table entry\nfor this call does not exist, the value of this object\nwill be zero.")
cCallHistoryPeerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryPeerIfIndex.setDescription("This is the ifIndex value of the peer table entry\nto which this call was made. If a peer table entry\nfor this call does not exist, the value of this object\nwill be zero.")
cCallHistoryLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryLogicalIfIndex.setDescription("This is the ifIndex value of the logical interface through\nwhich this call was made. For ISDN media, this would be\nthe ifIndex of the B channel which was used for this call.\nIf the ifIndex value is unknown, the value of this object \nwill be zero. For an IP call, the value will be zero.")
cCallHistoryDisconnectCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryDisconnectCause.setDescription("The encoded network cause value associated with this call.\n\nThe value of this object will depend on the interface type\nas well as on the protocol and protocol version being\nused on this interface. Some references for possible cause\nvalues are given below.")
cCallHistoryDisconnectText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryDisconnectText.setDescription("ASCII text describing the reason for call termination.\n\nThis object exists because it would be impossible for\na management station to store all possible cause values\nfor all types of interfaces. It should be used only if\na management station is unable to decode the value of\ndialCtlPeerStatsLastDisconnectCause.")
cCallHistoryConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryConnectTime.setDescription("The value of sysUpTime when the call was connected.")
cCallHistoryDisconnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryDisconnectTime.setDescription("The value of sysUpTime when the call was disconnected.")
cCallHistoryCallOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 12), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,1,)).subtype(namedValues=NamedValues(("originate", 1), ("answer", 2), ("callback", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryCallOrigin.setDescription("The call origin.")
cCallHistoryChargedUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 13), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryChargedUnits.setDescription("The number of charged units for this connection.\nFor incoming calls or if charging information is\nnot supplied by the switch, the value of this object\nwill be zero.")
cCallHistoryInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 14), Integer().subtype(subtypeSpec=SingleValueConstraint(10,7,8,3,4,5,6,1,2,9,)).subtype(namedValues=NamedValues(("other", 1), ("fax", 10), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryInfoType.setDescription("The information type for this call.")
cCallHistoryTransmitPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 15), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryTransmitPackets.setDescription("The number of packets which were transmitted while this\ncall was active.")
cCallHistoryTransmitBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 16), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryTransmitBytes.setDescription("The number of bytes which were transmitted while this\ncall was active.")
cCallHistoryReceivePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 17), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryReceivePackets.setDescription("The number of packets which were received while this\ncall was active.")
cCallHistoryReceiveBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 18), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryReceiveBytes.setDescription("The number of bytes which were received while this\ncall was active.")
cCallHistoryReleaseSource = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 19), Integer().subtype(subtypeSpec=SingleValueConstraint(1,10,7,9,6,2,8,3,5,4,)).subtype(namedValues=NamedValues(("callingPartyInPstn", 1), ("externalCallControlAgent", 10), ("callingPartyInVoip", 2), ("calledPartyInPstn", 3), ("calledPartyInVoip", 4), ("internalRelease", 5), ("internalCallControlApp", 6), ("consoleCommand", 7), ("externalRadiusServer", 8), ("externalNmsApp", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryReleaseSource.setDescription("Originator of the call release.")
cCallHistoryReleaseSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 3, 1, 20), Integer().subtype(subtypeSpec=SingleValueConstraint(13,1,14,12,9,5,11,6,7,2,10,8,3,4,)).subtype(namedValues=NamedValues(("callingPartyInPstn", 1), ("externalRadiusServer", 10), ("externalNmsApp", 11), ("externalCallControlAgent", 12), ("gatekeeper", 13), ("externalGKTMPServer", 14), ("callingPartyInVoip", 2), ("calledPartyInPstn", 3), ("calledPartyInVoip", 4), ("internalReleaseInPotsLeg", 5), ("internalReleaseInVoipLeg", 6), ("internalCallControlApp", 7), ("internalReleaseInVoipAAA", 8), ("consoleCommand", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryReleaseSrc.setDescription("Originator of the call release. Indicates the source of \nthe call release as follows : \n1) callingPartyInPstn : Calling party in PSTN.\n2) callingPartyInVoip : Calling party in VoIP.\n3) calledPartyInPstn : Called party in PSTN.\n4) calledPartyInVoip : Called party in VoIP.\n5) internalReleaseInPotsLeg : Due to an internal error \n   in Telephony call leg.\n6) internalReleaseInVoipLeg : Due to an internal error\n   in VoIP call leg.\n7) internalCallControlApp : Due to an internal error\n   in Session Application or Tcl or VXML script originated\n   release. \n8) internalReleaseInVoipAAA : Due to an internal error\n   in VoIP AAA module.\n9) consoleCommand : Due to CLI or MML.\n10) externalRadiusServer : Call failed during authorization\n    , authentication or due to receipt of POD from the \n    RADIUS server.\n11) externalNmsApp : Due to SNMP request to clear \n    the call.\n12) externalCallControlAgent : External Call Control Agent\n    initiated clear.\n13) gatekeeper : Gatekeeper initiated clear due to receipt\n    of Admission Reject, Disengage Request message.\n14) externalGKTMPServer : External GKTMP server initiated\n    clear due to receipt of Admission Reject message from\n    the gatekeeper, triggered by RESPONSE.ARJ message from\n    the GKTMP server.")
cCallHistoryIecTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 4))
if mibBuilder.loadTexts: cCallHistoryIecTable.setDescription("This table contains information about Internal Error\nCode(s) (IEC) which caused the call to fail.")
cCallHistoryIecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 4, 1)).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"), (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIecIndex"))
if mibBuilder.loadTexts: cCallHistoryIecEntry.setDescription("The IEC information regarding a single call.")
cCallHistoryIecIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: cCallHistoryIecIndex.setDescription("This object is used to index one or more IECs in the\ncontext of a single call.  In most cases there will\nonly be one IEC when a call fails.  However, it is\npossible for the software processing the call to \ngenerate multiple IECs before the call ultimately fails.\nIn that scenario, there will be multiple entries in\nthis table related to a single call (cCallHistoryIndex)\nand this object will serve to uniquely identify each IEC.")
cCallHistoryIec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 4, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cCallHistoryIec.setDescription("This object reflects the Internal Error Code.\nThe format is a string of dotted decimal numbers\ncomposed of the following components:\n\nVersion.Entity.Category.Subsystem.Errorcode.Diagnostic\n\nEach component is defined as follows:\nVersion     : The version of IEC software.\nEntity      : The network entity that originated\n              the error.\nCategory    : The category of the error (eg, software\n              error, hardware resource unavailable, ...)\nSubsystem   : The subsystem in which the error occurred.\nErrorcode   : A subsytem-specific error code.\nDiagnostic  : An implementation-specific diagnostic code.")
cPeerGlobalConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 5))
cPeerSearchType = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 25, 1, 5, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(3,1,2,)).subtype(namedValues=NamedValues(("none", 1), ("datavoice", 2), ("voicedata", 3), )).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cPeerSearchType.setDescription("Specifies the peer search preference based on the\ntype of peers in an universal/integrated port\nplatform.\n\nnone      - both voice and data peers are searched\n           in same preference.\ndatavoice - search data peers first. If no data peers\n           are found, the voice peers are searched.\nvoicedata - search voice peers first. If no voice peers\n           are found, the data peers are searched.")
ciscoDialControlMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 25, 3))
ciscoDialControlMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1))
ciscoDialControlMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2))

# Augmentions

# Groups

cCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 1)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerAddress"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryChargedUnits"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectCause"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryLogicalIfIndex"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectText"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerSubAddress"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitBytes"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerId"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryInfoType"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistorySetupTime"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceivePackets"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryConnectTime"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitPackets"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectTime"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerIfIndex"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceiveBytes"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryCallOrigin"), ) )
if mibBuilder.loadTexts: cCallHistoryGroup.setDescription("A collection of objects providing the Call History\ncapability.")
cCallHistoryGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 2)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerAddress"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryChargedUnits"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectCause"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryLogicalIfIndex"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectText"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerSubAddress"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReleaseSource"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitBytes"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerId"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryInfoType"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistorySetupTime"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceivePackets"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryConnectTime"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitPackets"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectTime"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerIfIndex"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceiveBytes"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryCallOrigin"), ) )
if mibBuilder.loadTexts: cCallHistoryGroupRev1.setDescription("A collection of objects providing the Call History\ncapability.")
cCallHistoryGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 3)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerAddress"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryChargedUnits"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectCause"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryLogicalIfIndex"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectText"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerSubAddress"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitBytes"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerId"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryInfoType"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistorySetupTime"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceivePackets"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryConnectTime"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryTransmitPackets"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryDisconnectTime"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryPeerIfIndex"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReleaseSrc"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryReceiveBytes"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryCallOrigin"), ) )
if mibBuilder.loadTexts: cCallHistoryGroupRev2.setDescription("A collection of objects providing the Call History\ncapability.")
cPeerGlobalConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 4)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cPeerSearchType"), ) )
if mibBuilder.loadTexts: cPeerGlobalConfigurationGroup.setDescription("A collection of objects providing the Peer global\nconfiguration.")
cCallHistoryIecGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 2, 5)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIec"), ) )
if mibBuilder.loadTexts: cCallHistoryIecGroup.setDescription("A collection of objects providing information about\nInternal Error Code.")

# Compliances

ciscoDialControlMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 1)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cCallHistoryGroup"), ) )
if mibBuilder.loadTexts: ciscoDialControlMibCompliance.setDescription("The compliance statement for entities which\nimplement the DIAL CONTROL MIB")
ciscoDialControlMibComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 2)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cCallHistoryGroupRev1"), ) )
if mibBuilder.loadTexts: ciscoDialControlMibComplianceRev1.setDescription("The compliance statement for entities which\nimplement the DIAL CONTROL MIB")
ciscoDialControlMibComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 3)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cCallHistoryGroupRev2"), ) )
if mibBuilder.loadTexts: ciscoDialControlMibComplianceRev2.setDescription("The compliance statement for entities which\nimplement the DIAL CONTROL MIB")
ciscoDialControlMibComplianceRev3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 4)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cCallHistoryGroupRev2"), ("CISCO-DIAL-CONTROL-MIB", "cPeerGlobalConfigurationGroup"), ) )
if mibBuilder.loadTexts: ciscoDialControlMibComplianceRev3.setDescription("The compliance statement for entities which\nimplement the DIAL CONTROL MIB")
ciscoDialControlMibComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 25, 3, 1, 5)).setObjects(*(("CISCO-DIAL-CONTROL-MIB", "cCallHistoryGroupRev2"), ("CISCO-DIAL-CONTROL-MIB", "cPeerGlobalConfigurationGroup"), ("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIecGroup"), ) )
if mibBuilder.loadTexts: ciscoDialControlMibComplianceRev4.setDescription("The compliance statement for entities which\nimplement the DIAL CONTROL MIB")

# Exports

# Module identity
mibBuilder.exportSymbols("CISCO-DIAL-CONTROL-MIB", PYSNMP_MODULE_ID=ciscoDialControlMib)

# Objects
mibBuilder.exportSymbols("CISCO-DIAL-CONTROL-MIB", ciscoDialControlMib=ciscoDialControlMib, ciscoDialControlMibObjects=ciscoDialControlMibObjects, cCallHistory=cCallHistory, cCallHistoryTable=cCallHistoryTable, cCallHistoryEntry=cCallHistoryEntry, cCallHistoryIndex=cCallHistoryIndex, cCallHistorySetupTime=cCallHistorySetupTime, cCallHistoryPeerAddress=cCallHistoryPeerAddress, cCallHistoryPeerSubAddress=cCallHistoryPeerSubAddress, cCallHistoryPeerId=cCallHistoryPeerId, cCallHistoryPeerIfIndex=cCallHistoryPeerIfIndex, cCallHistoryLogicalIfIndex=cCallHistoryLogicalIfIndex, cCallHistoryDisconnectCause=cCallHistoryDisconnectCause, cCallHistoryDisconnectText=cCallHistoryDisconnectText, cCallHistoryConnectTime=cCallHistoryConnectTime, cCallHistoryDisconnectTime=cCallHistoryDisconnectTime, cCallHistoryCallOrigin=cCallHistoryCallOrigin, cCallHistoryChargedUnits=cCallHistoryChargedUnits, cCallHistoryInfoType=cCallHistoryInfoType, cCallHistoryTransmitPackets=cCallHistoryTransmitPackets, cCallHistoryTransmitBytes=cCallHistoryTransmitBytes, cCallHistoryReceivePackets=cCallHistoryReceivePackets, cCallHistoryReceiveBytes=cCallHistoryReceiveBytes, cCallHistoryReleaseSource=cCallHistoryReleaseSource, cCallHistoryReleaseSrc=cCallHistoryReleaseSrc, cCallHistoryIecTable=cCallHistoryIecTable, cCallHistoryIecEntry=cCallHistoryIecEntry, cCallHistoryIecIndex=cCallHistoryIecIndex, cCallHistoryIec=cCallHistoryIec, cPeerGlobalConfiguration=cPeerGlobalConfiguration, cPeerSearchType=cPeerSearchType, ciscoDialControlMibConformance=ciscoDialControlMibConformance, ciscoDialControlMibCompliances=ciscoDialControlMibCompliances, ciscoDialControlMibGroups=ciscoDialControlMibGroups)

# Groups
mibBuilder.exportSymbols("CISCO-DIAL-CONTROL-MIB", cCallHistoryGroup=cCallHistoryGroup, cCallHistoryGroupRev1=cCallHistoryGroupRev1, cCallHistoryGroupRev2=cCallHistoryGroupRev2, cPeerGlobalConfigurationGroup=cPeerGlobalConfigurationGroup, cCallHistoryIecGroup=cCallHistoryIecGroup)

# Compliances
mibBuilder.exportSymbols("CISCO-DIAL-CONTROL-MIB", ciscoDialControlMibCompliance=ciscoDialControlMibCompliance, ciscoDialControlMibComplianceRev1=ciscoDialControlMibComplianceRev1, ciscoDialControlMibComplianceRev2=ciscoDialControlMibComplianceRev2, ciscoDialControlMibComplianceRev3=ciscoDialControlMibComplianceRev3, ciscoDialControlMibComplianceRev4=ciscoDialControlMibComplianceRev4)
