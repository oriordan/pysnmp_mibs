# PySNMP SMI module. Autogenerated from smidump -f python ARISTA-MAU-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:32 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( aristaMibs, ) = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "TimeTicks")

# Objects

aristaSnmpDot3MauMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 4))
aristaDot3MauType = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1))
aristaDot3MauType10GbaseCR = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 1))
if mibBuilder.loadTexts: aristaDot3MauType10GbaseCR.setDescription("Passive copper cable")
aristaDot3MauType10GbaseDwdmER = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 2))
if mibBuilder.loadTexts: aristaDot3MauType10GbaseDwdmER.setDescription("Dense Wavelength Division Multiplexing ER")
aristaDot3MauType40GbaseSR4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 3))
if mibBuilder.loadTexts: aristaDot3MauType40GbaseSR4.setDescription("Fiber over short-wavelength laser")
aristaDot3MauType40GbaseLR4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 4))
if mibBuilder.loadTexts: aristaDot3MauType40GbaseLR4.setDescription("Fiber over long-wavelength laser")
aristaDot3MauType40GbaseCR4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 5))
if mibBuilder.loadTexts: aristaDot3MauType40GbaseCR4.setDescription("Passive copper cable")
aristaDot3MauType10GbaseDwdmZR = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 6))
if mibBuilder.loadTexts: aristaDot3MauType10GbaseDwdmZR.setDescription("Dense Wavelength Division Multiplexing ZR")
aristaDot3MauType10GbaseCRA = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 7))
if mibBuilder.loadTexts: aristaDot3MauType10GbaseCRA.setDescription("Active copper cable")
aristaDot3MauType10GbaseZR = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 8))
if mibBuilder.loadTexts: aristaDot3MauType10GbaseZR.setDescription("Very long reach fiber")
aristaDot3MauType10GbaseLRL = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 9))
if mibBuilder.loadTexts: aristaDot3MauType10GbaseLRL.setDescription("Short single mode fiber")
aristaDot3MauType100GbaseSR10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 10))
if mibBuilder.loadTexts: aristaDot3MauType100GbaseSR10.setDescription("Fiber over short range wavelength laser")
aristaDot3MauType100GbaseLR4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 11))
if mibBuilder.loadTexts: aristaDot3MauType100GbaseLR4.setDescription("Fiber over long reach wavelength laser")
aristaDot3MauType100GbaseER4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 12))
if mibBuilder.loadTexts: aristaDot3MauType100GbaseER4.setDescription("Fiber over extended reach wavelength laser")
aristaDot3MauType40GbaseXSR4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 13))
if mibBuilder.loadTexts: aristaDot3MauType40GbaseXSR4.setDescription("Enhanced Reach (300m) 40GBaseSR4")
aristaDot3MauType40GbaseAR4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 14))
if mibBuilder.loadTexts: aristaDot3MauType40GbaseAR4.setDescription("Active cable")
aristaDot3MauType40GbasePLR4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 15))
if mibBuilder.loadTexts: aristaDot3MauType40GbasePLR4.setDescription("Long reach parallel fiber over long-wavelength laser")
aristaDot3MauType40GbasePLRL4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 1, 16))
if mibBuilder.loadTexts: aristaDot3MauType40GbasePLRL4.setDescription("Parallel lite fiber over long-wavelength laser")
aristaMauMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 4, 2)).setRevisions(("2012-04-10 00:00","2011-02-25 00:00",))
if mibBuilder.loadTexts: aristaMauMIB.setOrganization("Arista Networks, Inc.")
if mibBuilder.loadTexts: aristaMauMIB.setContactInfo("Arista Networks, Inc.\n\nPostal: 5470 Great America Parkway\n        Santa Clara, CA 95054\n\nTel: +1 408 547-5500\n\nE-mail: snmp@aristanetworks.com")
if mibBuilder.loadTexts: aristaMauMIB.setDescription("This MIB module extends dot3MauType OBJECT-IDENTITIES\ndefined in the IANA-MAU-MIB, covering all MAU types\nused by Arista Networks.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("ARISTA-MAU-MIB", PYSNMP_MODULE_ID=aristaMauMIB)

# Objects
mibBuilder.exportSymbols("ARISTA-MAU-MIB", aristaSnmpDot3MauMgt=aristaSnmpDot3MauMgt, aristaDot3MauType=aristaDot3MauType, aristaDot3MauType10GbaseCR=aristaDot3MauType10GbaseCR, aristaDot3MauType10GbaseDwdmER=aristaDot3MauType10GbaseDwdmER, aristaDot3MauType40GbaseSR4=aristaDot3MauType40GbaseSR4, aristaDot3MauType40GbaseLR4=aristaDot3MauType40GbaseLR4, aristaDot3MauType40GbaseCR4=aristaDot3MauType40GbaseCR4, aristaDot3MauType10GbaseDwdmZR=aristaDot3MauType10GbaseDwdmZR, aristaDot3MauType10GbaseCRA=aristaDot3MauType10GbaseCRA, aristaDot3MauType10GbaseZR=aristaDot3MauType10GbaseZR, aristaDot3MauType10GbaseLRL=aristaDot3MauType10GbaseLRL, aristaDot3MauType100GbaseSR10=aristaDot3MauType100GbaseSR10, aristaDot3MauType100GbaseLR4=aristaDot3MauType100GbaseLR4, aristaDot3MauType100GbaseER4=aristaDot3MauType100GbaseER4, aristaDot3MauType40GbaseXSR4=aristaDot3MauType40GbaseXSR4, aristaDot3MauType40GbaseAR4=aristaDot3MauType40GbaseAR4, aristaDot3MauType40GbasePLR4=aristaDot3MauType40GbasePLR4, aristaDot3MauType40GbasePLRL4=aristaDot3MauType40GbasePLRL4, aristaMauMIB=aristaMauMIB)

