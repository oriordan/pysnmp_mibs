# PySNMP SMI module. Autogenerated from smidump -f python JUNIPER-LSYSSP-POLICY-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:52 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( jnxLsysSpPolicy, ) = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpPolicy")
( Bits, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

jnxLsysSpPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1)).setRevisions(("2010-05-19 16:44",))
if mibBuilder.loadTexts: jnxLsysSpPolicyMIB.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: jnxLsysSpPolicyMIB.setContactInfo("Juniper Technical Assistance Center\nJuniper Networks, Inc.\n1194 N. Mathilda Avenue\nSunnyvale, CA 94089\n\nE-mail: support@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: jnxLsysSpPolicyMIB.setDescription("This module defines the policy-specific MIB for Juniper Enterprise \nLogical-System (LSYS) security profiles.  Juniper documentation \nis recommended as the reference. \n\nThe LSYS security profile provides various static and dynamic \nresource management by observing resource quota limits. \nSecurity policy resource is the focus in this MIB. ")
jnxLsysSpPolicyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1))
jnxLsysSpPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1))
if mibBuilder.loadTexts: jnxLsysSpPolicyTable.setDescription("LSYSPROFILE policy objects for policy resource consumption per LSYS.")
jnxLsysSpPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1)).setIndexNames((1, "JUNIPER-LSYSSP-POLICY-MIB", "jnxLsysSpPolicyLsysName"))
if mibBuilder.loadTexts: jnxLsysSpPolicyEntry.setDescription("An entry in policy resource table.")
jnxLsysSpPolicyLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: jnxLsysSpPolicyLsysName.setDescription("The name of the logical system for which policy resource information is retrieved. ")
jnxLsysSpPolicyProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyProfileName.setDescription("The security profile name string for the LSYS.")
jnxLsysSpPolicyUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyUsage.setDescription("The current resource usage count for the LSYS.")
jnxLsysSpPolicyReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyReserved.setDescription("The reserved resource count for the LSYS.")
jnxLsysSpPolicyMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyMaximum.setDescription("The maximum allowed resource usage count for the LSYS.")
jnxLsysSpPolicySummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2))
jnxLsysSpPolicyUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyUsedAmount.setDescription("The policy resource consumption over all LSYS.")
jnxLsysSpPolicyMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyMaxQuota.setDescription("The policy resource maximum quota for the whole device for all LSYS.")
jnxLsysSpPolicyAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyAvailableAmount.setDescription("The policy resource available in the whole device.")
jnxLsysSpPolicyHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyHeaviestUsage.setDescription("The most amount of policy resource consumed of a LSYS.")
jnxLsysSpPolicyHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyHeaviestUser.setDescription("The LSYS name that consume the most policy resource.")
jnxLsysSpPolicyLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyLightestUsage.setDescription("The least amount of policy resource consumed of a LSYS.")
jnxLsysSpPolicyLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 3, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpPolicyLightestUser.setDescription("The LSYS name that consume the least policy resource.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("JUNIPER-LSYSSP-POLICY-MIB", PYSNMP_MODULE_ID=jnxLsysSpPolicyMIB)

# Objects
mibBuilder.exportSymbols("JUNIPER-LSYSSP-POLICY-MIB", jnxLsysSpPolicyMIB=jnxLsysSpPolicyMIB, jnxLsysSpPolicyObjects=jnxLsysSpPolicyObjects, jnxLsysSpPolicyTable=jnxLsysSpPolicyTable, jnxLsysSpPolicyEntry=jnxLsysSpPolicyEntry, jnxLsysSpPolicyLsysName=jnxLsysSpPolicyLsysName, jnxLsysSpPolicyProfileName=jnxLsysSpPolicyProfileName, jnxLsysSpPolicyUsage=jnxLsysSpPolicyUsage, jnxLsysSpPolicyReserved=jnxLsysSpPolicyReserved, jnxLsysSpPolicyMaximum=jnxLsysSpPolicyMaximum, jnxLsysSpPolicySummary=jnxLsysSpPolicySummary, jnxLsysSpPolicyUsedAmount=jnxLsysSpPolicyUsedAmount, jnxLsysSpPolicyMaxQuota=jnxLsysSpPolicyMaxQuota, jnxLsysSpPolicyAvailableAmount=jnxLsysSpPolicyAvailableAmount, jnxLsysSpPolicyHeaviestUsage=jnxLsysSpPolicyHeaviestUsage, jnxLsysSpPolicyHeaviestUser=jnxLsysSpPolicyHeaviestUser, jnxLsysSpPolicyLightestUsage=jnxLsysSpPolicyLightestUsage, jnxLsysSpPolicyLightestUser=jnxLsysSpPolicyLightestUser)

