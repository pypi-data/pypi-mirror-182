import typing as t
from gettext import gettext as _
import types
import inspect

from click.utils import echo
from click.decorators import option
from click.core import Context
from click.core import Parameter
from click.decorators import FC


def man_option(
        *param_decls: str,
        **kwargs: t.Any,
) -> t.Callable[[FC], FC]:
    """
    """
    message = _("%(prog)s, version %(version)s")

    def callback(ctx: Context, param: Parameter, value: bool) -> None:
        if not value or ctx.resilient_parsing:
            return

        echo(message, color=ctx.color)
        ctx.exit()

    if not param_decls:
        param_decls = ("--man",)

    kwargs.setdefault("is_flag", True)
    kwargs.setdefault("expose_value", False)
    kwargs.setdefault("is_eager", True)
    kwargs.setdefault("help", _("Show the man page and exit."))
    kwargs["callback"] = callback
    return option(*param_decls, **kwargs)