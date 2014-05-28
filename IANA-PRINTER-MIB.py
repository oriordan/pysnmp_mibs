# PySNMP SMI module. Autogenerated from smidump -f python IANA-PRINTER-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 22 11:57:41 2014,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class PrtAlertCodeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(16,32,14,19,9,30,506,20,1106,902,808,501,901,36,23,1004,1502,6,804,5,13,803,1303,1115,1509,802,1001,1110,35,812,28,24,27,1102,504,26,3,1301,502,811,1113,15,904,807,22,21,11,813,7,29,1105,2,1101,810,1003,8,1304,1801,31,1114,505,1111,1103,1104,1302,1109,503,801,25,1108,4,1107,18,1112,10,1505,507,806,1005,1506,805,1501,1,33,809,38,12,1503,17,903,1507,34,1504,1002,37,)
    namedValues = NamedValues(("other", 1), ("subunitLifeAlmostOver", 10), ("markerFuserUnderTemperature", 1001), ("markerFuserOverTemperature", 1002), ("markerFuserTimingFailure", 1003), ("markerFuserThermistorFailure", 1004), ("markerAdjustingPrintQuality", 1005), ("subunitLifeOver", 11), ("markerTonerEmpty", 1101), ("markerInkEmpty", 1102), ("markerPrintRibbonEmpty", 1103), ("markerTonerAlmostEmpty", 1104), ("markerInkAlmostEmpty", 1105), ("markerPrintRibbonAlmostEmpty", 1106), ("markerWasteTonerReceptacleAlmostFull", 1107), ("markerWasteInkReceptacleAlmostFull", 1108), ("markerWasteTonerReceptacleFull", 1109), ("markerWasteInkReceptacleFull", 1110), ("markerOpcLifeAlmostOver", 1111), ("markerOpcLifeOver", 1112), ("markerDeveloperAlmostEmpty", 1113), ("markerDeveloperEmpty", 1114), ("markerTonerCartridgeMissing", 1115), ("subunitAlmostEmpty", 12), ("subunitEmpty", 13), ("mediaPathMediaTrayMissing", 1301), ("mediaPathMediaTrayAlmostFull", 1302), ("mediaPathMediaTrayFull", 1303), ("mediaPathCannotDuplexMediaSelected", 1304), ("subunitAlmostFull", 14), ("subunitFull", 15), ("interpreterMemoryIncrease", 1501), ("interpreterMemoryDecrease", 1502), ("interpreterCartridgeAdded", 1503), ("interpreterCartridgeDeleted", 1504), ("interpreterResourceAdded", 1505), ("interpreterResourceDeleted", 1506), ("interpreterResourceUnavailable", 1507), ("interpreterComplexPageEncountered", 1509), ("subunitNearLimit", 16), ("subunitAtLimit", 17), ("subunitOpened", 18), ("alertRemovalOfBinaryChangeEntry", 1801), ("subunitClosed", 19), ("unknown", 2), ("subunitTurnedOn", 20), ("subunitTurnedOff", 21), ("subunitOffline", 22), ("subunitPowerSaver", 23), ("subunitWarmingUp", 24), ("subunitAdded", 25), ("subunitRemoved", 26), ("subunitResourceAdded", 27), ("subunitResourceRemoved", 28), ("subunitRecoverableFailure", 29), ("coverOpen", 3), ("subunitUnrecoverableFailure", 30), ("subunitRecoverableStorageError", 31), ("subunitUnrecoverableStorageError", 32), ("subunitMotorFailure", 33), ("subunitMemoryExhausted", 34), ("subunitUnderTemperature", 35), ("subunitOverTemperature", 36), ("subunitTimingFailure", 37), ("subunitThermistorFailure", 38), ("coverClosed", 4), ("interlockOpen", 5), ("doorOpen", 501), ("doorClosed", 502), ("powerUp", 503), ("powerDown", 504), ("printerNMSReset", 505), ("printerManualReset", 506), ("printerReadyToPrint", 507), ("interlockClosed", 6), ("configurationChange", 7), ("jam", 8), ("inputMediaTrayMissing", 801), ("inputMediaSizeChange", 802), ("inputMediaWeightChange", 803), ("inputMediaTypeChange", 804), ("inputMediaColorChange", 805), ("inputMediaFormPartsChange", 806), ("inputMediaSupplyLow", 807), ("inputMediaSupplyEmpty", 808), ("inputMediaChangeRequest", 809), ("inputManualInputRequest", 810), ("inputTrayPositionFailure", 811), ("inputTrayElevationFailure", 812), ("inputCannotFeedSizeSelected", 813), ("subunitMissing", 9), ("outputMediaTrayMissing", 901), ("outputMediaTrayAlmostFull", 902), ("outputMediaTrayFull", 903), ("outputMailboxSelectFailure", 904), )
    
class PrtAlertGroupTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(13,16,30,4,5,10,15,2,7,11,1,8,14,31,17,18,12,3,6,32,33,9,)
    namedValues = NamedValues(("other", 1), ("marker", 10), ("markerSupplies", 11), ("markerColorant", 12), ("mediaPath", 13), ("channel", 14), ("interpreter", 15), ("consoleDisplayBuffer", 16), ("consoleLights", 17), ("alert", 18), ("unknown", 2), ("hostResourcesMIBStorageTable", 3), ("finDevice", 30), ("finSupply", 31), ("finSupplyMediaInput", 32), ("finAttribute", 33), ("hostResourcesMIBDeviceTable", 4), ("generalPrinter", 5), ("cover", 6), ("localization", 7), ("input", 8), ("output", 9), )
    
class PrtAlertTrainingLevelTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,4,2,7,6,5,3,)
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("untrained", 3), ("trained", 4), ("fieldService", 5), ("management", 6), ("noInterventionRequired", 7), )
    
class PrtChannelTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(21,38,19,12,9,32,35,2,10,11,33,3,17,45,25,13,20,28,26,27,41,4,31,42,8,18,24,23,36,14,39,30,37,1,34,7,44,29,40,15,6,5,22,16,43,)
    namedValues = NamedValues(("other", 1), ("chNetwarePServer", 10), ("chPort9100", 11), ("chAppSocket", 12), ("chFTP", 13), ("chTFTP", 14), ("chDLCLLCPort", 15), ("chIBM3270", 16), ("chIBM5250", 17), ("chFax", 18), ("chIEEE1394", 19), ("unknown", 2), ("chTransport1", 20), ("chCPAP", 21), ("chDCERemoteProcCall", 22), ("chONCRemoteProcCall", 23), ("chOLE", 24), ("chNamedPipe", 25), ("chPCPrint", 26), ("chServerMessageBlock", 27), ("chDPMF", 28), ("chDLLAPI", 29), ("chSerialPort", 3), ("chVxDAPI", 30), ("chSystemObjectManager", 31), ("chDECLAT", 32), ("chNPAP", 33), ("chUSB", 34), ("chIRDA", 35), ("chPrintXChange", 36), ("chPortTCP", 37), ("chBidirPortTCP", 38), ("chUNPP", 39), ("chParallelPort", 4), ("chAppleTalkADSP", 40), ("chPortSPX", 41), ("chPortHTTP", 42), ("chNDPS", 43), ("chIPP", 44), ("chSMTP", 45), ("chIEEE1284Port", 5), ("chSCSIPort", 6), ("chAppleTalkPAP", 7), ("chLPDServer", 8), ("chNetwareRPrinter", 9), )
    
class PrtConsoleColorTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(9,7,8,6,2,1,5,10,3,4,)
    namedValues = NamedValues(("other", 1), ("orange", 10), ("unknown", 2), ("white", 3), ("red", 4), ("green", 5), ("blue", 6), ("cyan", 7), ("magenta", 8), ("yellow", 9), )
    
class PrtConsoleDisableTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(4,3,)
    namedValues = NamedValues(("enabled", 3), ("disabled", 4), )
    
class PrtCoverStatusTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,3,5,6,2,4,)
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("coverOpen", 3), ("coverClosed", 4), ("interlockOpen", 5), ("interlockClosed", 6), )
    
class PrtGeneralResetTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(4,5,6,3,)
    namedValues = NamedValues(("notResetting", 3), ("powerCycleReset", 4), ("resetToNVRAM", 5), ("resetToFactoryDefaults", 6), )
    
class PrtInputTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(3,1,5,7,2,6,4,)
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("sheetFeedAutoRemovableTray", 3), ("sheetFeedAutoNonRemovableTray", 4), ("sheetFeedManual", 5), ("continuousRoll", 6), ("continuousFanFold", 7), )
    
class PrtInterpreterLangFamilyTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(57,13,52,39,15,42,47,60,17,14,28,21,33,4,49,6,45,8,64,61,31,2,58,53,10,3,16,7,48,63,1,9,35,24,11,32,38,65,20,27,43,34,18,54,25,62,29,59,50,46,30,36,40,26,19,23,5,37,22,12,51,44,56,55,41,)
    namedValues = NamedValues(("other", 1), ("langEpson", 10), ("langDDIF", 11), ("langInterpress", 12), ("langISO6429", 13), ("langLineData", 14), ("langMODCA", 15), ("langREGIS", 16), ("langSCS", 17), ("langSPDL", 18), ("langTEK4014", 19), ("unknown", 2), ("langPDS", 20), ("langIGP", 21), ("langCodeV", 22), ("langDSCDSE", 23), ("langWPS", 24), ("langLN03", 25), ("langCCITT", 26), ("langQUIC", 27), ("langCPAP", 28), ("langDecPPL", 29), ("langPCL", 3), ("langSimpleText", 30), ("langNPAP", 31), ("langDOC", 32), ("langimPress", 33), ("langPinwriter", 34), ("langNPDL", 35), ("langNEC201PL", 36), ("langAutomatic", 37), ("langPages", 38), ("langLIPS", 39), ("langHPGL", 4), ("langTIFF", 40), ("langDiagnostic", 41), ("langPSPrinter", 42), ("langCaPSL", 43), ("langEXCL", 44), ("langLCDS", 45), ("langXES", 46), ("langPCLXL", 47), ("langART", 48), ("langTIPSI", 49), ("langPJL", 5), ("langPrescribe", 50), ("langLinePrinter", 51), ("langIDP", 52), ("langXJCL", 53), ("langPDF", 54), ("langRPDL", 55), ("langIntermecIPL", 56), ("langUBIFingerprint", 57), ("langUBIDirectProtocol", 58), ("langFujitsu", 59), ("langPS", 6), ("langCGM", 60), ("langJPEG", 61), ("langCALS1", 62), ("langCALS2", 63), ("langNIRS", 64), ("langC4", 65), ("langIPDS", 7), ("langPPDS", 8), ("langEscapeP", 9), )
    
class PrtMarkerMarkTechTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(20,23,21,22,25,2,5,11,15,1,27,26,14,13,16,19,4,24,9,10,18,6,3,8,12,7,17,)
    namedValues = NamedValues(("other", 1), ("impactBand", 10), ("impactOther", 11), ("inkjetAqueous", 12), ("inkjetSolid", 13), ("inkjetOther", 14), ("pen", 15), ("thermalTransfer", 16), ("thermalSensitive", 17), ("thermalDiffusion", 18), ("thermalOther", 19), ("unknown", 2), ("electroerosion", 20), ("electrostatic", 21), ("photographicMicrofiche", 22), ("photographicImagesetter", 23), ("photographicOther", 24), ("ionDeposition", 25), ("eBeam", 26), ("typesetter", 27), ("electrophotographicLED", 3), ("electrophotographicLaser", 4), ("electrophotographicOther", 5), ("impactMovingHeadDotMatrix9pin", 6), ("impactMovingHeadDotMatrix24pin", 7), ("impactMovingHeadDotMatrixOther", 8), ("impactMovingHeadFullyFormed", 9), )
    
class PrtMarkerSuppliesTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(33,14,12,28,13,8,4,9,32,23,29,7,5,30,24,26,10,11,22,27,18,34,6,17,2,31,19,15,1,16,3,25,20,21,)
    namedValues = NamedValues(("other", 1), ("developer", 10), ("fuserOil", 11), ("solidWax", 12), ("ribbonWax", 13), ("wasteWax", 14), ("fuser", 15), ("coronaWire", 16), ("fuserOilWick", 17), ("cleanerUnit", 18), ("fuserCleaningPad", 19), ("unknown", 2), ("transferUnit", 20), ("tonerCartridge", 21), ("fuserOiler", 22), ("water", 23), ("wasteWater", 24), ("glueWaterAdditive", 25), ("wastePaper", 26), ("bindingSupply", 27), ("bandingSupply", 28), ("stitchingWire", 29), ("toner", 3), ("shrinkWrap", 30), ("paperWrap", 31), ("staples", 32), ("inserts", 33), ("covers", 34), ("wasteToner", 4), ("ink", 5), ("inkCartridge", 6), ("inkRibbon", 7), ("wasteInk", 8), ("opc", 9), )
    
class PrtMediaPathTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,5,2,3,4,)
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("longEdgeBindingDuplex", 3), ("shortEdgeBindingDuplex", 4), ("simplex", 5), )
    
class PrtOutputTypeTC(Integer):
    subtypeSpec = Integer.subtypeSpec+SingleValueConstraint(1,4,5,7,2,3,6,)
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("removableBin", 3), ("unRemovableBin", 4), ("continuousRollDevice", 5), ("mailBox", 6), ("continuousFanFold", 7), )
    

# Objects

ianaPrinterMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 109)).setRevisions(("2005-09-14 00:00","2004-06-02 00:00",))
if mibBuilder.loadTexts: ianaPrinterMIB.setOrganization("IANA")
if mibBuilder.loadTexts: ianaPrinterMIB.setContactInfo("Internet Assigned Numbers Authority\nPostal: ICANN\n        4676 Admiralty Way, Suite 330\n        Marina del Rey, CA 90292\n\nTel:    +1 310 823 9358\nE-Mail: iana&iana.org")
if mibBuilder.loadTexts: ianaPrinterMIB.setDescription("This MIB module defines a set of printing-related\nTEXTUAL-CONVENTIONs for use in Printer MIB (RFC 3805),\nFinisher MIB (RFC 3806), and other MIBs which need to\nspecify printing mechanism details.\n\nAny additions or changes to the contents of this MIB\nmodule require either publication of an RFC, or\nDesignated Expert Review as defined in RFC 2434,\nGuidelines for Writing an IANA Considerations Section\nin RFCs.  The Designated Expert will be selected by\nthe IESG Area Director(s) of the Applications Area.\n\nCopyright (C) The Internet Society (2004). The\ninitial version of this MIB module was published\nin RFC 3805.  For full legal notices see the RFC\nitself or see:\nhttp://www.ietf.org/copyrights/ianamib.html")

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("IANA-PRINTER-MIB", PYSNMP_MODULE_ID=ianaPrinterMIB)

# Types
mibBuilder.exportSymbols("IANA-PRINTER-MIB", PrtAlertCodeTC=PrtAlertCodeTC, PrtAlertGroupTC=PrtAlertGroupTC, PrtAlertTrainingLevelTC=PrtAlertTrainingLevelTC, PrtChannelTypeTC=PrtChannelTypeTC, PrtConsoleColorTC=PrtConsoleColorTC, PrtConsoleDisableTC=PrtConsoleDisableTC, PrtCoverStatusTC=PrtCoverStatusTC, PrtGeneralResetTC=PrtGeneralResetTC, PrtInputTypeTC=PrtInputTypeTC, PrtInterpreterLangFamilyTC=PrtInterpreterLangFamilyTC, PrtMarkerMarkTechTC=PrtMarkerMarkTechTC, PrtMarkerSuppliesTypeTC=PrtMarkerSuppliesTypeTC, PrtMediaPathTypeTC=PrtMediaPathTypeTC, PrtOutputTypeTC=PrtOutputTypeTC)

# Objects
mibBuilder.exportSymbols("IANA-PRINTER-MIB", ianaPrinterMIB=ianaPrinterMIB)

