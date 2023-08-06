# threatmodel
> Agile Threat Modeling as Code

## Install
```bash
pip install threatmodel
```

## How to use
```bash
python3 threatmodel.py
```

```python
#!/usr/bin/env python3

import threatmodel as tm
import threatmodel.plus as tm_plus

model = tm.Model("REST Login Model")

user = tm_plus.Browser(model, "User")

login_process = tm.Process(
    model,
    "WebApi",
    machine=tm.Machine.VIRTUAL,
    technology=tm.Technology.WEB_SERVICE_REST,
)

login = tm.DataFlow(
    model,
    "Login",
    user,
    login_process,
    protocol=tm.Protocol.HTTPS,
)

login.sends(tm.Data("LoginRequest"))
login.receives(tm.Data("LoginResponse"))

database = tm.DataStore(
    model,
    "Database",
    machine=tm.Machine.VIRTUAL,
    technology=tm.Technology.DATABASE,
)

authenticate= tm.DataFlow(
    model,
    "Authenticate",
    login_process,
    database ,
    protocol=tm.Protocol.SQL_ACCESS_PROTOCOL,
)

authenticate.sends(tm.Data("AuthenticateUserQuery"))
authenticate.receives(tm.Data("AuthenticateUserQueryResult"))

result = model.evaluate()

with open("example.pu","w+") as f:
    f.write(result.sequence_diagram())

print(result.risks_table(table_format=tm.TableFormat.GITHUB))
```
Output:
| SID              | Severity   | Category                   | Name             | Affected   | Treatment   |
|------------------|-------------|----------------------------|------------------|------------|-------------|
| CAPEC-100@WebApi | high        | Manipulate Data Structures | Overflow Buffers | WebApi     | unchecked   |
| CAPEC-66@WebApi  | elevated    | Inject Unexpected Items    | SQL Injection    | WebApi     | unchecked   |
|...|...|...|...|...|...|

## Jupyter Threatbook
> Threatmodeling with jupyter notebooks

![threatbook.png](https://github.com/hupe1980/threatmodel/raw/main/.assets/threatbook.png)

## Generating Diagrams
```python
result = model.evaluate()

with open("example.pu","w+") as f:
    f.write(result.sequence_diagram())
```
![threatbook.png](https://github.com/hupe1980/threatmodel/raw/main/.assets/sequence-diagram.png)

## High level elements (threatmodel/plus*)
```python
import threatmodel.plus_aws as tm_plus_aws

# ...

alb = tm_plus_aws.ApplicationLoadBalancer(model, "ALB", waf=True)

```

## Custom threatlib
```python
import threatmodel as tm

threatlib = tm.Threatlib()

threatlib.add_threat("""... your custom threats ...""")

model = tm.Model("Demo Model", threatlib=threatlib)
```
## Examples

See more complete [examples](https://github.com/hupe1980/threatmodel/tree/master/examples).

## Prior work and other related projects
- [pytm](https://github.com/izar/pytm) - A Pythonic framework for threat modeling
- [threagile](https://github.com/Threagile/threagile) - Agile Threat Modeling Toolkit
- [cdk-threagile](https://github.com/hupe1980/cdk-threagile) - Agile Threat Modeling as Code

## License

[MIT](LICENSE)