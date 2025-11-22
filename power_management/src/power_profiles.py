def get_power_profile(name: str) -> dict:
    """
    Return predefined power management profiles.

    Profiles:
    - 'eco'         : prioritize energy saving
    - 'balanced'    : normal operation with protection
    - 'performance' : maximum performance, less saving
    - 'resilience'  : protect core loads at all cost
    """
    profiles = {
        "eco": {
            "max_capacity_kw": 50.0,
            "safety_margin": 0.25,          # keep at most 75% loaded
            "critical_load_fraction": 0.3,  # 30% is critical
        },
        "balanced": {
            "max_capacity_kw": 50.0,
            "safety_margin": 0.2,           # up to 80%
            "critical_load_fraction": 0.4,
        },
        "performance": {
            "max_capacity_kw": 50.0,
            "safety_margin": 0.1,           # up to 90%
            "critical_load_fraction": 0.3,
        },
        "resilience": {
            "max_capacity_kw": 50.0,
            "safety_margin": 0.3,           # up to 70%
            "critical_load_fraction": 0.6,  # 60% critical
        },
    }

    return profiles.get(name, profiles["balanced"])
