"""Schema checks."""

from stormwater_monitoring_datasheet_extraction.lib.schema.checks.dataframe_checks import (
    pk_check,
)

# from stormwater_monitoring_datasheet_extraction.lib.schema.checks.field_checks import ...
# TODO: An alternative approach would be to create a custom class for the field type,
# handle validation in the class constructor, and then coerce the field to the class.
# This would allow us to generate better error messages, and would be more flexible
# for future changes.
# Consider doing this.
