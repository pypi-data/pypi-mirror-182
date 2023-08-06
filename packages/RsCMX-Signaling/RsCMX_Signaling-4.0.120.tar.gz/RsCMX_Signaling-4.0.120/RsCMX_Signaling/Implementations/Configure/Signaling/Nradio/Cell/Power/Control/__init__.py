from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ControlCls:
	"""Control commands group definition. 11 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("control", core, parent)

	@property
	def spbPower(self):
		"""spbPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spbPower'):
			from .SpbPower import SpbPowerCls
			self._spbPower = SpbPowerCls(self._core, self._cmd_group)
		return self._spbPower

	@property
	def pmax(self):
		"""pmax commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmax'):
			from .Pmax import PmaxCls
			self._pmax = PmaxCls(self._core, self._cmd_group)
		return self._pmax

	@property
	def tpControl(self):
		"""tpControl commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpControl'):
			from .TpControl import TpControlCls
			self._tpControl = TpControlCls(self._core, self._cmd_group)
		return self._tpControl

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import ChannelCls
			self._channel = ChannelCls(self._core, self._cmd_group)
		return self._channel

	@property
	def palphaSet(self):
		"""palphaSet commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_palphaSet'):
			from .PalphaSet import PalphaSetCls
			self._palphaSet = PalphaSetCls(self._core, self._cmd_group)
		return self._palphaSet

	@property
	def pnwGrant(self):
		"""pnwGrant commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pnwGrant'):
			from .PnwGrant import PnwGrantCls
			self._pnwGrant = PnwGrantCls(self._core, self._cmd_group)
		return self._pnwGrant

	def clone(self) -> 'ControlCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ControlCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
