from typing import Any, Mapping, Optional

# replace dagster._check with rcheck
import rcheck

class DbtOutput:
    """
    Base class for both DbtCliOutput and DbtRPCOutput. Contains a single field, `result`, which
    represents the dbt-formatted result of the command that was run (if any).

    Used internally, should not be instantiated directly by the user.
    """

    def __init__(self, result: Mapping[str, Any]):
        rcheck.assert_dict(result, "result", key_of=str)
        self._result = result

    @property
    def result(self) -> Mapping[str, Any]:
        return self._result

    @property
    def docs_url(self) -> Optional[str]:
        return None
