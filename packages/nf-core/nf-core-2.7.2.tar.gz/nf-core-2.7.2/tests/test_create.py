"""Some tests covering the pipeline creation sub command.
"""
import os
import unittest

import git

import nf_core.create

from .utils import with_temporary_folder


class NfcoreCreateTest(unittest.TestCase):
    @with_temporary_folder
    def setUp(self, tmp_path):
        self.pipeline_name = "nf-core/test"
        self.pipeline_description = "just for 4w3s0m3 tests"
        self.pipeline_author = "Chuck Norris"
        self.pipeline_version = "1.0.0"
        self.default_branch = "default"

        self.pipeline = nf_core.create.PipelineCreate(
            name=self.pipeline_name,
            description=self.pipeline_description,
            author=self.pipeline_author,
            version=self.pipeline_version,
            no_git=False,
            force=True,
            outdir=tmp_path,
            plain=True,
            default_branch=self.default_branch,
        )

    def test_pipeline_creation(self):
        assert self.pipeline.template_params["name"] == self.pipeline_name
        assert self.pipeline.template_params["description"] == self.pipeline_description
        assert self.pipeline.template_params["author"] == self.pipeline_author
        assert self.pipeline.template_params["version"] == self.pipeline_version

    def test_pipeline_creation_initiation(self):
        self.pipeline.init_pipeline()
        assert os.path.isdir(os.path.join(self.pipeline.outdir, ".git"))
        assert f" {self.default_branch}\n" in git.Repo.init(self.pipeline.outdir).git.branch()
