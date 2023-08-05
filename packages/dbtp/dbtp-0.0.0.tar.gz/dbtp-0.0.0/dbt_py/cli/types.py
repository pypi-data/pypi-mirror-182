from typing import Any, Mapping, Optional, Sequence

# replace dagster._check with the library rheck
import rcheck

from ..types import DbtOutput


class DbtCliOutput(DbtOutput):
    """The results of executing a dbt command, along with additional metadata about the dbt CLI
    process that was run.

    Note that users should not construct instances of this class directly. This class is intended
    to be constructed from the JSON output of dbt commands.

    Attributes:
        command (str): The full shell command that was executed.
        return_code (int): The return code of the dbt CLI process.
        raw_output (str): The raw output (``stdout``) of the dbt CLI process.
        logs (List[Dict[str, Any]]): List of parsed JSON logs produced by the dbt command.
        result (Optional[Dict[str, Any]]): Dictionary containing dbt-reported result information
            contained in run_results.json.  Some dbt commands do not produce results, and will
            therefore have result = None.
        docs_url (Optional[str]): Hostname where dbt docs are being served for this project.
    """

    def __init__(
        self,
        command: str,
        return_code: int,
        raw_output: str,
        logs: Sequence[Mapping[str, Any]],
        result: Mapping[str, Any],
        docs_url: Optional[str] = None,
    ):
        rcheck.assert_str(command, "command")
        self._command = command
    
        rcheck.assert_int(return_code, "return_code")
        self._return_code = return_code

        rcheck.assert_str(raw_output, "raw_output")
        self._raw_output = raw_output

        rcheck.assert_sequence(logs, "logs", of=dict)
        self._logs = logs
    
        rcheck.assert_opt_str(docs_url, "docs_url")
        self._docs_url = docs_url

        super().__init__(result)

    @property
    def command(self) -> str:
        return self._command

    @property
    def return_code(self) -> int:
        return self._return_code

    @property
    def raw_output(self) -> str:
        return self._raw_output

    @property
    def logs(self) -> Sequence[Mapping[str, Any]]:
        return self._logs

    @property
    def docs_url(self) -> Optional[str]:
        return self._docs_url
