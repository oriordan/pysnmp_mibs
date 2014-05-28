# PySNMP SMI module. Autogenerated from smidump -f python DISMAN-SCHEDULE-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:35 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, zeroDotZero, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2", "zeroDotZero")
( DateAndTime, RowStatus, StorageType, TextualConvention, VariablePointer, ) = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "RowStatus", "StorageType", "TextualConvention", "VariablePointer")

# Types

class SnmpPduErrorStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(18,8,13,7,6,15,11,0,17,3,5,9,4,14,-1,2,10,12,16,1,)
    namedValues = NamedValues(("noResponse", -1), ("noError", 0), ("tooBig", 1), ("wrongValue", 10), ("noCreation", 11), ("inconsistentValue", 12), ("resourceUnavailable", 13), ("commitFailed", 14), ("undoFailed", 15), ("authorizationError", 16), ("notWritable", 17), ("inconsistentName", 18), ("noSuchName", 2), ("badValue", 3), ("readOnly", 4), ("genErr", 5), ("noAccess", 6), ("wrongType", 7), ("wrongLength", 8), ("wrongEncoding", 9), )
    

# Objects

schedMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 63)).setRevisions(("2002-01-07 00:00","1998-11-17 18:00",))
if mibBuilder.loadTexts: schedMIB.setOrganization("IETF Distributed Management Working Group")
if mibBuilder.loadTexts: schedMIB.setContactInfo("WG EMail:  disman@dorothy.bmc.com\nSubscribe: disman-request@dorothy.bmc.com\n\nChair:     Randy Presuhn\n           BMC Software, Inc.\nPostal:    Office 1-3141\n           2141 North First Street\n           San Jose,  California 95131\n           USA\nEMail:     rpresuhn@bmc.com\nPhone:     +1 408 546-1006\n\nEditor:    David B. Levi\n           Nortel Networks\nPostal:    4401 Great America Parkway\n           Santa Clara, CA 95052-8185\n           USA\nEMail:     dlevi@nortelnetworks.com\nPhone:     +1 865 686 0432\n\nEditor:    Juergen Schoenwaelder\n           TU Braunschweig\nPostal:    Bueltenweg 74/75\n           38106 Braunschweig\n           Germany\nEMail:     schoenw@ibr.cs.tu-bs.de\nPhone:     +49 531 391-3283")
if mibBuilder.loadTexts: schedMIB.setDescription("This MIB module defines a MIB which provides mechanisms to\nschedule SNMP set operations periodically or at specific\npoints in time.")
schedObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 1))
schedLocalTime = MibScalar((1, 3, 6, 1, 2, 1, 63, 1, 1), DateAndTime().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLocalTime.setDescription("The local time used by the scheduler.  Schedules which\nrefer to calendar time will use the local time indicated\nby this object.  An implementation MUST return all 11 bytes\nof the DateAndTime textual-convention so that a manager\nmay retrieve the offset from GMT time.")
schedTable = MibTable((1, 3, 6, 1, 2, 1, 63, 1, 2))
if mibBuilder.loadTexts: schedTable.setDescription("This table defines scheduled actions triggered by\nSNMP set operations.")
schedEntry = MibTableRow((1, 3, 6, 1, 2, 1, 63, 1, 2, 1)).setIndexNames((0, "DISMAN-SCHEDULE-MIB", "schedOwner"), (0, "DISMAN-SCHEDULE-MIB", "schedName"))
if mibBuilder.loadTexts: schedEntry.setDescription("An entry describing a particular scheduled action.\n\nUnless noted otherwise, writable objects of this row\ncan be modified independent of the current value of\nschedRowStatus, schedAdminStatus and schedOperStatus.\nIn particular, it is legal to modify schedInterval\nand the objects in the schedCalendarGroup when\nschedRowStatus is active and schedAdminStatus and\nschedOperStatus are both enabled.")
schedOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: schedOwner.setDescription("The owner of this scheduling entry.  The exact semantics of\nthis string are subject to the security policy defined by\n\nthe security administrator.")
schedName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: schedName.setDescription("The locally-unique, administratively assigned name for this\nscheduling entry.  This object allows a schedOwner to have\nmultiple entries in the schedTable.")
schedDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 3), SnmpAdminString().clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedDescr.setDescription("The human readable description of the purpose of this\nscheduling entry.")
schedInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 4), Unsigned32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedInterval.setDescription("The number of seconds between two action invocations of\na periodic scheduler.  Implementations must guarantee\nthat action invocations will not occur before at least\nschedInterval seconds have passed.\n\nThe scheduler must ignore all periodic schedules that\nhave a schedInterval value of 0.  A periodic schedule\nwith a scheduling interval of 0 seconds will therefore\nnever invoke an action.\n\nImplementations may be forced to delay invocations in the\nface of local constraints.  A scheduled management function\nshould therefore not rely on the accuracy provided by the\nscheduler implementation.\n\nNote that implementations which maintain a list of pending\nactivations must re-calculate them when this object is\nchanged.")
schedWeekDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 5), Bits().subtype(namedValues=NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), )).clone(())).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedWeekDay.setDescription("The set of weekdays on which the scheduled action should\ntake place.  Setting multiple bits will include several\nweekdays in the set of possible weekdays for this schedule.\nSetting all bits will cause the scheduler to ignore the\nweekday.\n\nNote that implementations which maintain a list of pending\nactivations must re-calculate them when this object is\nchanged.")
schedMonth = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 6), Bits().subtype(namedValues=NamedValues(("january", 0), ("february", 1), ("november", 10), ("december", 11), ("march", 2), ("april", 3), ("may", 4), ("june", 5), ("july", 6), ("august", 7), ("september", 8), ("october", 9), )).clone(())).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedMonth.setDescription("The set of months during which the scheduled action should\ntake place.  Setting multiple bits will include several\nmonths in the set of possible months for this schedule.\n\nSetting all bits will cause the scheduler to ignore the\nmonth.\n\nNote that implementations which maintain a list of pending\nactivations must re-calculate them when this object is\nchanged.")
schedDay = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 7), Bits().subtype(namedValues=NamedValues(("d1", 0), ("d2", 1), ("d11", 10), ("d12", 11), ("d13", 12), ("d14", 13), ("d15", 14), ("d16", 15), ("d17", 16), ("d18", 17), ("d19", 18), ("d20", 19), ("d3", 2), ("d21", 20), ("d22", 21), ("d23", 22), ("d24", 23), ("d25", 24), ("d26", 25), ("d27", 26), ("d28", 27), ("d29", 28), ("d30", 29), ("d4", 3), ("d31", 30), ("r1", 31), ("r2", 32), ("r3", 33), ("r4", 34), ("r5", 35), ("r6", 36), ("r7", 37), ("r8", 38), ("r9", 39), ("d5", 4), ("r10", 40), ("r11", 41), ("r12", 42), ("r13", 43), ("r14", 44), ("r15", 45), ("r16", 46), ("r17", 47), ("r18", 48), ("r19", 49), ("d6", 5), ("r20", 50), ("r21", 51), ("r22", 52), ("r23", 53), ("r24", 54), ("r25", 55), ("r26", 56), ("r27", 57), ("r28", 58), ("r29", 59), ("d7", 6), ("r30", 60), ("r31", 61), ("d8", 7), ("d9", 8), ("d10", 9), )).clone(())).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedDay.setDescription("The set of days in a month on which a scheduled action\nshould take place.  There are two sets of bits one can\nuse to define the day within a month:\n\nEnumerations starting with the letter 'd' indicate a\nday in a month relative to the first day of a month.\nThe first day of the month can therefore be specified\nby setting the bit d1(0) and d31(30) means the last\nday of a month with 31 days.\n\nEnumerations starting with the letter 'r' indicate a\nday in a month in reverse order, relative to the last\nday of a month.  The last day in the month can therefore\nbe specified by setting the bit r1(31) and r31(61) means\nthe first day of a month with 31 days.\n\nSetting multiple bits will include several days in the set\nof possible days for this schedule.  Setting all bits will\ncause the scheduler to ignore the day within a month.\n\nSetting all bits starting with the letter 'd' or the\nletter 'r' will also cause the scheduler to ignore the\nday within a month.\n\nNote that implementations which maintain a list of pending\nactivations must re-calculate them when this object is\nchanged.")
schedHour = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 8), Bits().subtype(namedValues=NamedValues(("h0", 0), ("h1", 1), ("h10", 10), ("h11", 11), ("h12", 12), ("h13", 13), ("h14", 14), ("h15", 15), ("h16", 16), ("h17", 17), ("h18", 18), ("h19", 19), ("h2", 2), ("h20", 20), ("h21", 21), ("h22", 22), ("h23", 23), ("h3", 3), ("h4", 4), ("h5", 5), ("h6", 6), ("h7", 7), ("h8", 8), ("h9", 9), )).clone(())).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedHour.setDescription("The set of hours within a day during which the scheduled\naction should take place.\n\nNote that implementations which maintain a list of pending\nactivations must re-calculate them when this object is\nchanged.")
schedMinute = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 9), Bits().subtype(namedValues=NamedValues(("m0", 0), ("m1", 1), ("m10", 10), ("m11", 11), ("m12", 12), ("m13", 13), ("m14", 14), ("m15", 15), ("m16", 16), ("m17", 17), ("m18", 18), ("m19", 19), ("m2", 2), ("m20", 20), ("m21", 21), ("m22", 22), ("m23", 23), ("m24", 24), ("m25", 25), ("m26", 26), ("m27", 27), ("m28", 28), ("m29", 29), ("m3", 3), ("m30", 30), ("m31", 31), ("m32", 32), ("m33", 33), ("m34", 34), ("m35", 35), ("m36", 36), ("m37", 37), ("m38", 38), ("m39", 39), ("m4", 4), ("m40", 40), ("m41", 41), ("m42", 42), ("m43", 43), ("m44", 44), ("m45", 45), ("m46", 46), ("m47", 47), ("m48", 48), ("m49", 49), ("m5", 5), ("m50", 50), ("m51", 51), ("m52", 52), ("m53", 53), ("m54", 54), ("m55", 55), ("m56", 56), ("m57", 57), ("m58", 58), ("m59", 59), ("m6", 6), ("m7", 7), ("m8", 8), ("m9", 9), )).clone(())).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedMinute.setDescription("The set of minutes within an hour when the scheduled action\nshould take place.\n\nNote that implementations which maintain a list of pending\nactivations must re-calculate them when this object is\nchanged.")
schedContextName = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedContextName.setDescription("The context which contains the local MIB variable pointed\nto by schedVariable.")
schedVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 11), VariablePointer().clone('0.0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedVariable.setDescription("An object identifier pointing to a local MIB variable\nwhich resolves to an ASN.1 primitive type of INTEGER.")
schedValue = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 12), Integer32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedValue.setDescription("The value which is written to the MIB object pointed to by\nschedVariable when the scheduler invokes an action.  The\nimplementation shall enforce the use of access control\nrules when performing the set operation on schedVariable.\nThis is accomplished by calling the isAccessAllowed abstract\nservice interface as defined in RFC 2571.\n\nNote that an implementation may choose to issue an SNMP Set\nmessage to the SNMP engine and leave the access control\ndecision to the normal message processing procedure.")
schedType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 13), Integer().subtype(subtypeSpec=SingleValueConstraint(3,2,1,)).subtype(namedValues=NamedValues(("periodic", 1), ("calendar", 2), ("oneshot", 3), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedType.setDescription("The type of this schedule.  The value periodic(1) indicates\nthat this entry specifies a periodic schedule.  A periodic\nschedule is defined by the value of schedInterval.  The\nvalues of schedWeekDay, schedMonth, schedDay, schedHour\nand schedMinute are ignored.\n\nThe value calendar(2) indicates that this entry describes a\ncalendar schedule.  A calendar schedule is defined by the\nvalues of schedWeekDay, schedMonth, schedDay, schedHour and\nschedMinute.  The value of schedInterval is ignored.  A\ncalendar schedule will trigger on all local times that\nsatisfy the bits set in schedWeekDay, schedMonth, schedDay,\nschedHour and schedMinute.\n\nThe value oneshot(3) indicates that this entry describes a\none-shot schedule.  A one-shot schedule is similar to a\ncalendar schedule with the additional feature that it\ndisables itself by changing in the `finished'\nschedOperStatus once the schedule triggers an action.\n\nNote that implementations which maintain a list of pending\nactivations must re-calculate them when this object is\nchanged.")
schedAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 14), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), )).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedAdminStatus.setDescription("The desired state of the schedule.")
schedOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 15), Integer().subtype(subtypeSpec=SingleValueConstraint(2,3,1,)).subtype(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("finished", 3), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedOperStatus.setDescription("The current operational state of this schedule.  The state\nenabled(1) indicates this entry is active and that the\nscheduler will invoke actions at appropriate times.  The\ndisabled(2) state indicates that this entry is currently\ninactive and ignored by the scheduler.  The finished(3)\nstate indicates that the schedule has ended.  Schedules\nin the finished(3) state are ignored by the scheduler.\nA one-shot schedule enters the finished(3) state when it\ndeactivates itself.\n\nNote that the operational state must not be enabled(1)\nwhen the schedRowStatus is not active.")
schedFailures = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedFailures.setDescription("This variable counts the number of failures while invoking\nthe scheduled action.  This counter at most increments once\nfor a triggered action.")
schedLastFailure = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 17), SnmpPduErrorStatus().clone('noError')).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLastFailure.setDescription("The most recent error that occurred during the invocation of\na scheduled action.  The value noError(0) is returned\nif no errors have occurred yet.")
schedLastFailed = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 18), DateAndTime().clone(hexValue='0000000000000000')).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedLastFailed.setDescription("The date and time when the most recent failure occurred.\n\nThe value '0000000000000000'H is returned if no failure\noccurred since the last re-initialization of the scheduler.")
schedStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 19), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedStorageType.setDescription("This object defines whether this scheduled action is kept\nin volatile storage and lost upon reboot or if this row is\nbacked up by non-volatile or permanent storage.\n\nConceptual rows having the value `permanent' must allow\nwrite access to the columnar objects schedDescr,\nschedInterval, schedContextName, schedVariable, schedValue,\nand schedAdminStatus.  If an implementation supports the\nschedCalendarGroup, write access must be also allowed to\nthe columnar objects schedWeekDay, schedMonth, schedDay,\nschedHour, schedMinute.")
schedRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: schedRowStatus.setDescription("The status of this scheduled action.  A control that allows\nentries to be added and removed from this table.\n\nNote that the operational state must change to enabled\nwhen the administrative state is enabled and the row\nstatus changes to active(1).\n\nAttempts to destroy(6) a row or to set a row\nnotInService(2) while the operational state is enabled\nresult in inconsistentValue errors.\n\nThe value of this object has no effect on whether other\nobjects in this conceptual row can be modified.")
schedTriggers = MibTableColumn((1, 3, 6, 1, 2, 1, 63, 1, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: schedTriggers.setDescription("This variable counts the number of attempts (either\nsuccessful or failed) to invoke the scheduled action.")
schedNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2))
schedTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 2, 0))
schedConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3))
schedCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 1))
schedGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 63, 3, 2))

# Augmentions

# Notifications

schedActionFailure = NotificationType((1, 3, 6, 1, 2, 1, 63, 2, 0, 1)).setObjects(*(("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ) )
if mibBuilder.loadTexts: schedActionFailure.setDescription("This notification is generated whenever the invocation of a\nscheduled action fails.")

# Groups

schedGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 1)).setObjects(*(("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), ) )
if mibBuilder.loadTexts: schedGroup.setDescription("A collection of objects providing scheduling capabilities.")
schedCalendarGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 2)).setObjects(*(("DISMAN-SCHEDULE-MIB", "schedHour"), ("DISMAN-SCHEDULE-MIB", "schedMonth"), ("DISMAN-SCHEDULE-MIB", "schedWeekDay"), ("DISMAN-SCHEDULE-MIB", "schedDay"), ("DISMAN-SCHEDULE-MIB", "schedMinute"), ("DISMAN-SCHEDULE-MIB", "schedLocalTime"), ) )
if mibBuilder.loadTexts: schedCalendarGroup.setDescription("A collection of objects providing calendar based schedules.")
schedNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 3)).setObjects(*(("DISMAN-SCHEDULE-MIB", "schedActionFailure"), ) )
if mibBuilder.loadTexts: schedNotificationsGroup.setDescription("The notifications emitted by the scheduler.")
schedGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 63, 3, 2, 4)).setObjects(*(("DISMAN-SCHEDULE-MIB", "schedOperStatus"), ("DISMAN-SCHEDULE-MIB", "schedTriggers"), ("DISMAN-SCHEDULE-MIB", "schedLastFailed"), ("DISMAN-SCHEDULE-MIB", "schedStorageType"), ("DISMAN-SCHEDULE-MIB", "schedLastFailure"), ("DISMAN-SCHEDULE-MIB", "schedVariable"), ("DISMAN-SCHEDULE-MIB", "schedType"), ("DISMAN-SCHEDULE-MIB", "schedAdminStatus"), ("DISMAN-SCHEDULE-MIB", "schedDescr"), ("DISMAN-SCHEDULE-MIB", "schedRowStatus"), ("DISMAN-SCHEDULE-MIB", "schedValue"), ("DISMAN-SCHEDULE-MIB", "schedFailures"), ("DISMAN-SCHEDULE-MIB", "schedInterval"), ("DISMAN-SCHEDULE-MIB", "schedContextName"), ) )
if mibBuilder.loadTexts: schedGroup2.setDescription("A collection of objects providing scheduling capabilities.")

# Compliances

schedCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 63, 3, 1, 1)).setObjects(*(("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"), ("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"), ("DISMAN-SCHEDULE-MIB", "schedGroup"), ) )
if mibBuilder.loadTexts: schedCompliance.setDescription("The compliance statement for SNMP entities which implement\nthe scheduling MIB.")
schedCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 63, 3, 1, 2)).setObjects(*(("DISMAN-SCHEDULE-MIB", "schedNotificationsGroup"), ("DISMAN-SCHEDULE-MIB", "schedCalendarGroup"), ("DISMAN-SCHEDULE-MIB", "schedGroup2"), ) )
if mibBuilder.loadTexts: schedCompliance2.setDescription("The compliance statement for SNMP entities which implement\nthe scheduling MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", PYSNMP_MODULE_ID=schedMIB)

# Types
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", SnmpPduErrorStatus=SnmpPduErrorStatus)

# Objects
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedMIB=schedMIB, schedObjects=schedObjects, schedLocalTime=schedLocalTime, schedTable=schedTable, schedEntry=schedEntry, schedOwner=schedOwner, schedName=schedName, schedDescr=schedDescr, schedInterval=schedInterval, schedWeekDay=schedWeekDay, schedMonth=schedMonth, schedDay=schedDay, schedHour=schedHour, schedMinute=schedMinute, schedContextName=schedContextName, schedVariable=schedVariable, schedValue=schedValue, schedType=schedType, schedAdminStatus=schedAdminStatus, schedOperStatus=schedOperStatus, schedFailures=schedFailures, schedLastFailure=schedLastFailure, schedLastFailed=schedLastFailed, schedStorageType=schedStorageType, schedRowStatus=schedRowStatus, schedTriggers=schedTriggers, schedNotifications=schedNotifications, schedTraps=schedTraps, schedConformance=schedConformance, schedCompliances=schedCompliances, schedGroups=schedGroups)

# Notifications
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedActionFailure=schedActionFailure)

# Groups
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedGroup=schedGroup, schedCalendarGroup=schedCalendarGroup, schedNotificationsGroup=schedNotificationsGroup, schedGroup2=schedGroup2)

# Compliances
mibBuilder.exportSymbols("DISMAN-SCHEDULE-MIB", schedCompliance=schedCompliance, schedCompliance2=schedCompliance2)
