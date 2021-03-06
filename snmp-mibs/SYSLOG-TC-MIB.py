# PySNMP SMI module. Autogenerated from smidump -f python SYSLOG-TC-MIB
# by libsmi2pysnmp-0.1.3 at Fri May 23 07:47:56 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class SyslogFacility(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(15,9,5,20,11,8,14,2,10,12,4,1,21,7,23,22,17,16,19,18,13,3,6,0,)
    namedValues = NamedValues(("kern", 0), ("user", 1), ("authpriv", 10), ("ftp", 11), ("ntp", 12), ("audit", 13), ("console", 14), ("cron2", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("mail", 2), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23), ("daemon", 3), ("auth", 4), ("syslog", 5), ("lpr", 6), ("news", 7), ("uucp", 8), ("cron", 9), )
    
class SyslogSeverity(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(5,1,4,2,6,3,0,7,)
    namedValues = NamedValues(("emerg", 0), ("alert", 1), ("crit", 2), ("err", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), )
    

# Objects

syslogTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 173)).setRevisions(("2009-03-30 00:00",))
if mibBuilder.loadTexts: syslogTCMIB.setOrganization("IETF Syslog Working Group")
if mibBuilder.loadTexts: syslogTCMIB.setContactInfo("                      Glenn Mansfield Keeni\nPostal: Cyber Solutions Inc.\n        6-6-3, Minami Yoshinari\n        Aoba-ku, Sendai, Japan 989-3204.\n   Tel: +81-22-303-4012\n   Fax: +81-22-303-4015\n EMail: glenn@cysols.com\n\nSupport Group EMail: syslog@ietf.org")
if mibBuilder.loadTexts: syslogTCMIB.setDescription("The MIB module containing textual conventions for syslog\nmessages.\n\nCopyright (c) 2009 IETF Trust and the persons\nidentified as authors of the code.  All rights reserved.\n\nRedistribution and use in source and binary forms, with or\nwithout modification, are permitted provided that the\nfollowing conditions are met:\n\n- Redistributions of source code must retain the above\n  copyright notice, this list of conditions and the\n  following disclaimer.\n\n- Redistributions in binary form must reproduce the above\n  copyright notice, this list of conditions and the\n  following disclaimer in the documentation and/or other\n  materials provided with the distribution.\n\n- Neither the name of Internet Society, IETF or IETF\n  Trust, nor the names of specific contributors, may be\n  used to endorse or promote products derived from this\n  software without specific prior written permission.\n\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND\nCONTRIBUTORS 'AS IS' AND ANY EXPRESS OR IMPLIED\nWARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED\nWARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR\nPURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT\nOWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,\nINCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE\nGOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR\nBUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF\nLIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT\nOF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE\nPOSSIBILITY OF SUCH DAMAGE.\n\nThis version of this MIB module is part of RFC 5427;\nsee the RFC itself for full legal notices.")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("SYSLOG-TC-MIB", PYSNMP_MODULE_ID=syslogTCMIB)

# Types
mibBuilder.exportSymbols("SYSLOG-TC-MIB", SyslogFacility=SyslogFacility, SyslogSeverity=SyslogSeverity)

# Objects
mibBuilder.exportSymbols("SYSLOG-TC-MIB", syslogTCMIB=syslogTCMIB)

