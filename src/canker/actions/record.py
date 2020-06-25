import json
from pathlib import Path

from canker.action import Action


class Record(Action):
    def before_run(self, tool):
        record_file = Path(self._config["output"])

        with record_file.open("a") as io:
            record = {"tool": tool.wrapped_tool(), "args": tool.args}
            print(json.dumps(record), file=io)
