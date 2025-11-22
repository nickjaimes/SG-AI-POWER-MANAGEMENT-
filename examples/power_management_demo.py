---

## 1️⃣1️⃣ `examples/power_management_demo.py`

```python
"""
SG AI Power Management – Simple Simulation Demo
Simulates varying load and shows controller decisions.
"""

import random
import time

from power_management.src.power_controller import PowerController
from power_management.src.power_profiles import get_power_profile


def main():
    profile = get_power_profile("balanced")
    controller = PowerController(**profile)

    print("\n[SG AI POWER MANAGEMENT DEMO] Profile: balanced\n")

    for step in range(1, 31):
        current_load_kw = random.uniform(20.0, 60.0)  # simulate varying load
        decision = controller.compute_power_action(current_load_kw)

        print(
            f"Step {step:02d} | Load: {current_load_kw:5.2f} kW | "
            f"Shed: {decision['shed_non_critical']} | "
            f"Throttle: {decision['throttle_level']:.2f} | "
            f"Emergency: {decision['emergency']} | "
            f"HINT: {decision['recommended_profile']}"
        )

        time.sleep(0.2)

    print("\nDemo complete.\n")


if __name__ == "__main__":
    main()
