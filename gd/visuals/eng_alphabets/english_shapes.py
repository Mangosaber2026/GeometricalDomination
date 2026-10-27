# ⚓ Anchor for this module: [[english-shapes-anchor|english_shapes.py]] 

import uf

from .. import shapes
from . import english_alphabets_validators as eng_vls


# ⚓ Shapes anchor: [[EngShapes-anchor|class EngShapes]] 
#* 📝 Contains only the shapes, they are directly accessible through [[#Alphabets-anchor|Alphabets]] 
class EngShapes:
        """
        A collection of functions to draw shapes (and mathematical symbols).
        """

        # ⚓ plus anchor: [[EngShapes-plus-anchor|plus()]] 
        #* 📝 Draws a plus sign
        @staticmethod
        @eng_vls.alphabets_deco
        def plus(height, tls):     

            height_25 = uf.pct25(height)    
            height_50 = uf.pct50(height)    
            height_35 = uf.Percent(35)(height)
            (
                tls
                . rt(90)
                . fd_inv(height_25)
                . lt(90)
                . fd_inv(height_50)
                . rt(90)
            )
            shapes.Shapes.lines(height_25, 4, tls)
            (
                tls
                . fd_inv(height_35)
                . lt(90)
                .bk_inv(height_50)
            )


        # ⚓ equals anchor: [[EngShapes-equals-anchor|equals()]] 
        #* 📝 Draws an equal sign
        @staticmethod
        @eng_vls.alphabets_deco
        def equals(height, tls):     

            height_30 = uf.pct30(height)    
            height_50 = uf.pct50(height)    
            height_40 = uf.pct40(height)    
            height_60 = uf.pct60(height)    
            height_70 = uf.pct70(height)    
            (
                tls
                . fd_inv(height_30)
                . rt(90)
                . fd(height_50)
                . lt(90)
                . fd_inv(height_40)
                . lt(90)
                . fd(height_50)
                . bk_inv(height_60)
                . rt(90)
                . bk_inv(height_70)
            )


        # ⚓ times anchor: [[EngShapes-times-anchor|times()]] 
        #* 📝 Draws a multiplication sign
        @staticmethod
        @eng_vls.alphabets_deco
        def times(height, tls):     

            height_25 = uf.pct25(height)    
            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    

            side = uf.sine(45) * height_25
            (
                tls
                . fd_inv(height_50)
                . rt(90)
                . fd_inv(height_50)
                . rt(45)
            )
            shapes.Shapes.lines(height_25, 4, tls)
            (
                tls
                . lt(45)
                . fd_inv(side + height_10)
                . lt(90)
                . bk_inv(height_50)
            )


        # ⚓ minus anchor: [[EngShapes-minus-anchor|minus()]] 
        #* 📝 Draws a minus
        @staticmethod
        @eng_vls.alphabets_deco
        def minus(height, tls):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    
            (
                tls
                . fd_inv(height_50)
                . rt(90)
                . fd(height_50)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height_50)
            )


        # ⚓ underline anchor: [[EngShapes-underline-anchor|underline()]] 
        #* 📝 Draws an underline
        @staticmethod
        @eng_vls.alphabets_deco
        def underline(height, tls):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    

            (
                tls
                . rt(90)
                . fd(height_50)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ heart anchor: [[EngShapes-heart-anchor|heart()]] 
        #* 📝 Draws a heart shape
        @staticmethod
        @eng_vls.alphabets_deco
        def heart(height, tls):     

            height_60 = uf.pct60(height)    
            height_65 = uf.Percent(65)(height)
            height_32_5 = uf.Percent(32.5)(height)
            (
                tls
                . rt(90)
                . fd_inv(height_60)
                . lt(135)
                . begin_fill()
                . fd(height_65)

                .circle(-height_32_5, 180)
                .lt(90)
                .circle(-height_32_5, 180)

                .fd(height_65)
                .end_fill()
                .lt(135)
                .fd_inv(height_65)
                .lt(90)
            )


        # ⚓ star anchor: [[EngShapes-star-anchor|star()]] 
        #* 📝 Draws a star shape
        @staticmethod
        @eng_vls.alphabets_deco
        def star(height, tls):     

            direction = tls.heading()
            side = height / uf.sine(62)
            geo_fix = uf.Percent(-1e-05)(height)
            height_40 = uf.pct40(height)        
            (
                tls
                . rt(90)
                . fd_inv(height)
                . lt(90)
                . fd(geo_fix)
                . lt(17)
            )
            for _ in range(5):
                tls.fd(side).lt(144)

            (
                tls
                . seth(direction - 90)
                . fd(height_40)
                . lt(90)
            )