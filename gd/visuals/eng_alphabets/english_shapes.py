# ⚓ Anchor for this module: [[english-shapes-anchor|english_shapes.py]] 

import turtle_extension as tx
import uf

from ..premade_shapes import shapes
from . import english_alphabets_validators as eng_vls


# ⚓ Shapes anchor: [[EngShapes-anchor|class EngShapes]] 
#* 📝 Contains only the shapes, they are directly accessible through [[#EngAlphabets-anchor|EngAlphabets]] 
class EngShapes:
        """
        A collection of functions to draw shapes (and mathematical symbols).
        """

        # ⚓ plus anchor: [[EngShapes-plus-anchor|plus()]] 
        #* 📝 Draws a plus sign
        @staticmethod
        @eng_vls.alphabets_deco
        def plus(height, tls: tx.ChainTurtle):     

            height_25 = uf.pct25(height)    
            height_50 = uf.pct50(height)    
            height_35 = uf.Percent(35)(height)
            (
                tls
                . right(90)
                . fd_inv(height_25)
                . left(90)
                . fd_inv(height_50)
                . right(90)
            )
            shapes.Shapes.lines(height_25, 4, tls)
            (
                tls
                . fd_inv(height_35)
                . left(90)
                .bk_inv(height_50)
            )


        # ⚓ equals anchor: [[EngShapes-equals-anchor|equals()]] 
        #* 📝 Draws an equal sign
        @staticmethod
        @eng_vls.alphabets_deco
        def equals(height, tls: tx.ChainTurtle):     

            height_30 = uf.pct30(height)    
            height_50 = uf.pct50(height)    
            height_40 = uf.pct40(height)    
            height_60 = uf.pct60(height)    
            height_70 = uf.pct70(height)    
            (
                tls
                . fd_inv(height_30)
                . right(90)
                . forward(height_50)
                . left(90)
                . fd_inv(height_40)
                . left(90)
                . forward(height_50)
                . bk_inv(height_60)
                . right(90)
                . bk_inv(height_70)
            )


        # ⚓ times anchor: [[EngShapes-times-anchor|times()]] 
        #* 📝 Draws a multiplication sign
        @staticmethod
        @eng_vls.alphabets_deco
        def times(height, tls: tx.ChainTurtle):     

            height_25 = uf.pct25(height)    
            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    

            side = uf.sine(45) * height_25
            (
                tls
                . fd_inv(height_50)
                . right(90)
                . fd_inv(height_50)
                . right(45)
            )
            shapes.Shapes.lines(height_25, 4, tls)
            (
                tls
                . left(45)
                . fd_inv(side + height_10)                               # pyright: ignore[reportOperatorIssue, reportArgumentType]
                . left(90)
                . bk_inv(height_50)
            )


        # ⚓ minus anchor: [[EngShapes-minus-anchor|minus()]] 
        #* 📝 Draws a minus
        @staticmethod
        @eng_vls.alphabets_deco
        def minus(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    
            (
                tls
                . fd_inv(height_50)
                . right(90)
                . forward(height_50)
                . fd_inv(height_10)
                . left(90)
                . bk_inv(height_50)
            )


        # ⚓ underline anchor: [[EngShapes-underline-anchor|underline()]] 
        #* 📝 Draws an underline
        @staticmethod
        @eng_vls.alphabets_deco
        def underline(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    

            (
                tls
                . right(90)
                . forward(height_50)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ heart anchor: [[EngShapes-heart-anchor|heart()]] 
        #* 📝 Draws a heart shape
        @staticmethod
        @eng_vls.alphabets_deco
        def heart(height, tls: tx.ChainTurtle):     

            height_60 = uf.pct60(height)    
            height_65 = uf.Percent(65)(height)
            height_32_5 = uf.Percent(32.5)(height)
            (
                tls
                . right(90)
                . fd_inv(height_60)
                . left(135)
                . begin_fill()
                . forward(height_65)

                . circle(-height_32_5, 180)                              # pyright: ignore[reportArgumentType]
                . left(90)
                . circle(-height_32_5, 180)                              # pyright: ignore[reportArgumentType]

                . forward(height_65)
                . end_fill()
                . left(135)
                . fd_inv(height_65)
                . left(90)
            )


        # ⚓ star anchor: [[EngShapes-star-anchor|star()]] 
        #* 📝 Draws a star shape
        @staticmethod
        @eng_vls.alphabets_deco
        def star(height, tls: tx.ChainTurtle):     

            direction = tls.heading()
            side = height / uf.sine(62)
            geo_fix = uf.Percent(-1e-05)(height)
            height_40 = uf.pct40(height)        
            (
                tls
                . right(90)
                . fd_inv(height)
                . left(90)
                . forward(geo_fix)
                . left(17)
            )
            for _ in range(5):
                tls.forward(side).left(144)

            (
                tls
                . setheading(direction - 90)
                . forward(height_40)
                . left(90)
            )