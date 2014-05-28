# PySNMP SMI module. Autogenerated from smidump -f python WLSX-VOICE-MIB
# by libsmi2pysnmp-0.1.3 at Tue May 27 09:00:44 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( wlanAPBSSID, wlanAPMacAddress, wlanAPRadioNumber, wlanStaPhyAddress, ) = mibBuilder.importSymbols("", "wlanAPBSSID", "wlanAPMacAddress", "wlanAPRadioNumber", "wlanStaPhyAddress")
( wlsxEnterpriseMibModules, ) = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
( ArubaCallStates, ArubaEnableValue, ArubaVlanValidRange, ArubaVoiceCacBit, ArubaVoiceCdrDirection, ArubaVoipProtocol, ArubaVoipRegState, ) = mibBuilder.importSymbols("ARUBA-TC", "ArubaCallStates", "ArubaEnableValue", "ArubaVlanValidRange", "ArubaVoiceCacBit", "ArubaVoiceCdrDirection", "ArubaVoipProtocol", "ArubaVoipRegState")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "snmpModules")
( DateAndTime, DisplayString, MacAddress, PhysAddress, RowStatus, StorageType, TAddress, TDomain, TextualConvention, TestAndIncr, TimeInterval, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "MacAddress", "PhysAddress", "RowStatus", "StorageType", "TAddress", "TDomain", "TextualConvention", "TestAndIncr", "TimeInterval", "TruthValue")

# Objects

wlsxVoiceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12)).setRevisions(("1908-04-16 02:06",))
if mibBuilder.loadTexts: wlsxVoiceMIB.setOrganization("Aruba Wireless Networks")
if mibBuilder.loadTexts: wlsxVoiceMIB.setContactInfo("Postal:    1322 Crossman Avenue\nSunnyvale, CA 94089	\nE-mail:     dl-support@arubanetworks.com\nPhone:      +1 408 227 4500")
if mibBuilder.loadTexts: wlsxVoiceMIB.setDescription("This MIB module defines MIB objects which provide\ninformation about Voice call status and call detail reporting\n	in the Aruba controller.")
wlsxVoiceStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1))
wlsxVoiceCdrInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1))
wlsxVoiceCdrTotal = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxVoiceCdrTotal.setDescription("\nTotal Number of CDR info in the controller.")
wlsxVoiceCdrTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2))
if mibBuilder.loadTexts: wlsxVoiceCdrTable.setDescription("\nThis table lists Call Detail Record Info. ")
wlsxVoiceCdrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1)).setIndexNames((0, "WLSX-VOICE-MIB", "voiceCdrId"))
if mibBuilder.loadTexts: wlsxVoiceCdrEntry.setDescription("")
voiceCdrId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: voiceCdrId.setDescription("\nVoice CDR id")
voiceCdrIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrIp.setDescription("\nVoice CDR IP")
voiceCdrMac = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrMac.setDescription("\nVoice CDR MAC")
voiceCdrName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrName.setDescription("\nVoice CDR Name")
voiceCdrDialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrDialNum.setDescription("\nVoice CDR dialed number")
voiceCdrDir = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 6), ArubaVoiceCdrDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrDir.setDescription("\nVoice CDR direction incoming or outgoing")
voiceCdrOrigTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrOrigTime.setDescription("\nVoice CDR orig time")
voiceCdrSetupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrSetupTime.setDescription("\nVoice CDR setup time")
voiceCdrTeardownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrTeardownTime.setDescription("\nVoice CDR teardown number")
voiceCdrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 10), ArubaCallStates()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrStatus.setDescription("\nVoice CDR Status")
voiceCdrReason = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrReason.setDescription("\nVoice CDR Reason")
voiceCdrDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrDuration.setDescription("\nVoice CDR Duration")
voiceCdrRValue = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrRValue.setDescription("\nVoice CDR R-Value")
voiceCdrApSwitchDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrApSwitchDelay.setDescription("\nVoice CDR AP switch delay")
voiceCdrCodec = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrCodec.setDescription("\nVoice CDR codec")
voiceCdrApName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrApName.setDescription("\nVoice CDR AP Name")
voiceCdrApMac = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 17), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrApMac.setDescription("\nVoice CDR AP MAC Address")
voiceCdrBssid = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrBssid.setDescription("\nVoice CDR BSSID")
voiceCdrEssid = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrEssid.setDescription("\nVoice CDR ESSID")
voiceCdrHandovers = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrHandovers.setDescription("\nVoice CDR client handovers AKA mobility rate")
voiceCdrMOS = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 1, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCdrMOS.setDescription("\nVoice CDR MOS")
wlsxVoiceCallCtrsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2))
voiceCallCtrsTotal = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsTotal.setDescription("\nTotal Number of calls.")
voiceCallCtrsSuccess = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsSuccess.setDescription("\nTotal Number of successful calls.")
voiceCallCtrsFailed = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsFailed.setDescription("\nTotal Number of failed calls.")
voiceCallCtrsRejected = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsRejected.setDescription("\nTotal Number of rejected calls.")
voiceCallCtrsAborted = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsAborted.setDescription("\nTotal Number of aborted calls.")
voiceCallCtrsOrig = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsOrig.setDescription("\nTotal Number of originated calls.")
voiceCallCtrsRecvd = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsRecvd.setDescription("\nTotal number of received calls.")
voiceCallCtrsActive = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsActive.setDescription("\nTotal number of active calls.")
voiceCallCtrsNotFnd = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsNotFnd.setDescription("\nTotal number of not found calls.")
voiceCallCtrsBusy = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsBusy.setDescription("\nTotal number of busy calls.")
voiceCallCtrsSvc = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsSvc.setDescription("\nTotal number of service unavailable calls.")
voiceCallCtrsReqTerm = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsReqTerm.setDescription("\nTotal number of request terminated calls.")
voiceCallCtrsDecline = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsDecline.setDescription("\nTotal number of declined calls.")
voiceCallCtrsUnauth = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsUnauth.setDescription("\nTotal number of unauthorized calls.")
voiceCallCtrsMisc = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 2, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceCallCtrsMisc.setDescription("\nTotal number of miscellaneous calls.")
wlsxVoiceClientInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3))
wlsxVoiceClientTotal = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxVoiceClientTotal.setDescription("\nTotal Number of Active client sessions in the controller.")
wlsxVoiceClientTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2))
if mibBuilder.loadTexts: wlsxVoiceClientTable.setDescription("\nThis table lists all voice client Info")
wlsxVoiceClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1)).setIndexNames((0, "", "wlanStaPhyAddress"))
if mibBuilder.loadTexts: wlsxVoiceClientEntry.setDescription("")
voiceClientIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceClientIp.setDescription("\nVoice client IP Address ")
voiceClientProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 2), ArubaVoipProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceClientProtocol.setDescription("\nVoice client protocol used")
voiceClientRegState = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 3), ArubaVoipRegState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceClientRegState.setDescription("\nVoice client state")
voiceClientContactName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceClientContactName.setDescription("\nVoice client contact name")
voiceClientServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceClientServerName.setDescription("\nVoice client Server name")
voiceClientEssid = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceClientEssid.setDescription("\nVoice client ESSID")
voiceClientVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 7), ArubaVlanValidRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceClientVlanId.setDescription("\nVoice client VLAN id ")
voiceClientTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceClientTunnelId.setDescription("\nVoice client tunnel ID")
wlsxVoiceAPBssidInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4))
wlsxVoiceAPBssidTotal = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxVoiceAPBssidTotal.setDescription("\nTotal Number of active voip info in the controller.")
wlsxVoiceAPBssidTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2))
if mibBuilder.loadTexts: wlsxVoiceAPBssidTable.setDescription("\nThis table lists Active Voip Info. ")
wlsxVoiceAPBssidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1)).setIndexNames((0, "", "wlanAPMacAddress"), (0, "", "wlanAPRadioNumber"), (0, "", "wlanAPBSSID"))
if mibBuilder.loadTexts: wlsxVoiceAPBssidEntry.setDescription("")
voiceAPBssidName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidName.setDescription("\nVoice AP Name")
voiceAPBssidGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidGroup.setDescription("\nVoice AP Group")
voiceAPBssidIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidIp.setDescription("\nVoice AP IP address")
voiceAPBssidTotCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidTotCalls.setDescription("\nVoice AP current calls")
voiceAPBssidVoiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidVoiceType.setDescription("\nVoice AP Type")
voiceAPBssidFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 6), Bits().subtype(namedValues=NamedValues(("apRemoteAP", 0), ("apPPPOE", 1), ("apWiredApEnabled", 2), ("apEnet1Mode", 3), ("apActiveLoadBalancing", 4), ("apDisconnectExtraCalls", 5), ("apBatteryBoost", 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidFlag.setDescription("\nVoice AP flag")
voiceAPBssidUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidUpTime.setDescription("\nVoice AP up time")
voiceAPBssid100Sent = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssid100Sent.setDescription("\nVoice 100 sent")
voiceAPBssid503Sent = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssid503Sent.setDescription("\nVoice 503 sent")
voiceAPBssidExtraCallDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidExtraCallDisc.setDescription("\nVoice AP extra call disconnect")
voiceAPBssidKickedOff = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidKickedOff.setDescription("\nVoice AP kicked off")
voiceAPBssidTspecDenied = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidTspecDenied.setDescription("\nVoice AP Tspec Denied")
voiceAPBssidCacFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 13), ArubaVoiceCacBit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidCacFlag.setDescription("\nVoice AP CAC flag")
voiceAPBssidTotVoiceClients = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidTotVoiceClients.setDescription("\nVoice AP total number of voice clients")
voiceAPBssidCallsSCCP = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidCallsSCCP.setDescription("\nVoice AP Total SCCP calls")
voiceAPBssidCallsSIP = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidCallsSIP.setDescription("\nVoice AP Total SIP calls")
voiceAPBssidCallsSVP = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidCallsSVP.setDescription("\nVoice AP Total SVP calls")
voiceAPBssidCallsVocera = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidCallsVocera.setDescription("\nVoice AP Total Vocera calls")
voiceAPBssidCallsNoe = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidCallsNoe.setDescription("\nVoice AP Total NOE calls")
voiceAPBssidEssid = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidEssid.setDescription("\nVoice AP ESSID")
voiceAPBssidCallsSIPS = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 4, 2, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voiceAPBssidCallsSIPS.setDescription("\nVoice AP Total SIPS calls")
wlsxVoiceClientLocationInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5))
wlsxVoiceClientLocationTotal = MibScalar((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxVoiceClientLocationTotal.setDescription("\nTotal Number of Active voice clients in the controller.")
wlsxVoiceClientLocationTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2))
if mibBuilder.loadTexts: wlsxVoiceClientLocationTable.setDescription("\nThis table lists all voice client Location Info")
wlsxVoiceClientLocationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1)).setIndexNames((0, "", "wlanStaPhyAddress"))
if mibBuilder.loadTexts: wlsxVoiceClientLocationEntry.setDescription("")
vcLocationIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcLocationIp.setDescription("\nVoice client IP Address ")
vcLocationMac = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcLocationMac.setDescription("\nVoice client Mac Address ")
vcLocationSwitchIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcLocationSwitchIp.setDescription("\nVoice Client Switch IP Address ")
vcLocationApName = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcLocationApName.setDescription("\nVoice Client AP Name")
vcLocationApMac = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcLocationApMac.setDescription("\nVoice client AP Mac Address ")
vcLocationApMode = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcLocationApMode.setDescription("\nVoice client AP Mode")
vcLocationApLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 12, 1, 5, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vcLocationApLoc.setDescription("\nVoice client Ap Location ")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("WLSX-VOICE-MIB", PYSNMP_MODULE_ID=wlsxVoiceMIB)

# Objects
mibBuilder.exportSymbols("WLSX-VOICE-MIB", wlsxVoiceMIB=wlsxVoiceMIB, wlsxVoiceStatsGroup=wlsxVoiceStatsGroup, wlsxVoiceCdrInfoGroup=wlsxVoiceCdrInfoGroup, wlsxVoiceCdrTotal=wlsxVoiceCdrTotal, wlsxVoiceCdrTable=wlsxVoiceCdrTable, wlsxVoiceCdrEntry=wlsxVoiceCdrEntry, voiceCdrId=voiceCdrId, voiceCdrIp=voiceCdrIp, voiceCdrMac=voiceCdrMac, voiceCdrName=voiceCdrName, voiceCdrDialNum=voiceCdrDialNum, voiceCdrDir=voiceCdrDir, voiceCdrOrigTime=voiceCdrOrigTime, voiceCdrSetupTime=voiceCdrSetupTime, voiceCdrTeardownTime=voiceCdrTeardownTime, voiceCdrStatus=voiceCdrStatus, voiceCdrReason=voiceCdrReason, voiceCdrDuration=voiceCdrDuration, voiceCdrRValue=voiceCdrRValue, voiceCdrApSwitchDelay=voiceCdrApSwitchDelay, voiceCdrCodec=voiceCdrCodec, voiceCdrApName=voiceCdrApName, voiceCdrApMac=voiceCdrApMac, voiceCdrBssid=voiceCdrBssid, voiceCdrEssid=voiceCdrEssid, voiceCdrHandovers=voiceCdrHandovers, voiceCdrMOS=voiceCdrMOS, wlsxVoiceCallCtrsGroup=wlsxVoiceCallCtrsGroup, voiceCallCtrsTotal=voiceCallCtrsTotal, voiceCallCtrsSuccess=voiceCallCtrsSuccess, voiceCallCtrsFailed=voiceCallCtrsFailed, voiceCallCtrsRejected=voiceCallCtrsRejected, voiceCallCtrsAborted=voiceCallCtrsAborted, voiceCallCtrsOrig=voiceCallCtrsOrig, voiceCallCtrsRecvd=voiceCallCtrsRecvd, voiceCallCtrsActive=voiceCallCtrsActive, voiceCallCtrsNotFnd=voiceCallCtrsNotFnd, voiceCallCtrsBusy=voiceCallCtrsBusy, voiceCallCtrsSvc=voiceCallCtrsSvc, voiceCallCtrsReqTerm=voiceCallCtrsReqTerm, voiceCallCtrsDecline=voiceCallCtrsDecline, voiceCallCtrsUnauth=voiceCallCtrsUnauth, voiceCallCtrsMisc=voiceCallCtrsMisc, wlsxVoiceClientInfoGroup=wlsxVoiceClientInfoGroup, wlsxVoiceClientTotal=wlsxVoiceClientTotal, wlsxVoiceClientTable=wlsxVoiceClientTable, wlsxVoiceClientEntry=wlsxVoiceClientEntry, voiceClientIp=voiceClientIp, voiceClientProtocol=voiceClientProtocol, voiceClientRegState=voiceClientRegState, voiceClientContactName=voiceClientContactName, voiceClientServerName=voiceClientServerName, voiceClientEssid=voiceClientEssid, voiceClientVlanId=voiceClientVlanId, voiceClientTunnelId=voiceClientTunnelId, wlsxVoiceAPBssidInfoGroup=wlsxVoiceAPBssidInfoGroup, wlsxVoiceAPBssidTotal=wlsxVoiceAPBssidTotal, wlsxVoiceAPBssidTable=wlsxVoiceAPBssidTable, wlsxVoiceAPBssidEntry=wlsxVoiceAPBssidEntry, voiceAPBssidName=voiceAPBssidName, voiceAPBssidGroup=voiceAPBssidGroup, voiceAPBssidIp=voiceAPBssidIp, voiceAPBssidTotCalls=voiceAPBssidTotCalls, voiceAPBssidVoiceType=voiceAPBssidVoiceType, voiceAPBssidFlag=voiceAPBssidFlag, voiceAPBssidUpTime=voiceAPBssidUpTime, voiceAPBssid100Sent=voiceAPBssid100Sent, voiceAPBssid503Sent=voiceAPBssid503Sent, voiceAPBssidExtraCallDisc=voiceAPBssidExtraCallDisc, voiceAPBssidKickedOff=voiceAPBssidKickedOff, voiceAPBssidTspecDenied=voiceAPBssidTspecDenied, voiceAPBssidCacFlag=voiceAPBssidCacFlag, voiceAPBssidTotVoiceClients=voiceAPBssidTotVoiceClients, voiceAPBssidCallsSCCP=voiceAPBssidCallsSCCP, voiceAPBssidCallsSIP=voiceAPBssidCallsSIP, voiceAPBssidCallsSVP=voiceAPBssidCallsSVP, voiceAPBssidCallsVocera=voiceAPBssidCallsVocera, voiceAPBssidCallsNoe=voiceAPBssidCallsNoe, voiceAPBssidEssid=voiceAPBssidEssid, voiceAPBssidCallsSIPS=voiceAPBssidCallsSIPS, wlsxVoiceClientLocationInfoGroup=wlsxVoiceClientLocationInfoGroup, wlsxVoiceClientLocationTotal=wlsxVoiceClientLocationTotal, wlsxVoiceClientLocationTable=wlsxVoiceClientLocationTable, wlsxVoiceClientLocationEntry=wlsxVoiceClientLocationEntry, vcLocationIp=vcLocationIp, vcLocationMac=vcLocationMac, vcLocationSwitchIp=vcLocationSwitchIp, vcLocationApName=vcLocationApName, vcLocationApMac=vcLocationApMac, vcLocationApMode=vcLocationApMode, vcLocationApLoc=vcLocationApLoc)

