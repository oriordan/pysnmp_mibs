# PySNMP SMI module. Autogenerated from smidump -f python TOKENRING-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:16 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, transmission, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "transmission")
( MacAddress, TimeStamp, ) = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TimeStamp")

# Objects

dot5 = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 9)).setRevisions(("1994-10-23 11:50",))
if mibBuilder.loadTexts: dot5.setOrganization("IETF Interfaces MIB Working Group")
if mibBuilder.loadTexts: dot5.setContactInfo("        Keith McCloghrie\n\nPostal: cisco Systems, Inc.\n        170 West Tasman Drive,\n        San Jose, CA 95134-1706\n        US\n\n Phone: +1 408 526 5260\n EMail: kzm@cisco.com")
if mibBuilder.loadTexts: dot5.setDescription("The MIB module for IEEE Token Ring entities.")
dot5Table = MibTable((1, 3, 6, 1, 2, 1, 10, 9, 1))
if mibBuilder.loadTexts: dot5Table.setDescription("This table contains Token Ring interface\nparameters and state variables, one entry\nper 802.5 interface.")
dot5Entry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 9, 1, 1)).setIndexNames((0, "TOKENRING-MIB", "dot5IfIndex"))
if mibBuilder.loadTexts: dot5Entry.setDescription("A list of Token Ring status and parameter\nvalues for an 802.5 interface.")
dot5IfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5IfIndex.setDescription("The value of this object identifies the\n802.5 interface for which this entry\ncontains management information.  The\nvalue of this object for a particular\ninterface has the same value as the\nifIndex object, defined in MIB-II for\nthe same interface.")
dot5Commands = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,4,)).subtype(namedValues=NamedValues(("noop", 1), ("open", 2), ("reset", 3), ("close", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot5Commands.setDescription("When this object is set to the value of\nopen(2), the station should go into the\nopen state.  The progress and success of\nthe open is given by the values of the\nobjects dot5RingState and\ndot5RingOpenStatus.\n    When this object is set to the value\nof reset(3), then the station should do\na reset.  On a reset, all MIB counters\nshould retain their values, if possible.\nOther side affects are dependent on the\nhardware chip set.\n    When this object is set to the value\nof close(4), the station should go into\nthe stopped state by removing itself\nfrom the ring.\n    Setting this object to a value of\nnoop(1) has no effect.\n    When read, this object always has a\nvalue of noop(1).\n    The open(2) and close(4) values\ncorrespond to the up(1) and down(2) values\nof MIB-II's ifAdminStatus and ifOperStatus,\ni.e., the setting of ifAdminStatus and\ndot5Commands affects the values of both\ndot5Commands and ifOperStatus.")
dot5RingStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 262143))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5RingStatus.setDescription("The current interface status which can\nbe used to diagnose fluctuating problems\nthat can occur on token rings, after a\nstation has successfully been added to\nthe ring.\n   Before an open is completed, this\nobject has the value for the 'no status'\ncondition.  The dot5RingState and\ndot5RingOpenStatus objects provide for\ndebugging problems when the station\ncan not even enter the ring.\n    The object's value is a sum of\nvalues, one for each currently applicable\ncondition.  The following values are\ndefined for various conditions:\n\n        0 = No Problems detected\n       32 = Ring Recovery\n       64 = Single Station\n      256 = Remove Received\n      512 = reserved\n     1024 = Auto-Removal Error\n     2048 = Lobe Wire Fault\n     4096 = Transmit Beacon\n     8192 = Soft Error\n    16384 = Hard Error\n    32768 = Signal Loss\n   131072 = no status, open not completed.")
dot5RingState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(6,1,3,5,2,4,)).subtype(namedValues=NamedValues(("opened", 1), ("closed", 2), ("opening", 3), ("closing", 4), ("openFailure", 5), ("ringFailure", 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5RingState.setDescription("The current interface state with respect\nto entering or leaving the ring.")
dot5RingOpenStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(5,6,9,8,1,2,11,7,3,10,4,)).subtype(namedValues=NamedValues(("noOpen", 1), ("removeReceived", 10), ("open", 11), ("badParam", 2), ("lobeFailed", 3), ("signalLoss", 4), ("insertionTimeout", 5), ("ringFailed", 6), ("beaconing", 7), ("duplicateMAC", 8), ("requestFailed", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5RingOpenStatus.setDescription("This object indicates the success, or the\nreason for failure, of the station's most\nrecent attempt to enter the ring.")
dot5RingSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,4,)).subtype(namedValues=NamedValues(("unknown", 1), ("oneMegabit", 2), ("fourMegabit", 3), ("sixteenMegabit", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot5RingSpeed.setDescription("The ring-speed at the next insertion into\nthe ring.  Note that this may or may not be\ndifferent to the current ring-speed which is\ngiven by MIB-II's ifSpeed.  For interfaces\nwhich do not support changing ring-speed,\ndot5RingSpeed can only be set to its current\nvalue.  When dot5RingSpeed has the value\nunknown(1), the ring's actual ring-speed is\nto be used.")
dot5UpStream = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5UpStream.setDescription("The MAC-address of the up stream neighbor\nstation in the ring.")
dot5ActMonParticipate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("true", 1), ("false", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot5ActMonParticipate.setDescription("If this object has a value of true(1) then\nthis interface will participate in the\nactive monitor selection process.  If the\nvalue is false(2) then it will not.\nSetting this object does not take effect\nuntil the next Active Monitor election, and\nmight not take effect until the next time\nthe interface is opened.")
dot5Functional = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 9), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot5Functional.setDescription("The bit mask of all Token Ring functional\naddresses for which this interface will\naccept frames.")
dot5LastBeaconSent = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5LastBeaconSent.setDescription("The value of MIB-II's sysUpTime object at which\nthe local system last transmitted a Beacon frame\non this interface.")
dot5StatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 9, 2))
if mibBuilder.loadTexts: dot5StatsTable.setDescription("A table containing Token Ring statistics,\none entry per 802.5 interface.\n    All the statistics are defined using\nthe syntax Counter32 as 32-bit wrap around\ncounters.  Thus, if an interface's\nhardware maintains these statistics in\n16-bit counters, then the agent must read\nthe hardware's counters frequently enough\nto prevent loss of significance, in order\nto maintain 32-bit counters in software.")
dot5StatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 9, 2, 1)).setIndexNames((0, "TOKENRING-MIB", "dot5StatsIfIndex"))
if mibBuilder.loadTexts: dot5StatsEntry.setDescription("An entry contains the 802.5 statistics\nfor a particular interface.")
dot5StatsIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsIfIndex.setDescription("The value of this object identifies the\n802.5 interface for which this entry\ncontains management information.  The\nvalue of this object for a particular\ninterface has the same value as MIB-II's\nifIndex object for the same interface.")
dot5StatsLineErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsLineErrors.setDescription("This counter is incremented when a frame\nor token is copied or repeated by a\nstation, the E bit is zero in the frame\nor token and one of the following\nconditions exists: 1) there is a\nnon-data bit (J or K bit) between the SD\nand the ED of the frame or token, or\n2) there is an FCS error in the frame.")
dot5StatsBurstErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsBurstErrors.setDescription("This counter is incremented when a station\ndetects the absence of transitions for five\nhalf-bit timers (burst-five error).")
dot5StatsACErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsACErrors.setDescription("This counter is incremented when a station\nreceives an AMP or SMP frame in which A is\nequal to C is equal to 0, and then receives\nanother SMP frame with A is equal to C is\nequal to 0 without first receiving an AMP\nframe. It denotes a station that cannot set\nthe AC bits properly.")
dot5StatsAbortTransErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsAbortTransErrors.setDescription("This counter is incremented when a station\ntransmits an abort delimiter while\ntransmitting.")
dot5StatsInternalErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsInternalErrors.setDescription("This counter is incremented when a station\nrecognizes an internal error.")
dot5StatsLostFrameErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsLostFrameErrors.setDescription("This counter is incremented when a station\nis transmitting and its TRR timer expires.\nThis condition denotes a condition where a\ntransmitting station in strip mode does not\nreceive the trailer of the frame before the\nTRR timer goes off.")
dot5StatsReceiveCongestions = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsReceiveCongestions.setDescription("This counter is incremented when a station\nrecognizes a frame addressed to its\nspecific address, but has no available\nbuffer space indicating that the station\nis congested.")
dot5StatsFrameCopiedErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsFrameCopiedErrors.setDescription("This counter is incremented when a station\nrecognizes a frame addressed to its\nspecific address and detects that the FS\nfield A bits are set to 1 indicating a\npossible line hit or duplicate address.")
dot5StatsTokenErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsTokenErrors.setDescription("This counter is incremented when a station\nacting as the active monitor recognizes an\nerror condition that needs a token\ntransmitted.")
dot5StatsSoftErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsSoftErrors.setDescription("The number of Soft Errors the interface\nhas detected. It directly corresponds to\nthe number of Report Error MAC frames\nthat this interface has transmitted.\nSoft Errors are those which are\nrecoverable by the MAC layer protocols.")
dot5StatsHardErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsHardErrors.setDescription("The number of times this interface has\ndetected an immediately recoverable\nfatal error.  It denotes the number of\ntimes this interface is either\ntransmitting or receiving beacon MAC\nframes.")
dot5StatsSignalLoss = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsSignalLoss.setDescription("The number of times this interface has\ndetected the loss of signal condition from\nthe ring.")
dot5StatsTransmitBeacons = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsTransmitBeacons.setDescription("The number of times this interface has\ntransmitted a beacon frame.")
dot5StatsRecoverys = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsRecoverys.setDescription("The number of Claim Token MAC frames\nreceived or transmitted after the interface\nhas received a Ring Purge MAC frame.  This\ncounter signifies the number of times the\nring has been purged and is being recovered\nback into a normal operating state.")
dot5StatsLobeWires = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsLobeWires.setDescription("The number of times the interface has\ndetected an open or short circuit in the\nlobe data path.  The adapter will be closed\nand dot5RingState will signify this\ncondition.")
dot5StatsRemoves = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsRemoves.setDescription("The number of times the interface has\nreceived a Remove Ring Station MAC frame\nrequest.  When this frame is received\nthe interface will enter the close state\nand dot5RingState will signify this\ncondition.")
dot5StatsSingles = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsSingles.setDescription("The number of times the interface has\nsensed that it is the only station on the\nring.  This will happen if the interface\nis the first one up on a ring, or if\nthere is a hardware problem.")
dot5StatsFreqErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5StatsFreqErrors.setDescription("The number of times the interface has\ndetected that the frequency of the\nincoming signal differs from the expected\nfrequency by more than that specified by\nthe IEEE 802.5 standard.")
dot5Tests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 3))
dot5TestInsertFunc = ObjectIdentity((1, 3, 6, 1, 2, 1, 10, 9, 3, 1))
if mibBuilder.loadTexts: dot5TestInsertFunc.setDescription("Invoking this test causes the station to test the insert\nring logic of the hardware if the station's lobe media\ncable is connected to a wiring concentrator.  Note that\nthis command inserts the station into the network, and\nthus, could cause problems if the station is connected\nto a operational network.")
dot5TestFullDuplexLoopBack = ObjectIdentity((1, 3, 6, 1, 2, 1, 10, 9, 3, 2))
if mibBuilder.loadTexts: dot5TestFullDuplexLoopBack.setDescription("Invoking this test on a 802.5 interface causes the\ninterface to check the path from memory through the\nchip set's internal logic and back to memory, thus\nchecking the proper functioning of the system's\ninterface to the chip set.")
dot5ChipSets = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 4))
dot5ChipSetIBM16 = ObjectIdentity((1, 3, 6, 1, 2, 1, 10, 9, 4, 1))
if mibBuilder.loadTexts: dot5ChipSetIBM16.setDescription("IBM's 16/4 Mbs chip set.")
dot5ChipSetTItms380 = ObjectIdentity((1, 3, 6, 1, 2, 1, 10, 9, 4, 2))
if mibBuilder.loadTexts: dot5ChipSetTItms380.setDescription("Texas Instruments' TMS 380 4Mbs chip-set")
dot5ChipSetTItms380c16 = ObjectIdentity((1, 3, 6, 1, 2, 1, 10, 9, 4, 3))
if mibBuilder.loadTexts: dot5ChipSetTItms380c16.setDescription("Texas Instruments' TMS 380C16 16/4 Mbs chip-set")
dot5TimerTable = MibTable((1, 3, 6, 1, 2, 1, 10, 9, 5))
if mibBuilder.loadTexts: dot5TimerTable.setDescription("This table contains Token Ring interface\ntimer values, one entry per 802.5\ninterface.")
dot5TimerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 9, 5, 1)).setIndexNames((0, "TOKENRING-MIB", "dot5TimerIfIndex"))
if mibBuilder.loadTexts: dot5TimerEntry.setDescription("A list of Token Ring timer values for an\n802.5 interface.")
dot5TimerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerIfIndex.setDescription("The value of this object identifies the\n802.5 interface for which this entry\ncontains timer values.  The value of\nthis object for a particular interface\nhas the same value as MIB-II's ifIndex\nobject for the same interface.")
dot5TimerReturnRepeat = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerReturnRepeat.setDescription("The time-out value used to ensure the\ninterface will return to Repeat State, in\nunits of 100 micro-seconds.  The value\nshould be greater than the maximum ring\nlatency.")
dot5TimerHolding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerHolding.setDescription("Maximum period of time a station is\npermitted to transmit frames after capturing\na token, in units of 100 micro-seconds.")
dot5TimerQueuePDU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerQueuePDU.setDescription("The time-out value for enqueuing of an SMP\nPDU after reception of an AMP or SMP\nframe in which the A and C bits were\nequal to 0, in units of 100\nmicro-seconds.")
dot5TimerValidTransmit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerValidTransmit.setDescription("The time-out value used by the active\nmonitor to detect the absence of valid\ntransmissions, in units of 100\nmicro-seconds.")
dot5TimerNoToken = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerNoToken.setDescription("The time-out value used to recover from\nvarious-related error situations.\nIf N is the maximum number of stations on\nthe ring, the value of this timer is\nnormally:\ndot5TimerReturnRepeat + N*dot5TimerHolding.")
dot5TimerActiveMon = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerActiveMon.setDescription("The time-out value used by the active\nmonitor to stimulate the enqueuing of an\nAMP PDU for transmission, in units of\n100 micro-seconds.")
dot5TimerStandbyMon = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerStandbyMon.setDescription("The time-out value used by the stand-by\nmonitors to ensure that there is an active\nmonitor on the ring and to detect a\ncontinuous stream of tokens, in units of\n100 micro-seconds.")
dot5TimerErrorReport = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerErrorReport.setDescription("The time-out value which determines how\noften a station shall send a Report Error\nMAC frame to report its error counters,\nin units of 100 micro-seconds.")
dot5TimerBeaconTransmit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerBeaconTransmit.setDescription("The time-out value which determines how\nlong a station shall remain in the state\nof transmitting Beacon frames before\nentering the Bypass state, in units of\n100 micro-seconds.")
dot5TimerBeaconReceive = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot5TimerBeaconReceive.setDescription("The time-out value which determines how\nlong a station shall receive Beacon\nframes from its downstream neighbor\nbefore entering the Bypass state, in\nunits of 100 micro-seconds.")
dot5Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 6))
dot5Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 6, 1))
dot5Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 9, 6, 2))

# Augmentions

# Groups

dot5StateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 9, 6, 1, 1)).setObjects(*(("TOKENRING-MIB", "dot5RingOpenStatus"), ("TOKENRING-MIB", "dot5RingSpeed"), ("TOKENRING-MIB", "dot5Functional"), ("TOKENRING-MIB", "dot5RingState"), ("TOKENRING-MIB", "dot5ActMonParticipate"), ("TOKENRING-MIB", "dot5Commands"), ("TOKENRING-MIB", "dot5RingStatus"), ("TOKENRING-MIB", "dot5UpStream"), ("TOKENRING-MIB", "dot5LastBeaconSent"), ) )
if mibBuilder.loadTexts: dot5StateGroup.setDescription("A collection of objects providing state information\nand parameters for IEEE 802.5 interfaces.")
dot5StatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 9, 6, 1, 2)).setObjects(*(("TOKENRING-MIB", "dot5StatsRecoverys"), ("TOKENRING-MIB", "dot5StatsHardErrors"), ("TOKENRING-MIB", "dot5StatsACErrors"), ("TOKENRING-MIB", "dot5StatsRemoves"), ("TOKENRING-MIB", "dot5StatsFrameCopiedErrors"), ("TOKENRING-MIB", "dot5StatsSoftErrors"), ("TOKENRING-MIB", "dot5StatsBurstErrors"), ("TOKENRING-MIB", "dot5StatsTokenErrors"), ("TOKENRING-MIB", "dot5StatsLineErrors"), ("TOKENRING-MIB", "dot5StatsSignalLoss"), ("TOKENRING-MIB", "dot5StatsSingles"), ("TOKENRING-MIB", "dot5StatsLostFrameErrors"), ("TOKENRING-MIB", "dot5StatsTransmitBeacons"), ("TOKENRING-MIB", "dot5StatsFreqErrors"), ("TOKENRING-MIB", "dot5StatsLobeWires"), ("TOKENRING-MIB", "dot5StatsAbortTransErrors"), ("TOKENRING-MIB", "dot5StatsInternalErrors"), ("TOKENRING-MIB", "dot5StatsReceiveCongestions"), ) )
if mibBuilder.loadTexts: dot5StatsGroup.setDescription("A collection of objects providing statistics for\nIEEE 802.5 interfaces.")

# Compliances

dot5Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 9, 6, 2, 1)).setObjects(*(("TOKENRING-MIB", "dot5StateGroup"), ("TOKENRING-MIB", "dot5StatsGroup"), ) )
if mibBuilder.loadTexts: dot5Compliance.setDescription("The compliance statement for SNMPv2 entities\nwhich implement the IEEE 802.5 MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("TOKENRING-MIB", PYSNMP_MODULE_ID=dot5)

# Objects
mibBuilder.exportSymbols("TOKENRING-MIB", dot5=dot5, dot5Table=dot5Table, dot5Entry=dot5Entry, dot5IfIndex=dot5IfIndex, dot5Commands=dot5Commands, dot5RingStatus=dot5RingStatus, dot5RingState=dot5RingState, dot5RingOpenStatus=dot5RingOpenStatus, dot5RingSpeed=dot5RingSpeed, dot5UpStream=dot5UpStream, dot5ActMonParticipate=dot5ActMonParticipate, dot5Functional=dot5Functional, dot5LastBeaconSent=dot5LastBeaconSent, dot5StatsTable=dot5StatsTable, dot5StatsEntry=dot5StatsEntry, dot5StatsIfIndex=dot5StatsIfIndex, dot5StatsLineErrors=dot5StatsLineErrors, dot5StatsBurstErrors=dot5StatsBurstErrors, dot5StatsACErrors=dot5StatsACErrors, dot5StatsAbortTransErrors=dot5StatsAbortTransErrors, dot5StatsInternalErrors=dot5StatsInternalErrors, dot5StatsLostFrameErrors=dot5StatsLostFrameErrors, dot5StatsReceiveCongestions=dot5StatsReceiveCongestions, dot5StatsFrameCopiedErrors=dot5StatsFrameCopiedErrors, dot5StatsTokenErrors=dot5StatsTokenErrors, dot5StatsSoftErrors=dot5StatsSoftErrors, dot5StatsHardErrors=dot5StatsHardErrors, dot5StatsSignalLoss=dot5StatsSignalLoss, dot5StatsTransmitBeacons=dot5StatsTransmitBeacons, dot5StatsRecoverys=dot5StatsRecoverys, dot5StatsLobeWires=dot5StatsLobeWires, dot5StatsRemoves=dot5StatsRemoves, dot5StatsSingles=dot5StatsSingles, dot5StatsFreqErrors=dot5StatsFreqErrors, dot5Tests=dot5Tests, dot5TestInsertFunc=dot5TestInsertFunc, dot5TestFullDuplexLoopBack=dot5TestFullDuplexLoopBack, dot5ChipSets=dot5ChipSets, dot5ChipSetIBM16=dot5ChipSetIBM16, dot5ChipSetTItms380=dot5ChipSetTItms380, dot5ChipSetTItms380c16=dot5ChipSetTItms380c16, dot5TimerTable=dot5TimerTable, dot5TimerEntry=dot5TimerEntry, dot5TimerIfIndex=dot5TimerIfIndex, dot5TimerReturnRepeat=dot5TimerReturnRepeat, dot5TimerHolding=dot5TimerHolding, dot5TimerQueuePDU=dot5TimerQueuePDU, dot5TimerValidTransmit=dot5TimerValidTransmit, dot5TimerNoToken=dot5TimerNoToken, dot5TimerActiveMon=dot5TimerActiveMon, dot5TimerStandbyMon=dot5TimerStandbyMon, dot5TimerErrorReport=dot5TimerErrorReport, dot5TimerBeaconTransmit=dot5TimerBeaconTransmit, dot5TimerBeaconReceive=dot5TimerBeaconReceive, dot5Conformance=dot5Conformance, dot5Groups=dot5Groups, dot5Compliances=dot5Compliances)

# Groups
mibBuilder.exportSymbols("TOKENRING-MIB", dot5StateGroup=dot5StateGroup, dot5StatsGroup=dot5StatsGroup)

# Compliances
mibBuilder.exportSymbols("TOKENRING-MIB", dot5Compliance=dot5Compliance)
