import os
import re


def readme(self):
    """Repository ``README.md`` tests

    The ``README.md`` files for a project are very important and must meet some requirements:

    * Nextflow badge

      * If no Nextflow badge is found, a warning is given
      * If a badge is found but the version doesn't match the minimum version in the config file, the test fails
      * Example badge code:

        .. code-block:: md

           [![Nextflow](https://img.shields.io/badge/nextflow-%E2%89%A50.27.6-brightgreen.svg)](https://www.nextflow.io/)

    * Bioconda badge

      * If your pipeline contains a file called ``environment.yml`` in the root directory, a bioconda badge is required
      * Required badge code:

        .. code-block:: md

           [![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg)](https://bioconda.github.io/)

    .. note:: These badges are a markdown image ``![alt-text](<image URL>)`` *inside* a markdown link ``[markdown image](<link URL>)``, so a bit fiddly to write.
    """
    passed = []
    warned = []
    failed = []

    # Remove field that should be ignored according to the linting config
    ignore_configs = self.lint_config.get("readme", [])

    with open(os.path.join(self.wf_path, "README.md"), "r") as fh:
        content = fh.read()

    if "nextflow_badge" not in ignore_configs:
        # Check that there is a readme badge showing the minimum required version of Nextflow
        # [![Nextflow](https://img.shields.io/badge/nextflow%20DSL2-%E2%89%A522.10.1-23aa62.svg)](https://www.nextflow.io/)
        # and that it has the correct version
        nf_badge_re = r"\[!\[Nextflow\]\(https://img\.shields\.io/badge/nextflow%20DSL2-!?(?:%E2%89%A5|%3E%3D)([\d\.]+)-23aa62\.svg\)\]\(https://www\.nextflow\.io/\)"
        match = re.search(nf_badge_re, content)
        if match:
            nf_badge_version = match.group(1).strip("'\"")
            try:
                if nf_badge_version != self.minNextflowVersion:
                    raise AssertionError()
            except (AssertionError, KeyError):
                failed.append(
                    f"README Nextflow minimum version badge does not match config. Badge: `{nf_badge_version}`, "
                    f"Config: `{self.minNextflowVersion}`"
                )
            else:
                passed.append(
                    f"README Nextflow minimum version badge matched config. Badge: `{nf_badge_version}`, "
                    f"Config: `{self.minNextflowVersion}`"
                )
        else:
            warned.append("README did not have a Nextflow minimum version badge.")

    # Check that the minimum version mentioned in the quick start section is consistent
    # Looking for: "1. Install [`Nextflow`](https://www.nextflow.io/docs/latest/getstarted.html#installation) (`>=22.10.1`)"
    nf_version_re = r"1\.\s*Install\s*\[`Nextflow`\]\(https://www.nextflow.io/docs/latest/getstarted.html#installation\)\s*\(`>=(\d*\.\d*\.\d*)`\)"
    match = re.search(nf_version_re, content)
    if match:
        nf_quickstart_version = match.group(1)
        try:
            if nf_quickstart_version != self.minNextflowVersion:
                raise AssertionError()
        except (AssertionError, KeyError):
            failed.append(
                f"README Nextflow minimium version in Quick Start section does not match config. README: `{nf_quickstart_version}`, Config `{self.minNextflowVersion}`"
            )
        else:
            passed.append(
                f"README Nextflow minimum version in Quick Start section matched config. README: `{nf_quickstart_version}`, Config: `{self.minNextflowVersion}`"
            )
    else:
        warned.append("README did not have a Nextflow minimum version mentioned in Quick Start section.")

    return {"passed": passed, "warned": warned, "failed": failed}
