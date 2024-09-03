#  Copyright (c) 2021 NSTDA

{
    "name": "Observation",
    "version": "16.0.0.4.0",
    "development_status": "Alpha",
    "category": "Healthcare",
    "author": "NSTDA, Piruin P.",
    "website": "https://nirun.life/",
    "license": "LGPL-3",
    "maintainers": ["piruin"],
    "depends": ["ni_patient", "mail", "uom", "uom_alias"],
    "data": [
        "security/ni_observation_group.xml",
        "security/ni_observation_security.xml",
        "security/ir.model.access.csv",
        "data/ir_cron_data.xml",
        "data/ir_sequence_data.xml",
        "data/uom_uom_data.xml",
        "data/ni_observation_interpretation_data.xml",
        "data/ni_observation_category_data.xml",
        "data/ni_observation_type_data.xml",
        "data/ni_observation_reference_range_data.xml",
        "views/ni_observation_category_views.xml",
        "views/ni_observation_interpretation_views.xml",
        "views/ni_observation_reference_range_views.xml",
        "views/ni_observation_type_views.xml",
        "views/ni_observation_value_code_views.xml",
        "views/ni_observation_views.xml",
        "views/ni_observation_sheet_views.xml",
        "views/ni_observation_menu.xml",
        "views/ni_patient_views.xml",
        "views/ni_encounter_views.xml",
        "report/ni_encounter_observation_view.xml",
        "report/ni_patient_observation_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "/ni_observation/static/src/component/**/*",
            "/ni_observation/static/src/scss/observation.scss",
        ],
    },
    "demo": [],
    "application": True,
    "auto_install": False,
    "installable": True,
}
