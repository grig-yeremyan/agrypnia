#!/usr/bin/env python3
"""
Agrypnia
First automation script.

Displays the current status of Agrypnia OSINT modules.
"""


def summarize_modules(modules):
    """
    Display module status and return the number of unfinished modules.
    """
    remaining = 0

    for module in modules:
        name = module["name"]

        if module["status"] == "Ready":
            print(f"[✓] {name:<30} {module['status']}")

        elif module["status"] == "In Progress":
            print(f"[~] {name:<30} {module['status']}")
            remaining += 1

        else:
            print(f"[ ] {name:<30} {module['status']}")
            remaining += 1

    return remaining


def main():
    project_name = "Agrypnia"

    modules = [
        {"name": "README", "status": "Ready"},
        {"name": "WHOIS Collector", "status": "Planned"},
        {"name": "DNS Intelligence", "status": "Planned"},
        {"name": "SSL Analyzer", "status": "Planned"},
        {"name": "Dashboard", "status": "Planned"},
        {"name": "Threat Intelligence", "status": "Planned"},
    ]

    print("=" * 50)
    print(f"{project_name} - OSINT Platform")
    print("=" * 50)

    remaining = summarize_modules(modules)

    print()

    if remaining == 0:
        print("All modules are complete.")

    elif remaining < 3:
        print(f"{remaining} module(s) remaining.")

    else:
        print(f"{remaining} modules still need development.")

    return remaining


if __name__ == "__main__":
    raise SystemExit(main())
