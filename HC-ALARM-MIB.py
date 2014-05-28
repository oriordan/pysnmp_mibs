# PySNMP SMI module. Autogenerated from smidump -f python HC-ALARM-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:40 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( CounterBasedGauge64, ) = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
( OwnerString, rmon, rmonEventGroup, ) = mibBuilder.importSymbols("RMON-MIB", "OwnerString", "rmon", "rmonEventGroup")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter32, Integer32, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowStatus, StorageType, TextualConvention, VariablePointer, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention", "VariablePointer")

# Types

class HcValueStatus(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,2,3,)
    namedValues = NamedValues(("valueNotAvailable", 1), ("valuePositive", 2), ("valueNegative", 3), )
    

# Objects

hcAlarmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 29)).setRevisions(("2002-12-16 00:00",))
if mibBuilder.loadTexts: hcAlarmMIB.setOrganization("IETF RMONMIB Working Group")
if mibBuilder.loadTexts: hcAlarmMIB.setContactInfo("        Andy Bierman\nCisco Systems, Inc.\nTel: +1 408 527-3711\n\n\n\nE-mail: abierman@cisco.com\nPostal: 170 West Tasman Drive\nSan Jose, CA USA 95134\n\nKeith McCloghrie\nCisco Systems, Inc.\nTel: +1 408 526-5260\nE-mail: kzm@cisco.com\nPostal: 170 West Tasman Drive\nSan Jose, CA USA 95134\n\nSend comments to <rmonmib@ietf.org>\nMailing list subscription info:\nhttp://www.ietf.org/mailman/listinfo/rmonmib ")
if mibBuilder.loadTexts: hcAlarmMIB.setDescription("This module defines Remote Monitoring MIB extensions for\nHigh Capacity Alarms.\n\nCopyright (C) The Internet Society (2002). This version\nof this MIB module is part of RFC 3434; see the RFC\nitself for full legal notices.")
hcAlarmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1))
hcAlarmControlObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1, 1))
hcAlarmTable = MibTable((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1))
if mibBuilder.loadTexts: hcAlarmTable.setDescription("A list of entries for the configuration of high capacity\nalarms.")
hcAlarmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1)).setIndexNames((0, "HC-ALARM-MIB", "hcAlarmIndex"))
if mibBuilder.loadTexts: hcAlarmEntry.setDescription("A conceptual row in the hcAlarmTable. Entries are usually\ncreated in this table by management application action, but\nmay also be created by agent action as well.")
hcAlarmIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: hcAlarmIndex.setDescription("An arbitrary integer index value used to uniquely identify\nthis high capacity alarm entry.")
hcAlarmInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmInterval.setDescription("The interval in seconds over which the data is sampled and\ncompared with the rising and falling thresholds.  When\nsetting this variable, care should be taken in the case of\ndeltaValue sampling - the interval should be set short\nenough that the sampled variable is very unlikely to\nincrease or decrease by more than 2^63 - 1 during a single\nsampling interval.\n\n\n\n\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 3), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmVariable.setDescription("The object identifier of the particular variable to be\nsampled.  Only variables that resolve to an ASN.1 primitive\ntype of INTEGER (INTEGER, Integer32, Counter32, Counter64,\nGauge, or TimeTicks) may be sampled.\n\nBecause SNMP access control is articulated entirely in terms\nof the contents of MIB views, no access control mechanism\nexists that can restrict the value of this object to\nidentify only those objects that exist in a particular MIB\nview.  Because there is thus no acceptable means of\nrestricting the read access that could be obtained through\nthe alarm mechanism, the probe must only grant write access\nto this object in those views that have read access to all\nobjects on the probe.\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmSampleType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmSampleType.setDescription("The method of sampling the selected variable and\ncalculating the value to be compared against the thresholds.\nIf the value of this object is absoluteValue(1), the value\nof the selected variable will be compared directly with the\nthresholds at the end of the sampling interval.  If the\nvalue of this object is deltaValue(2), the value of the\nselected variable at the last sample will be subtracted from\nthe current value, and the difference compared with the\nthresholds.\n\nIf the associated hcAlarmVariable instance could not be\nobtained at the previous sample interval, then a delta\n\n\n\nsample is not possible, and the value of the associated\nhcAlarmValueStatus object for this interval will be\nvalueNotAvailable(1).\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmAbsValue = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 5), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmAbsValue.setDescription("The absolute value (i.e., unsigned value) of the\nhcAlarmVariable statistic during the last sampling period.\nThe value during the current sampling period is not made\navailable until the period is completed.\n\nTo obtain the true value for this sampling interval, the\nassociated instance of hcAlarmValueStatus must be checked,\nand the value of this object adjusted as necessary.\n\nIf the MIB instance could not be accessed during the\nsampling interval, then this object will have a value of\nzero and the associated instance of hcAlarmValueStatus will\nbe set to 'valueNotAvailable(1)'.")
hcAlarmValueStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 6), HcValueStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmValueStatus.setDescription("This object indicates the validity and sign of the data for\nthe hcAlarmAbsValue object, as described in the\nHcValueStatus textual convention.")
hcAlarmStartupAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,3,)).subtype(namedValues=NamedValues(("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmStartupAlarm.setDescription("The alarm that may be sent when this entry is first set to\n\n\n\nactive.  If the first sample after this entry becomes active\nis greater than or equal to the rising threshold and this\nobject is equal to risingAlarm(1) or\nrisingOrFallingAlarm(3), then a single rising alarm will be\ngenerated.  If the first sample after this entry becomes\nvalid is less than or equal to the falling threshold and\nthis object is equal to fallingAlarm(2) or\nrisingOrFallingAlarm(3), then a single falling alarm will be\ngenerated.\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmRisingThreshAbsValueLo = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingThreshAbsValueLo.setDescription("The lower 32 bits of the absolute value for threshold for\nthe sampled statistic.  The actual threshold value is\ndetermined by the associated instances of the\nhcAlarmRisingThreshAbsValueHi and\nhcAlarmRisingThresholdValStatus objects, as follows:\n\n   ABS(threshold) = hcAlarmRisingThreshAbsValueLo +\n         (hcAlarmRisingThreshAbsValueHi * 2^^32)\n\nThe absolute value of the threshold is adjusted as required,\nas described in the HcValueStatus textual convention.  These\nthree object instances are conceptually combined to\nrepresent the rising threshold for this entry.\n\nWhen the current sampled value is greater than or equal to\nthis threshold, and the value at the last sampling interval\nwas less than this threshold, a single event will be\ngenerated.  A single event will also be generated if the\nfirst sample after this entry becomes valid is greater than\nor equal to this threshold and the associated\nhcAlarmStartupAlarm is equal to risingAlarm(1) or\nrisingOrFallingAlarm(3).\n\nAfter a rising event is generated, another such event will\nnot be generated until the sampled value falls below this\nthreshold and reaches the threshold identified by the\nhcAlarmFallingThreshAbsValueLo,\nhcAlarmFallingThreshAbsValueHi, and\nhcAlarmFallingThresholdValStatus objects.\n\n\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmRisingThreshAbsValueHi = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingThreshAbsValueHi.setDescription("The upper 32 bits of the absolute value for threshold for\nthe sampled statistic.  The actual threshold value is\ndetermined by the associated instances of the\nhcAlarmRisingThreshAbsValueLo and\nhcAlarmRisingThresholdValStatus objects, as follows:\n\n   ABS(threshold) = hcAlarmRisingThreshAbsValueLo +\n         (hcAlarmRisingThreshAbsValueHi * 2^^32)\n\nThe absolute value of the threshold is adjusted as required,\nas described in the HcValueStatus textual convention.  These\nthree object instances are conceptually combined to\nrepresent the rising threshold for this entry.\n\nWhen the current sampled value is greater than or equal to\nthis threshold, and the value at the last sampling interval\nwas less than this threshold, a single event will be\ngenerated.  A single event will also be generated if the\nfirst sample after this entry becomes valid is greater than\nor equal to this threshold and the associated\nhcAlarmStartupAlarm is equal to risingAlarm(1) or\nrisingOrFallingAlarm(3).\n\nAfter a rising event is generated, another such event will\nnot be generated until the sampled value falls below this\nthreshold and reaches the threshold identified by the\nhcAlarmFallingThreshAbsValueLo,\nhcAlarmFallingThreshAbsValueHi, and\nhcAlarmFallingThresholdValStatus objects.\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmRisingThresholdValStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 10), HcValueStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingThresholdValStatus.setDescription("This object indicates the sign of the data for the rising\nthreshold, as defined by the hcAlarmRisingThresAbsValueLo\nand hcAlarmRisingThresAbsValueHi objects, as described in\nthe HcValueStatus textual convention.\n\nThe enumeration 'valueNotAvailable(1)' is not allowed, and\nthe associated hcAlarmStatus object cannot be equal to\n'active(1)' if this object is set to this value.\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmFallingThreshAbsValueLo = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingThreshAbsValueLo.setDescription("The lower 32 bits of the absolute value for threshold for\nthe sampled statistic.  The actual threshold value is\ndetermined by the associated instances of the\nhcAlarmFallingThreshAbsValueHi and\nhcAlarmFallingThresholdValStatus objects, as follows:\n\n   ABS(threshold) = hcAlarmFallingThreshAbsValueLo +\n         (hcAlarmFallingThreshAbsValueHi * 2^^32)\n\nThe absolute value of the threshold is adjusted as required,\nas described in the HcValueStatus textual convention.  These\nthree object instances are conceptually combined to\nrepresent the falling threshold for this entry.\n\nWhen the current sampled value is less than or equal to this\nthreshold, and the value at the last sampling interval was\ngreater than this threshold, a single event will be\ngenerated.  A single event will also be generated if the\nfirst sample after this entry becomes valid is less than or\nequal to this threshold and the associated\nhcAlarmStartupAlarm is equal to fallingAlarm(2) or\nrisingOrFallingAlarm(3).\n\nAfter a falling event is generated, another such event will\nnot be generated until the sampled value rises above this\nthreshold and reaches the threshold identified by the\nhcAlarmRisingThreshAbsValueLo,\nhcAlarmRisingThreshAbsValueHi, and\nhcAlarmRisingThresholdValStatus objects.\n\n\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmFallingThreshAbsValueHi = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingThreshAbsValueHi.setDescription("The upper 32 bits of the absolute value for threshold for\nthe sampled statistic.  The actual threshold value is\ndetermined by the associated instances of the\nhcAlarmFallingThreshAbsValueLo and\nhcAlarmFallingThresholdValStatus objects, as follows:\n\n   ABS(threshold) = hcAlarmFallingThreshAbsValueLo +\n         (hcAlarmFallingThreshAbsValueHi * 2^^32)\n\nThe absolute value of the threshold is adjusted as required,\nas described in the HcValueStatus textual convention.  These\nthree object instances are conceptually combined to\nrepresent the falling threshold for this entry.\n\nWhen the current sampled value is less than or equal to this\nthreshold, and the value at the last sampling interval was\ngreater than this threshold, a single event will be\ngenerated.  A single event will also be generated if the\nfirst sample after this entry becomes valid is less than or\nequal to this threshold and the associated\nhcAlarmStartupAlarm is equal to fallingAlarm(2) or\nrisingOrFallingAlarm(3).\n\nAfter a falling event is generated, another such event will\nnot be generated until the sampled value rises above this\nthreshold and reaches the threshold identified by the\nhcAlarmRisingThreshAbsValueLo,\nhcAlarmRisingThreshAbsValueHi, and\nhcAlarmRisingThresholdValStatus objects.\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmFallingThresholdValStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 13), HcValueStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingThresholdValStatus.setDescription("This object indicates the sign of the data for the falling\nthreshold, as defined by the hcAlarmFallingThreshAbsValueLo\nand hcAlarmFallingThreshAbsValueHi objects, as described in\nthe HcValueStatus textual convention.\n\nThe enumeration 'valueNotAvailable(1)' is not allowed, and\nthe associated hcAlarmStatus object cannot be equal to\n'active(1)' if this object is set to this value.\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmRisingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingEventIndex.setDescription("The index of the eventEntry that is used when a rising\nthreshold is crossed.  The eventEntry identified by a\nparticular value of this index is the same as identified by\nthe same value of the eventIndex object.  If there is no\ncorresponding entry in the eventTable, then no association\nexists.  In particular, if this value is zero, no associated\nevent will be generated, as zero is not a valid event index.\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmFallingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingEventIndex.setDescription("The index of the eventEntry that is used when a falling\nthreshold is crossed.  The eventEntry identified by a\nparticular value of this index is the same as identified by\nthe same value of the eventIndex object.  If there is no\ncorresponding entry in the eventTable, then no association\nexists.  In particular, if this value is zero, no associated\nevent will be generated, as zero is not a valid event index.\n\nThis object may not be modified if the associated\nhcAlarmStatus object is equal to active(1).")
hcAlarmValueFailedAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmValueFailedAttempts.setDescription("The number of times the associated hcAlarmVariable instance\nwas polled on behalf of this hcAlarmEntry, (while in the\nactive state) and the value was not available.  This counter\nmay experience a discontinuity if the agent restarts,\nindicated by the value of sysUpTime.")
hcAlarmOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 17), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmOwner.setDescription("The entity that configured this entry and is therefore\nusing the resources assigned to it.")
hcAlarmStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 18), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmStorageType.setDescription("The type of non-volatile storage configured for this entry.\nIf this object is equal to 'permanent(4)', then the\nassociated hcAlarmRisingEventIndex and\nhcAlarmFallingEventIndex objects must be writable.")
hcAlarmStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmStatus.setDescription("The status of this row.\n\nAn entry MUST NOT exist in the active state unless all\nobjects in the entry have an appropriate value, as described\nin the description clause for each writable object.\n\nThe hcAlarmStatus object may be modified if the associated\ninstance of this object is equal to active(1),\nnotInService(2), or notReady(3).  All other writable objects\nmay be modified if the associated instance of this object is\nequal to notInService(2) or notReady(3).")
hcAlarmCapabilitiesObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1, 2))
hcAlarmCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 16, 29, 1, 2, 1), Bits().subtype(namedValues=NamedValues(("hcAlarmCreation", 0), ("hcAlarmNvStorage", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmCapabilities.setDescription("An indication of the high capacity alarm capabilities\nsupported by this agent.\n\nIf the 'hcAlarmCreation' BIT is set, then this agent allows\nNMS applications to create entries in the hcAlarmTable.\n\nIf the 'hcAlarmNvStorage' BIT is set, then this agent allows\nentries in the hcAlarmTable which will be recreated after a\nsystem restart, as controlled by the hcAlarmStorageType\nobject.")
hcAlarmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 2))
hcAlarmNotifPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 2, 0))
hcAlarmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3))
hcAlarmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3, 1))
hcAlarmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3, 2))

# Augmentions

# Notifications

hcRisingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 1)).setObjects(*(("HC-ALARM-MIB", "hcAlarmRisingEventIndex"), ("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ) )
if mibBuilder.loadTexts: hcRisingAlarm.setDescription("The SNMP notification that is generated when a high\ncapacity alarm entry crosses its rising threshold and\ngenerates an event that is configured for sending SNMP\ntraps.\n\nThe hcAlarmEntry object instances identified in the OBJECTS\n\n\n\nclause are from the entry that causes this notification to\nbe generated.")
hcFallingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 2)).setObjects(*(("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"), ) )
if mibBuilder.loadTexts: hcFallingAlarm.setDescription("The SNMP notification that is generated when a high\ncapacity alarm entry crosses its falling threshold and\ngenerates an event that is configured for sending SNMP\ntraps.\n\nThe hcAlarmEntry object instances identified in the OBJECTS\nclause are from the entry that causes this notification to\nbe generated.")

# Groups

hcAlarmControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 1)).setObjects(*(("HC-ALARM-MIB", "hcAlarmRisingEventIndex"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmOwner"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmStorageType"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmStartupAlarm"), ("HC-ALARM-MIB", "hcAlarmValueFailedAttempts"), ("HC-ALARM-MIB", "hcAlarmInterval"), ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmStatus"), ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"), ) )
if mibBuilder.loadTexts: hcAlarmControlGroup.setDescription("A collection of objects used to configure entries for high\ncapacity alarm threshold monitoring purposes.")
hcAlarmCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 2)).setObjects(*(("HC-ALARM-MIB", "hcAlarmCapabilities"), ) )
if mibBuilder.loadTexts: hcAlarmCapabilitiesGroup.setDescription("A collection of objects used to indicate an agent's high\ncapacity alarm threshold monitoring capabilities.")
hcAlarmNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 3)).setObjects(*(("HC-ALARM-MIB", "hcRisingAlarm"), ("HC-ALARM-MIB", "hcFallingAlarm"), ) )
if mibBuilder.loadTexts: hcAlarmNotificationsGroup.setDescription("A collection of notifications to deliver information\nrelated to a high capacity rising or falling threshold event\n\n\n\nto a management application.")

# Compliances

hcAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 29, 3, 1, 1)).setObjects(*(("HC-ALARM-MIB", "hcAlarmCapabilitiesGroup"), ("RMON-MIB", "rmonEventGroup"), ("HC-ALARM-MIB", "hcAlarmControlGroup"), ("HC-ALARM-MIB", "hcAlarmNotificationsGroup"), ) )
if mibBuilder.loadTexts: hcAlarmCompliance.setDescription("Describes the requirements for conformance to the High\nCapacity Alarm MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("HC-ALARM-MIB", PYSNMP_MODULE_ID=hcAlarmMIB)

# Types
mibBuilder.exportSymbols("HC-ALARM-MIB", HcValueStatus=HcValueStatus)

# Objects
mibBuilder.exportSymbols("HC-ALARM-MIB", hcAlarmMIB=hcAlarmMIB, hcAlarmObjects=hcAlarmObjects, hcAlarmControlObjects=hcAlarmControlObjects, hcAlarmTable=hcAlarmTable, hcAlarmEntry=hcAlarmEntry, hcAlarmIndex=hcAlarmIndex, hcAlarmInterval=hcAlarmInterval, hcAlarmVariable=hcAlarmVariable, hcAlarmSampleType=hcAlarmSampleType, hcAlarmAbsValue=hcAlarmAbsValue, hcAlarmValueStatus=hcAlarmValueStatus, hcAlarmStartupAlarm=hcAlarmStartupAlarm, hcAlarmRisingThreshAbsValueLo=hcAlarmRisingThreshAbsValueLo, hcAlarmRisingThreshAbsValueHi=hcAlarmRisingThreshAbsValueHi, hcAlarmRisingThresholdValStatus=hcAlarmRisingThresholdValStatus, hcAlarmFallingThreshAbsValueLo=hcAlarmFallingThreshAbsValueLo, hcAlarmFallingThreshAbsValueHi=hcAlarmFallingThreshAbsValueHi, hcAlarmFallingThresholdValStatus=hcAlarmFallingThresholdValStatus, hcAlarmRisingEventIndex=hcAlarmRisingEventIndex, hcAlarmFallingEventIndex=hcAlarmFallingEventIndex, hcAlarmValueFailedAttempts=hcAlarmValueFailedAttempts, hcAlarmOwner=hcAlarmOwner, hcAlarmStorageType=hcAlarmStorageType, hcAlarmStatus=hcAlarmStatus, hcAlarmCapabilitiesObjects=hcAlarmCapabilitiesObjects, hcAlarmCapabilities=hcAlarmCapabilities, hcAlarmNotifications=hcAlarmNotifications, hcAlarmNotifPrefix=hcAlarmNotifPrefix, hcAlarmConformance=hcAlarmConformance, hcAlarmCompliances=hcAlarmCompliances, hcAlarmGroups=hcAlarmGroups)

# Notifications
mibBuilder.exportSymbols("HC-ALARM-MIB", hcRisingAlarm=hcRisingAlarm, hcFallingAlarm=hcFallingAlarm)

# Groups
mibBuilder.exportSymbols("HC-ALARM-MIB", hcAlarmControlGroup=hcAlarmControlGroup, hcAlarmCapabilitiesGroup=hcAlarmCapabilitiesGroup, hcAlarmNotificationsGroup=hcAlarmNotificationsGroup)

# Compliances
mibBuilder.exportSymbols("HC-ALARM-MIB", hcAlarmCompliance=hcAlarmCompliance)
