# ⚓ Anchor for this module: [[english-punctuations-anchor|english_punctuations.py]] 

import uf

from .. import shapes
from . import english_alphabets_validators as eng_vls


# ⚓ Punctuation anchor: [[Punctuation-anchor|class Punctuation]] 
#* 📝 Contains only the punctuations, they are directly accessible through [[#Alphabets-anchor|Alphabets]] 
class Punctuation:
        """
        A collection of functions to draw English punctuation marks.
        """

        # ⚓ space anchor: [[#Punctuation-space-anchor|space()]] 
        #* 📝 Draws a space
        @staticmethod
        @eng_vls.alphabets_deco
        def space(height, tls):     

            height_25 = uf.pct25(height)    
            tls.rt(90).fd_inv(height_25).lt(90)


        # ⚓ dot anchor: [[#Punctuation-dot-anchor|dot()]] 
        #* 📝 Draws a dot
        @staticmethod
        @eng_vls.alphabets_deco
        def dot(height, tls):     

            height_5 = uf.Percent(5)(height)    
            height_10 = uf.pct10(height)    
            height_15 = uf.Percent(15)(height)    
            (
                tls
                . rt(90)
                . fd_inv(height_5)
                . dot(height_10)
                . fd_inv(height_15)
                . lt(90)
            )


        # ⚓ exclamation anchor: [[#Punctuation-exclamation-anchor|exclamation()]] 
        #* 📝 Draws an exclamation mark
        @staticmethod
        @eng_vls.alphabets_deco
        def exclamation(height, tls):     

            height_20 = uf.pct20(height)    
            height_10 = uf.pct10(height)    
            height_5 = uf.Percent(5)(height)
            height_80 = uf.pct80(height)    

            tls.fd_inv(height_20)
            shapes.Shapes.rectangle_fill(height_80, height_10, -1, tls)

            (
                tls
                . lt(180)
                . fd_inv(height_10)
                . circle_fill(height_5, 540)
                . bk_inv(height_5)
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ question anchor: [[#Punctuation-question-anchor|question()]] 
        #* 📝 Draws a question mark
        @staticmethod
        @eng_vls.alphabets_deco
        def question(height, tls):     

            height_10 = uf.pct10(height)    
            height_25 = uf.pct25(height)    
            height_fifth = uf.pct20(height)    
            (
                tls
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
                . fd_inv(height)
                . lt(36)
                . begin_fill()

                . fd(height_10)
                . rt(90)
                . circle(-height_fifth, 216)
                .circle(height_fifth, 216)
                .rt(90)
                .fd(height_10)
                .rt(90)
                .circle(-height_fifth, 216)
                .circle(height_fifth, 216)

                .end_fill()
                .lt(54)
                .fd_inv(height)
                .lt(90)
                .fd_inv(height_10)
                .dot(height_10)
                .fd_inv(height_25)
                .lt(90)
            )


        # ⚓ apostrophe anchor: [[#Punctuation-apostrophe-anchor|apostrophe()]] 
        #* 📝 Draws an apostrophe
        @staticmethod
        @eng_vls.alphabets_deco
        def apostrophe(height, tls):     

            height_70 = uf.pct70(height)    
            height_30 = uf.pct30(height)        
            height_5 = uf.Percent(5)(height)    
            height_15 = uf.Percent(15)(height)    

            tls.fd_inv(height_70)

            shapes.Shapes.rectangle_fill(height_30, height_5, -1, tls)

            tls.rt(90).fd_inv(height_15).lt(90).bk_inv(height_70)


        # ⚓ colon anchor: [[#Punctuation-colon-anchor|colon()]] 
        #* 📝 Draws a colon
        @staticmethod
        @eng_vls.alphabets_deco
        def colon(height, tls):     

            height_7 = uf.Percent(7)(height)    
            height_28 = uf.Percent(28)(height)    
            height_17 = uf.Percent(17)(height)    
            (
                tls
                . rt(90)
                . fd_inv(height_7)
                . circle_fill(height_7, 360)
                . lt(90)
                . fd_inv(height_28)

                .rt(90)
                .circle_fill(height_7, 360)
                .fd_inv(height_17)
                .lt(90)
                .bk_inv(height_28)
            )


        # ⚓ comma anchor: [[#Punctuation-comma-anchor|comma()]] 
        #* 📝 Draws a comma
        @staticmethod
        @eng_vls.alphabets_deco
        def comma(height, tls):     

            height_5 = uf.Percent(5)(height)    
            height_1 = uf.Percent(1)(height)
            height_15 = uf.Percent(15)(height)    
            (
                tls
                . begin_fill()
                . rt(180)
                . fd(height_5)
                . circle(-height_5, 90)
                . lt(90)
                . fd(height_5)
                . lt(90)

                . circle(height_1, 90)
                . fd(height_5)
                . lt(90)
                . fd(height_5)
                . end_fill()
                . rt(180)
                . fd_inv(height_15)
                . lt(90)
            )