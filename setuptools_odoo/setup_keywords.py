# -*- coding: utf-8 -*-
# © 2015 ACSONE SA/NV
# License LGPLv3 (http://www.gnu.org/licenses/lgpl-3.0-standalone.html)

import warnings

from .core import (
    prepare_odoo_addon,
    prepare_odoo_addons,
)


def _set_dist_keywords(dist, setup_keywords):
    # got this trick from pbr
    for key, val in setup_keywords.items():
        if hasattr(dist.metadata, key):
            if getattr(dist.metadata, key) is None:
                setattr(dist.metadata, key, val)
        elif hasattr(dist, key):
            if getattr(dist, key) is None:
                setattr(dist, key, val)
        else:
            msg = 'Unknown distribution option: %s' % repr(key)
            warnings.warn(msg)


def _parse_options(value):
    depends_override = {}
    external_dependencies_override = {}
    if isinstance(value, dict):
        depends_override = \
            value.get('depends_override', {})
        external_dependencies_override = \
            value.get('external_dependencies_override', {})
    return depends_override, external_dependencies_override


def odoo_addon(dist, attr, value):
    depends_override, external_dependencies_override = _parse_options(value)
    setup_keywords = prepare_odoo_addon(
        depends_override=depends_override,
        external_dependencies_override=external_dependencies_override,
    )
    _set_dist_keywords(dist, setup_keywords)


def odoo_addons(dist, attr, value):
    depends_override, external_dependencies_override = _parse_options(value)
    setup_keywords = prepare_odoo_addons(
        depends_override=depends_override,
        external_dependencies_override=external_dependencies_override,
    )
    _set_dist_keywords(dist, setup_keywords)
