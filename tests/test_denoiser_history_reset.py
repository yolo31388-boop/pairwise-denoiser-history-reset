import pytest
import render.denoiser_history_reset as mod

CASES = [
    ("motion_magnitude_clamp", (4.0, 2.0)),
    ("reproject", (1, 2)),
    ("history_len", (8, 16)),
    ("spatial_fallback", (1, 2)),
    ("nan_guard", (1, 2)),
    ("specular_clamp", (0.8, 1.0)),
    ("disocclusion", (1, 2)),
    ("variance_estimate", (0.3, 0.5)),
    ("frame_reset", (1, 2)),
    ("ghost_score", (1.0, 2.0)),
    ("adaptive_alpha", (0.1, 0.2)),
    ("firefly_removal", (1, 2)),
    ("temporal_blend", (0.5, 0.3)),
    ("history_validate", (1, 2)),
    ("camera_rotation_handling", (180.0, 2.0)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
