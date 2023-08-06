from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ScellCls:
	"""Scell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scell", core, parent)

	def set(self, cell_group_name: str, cell_name: str, activation: bool = None, ul_enable: bool = None) -> None:
		"""SCPI: ADD:SIGNaling:LTE:CA:SCELl \n
		Snippet: driver.add.signaling.lte.ca.scell.set(cell_group_name = '1', cell_name = '1', activation = False, ul_enable = False) \n
		Adds one or more existing cells to an existing cell group, as SCells. \n
			:param cell_group_name: No help available
			:param cell_name: No help available
			:param activation: ON: automatic MAC activation (default) OFF: manual MAC activation via separate command
			:param ul_enable: Enables the UL (UL carrier aggregation)
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cell_group_name', cell_group_name, DataType.String), ArgSingle('cell_name', cell_name, DataType.String), ArgSingle('activation', activation, DataType.Boolean, None, is_optional=True), ArgSingle('ul_enable', ul_enable, DataType.Boolean, None, is_optional=True))
		self._core.io.write(f'ADD:SIGNaling:LTE:CA:SCELl {param}'.rstrip())
