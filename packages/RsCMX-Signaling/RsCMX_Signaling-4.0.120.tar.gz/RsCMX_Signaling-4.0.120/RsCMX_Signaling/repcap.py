from enum import Enum
# noinspection PyPep8Naming
from .Internal.RepeatedCapability import VALUE_DEFAULT as DefaultRepCap
# noinspection PyPep8Naming
from .Internal.RepeatedCapability import VALUE_EMPTY as EmptyRepCap


# noinspection SpellCheckingInspection
class Cword(Enum):
	"""Repeated capability Cword"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class Nnum(Enum):
	"""Repeated capability Nnum"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr310 = 310
	Nr311 = 311


# noinspection SpellCheckingInspection
class Pattern(Enum):
	"""Repeated capability Pattern"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1


# noinspection SpellCheckingInspection
class QamOrder(Enum):
	"""Repeated capability QamOrder"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Order64 = 64
	Order256 = 256


# noinspection SpellCheckingInspection
class Tnum(Enum):
	"""Repeated capability Tnum"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr300 = 300
	Nr301 = 301
	Nr310 = 310
	Nr311 = 311
	Nr319 = 319
