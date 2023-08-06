from typing import Dict, Any, Union
import yaml
import re
import os
import copy


class Namespace(dict):
    """Simple object for storing attributes.

    Implements equality by attribute names and values, and provides a simple
    string representation.
    """

    def __init__(self, **kwargs):
        for name in kwargs:
            setattr(self, name, kwargs[name])

    def __eq__(self, other):
        if not isinstance(other, Namespace):
            return NotImplemented
        return vars(self) == vars(other)

    def __contains__(self, key):
        return key in self.__dict__

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __repr__(self):
        type_name = type(self).__name__
        arg_strings = []
        star_args = {}
        for arg in self._get_args():
            arg_strings.append(repr(arg))
        for name, value in self._get_kwargs():
            if name.isidentifier():
                arg_strings.append("%s=%r" % (name, value))
            else:
                star_args[name] = value
        if star_args:
            arg_strings.append("**%s" % repr(star_args))
        return "%s(%s)" % (type_name, ", ".join(arg_strings))

    def __len__(self) -> int:
        return len(self.keys())

    def _get_kwargs(self):
        return list(self.__dict__.items())

    def _get_args(self):
        return []

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def copy(self):
        return copy.deepcopy(self)

    def to_dict(self):
        def _to_dict_recursive(d: Any):
            if isinstance(d, Namespace):
                d = d.__dict__
                for k, v in d.items():
                    d[k] = _to_dict_recursive(v)
            return d

        cvt_dict = self.copy()
        cvt_dict = _to_dict_recursive(cvt_dict)
        return cvt_dict


def to_namespace(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = to_namespace(v)
        elif isinstance(v, str):
            d[k] = v
    return Namespace(**d)


def load_yaml_config(
    file_path: str, env: str, to_args: bool = True, verbose: bool = False
) -> Namespace:
    """Load yaml configuration file
    For example:
    ```
        default: &default
            mysql_user: Xxx
            mysql_password: Xxx
            mysql_host: 0.0.0.0
            mysql_port: 3306

        development:
            <<: *default

        local:
            <<: *default

        production:
            <<: *default

        staging:
            <<: *default
    ```
    Args:
        file_path (str): file to path
        to_args (bool, optional): return Namespace. Defaults to True.
        verbose (bool, optional): verbose. Defaults to True.
    """
    assert env in ["default", "production", "development", "local", "staging"]
    if verbose:
        print("> Load yaml config file from", file_path)
    with open(file_path, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    data = data[env]
    return to_namespace(data)


def set_as_environment_variables(
    d: Union[Dict[Any, Any], Namespace], override: bool = True
) -> bool:
    """
    Load the current dotenv as system environment variable.
    """
    if type(d) not in [dict, Namespace]:
        return False

    if isinstance(d, Namespace):
        d = d.to_dict()

    for k, v in d.items():
        if k in os.environ and not override:
            continue
        if v is not None:
            os.environ[k] = str(v)
    return True


def load_query_from_file(file_path):
    """Load query from file

    Args:
        file_path (str): file to path
    """
    with open(file_path, "r") as f:
        query_str = f.read()
    query_str = re.sub("\n+", " ", query_str)
    query_str = re.sub("\s+", " ", query_str)
    return query_str
