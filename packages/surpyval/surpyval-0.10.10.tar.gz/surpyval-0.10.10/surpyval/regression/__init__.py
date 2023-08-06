import autograd.numpy as np
from collections import defaultdict

from .cox_ph import CoxPH

from .proportional_hazards import ProportionalHazardsFitter
from .accelerated_failure_time import AcceleratedFailureTimeFitter
from .parameter_substitution import ParameterSubstitutionFitter

import surpyval as surv
from .lifemodels import (
    InversePower, Power,
    InverseExponential, Exponential,
    Linear,
    Eyring, InverseEyring,
    DualExponential,
    DualPower,
    PowerExponential,
    GeneralLogLinear
)

from ..parametric import (
    LogNormal,
    Normal,
    Weibull,
    Gumbel,
    Logistic
)

# Useful for proportional odds
# https://data.princeton.edu/pop509/parametricsurvival.pdf

# Semi-Parametric Proportional Hazard
# CoxPH = CoxProportionalHazardsFitter()

DISTS = [surv.Exponential, Normal, Weibull, Gumbel, Logistic, LogNormal]
LIFE_PARAMS = ['lambda', 'mu', 'alpha', 'mu', 'mu', 'mu']
LIFE_MODELS = [
    Power, 
    InversePower,
    Exponential,
    InverseExponential,
    Eyring,
    InverseEyring,
    Linear,
    DualExponential,
    DualPower,
    PowerExponential
]

life_parameter_transform = defaultdict(lambda: None)
life_parameter_inverse_transform = defaultdict(lambda: None)
baseline_parameters = defaultdict(lambda: [])

life_parameter_transform['LogNormal'] = lambda x: np.log(x)
life_parameter_transform['Exponential'] = lambda x: 1./x

life_parameter_inverse_transform['LogNormal'] = lambda x: np.exp(x)
life_parameter_inverse_transform['Exponential'] = lambda x: 1./x

# Quite remarkable - creates every life model and distribution class!
for dist, parameter in zip(DISTS, LIFE_PARAMS):
    for life_model in LIFE_MODELS:
        name = dist.name + life_model.name + "AL"
        vars()[name] = ParameterSubstitutionFitter(
                            'Accelerated Life', 
                            name, dist, life_model, 
                            parameter,
                            param_transform=life_parameter_transform[dist.name],
                            inverse_param_transform=life_parameter_inverse_transform[dist.name]
                        )

# I think the baseline feature should be removed
# I think the logic behind it was flawed from the start.
for dist, parameter in zip(DISTS, LIFE_PARAMS):
    name = dist.name + life_model.name + "AL"
    vars()[name] = ParameterSubstitutionFitter(
                        'Accelerated Life', 
                        name,
                        dist,
                        GeneralLogLinear,
                        parameter,
                        baseline=[parameter],
                        param_transform=life_parameter_transform[dist.name],
                        inverse_param_transform=life_parameter_inverse_transform[dist.name]
                    )

# Parametric Proportional Hazard
ExponentialPH = ProportionalHazardsFitter(
    'ExponentialPH', 
    surv.Exponential,
    lambda Z, *params: np.exp(np.dot(Z, np.array(params))),
    lambda Z: (((None, None),) * Z.shape[1]),
    phi_param_map=lambda Z: {'beta_' + str(i) : i for i in range(Z.shape[1])},
    baseline=[],
    phi_init=lambda Z: np.zeros(Z.shape[1])
)

# Parametric Proportional Hazard
WeibullPH = ProportionalHazardsFitter(
    'WeibullPH', 
    surv.Weibull,
    lambda Z, *params: np.exp(np.dot(Z, np.array(params))),
    lambda Z: (((None, None),) * Z.shape[1]),
    phi_param_map=lambda Z: {'beta_' + str(i) : i for i in range(Z.shape[1])},
    baseline=[],
    phi_init=lambda Z: np.zeros(Z.shape[1])
)


# Parametric AFT
WeibullInversePowerAFT = AcceleratedFailureTimeFitter(
    'WeibullInversePowerAFT', 
    surv.Weibull,
    InversePower
)
