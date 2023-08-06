from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def mta(self):
		"""mta commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mta'):
			from .Mta import MtaCls
			self._mta = MtaCls(self._core, self._cmd_group)
		return self._mta

	@property
	def mtb(self):
		"""mtb commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mtb'):
			from .Mtb import MtbCls
			self._mtb = MtbCls(self._core, self._cmd_group)
		return self._mtb

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
