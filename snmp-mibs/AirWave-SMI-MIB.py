# PySNMP SMI module. Autogenerated from smidump -f python AirWave-SMI-MIB
# by libsmi2pysnmp-0.1.3 at Tue Jun  3 12:38:29 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks", "enterprises")

# Objects

airwave = ModuleIdentity((1, 3, 6, 1, 4, 1, 12028)).setRevisions(("2004-01-07 00:00","2002-01-03 00:00",))
if mibBuilder.loadTexts: airwave.setOrganization("AirWave Wireless")
if mibBuilder.loadTexts: airwave.setContactInfo("        Paul Gray\n\nPostal: Aruba Networks, Inc.\n        1344 Crossman Ave\n        Sunnyvale, CA 94402\n        \n   Tel: +1 408 227 4500\n   \n Email: paul@arubanetworks.com\n   Web: http://www.arubanetworks.com/")
if mibBuilder.loadTexts: airwave.setDescription("The MIB module for AirWave products.")
airwaveProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 12028, 1))
if mibBuilder.loadTexts: airwaveProducts.setDescription("AirWave products. See AirWave-Products-MIB.")
airwaveModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 12028, 2))
if mibBuilder.loadTexts: airwaveModules.setDescription("AirWave MIB modules.")
airwaveDev = ObjectIdentity((1, 3, 6, 1, 4, 1, 12028, 3))
if mibBuilder.loadTexts: airwaveDev.setDescription("AirWave internal MIB for products under development.")
awamp = ObjectIdentity((1, 3, 6, 1, 4, 1, 12028, 4))
if mibBuilder.loadTexts: awamp.setDescription("AirWave Management Platform MIB for NMS integration.\nSee AWAMP-MIB.")
airwaveSimulator = MibIdentifier((1, 3, 6, 1, 4, 1, 12028, 5))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("AirWave-SMI-MIB", PYSNMP_MODULE_ID=airwave)

# Objects
mibBuilder.exportSymbols("AirWave-SMI-MIB", airwave=airwave, airwaveProducts=airwaveProducts, airwaveModules=airwaveModules, airwaveDev=airwaveDev, awamp=awamp, airwaveSimulator=airwaveSimulator)

