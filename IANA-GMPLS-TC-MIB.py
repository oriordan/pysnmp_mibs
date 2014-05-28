# PySNMP SMI module. Autogenerated from smidump -f python IANA-GMPLS-TC-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:41 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class IANAGmplsAdminStatusInformationTC(Bits):
    namedValues = NamedValues(("reflect", 0), ("reserved1", 1), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved2", 2), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("testing", 29), ("reserved3", 3), ("administrativelyDown", 30), ("deleteInProgress", 31), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), )
    
class IANAGmplsGeneralizedPidTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(18,28,44,46,21,15,14,23,30,0,8,53,24,42,50,7,13,43,26,5,27,51,48,58,49,10,31,11,38,47,20,17,16,22,9,29,6,52,40,45,54,12,36,55,19,41,25,56,32,34,57,33,37,)
    namedValues = NamedValues(("unknown", 0), ("asynchDS2T2", 10), ("bitsynchDS2T2", 11), ("reservedByRFC3471first", 12), ("asynchE1", 13), ("bytesynchE1", 14), ("bytesynch31ByDS0", 15), ("asynchDS1T1", 16), ("bitsynchDS1T1", 17), ("bytesynchDS1T1", 18), ("vc1vc12", 19), ("reservedByRFC3471second", 20), ("reservedByRFC3471third", 21), ("ds1SFAsynch", 22), ("ds1ESFAsynch", 23), ("ds3M23Asynch", 24), ("ds3CBitParityAsynch", 25), ("vtLovc", 26), ("stsSpeHovc", 27), ("posNoScramble16BitCrc", 28), ("posNoScramble32BitCrc", 29), ("posScramble16BitCrc", 30), ("posScramble32BitCrc", 31), ("atm", 32), ("ethernet", 33), ("sdhSonet", 34), ("digitalwrapper", 36), ("lambda", 37), ("ansiEtsiPdh", 38), ("lapsSdh", 40), ("fddi", 41), ("dqdb", 42), ("fiberChannel3", 43), ("hdlc", 44), ("ethernetV2DixOnly", 45), ("ethernet802dot3Only", 46), ("g709ODUj", 47), ("g709OTUk", 48), ("g709CBRorCBRa", 49), ("asynchE4", 5), ("g709CBRb", 50), ("g709BSOT", 51), ("g709BSNT", 52), ("gfpIPorPPP", 53), ("gfpEthernetMAC", 54), ("gfpEthernetPHY", 55), ("g709ESCON", 56), ("g709FICON", 57), ("g709FiberChannel", 58), ("asynchDS3T3", 6), ("asynchE3", 7), ("bitsynchE3", 8), ("bytesynchE3", 9), )
    
class IANAGmplsLSPEncodingTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(9,13,3,11,5,2,1,8,7,12,0,)
    namedValues = NamedValues(("tunnelLspNotGmpls", 0), ("tunnelLspPacket", 1), ("tunnelLspFiberChannel", 11), ("tunnelDigitalPath", 12), ("tunnelOpticalChannel", 13), ("tunnelLspEthernet", 2), ("tunnelLspAnsiEtsiPdh", 3), ("tunnelLspSdhSonet", 5), ("tunnelLspDigitalWrapper", 7), ("tunnelLspLambda", 8), ("tunnelLspFiber", 9), )
    
class IANAGmplsSwitchingTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(150,100,51,200,2,0,1,4,3,)
    namedValues = NamedValues(("unknown", 0), ("psc1", 1), ("tdm", 100), ("lsc", 150), ("psc2", 2), ("fsc", 200), ("psc3", 3), ("psc4", 4), ("l2sc", 51), )
    

# Objects

ianaGmpls = ModuleIdentity((1, 3, 6, 1, 2, 1, 152)).setRevisions(("2007-02-27 00:00",))
if mibBuilder.loadTexts: ianaGmpls.setOrganization("IANA")
if mibBuilder.loadTexts: ianaGmpls.setContactInfo("Internet Assigned Numbers Authority\nPostal: 4676 Admiralty Way, Suite 330\n        Marina del Rey, CA 90292\nTel:    +1 310 823 9358\nE-Mail: iana&iana.org")
if mibBuilder.loadTexts: ianaGmpls.setDescription("Copyright (C) The IETF Trust (2007).  The initial version\nof this MIB module was published in RFC 4802.  For full legal\nnotices see the RFC itself.  Supplementary information\nmay be available on:\nhttp://www.ietf.org/copyrights/ianamib.html")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("IANA-GMPLS-TC-MIB", PYSNMP_MODULE_ID=ianaGmpls)

# Types
mibBuilder.exportSymbols("IANA-GMPLS-TC-MIB", IANAGmplsAdminStatusInformationTC=IANAGmplsAdminStatusInformationTC, IANAGmplsGeneralizedPidTC=IANAGmplsGeneralizedPidTC, IANAGmplsLSPEncodingTypeTC=IANAGmplsLSPEncodingTypeTC, IANAGmplsSwitchingTypeTC=IANAGmplsSwitchingTypeTC)

# Objects
mibBuilder.exportSymbols("IANA-GMPLS-TC-MIB", ianaGmpls=ianaGmpls)

