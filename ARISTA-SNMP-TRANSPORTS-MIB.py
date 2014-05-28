# PySNMP SMI module. Autogenerated from smidump -f python ARISTA-SNMP-TRANSPORTS-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:33 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( aristaMibs, ) = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( TAddress, TDomain, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "TDomain", "TextualConvention")

# Types

class TransportAddressIPv4NS(TextualConvention, OctetString):
    displayHint = "1d.1d.1d.1d:2d@*1t"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(7,255)
    
class TransportAddressIPv6NS(TextualConvention, OctetString):
    displayHint = "0a[2x:2x:2x:2x:2x:2x:2x:2x]0a:2d@*1t"
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(19,255)
    

# Objects

aristaSnmpTransportMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10)).setRevisions(("2012-01-09 13:00","2012-01-05 18:30",))
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setOrganization("Arista Networks, Inc.")
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setContactInfo("Arista Networks, Inc.\n\nPostal: 5470 Great America Parkway\n        Santa Clara, CA 95054\n\nTel: +1 408 547-5500\n\nE-mail: snmp@aristanetworks.com")
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setDescription("The Arista Networks specific SNMP transport domains.")
aristaUDPNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 1))
if mibBuilder.loadTexts: aristaUDPNSDomain.setDescription("The SNMP over UDP transport domain.  The corresponding socket is\nopened in a specific namespace.")
aristaTCPNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 2))
if mibBuilder.loadTexts: aristaTCPNSDomain.setDescription("The SNMP over TCP transport domain.  The corresponding socket is\nopened in a specific namespace.")
aristaUDPNS6Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 3))
if mibBuilder.loadTexts: aristaUDPNS6Domain.setDescription("The SNMP over UDP6 transport domain. The corresponding socket is\nopened in a specific namespace.")
aristaTCPNS6Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 4))
if mibBuilder.loadTexts: aristaTCPNS6Domain.setDescription("The SNMP over TCP6 transport domain. The corresponding socket is\nopened in a specific namespace.")
aristaAuthFailTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5))
aristaAuthFailTrapTDomain = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 1), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaAuthFailTrapTDomain.setDescription("Transport Domain of the offending request that caused this trap")
aristaAuthFailTrapSrcTAddress = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 2), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaAuthFailTrapSrcTAddress.setDescription("Source Transport Address of the offending request that caused \nthis trap")
aristaTransportConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6))
aristaAuthFailTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1))
aristaAuthFailCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2))

# Augmentions

# Groups

aristaAuthFailTrapObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1, 1)).setObjects(*(("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapSrcTAddress"), ("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapTDomain"), ) )
if mibBuilder.loadTexts: aristaAuthFailTrapObjectsGroup.setDescription("Collections of objects for Authentication Failure Trap.")

# Compliances

aristaAuthFailCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2, 1)).setObjects(*(("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapObjectsGroup"), ) )
if mibBuilder.loadTexts: aristaAuthFailCompliance.setDescription("The compliance statement for SNMP entities which implement\nthe ARISTA AuthFailure MIB.")

# Exports

# Module identity
mibBuilder.exportSymbols("ARISTA-SNMP-TRANSPORTS-MIB", PYSNMP_MODULE_ID=aristaSnmpTransportMIB)

# Types
mibBuilder.exportSymbols("ARISTA-SNMP-TRANSPORTS-MIB", TransportAddressIPv4NS=TransportAddressIPv4NS, TransportAddressIPv6NS=TransportAddressIPv6NS)

# Objects
mibBuilder.exportSymbols("ARISTA-SNMP-TRANSPORTS-MIB", aristaSnmpTransportMIB=aristaSnmpTransportMIB, aristaUDPNSDomain=aristaUDPNSDomain, aristaTCPNSDomain=aristaTCPNSDomain, aristaUDPNS6Domain=aristaUDPNS6Domain, aristaTCPNS6Domain=aristaTCPNS6Domain, aristaAuthFailTrapObjects=aristaAuthFailTrapObjects, aristaAuthFailTrapTDomain=aristaAuthFailTrapTDomain, aristaAuthFailTrapSrcTAddress=aristaAuthFailTrapSrcTAddress, aristaTransportConformance=aristaTransportConformance, aristaAuthFailTrapGroups=aristaAuthFailTrapGroups, aristaAuthFailCompliances=aristaAuthFailCompliances)

# Groups
mibBuilder.exportSymbols("ARISTA-SNMP-TRANSPORTS-MIB", aristaAuthFailTrapObjectsGroup=aristaAuthFailTrapObjectsGroup)

# Compliances
mibBuilder.exportSymbols("ARISTA-SNMP-TRANSPORTS-MIB", aristaAuthFailCompliance=aristaAuthFailCompliance)
