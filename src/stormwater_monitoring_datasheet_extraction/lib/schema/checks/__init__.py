"""Schema checks."""

from stormwater_monitoring_datasheet_extraction.lib.schema.checks.dataframe_checks import (
    pk_check,
)
from stormwater_monitoring_datasheet_extraction.lib.schema.checks.field_checks import (
    is_valid_date,
)

# TODO: An alternative approach would be to create a custom class for the field type,
# handle validation in the class constructor, and then coerce the field to the class.
# This would allow us to generate better error messages, and would be more flexible
# for future changes.
# Consider doing this.
# On the other hand, would also be vulnerable to changes in nullability. If we find out a
# field can be null, and we've made a custom class to carry out our validations, we'd need
# to then coerce the null into the class, which in itself could be tricky, and which would
# also mean we'd end up with a non-null value, even if empty. (In other words, we'd get too
# "Pythonic" for real data integrity.)
# Also, we'd end up having field validations in multiple places unless we chose one approach
# or the other.
