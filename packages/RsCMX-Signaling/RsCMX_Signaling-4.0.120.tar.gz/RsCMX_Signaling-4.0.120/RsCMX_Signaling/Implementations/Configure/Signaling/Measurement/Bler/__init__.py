from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlerCls:
	"""Bler commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bler", core, parent)

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import EnableCls
			self._enable = EnableCls(self._core, self._cmd_group)
		return self._enable

	@property
	def scondition(self):
		"""scondition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scondition'):
			from .Scondition import SconditionCls
			self._scondition = SconditionCls(self._core, self._cmd_group)
		return self._scondition

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.signaling.measurement.bler.get_repetition() \n
		Specifies whether the measurement is stopped after a single shot or repeated continuously. After setting SINGleshot,
		configure also a stop condition. After setting CONTinuous, do not configure a stop condition.
		See [CONFigure:]SIGNaling:MEASurement:BLER:SCONdition. \n
			:return: repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:MEASurement:BLER:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: [CONFigure]:SIGNaling:MEASurement:BLER:REPetition \n
		Snippet: driver.configure.signaling.measurement.bler.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies whether the measurement is stopped after a single shot or repeated continuously. After setting SINGleshot,
		configure also a stop condition. After setting CONTinuous, do not configure a stop condition.
		See [CONFigure:]SIGNaling:MEASurement:BLER:SCONdition. \n
			:param repetition: SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:SIGNaling:MEASurement:BLER:REPetition {param}')

	def clone(self) -> 'BlerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BlerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
