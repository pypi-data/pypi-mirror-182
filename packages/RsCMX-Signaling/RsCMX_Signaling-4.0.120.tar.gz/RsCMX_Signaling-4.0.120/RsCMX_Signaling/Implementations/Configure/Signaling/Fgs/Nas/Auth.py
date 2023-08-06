from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AuthCls:
	"""Auth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auth", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:AUTH:ENABle \n
		Snippet: value: bool = driver.configure.signaling.fgs.nas.auth.get_enable() \n
		Enables authentication for 5G tracking areas. \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:SIGNaling:FGS:NAS:AUTH:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: [CONFigure]:SIGNaling:FGS:NAS:AUTH:ENABle \n
		Snippet: driver.configure.signaling.fgs.nas.auth.set_enable(enable = False) \n
		Enables authentication for 5G tracking areas. \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:SIGNaling:FGS:NAS:AUTH:ENABle {param}')
