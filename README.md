pysnmp_mibs
===========

A collection of IETF &amp; IANA &amp; network vendor specific MIBs pre-compiled for PySNMP

[pysnmp](http://pysnmp.sf.net) and [pyasn1](http://pyasn1.sf.net) are great libraries for working with SNMP in Python.
Ilya Etingof (the author of the above projects) made a pypi package called [pysnmp-mibs](https://pypi.python.org/pypi/pysnmp-mibs/),
which contains standard mibs, however if you need to work with some proprietary network hardware, you'll need to compile your own files.
The process is not always straightforward, and this repo supposed to help you getting there in an easier way.
 
##Vendor resources:
 * Cisco: http://tools.cisco.com/Support/SNMP/do/BrowseMIB.do?local=en&step=2
 * Juniper: http://www.juniper.net/techpubs/software/index_mibs.html
 * Netscreen: http://www.juniper.net/techpubs/software/screenos/mibs.html
 * Arista: http://www.arista.com/en/support/arista-snmp-mibs
 * Aruba: http://support.arubanetworks.com (support account required)
 * Perle: http://www.perle.com/downloads/software/IOLAN
 * F5: https://support.f5.com/kb/en-us/solutions/public/0000/500/sol503.html (an actual F5 required)

##Usage:

```sh
> git clone https://github.com/oriordan/pysnmp_mibs/
> python
>>> from pyasn1.type import univ
>>> from pysnmp.entity.rfc3413.oneliner.mibvar import MibVariable
>>> from pysnmp.smi import builder, view
>>> mibBuilder = builder.MibBuilder().loadModules('SNMPv2-MIB')
>>> mibViewController = view.MibViewController(mibBuilder)
>>> x = MibVariable(univ.ObjectIdentifier('1.3.6.1.2.1.1.1')).resolveWithMib(mibViewController)
>>> x.getLabel()
('iso', 'org', 'dod', 'internet', 'mgmt', 'mib-2', 'system', 'sysDescr')
>>>
```

##Hints:

Sometimes network devices are not sending the traps according to their own MIB specification.
In order to minimize OID resolution issues, some compiled mibs are altered:
 * IF-MIB.py: Allowing zero interface index (because Cisco voice gateways are "special")
 * BGP4-V2-MIB-JUNIPER.py: Using InetAddressIPv6 for jnxBgpM2PeerLocalAddr and jnxBgpM2PeerRemoteAddr
 * CISCO-BGP4-MIB.py: Dropping cbgpPeer2Type from cbgpPeer2Entry
 * CISCO-DIAL-CONTROL-MIB.py: Using Integer for cCallHistoryConnectTime and cCallHistoryDisconnectTime
