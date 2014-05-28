# PySNMP SMI module. Autogenerated from smidump -f python RFC1065-SMI
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:58:08 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, Unsigned32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Unsigned32", "MibIdentifier", "TimeTicks")

# Types

class Counter(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)
    
class Gauge(Unsigned32):
    subtypeSpec = Unsigned32.subtypeSpec+ValueRangeConstraint(0,4294967295)
    
class IpAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec+ValueSizeConstraint(4,4)
    fixedLength = 4
    
class ObjectName(ObjectIdentifier):
    pass

class Opaque(OctetString):
    pass

class TimeTicks(Unsigned32):
    pass

class NetworkAddress(IpAddress):
    pass


# Objects

internet = MibIdentifier((1, 3, 6, 1))
directory = MibIdentifier((1, 3, 6, 1, 1))
mgmt = MibIdentifier((1, 3, 6, 1, 2))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("RFC1065-SMI", Counter=Counter, Gauge=Gauge, IpAddress=IpAddress, ObjectName=ObjectName, Opaque=Opaque, TimeTicks=TimeTicks, NetworkAddress=NetworkAddress)

# Objects
mibBuilder.exportSymbols("RFC1065-SMI", internet=internet, directory=directory, mgmt=mgmt, experimental=experimental, private=private, enterprises=enterprises)

