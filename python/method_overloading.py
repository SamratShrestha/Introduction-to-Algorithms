from functools import singledispatch
from datetime import datetime
from numbers import Real

@singledispatch
def report(value):
    return f"raw: {value}"

@report.register
def _(value: datetime):
    return f"dt: {value.isoformat()}"

@report.register(complex)
def _(value):
    return f"complex: {value.real}{value.imag:+}j"

@report.register(Real)
def _(value):
    return f"real: {value:f}"


print(report(datetime.now()))
print(report('test'))
print(report(100-30j))
