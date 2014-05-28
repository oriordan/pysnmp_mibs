# PySNMP SMI module. Autogenerated from smidump -f python SNMP-VIEW-BASED-ACM-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:14 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( SnmpAdminString, SnmpSecurityLevel, SnmpSecurityModel, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpSecurityLevel", "SnmpSecurityModel")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, snmpModules, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "snmpModules")
( RowStatus, StorageType, TestAndIncr, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TestAndIncr")

# Objects

snmpVacmMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 16)).setRevisions(("2002-10-16 00:00","1999-01-20 00:00","1997-11-20 00:00",))
if mibBuilder.loadTexts: snmpVacmMIB.setOrganization("SNMPv3 Working Group")
if mibBuilder.loadTexts: snmpVacmMIB.setContactInfo("WG-email:   snmpv3@lists.tislabs.com\nSubscribe:  majordomo@lists.tislabs.com\n            In message body:  subscribe snmpv3\n\nCo-Chair:   Russ Mundy\n            Network Associates Laboratories\npostal:     15204 Omega Drive, Suite 300\n            Rockville, MD 20850-4601\n            USA\nemail:      mundy@tislabs.com\nphone:      +1 301-947-7107\n\nCo-Chair:   David Harrington\n            Enterasys Networks\nPostal:     35 Industrial Way\n            P. O. Box 5004\n            Rochester, New Hampshire 03866-5005\n            USA\nEMail:      dbh@enterasys.com\nPhone:      +1 603-337-2614\n\nCo-editor:  Bert Wijnen\n            Lucent Technologies\npostal:     Schagen 33\n            3461 GL Linschoten\n            Netherlands\nemail:      bwijnen@lucent.com\nphone:      +31-348-480-685\n\nCo-editor:  Randy Presuhn\n            BMC Software, Inc.\n\npostal:     2141 North First Street\n            San Jose, CA 95131\n            USA\nemail:      randy_presuhn@bmc.com\nphone:      +1 408-546-1006\n\nCo-editor:  Keith McCloghrie\n            Cisco Systems, Inc.\npostal:     170 West Tasman Drive\n            San Jose, CA  95134-1706\n            USA\nemail:      kzm@cisco.com\nphone:      +1-408-526-5260")
if mibBuilder.loadTexts: snmpVacmMIB.setDescription("The management information definitions for the\nView-based Access Control Model for SNMP.\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3415;\nsee the RFC itself for full legal notices.")
vacmMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 1))
vacmContextTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 1))
if mibBuilder.loadTexts: vacmContextTable.setDescription("The table of locally available contexts.\n\nThis table provides information to SNMP Command\n\nGenerator applications so that they can properly\nconfigure the vacmAccessTable to control access to\nall contexts at the SNMP entity.\n\nThis table may change dynamically if the SNMP entity\nallows that contexts are added/deleted dynamically\n(for instance when its configuration changes).  Such\nchanges would happen only if the management\ninstrumentation at that SNMP entity recognizes more\n(or fewer) contexts.\n\nThe presence of entries in this table and of entries\nin the vacmAccessTable are independent.  That is, a\ncontext identified by an entry in this table is not\nnecessarily referenced by any entries in the\nvacmAccessTable; and the context(s) referenced by an\nentry in the vacmAccessTable does not necessarily\ncurrently exist and thus need not be identified by an\nentry in this table.\n\nThis table must be made accessible via the default\ncontext so that Command Responder applications have\na standard way of retrieving the information.\n\nThis table is read-only.  It cannot be configured via\nSNMP.")
vacmContextEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 1, 1)).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"))
if mibBuilder.loadTexts: vacmContextEntry.setDescription("Information about a particular context.")
vacmContextName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmContextName.setDescription("A human readable name identifying a particular\ncontext at a particular SNMP entity.\n\nThe empty contextName (zero length) represents the\ndefault context.")
vacmSecurityToGroupTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 2))
if mibBuilder.loadTexts: vacmSecurityToGroupTable.setDescription("This table maps a combination of securityModel and\nsecurityName into a groupName which is used to define\nan access control policy for a group of principals.")
vacmSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 2, 1)).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityName"))
if mibBuilder.loadTexts: vacmSecurityToGroupEntry.setDescription("An entry in this table maps the combination of a\nsecurityModel and securityName into a groupName.")
vacmSecurityModel = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 1), SnmpSecurityModel().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vacmSecurityModel.setDescription("The Security Model, by which the vacmSecurityName\nreferenced by this entry is provided.\n\nNote, this object may not take the 'any' (0) value.")
vacmSecurityName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vacmSecurityName.setDescription("The securityName for the principal, represented in a\nSecurity Model independent format, which is mapped by\nthis entry to a groupName.")
vacmGroupName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmGroupName.setDescription("The name of the group to which this entry (e.g., the\ncombination of securityModel and securityName)\nbelongs.\n\nThis groupName is used as index into the\nvacmAccessTable to select an access control policy.\nHowever, a value in this table does not imply that an\ninstance with the value exists in table vacmAccesTable.")
vacmSecurityToGroupStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmSecurityToGroupStorageType.setDescription("The storage type for this conceptual row.\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
vacmSecurityToGroupStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmSecurityToGroupStatus.setDescription("The status of this conceptual row.\n\nUntil instances of all corresponding columns are\nappropriately configured, the value of the\n\ncorresponding instance of the vacmSecurityToGroupStatus\ncolumn is 'notReady'.\n\nIn particular, a newly created row cannot be made\nactive until a value has been set for vacmGroupName.\n\nThe  RowStatus TC [RFC2579] requires that this\nDESCRIPTION clause states under which circumstances\nother objects in this row can be modified:\n\nThe value of this object has no effect on whether\nother objects in this conceptual row can be modified.")
vacmAccessTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 4))
if mibBuilder.loadTexts: vacmAccessTable.setDescription("The table of access rights for groups.\n\nEach entry is indexed by a groupName, a contextPrefix,\na securityModel and a securityLevel.  To determine\nwhether access is allowed, one entry from this table\nneeds to be selected and the proper viewName from that\nentry must be used for access control checking.\n\nTo select the proper entry, follow these steps:\n\n1) the set of possible matches is formed by the\n   intersection of the following sets of entries:\n\n     the set of entries with identical vacmGroupName\n     the union of these two sets:\n      - the set with identical vacmAccessContextPrefix\n      - the set of entries with vacmAccessContextMatch\n        value of 'prefix' and matching\n        vacmAccessContextPrefix\n     intersected with the union of these two sets:\n      - the set of entries with identical\n        vacmSecurityModel\n      - the set of entries with vacmSecurityModel\n        value of 'any'\n     intersected with the set of entries with\n     vacmAccessSecurityLevel value less than or equal\n     to the requested securityLevel\n\n2) if this set has only one member, we're done\n   otherwise, it comes down to deciding how to weight\n   the preferences between ContextPrefixes,\n   SecurityModels, and SecurityLevels as follows:\n   a) if the subset of entries with securityModel\n      matching the securityModel in the message is\n      not empty, then discard the rest.\n   b) if the subset of entries with\n      vacmAccessContextPrefix matching the contextName\n      in the message is not empty,\n      then discard the rest\n   c) discard all entries with ContextPrefixes shorter\n      than the longest one remaining in the set\n   d) select the entry with the highest securityLevel\n\nPlease note that for securityLevel noAuthNoPriv, all\ngroups are really equivalent since the assumption that\nthe securityName has been authenticated does not hold.")
vacmAccessEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 4, 1)).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextPrefix"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityLevel"))
if mibBuilder.loadTexts: vacmAccessEntry.setDescription("An access right configured in the Local Configuration\nDatastore (LCD) authorizing access to an SNMP context.\n\nEntries in this table can use an instance value for\nobject vacmGroupName even if no entry in table\nvacmAccessSecurityToGroupTable has a corresponding\nvalue for object vacmGroupName.")
vacmAccessContextPrefix = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vacmAccessContextPrefix.setDescription("In order to gain the access rights allowed by this\nconceptual row, a contextName must match exactly\n(if the value of vacmAccessContextMatch is 'exact')\nor partially (if the value of vacmAccessContextMatch\nis 'prefix') to the value of the instance of this\nobject.")
vacmAccessSecurityModel = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 2), SnmpSecurityModel()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vacmAccessSecurityModel.setDescription("In order to gain the access rights allowed by this\nconceptual row, this securityModel must be in use.")
vacmAccessSecurityLevel = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 3), SnmpSecurityLevel()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vacmAccessSecurityLevel.setDescription("The minimum level of security required in order to\ngain the access rights allowed by this conceptual\nrow.  A securityLevel of noAuthNoPriv is less than\nauthNoPriv which in turn is less than authPriv.\n\nIf multiple entries are equally indexed except for\nthis vacmAccessSecurityLevel index, then the entry\nwhich has the highest value for\nvacmAccessSecurityLevel is selected.")
vacmAccessContextMatch = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("exact", 1), ("prefix", 2), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessContextMatch.setDescription("If the value of this object is exact(1), then all\nrows where the contextName exactly matches\nvacmAccessContextPrefix are selected.\n\nIf the value of this object is prefix(2), then all\nrows where the contextName whose starting octets\nexactly match vacmAccessContextPrefix are selected.\nThis allows for a simple form of wildcarding.")
vacmAccessReadViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessReadViewName.setDescription("The value of an instance of this object identifies\nthe MIB view of the SNMP context to which this\nconceptual row authorizes read access.\n\nThe identified MIB view is that one for which the\nvacmViewTreeFamilyViewName has the same value as the\ninstance of this object; if the value is the empty\nstring or if there is no active MIB view having this\nvalue of vacmViewTreeFamilyViewName, then no access\nis granted.")
vacmAccessWriteViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessWriteViewName.setDescription("The value of an instance of this object identifies\nthe MIB view of the SNMP context to which this\nconceptual row authorizes write access.\n\nThe identified MIB view is that one for which the\nvacmViewTreeFamilyViewName has the same value as the\ninstance of this object; if the value is the empty\nstring or if there is no active MIB view having this\nvalue of vacmViewTreeFamilyViewName, then no access\nis granted.")
vacmAccessNotifyViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessNotifyViewName.setDescription("The value of an instance of this object identifies\nthe MIB view of the SNMP context to which this\nconceptual row authorizes access for notifications.\n\nThe identified MIB view is that one for which the\nvacmViewTreeFamilyViewName has the same value as the\ninstance of this object; if the value is the empty\nstring or if there is no active MIB view having this\nvalue of vacmViewTreeFamilyViewName, then no access\nis granted.")
vacmAccessStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessStorageType.setDescription("The storage type for this conceptual row.\n\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
vacmAccessStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessStatus.setDescription("The status of this conceptual row.\n\nThe  RowStatus TC [RFC2579] requires that this\nDESCRIPTION clause states under which circumstances\nother objects in this row can be modified:\n\nThe value of this object has no effect on whether\nother objects in this conceptual row can be modified.")
vacmMIBViews = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 1, 5))
vacmViewSpinLock = MibScalar((1, 3, 6, 1, 6, 3, 16, 1, 5, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmViewSpinLock.setDescription("An advisory lock used to allow cooperating SNMP\nCommand Generator applications to coordinate their\nuse of the Set operation in creating or modifying\nviews.\n\nWhen creating a new view or altering an existing\nview, it is important to understand the potential\ninteractions with other uses of the view.  The\nvacmViewSpinLock should be retrieved.  The name of\nthe view to be created should be determined to be\nunique by the SNMP Command Generator application by\nconsulting the vacmViewTreeFamilyTable.  Finally,\nthe named view may be created (Set), including the\nadvisory lock.\nIf another SNMP Command Generator application has\naltered the views in the meantime, then the spin\nlock's value will have changed, and so this creation\nwill fail because it will specify the wrong value for\nthe spin lock.\n\nSince this is an advisory lock, the use of this lock\nis not enforced.")
vacmViewTreeFamilyTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 5, 2))
if mibBuilder.loadTexts: vacmViewTreeFamilyTable.setDescription("Locally held information about families of subtrees\nwithin MIB views.\n\nEach MIB view is defined by two sets of view subtrees:\n  - the included view subtrees, and\n  - the excluded view subtrees.\nEvery such view subtree, both the included and the\n\nexcluded ones, is defined in this table.\n\nTo determine if a particular object instance is in\na particular MIB view, compare the object instance's\nOBJECT IDENTIFIER with each of the MIB view's active\nentries in this table.  If none match, then the\nobject instance is not in the MIB view.  If one or\nmore match, then the object instance is included in,\nor excluded from, the MIB view according to the\nvalue of vacmViewTreeFamilyType in the entry whose\nvalue of vacmViewTreeFamilySubtree has the most\nsub-identifiers.  If multiple entries match and have\nthe same number of sub-identifiers (when wildcarding\nis specified with the value of vacmViewTreeFamilyMask),\nthen the lexicographically greatest instance of\nvacmViewTreeFamilyType determines the inclusion or\nexclusion.\n\nAn object instance's OBJECT IDENTIFIER X matches an\nactive entry in this table when the number of\nsub-identifiers in X is at least as many as in the\nvalue of vacmViewTreeFamilySubtree for the entry,\nand each sub-identifier in the value of\nvacmViewTreeFamilySubtree matches its corresponding\nsub-identifier in X.  Two sub-identifiers match\neither if the corresponding bit of the value of\nvacmViewTreeFamilyMask for the entry is zero (the\n'wild card' value), or if they are equal.\n\nA 'family' of subtrees is the set of subtrees defined\nby a particular combination of values of\nvacmViewTreeFamilySubtree and vacmViewTreeFamilyMask.\n\nIn the case where no 'wild card' is defined in the\nvacmViewTreeFamilyMask, the family of subtrees reduces\nto a single subtree.\n\nWhen creating or changing MIB views, an SNMP Command\nGenerator application should utilize the\nvacmViewSpinLock to try to avoid collisions.  See\nDESCRIPTION clause of vacmViewSpinLock.\n\nWhen creating MIB views, it is strongly advised that\nfirst the 'excluded' vacmViewTreeFamilyEntries are\ncreated and then the 'included' entries.\n\nWhen deleting MIB views, it is strongly advised that\nfirst the 'included' vacmViewTreeFamilyEntries are\n\ndeleted and then the 'excluded' entries.\n\nIf a create for an entry for instance-level access\ncontrol is received and the implementation does not\nsupport instance-level granularity, then an\ninconsistentName error must be returned.")
vacmViewTreeFamilyEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1)).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyViewName"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilySubtree"))
if mibBuilder.loadTexts: vacmViewTreeFamilyEntry.setDescription("Information on a particular family of view subtrees\nincluded in or excluded from a particular SNMP\ncontext's MIB view.\n\nImplementations must not restrict the number of\nfamilies of view subtrees for a given MIB view,\nexcept as dictated by resource constraints on the\noverall number of entries in the\nvacmViewTreeFamilyTable.\n\nIf no conceptual rows exist in this table for a given\nMIB view (viewName), that view may be thought of as\nconsisting of the empty set of view subtrees.")
vacmViewTreeFamilyViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vacmViewTreeFamilyViewName.setDescription("The human readable name for a family of view subtrees.")
vacmViewTreeFamilySubtree = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 2), ObjectIdentifier()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: vacmViewTreeFamilySubtree.setDescription("The MIB subtree which when combined with the\ncorresponding instance of vacmViewTreeFamilyMask\ndefines a family of view subtrees.")
vacmViewTreeFamilyMask = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyMask.setDescription("The bit mask which, in combination with the\ncorresponding instance of vacmViewTreeFamilySubtree,\ndefines a family of view subtrees.\n\nEach bit of this bit mask corresponds to a\nsub-identifier of vacmViewTreeFamilySubtree, with the\nmost significant bit of the i-th octet of this octet\nstring value (extended if necessary, see below)\ncorresponding to the (8*i - 7)-th sub-identifier, and\nthe least significant bit of the i-th octet of this\noctet string corresponding to the (8*i)-th\nsub-identifier, where i is in the range 1 through 16.\n\nEach bit of this bit mask specifies whether or not\nthe corresponding sub-identifiers must match when\ndetermining if an OBJECT IDENTIFIER is in this\nfamily of view subtrees; a '1' indicates that an\nexact match must occur; a '0' indicates 'wild card',\ni.e., any sub-identifier value matches.\n\nThus, the OBJECT IDENTIFIER X of an object instance\nis contained in a family of view subtrees if, for\neach sub-identifier of the value of\nvacmViewTreeFamilySubtree, either:\n\n  the i-th bit of vacmViewTreeFamilyMask is 0, or\n\n  the i-th sub-identifier of X is equal to the i-th\n  sub-identifier of the value of\n  vacmViewTreeFamilySubtree.\n\nIf the value of this bit mask is M bits long and\n\nthere are more than M sub-identifiers in the\ncorresponding instance of vacmViewTreeFamilySubtree,\nthen the bit mask is extended with 1's to be the\nrequired length.\n\nNote that when the value of this object is the\nzero-length string, this extension rule results in\na mask of all-1's being used (i.e., no 'wild card'),\nand the family of view subtrees is the one view\nsubtree uniquely identified by the corresponding\ninstance of vacmViewTreeFamilySubtree.\n\nNote that masks of length greater than zero length\ndo not need to be supported.  In this case this\nobject is made read-only.")
vacmViewTreeFamilyType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(1,2,)).subtype(namedValues=NamedValues(("included", 1), ("excluded", 2), )).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyType.setDescription("Indicates whether the corresponding instances of\nvacmViewTreeFamilySubtree and vacmViewTreeFamilyMask\ndefine a family of view subtrees which is included in\nor excluded from the MIB view.")
vacmViewTreeFamilyStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyStorageType.setDescription("The storage type for this conceptual row.\n\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
vacmViewTreeFamilyStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyStatus.setDescription("The status of this conceptual row.\n\nThe  RowStatus TC [RFC2579] requires that this\nDESCRIPTION clause states under which circumstances\nother objects in this row can be modified:\n\nThe value of this object has no effect on whether\nother objects in this conceptual row can be modified.")
vacmMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 2))
vacmMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 2, 1))
vacmMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 2, 2))

# Augmentions

# Groups

vacmBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 16, 2, 2, 1)).setObjects(*(("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyStorageType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextMatch"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessReadViewName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityToGroupStatus"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessWriteViewName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessNotifyViewName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessStorageType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyStatus"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessStatus"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityToGroupStorageType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyMask"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewSpinLock"), ) )
if mibBuilder.loadTexts: vacmBasicGroup.setDescription("A collection of objects providing for remote\nconfiguration of an SNMP engine which implements\n\nthe SNMP View-based Access Control Model.")

# Compliances

vacmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 16, 2, 1, 1)).setObjects(*(("SNMP-VIEW-BASED-ACM-MIB", "vacmBasicGroup"), ) )
if mibBuilder.loadTexts: vacmMIBCompliance.setDescription("The compliance statement for SNMP engines which\nimplement the SNMP View-based Access Control Model\nconfiguration MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("SNMP-VIEW-BASED-ACM-MIB", PYSNMP_MODULE_ID=snmpVacmMIB)

# Objects
mibBuilder.exportSymbols("SNMP-VIEW-BASED-ACM-MIB", snmpVacmMIB=snmpVacmMIB, vacmMIBObjects=vacmMIBObjects, vacmContextTable=vacmContextTable, vacmContextEntry=vacmContextEntry, vacmContextName=vacmContextName, vacmSecurityToGroupTable=vacmSecurityToGroupTable, vacmSecurityToGroupEntry=vacmSecurityToGroupEntry, vacmSecurityModel=vacmSecurityModel, vacmSecurityName=vacmSecurityName, vacmGroupName=vacmGroupName, vacmSecurityToGroupStorageType=vacmSecurityToGroupStorageType, vacmSecurityToGroupStatus=vacmSecurityToGroupStatus, vacmAccessTable=vacmAccessTable, vacmAccessEntry=vacmAccessEntry, vacmAccessContextPrefix=vacmAccessContextPrefix, vacmAccessSecurityModel=vacmAccessSecurityModel, vacmAccessSecurityLevel=vacmAccessSecurityLevel, vacmAccessContextMatch=vacmAccessContextMatch, vacmAccessReadViewName=vacmAccessReadViewName, vacmAccessWriteViewName=vacmAccessWriteViewName, vacmAccessNotifyViewName=vacmAccessNotifyViewName, vacmAccessStorageType=vacmAccessStorageType, vacmAccessStatus=vacmAccessStatus, vacmMIBViews=vacmMIBViews, vacmViewSpinLock=vacmViewSpinLock, vacmViewTreeFamilyTable=vacmViewTreeFamilyTable, vacmViewTreeFamilyEntry=vacmViewTreeFamilyEntry, vacmViewTreeFamilyViewName=vacmViewTreeFamilyViewName, vacmViewTreeFamilySubtree=vacmViewTreeFamilySubtree, vacmViewTreeFamilyMask=vacmViewTreeFamilyMask, vacmViewTreeFamilyType=vacmViewTreeFamilyType, vacmViewTreeFamilyStorageType=vacmViewTreeFamilyStorageType, vacmViewTreeFamilyStatus=vacmViewTreeFamilyStatus, vacmMIBConformance=vacmMIBConformance, vacmMIBCompliances=vacmMIBCompliances, vacmMIBGroups=vacmMIBGroups)

# Groups
mibBuilder.exportSymbols("SNMP-VIEW-BASED-ACM-MIB", vacmBasicGroup=vacmBasicGroup)

# Compliances
mibBuilder.exportSymbols("SNMP-VIEW-BASED-ACM-MIB", vacmMIBCompliance=vacmMIBCompliance)
