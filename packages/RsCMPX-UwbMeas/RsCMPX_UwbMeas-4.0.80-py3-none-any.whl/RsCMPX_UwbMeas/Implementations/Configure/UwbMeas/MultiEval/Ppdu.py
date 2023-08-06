from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PpduCls:
	"""Ppdu commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ppdu", core, parent)

	def get_number(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:NUMBer \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.ppdu.get_number() \n
		No command help available \n
			:return: ppdu_number: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:NUMBer?')
		return Conversions.str_to_int(response)

	def set_number(self, ppdu_number: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:NUMBer \n
		Snippet: driver.configure.uwbMeas.multiEval.ppdu.set_number(ppdu_number = 1) \n
		No command help available \n
			:param ppdu_number: No help available
		"""
		param = Conversions.decimal_value_to_str(ppdu_number)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:NUMBer {param}')
