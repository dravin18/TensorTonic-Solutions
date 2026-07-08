import numpy as np

def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    """
    # Write code here
    return {
        "min": np.full(D, np.inf, dtype=np.float64),
        "max": np.full(D, -np.inf, dtype=np.float64),
    }
    
def streaming_minmax_update(state, X_batch, eps=1e-8):
    """
    Update state's min/max with X_batch, return normalized batch.
    """
    # Write code here
    X_batch = np.asarray(X_batch, dtype=state["min"].dtype)

    # Update running min/max
    state["min"] = np.minimum(state["min"], X_batch.min(axis=0))
    state["max"] = np.maximum(state["max"], X_batch.max(axis=0))

    # Normalize
    return (X_batch - state["min"]) / (state["max"] - state["min"] + eps)