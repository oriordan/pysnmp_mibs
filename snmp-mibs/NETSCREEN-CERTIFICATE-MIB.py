# PySNMP SMI module. Autogenerated from smidump -f python NETSCREEN-CERTIFICATE-MIB
# by libsmi2pysnmp-0.1.3 at Fri May 30 14:12:55 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( netscreenVpn, netscreenVpnMibModule, ) = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn", "netscreenVpnMibModule")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
( DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString")

# Objects

netscreenCertificateMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 4, 0, 7)).setRevisions(("2004-05-03 20:22","2004-05-03 00:00","2004-03-03 00:00","2003-11-12 00:00","2001-09-28 00:00","2001-05-15 00:00",))
if mibBuilder.loadTexts: netscreenCertificateMibModule.setOrganization("Juniper Networks, Inc.")
if mibBuilder.loadTexts: netscreenCertificateMibModule.setContactInfo("Customer Support\n\n1194 North Mathilda Avenue \nSunnyvale, California 94089-1206\nUSA\n\nTel: 1-800-638-8296\nE-mail: customerservice@juniper.net\nHTTP://www.juniper.net")
if mibBuilder.loadTexts: netscreenCertificateMibModule.setDescription("This module defines the object that are used to monitor \nVPN certificates")
nsVpnCert = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 4, 7))
nsVpnCertDefTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 7, 1))
if mibBuilder.loadTexts: nsVpnCertDefTable.setDescription("Certificate default setting table collects the default\ncertificates used when establish a secure VPN connection in\nNetScreen device.")
nsVpnCertDefEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1)).setIndexNames((0, "NETSCREEN-CERTIFICATE-MIB", "nsVpnCertDefIndex"))
if mibBuilder.loadTexts: nsVpnCertDefEntry.setDescription("An entry containing attributes of a certificate")
nsVpnCertDefIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertDefIndex.setDescription("Table index using as primary key when retrieving the table.")
nsVpnCertDefLdap = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertDefLdap.setDescription("LDAP server name.")
nsVpnCertDefCrlUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertDefCrlUrl.setDescription("URL of CRL.")
nsVpnCertDefRefresh = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertDefRefresh.setDescription("CRL Refresh Frequency.")
nsVpnCertDefX509 = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 5), Integer().subtype(subtypeSpec=SingleValueConstraint(1,0,)).subtype(namedValues=NamedValues(("partial", 0), ("full", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertDefX509.setDescription("X509 Certificate Path Validation Level.")
nsVpnCertDefVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertDefVsys.setDescription("vsys the cert setting belongs to.")
nsVpnCertCfgTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 7, 2))
if mibBuilder.loadTexts: nsVpnCertCfgTable.setDescription("This table collects detail certificate information.")
nsVpnCertCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1)).setIndexNames((0, "NETSCREEN-CERTIFICATE-MIB", "nsVpnCertCfgIndex"))
if mibBuilder.loadTexts: nsVpnCertCfgEntry.setDescription("Each entry in the nsVpnCertCfgTable contains a set of\nattributes for a certificate")
nsVpnCertCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertCfgIndex.setDescription("A unique value for certification table.  Its value ranges\nbetween 0 and 65535 and may not be contiguous.")
nsVpnCertCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 2), Integer().subtype(subtypeSpec=SingleValueConstraint(0,1,)).subtype(namedValues=NamedValues(("ca", 0), ("local", 1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertCfgType.setDescription("Certificate type.")
nsVpnCertCfgSubject = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertCfgSubject.setDescription("Certificate subject.")
nsVpnCertCfgExpire = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertCfgExpire.setDescription("Certificate expire date.")
nsVpnCertCfgIssuer = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertCfgIssuer.setDescription("Certificate configuration details.")
nsVpnCertCfgVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 7, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnCertCfgVsys.setDescription("Certificate's vsys.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("NETSCREEN-CERTIFICATE-MIB", PYSNMP_MODULE_ID=netscreenCertificateMibModule)

# Objects
mibBuilder.exportSymbols("NETSCREEN-CERTIFICATE-MIB", netscreenCertificateMibModule=netscreenCertificateMibModule, nsVpnCert=nsVpnCert, nsVpnCertDefTable=nsVpnCertDefTable, nsVpnCertDefEntry=nsVpnCertDefEntry, nsVpnCertDefIndex=nsVpnCertDefIndex, nsVpnCertDefLdap=nsVpnCertDefLdap, nsVpnCertDefCrlUrl=nsVpnCertDefCrlUrl, nsVpnCertDefRefresh=nsVpnCertDefRefresh, nsVpnCertDefX509=nsVpnCertDefX509, nsVpnCertDefVsys=nsVpnCertDefVsys, nsVpnCertCfgTable=nsVpnCertCfgTable, nsVpnCertCfgEntry=nsVpnCertCfgEntry, nsVpnCertCfgIndex=nsVpnCertCfgIndex, nsVpnCertCfgType=nsVpnCertCfgType, nsVpnCertCfgSubject=nsVpnCertCfgSubject, nsVpnCertCfgExpire=nsVpnCertCfgExpire, nsVpnCertCfgIssuer=nsVpnCertCfgIssuer, nsVpnCertCfgVsys=nsVpnCertCfgVsys)
