#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
# Django server managment script 
import os
import sys

# print(sys.path)

def main():
    """Run administrative tasks."""
    
    # explicitly yell at python that this is the path omg 
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'api'))

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wildguard.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
