from typing import Dict, Generic, Literal, Tuple, Type, TypeVar

import casadi as cs

T = TypeVar("T", cs.SX, cs.MX)


class HasParameters(Generic[T]):
    """Class for creating and storing symbolic parameters of an NLP problem."""

    def __init__(self, sym_type: Literal["SX", "MX"] = "SX") -> None:
        """Instantiate the class.

        Parameters
        ----------
        sym_type : "SX" or "MX", optional
            The CasADi symbolic variable type to use in the NLP, by default "SX".
        """
        super().__init__()
        self._csXX: Type[T] = getattr(cs, sym_type)
        self._pars: Dict[str, T] = {}
        self._p = self._csXX()

    @property
    def p(self) -> T:
        """Gets the parameters of the NLP scheme."""
        return self._p

    @property
    def np(self) -> int:
        """Number of parameters in the NLP scheme."""
        return self._p.shape[0]

    @property
    def parameters(self) -> Dict[str, T]:
        """Gets the parameters of the NLP scheme."""
        return self._pars

    def parameter(self, name: str, shape: Tuple[int, int] = (1, 1)) -> T:
        """Adds a parameter to the NLP scheme.

        Parameters
        ----------
        name : str
            Name of the new parameter. Must not be already in use.
        shape : tuple[int, int], optional
            Shape of the new parameter. By default, a scalar.

        Returns
        -------
        casadi.SX or MX
            The symbol for the new parameter.

        Raises
        ------
        ValueError
            Raises if there is already another parameter with the same name.
        """
        if name in self._pars:
            raise ValueError(f"Parameter name '{name}' already exists.")
        par = self._csXX.sym(name, *shape)
        self._pars[name] = par
        self._p = cs.vertcat(self._p, cs.vec(par))
        return par
