from citeon.observer_collapse import ObserverCollapse

def test_entropy_collapse():
    oc = ObserverCollapse()
    result = oc.collapse_entropy(input_entropy=0.8, observer_bias=0.5)
    assert 0.0 <= result <= 1.0
