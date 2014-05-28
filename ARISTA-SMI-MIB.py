# PySNMP SMI module. Autogenerated from smidump -f python ARISTA-SMI-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:33 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "enterprises")

# Objects

arista = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065)).setRevisions(("2011-03-31 13:00","2008-10-27 18:30",))
if mibBuilder.loadTexts: arista.setOrganization("Arista Networks, Inc.")
if mibBuilder.loadTexts: arista.setContactInfo("Arista Networks, Inc.\n\nPostal: 5470 Great America Parkway\n        Santa Clara, CA 95054\n\nTel: +1 408 547-5500\n\nE-mail: snmp@aristanetworks.com")
if mibBuilder.loadTexts: arista.setDescription("The Structure of Management Information for the\nArista Networks enterprise.")
aristaProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 1))
if mibBuilder.loadTexts: aristaProducts.setDescription("aristaProducts is the root object identifier from\nwhich sysObjectID values are assigned.  Values are\ndefined in ARISTA-PRODUCTS-MIB.")
aristaModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 2))
if mibBuilder.loadTexts: aristaModules.setDescription("aristaModules provides a root object identifier\nfrom which MODULE-IDENTITY values may be assigned.")
aristaMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3))
if mibBuilder.loadTexts: aristaMibs.setDescription("aristaMibs provides a root object identifier\nfor management-related MIBs.")
aristaExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 4))
if mibBuilder.loadTexts: aristaExperiment.setDescription("aristaExperiment provides a root object identifier\nfor experimental MIBs.  The structure of information\nfor these MIBs can not be guaranteed between releases.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("ARISTA-SMI-MIB", PYSNMP_MODULE_ID=arista)

# Objects
mibBuilder.exportSymbols("ARISTA-SMI-MIB", arista=arista, aristaProducts=aristaProducts, aristaModules=aristaModules, aristaMibs=aristaMibs, aristaExperiment=aristaExperiment)

