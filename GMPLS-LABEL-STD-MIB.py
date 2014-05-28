# PySNMP SMI module. Autogenerated from smidump -f python GMPLS-LABEL-STD-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:39 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( IndexIntegerNextFree, ) = mibBuilder.importSymbols("DIFFSERV-MIB", "IndexIntegerNextFree")
( GmplsFreeformLabelTC, GmplsLabelTypeTC, ) = mibBuilder.importSymbols("GMPLS-TC-STD-MIB", "GmplsFreeformLabelTC", "GmplsLabelTypeTC")
( InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
( MplsLabel, mplsStdMIB, ) = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "MplsLabel", "mplsStdMIB")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Integer32, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( RowStatus, StorageType, ) = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType")

# Objects

gmplsLabelStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 16)).setRevisions(("2007-02-27 00:00",))
if mibBuilder.loadTexts: gmplsLabelStdMIB.setOrganization("IETF Common Control and Measurement Plane (CCAMP) Working Group")
if mibBuilder.loadTexts: gmplsLabelStdMIB.setContactInfo("       Thomas D. Nadeau\nCisco Systems, Inc.\nEmail: tnadeau@cisco.com\n\nAdrian Farrel\nOld Dog Consulting\nEmail: adrian@olddog.co.uk\n\nComments about this document should be emailed directly to the\nCCAMP working group mailing list at ccamp@ops.ietf.org.")
if mibBuilder.loadTexts: gmplsLabelStdMIB.setDescription("Copyright (C) The IETF Trust (2007).  This version of\nthis MIB module is part of RFC 4803; see the RFC itself for\nfull legal notices.\n\n\n\n\nThis MIB module contains managed object definitions for labels\nwithin GMPLS systems as defined in\nGeneralized Multi-Protocol Label Switching (GMPLS) Signaling\nFunctional Description, Berger, L. (Editor), RFC 3471,\nJanuary 2003.")
gmplsLabelObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 16, 1))
gmplsLabelIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 1), IndexIntegerNextFree()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gmplsLabelIndexNext.setDescription("This object contains an unused value for gmplsLabelIndex,\nor a zero to indicate that no unused value exists or is\navailable.\n\nA management application wishing to create a row in the\ngmplsLabelTable may read this object and then attempt to\ncreate a row in the table.  If row creation fails (because\nanother application has already created a row with the\nsupplied index), the management application should read this\nobject again to get a new index value.\n\nWhen a row is created in the gmplsLabelTable with the\ngmplsLabelIndex value held by this object, an implementation\nMUST change the value in this object.")
gmplsLabelTable = MibTable((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2))
if mibBuilder.loadTexts: gmplsLabelTable.setDescription("Table of GMPLS Labels.  This table allows the representation\nof the more complex label forms required for GMPLS that cannot\nbe held within the TEXTUAL-CONVENTION MplsLabel; that is, labels\nthat cannot be encoded within 32 bits.  It is, nevertheless, also\ncapable of holding 32-bit labels or regular MPLS Labels if\ndesired.\n\n\nEach entry in this table represents an individual GMPLS Label\nvalue.  The representation of Labels in tables in other MIB\nmodules may be achieved by a referrence to an entry in this\ntable by means of a row pointer into this table.  The indexing\nof this table provides for arbitrary indexing and also for\nconcatenation of labels.\n\nFor an example of label concatenation, see RFC 3945, section 7.1.\nIn essence, a GMPLS Label may be composite in order to identify\na set of resources in the data plane.  Practical examples are\ntimeslots and wavelength sets (which are not contiguous like\nwavebands).\n\nThe indexing mechanism allows multiple entries in this table to\nbe seen as a sequence of labels that should be concatenated.\nOrdering is potentially very sensitive for concatenation.")
gmplsLabelEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1)).setIndexNames((0, "GMPLS-LABEL-STD-MIB", "gmplsLabelInterface"), (0, "GMPLS-LABEL-STD-MIB", "gmplsLabelIndex"), (0, "GMPLS-LABEL-STD-MIB", "gmplsLabelSubindex"))
if mibBuilder.loadTexts: gmplsLabelEntry.setDescription("An entry in this table represents a single label value.  There\nare three indexes into the table.\n\n-  The interface index may be helpful to distinguish which\n   labels are in use on which interfaces or to handle cases\n   where there are a very large number of labels in use in the\n   system.  When label representation is desired to apply to the\n   whole system or when it is not important to distinguish\n   labels by their interfaces, this index MAY be set to zero.\n\n-  The label index provides a way of identifying the label.\n\n-  The label sub-index is only used for concatenated labels.  It\n   identifies each component label.  When non-concatenated labels\n   are used, this index SHOULD be set to zero.\n\nA storage type object is supplied to control the storage type\nfor each entry, but implementations should note that the storage\ntype of conceptual rows in other tables that include row\npointers to an entry in this table SHOULD dictate the storage\ntype of the rows in this table where the row in the other table\nis more persistent.")
gmplsLabelInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 1), InterfaceIndexOrZero()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: gmplsLabelInterface.setDescription("The interface on which this label is used.  If this object is set\nto zero, the label MUST have applicability across the\nwhole system and not be limited to a single interface.")
gmplsLabelIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: gmplsLabelIndex.setDescription("An arbitrary index into the table to identify a label.\n\nNote that implementations that are representing 32-bit labels\nwithin this table MAY choose to align this index with the value\nof the label, and this may result in the use of the value zero\nsince it represents a valid label value.  Such implementation\nshould be aware of the implications of sparsely populated\n\n\ntables.\n\nA management application may read the gmplsLabelIndexNext\nobject to find a suitable value for this object.")
gmplsLabelSubindex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("noaccess")
if mibBuilder.loadTexts: gmplsLabelSubindex.setDescription("In conjunction with gmplsLabelInterface and gmplsLabelIndex,\nthis object uniquely identifies this row.  This sub-index allows\na single GMPLS Label to be defined as a concatenation of labels.\nThis is particularly useful in TDM.\n\nThe ordering of sub-labels is strict with the sub-label with\nthe lowest gmplsLabelSubindex appearing first.  Note that all\nsub-labels of a single GMPLS Label must share the same\ngmplsLabelInterface and gmplsLabelIndex values.  For labels that\nare not composed of concatenated sub-labels, this value SHOULD\nbe set to zero.")
gmplsLabelType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 4), GmplsLabelTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelType.setDescription("Identifies the type of this label.  Note that this object does\nnot determine whether MPLS or GMPLS signaling is in use: a value\nof gmplsMplsLabel(1) denotes that an MPLS Packet Label is\npresent in the gmplsLabelMplsLabel object and encoded using the\nMplsLabel TEXTUAL-CONVENTION (may be a 20-bit MPLS Label, a 10-\nor 23-bit Frame Relay Label, or an Asynchronous Transfer Mode\n(ATM) Label), but does not describe whether this is signaled\nusing MPLS or GMPLS.\n\nThe value of this object helps determine which of the following\nobjects are valid.  This object cannot be modified if\ngmplsLabelRowStatus is active(1).")
gmplsLabelMplsLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 5), MplsLabel().clone('0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelMplsLabel.setDescription("The value of an MPLS Label (that is a Packet Label) if this\ntable is used to store it.  This may be used in MPLS systems even\nthough the label values can be adequately stored in the MPLS MIB\nmodules (MPLS-LSR-STD-MIB and MPLS-TE-STD-MIB).  Furthermore, in\nmixed MPLS and GMPLS systems, it may be advantageous to store all\nlabels in a single label table.  Lastly, in GMPLS systems where\nPacket Labels are used (that is in systems that use GMPLS\nsignaling and GMPLS Labels for packet switching), it may be\ndesirable to use this table.\n\nThis object is only valid if gmplsLabelType is set\nto gmplsMplsLabel(1).  This object cannot be modified if\ngmplsLabelRowStatus is active(1).")
gmplsLabelPortWavelength = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 6), Unsigned32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelPortWavelength.setDescription("The value of a Port or Wavelength Label when carried as a\nGeneralized Label.  Only valid if gmplsLabelType is set to\ngmplsPortWavelengthLabel(2).  This object cannot be modified if\ngmplsLabelRowStatus is active(1).")
gmplsLabelFreeform = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 7), GmplsFreeformLabelTC().clone(hexValue='00')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelFreeform.setDescription("The value of a Freeform Generalized Label that does not conform\nto one of the standardized label encodings or that an\nimplementation chooses to represent as an octet string without\nfurther decoding.  Only valid if gmplsLabelType is set to\ngmplsFreeformLabel(3).  This object cannot be modified\nif gmplsLabelRowStatus is active(1).")
gmplsLabelSonetSdhSignalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSonetSdhSignalIndex.setDescription("The Signal Index value (S) of a SONET or SDH Generalized Label.\nZero indicates that this field is non-significant.  Only valid if\ngmplsLabelType is set to gmplsSonetLabel(4) or gmplsSdhLabel(5).\nThis object cannot be modified if gmplsLabelRowStatus is\nactive(1).")
gmplsLabelSdhVc = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSdhVc.setDescription("The VC Indicator (U) of an SDH Generalized Label.  Zero indicates\nthat this field is non-significant.  Only valid if gmplsLabelType\nis set to gmplsSdhLabel(5).  This object cannot be modified if\ngmplsLabelRowStatus is active(1).")
gmplsLabelSdhVcBranch = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSdhVcBranch.setDescription("The VC Branch Indicator (K) of an SDH Generalized Label.  Zero\nindicates that this field is non-significant.  Only valid if\ngmplsLabelType is set to gmplsSdhLabel(5).  This\nobject cannot be modified if gmplsLabelRowStatus is active(1).")
gmplsLabelSonetSdhBranch = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSonetSdhBranch.setDescription("The Branch Indicator (L) of a SONET or SDH Generalized Label.\nZero indicates that this field is non-significant.  Only valid\ngmplsLabelType is set to gmplsSonetLabel(4) or\ngmplsSdhLabel(5).  This object cannot be modified if\ngmplsLabelRowStatus is active(1).")
gmplsLabelSonetSdhGroupBranch = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelSonetSdhGroupBranch.setDescription("The Group Branch Indicator (M) of a SONET or SDH Generalized\nLabel.  Zero indicates that this field is non-significant.\nOnly valid if gmplsLabelType is set to gmplsSonetLabel(4) or\ngmplsSdhLabel(5).  This object cannot be modified if\ngmplsLabelRowStatus is active(1).")
gmplsLabelWavebandId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 13), Unsigned32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelWavebandId.setDescription("The waveband identifier component of a Waveband Label.  Only\nvalid if gmplsLabelType is set to gmplsWavebandLabel(6).  This\nobject cannot be modified if gmplsLabelRowStatus is active(1).")
gmplsLabelWavebandStart = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 14), Unsigned32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelWavebandStart.setDescription("The starting label component of a Waveband Label.  Only valid if\ngmplsLabelType is set to gmplsWavebandLabel(6).  This object\ncannot be modified if gmplsLabelRowStatus is active(1).")
gmplsLabelWavebandEnd = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 15), Unsigned32().clone(0)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelWavebandEnd.setDescription("The end label component of a Waveband Label.  Only valid if\ngmplsLabelType is set to gmplsWavebandLabel(6).  This object\ncannot be modified if gmplsLabelRowStatus is active(1).")
gmplsLabelStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 16), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelStorageType.setDescription("This variable indicates the storage type for this row.  The\nagent MUST ensure that this object's value remains consistent\nwith the storage type of any rows in other tables that contain\npointers to this row.  In particular, the storage type of this\nrow must be at least as permanent as that of any row that points\nto it.\nConceptual rows having the value 'permanent' need not\nallow write-access to any columnar objects in the row.")
gmplsLabelRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: gmplsLabelRowStatus.setDescription("This variable is used to create, modify, and/or delete a row in\nthis table.  When a row in this table has a row in the active(1)\nstate, no objects in this row can be modified except the\ngmplsLabelRowStatus and gmplsLabelStorageType.\n\nThe gmplsLabelType object does not have a default and must be\nset before a row can become active.  The corresponding label\nobjects (dependent on the value of gmplsLabelType) should also\nbe set unless they happen to need to use the specified default\nvalues as follows:\n\ngmplsLabelType setting             objects to be set\n--------------------------------------------------------------\ngmplsMplsLabel(1)                  gmplsLabelMplsLabel\n\ngmplsPortWavelengthLabel(2)        gmplsLabelPortWavelength\n\ngmplsFreeformLabel(3)              gmplsLabelFreeform\n\ngmplsSonetLabel(4)                 gmplsLabelSonetSdhSignalIndex\n                                   gmplsLabelSdhVc\n                                   gmplsLabelSdhVcBranch\n                                   gmplsLabelSonetSdhBranch\n                                   gmplsLabelSonetSdhGroupBranch\n\ngmplsSdhLabel(5)                   gmplsLabelSonetSdhSignalIndex\n                                   gmplsLabelSdhVc\n                                   gmplsLabelSdhVcBranch\n                                   gmplsLabelSonetSdhBranch\n                                   gmplsLabelSonetSdhGroupBranch\n\ngmplsWavebandLabel(6)              gmplsLabelWavebandId\n                                   gmplsLabelWavebandStart\n                                   gmplsLabelWavebandEnd")
gmplsLabelConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 16, 2))
gmplsLabelGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1))
gmplsLabelCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 2))

# Augmentions

# Groups

gmplsLabelTableGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 1)).setObjects(*(("GMPLS-LABEL-STD-MIB", "gmplsLabelType"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelRowStatus"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelIndexNext"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelStorageType"), ) )
if mibBuilder.loadTexts: gmplsLabelTableGroup.setDescription("Necessary, but not sufficient, set of objects to implement label\ntable support.  In addition, depending on the type of labels\nsupported, the following other groups defined below are\nmandatory:\n\n  gmplsLabelWavebandGroup and/or\n  gmplsLabelPacketGroup and/or\n  gmplsLabelPortWavelengthGroup and/or\n  gmplsLabelFreeformGroup and/or\n  gmplsLabelSonetSdhGroup.")
gmplsLabelPacketGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 2)).setObjects(*(("GMPLS-LABEL-STD-MIB", "gmplsLabelMplsLabel"), ) )
if mibBuilder.loadTexts: gmplsLabelPacketGroup.setDescription("Object needed to implement Packet (MPLS) Labels.")
gmplsLabelPortWavelengthGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 3)).setObjects(*(("GMPLS-LABEL-STD-MIB", "gmplsLabelPortWavelength"), ) )
if mibBuilder.loadTexts: gmplsLabelPortWavelengthGroup.setDescription("Object needed to implement Port and Wavelength Labels.")
gmplsLabelFreeformGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 4)).setObjects(*(("GMPLS-LABEL-STD-MIB", "gmplsLabelFreeform"), ) )
if mibBuilder.loadTexts: gmplsLabelFreeformGroup.setDescription("Object needed to implement Freeform Labels.")
gmplsLabelSonetSdhGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 5)).setObjects(*(("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhSignalIndex"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelSdhVc"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhBranch"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelSdhVcBranch"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhGroupBranch"), ) )
if mibBuilder.loadTexts: gmplsLabelSonetSdhGroup.setDescription("Objects needed to implement SONET and SDH Labels.")
gmplsLabelWavebandGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 6)).setObjects(*(("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandStart"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandEnd"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandId"), ) )
if mibBuilder.loadTexts: gmplsLabelWavebandGroup.setDescription("Objects needed to implement Waveband Labels.")

# Compliances

gmplsLabelModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 2, 1)).setObjects(*(("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelFreeformGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelPacketGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelPortWavelengthGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelTableGroup"), ("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandGroup"), ) )
if mibBuilder.loadTexts: gmplsLabelModuleReadOnlyCompliance.setDescription("Compliance requirement for implementations that only provide\nread-only support for GMPLS-LABEL-STD-MIB.  Such devices can then\nbe monitored but cannot be configured using this MIB module.")
gmplsLabelModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 2, 2)).setObjects(*(("GMPLS-LABEL-STD-MIB", "gmplsLabelTableGroup"), ) )
if mibBuilder.loadTexts: gmplsLabelModuleFullCompliance.setDescription("Compliance statement for agents that support the complete\nGMPLS-LABEL-STD-MIB module.\n\nThe mandatory groups have to be implemented by GMPLS LSRs\nclaiming support for this MIB module.  This MIB module is,\nhowever, not mandatory for a working implementation of a GMPLS\nLSR with full MIB support if the GMPLS Labels in use can be\nrepresented within a 32-bit quantity.")

# Exports

# Module identity
mibBuilder.exportSymbols("GMPLS-LABEL-STD-MIB", PYSNMP_MODULE_ID=gmplsLabelStdMIB)

# Objects
mibBuilder.exportSymbols("GMPLS-LABEL-STD-MIB", gmplsLabelStdMIB=gmplsLabelStdMIB, gmplsLabelObjects=gmplsLabelObjects, gmplsLabelIndexNext=gmplsLabelIndexNext, gmplsLabelTable=gmplsLabelTable, gmplsLabelEntry=gmplsLabelEntry, gmplsLabelInterface=gmplsLabelInterface, gmplsLabelIndex=gmplsLabelIndex, gmplsLabelSubindex=gmplsLabelSubindex, gmplsLabelType=gmplsLabelType, gmplsLabelMplsLabel=gmplsLabelMplsLabel, gmplsLabelPortWavelength=gmplsLabelPortWavelength, gmplsLabelFreeform=gmplsLabelFreeform, gmplsLabelSonetSdhSignalIndex=gmplsLabelSonetSdhSignalIndex, gmplsLabelSdhVc=gmplsLabelSdhVc, gmplsLabelSdhVcBranch=gmplsLabelSdhVcBranch, gmplsLabelSonetSdhBranch=gmplsLabelSonetSdhBranch, gmplsLabelSonetSdhGroupBranch=gmplsLabelSonetSdhGroupBranch, gmplsLabelWavebandId=gmplsLabelWavebandId, gmplsLabelWavebandStart=gmplsLabelWavebandStart, gmplsLabelWavebandEnd=gmplsLabelWavebandEnd, gmplsLabelStorageType=gmplsLabelStorageType, gmplsLabelRowStatus=gmplsLabelRowStatus, gmplsLabelConformance=gmplsLabelConformance, gmplsLabelGroups=gmplsLabelGroups, gmplsLabelCompliances=gmplsLabelCompliances)

# Groups
mibBuilder.exportSymbols("GMPLS-LABEL-STD-MIB", gmplsLabelTableGroup=gmplsLabelTableGroup, gmplsLabelPacketGroup=gmplsLabelPacketGroup, gmplsLabelPortWavelengthGroup=gmplsLabelPortWavelengthGroup, gmplsLabelFreeformGroup=gmplsLabelFreeformGroup, gmplsLabelSonetSdhGroup=gmplsLabelSonetSdhGroup, gmplsLabelWavebandGroup=gmplsLabelWavebandGroup)

# Compliances
mibBuilder.exportSymbols("GMPLS-LABEL-STD-MIB", gmplsLabelModuleReadOnlyCompliance=gmplsLabelModuleReadOnlyCompliance, gmplsLabelModuleFullCompliance=gmplsLabelModuleFullCompliance)
