from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NradioCls:
	"""Nradio commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nradio", core, parent)

	@property
	def dbReport(self):
		"""dbReport commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbReport'):
			from .DbReport import DbReportCls
			self._dbReport = DbReportCls(self._core, self._cmd_group)
		return self._dbReport

	@property
	def oassistance(self):
		"""oassistance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_oassistance'):
			from .Oassistance import OassistanceCls
			self._oassistance = OassistanceCls(self._core, self._cmd_group)
		return self._oassistance

	@property
	def drxPref(self):
		"""drxPref commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_drxPref'):
			from .DrxPref import DrxPrefCls
			self._drxPref = DrxPrefCls(self._core, self._cmd_group)
		return self._drxPref

	@property
	def mbwPref(self):
		"""mbwPref commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mbwPref'):
			from .MbwPref import MbwPrefCls
			self._mbwPref = MbwPrefCls(self._core, self._cmd_group)
		return self._mbwPref

	@property
	def mccPref(self):
		"""mccPref commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mccPref'):
			from .MccPref import MccPrefCls
			self._mccPref = MccPrefCls(self._core, self._cmd_group)
		return self._mccPref

	@property
	def mmLayer(self):
		"""mmLayer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmLayer'):
			from .MmLayer import MmLayerCls
			self._mmLayer = MmLayerCls(self._core, self._cmd_group)
		return self._mmLayer

	@property
	def msOffset(self):
		"""msOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_msOffset'):
			from .MsOffset import MsOffsetCls
			self._msOffset = MsOffsetCls(self._core, self._cmd_group)
		return self._msOffset

	@property
	def relPref(self):
		"""relPref commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relPref'):
			from .RelPref import RelPrefCls
			self._relPref = RelPrefCls(self._core, self._cmd_group)
		return self._relPref

	def clone(self) -> 'NradioCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NradioCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
