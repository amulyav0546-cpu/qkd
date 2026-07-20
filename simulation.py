import numpy as np

def channel_transmission(distance, loss):
    """
    Calculate transmission probability.
    """
    return np.exp(-loss * distance / 10)


def estimate_key_rate(distance,
                      qber,
                      detector_efficiency,
                      loss,
                      beta,
                      network_factor=1.0):
    """
    Simplified secret key-rate estimation.
    """

    transmission = channel_transmission(distance, loss)

    key_rate = (
        beta
        * detector_efficiency
        * transmission
        * max(0, (1 - 2*qber))
        * network_factor
    )

    return max(key_rate, 0)