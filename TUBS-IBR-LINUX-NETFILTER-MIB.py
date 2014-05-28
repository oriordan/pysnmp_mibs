# PySNMP SMI module. Autogenerated from smidump -f python TUBS-IBR-LINUX-NETFILTER-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:17 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressPrefixLength, InetAddressType, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressPrefixLength", "InetAddressType")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Counter64, Integer32, ModuleIdentity, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowStatus, StorageType, TextualConvention, TimeStamp, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "TextualConvention", "TimeStamp", "TruthValue")
( ibr, ) = mibBuilder.importSymbols("TUBS-SMI", "ibr")

# Types

class LnfTarget(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(5,1,2,6,7,3,4,)
    namedValues = NamedValues(("none", 1), ("other", 2), ("drop", 3), ("accept", 4), ("queue", 5), ("return", 6), ("chain", 7), )
    

# Objects

lnfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 13)).setRevisions(("2002-07-26 00:00","2002-07-23 00:00",))
if mibBuilder.loadTexts: lnfMIB.setOrganization("TU Braunschweig")
if mibBuilder.loadTexts: lnfMIB.setContactInfo("Frank Strauss, Oliver Wellnitz\nTU Braunschweig\nMuehlenpfordtstrasse 23\n38106 Braunschweig\nGermany\n\nTel: +49 531 391 3283\nFax: +49 531 391 5936\nE-mail: {strauss,wellnitz}@ibr.cs.tu-bs.de")
if mibBuilder.loadTexts: lnfMIB.setDescription("Experimental MIB module for the Linux 2.4 netfilter\nsubsystem.")
lnfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1))
lnfLastChange = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lnfLastChange.setDescription("The time of the last netfilter configuration change of any kind,\nincluding any creation, deletion or modification of any table of this\nMIB.")
lnfTableTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2))
if mibBuilder.loadTexts: lnfTableTable.setDescription("A list of all tables installed on the netfilter subsystem.")
lnfTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2, 1)).setIndexNames((0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableAddressType"), (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableName"))
if mibBuilder.loadTexts: lnfTableEntry.setDescription("An entry describing a particular netfilter table.")
lnfTableAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(2,1,)).subtype(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2), ))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: lnfTableAddressType.setDescription("The address type for which the netfilter table works.")
lnfTableName = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: lnfTableName.setDescription("The name of the netfilter table.")
lnfTableLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lnfTableLastChange.setDescription("The time of the last modification of this netfilter\ntable, including the creation or deletion of a netfilter\nchain that belongs to this table.")
lnfChainTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3))
if mibBuilder.loadTexts: lnfChainTable.setDescription("A list of all chains installed on the netfilter\nsubsystem.")
lnfChainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1)).setIndexNames((0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableAddressType"), (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableName"), (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainName"))
if mibBuilder.loadTexts: lnfChainEntry.setDescription("An entry describing a particular netfilter chain.")
lnfChainName = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: lnfChainName.setDescription("The netfilter chain to which the rule belongs.")
lnfChainPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lnfChainPackets.setDescription("The number of packets that passed this chain since\nthe rule was installed or reset.")
lnfChainOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lnfChainOctets.setDescription("The number of octets that passed this chain since \nthe chain was installed or reset.")
lnfChainTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 4), Integer().subtype(subtypeSpec=SingleValueConstraint(3,6,4,)).subtype(namedValues=NamedValues(("drop", 3), ("accept", 4), ("return", 6), )).clone(6)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfChainTarget.setDescription("The action that shall be applied to a packet if no rule\nwithin the chain matches. Note that user-defined chains\nonly allow return(6).")
lnfChainLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lnfChainLastChange.setDescription("The time of the last modification of this netfilter\nchain, including the creation or deletion of a netfilter\nrule that belongs to this chain.")
lnfChainStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfChainStorage.setDescription("This object defines whether this row is kept in\nvolatile storage and lost upon reboot or whether it\nis backed up by stable storage or builtin.")
lnfChainStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfChainStatus.setDescription("This object is used to create and delete rows in the\nlnfChainTable.")
lnfRuleTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4))
if mibBuilder.loadTexts: lnfRuleTable.setDescription("A list of all rules installed on the netfilter\nsubsystem.")
lnfRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1)).setIndexNames((0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableAddressType"), (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableName"), (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainName"), (0, "TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleIndex"))
if mibBuilder.loadTexts: lnfRuleEntry.setDescription("An entry describing a particular netfilter rule. Rules\nof different netfilter tables and chains are\ndistinguished by the corresponding index objects.")
lnfRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 1), Unsigned32()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: lnfRuleIndex.setDescription("A unique number identifying the rule within a netfilter\nchain.")
lnfRuleProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleProtocol.setDescription("The protocol of the rule. The number zero matches all\nprotocols.")
lnfRuleProtocolInv = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleProtocolInv.setDescription("This flag specifies whether the lnfRuleProtocol test\nhas to be inverted.")
lnfRuleSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleSourceAddress.setDescription("The source address of a packet. The exact format depends\non the address type specified by lnfRuleAddressType.\nThis test is applied for an address prefix whose length\nis specified by lnfRuleSourceAddressPrefixLength.\n\nIf a new row is created this object should default to\nan all-zeros value with a length approrpiate for the\ncorresponding lnfRuleAddressType object value.")
lnfRuleSourceAddressPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 5), InetAddressPrefixLength().clone('0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleSourceAddressPrefixLength.setDescription("The network prefix length associated with\nlnfRuleSourceAddress.")
lnfRuleSourceAddressInv = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleSourceAddressInv.setDescription("This flag specifies whether the lnfRuleSourceAddress\nand lnfRuleSourceAddressPrefixLength test has to\nbe inverted.")
lnfRuleDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleDestinationAddress.setDescription("The destination address of a packet. The exact format\ndepends on the address type specified by \nlnfRuleAddressType. This test is applied for an address\nprefix whose length is specified by \nlnfRuleDestinationAddressPrefixLength.\n\nIf a new row is created this object should default to\nan all-zeros value with a length approrpiate for the\ncorresponding lnfRuleAddressType object value.")
lnfRuleDestinationAddressPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 8), InetAddressPrefixLength().clone('0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleDestinationAddressPrefixLength.setDescription("The network prefix length associated with\nlnfRuleDestinationAddress.")
lnfRuleDestinationAddressInv = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleDestinationAddressInv.setDescription("This flag specifies whether the lnfRuleDestinationAddress\nand lnfRuleDestinationAddressPrefixLength test has to\nbe inverted.")
lnfRuleInInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleInInterface.setDescription("Name of an interface via which a packet is going to be\nreceived (only for packets entering the INPUT, FORWARD and\nPREROUTING chains).  If the interface name ends in a '+',\nthen any interface which begins with this name will match.\nIf this is an empty string, any interface name will match.")
lnfRuleInInterfaceInv = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleInInterfaceInv.setDescription("This flag specifies whether the lnfRuleInInterface test\nhas to be inverted.")
lnfRuleOutInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 12), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone('')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleOutInterface.setDescription("Name of an interface via which a packet is going to be\nsent (for packets entering the FORWARD, OUTPUT and\nPOSTROUTING chains).  If the interface name ends in a '+',\nthen any interface which begins with this name will match.\nIf this is an empty string, any interface name will match.")
lnfRuleOutInterfaceInv = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 13), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleOutInterfaceInv.setDescription("This flag specifies whether the lnfRuleOutInterface test\nhas to be inverted.")
lnfRuleFragment = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleFragment.setDescription("If this flag is true, the rule only refers to second and\nfurther fragments of fragmented packets.  Since there is\nno way to tell the source or destination ports of such a\npacket (or ICMP type), such a packet will not match any\nrules which specify them.")
lnfRuleFragmentInv = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleFragmentInv.setDescription("This flag specifies whether the lnfRuleFragmentInv test,\nif true, has to be inverted. An inverted rule will only\nmatch head fragments, or unfragmented packets.")
lnfRulePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lnfRulePackets.setDescription("The number of packets that matched this rule since\nthe rule was installed or reset.")
lnfRuleOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lnfRuleOctets.setDescription("The number of octets that matched this rule since the \nrule was installed or reset.")
lnfRuleTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 18), LnfTarget().clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleTarget.setDescription("The action that shall be applied to a packet if the\nrule matches. If the value is chain(7), then jump to\nthe user chain specified by lnfRuleTargetChain.")
lnfRuleTargetChain = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 19), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleTargetChain.setDescription("The name of the target chain if the value of\nlnfRuleTarget is chain(7).")
lnfRuleTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 20), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleTrapEnable.setDescription("Indicates whether lnfRuleMatch traps should be\ngenerated for packets matching this rule. Note\nthat it's up to the implementation to delay and\naccumulate mutliple traps in order to reduce the\nnumber of emitted traps.")
lnfRuleLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 21), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lnfRuleLastChange.setDescription("The time of the last modification of this netfilter rule.\nIf it has been unchanged since the last re-initialization\nof the local network management subsystem, then this\nobject contains a zero value.")
lnfRuleStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 22), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleStorage.setDescription("This object defines whether this row is kept in\nvolatile storage and lost upon reboot or whether it\nis backed up by stable storage or builtin.")
lnfRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 13, 1, 4, 1, 23), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: lnfRuleStatus.setDescription("This object is used to create and delete rows in the\nlnfRuleTable.")
lnfTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 13, 2))
lnfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 13, 2, 0))
lnfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 13, 3))
lnfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 1))
lnfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 2))

# Augmentions

# Notifications

lnfRuleMatch = NotificationType((1, 3, 6, 1, 4, 1, 1575, 1, 13, 2, 0, 1)).setObjects(*(("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleOctets"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRulePackets"), ) )
if mibBuilder.loadTexts: lnfRuleMatch.setDescription("A lnfRuleMatch trap signifies that the rule to which\nthe lnfRulePackets and lnfRuleOctets objects belong\nwas matched by at least one packets since the last\ntrap for the same rule was emitted.\n\nThe agent may delay and accumulate mutliple traps in order\nto reduce the number of emitted traps, but the time for\naccumulation should be no more than 60 seconds.\n\nNote that detailed information on the packet(s) that\ntriggered a trap is not available from the trap's \nobjects. This would cause problems with the accumulation\nof matches and/or increased trap traffic.")

# Groups

lnfGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 2, 1)).setObjects(*(("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainStorage"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleDestinationAddressPrefixLength"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainOctets"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleFragmentInv"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfLastChange"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainPackets"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleStatus"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleOutInterface"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleOctets"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleOutInterfaceInv"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleDestinationAddressInv"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainLastChange"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleSourceAddressPrefixLength"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainTarget"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleLastChange"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleProtocolInv"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleSourceAddress"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleTrapEnable"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleDestinationAddress"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleTargetChain"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleSourceAddressInv"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleTarget"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRulePackets"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleProtocol"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfTableLastChange"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleInInterfaceInv"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleFragment"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleInInterface"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleStorage"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfChainStatus"), ) )
if mibBuilder.loadTexts: lnfGeneralGroup.setDescription("A collection of all Linux Netfilter objects of\nthe core table.")
lnfNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 2, 2)).setObjects(*(("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfRuleMatch"), ) )
if mibBuilder.loadTexts: lnfNotificationGroup.setDescription("A collection of all Linux Netfilter notifications.")

# Compliances

lnfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1575, 1, 13, 3, 1, 1)).setObjects(*(("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfNotificationGroup"), ("TUBS-IBR-LINUX-NETFILTER-MIB", "lnfGeneralGroup"), ) )
if mibBuilder.loadTexts: lnfCompliance.setDescription("The compliance statement for an SNMP entity which\nimplements the Linux Netfilter MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("TUBS-IBR-LINUX-NETFILTER-MIB", PYSNMP_MODULE_ID=lnfMIB)

# Types
mibBuilder.exportSymbols("TUBS-IBR-LINUX-NETFILTER-MIB", LnfTarget=LnfTarget)

# Objects
mibBuilder.exportSymbols("TUBS-IBR-LINUX-NETFILTER-MIB", lnfMIB=lnfMIB, lnfObjects=lnfObjects, lnfLastChange=lnfLastChange, lnfTableTable=lnfTableTable, lnfTableEntry=lnfTableEntry, lnfTableAddressType=lnfTableAddressType, lnfTableName=lnfTableName, lnfTableLastChange=lnfTableLastChange, lnfChainTable=lnfChainTable, lnfChainEntry=lnfChainEntry, lnfChainName=lnfChainName, lnfChainPackets=lnfChainPackets, lnfChainOctets=lnfChainOctets, lnfChainTarget=lnfChainTarget, lnfChainLastChange=lnfChainLastChange, lnfChainStorage=lnfChainStorage, lnfChainStatus=lnfChainStatus, lnfRuleTable=lnfRuleTable, lnfRuleEntry=lnfRuleEntry, lnfRuleIndex=lnfRuleIndex, lnfRuleProtocol=lnfRuleProtocol, lnfRuleProtocolInv=lnfRuleProtocolInv, lnfRuleSourceAddress=lnfRuleSourceAddress, lnfRuleSourceAddressPrefixLength=lnfRuleSourceAddressPrefixLength, lnfRuleSourceAddressInv=lnfRuleSourceAddressInv, lnfRuleDestinationAddress=lnfRuleDestinationAddress, lnfRuleDestinationAddressPrefixLength=lnfRuleDestinationAddressPrefixLength, lnfRuleDestinationAddressInv=lnfRuleDestinationAddressInv, lnfRuleInInterface=lnfRuleInInterface, lnfRuleInInterfaceInv=lnfRuleInInterfaceInv, lnfRuleOutInterface=lnfRuleOutInterface, lnfRuleOutInterfaceInv=lnfRuleOutInterfaceInv, lnfRuleFragment=lnfRuleFragment, lnfRuleFragmentInv=lnfRuleFragmentInv, lnfRulePackets=lnfRulePackets, lnfRuleOctets=lnfRuleOctets, lnfRuleTarget=lnfRuleTarget, lnfRuleTargetChain=lnfRuleTargetChain, lnfRuleTrapEnable=lnfRuleTrapEnable, lnfRuleLastChange=lnfRuleLastChange, lnfRuleStorage=lnfRuleStorage, lnfRuleStatus=lnfRuleStatus, lnfTraps=lnfTraps, lnfNotifications=lnfNotifications, lnfConformance=lnfConformance, lnfCompliances=lnfCompliances, lnfGroups=lnfGroups)

# Notifications
mibBuilder.exportSymbols("TUBS-IBR-LINUX-NETFILTER-MIB", lnfRuleMatch=lnfRuleMatch)

# Groups
mibBuilder.exportSymbols("TUBS-IBR-LINUX-NETFILTER-MIB", lnfGeneralGroup=lnfGeneralGroup, lnfNotificationGroup=lnfNotificationGroup)

# Compliances
mibBuilder.exportSymbols("TUBS-IBR-LINUX-NETFILTER-MIB", lnfCompliance=lnfCompliance)
