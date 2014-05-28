# PySNMP SMI module. Autogenerated from smidump -f python OLD-CISCO-TS-MIB
# by libsmi2pysnmp-0.1.3 at Tue May 27 10:13:45 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( local, ) = mibBuilder.importSymbols("CISCO-SMI", "local")
( MibScalar, MibTable, MibTableRow, MibTableColumn, ) = mibBuilder.importSymbols("RFC-1212", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
( IpAddress, ) = mibBuilder.importSymbols("RFC1155-SMI", "IpAddress")
( DisplayString, ) = mibBuilder.importSymbols("RFC1213-MIB", "DisplayString")
( Bits, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "TimeTicks")

# Objects

lts = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 2, 9))
tsLines = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLines.setDescription("Number of terminal lines on this device.\nIncludes virtual lines.")
ltsLineTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 9, 2))
if mibBuilder.loadTexts: ltsLineTable.setDescription("A list of terminal server line entries.")
ltsLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1)).setIndexNames((0, "OLD-CISCO-TS-MIB", "tsLineNumber"))
if mibBuilder.loadTexts: ltsLineEntry.setDescription("A collection of per TTY objects in the\ncisco Terminal Server implementation.")
tsLineActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineActive.setDescription("Boolean whether this line is active or not.")
tsLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(2,6,1,5,3,4,)).subtype(namedValues=NamedValues(("unknown", 1), ("console", 2), ("terminal", 3), ("line-printer", 4), ("virtual-terminal", 5), ("auxiliary", 6), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineType.setDescription("Type of line.")
tsLineAutobaud = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineAutobaud.setDescription("Boolean whether line will autobaud or not.")
tsLineSpeedin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineSpeedin.setDescription("What input speed the line is running at.")
tsLineSpeedout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineSpeedout.setDescription("What output speed the line is running at.")
tsLineFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(5,6,2,4,1,3,8,7,)).subtype(namedValues=NamedValues(("unknown", 1), ("none", 2), ("software-input", 3), ("software-output", 4), ("software-both", 5), ("hardware-input", 6), ("hardware-output", 7), ("hardware-both", 8), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineFlow.setDescription("What kind of flow control the line is\nusing.")
tsLineModem = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,5,6,1,4,7,)).subtype(namedValues=NamedValues(("unknown", 1), ("none", 2), ("call-in", 3), ("call-out", 4), ("cts-required", 5), ("ri-is-cd", 6), ("inout", 7), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineModem.setDescription("What kind of modem control the line is\nusing.")
tsLineLoc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineLoc.setDescription("Describes the line's physical location.")
tsLineTerm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineTerm.setDescription("Describes the line's terminal type.")
tsLineScrlen = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineScrlen.setDescription("Length in lines of the screen of terminal\nattached to this line.")
tsLineScrwid = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineScrwid.setDescription("Width in characters of the screen of\nterminal attached to this line.")
tsLineEsc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineEsc.setDescription("Escape character used to break out of active\nsessions.")
tsLineTmo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineTmo.setDescription("Line idleness timeout in seconds.")
tsLineSestmo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineSestmo.setDescription("Session idleness timeout in seconds.")
tsLineRotary = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineRotary.setDescription("Rotary group number the line belongs in.")
tsLineUses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineUses.setDescription("Number of times a connection has been made\nto or from this line.")
tsLineNses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineNses.setDescription("Current number of sessions in use on this\nline.")
tsLineUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineUser.setDescription("TACACS user name, if TACACS enabled, of user\non this line.")
tsLineNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineNoise.setDescription("Count of garbage characters received when\nline inactive.")
tsLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineNumber.setDescription("The line i've been talking about.")
tsLineTimeActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsLineTimeActive.setDescription("The time in seconds since line was activated.")
ltsLineSessionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 2, 9, 3))
if mibBuilder.loadTexts: ltsLineSessionTable.setDescription("A list of terminal server line and session\nentries.")
ltsLineSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1)).setIndexNames((0, "OLD-CISCO-TS-MIB", "tslineSesLine"), (0, "OLD-CISCO-TS-MIB", "tslineSesSession"))
if mibBuilder.loadTexts: ltsLineSessionEntry.setDescription("A collection of per session and per TTY\nobjects in the cisco Terminal Server\nimplementation.")
tslineSesType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(3,8,6,5,9,7,11,4,1,2,10,)).subtype(namedValues=NamedValues(("unknown", 1), ("xremote", 10), ("rshell", 11), ("pad", 2), ("stream", 3), ("rlogin", 4), ("telnet", 5), ("tcp", 6), ("lat", 7), ("mop", 8), ("slip", 9), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tslineSesType.setDescription("Type of session.")
tslineSesDir = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(1,3,2,)).subtype(namedValues=NamedValues(("unknown", 1), ("incoming", 2), ("outgoing", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tslineSesDir.setDescription("Direction of session.")
tslineSesAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tslineSesAddr.setDescription("Remote host address of session. [What about\nPAD connections?]")
tslineSesName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tslineSesName.setDescription("Remote host name of session.")
tslineSesCur = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tslineSesCur.setDescription("Boolean whether session is the currently\nactive one.")
tslineSesIdle = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tslineSesIdle.setDescription("Time in seconds session has been idle.")
tslineSesLine = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tslineSesLine.setDescription("Table index 1.")
tslineSesSession = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tslineSesSession.setDescription("Table index 2.")
tsMsgTtyLine = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 9, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsMsgTtyLine.setDescription("tty line to send the message to. -1 will\nsend it to all tty lines")
tsMsgIntervaltim = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 9, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsMsgIntervaltim.setDescription("Interval between reissuing message in\nmilliseconds. Minimum non-zero setting is\n10000. 0 will cause the routine to choose its\nown intervals becoming more frequent as\nMessageDuration gets close to expiring. 2hr,\n1hr, 30min, 5min, 1min")
tsMsgDuration = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 9, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsMsgDuration.setDescription("Length of time to reissue message in\nmilliseconds. Minimum non-zero setting is\n10000. A setting of 0 will not repeat the\nmessage.")
tsMsgText = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 9, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsMsgText.setDescription("Up to 256 characters that will make up the\nmessage")
tsMsgTmpBanner = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 9, 8), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("no", 1), ("additive", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsMsgTmpBanner.setDescription("Should the message be used as a temporary\nbanner. 1 - No. 2 - In addition to the normal\nbanner")
tsMsgSend = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 9, 9), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,3,4,)).subtype(namedValues=NamedValues(("nothing", 1), ("reload", 2), ("messagedone", 3), ("abort", 4), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsMsgSend.setDescription("Sends the message. The value determines what\nto do after the message has completed.")
tsClrTtyLine = MibScalar((1, 3, 6, 1, 4, 1, 9, 2, 9, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsClrTtyLine.setDescription("tty line to clear.  Read returns the last line\ncleared.  A value of -1 indicates no lines have \nbeen cleared.")

# Augmentions

# Exports

# Objects
mibBuilder.exportSymbols("OLD-CISCO-TS-MIB", lts=lts, tsLines=tsLines, ltsLineTable=ltsLineTable, ltsLineEntry=ltsLineEntry, tsLineActive=tsLineActive, tsLineType=tsLineType, tsLineAutobaud=tsLineAutobaud, tsLineSpeedin=tsLineSpeedin, tsLineSpeedout=tsLineSpeedout, tsLineFlow=tsLineFlow, tsLineModem=tsLineModem, tsLineLoc=tsLineLoc, tsLineTerm=tsLineTerm, tsLineScrlen=tsLineScrlen, tsLineScrwid=tsLineScrwid, tsLineEsc=tsLineEsc, tsLineTmo=tsLineTmo, tsLineSestmo=tsLineSestmo, tsLineRotary=tsLineRotary, tsLineUses=tsLineUses, tsLineNses=tsLineNses, tsLineUser=tsLineUser, tsLineNoise=tsLineNoise, tsLineNumber=tsLineNumber, tsLineTimeActive=tsLineTimeActive, ltsLineSessionTable=ltsLineSessionTable, ltsLineSessionEntry=ltsLineSessionEntry, tslineSesType=tslineSesType, tslineSesDir=tslineSesDir, tslineSesAddr=tslineSesAddr, tslineSesName=tslineSesName, tslineSesCur=tslineSesCur, tslineSesIdle=tslineSesIdle, tslineSesLine=tslineSesLine, tslineSesSession=tslineSesSession, tsMsgTtyLine=tsMsgTtyLine, tsMsgIntervaltim=tsMsgIntervaltim, tsMsgDuration=tsMsgDuration, tsMsgText=tsMsgText, tsMsgTmpBanner=tsMsgTmpBanner, tsMsgSend=tsMsgSend, tsClrTtyLine=tsClrTtyLine)

