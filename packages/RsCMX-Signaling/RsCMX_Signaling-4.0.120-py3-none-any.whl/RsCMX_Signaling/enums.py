from enum import Enum


# noinspection SpellCheckingInspection
class AckOrDtx(Enum):
	"""2 Members, CONTinue ... STOP"""
	CONTinue = 0
	STOP = 1


# noinspection SpellCheckingInspection
class Action(Enum):
	"""2 Members, CONNect ... DISConnect"""
	CONNect = 0
	DISConnect = 1


# noinspection SpellCheckingInspection
class Algorithm(Enum):
	"""4 Members, ERC1 ... ERC4"""
	ERC1 = 0
	ERC2 = 1
	ERC3 = 2
	ERC4 = 3


# noinspection SpellCheckingInspection
class Alpha(Enum):
	"""8 Members, A00 ... A10"""
	A00 = 0
	A04 = 1
	A05 = 2
	A06 = 3
	A07 = 4
	A08 = 5
	A09 = 6
	A10 = 7


# noinspection SpellCheckingInspection
class AntNoPorts(Enum):
	"""3 Members, P1 ... P4"""
	P1 = 0
	P2 = 1
	P4 = 2


# noinspection SpellCheckingInspection
class AntNoPortsB(Enum):
	"""4 Members, P1 ... P8"""
	P1 = 0
	P2 = 1
	P4 = 2
	P8 = 3


# noinspection SpellCheckingInspection
class Aoa(Enum):
	"""3 Members, AOA1 ... CONDucted"""
	AOA1 = 0
	AOA2 = 1
	CONDucted = 2


# noinspection SpellCheckingInspection
class Assignment(Enum):
	"""8 Members, NONE ... SA6"""
	NONE = 0
	SA0 = 1
	SA1 = 2
	SA2 = 3
	SA3 = 4
	SA4 = 5
	SA5 = 6
	SA6 = 7


# noinspection SpellCheckingInspection
class AuthProcedure(Enum):
	"""2 Members, EAKA ... FAKA"""
	EAKA = 0
	FAKA = 1


# noinspection SpellCheckingInspection
class AutoMode(Enum):
	"""3 Members, AUTO ... ON"""
	AUTO = 0
	OFF = 1
	ON = 2


# noinspection SpellCheckingInspection
class BandwidthCommon(Enum):
	"""8 Members, BW0 ... BW7"""
	BW0 = 0
	BW1 = 1
	BW2 = 2
	BW3 = 3
	BW4 = 4
	BW5 = 5
	BW6 = 6
	BW7 = 7


# noinspection SpellCheckingInspection
class BandwidthDedicated(Enum):
	"""4 Members, BW0 ... BW3"""
	BW0 = 0
	BW1 = 1
	BW2 = 2
	BW3 = 3


# noinspection SpellCheckingInspection
class BandwidthHoping(Enum):
	"""4 Members, HBW0 ... HBW3"""
	HBW0 = 0
	HBW1 = 1
	HBW2 = 2
	HBW3 = 3


# noinspection SpellCheckingInspection
class BeamConfigMode(Enum):
	"""3 Members, ALL ... UDEFined"""
	ALL = 0
	AUTO = 1
	UDEFined = 2


# noinspection SpellCheckingInspection
class BeamNoPorts(Enum):
	"""5 Members, NONE ... P8"""
	NONE = 0
	P1 = 1
	P2 = 2
	P4 = 3
	P8 = 4


# noinspection SpellCheckingInspection
class BlerState(Enum):
	"""3 Members, FAIL ... PENDing"""
	FAIL = 0
	PASS = 1
	PENDing = 2


# noinspection SpellCheckingInspection
class CellDeployment(Enum):
	"""2 Members, REAL ... VIRTual"""
	REAL = 0
	VIRTual = 1


# noinspection SpellCheckingInspection
class CellsToMeasure(Enum):
	"""4 Members, ALL ... OFF"""
	ALL = 0
	LTE = 1
	NRADio = 2
	OFF = 3


# noinspection SpellCheckingInspection
class CellType(Enum):
	"""2 Members, LTE ... NR"""
	LTE = 0
	NR = 1


# noinspection SpellCheckingInspection
class CipherAlgorithm(Enum):
	"""9 Members, EA0 ... HIGHest"""
	EA0 = 0
	EA1 = 1
	EA2 = 2
	EA3 = 3
	EA4 = 4
	EA5 = 5
	EA6 = 6
	EA7 = 7
	HIGHest = 8


# noinspection SpellCheckingInspection
class Class(Enum):
	"""4 Members, C0 ... C3"""
	C0 = 0
	C1 = 1
	C2 = 2
	C3 = 3


# noinspection SpellCheckingInspection
class Coding(Enum):
	"""3 Members, EIGHt ... UCS2"""
	EIGHt = 0
	GSM = 1
	UCS2 = 2


# noinspection SpellCheckingInspection
class CodingGroup(Enum):
	"""3 Members, G7 ... U2L"""
	G7 = 0
	G7L = 1
	U2L = 2


# noinspection SpellCheckingInspection
class ConfigMode(Enum):
	"""2 Members, AUTO ... UDEFined"""
	AUTO = 0
	UDEFined = 1


# noinspection SpellCheckingInspection
class ConfigType(Enum):
	"""2 Members, T1 ... T2"""
	T1 = 0
	T2 = 1


# noinspection SpellCheckingInspection
class Control(Enum):
	"""5 Members, CLOop ... PATTern"""
	CLOop = 0
	KEEP = 1
	MAX = 2
	MIN = 3
	PATTern = 4


# noinspection SpellCheckingInspection
class CoreNetwork(Enum):
	"""2 Members, EPS ... FG"""
	EPS = 0
	FG = 1


# noinspection SpellCheckingInspection
class Counter(Enum):
	"""9 Members, N1 ... N8"""
	N1 = 0
	N10 = 1
	N2 = 2
	N20 = 3
	N3 = 4
	N4 = 5
	N5 = 6
	N6 = 7
	N8 = 8


# noinspection SpellCheckingInspection
class DataFlow(Enum):
	"""4 Members, MCG ... SCGSplit"""
	MCG = 0
	MCGSplit = 1
	SCG = 2
	SCGSplit = 3


# noinspection SpellCheckingInspection
class DciFormat(Enum):
	"""10 Members, D0 ... D2D"""
	D0 = 0
	D1 = 1
	D1A = 2
	D1B = 3
	D1C = 4
	D2 = 5
	D2A = 6
	D2B = 7
	D2C = 8
	D2D = 9


# noinspection SpellCheckingInspection
class DciFormatB(Enum):
	"""2 Members, D10 ... D11"""
	D10 = 0
	D11 = 1


# noinspection SpellCheckingInspection
class DciFormatC(Enum):
	"""2 Members, D00 ... D01"""
	D00 = 0
	D01 = 1


# noinspection SpellCheckingInspection
class DcMode(Enum):
	"""5 Members, ENDC ... OFF"""
	ENDC = 0
	LTE = 1
	NR = 2
	NRDC = 3
	OFF = 4


# noinspection SpellCheckingInspection
class DiagBaseband(Enum):
	"""2 Members, BBCombining ... MRFPerf"""
	BBCombining = 0
	MRFPerf = 1


# noinspection SpellCheckingInspection
class DiagCellSignal(Enum):
	"""4 Members, COMBining ... SEParation"""
	COMBining = 0
	OTA = 1
	OTASep = 2
	SEParation = 3


# noinspection SpellCheckingInspection
class DisplayMode(Enum):
	"""2 Members, IMMediate ... NORMal"""
	IMMediate = 0
	NORMal = 1


# noinspection SpellCheckingInspection
class DlIqDataStreams(Enum):
	"""4 Members, S1 ... S8"""
	S1 = 0
	S2 = 1
	S4 = 2
	S8 = 3


# noinspection SpellCheckingInspection
class DlUlBandwidth(Enum):
	"""30 Members, B005 ... M90"""
	B005 = 0
	B010 = 1
	B015 = 2
	B020 = 3
	B025 = 4
	B030 = 5
	B040 = 6
	B050 = 7
	B060 = 8
	B070 = 9
	B080 = 10
	B090 = 11
	B100 = 12
	B200 = 13
	B400 = 14
	M10 = 15
	M100 = 16
	M15 = 17
	M20 = 18
	M200 = 19
	M25 = 20
	M30 = 21
	M40 = 22
	M400 = 23
	M5 = 24
	M50 = 25
	M60 = 26
	M70 = 27
	M80 = 28
	M90 = 29


# noinspection SpellCheckingInspection
class DlUlLocation(Enum):
	"""4 Members, HIGH ... USER"""
	HIGH = 0
	LOW = 1
	MID = 2
	USER = 3


# noinspection SpellCheckingInspection
class DuplexModeB(Enum):
	"""3 Members, FDD ... TDD"""
	FDD = 0
	SDL = 1
	TDD = 2


# noinspection SpellCheckingInspection
class EnableCqi(Enum):
	"""4 Members, APERiodic ... SPERsistant"""
	APERiodic = 0
	OFF = 1
	PERiodic = 2
	SPERsistant = 3


# noinspection SpellCheckingInspection
class EsmCause(Enum):
	"""45 Members, C100 ... C99"""
	C100 = 0
	C101 = 1
	C111 = 2
	C112 = 3
	C113 = 4
	C16 = 5
	C26 = 6
	C27 = 7
	C28 = 8
	C29 = 9
	C30 = 10
	C31 = 11
	C32 = 12
	C33 = 13
	C34 = 14
	C35 = 15
	C36 = 16
	C37 = 17
	C38 = 18
	C39 = 19
	C41 = 20
	C42 = 21
	C43 = 22
	C44 = 23
	C45 = 24
	C46 = 25
	C47 = 26
	C49 = 27
	C50 = 28
	C51 = 29
	C52 = 30
	C53 = 31
	C54 = 32
	C55 = 33
	C56 = 34
	C59 = 35
	C60 = 36
	C65 = 37
	C66 = 38
	C81 = 39
	C95 = 40
	C96 = 41
	C97 = 42
	C98 = 43
	C99 = 44


# noinspection SpellCheckingInspection
class FadingMode(Enum):
	"""2 Members, NORMal ... USER"""
	NORMal = 0
	USER = 1


# noinspection SpellCheckingInspection
class FadingProfile(Enum):
	"""80 Members, CTES ... UMIL"""
	CTES = 0
	EP5A = 1
	EP5H = 2
	EP5L = 3
	EP5M = 4
	EPAE = 5
	EPHE = 6
	EPLE = 7
	EPME = 8
	ET1A = 9
	ET1H = 10
	ET1L = 11
	ET1M = 12
	ET3A = 13
	ET3H = 14
	ET3L = 15
	ET3M = 16
	ET7A = 17
	ET7H = 18
	ET7L = 19
	ET7M = 20
	ETA3 = 21
	ETAE = 22
	ETHA = 23
	ETHE = 24
	ETLA = 25
	ETLE = 26
	ETMA = 27
	ETME = 28
	EV5A = 29
	EV5H = 30
	EV5L = 31
	EV5M = 32
	EV7A = 33
	EV7H = 34
	EV7L = 35
	EV7M = 36
	EVAE = 37
	EVHE = 38
	EVLE = 39
	EVME = 40
	HST = 41
	HST2 = 42
	INHL = 43
	INHN = 44
	MBSF = 45
	NONE = 46
	RMAL = 47
	RMAN = 48
	SMAL = 49
	SMAN = 50
	TAAA = 51
	TAAN = 52
	TAHA = 53
	TAHN = 54
	TALA = 55
	TALN = 56
	TAMA = 57
	TAMN = 58
	TBAC = 59
	TBHC = 60
	TBLC = 61
	TBMC = 62
	TCAD = 63
	TCAO = 64
	TCHD = 65
	TCHO = 66
	TCLD = 67
	TCLO = 68
	TCMD = 69
	TCMO = 70
	UMA3 = 71
	UMAA = 72
	UMAL = 73
	UMAN = 74
	UMI1 = 75
	UMI2 = 76
	UMI3 = 77
	UMIA = 78
	UMIL = 79


# noinspection SpellCheckingInspection
class FilterCoeff(Enum):
	"""15 Members, FC0 ... FC9"""
	FC0 = 0
	FC1 = 1
	FC11 = 2
	FC13 = 3
	FC15 = 4
	FC17 = 5
	FC19 = 6
	FC2 = 7
	FC3 = 8
	FC4 = 9
	FC5 = 10
	FC6 = 11
	FC7 = 12
	FC8 = 13
	FC9 = 14


# noinspection SpellCheckingInspection
class FlowControl(Enum):
	"""2 Members, GUARanteed ... NGUaranteed"""
	GUARanteed = 0
	NGUaranteed = 1


# noinspection SpellCheckingInspection
class FollowCqi(Enum):
	"""5 Members, DISabled ... WB"""
	DISabled = 0
	MSB = 1
	UEBSubband = 2
	UEPSubband = 3
	WB = 4


# noinspection SpellCheckingInspection
class FollowPmi(Enum):
	"""4 Members, DISabled ... WBEXplicit"""
	DISabled = 0
	SB = 1
	WB = 2
	WBEXplicit = 3


# noinspection SpellCheckingInspection
class FollowRi(Enum):
	"""3 Members, DISabled ... RETX"""
	DISabled = 0
	ENABled = 1
	RETX = 2


# noinspection SpellCheckingInspection
class FollowType(Enum):
	"""2 Members, DISabled ... ENABled"""
	DISabled = 0
	ENABled = 1


# noinspection SpellCheckingInspection
class FormatCqi(Enum):
	"""2 Members, SB ... WB"""
	SB = 0
	WB = 1


# noinspection SpellCheckingInspection
class Frame(Enum):
	"""5 Members, T16 ... T8"""
	T16 = 0
	T1T = 1
	T2 = 2
	T4 = 3
	T8 = 4


# noinspection SpellCheckingInspection
class FramesOffset(Enum):
	"""8 Members, T16 ... T8"""
	T16 = 0
	T1T = 1
	T2 = 2
	T2T = 3
	T32 = 4
	T4 = 5
	T4T = 6
	T8 = 7


# noinspection SpellCheckingInspection
class FrequencyRange(Enum):
	"""2 Members, FR1 ... FR2"""
	FR1 = 0
	FR2 = 1


# noinspection SpellCheckingInspection
class GroupLanguage(Enum):
	"""2 Members, G7L ... U2L"""
	G7L = 0
	U2L = 1


# noinspection SpellCheckingInspection
class IgnorePrachMode(Enum):
	"""3 Members, IALLways ... RALLways"""
	IALLways = 0
	IXTimes = 1
	RALLways = 2


# noinspection SpellCheckingInspection
class Info(Enum):
	"""3 Members, ALL ... UL"""
	ALL = 0
	DL = 1
	UL = 2


# noinspection SpellCheckingInspection
class IntegrityAlgorithm(Enum):
	"""9 Members, HIGHest ... IA7"""
	HIGHest = 0
	IA0 = 1
	IA1 = 2
	IA2 = 3
	IA3 = 4
	IA4 = 5
	IA5 = 6
	IA6 = 7
	IA7 = 8


# noinspection SpellCheckingInspection
class ItRateUnit(Enum):
	"""25 Members, G1 ... T64"""
	G1 = 0
	G16 = 1
	G256 = 2
	G4 = 3
	G64 = 4
	K1 = 5
	K16 = 6
	K256 = 7
	K4 = 8
	K64 = 9
	M1 = 10
	M16 = 11
	M256 = 12
	M4 = 13
	M64 = 14
	P1 = 15
	P16 = 16
	P256 = 17
	P4 = 18
	P64 = 19
	T1 = 20
	T16 = 21
	T256 = 22
	T4 = 23
	T64 = 24


# noinspection SpellCheckingInspection
class Ktc(Enum):
	"""2 Members, N2 ... N4"""
	N2 = 0
	N4 = 1


# noinspection SpellCheckingInspection
class LanguageB(Enum):
	"""16 Members, DANish ... UNSPecified"""
	DANish = 0
	DUTCh = 1
	ENGLish = 2
	FINNish = 3
	FRENch = 4
	GERMan = 5
	GREek = 6
	HUNGarian = 7
	ITALian = 8
	NORWegian = 9
	POLish = 10
	PORTuguese = 11
	SPANish = 12
	SWEDish = 13
	TURKish = 14
	UNSPecified = 15


# noinspection SpellCheckingInspection
class Level(Enum):
	"""5 Members, AL1 ... AL8"""
	AL1 = 0
	AL16 = 1
	AL2 = 2
	AL4 = 3
	AL8 = 4


# noinspection SpellCheckingInspection
class Location(Enum):
	"""3 Members, HIGH ... MID"""
	HIGH = 0
	LOW = 1
	MID = 2


# noinspection SpellCheckingInspection
class LogLevel(Enum):
	"""3 Members, BRIef ... VERBose"""
	BRIef = 0
	NONE = 1
	VERBose = 2


# noinspection SpellCheckingInspection
class LogType(Enum):
	"""4 Members, DISable ... PAYLoad"""
	DISable = 0
	FULL = 1
	HEADer = 2
	PAYLoad = 3


# noinspection SpellCheckingInspection
class Mapping(Enum):
	"""2 Members, A ... B"""
	A = 0
	B = 1


# noinspection SpellCheckingInspection
class MappingI(Enum):
	"""2 Members, INT ... NINT"""
	INT = 0
	NINT = 1


# noinspection SpellCheckingInspection
class MaxLength(Enum):
	"""2 Members, L1 ... L2"""
	L1 = 0
	L2 = 1


# noinspection SpellCheckingInspection
class McsTable(Enum):
	"""3 Members, Q1K ... Q64"""
	Q1K = 0
	Q256 = 1
	Q64 = 2


# noinspection SpellCheckingInspection
class McsTableB(Enum):
	"""3 Members, L64 ... Q64"""
	L64 = 0
	Q256 = 1
	Q64 = 2


# noinspection SpellCheckingInspection
class McsTableC(Enum):
	"""3 Members, AUTO ... UDEFined"""
	AUTO = 0
	P521 = 1
	UDEFined = 2


# noinspection SpellCheckingInspection
class Mimo(Enum):
	"""4 Members, M22 ... SISO"""
	M22 = 0
	M33 = 1
	M44 = 2
	SISO = 3


# noinspection SpellCheckingInspection
class MimoB(Enum):
	"""2 Members, M22 ... SISO"""
	M22 = 0
	SISO = 1


# noinspection SpellCheckingInspection
class Mode(Enum):
	"""3 Members, BINDex ... SSBBeam"""
	BINDex = 0
	CSIRs = 1
	SSBBeam = 2


# noinspection SpellCheckingInspection
class ModeB(Enum):
	"""2 Members, AUTO ... USER"""
	AUTO = 0
	USER = 1


# noinspection SpellCheckingInspection
class ModeBfollow(Enum):
	"""3 Members, AUTO ... OFF"""
	AUTO = 0
	BLOCk = 1
	OFF = 2


# noinspection SpellCheckingInspection
class ModeC(Enum):
	"""3 Members, AUTO ... USER"""
	AUTO = 0
	NOTC = 1
	USER = 2


# noinspection SpellCheckingInspection
class ModeD(Enum):
	"""3 Members, MAX ... UDEFined"""
	MAX = 0
	MIN = 1
	UDEFined = 2


# noinspection SpellCheckingInspection
class ModeE(Enum):
	"""8 Members, CPRI ... UDEFined"""
	CPRI = 0
	CQI = 1
	CRI = 2
	FIXed = 3
	PMI = 4
	PRI = 5
	RI = 6
	UDEFined = 7


# noinspection SpellCheckingInspection
class ModeFrecovery(Enum):
	"""3 Members, AUTO ... UDEFined"""
	AUTO = 0
	OFF = 1
	UDEFined = 2


# noinspection SpellCheckingInspection
class ModeSrs(Enum):
	"""4 Members, A508 ... UDEFined"""
	A508 = 0
	A521 = 1
	OFF = 2
	UDEFined = 3


# noinspection SpellCheckingInspection
class ModeUeCapability(Enum):
	"""3 Members, AUTO ... UDEFined"""
	AUTO = 0
	SKIP = 1
	UDEFined = 2


# noinspection SpellCheckingInspection
class ModeUeScheduling(Enum):
	"""5 Members, CPRI ... UDEFined"""
	CPRI = 0
	CQI = 1
	FIXed = 2
	PRI = 3
	UDEFined = 4


# noinspection SpellCheckingInspection
class Modulation(Enum):
	"""7 Members, BPSK ... QPSK"""
	BPSK = 0
	P2BPsk = 1
	Q1024 = 2
	Q16 = 3
	Q256 = 4
	Q64 = 5
	QPSK = 6


# noinspection SpellCheckingInspection
class ModulationB(Enum):
	"""7 Members, BPSK ... QPSK"""
	BPSK = 0
	P2BPsk = 1
	Q16 = 2
	Q1K = 3
	Q256 = 4
	Q64 = 5
	QPSK = 6


# noinspection SpellCheckingInspection
class ModulationRetr(Enum):
	"""8 Members, AUTO ... QPSK"""
	AUTO = 0
	BPSK = 1
	HPBP = 2
	Q16 = 3
	Q1K = 4
	Q256 = 5
	Q64 = 6
	QPSK = 7


# noinspection SpellCheckingInspection
class MtxPosition(Enum):
	"""4 Members, P0 ... P3"""
	P0 = 0
	P1 = 1
	P2 = 2
	P3 = 3


# noinspection SpellCheckingInspection
class NameType(Enum):
	"""2 Members, GUI ... RESource"""
	GUI = 0
	RESource = 1


# noinspection SpellCheckingInspection
class NcellsToMeasure(Enum):
	"""5 Members, ALL ... OFF"""
	ALL = 0
	IAFRequency = 1
	IFRequency = 2
	IRAT = 3
	OFF = 4


# noinspection SpellCheckingInspection
class NcellType(Enum):
	"""3 Members, IAFRequency ... IRAT"""
	IAFRequency = 0
	IFRequency = 1
	IRAT = 2


# noinspection SpellCheckingInspection
class NcoherentTpmi(Enum):
	"""2 Members, FPARtial ... NCOHerent"""
	FPARtial = 0
	NCOHerent = 1


# noinspection SpellCheckingInspection
class NeighborCellType(Enum):
	"""3 Members, CNETwork ... SIB"""
	CNETwork = 0
	NCList = 1
	SIB = 2


# noinspection SpellCheckingInspection
class NoSymbols(Enum):
	"""4 Members, S1 ... S4"""
	S1 = 0
	S2 = 1
	S3 = 2
	S4 = 3


# noinspection SpellCheckingInspection
class NoSymbolsN(Enum):
	"""3 Members, N1 ... N4"""
	N1 = 0
	N2 = 1
	N4 = 2


# noinspection SpellCheckingInspection
class OnDurationTimer(Enum):
	"""55 Members, M1 ... M9D"""
	M1 = 0
	M10 = 1
	M100 = 2
	M10D = 3
	M11D = 4
	M12D = 5
	M13D = 6
	M14D = 7
	M15D = 8
	M16D = 9
	M17D = 10
	M18D = 11
	M19D = 12
	M1D = 13
	M1K0 = 14
	M1K2 = 15
	M1K6 = 16
	M2 = 17
	M20 = 18
	M200 = 19
	M20D = 20
	M21D = 21
	M22D = 22
	M23D = 23
	M24D = 24
	M25D = 25
	M26D = 26
	M27D = 27
	M28D = 28
	M29D = 29
	M2D = 30
	M3 = 31
	M30 = 32
	M300 = 33
	M30D = 34
	M31D = 35
	M3D = 36
	M4 = 37
	M40 = 38
	M400 = 39
	M4D = 40
	M5 = 41
	M50 = 42
	M500 = 43
	M5D = 44
	M6 = 45
	M60 = 46
	M600 = 47
	M6D = 48
	M7D = 49
	M8 = 50
	M80 = 51
	M800 = 52
	M8D = 53
	M9D = 54


# noinspection SpellCheckingInspection
class PagingCycle(Enum):
	"""4 Members, P128 ... P64"""
	P128 = 0
	P256 = 1
	P32 = 2
	P64 = 3


# noinspection SpellCheckingInspection
class Pattern(Enum):
	"""4 Members, D1 ... U3"""
	D1 = 0
	KEEP = 1
	U1 = 2
	U3 = 3


# noinspection SpellCheckingInspection
class PdcchFormat(Enum):
	"""5 Members, N1 ... NAV"""
	N1 = 0
	N2 = 1
	N4 = 2
	N8 = 3
	NAV = 4


# noinspection SpellCheckingInspection
class PduState(Enum):
	"""6 Members, ACTive ... MIP"""
	ACTive = 0
	AIP = 1
	AUIP = 2
	DIP = 3
	INACtive = 4
	MIP = 5


# noinspection SpellCheckingInspection
class Periodicity(Enum):
	"""10 Members, P0P5 ... P5"""
	P0P5 = 0
	P0P6 = 1
	P1 = 2
	P10 = 3
	P1P2 = 4
	P2 = 5
	P2P5 = 6
	P3 = 7
	P4 = 8
	P5 = 9


# noinspection SpellCheckingInspection
class PeriodicityB(Enum):
	"""6 Members, P10 ... P80"""
	P10 = 0
	P160 = 1
	P20 = 2
	P40 = 3
	P5 = 4
	P80 = 5


# noinspection SpellCheckingInspection
class PeriodicityCqiReport(Enum):
	"""11 Members, P10 ... UDEFined"""
	P10 = 0
	P16 = 1
	P160 = 2
	P20 = 3
	P320 = 4
	P4 = 5
	P40 = 6
	P5 = 7
	P8 = 8
	P80 = 9
	UDEFined = 10


# noinspection SpellCheckingInspection
class PeriodicityReport(Enum):
	"""10 Members, P10 ... P80"""
	P10 = 0
	P16 = 1
	P160 = 2
	P20 = 3
	P320 = 4
	P4 = 5
	P40 = 6
	P5 = 7
	P8 = 8
	P80 = 9


# noinspection SpellCheckingInspection
class PeriodicityRsrc(Enum):
	"""13 Members, P10 ... P80"""
	P10 = 0
	P16 = 1
	P160 = 2
	P20 = 3
	P32 = 4
	P320 = 5
	P4 = 6
	P40 = 7
	P5 = 8
	P64 = 9
	P640 = 10
	P8 = 11
	P80 = 12


# noinspection SpellCheckingInspection
class Ports(Enum):
	"""8 Members, P1 ... P8"""
	P1 = 0
	P12 = 1
	P16 = 2
	P2 = 3
	P24 = 4
	P32 = 5
	P4 = 6
	P8 = 7


# noinspection SpellCheckingInspection
class Power(Enum):
	"""16 Members, P100 ... P98"""
	P100 = 0
	P102 = 1
	P104 = 2
	P106 = 3
	P108 = 4
	P110 = 5
	P112 = 6
	P114 = 7
	P116 = 8
	P118 = 9
	P120 = 10
	P90 = 11
	P92 = 12
	P94 = 13
	P96 = 14
	P98 = 15


# noinspection SpellCheckingInspection
class PowerScaling(Enum):
	"""2 Members, TGPP ... TOPTimized"""
	TGPP = 0
	TOPTimized = 1


# noinspection SpellCheckingInspection
class Predefined3Gpp(Enum):
	"""38 Members, M1 ... M9"""
	M1 = 0
	M10 = 1
	M11 = 2
	M11A = 3
	M11B = 4
	M12 = 5
	M12A = 6
	M12B = 7
	M13 = 8
	M14 = 9
	M15 = 10
	M16 = 11
	M17 = 12
	M18 = 13
	M19 = 14
	M1A = 15
	M1B = 16
	M2 = 17
	M20 = 18
	M21 = 19
	M22 = 20
	M23 = 21
	M24 = 22
	M25 = 23
	M26 = 24
	M27 = 25
	M28 = 26
	M29 = 27
	M2A = 28
	M3 = 29
	M3A = 30
	M4 = 31
	M4A = 32
	M5 = 33
	M6 = 34
	M7 = 35
	M8 = 36
	M9 = 37


# noinspection SpellCheckingInspection
class PreferredNetw(Enum):
	"""4 Members, AUTO ... NONE"""
	AUTO = 0
	EPS = 1
	FG = 2
	NONE = 3


# noinspection SpellCheckingInspection
class ProhibitTimer(Enum):
	"""24 Members, INF ... S90"""
	INF = 0
	S0 = 1
	S0D4 = 2
	S0D5 = 3
	S0D8 = 4
	S1 = 5
	S10 = 6
	S12 = 7
	S120 = 8
	S1D6 = 9
	S2 = 10
	S20 = 11
	S3 = 12
	S30 = 13
	S300 = 14
	S4 = 15
	S5 = 16
	S6 = 17
	S60 = 18
	S600 = 19
	S7 = 20
	S8 = 21
	S9 = 22
	S90 = 23


# noinspection SpellCheckingInspection
class PwrRampingStepA(Enum):
	"""4 Members, S0 ... S6"""
	S0 = 0
	S2 = 1
	S4 = 2
	S6 = 3


# noinspection SpellCheckingInspection
class PwrRampingStepB(Enum):
	"""4 Members, S0 ... S4"""
	S0 = 0
	S2 = 1
	S3 = 2
	S4 = 3


# noinspection SpellCheckingInspection
class Qi(Enum):
	"""21 Members, Q1 ... Q9"""
	Q1 = 0
	Q2 = 1
	Q3 = 2
	Q4 = 3
	Q5 = 4
	Q6 = 5
	Q65 = 6
	Q66 = 7
	Q67 = 8
	Q69 = 9
	Q7 = 10
	Q70 = 11
	Q75 = 12
	Q79 = 13
	Q8 = 14
	Q80 = 15
	Q82 = 16
	Q83 = 17
	Q84 = 18
	Q85 = 19
	Q9 = 20


# noinspection SpellCheckingInspection
class Quantity(Enum):
	"""10 Members, OFF ... Q9"""
	OFF = 0
	Q1 = 1
	Q2 = 2
	Q3 = 3
	Q4 = 4
	Q5 = 5
	Q6 = 6
	Q7 = 7
	Q8 = 8
	Q9 = 9


# noinspection SpellCheckingInspection
class RangeChoice(Enum):
	"""5 Members, HASYmmetric ... UDEFined"""
	HASYmmetric = 0
	HIGH = 1
	LOW = 2
	MID = 3
	UDEFined = 4


# noinspection SpellCheckingInspection
class RegState(Enum):
	"""9 Members, DREG ... RIP"""
	DREG = 0
	DRIP = 1
	FREG = 2
	FRIP = 3
	NFReg = 4
	NREG = 5
	NRIP = 6
	REG = 7
	RIP = 8


# noinspection SpellCheckingInspection
class RegStateB(Enum):
	"""9 Members, CREG ... REG"""
	CREG = 0
	CRIP = 1
	DREG = 2
	DRIP = 3
	EREG = 4
	ERIP = 5
	LREG = 6
	LRIP = 7
	REG = 8


# noinspection SpellCheckingInspection
class Repeat(Enum):
	"""2 Members, CONTinuous ... SINGleshot"""
	CONTinuous = 0
	SINGleshot = 1


# noinspection SpellCheckingInspection
class ReportFormat(Enum):
	"""3 Members, OFF ... WB"""
	OFF = 0
	SB = 1
	WB = 2


# noinspection SpellCheckingInspection
class ReportInterval(Enum):
	"""14 Members, I1 ... I9"""
	I1 = 0
	I10 = 1
	I11 = 2
	I12 = 3
	I13 = 4
	I14 = 5
	I2 = 6
	I3 = 7
	I4 = 8
	I5 = 9
	I6 = 10
	I7 = 11
	I8 = 12
	I9 = 13


# noinspection SpellCheckingInspection
class ReportMode(Enum):
	"""2 Members, S1 ... S2"""
	S1 = 0
	S2 = 1


# noinspection SpellCheckingInspection
class ReportType(Enum):
	"""3 Members, APERiodic ... PERiodic"""
	APERiodic = 0
	OFF = 1
	PERiodic = 2


# noinspection SpellCheckingInspection
class ResourceId(Enum):
	"""2 Members, R1 ... R2"""
	R1 = 0
	R2 = 1


# noinspection SpellCheckingInspection
class RlcMode(Enum):
	"""4 Members, ACK ... UAUL"""
	ACK = 0
	UACK = 1
	UADL = 2
	UAUL = 3


# noinspection SpellCheckingInspection
class RnauTimer(Enum):
	"""9 Members, M10 ... OFF"""
	M10 = 0
	M120 = 1
	M20 = 2
	M30 = 3
	M360 = 4
	M5 = 5
	M60 = 6
	M720 = 7
	OFF = 8


# noinspection SpellCheckingInspection
class Routing(Enum):
	"""2 Members, DUT ... FIXed"""
	DUT = 0
	FIXed = 1


# noinspection SpellCheckingInspection
class RrcState(Enum):
	"""3 Members, CONNected ... INACtive"""
	CONNected = 0
	IDLE = 1
	INACtive = 2


# noinspection SpellCheckingInspection
class Schema(Enum):
	"""3 Members, CODebook ... TXASwitching"""
	CODebook = 0
	NCODebook = 1
	TXASwitching = 2


# noinspection SpellCheckingInspection
class SecurityAlgorithm(Enum):
	"""4 Members, AES ... ZUC"""
	AES = 0
	OFF = 1
	SNOW = 2
	ZUC = 3


# noinspection SpellCheckingInspection
class SecurityAlgorithmB(Enum):
	"""9 Members, EEA0 ... HIGHest"""
	EEA0 = 0
	EEA1 = 1
	EEA2 = 2
	EEA3 = 3
	EEA4 = 4
	EEA5 = 5
	EEA6 = 6
	EEA7 = 7
	HIGHest = 8


# noinspection SpellCheckingInspection
class SecurityAlgorithmC(Enum):
	"""9 Members, EIA0 ... HIGHest"""
	EIA0 = 0
	EIA1 = 1
	EIA2 = 2
	EIA3 = 3
	EIA4 = 4
	EIA5 = 5
	EIA6 = 6
	EIA7 = 7
	HIGHest = 8


# noinspection SpellCheckingInspection
class Severity(Enum):
	"""3 Members, ERRor ... WARNing"""
	ERRor = 0
	INFO = 1
	WARNing = 2


# noinspection SpellCheckingInspection
class SpecialPattern(Enum):
	"""12 Members, P0 ... PAV2"""
	P0 = 0
	P1 = 1
	P2 = 2
	P3 = 3
	P4 = 4
	P5 = 5
	P6 = 6
	P7 = 7
	P8 = 8
	P9 = 9
	PAV1 = 10
	PAV2 = 11


# noinspection SpellCheckingInspection
class SrcType(Enum):
	"""3 Members, PUCC ... PUSC"""
	PUCC = 0
	PUPU = 1
	PUSC = 2


# noinspection SpellCheckingInspection
class State(Enum):
	"""3 Members, OFF ... RUN"""
	OFF = 0
	RDY = 1
	RUN = 2


# noinspection SpellCheckingInspection
class StateCnetwork(Enum):
	"""10 Members, CREating ... TESTing"""
	CREating = 0
	DELeting = 1
	ERRor = 2
	EXHausted = 3
	IDLE = 4
	NAV = 5
	RUNNing = 6
	STARting = 7
	STOPping = 8
	TESTing = 9


# noinspection SpellCheckingInspection
class StateTest(Enum):
	"""2 Members, ERRor ... SUCCess"""
	ERRor = 0
	SUCCess = 1


# noinspection SpellCheckingInspection
class StopCondition(Enum):
	"""3 Members, CONFidence ... TIME"""
	CONFidence = 0
	SAMPles = 1
	TIME = 2


# noinspection SpellCheckingInspection
class SubCarrSpacing(Enum):
	"""5 Members, A15 ... E240"""
	A15 = 0
	B30 = 1
	C30 = 2
	D120 = 3
	E240 = 4


# noinspection SpellCheckingInspection
class Subframe(Enum):
	"""16 Members, SC0 ... SC9"""
	SC0 = 0
	SC1 = 1
	SC10 = 2
	SC11 = 3
	SC12 = 4
	SC13 = 5
	SC14 = 6
	SC15 = 7
	SC2 = 8
	SC3 = 9
	SC4 = 10
	SC5 = 11
	SC6 = 12
	SC7 = 13
	SC8 = 14
	SC9 = 15


# noinspection SpellCheckingInspection
class Target(Enum):
	"""5 Members, ALL ... TOPology"""
	ALL = 0
	CELL = 1
	LTE = 2
	NRADio = 3
	TOPology = 4


# noinspection SpellCheckingInspection
class TargetCellScg(Enum):
	"""1 Members, RELease ... RELease"""
	RELease = 0


# noinspection SpellCheckingInspection
class Tdd(Enum):
	"""3 Members, CP1 ... SEParation"""
	CP1 = 0
	CP2 = 1
	SEParation = 2


# noinspection SpellCheckingInspection
class TdType(Enum):
	"""3 Members, APERiodic ... PERSistent"""
	APERiodic = 0
	PERiodic = 1
	PERSistent = 2


# noinspection SpellCheckingInspection
class TestFunction(Enum):
	"""3 Members, RX ... TX"""
	RX = 0
	RXTX = 1
	TX = 2


# noinspection SpellCheckingInspection
class TestLoopState(Enum):
	"""2 Members, CLOSe ... OPEN"""
	CLOSe = 0
	OPEN = 1


# noinspection SpellCheckingInspection
class TimerUnit(Enum):
	"""8 Members, DEACtivated ... S30"""
	DEACtivated = 0
	H1 = 1
	H10 = 2
	H320 = 3
	M1 = 4
	M10 = 5
	S2 = 6
	S30 = 7


# noinspection SpellCheckingInspection
class TimerUnitB(Enum):
	"""4 Members, DEACtivated ... S2"""
	DEACtivated = 0
	M1 = 1
	M6 = 2
	S2 = 3


# noinspection SpellCheckingInspection
class Tmode(Enum):
	"""10 Members, TM1 ... TM9"""
	TM1 = 0
	TM10 = 1
	TM2 = 2
	TM3 = 3
	TM4 = 4
	TM5 = 5
	TM6 = 6
	TM7 = 7
	TM8 = 8
	TM9 = 9


# noinspection SpellCheckingInspection
class Tpmi(Enum):
	"""6 Members, T0 ... T5"""
	T0 = 0
	T1 = 1
	T2 = 2
	T3 = 3
	T4 = 4
	T5 = 5


# noinspection SpellCheckingInspection
class TxRxSeparation(Enum):
	"""2 Members, DEFault ... UDEFined"""
	DEFault = 0
	UDEFined = 1


# noinspection SpellCheckingInspection
class Type(Enum):
	"""2 Members, DCMC ... GDC"""
	DCMC = 0
	GDC = 1


# noinspection SpellCheckingInspection
class TypeB(Enum):
	"""1 Members, UDEFined ... UDEFined"""
	UDEFined = 0


# noinspection SpellCheckingInspection
class TypeDlUl(Enum):
	"""2 Members, RMC ... UDEFined"""
	RMC = 0
	UDEFined = 1


# noinspection SpellCheckingInspection
class UecState(Enum):
	"""7 Members, CESTablish ... SCGFailure"""
	CESTablish = 0
	CREestablish = 1
	CRELease = 2
	HANDover = 3
	OK = 4
	PAGing = 5
	SCGFailure = 6


# noinspection SpellCheckingInspection
class UlBandwidth(Enum):
	"""12 Members, B014 ... M5"""
	B014 = 0
	B030 = 1
	B050 = 2
	B100 = 3
	B150 = 4
	B200 = 5
	M10 = 6
	M15 = 7
	M1K4 = 8
	M20 = 9
	M3 = 10
	M5 = 11


# noinspection SpellCheckingInspection
class Version(Enum):
	"""5 Members, AUTO ... RV3"""
	AUTO = 0
	RV0 = 1
	RV1 = 2
	RV2 = 3
	RV3 = 4


# noinspection SpellCheckingInspection
class VoiceHandling(Enum):
	"""4 Members, EFHandover ... VONR"""
	EFHandover = 0
	EFRedirect = 1
	UECap = 2
	VONR = 3


# noinspection SpellCheckingInspection
class Waveform(Enum):
	"""2 Members, CP ... DTFS"""
	CP = 0
	DTFS = 1
