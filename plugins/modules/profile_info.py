#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This module allows users to retrieve information about the current Linode profile."""

from __future__ import absolute_import, division, print_function

# pylint: disable=unused-import
from typing import List, Any, Optional

from linode_api4 import Volume

from ansible_collections.linode.cloud.plugins.module_utils.linode_common import LinodeModuleBase
from ansible_collections.linode.cloud.plugins.module_utils.linode_helper import create_filter_and
from ansible_collections.linode.cloud.plugins.module_utils.linode_docs import global_authors, \
    global_requirements

import ansible_collections.linode.cloud.plugins.module_utils.doc_fragments.profile_info as docs

spec = dict(
    # Disable the default values
    label=dict(type='str', required=False, doc_hide=True),
    state=dict(type='str', required=False, doc_hide=True),
)

specdoc_meta = dict(
    description=[
        'Get info about a Linode Profile.'
    ],
    requirements=global_requirements,
    author=global_authors,
    spec=spec,
    examples=docs.specdoc_examples,
    return_values=dict(
        profile=dict(
            description='The profile info in JSON serialized form.',
            docs_url='https://www.linode.com/docs/api/profile/#profile-view__response-samples',
            type='dict',
            sample=docs.result_profile_samples
        )
    )
)


class Module(LinodeModuleBase):
    """Module for getting info about a Linode Profile"""

    def __init__(self) -> None:
        self.required_one_of: List[str] = []
        self.results = dict(
            profile=None,
        )

        self.module_arg_spec = spec

        super().__init__(module_arg_spec=self.module_arg_spec,
                         required_one_of=self.required_one_of)

    def exec_module(self, **kwargs: Any) -> Optional[dict]:
        """Entrypoint for volume info module"""

        self.results['profile'] = self.client.profile()._raw_json

        return self.results


def main() -> None:
    """Constructs and calls the profile_info module"""
    Module()


if __name__ == '__main__':
    main()