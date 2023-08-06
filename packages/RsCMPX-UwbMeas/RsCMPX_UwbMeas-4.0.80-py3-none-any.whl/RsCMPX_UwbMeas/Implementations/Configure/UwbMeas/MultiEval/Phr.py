from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhrCls:
	"""Phr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phr", core, parent)

	def get_bitrate(self) -> str:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PHR:BITRate \n
		Snippet: value: str = driver.configure.uwbMeas.multiEval.phr.get_bitrate() \n
		Queries the data rate of the PHR. \n
			:return: phr_bitrate: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PHR:BITRate?')
		return trim_str_response(response)
