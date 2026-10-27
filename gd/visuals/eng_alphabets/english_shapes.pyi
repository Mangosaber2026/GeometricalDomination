
#* 📝 File type: Python type stub (.pyi)
#* 📝 Purpose: Describes the module's interface for documentation,
#* 📝         editor support, and static type checking.
#* 📝 Runtime: Contains no implementation; see the corresponding
#* 📝         .py file for executable code.

import numbers as num  # noqa: I001

import turtle_extension as tx


class EngShapes:

    @staticmethod
    def plus(height: num.Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a plus with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """

    @staticmethod
    def equals(height: num.Real, tls: tx.ChainTurtle) -> None:
        """
        Draws an equal sign with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """

    @staticmethod
    def times(height: num.Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a multiplication sign with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """

    @staticmethod
    def minus(height: num.Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a minus sign with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """

    @staticmethod
    def underline(height: num.Real, tls: tx.ChainTurtle) -> None:
        """
        Draws an underline with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """

    @staticmethod
    def heart(height: num.Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a heart with given height and ChainTurtle

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """

    @staticmethod
    def star(height: num.Real, tls: tx.ChainTurtle) -> None:
        """
        Draws a star with given height and ChainTurtle.

        :param height: height of the letters

        :param tls: a ChainTurtle

        :return: None
        """