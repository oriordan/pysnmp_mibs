# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-EVENT-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:49 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxEventNotifications, jnxMibs, ) = mibBuilder.importSymbols("JUNIPER-SMI", "jnxEventNotifications", "jnxMibs")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

jnxEvent = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 37)).setRevisions(("2006-08-16 21:53",))
if mibBuilder.loadTexts: jnxEvent.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxEvent.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\nE-mail: support@juniper.net")
if mibBuilder.loadTexts: jnxEvent.setDescription("This is Juniper Networks implementation of enterprise\nspecific MIB for generic event notifications.")
jnxEventNotifyVars = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1))
if mibBuilder.loadTexts: jnxEventNotifyVars.setDescription("Notification object definitions.")
jnxEventTrapDescr = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 1), DisplayString()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxEventTrapDescr.setDescription("Description of the trap generated by op-script \nor event-policies.")
jnxEventAvTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2))
if mibBuilder.loadTexts: jnxEventAvTable.setDescription("A table of attribute value pairs for the trap \ngenerated by the op-scripts or event-policies.")
jnxEventAvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1)).setIndexNames((0, "JUNIPER-EVENT-MIB", "jnxEventAvIndex"))
if mibBuilder.loadTexts: jnxEventAvEntry.setDescription("An entry of attribute value pair.")
jnxEventAvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxEventAvIndex.setDescription("Identifies the sequence number of attribute-value\npair in the trap generated by  op-scripts or \nevent-policies.")
jnxEventAvAttribute = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1, 2), DisplayString()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxEventAvAttribute.setDescription("Attribute name in the trap generated by op-script \nor event-policies.")
jnxEventAvValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 37, 1, 2, 1, 3), DisplayString()).setMaxAccess("notifyonly")
if mibBuilder.loadTexts: jnxEventAvValue.setDescription("Value of the attribute identified by jnxEventAvAttribute.")
jnxEventNotificationPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 4, 13, 0))
if mibBuilder.loadTexts: jnxEventNotificationPrefix.setDescription("All Event notifications are registered under \nthis branch.")

# Augmentions

# Notifications

jnxEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 2636, 4, 13, 0, 1)).setObjects(*(("JUNIPER-EVENT-MIB", "jnxEventTrapDescr"), ) )
if mibBuilder.loadTexts: jnxEventTrap.setDescription("Notification generated by op-script or event-policies. Apart \nfrom the jnxEventTrap objects, this notification can include \n one or more attribute-value pairs. The attribute-value pairs \n shall be identified by objects jnxEventAvAttribute and \n jnxEventAvValue.")

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-EVENT-MIB", PYSNMP_MODULE_ID=jnxEvent)

# Objects
mibBuilder.exportSymbols("JUNIPER-EVENT-MIB", jnxEvent=jnxEvent, jnxEventNotifyVars=jnxEventNotifyVars, jnxEventTrapDescr=jnxEventTrapDescr, jnxEventAvTable=jnxEventAvTable, jnxEventAvEntry=jnxEventAvEntry, jnxEventAvIndex=jnxEventAvIndex, jnxEventAvAttribute=jnxEventAvAttribute, jnxEventAvValue=jnxEventAvValue, jnxEventNotificationPrefix=jnxEventNotificationPrefix)

# Notifications
mibBuilder.exportSymbols("JUNIPER-EVENT-MIB", jnxEventTrap=jnxEventTrap)

