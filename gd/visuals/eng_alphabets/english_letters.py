# ⚓ Anchor for this module: [[english-letters-anchor|english_letters.py]] 

import math

import turtle_extension as tx
import uf

from . import english_alphabets_validators as eng_vls


# ⚓ EngLetters anchor: [[EngLetters-anchor|class EngLetters]] 
#* 📝 Contains only the letters, they are directly accessible through [[#EngAlphabets-anchor|EngAlphabets]] 
class EngLetters:

        # ⚓ A anchor: [[Letters-A-anchor|A()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def A(height, tls: tx.ChainTurtle):     

            height_60 = uf.pct60(height)    
            height_40 = uf.pct40(height)    
            height_10 = uf.pct10(height)    

            a = height_60 / uf.sine(70)     
            b = height_40 / uf.sine(70)     
            c = 2 * math.sqrt(a ** 2 - height_60 ** 2)                  # pyright: ignore[reportOperatorIssue]

            (
                tls
                . right(20)
                . forward(b)                                            # pyright: ignore[reportArgumentType]
                . right(70)
                . forward(c)
                . backward(c)
                . left(70)
                . forward(a)                                            # pyright: ignore[reportArgumentType]
                . right(140)
                . forward(a + b)                                        # pyright: ignore[reportOperatorIssue]
                . left(70)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ B anchor: [[Letters-B-anchor|B()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def B(height, tls: tx.ChainTurtle):     

            height_20 = uf.pct20(height)    
            height_25 = uf.pct25(height)    
            height_50 = uf.pct50(height) 
               
            (
                tls.forward(height)
                . right(90)
                . forward(height_20)
                . circle(-height_25, 180)                               # pyright: ignore[reportArgumentType]
                . left(180)
                . circle(-height_25, 180)                               # pyright: ignore[reportArgumentType]
                . forward(height_20)
                . right(180)
                . fd_inv(height_50 + 5)                                 # pyright: ignore[reportArgumentType]
                . left(90)
             )
            

        # ⚓ C anchor: [[Letters-C-anchor|C()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def C(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    

            (
                tls
                . right(90)
                . fd_inv(height_50)
                . left(90)
                . fd_inv(height)
                . left(90)
                . circle(height_50, 180)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ D anchor: [[Letters-D-anchor|D()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def D(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)

            (
                tls
                . forward(height)
                . right(90)
                . circle(-height_50, 180)                               # pyright: ignore[reportArgumentType]
                . right(180)
                . fd_inv(height_50+10)                                  # pyright: ignore[reportArgumentType]
                . left(90)
            )


        # ⚓ E anchor: [[Letters-E-anchor|E()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def E(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)  

            (
                tls
                . right(90)
                . fd_inv(height_50)
                . left(90)
                . fd_inv(height)
            )
            for _ in range(3):
                tls.left(90).forward(height_50)

            (
                tls
                . backward(height_50)
                . right(90)
                . forward(height_50)
                . left(90)
                . forward(height_50)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ F anchor: [[Letters-F-anchor|F()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def F(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_60 = uf.pct60(height)  

            for _ in range(2):
                (
                    tls
                    . forward(height_50)
                    . right(90)
                    . forward(height_50)
                    . backward(height_50)
                    . left(90)
                )
            (
                tls
                . left(90)
                . bk_inv(height_60)
                . right(90)
                . bk_inv(height)
            )


        # ⚓ G anchor: [[Letters-G-anchor|G()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def G(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_30 = uf.pct30(height)        
            height_40 = uf.pct40(height)  

            (
                tls
                . right(90)
                . fd_inv(height_50)
                . left(90)
                . fd_inv(height)
                . left(90)
                . circle(height_50, 180).left(90)
                . forward(height_50)
                . left(90)
                . forward(height_30)
                . right(180)
                . fd_inv(height_40)
                . left(90)
                . bk_inv(height_50)
            )


        # ⚓ H anchor: [[Letters-H-anchor|H()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def H(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)  

            (
                tls
                . forward(height)
                . backward(height_50)
                . right(90)
                . forward(height_50)
                . left(90)
                . forward(height_50)
                . backward(height)
                . right(90)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ I anchor: [[Letters-I-anchor|I()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def I(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_25 = uf.pct25(height)    
            height_10 = uf.pct10(height)  

            (
                tls
                . right(90)
                . forward(height_50)
                . backward(height_25)
                . left(90)
                . forward(height)
                . right(90)
                . backward(height_25)
                . forward(height_50)
                . fd_inv(height_10)
                . left(90)
                . bk_inv(height)
            )


        # ⚓ J anchor: [[Letters-J-anchor|J()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def J(height, tls: tx.ChainTurtle):     

            height_60 = uf.pct60(height)    
            height_70 = uf.pct70(height)    
            height_30 = uf.pct30(height)       

            (
                tls
                . fd_inv(height)
                . right(90)
                . forward(height_60)
                . right(90)
                . forward(height_70)
                . circle(-height_30, 180)                               # pyright: ignore[reportArgumentType]
                . right(90)
                . fd_inv(height_70)
                . left(90)
                . bk_inv(height_30)
            )


        # ⚓ K anchor: [[Letters-K-anchor|K()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def K(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    
            diagonal = math.sqrt(height_50 ** 2 * 2)                    # pyright: ignore[reportOperatorIssue]

            (
                tls
                . forward(height)
                . backward(height_50)
                . right(45)
                . forward(diagonal)
                . backward(diagonal)
                . right(90)
                . forward(diagonal)
                . left(45)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ L anchor: [[Letters-L-anchor|L()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def L(height, tls: tx.ChainTurtle):     

            height_45 = uf.Percent(45)(height)    
            height_10 = uf.pct10(height)    
            (
                tls
                . forward(height)
                . backward(height)
                . right(90)
                . forward(height_45)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ M anchor: [[Letters-M-anchor|M()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def M(height, tls: tx.ChainTurtle):     

            diagonal = (height / uf.cosine(30)) / 2
            height_10 = uf.pct10(height)    

            (
                tls
                . forward(height)
                . right(150)
                . forward(diagonal)
                . left(120)
                . forward(diagonal)
                . right(150)
                . forward(height)
                . left(90)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ N anchor: [[Letters-N-anchor|N()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def N(height, tls: tx.ChainTurtle):     

            diagonal = height / uf.cosine(30)
            height_10 = uf.pct10(height)    

            (
                tls
                . forward(height)
                . right(150)
                . forward(diagonal)
                . left(150)
                . forward(height)
                . backward(height)
                . right(90)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ O anchor: [[Letters-O-anchor|O()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def O(height, tls: tx.ChainTurtle):     

            height_40 = uf.pct40(height)    
            height_20 = uf.pct20(height)    
            height_90 = uf.pct90(height)
            (
                tls
                . fd_inv(height_40)
                . right(180)
                . circle(height_40, 180)
                . forward(height_20)
                . circle(height_40, 180)
                . forward(height_20)
                . left(90)
                . fd_inv(height_90)
                . left(90)
                . bk_inv(height_40)
            )


        # ⚓ P anchor: [[Letters-P-anchor|P()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def P(height, tls: tx.ChainTurtle):     

            height_27 = uf.Percent(27)(height)
            height_37 = uf.Percent(37)(height)
            height_46 = uf.Percent(46)(height)
            (
                tls
                . forward(height)
                . right(90)
                . circle(-height_27, 180)                               # pyright: ignore[reportArgumentType]
                . right(180)
                . fd_inv(height_37)
                . left(90)
                . bk_inv(height_46)
            )


        # ⚓ Q anchor: [[Letters-Q-anchor|Q()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def Q(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_35 = uf.Percent(35)(height)
            height_10 = uf.pct10(height)    

            side_a = math.sqrt(height_35 ** 2 + height_50 ** 2)         # pyright: ignore[reportOperatorIssue]
            turn_right = uf.asine(height_50 / side_a)                   # pyright: ignore[reportArgumentType]

            (
                tls
                . right(90)
                . fd_inv(height_50)
                . circle(height_50, 360)
                . left(90)
                . fd_inv(height_35)
                . right(180 - turn_right)                               # pyright: ignore[reportArgumentType]
                . forward(side_a)
                . left(90 - turn_right)                                 # pyright: ignore[reportArgumentType]
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ R anchor: [[Letters-R-anchor|R()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def R(height, tls: tx.ChainTurtle):     

            height_27 = uf.Percent(27)(height)
            height_46 = uf.Percent(46)(height)
            height_10 = uf.pct10(height)    
            (
                tls
                . forward(height)
                . right(90)
                . circle(-height_27, 180)                               # pyright: ignore[reportArgumentType]
                . left(120)
                . forward(height_46 / uf.sine(60))                      # pyright: ignore[reportArgumentType]
                . left(60)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ S anchor: [[Letters-S-anchor|S()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def S(height, tls: tx.ChainTurtle):     

            height_27 = uf.Percent(27)(height)
            height_54 = uf.Percent(54)(height)
            height_37 = uf.Percent(37)(height)
            arc_70 = uf.pct70(360)
            arc_30 = uf.pct30(360)

            geo_fix = uf.sine(20) - uf.sine(272)
            radius = height_27

            (
                tls
                . right(90)
                . fd_inv(height_54)
                . left(90)
                . fd_inv(height_54 + geo_fix * radius)                  # pyright: ignore[reportArgumentType, reportOperatorIssue]
                . left(20)
                . circle(radius, arc_70)
                . circle(-radius, arc_70)                               # pyright: ignore[reportArgumentType]
                . penup()
                . circle(-radius, arc_30)                               # pyright: ignore[reportArgumentType]
                . right(2)
                . forward(height_37)
                . left(90)
                . backward(height_54)
                . pendown()
            )


        # ⚓ T anchor: [[Letters-T-anchor|T()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def T(height, tls: tx.ChainTurtle):     

            height_45 = uf.Percent(45)(height)    
            height_90 = uf.pct90(height)
            height_10 = uf.pct10(height)    
            (
                tls
                . right(90)
                . fd_inv(height_45)
                . left(90)
                . forward(height)
                . left(90)
                . forward(height_45)
                . backward(height_90)
                . bk_inv(height_10)
                . right(90)
                . bk_inv(height)
            )


        # ⚓ U anchor: [[Letters-U-anchor|U()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def U(height, tls: tx.ChainTurtle):     

            height_70 = uf.pct70(height)    
            height_30 = uf.pct30(height)        
            height_10 = uf.pct10(height)    
            (
                tls
                . fd_inv(height)
                . right(180)
                . forward(height_70)
                . circle(height_30, 180)
                . forward(height_70)
                . right(90)
                . fd_inv(height_10)
                . left(90)
                . bk_inv(height)
            )


        # ⚓ V anchor: [[Letters-V-anchor|V()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def V(height, tls: tx.ChainTurtle):     

            height_10 = uf.pct10(height)    
            diagonal = height / uf.sine(65)
            (
                tls
                . fd_inv(height)
                . right(155)
                . forward(diagonal)
                . left(130)
                . forward(diagonal)
                . right(65)
                . fd_inv(height_10)
                . left(90)
                . bk_inv(height)
            )


        # ⚓ W anchor: [[Letters-W-anchor|W()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def W(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    

            side_a = height / uf.sine(75)
            side_c = height_50 / uf.sine(75)

            (
                tls
                . fd_inv(height)
                . right(165)
                . forward(side_a)
                . left(150)

                . forward(side_c)                                       # pyright: ignore[reportArgumentType]
                . right(150)
                . forward(side_c)                                       # pyright: ignore[reportArgumentType]
                . left(150)
                . forward(side_a)

                . right(75)
                . fd_inv(height_10)
                . left(90)
                . bk_inv(height)
            )


        # ⚓ X anchor: [[Letters-X-anchor|X()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def X(height, tls: tx.ChainTurtle):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    

            a_half = height_50 / uf.sine(55)
            a_full = a_half * 2                                         # pyright: ignore[reportOperatorIssue]
            side_b = math.sqrt(a_half ** 2 - height_50 ** 2)            # pyright: ignore[reportOperatorIssue]
            (
                tls
                . right(35)
                . forward(a_full)
                . left(125)
                . fd_inv(side_b * 2)
                . left(125)
                . forward(a_full)
                . left(55)
                . fd_inv(height_10)
                . left(90)
            )


        # ⚓ Y anchor: [[Letters-Y-anchor|Y()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def Y(height, tls: tx.ChainTurtle):     

            height_40 = uf.pct40(height)    
            height_60 = uf.pct60(height)    
            height_10 = uf.pct10(height)    

            side = height_40 / uf.sine(55)
            width = math.sqrt(side ** 2 - height_40 ** 2)               # pyright: ignore[reportOperatorIssue]

            (
                tls
                . right(90)
                . fd_inv(width)
                . left(90)
                . forward(height_60)
                . right(35)
                . forward(side)                                         # pyright: ignore[reportArgumentType]

                . backward(side)                                        # pyright: ignore[reportArgumentType]
                . left(70)
                . forward(side)                                         # pyright: ignore[reportArgumentType]
                . right(35)
                . bk_inv(height)
                . right(90)
                . fd_inv(2 * width + height_10)                         # pyright: ignore[reportArgumentType]
                . left(90)
            )


        # ⚓ Z anchor: [[Letters-Z-anchor|Z()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def Z(height, tls: tx.ChainTurtle):     

            height_10 = uf.pct10(height)    

            side_a = height / uf.sine(50)
            side_b = math.sqrt(side_a ** 2 - height ** 2)

            (
                tls
                . fd_inv(height)
                . right(90)
                . forward(side_b)
                . right(130)
                . forward(side_a)
                . left(130)
                . forward(side_b)
                . fd_inv(height_10)
                . left(90)
            )