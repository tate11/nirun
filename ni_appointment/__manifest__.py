#  Copyright (c) 2023 NSTDA

{
    "name": "Appointment",
    "version": "16.0.0.1.0",
    "development_status": "Alpha",
    "category": "Medical",
    "author": "NSTDA, Piruin P.",
    "website": "https://nirun.life/",
    "license": "LGPL-3",
    "maintainers": ["piruin"],
    "depends": ["ni_patient", "ni_condition", "calendar"],
    "data": [
        "data/ni_appointment_type_data.xml",
        "data/ni_appointment_cancel_reason_data.xml",
        "security/ir.model.access.csv",
        "views/ni_encounter_views.xml",
        "views/ni_appointment_views.xml",
        "views/ni_appointment_cancel_reason_views.xml",
        "views/ni_appointment_instruction_views.xml",
        "views/ni_appointment_type_views.xml",
        "views/ni_appointment_menu.xml",
        "wizard/ni_appointment_cancel_wizard_view.xml",
    ],
    "application": False,
    "auto_install": False,
    "installable": True,
}
