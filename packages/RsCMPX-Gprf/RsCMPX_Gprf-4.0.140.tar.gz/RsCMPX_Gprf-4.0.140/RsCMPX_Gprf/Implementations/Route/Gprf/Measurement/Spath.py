from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpathCls:
	"""Spath commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	def get_count(self) -> int:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SPATh:COUNt \n
		Snippet: value: int = driver.route.gprf.measurement.spath.get_count() \n
		No command help available \n
			:return: signal_path_count: No help available
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SPATh:COUNt?')
		return Conversions.str_to_int(response)

	def get_value(self) -> str:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SPATh \n
		Snippet: value: str = driver.route.gprf.measurement.spath.get_value() \n
		Selects the signal input path (RF connection) for the measured signal. For possible signal path strings, see method
		RsCMPX_Gprf.Catalog.Gprf.Measurement.Spath.get_. \n
			:return: signal_path: Name of the RF connection
		"""
		response = self._core.io.query_str('ROUTe:GPRF:MEASurement<Instance>:SPATh?')
		return trim_str_response(response)

	def set_value(self, signal_path: str) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SPATh \n
		Snippet: driver.route.gprf.measurement.spath.set_value(signal_path = '1') \n
		Selects the signal input path (RF connection) for the measured signal. For possible signal path strings, see method
		RsCMPX_Gprf.Catalog.Gprf.Measurement.Spath.get_. \n
			:param signal_path: Name of the RF connection
		"""
		param = Conversions.value_to_quoted_str(signal_path)
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:SPATh {param}')
