#  Copyright (c) 2021-2023 NSTDA

{
    "name": "Condition (Problem)",
    "version": "16.0.0.1.0",
    "development_status": "Alpha",
    "category": "Medical",
    "author": "NSTDA, Piruin P.",
    "website": "https://nirun.life/",
    "license": "LGPL-3",
    "maintainers": ["piruin"],
    "depends": ["ni_patient"],
    "data": [
        "data/condition_class_data.xml",
        "data/condition_verification_data.xml",
        "security/ir.model.access.csv",
        "security/condition_rules.xml",
        "views/ni_condition_code_views.xml",
        "views/ni_condition_class_views.xml",
        "views/ni_condition_verification_views.xml",
        "views/ni_condition_views.xml",
        "views/ni_patient_views.xml",
        "views/ni_encounter_views.xml",
        "views/ni_condition_menu.xml",
    ],
    "application": False,
    "auto_install": False,
    "installable": True,
}
