from pathlib import Path
from typing import List

from jinja2 import Environment, PackageLoader

from .finding import Finding

env = Environment(loader=PackageLoader("gcptool", "findings"), trim_blocks=True, lstrip_blocks=True)


def write_findings(output_folder: Path, findings: List[Finding]) -> None:
    for finding in findings:
        template = env.get_template(finding.template)

        sev_name = finding.severity.name
        content = template.render(finding_title=finding.title, severity=sev_name, **finding.vars)

        filename = "gcp_" + finding.template

        with open(str(output_folder / filename), "w") as f:
            f.write(content)
