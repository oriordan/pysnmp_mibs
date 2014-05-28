# PySNMP SMI module. Autogenerated from smidump -f python IPS-AUTH-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:43 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( AddressFamilyNumbers, ) = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")
( AutonomousType, RowStatus, StorageType, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "RowStatus", "StorageType", "TextualConvention")

# Types

class IpsAuthAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(0,255)
    

# Objects

ipsAuthMibModule = ModuleIdentity((1, 3, 6, 1, 2, 1, 141)).setRevisions(("2006-05-22 00:00",))
if mibBuilder.loadTexts: ipsAuthMibModule.setOrganization("IETF IPS Working Group")
if mibBuilder.loadTexts: ipsAuthMibModule.setContactInfo("\nMark Bakke\nPostal: Cisco Systems, Inc\n7900 International Drive, Suite 400\nBloomington, MN\nUSA 55425\n\nE-mail: mbakke@cisco.com\n\nJames Muchow\nPostal: Qlogic Corp.\n6321 Bury Dr.\nEden Prairie, MN\nUSA 55346\n\nE-Mail: james.muchow@qlogic.com")
if mibBuilder.loadTexts: ipsAuthMibModule.setDescription("The IP Storage Authorization MIB module.\nCopyright (C) The Internet Society (2006).  This version of\nthis MIB module is part of RFC 4545;  see the RFC itself for\nfull legal notices.")
ipsAuthNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 0))
ipsAuthObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1))
ipsAuthDescriptors = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 1))
ipsAuthMethodTypes = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1))
if mibBuilder.loadTexts: ipsAuthMethodTypes.setDescription("Registration point for Authentication Method Types.")
ipsAuthMethodNone = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 1))
if mibBuilder.loadTexts: ipsAuthMethodNone.setDescription("The authoritative identifier when no authentication\nmethod is used.")
ipsAuthMethodSrp = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 2))
if mibBuilder.loadTexts: ipsAuthMethodSrp.setDescription("The authoritative identifier when the authentication\nmethod is SRP.")
ipsAuthMethodChap = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 3))
if mibBuilder.loadTexts: ipsAuthMethodChap.setDescription("The authoritative identifier when the authentication\nmethod is CHAP.")
ipsAuthMethodKerberos = ObjectIdentity((1, 3, 6, 1, 2, 1, 141, 1, 1, 1, 4))
if mibBuilder.loadTexts: ipsAuthMethodKerberos.setDescription("The authoritative identifier when the authentication\nmethod is Kerberos.")
ipsAuthInstance = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 2))
ipsAuthInstanceAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 2, 2))
if mibBuilder.loadTexts: ipsAuthInstanceAttributesTable.setDescription("A list of Authorization instances present on the system.")
ipsAuthInstanceAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1)).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"))
if mibBuilder.loadTexts: ipsAuthInstanceAttributesEntry.setDescription("An entry (row) containing management information\napplicable to a particular Authorization instance.")
ipsAuthInstIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ipsAuthInstIndex.setDescription("An arbitrary integer used to uniquely identify a\nparticular authorization instance.  This index value\nmust not be modified or reused by an agent unless\na reboot has occurred.  An agent should attempt to\nkeep this value persistent across reboots.")
ipsAuthInstDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1, 2), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipsAuthInstDescr.setDescription("A character string, determined by the implementation to\ndescribe the authorization instance.  When only a single\ninstance is present, this object may be set to the\nzero-length string; with multiple authorization\ninstances, it must be set to a unique value in an\nimplementation-dependent manner to describe the purpose\nof the respective instance.  If this is deployed in a\nmaster agent with more than one subagent implementing\nthis MIB module, the master agent is responsible for\nensuring that this object is unique across all\nsubagents.")
ipsAuthInstStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 2, 2, 1, 3), StorageType().clone('volatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipsAuthInstStorageType.setDescription("The storage type for all read-write objects within this\nrow.  Rows in this table are always created via an\nexternal process, and may have a storage type of readOnly\nor permanent.  Conceptual rows having the value 'permanent'\nneed not allow write access to any columnar objects in\nthe row.\n\nIf this object has the value 'volatile', modifications\nto read-write objects in this row are not persistent\nacross reboots.  If this object has the value\n'nonVolatile', modifications to objects in this row\nare persistent.\n\nAn implementation may choose to allow this object\nto be set to either 'nonVolatile' or 'volatile',\nallowing the management application to choose this\nbehavior.")
ipsAuthIdentity = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 3))
ipsAuthIdentAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 3, 1))
if mibBuilder.loadTexts: ipsAuthIdentAttributesTable.setDescription("A list of user identities, each belonging to a\nparticular ipsAuthInstance.")
ipsAuthIdentAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1)).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"))
if mibBuilder.loadTexts: ipsAuthIdentAttributesEntry.setDescription("An entry (row) containing management information\ndescribing a user identity within an authorization\ninstance on this node.")
ipsAuthIdentIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ipsAuthIdentIndex.setDescription("An arbitrary integer used to uniquely identify a\nparticular identity instance within an authorization\ninstance present on the node.  This index value\nmust not be modified or reused by an agent unless\na reboot has occurred.  An agent should attempt to\nkeep this value persistent across reboots.")
ipsAuthIdentDescription = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentDescription.setDescription("A character string describing this particular identity.")
ipsAuthIdentRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentRowStatus.setDescription("This field allows entries to be dynamically added and\nremoved from this table via SNMP.  When adding a row to\nthis table, all non-Index/RowStatus objects must be set.\nRows may be discarded using RowStatus.  The value of\nipsAuthIdentDescription may be set while\nipsAuthIdentRowStatus is 'active'.")
ipsAuthIdentStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 3, 1, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentStorageType.setDescription("The storage type for all read-create objects in this row.\nRows in this table that were created through an external\nprocess may have a storage type of readOnly or permanent.\nConceptual rows having the value 'permanent' need not\nallow write access to any columnar objects in the row.")
ipsAuthIdentityName = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 4))
ipsAuthIdentNameAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 4, 1))
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesTable.setDescription("A list of unique names that can be used to positively\nidentify a particular user identity.")
ipsAuthIdentNameAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1)).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentNameIndex"))
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesEntry.setDescription("An entry (row) containing management information\napplicable to a unique identity name, which can be used\nto identify a user identity within a particular\nauthorization instance.")
ipsAuthIdentNameIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ipsAuthIdentNameIndex.setDescription("An arbitrary integer used to uniquely identify a\nparticular identity name instance within an\nipsAuthIdentity within an authorization instance.\nThis index value must not be modified or reused by\nan agent unless a reboot has occurred.  An agent\nshould attempt to keep this value persistent across\nreboots.")
ipsAuthIdentName = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 2), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentName.setDescription("A character string that is the unique name of an\nidentity that may be used to identify this ipsAuthIdent\nentry.")
ipsAuthIdentNameRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentNameRowStatus.setDescription("This field allows entries to be dynamically added and\nremoved from this table via SNMP.  When adding a row to\nthis table, all non-Index/RowStatus objects must be set.\nRows may be discarded using RowStatus.  The value of\nipsAuthIdentName may be set when this value is 'active'.")
ipsAuthIdentNameStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 4, 1, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentNameStorageType.setDescription("The storage type for all read-create objects in this row.\nRows in this table that were created through an external\nprocess may have a storage type of readOnly or permanent.\nConceptual rows having the value 'permanent' need not\nallow write access to any columnar objects in the row.")
ipsAuthIdentityAddress = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 5))
ipsAuthIdentAddrAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 5, 1))
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesTable.setDescription("A list of address ranges that are allowed to serve\nas the endpoint addresses of a particular identity.\nAn address range includes a starting and ending address\nand an optional netmask, and an address type indicator,\nwhich can specify whether the address is IPv4, IPv6,\nFC-WWPN, or FC-WWNN.")
ipsAuthIdentAddrAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1)).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentAddrIndex"))
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesEntry.setDescription("An entry (row) containing management information\napplicable to an address range that is used as part\nof the authorization of an identity\nwithin an authorization instance on this node.")
ipsAuthIdentAddrIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ipsAuthIdentAddrIndex.setDescription("An arbitrary integer used to uniquely identify a\nparticular ipsAuthIdentAddress instance within an\nipsAuthIdentity within an authorization instance\npresent on the node.\nThis index value must not be modified or reused by\nan agent unless a reboot has occurred.  An agent\nshould attempt to keep this value persistent across\nreboots.")
ipsAuthIdentAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 2), AddressFamilyNumbers()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrType.setDescription("The address types used in the ipsAuthIdentAddrStart\nand ipsAuthAddrEnd objects.  This type is taken\nfrom the IANA address family types.")
ipsAuthIdentAddrStart = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 3), IpsAuthAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrStart.setDescription("The starting address of the allowed address range.\nThe format of this object is determined by\nipsAuthIdentAddrType.")
ipsAuthIdentAddrEnd = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 4), IpsAuthAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrEnd.setDescription("The ending address of the allowed address range.\nIf the ipsAuthIdentAddrEntry specifies a single\naddress, this shall match the ipsAuthIdentAddrStart.\nThe format of this object is determined by\nipsAuthIdentAddrType.")
ipsAuthIdentAddrRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrRowStatus.setDescription("This field allows entries to be dynamically added and\nremoved from this table via SNMP.  When adding a row to\nthis table, all non-Index/RowStatus objects must be set.\nRows may be discarded using RowStatus.  The values of\nipsAuthIdentAddrStart and ipsAuthIdentAddrEnd may be set\nwhen this value is 'active'.  The value of\nipsAuthIdentAddrType may not be set when this value is\n'active'.")
ipsAuthIdentAddrStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 5, 1, 1, 6), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthIdentAddrStorageType.setDescription("The storage type for all read-create objects in this row.\nRows in this table that were created through an external\nprocess may have a storage type of readOnly or permanent.\nConceptual rows having the value 'permanent' need not\nallow write access to any columnar objects in the row.")
ipsAuthCredential = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 6))
ipsAuthCredentialAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 6, 1))
if mibBuilder.loadTexts: ipsAuthCredentialAttributesTable.setDescription("A list of credentials related to user identities\nthat are allowed as valid authenticators of the\nparticular identity.")
ipsAuthCredentialAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1)).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredentialAttributesEntry.setDescription("An entry (row) containing management information\napplicable to a credential that verifies a user\nidentity within an authorization instance.\n\n\n\nTo provide complete information in this MIB for a credential,\nthe management station must not only create the row in this\ntable but must also create a row in another table, where the\nother table is determined by the value of\nipsAuthCredAuthMethod, e.g., if ipsAuthCredAuthMethod has the\nvalue ipsAuthMethodChap, a row must be created in the\nipsAuthCredChapAttributesTable.")
ipsAuthCredIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: ipsAuthCredIndex.setDescription("An arbitrary integer used to uniquely identify a\nparticular Credential instance within an instance\npresent on the node.\nThis index value must not be modified or reused by\nan agent unless a reboot has occurred.  An agent\nshould attempt to keep this value persistent across\nreboots.")
ipsAuthCredAuthMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 2), AutonomousType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredAuthMethod.setDescription("This object contains an OBJECT IDENTIFIER\nthat identifies the authentication method\nused with this credential.\n\nWhen a row is created in this table, a corresponding\nrow must be created by the management station\nin a corresponding table specified by this value.\n\nWhen a row is deleted from this table, the corresponding\nrow must be automatically deleted by the agent in\nthe corresponding table specified by this value.\n\n\n\n\nIf the value of this object is ipsAuthMethodNone, no\ncorresponding rows are created or deleted from other\ntables.\n\nSome standardized values for this object are defined\nwithin the ipsAuthMethodTypes subtree.")
ipsAuthCredRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredRowStatus.setDescription("This field allows entries to be dynamically added and\nremoved from this table via SNMP.  When adding a row to\nthis table, all non-Index/RowStatus objects must be set.\nRows may be discarded using RowStatus.  The value of\nipsAuthCredAuthMethod must not be changed while this row\nis 'active'.")
ipsAuthCredStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 6, 1, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredStorageType.setDescription("The storage type for all read-create objects in this row.\nRows in this table that were created through an external\nprocess may have a storage type of readOnly or permanent.\nConceptual rows having the value 'permanent' need not\nallow write access to any columnar objects in the row.")
ipsAuthCredChap = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 7))
ipsAuthCredChapAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 7, 1))
if mibBuilder.loadTexts: ipsAuthCredChapAttributesTable.setDescription("A list of CHAP attributes for credentials that\nuse ipsAuthMethodChap as their ipsAuthCredAuthMethod.\n\nA row in this table can only exist when an instance of\nthe ipsAuthCredAuthMethod object exists (or is created\n\n\n\nsimultaneously) having the same instance identifiers\nand a value of 'ipsAuthMethodChap'.")
ipsAuthCredChapAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1)).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredChapAttributesEntry.setDescription("An entry (row) containing management information\napplicable to a credential that uses\nipsAuthMethodChap as their ipsAuthCredAuthMethod.\n\nWhen a row is created in ipsAuthCredentialAttributesTable\nwith ipsAuthCredAuthMethod = ipsAuthCredChap, the\nmanagement station must create a corresponding row\nin this table.\n\nWhen a row is deleted from ipsAuthCredentialAttributesTable\nwith ipsAuthCredAuthMethod = ipsAuthCredChap, the\nagent must delete the corresponding row (if any) in\nthis table.")
ipsAuthCredChapUserName = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredChapUserName.setDescription("A character string containing the CHAP user name for this\ncredential.")
ipsAuthCredChapRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredChapRowStatus.setDescription("This field allows entries to be dynamically added and\nremoved from this table via SNMP.  When adding a row to\nthis table, all non-Index/RowStatus objects must be set.\nRows may be discarded using RowStatus.  The value of\nipsAuthCredChapUserName may be changed while this row\nis 'active'.")
ipsAuthCredChapStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 7, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredChapStorageType.setDescription("The storage type for all read-create objects in this row.\nRows in this table that were created through an external\nprocess may have a storage type of readOnly or permanent.\nConceptual rows having the value 'permanent' need not\nallow write access to any columnar objects in the row.")
ipsAuthCredSrp = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 8))
ipsAuthCredSrpAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 8, 1))
if mibBuilder.loadTexts: ipsAuthCredSrpAttributesTable.setDescription("A list of SRP attributes for credentials that\nuse ipsAuthMethodSrp as its ipsAuthCredAuthMethod.\n\nA row in this table can only exist when an instance of\nthe ipsAuthCredAuthMethod object exists (or is created\nsimultaneously) having the same instance identifiers\nand a value of 'ipsAuthMethodSrp'.")
ipsAuthCredSrpAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1)).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredSrpAttributesEntry.setDescription("An entry (row) containing management information\napplicable to a credential that uses\nipsAuthMethodSrp as their ipsAuthCredAuthMethod.\n\n\n\n\nWhen a row is created in ipsAuthCredentialAttributesTable\nwith ipsAuthCredAuthMethod = ipsAuthCredSrp, the\nmanagement station must create a corresponding row\nin this table.\n\nWhen a row is deleted from ipsAuthCredentialAttributesTable\nwith ipsAuthCredAuthMethod = ipsAuthCredSrp, the\nagent must delete the corresponding row (if any) in\nthis table.")
ipsAuthCredSrpUserName = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredSrpUserName.setDescription("A character string containing the SRP user name for this\ncredential.")
ipsAuthCredSrpRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredSrpRowStatus.setDescription("This field allows entries to be dynamically added and\nremoved from this table via SNMP.  When adding a row to\nthis table, all non-Index/RowStatus objects must be set.\nRows may be discarded using RowStatus.  The value of\nipsAuthCredSrpUserName may be changed while the status\nof this row is 'active'.")
ipsAuthCredSrpStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 8, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredSrpStorageType.setDescription("The storage type for all read-create objects in this row.\nRows in this table that were created through an external\nprocess may have a storage type of readOnly or permanent.\nConceptual rows having the value 'permanent' need not\nallow write access to any columnar objects in the row.")
ipsAuthCredKerberos = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 1, 9))
ipsAuthCredKerbAttributesTable = MibTable((1, 3, 6, 1, 2, 1, 141, 1, 9, 1))
if mibBuilder.loadTexts: ipsAuthCredKerbAttributesTable.setDescription("A list of Kerberos attributes for credentials that\nuse ipsAuthMethodKerberos as their ipsAuthCredAuthMethod.\n\nA row in this table can only exist when an instance of\nthe ipsAuthCredAuthMethod object exists (or is created\nsimultaneously) having the same instance identifiers\nand a value of 'ipsAuthMethodKerb'.")
ipsAuthCredKerbAttributesEntry = MibTableRow((1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1)).setIndexNames((0, "IPS-AUTH-MIB", "ipsAuthInstIndex"), (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"), (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"))
if mibBuilder.loadTexts: ipsAuthCredKerbAttributesEntry.setDescription("An entry (row) containing management information\napplicable to a credential that uses\nipsAuthMethodKerberos as its ipsAuthCredAuthMethod.\n\nWhen a row is created in ipsAuthCredentialAttributesTable\nwith ipsAuthCredAuthMethod = ipsAuthCredKerberos, the\nmanagement station must create a corresponding row\nin this table.\n\nWhen a row is deleted from ipsAuthCredentialAttributesTable\nwith ipsAuthCredAuthMethod = ipsAuthCredKerberos, the\nagent must delete the corresponding row (if any) in\nthis table.")
ipsAuthCredKerbPrincipal = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1, 1), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredKerbPrincipal.setDescription("A character string containing a Kerberos principal\nfor this credential.")
ipsAuthCredKerbRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredKerbRowStatus.setDescription("This field allows entries to be dynamically added and\nremoved from this table via SNMP.  When adding a row to\nthis table, all non-Index/RowStatus objects must be set.\nRows may be discarded using RowStatus.  The value of\nipsAuthCredKerbPrincipal may be changed while this row\nis 'active'.")
ipsAuthCredKerbStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 141, 1, 9, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipsAuthCredKerbStorageType.setDescription("The storage type for all read-create objects in this row.\nRows in this table that were created through an external\nprocess may have a storage type of readOnly or permanent.\nConceptual rows having the value 'permanent' need not\nallow write access to any columnar objects in the row.")
ipsAuthConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 2))
ipsAuthCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 2, 1))
ipsAuthGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 141, 2, 2))

# Augmentions

# Groups

ipsAuthInstanceAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 1)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthInstStorageType"), ("IPS-AUTH-MIB", "ipsAuthInstDescr"), ) )
if mibBuilder.loadTexts: ipsAuthInstanceAttributesGroup.setDescription("A collection of objects providing information about\nauthorization instances.")
ipsAuthIdentAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 2)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthIdentRowStatus"), ("IPS-AUTH-MIB", "ipsAuthIdentStorageType"), ("IPS-AUTH-MIB", "ipsAuthIdentDescription"), ) )
if mibBuilder.loadTexts: ipsAuthIdentAttributesGroup.setDescription("A collection of objects providing information about\nuser identities within an authorization instance.")
ipsAuthIdentNameAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 3)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthIdentNameStorageType"), ("IPS-AUTH-MIB", "ipsAuthIdentNameRowStatus"), ("IPS-AUTH-MIB", "ipsAuthIdentName"), ) )
if mibBuilder.loadTexts: ipsAuthIdentNameAttributesGroup.setDescription("A collection of objects providing information about\nuser names within user identities within an authorization\ninstance.")
ipsAuthIdentAddrAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 4)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthIdentAddrStart"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrStorageType"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrType"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrEnd"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrRowStatus"), ) )
if mibBuilder.loadTexts: ipsAuthIdentAddrAttributesGroup.setDescription("A collection of objects providing information about\naddress ranges within user identities within an\nauthorization instance.")
ipsAuthIdentCredAttributesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 5)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthCredAuthMethod"), ("IPS-AUTH-MIB", "ipsAuthCredStorageType"), ("IPS-AUTH-MIB", "ipsAuthCredRowStatus"), ) )
if mibBuilder.loadTexts: ipsAuthIdentCredAttributesGroup.setDescription("A collection of objects providing information about\ncredentials within user identities within an authorization\ninstance.")
ipsAuthIdentChapAttrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 6)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthCredChapUserName"), ("IPS-AUTH-MIB", "ipsAuthCredChapStorageType"), ("IPS-AUTH-MIB", "ipsAuthCredChapRowStatus"), ) )
if mibBuilder.loadTexts: ipsAuthIdentChapAttrGroup.setDescription("A collection of objects providing information about\nCHAP credentials within user identities within an\nauthorization instance.")
ipsAuthIdentSrpAttrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 7)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthCredSrpRowStatus"), ("IPS-AUTH-MIB", "ipsAuthCredSrpUserName"), ("IPS-AUTH-MIB", "ipsAuthCredSrpStorageType"), ) )
if mibBuilder.loadTexts: ipsAuthIdentSrpAttrGroup.setDescription("A collection of objects providing information about\nSRP credentials within user identities within an\nauthorization instance.")
ipsAuthIdentKerberosAttrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 141, 2, 2, 8)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthCredKerbPrincipal"), ("IPS-AUTH-MIB", "ipsAuthCredKerbStorageType"), ("IPS-AUTH-MIB", "ipsAuthCredKerbRowStatus"), ) )
if mibBuilder.loadTexts: ipsAuthIdentKerberosAttrGroup.setDescription("A collection of objects providing information about\nKerberos credentials within user identities within an\nauthorization instance.")

# Compliances

ipsAuthComplianceV1 = ModuleCompliance((1, 3, 6, 1, 2, 1, 141, 2, 1, 1)).setObjects(*(("IPS-AUTH-MIB", "ipsAuthInstanceAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentNameAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentChapAttrGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentKerberosAttrGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentCredAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentAddrAttributesGroup"), ("IPS-AUTH-MIB", "ipsAuthIdentSrpAttrGroup"), ) )
if mibBuilder.loadTexts: ipsAuthComplianceV1.setDescription("Initial version of compliance statement based on\ninitial version of this MIB module.\n\nThe Instance and Identity groups are mandatory;\nat least one of the other groups (Name, Address,\nCredential, Certificate) is also mandatory for\nany given implementation.")

# Exports

# Module identity
mibBuilder.exportSymbols("IPS-AUTH-MIB", PYSNMP_MODULE_ID=ipsAuthMibModule)

# Types
mibBuilder.exportSymbols("IPS-AUTH-MIB", IpsAuthAddress=IpsAuthAddress)

# Objects
mibBuilder.exportSymbols("IPS-AUTH-MIB", ipsAuthMibModule=ipsAuthMibModule, ipsAuthNotifications=ipsAuthNotifications, ipsAuthObjects=ipsAuthObjects, ipsAuthDescriptors=ipsAuthDescriptors, ipsAuthMethodTypes=ipsAuthMethodTypes, ipsAuthMethodNone=ipsAuthMethodNone, ipsAuthMethodSrp=ipsAuthMethodSrp, ipsAuthMethodChap=ipsAuthMethodChap, ipsAuthMethodKerberos=ipsAuthMethodKerberos, ipsAuthInstance=ipsAuthInstance, ipsAuthInstanceAttributesTable=ipsAuthInstanceAttributesTable, ipsAuthInstanceAttributesEntry=ipsAuthInstanceAttributesEntry, ipsAuthInstIndex=ipsAuthInstIndex, ipsAuthInstDescr=ipsAuthInstDescr, ipsAuthInstStorageType=ipsAuthInstStorageType, ipsAuthIdentity=ipsAuthIdentity, ipsAuthIdentAttributesTable=ipsAuthIdentAttributesTable, ipsAuthIdentAttributesEntry=ipsAuthIdentAttributesEntry, ipsAuthIdentIndex=ipsAuthIdentIndex, ipsAuthIdentDescription=ipsAuthIdentDescription, ipsAuthIdentRowStatus=ipsAuthIdentRowStatus, ipsAuthIdentStorageType=ipsAuthIdentStorageType, ipsAuthIdentityName=ipsAuthIdentityName, ipsAuthIdentNameAttributesTable=ipsAuthIdentNameAttributesTable, ipsAuthIdentNameAttributesEntry=ipsAuthIdentNameAttributesEntry, ipsAuthIdentNameIndex=ipsAuthIdentNameIndex, ipsAuthIdentName=ipsAuthIdentName, ipsAuthIdentNameRowStatus=ipsAuthIdentNameRowStatus, ipsAuthIdentNameStorageType=ipsAuthIdentNameStorageType, ipsAuthIdentityAddress=ipsAuthIdentityAddress, ipsAuthIdentAddrAttributesTable=ipsAuthIdentAddrAttributesTable, ipsAuthIdentAddrAttributesEntry=ipsAuthIdentAddrAttributesEntry, ipsAuthIdentAddrIndex=ipsAuthIdentAddrIndex, ipsAuthIdentAddrType=ipsAuthIdentAddrType, ipsAuthIdentAddrStart=ipsAuthIdentAddrStart, ipsAuthIdentAddrEnd=ipsAuthIdentAddrEnd, ipsAuthIdentAddrRowStatus=ipsAuthIdentAddrRowStatus, ipsAuthIdentAddrStorageType=ipsAuthIdentAddrStorageType, ipsAuthCredential=ipsAuthCredential, ipsAuthCredentialAttributesTable=ipsAuthCredentialAttributesTable, ipsAuthCredentialAttributesEntry=ipsAuthCredentialAttributesEntry, ipsAuthCredIndex=ipsAuthCredIndex, ipsAuthCredAuthMethod=ipsAuthCredAuthMethod, ipsAuthCredRowStatus=ipsAuthCredRowStatus, ipsAuthCredStorageType=ipsAuthCredStorageType, ipsAuthCredChap=ipsAuthCredChap, ipsAuthCredChapAttributesTable=ipsAuthCredChapAttributesTable, ipsAuthCredChapAttributesEntry=ipsAuthCredChapAttributesEntry, ipsAuthCredChapUserName=ipsAuthCredChapUserName, ipsAuthCredChapRowStatus=ipsAuthCredChapRowStatus, ipsAuthCredChapStorageType=ipsAuthCredChapStorageType, ipsAuthCredSrp=ipsAuthCredSrp, ipsAuthCredSrpAttributesTable=ipsAuthCredSrpAttributesTable, ipsAuthCredSrpAttributesEntry=ipsAuthCredSrpAttributesEntry, ipsAuthCredSrpUserName=ipsAuthCredSrpUserName, ipsAuthCredSrpRowStatus=ipsAuthCredSrpRowStatus, ipsAuthCredSrpStorageType=ipsAuthCredSrpStorageType, ipsAuthCredKerberos=ipsAuthCredKerberos, ipsAuthCredKerbAttributesTable=ipsAuthCredKerbAttributesTable, ipsAuthCredKerbAttributesEntry=ipsAuthCredKerbAttributesEntry, ipsAuthCredKerbPrincipal=ipsAuthCredKerbPrincipal, ipsAuthCredKerbRowStatus=ipsAuthCredKerbRowStatus, ipsAuthCredKerbStorageType=ipsAuthCredKerbStorageType, ipsAuthConformance=ipsAuthConformance, ipsAuthCompliances=ipsAuthCompliances, ipsAuthGroups=ipsAuthGroups)

# Groups
mibBuilder.exportSymbols("IPS-AUTH-MIB", ipsAuthInstanceAttributesGroup=ipsAuthInstanceAttributesGroup, ipsAuthIdentAttributesGroup=ipsAuthIdentAttributesGroup, ipsAuthIdentNameAttributesGroup=ipsAuthIdentNameAttributesGroup, ipsAuthIdentAddrAttributesGroup=ipsAuthIdentAddrAttributesGroup, ipsAuthIdentCredAttributesGroup=ipsAuthIdentCredAttributesGroup, ipsAuthIdentChapAttrGroup=ipsAuthIdentChapAttrGroup, ipsAuthIdentSrpAttrGroup=ipsAuthIdentSrpAttrGroup, ipsAuthIdentKerberosAttrGroup=ipsAuthIdentKerberosAttrGroup)

# Compliances
mibBuilder.exportSymbols("IPS-AUTH-MIB", ipsAuthComplianceV1=ipsAuthComplianceV1)
