from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsduCls:
	"""Psdu commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psdu", core, parent)

	def get_bitrate(self) -> str:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PSDU:BITRate \n
		Snippet: value: str = driver.configure.uwbMeas.multiEval.psdu.get_bitrate() \n
		Queries the PSDU bit rate. \n
			:return: psdu_bitrate: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PSDU:BITRate?')
		return trim_str_response(response)
