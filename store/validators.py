from django.core.exceptions import ValidationError

MAX_SIZE_KB = 500


def validate_file_size(file):
    if file.size > MAX_SIZE_KB * 1024:
        raise ValidationError(f"Files can't be larger than {MAX_SIZE_KB}KB")
