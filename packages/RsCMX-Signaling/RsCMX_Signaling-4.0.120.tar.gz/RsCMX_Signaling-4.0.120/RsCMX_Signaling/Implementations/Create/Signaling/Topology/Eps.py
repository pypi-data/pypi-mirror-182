from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EpsCls:
	"""Eps commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eps", core, parent)

	def set(self, name_ta: str, name_plmn: str, ta_code: int = None, time_3412: float = None) -> None:
		"""SCPI: CREate:SIGNaling:TOPology:EPS \n
		Snippet: driver.create.signaling.topology.eps.set(name_ta = '1', name_plmn = '1', ta_code = 1, time_3412 = 1.0) \n
		Creates an EPS tracking area in a selected PLMN and optionally defines tracking area settings. Assign a unique name to
		each named object within the test environment. Assigning an already used name can be rejected with an error message, even
		if the other object has not the same type as the new object. \n
			:param name_ta: Assigns a name to the tracking area. The string is used in other commands to select this tracking area.
			:param name_plmn: PLMN containing the tracking area.
			:param ta_code: Tracking area code (TAC) .
			:param time_3412: Has no effect, for future use.
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_ta', name_ta, DataType.String), ArgSingle('name_plmn', name_plmn, DataType.String), ArgSingle('ta_code', ta_code, DataType.Integer, None, is_optional=True), ArgSingle('time_3412', time_3412, DataType.Float, None, is_optional=True))
		self._core.io.write(f'CREate:SIGNaling:TOPology:EPS {param}'.rstrip())
