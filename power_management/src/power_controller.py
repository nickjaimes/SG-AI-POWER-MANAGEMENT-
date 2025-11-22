from dataclasses import dataclass


@dataclass
class PowerController:
    """
    SG AI Power Controller

    - Tracks load vs capacity
    - Decides when to:

      * shed non-critical loads
      * throttle performance
      * enter emergency mode

    - Integrates with:

      * TRINITY AI (high-level decisions)
      * QNSF (learning long-term patterns)
      * Thermal controller (joint optimizations)
    """

    max_capacity_kw: float      # maximum safe power capacity
    safety_margin: float        # fraction reserved as safety (0.0 - 0.5)
    critical_load_fraction: float  # fraction of load considered 'critical'

    def compute_power_action(self, current_load_kw: float) -> dict:
        """
        Compute action based on current load.

        Returns:
        {
          "shed_non_critical": bool,
          "throttle_level": float (0.0 - 1.0),
          "emergency": bool,
          "recommended_profile": str,
        }
        """
        safe_limit_kw = self.max_capacity_kw * (1.0 - self.safety_margin)

        load_ratio = current_load_kw / max(self.max_capacity_kw, 0.0001)

        shed_non_critical = False
        emergency = False

        # Base throttle level (0 = no throttle, 1 = maximum throttle)
        throttle_level = 0.0

        if current_load_kw > safe_limit_kw:
            # entering overload territory
            shed_non_critical = True
            overload_fraction = (current_load_kw - safe_limit_kw) / max(safe_limit_kw, 0.0001)
            throttle_level = min(1.0, 0.5 + overload_fraction)

        if current_load_kw > self.max_capacity_kw:
            emergency = True
            throttle_level = 1.0
            shed_non_critical = True

        # Recommended profile hint (symbolic – could be used by TRINITY)
        if load_ratio < 0.5:
            profile_hint = "eco"
        elif load_ratio < 0.8:
            profile_hint = "balanced"
        else:
            profile_hint = "resilience" if emergency else "performance"

        return {
            "shed_non_critical": shed_non_critical,
            "throttle_level": throttle_level,
            "emergency": emergency,
            "recommended_profile": profile_hint,
        }
