from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BitrateCls:
	"""Bitrate commands group definition. 2 total commands, 0 Subgroups, 2 group commands
	Repeated Capability: Pddu, default value after init: Pddu.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bitrate", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_pddu_get', 'repcap_pddu_set', repcap.Pddu.Nr1)

	def repcap_pddu_set(self, pddu: repcap.Pddu) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Pddu.Default
		Default value after init: Pddu.Nr1"""
		self._cmd_group.set_repcap_enum_value(pddu)

	def repcap_pddu_get(self) -> repcap.Pddu:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def fetch(self, pddu=repcap.Pddu.Default) -> float:
		"""SCPI: FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:BITRate<PPDU> \n
		Snippet: value: float = driver.uwbMeas.multiEval.sinfo.phr.bitrate.fetch(pddu = repcap.Pddu.Default) \n
		Returns the data rate of the PHR. \n
			:param pddu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bitrate')
			:return: phr_bitrate: No help available"""
		pddu_cmd_val = self._cmd_group.get_repcap_cmd_value(pddu, repcap.Pddu)
		response = self._core.io.query_str(f'FETCh:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:BITRate{pddu_cmd_val}?')
		return Conversions.str_to_float(response)

	def read(self, pddu=repcap.Pddu.Default) -> float:
		"""SCPI: READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:BITRate<PPDU> \n
		Snippet: value: float = driver.uwbMeas.multiEval.sinfo.phr.bitrate.read(pddu = repcap.Pddu.Default) \n
		Returns the data rate of the PHR. \n
			:param pddu: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bitrate')
			:return: phr_bitrate: No help available"""
		pddu_cmd_val = self._cmd_group.get_repcap_cmd_value(pddu, repcap.Pddu)
		response = self._core.io.query_str(f'READ:UWB:MEASurement<Instance>:MEValuation:SINFo:PHR:BITRate{pddu_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'BitrateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BitrateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
