# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-LSYSSP-NATSRCRULE-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:52 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxLsysSpNATsrcrule, ) = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpNATsrcrule")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

jnxLsysSpNATsrcruleMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1)).setRevisions(("2010-05-19 16:44",))
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMIB.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\n\nE-mail: support@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMIB.setDescription("This module defines the NAT-source-rule-specific MIB for \nJuniper Enterprise Logical-System (LSYS) security profiles.  \nJuniper documentation is recommended as the reference. \n\nThe LSYS security profile provides various static and dynamic \nresource management by observing resource quota limits. \nSecurity NAT-source-rule resource is the focus in this MIB. ")
jnxLsysSpNATsrcruleObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1))
jnxLsysSpNATsrcruleTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1))
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleTable.setDescription("LSYSPROFILE NAT-source-rule objects for NAT-source-rule \nresource consumption per LSYS.")
jnxLsysSpNATsrcruleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1)).setIndexNames((1, "JUNIPER-LSYSSP-NATSRCRULE-MIB", "jnxLsysSpNATsrcruleLsysName"))
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleEntry.setDescription("An entry in NAT-source-rule resource table.")
jnxLsysSpNATsrcruleLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleLsysName.setDescription("The name of the logical system for which NAT-source-rule \nresource information is retrieved. ")
jnxLsysSpNATsrcruleProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleProfileName.setDescription("The security profile name string for the LSYS.")
jnxLsysSpNATsrcruleUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleUsage.setDescription("The current resource usage count for the LSYS.")
jnxLsysSpNATsrcruleReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleReserved.setDescription("The reserved resource count for the LSYS.")
jnxLsysSpNATsrcruleMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMaximum.setDescription("The maximum allowed resource usage count for the LSYS.")
jnxLsysSpNATsrcruleSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2))
jnxLsysSpNATsrcruleUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleUsedAmount.setDescription("The NAT-source-rule resource consumption over all LSYS.")
jnxLsysSpNATsrcruleMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleMaxQuota.setDescription("The NAT-source-rule resource maximum quota for the whole \ndevice for all LSYS.")
jnxLsysSpNATsrcruleAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleAvailableAmount.setDescription("The NAT-source-rule resource available in the whole device.")
jnxLsysSpNATsrcruleHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleHeaviestUsage.setDescription("The most amount of NAT-source-rule resource consumed of a \nLSYS.")
jnxLsysSpNATsrcruleHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleHeaviestUser.setDescription("The LSYS name that consume the most NAT-source-rule resource.")
jnxLsysSpNATsrcruleLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleLightestUsage.setDescription("The least amount of NAT-source-rule resource consumed of a \nLSYS.")
jnxLsysSpNATsrcruleLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 12, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcruleLightestUser.setDescription("The LSYS name that consume the least NAT-source-rule resource.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATSRCRULE-MIB", PYSNMP_MODULE_ID=jnxLsysSpNATsrcruleMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATSRCRULE-MIB", jnxLsysSpNATsrcruleMIB=jnxLsysSpNATsrcruleMIB, jnxLsysSpNATsrcruleObjects=jnxLsysSpNATsrcruleObjects, jnxLsysSpNATsrcruleTable=jnxLsysSpNATsrcruleTable, jnxLsysSpNATsrcruleEntry=jnxLsysSpNATsrcruleEntry, jnxLsysSpNATsrcruleLsysName=jnxLsysSpNATsrcruleLsysName, jnxLsysSpNATsrcruleProfileName=jnxLsysSpNATsrcruleProfileName, jnxLsysSpNATsrcruleUsage=jnxLsysSpNATsrcruleUsage, jnxLsysSpNATsrcruleReserved=jnxLsysSpNATsrcruleReserved, jnxLsysSpNATsrcruleMaximum=jnxLsysSpNATsrcruleMaximum, jnxLsysSpNATsrcruleSummary=jnxLsysSpNATsrcruleSummary, jnxLsysSpNATsrcruleUsedAmount=jnxLsysSpNATsrcruleUsedAmount, jnxLsysSpNATsrcruleMaxQuota=jnxLsysSpNATsrcruleMaxQuota, jnxLsysSpNATsrcruleAvailableAmount=jnxLsysSpNATsrcruleAvailableAmount, jnxLsysSpNATsrcruleHeaviestUsage=jnxLsysSpNATsrcruleHeaviestUsage, jnxLsysSpNATsrcruleHeaviestUser=jnxLsysSpNATsrcruleHeaviestUser, jnxLsysSpNATsrcruleLightestUsage=jnxLsysSpNATsrcruleLightestUsage, jnxLsysSpNATsrcruleLightestUser=jnxLsysSpNATsrcruleLightestUser)

