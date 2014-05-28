# PySNMP SMI module. Autogenerated from smidump -f python SIP-TC-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:11 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class SipTCEntityRole(Bits):
    namedValues = NamedValues(("other", 0), ("userAgent", 1), ("proxyServer", 2), ("redirectServer", 3), ("registrarServer", 4), )
    
class SipTCMethodName(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(1,100)
    
class SipTCOptionTagHeaders(Bits):
    namedValues = NamedValues(("require", 0), ("proxyRequire", 1), ("supported", 2), ("unsupported", 3), )
    
class SipTCTransportProtocol(Bits):
    namedValues = NamedValues(("other", 0), ("udp", 1), ("tcp", 2), ("sctp", 3), ("tlsTcp", 4), ("tlsSctp", 5), )
    

# Objects

sipTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 148)).setRevisions(("2007-04-20 00:00",))
if mibBuilder.loadTexts: sipTC.setOrganization("IETF Session Initiation Protocol Working Group")
if mibBuilder.loadTexts: sipTC.setContactInfo("SIP WG email: sip@ietf.org\n\nCo-editor  Kevin Lingle\n           Cisco Systems, Inc.\npostal:    7025 Kit Creek Road\n           P.O. Box 14987\n           Research Triangle Park, NC 27709\n           USA\nemail:     klingle@cisco.com\nphone:     +1 919 476 2029\n\nCo-editor  Joon Maeng\nemail:     jmaeng@austin.rr.com\n\nCo-editor  Jean-Francois Mule\n           CableLabs\npostal:    858 Coal Creek Circle\n           Louisville, CO 80027\n           USA\nemail:     jf.mule@cablelabs.com\nphone:     +1 303 661 9100\n\nCo-editor  Dave Walker\nemail:     drwalker@rogers.com")
if mibBuilder.loadTexts: sipTC.setDescription("Session Initiation Protocol (SIP) MIB TEXTUAL-CONVENTION\nmodule used by other SIP-related MIB Modules.\n\nCopyright (C) The IETF Trust (2007).  This version of\nthis MIB module is part of RFC 4780; see the RFC itself for\n\n\n\nfull legal notices.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("SIP-TC-MIB", PYSNMP_MODULE_ID=sipTC)

# Types
mibBuilder.exportSymbols("SIP-TC-MIB", SipTCEntityRole=SipTCEntityRole, SipTCMethodName=SipTCMethodName, SipTCOptionTagHeaders=SipTCOptionTagHeaders, SipTCTransportProtocol=SipTCTransportProtocol)

# Objects
mibBuilder.exportSymbols("SIP-TC-MIB", sipTC=sipTC)

