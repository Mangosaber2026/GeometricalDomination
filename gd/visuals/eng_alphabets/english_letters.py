# ⚓ Anchor for this module: [[english-letters-anchor|english_letters.py]] 

import math

import uf

from . import english_alphabets_validators as eng_vls


# ⚓ Letters anchor: [[Letters-anchor|class Letters]] 
#* 📝 Contains only the letters, they are directly accessible through [[#Alphabets-anchor|Alphabets]] 
class Letters:

        # ⚓ A anchor: [[Letters-A-anchor|A()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def A(height, tls):     

            height_60 = uf.pct60(height)    
            height_40 = uf.pct40(height)    
            height_10 = uf.pct10(height)    

            a = height_60 / uf.sine(70)     
            b = height_40 / uf.sine(70)     
            c = 2 * math.sqrt(a ** 2 - height_60 ** 2)

            (
                tls
                . rt(20)
                . fd(b)
                . rt(70)
                . fd(c)
                . bk(c)
                . lt(70)
                . fd(a)
                . rt(140)
                . fd(a + b)
                . lt(70)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ B anchor: [[Letters-B-anchor|B()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def B(height, tls):     

            height_20 = uf.pct20(height)    
            height_25 = uf.pct25(height)    
            height_50 = uf.pct50(height)    
            (
                tls.fd(height)
                . rt(90)
                . fd(height_20)
                . circle(-height_25, 180)
                . lt(180)
                . circle(-height_25, 180)
                . fd(height_20)
                . rt(180)
                . fd_inv(height_50+5)
                . lt(90)
             )
            

        # ⚓ C anchor: [[Letters-C-anchor|C()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def C(height, tls):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    
            (
                tls
                . rt(90)
                . fd_inv(height_50)
                . lt(90)
                . fd_inv(height)
                . lt(90)
                . circle(height_50, 180)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ D anchor: [[Letters-D-anchor|D()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def D(height, tls):     

            height_50 = uf.pct50(height)    
            (
                tls
                . fd(height)
                . rt(90)
                . circle(-height_50, 180)
                . rt(180)
                . fd_inv(height_50+10)
                . lt(90)
            )


        # ⚓ E anchor: [[Letters-E-anchor|E()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def E(height, tls):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    
            (
                tls
                . rt(90)
                . fd_inv(height_50)
                . lt(90)
                . fd_inv(height)
            )
            for _ in range(3):
                tls.lt(90).fd(height_50)

            (
                tls
                . bk(height_50)
                . rt(90)
                . fd(height_50)
                . lt(90)
                . fd(height_50)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ F anchor: [[Letters-F-anchor|F()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def F(height, tls):     

            height_50 = uf.pct50(height)    
            height_60 = uf.pct60(height)    
            for _ in range(2):
                (
                    tls
                    . fd(height_50)
                    . rt(90)
                    . fd(height_50)
                    . bk(height_50)
                    . lt(90)
                )
            (
                tls
                . lt(90)
                . bk_inv(height_60)
                . rt(90)
                . bk_inv(height)
            )


        # ⚓ G anchor: [[Letters-G-anchor|G()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def G(height, tls):     

            height_50 = uf.pct50(height)    
            height_30 = uf.pct30(height)        
            height_40 = uf.pct40(height)    
            (
                tls
                . rt(90)
                . fd_inv(height_50)
                . lt(90)
                . fd_inv(height)
                . lt(90)
                . circle(height_50, 180).lt(90)
                . fd(height_50)
                . lt(90)
                . fd(height_30)
                . rt(180)
                . fd_inv(height_40)
                . lt(90)
                . bk_inv(height_50)
            )


        # ⚓ H anchor: [[Letters-H-anchor|H()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def H(height, tls):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    
            (
                tls
                . fd(height)
                . bk(height_50)
                . rt(90)
                . fd(height_50)
                . lt(90)
                . fd(height_50)
                . bk(height)
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ I anchor: [[Letters-I-anchor|I()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def I(height, tls):     

            height_50 = uf.pct50(height)    
            height_25 = uf.pct25(height)    
            height_10 = uf.pct10(height)    
            (
                tls
                . rt(90)
                . fd(height_50)
                . bk(height_25)
                . lt(90)
                . fd(height)
                . rt(90)
                . bk(height_25)
                . fd(height_50)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height)
            )


        # ⚓ J anchor: [[Letters-J-anchor|J()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def J(height, tls):     

            height_60 = uf.pct60(height)    
            height_70 = uf.pct70(height)    
            height_30 = uf.pct30(height)        
            (
                tls
                . fd_inv(height)
                . rt(90)
                . fd(height_60)
                . rt(90)
                . fd(height_70)
                . circle(-height_30, 180)
                . rt(90)
                . fd_inv(height_70)
                . lt(90)
                . bk_inv(height_30)
            )


        # ⚓ K anchor: [[Letters-K-anchor|K()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def K(height, tls):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    
            diagonal = math.sqrt(height_50 ** 2 * 2)

            (
                tls
                . fd(height)
                . bk(height_50)
                . rt(45)
                . fd(diagonal)
                . bk(diagonal)
                . rt(90)
                . fd(diagonal)
                . lt(45)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ L anchor: [[Letters-L-anchor|L()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def L(height, tls):     

            height_45 = uf.Percent(45)(height)    
            height_10 = uf.pct10(height)    
            (
                tls
                . fd(height)
                . bk(height)
                . rt(90)
                . fd(height_45)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ M anchor: [[Letters-M-anchor|M()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def M(height, tls):     

            diagonal = (height / uf.cosine(30)) / 2
            height_10 = uf.pct10(height)    

            (
                tls
                . fd(height)
                . rt(150)
                . fd(diagonal)
                . lt(120)
                . fd(diagonal)
                . rt(150)
                . fd(height)
                . lt(90)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ N anchor: [[Letters-N-anchor|N()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def N(height, tls):     

            diagonal = height / uf.cosine(30)
            height_10 = uf.pct10(height)    

            (
                tls
                . fd(height)
                . rt(150)
                . fd(diagonal)
                . lt(150)
                . fd(height)
                . bk(height)
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ O anchor: [[Letters-O-anchor|O()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def O(height, tls):     

            height_40 = uf.pct40(height)    
            height_20 = uf.pct20(height)    
            height_90 = uf.pct90(height)
            (
                tls
                . fd_inv(height_40)
                . rt(180)
                . circle(height_40, 180)
                . fd(height_20)
                . circle(height_40, 180)
                . fd(height_20)
                . lt(90)
                . fd_inv(height_90)
                . lt(90)
                . bk_inv(height_40)
            )


        # ⚓ P anchor: [[Letters-P-anchor|P()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def P(height, tls):     

            height_27 = uf.Percent(27)(height)
            height_37 = uf.Percent(37)(height)
            height_46 = uf.Percent(46)(height)
            (
                tls
                . fd(height)
                . rt(90)
                . circle(-height_27, 180)
                . rt(180)
                . fd_inv(height_37)
                . lt(90)
                . bk_inv(height_46)
            )


        # ⚓ Q anchor: [[Letters-Q-anchor|Q()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def Q(height, tls):     

            height_50 = uf.pct50(height)    
            height_35 = uf.Percent(35)(height)
            height_10 = uf.pct10(height)    

            side_a = math.sqrt(height_35 ** 2 + height_50 ** 2)
            turn_right = uf.asine(height_50 / side_a)

            (
                tls
                . rt(90)
                . fd_inv(height_50)
                . circle(height_50, 360)
                . lt(90)
                . fd_inv(height_35)
                . rt(180 - turn_right)
                . fd(side_a)
                . lt(90 - turn_right)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ R anchor: [[Letters-R-anchor|R()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def R(height, tls):     

            height_27 = uf.Percent(27)(height)
            height_46 = uf.Percent(46)(height)
            height_10 = uf.pct10(height)    
            (
                tls
                . fd(height)
                . rt(90)
                . circle(-height_27, 180)
                . lt(120)
                . fd(height_46 / uf.sine(60))
                . lt(60)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ S anchor: [[Letters-S-anchor|S()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def S(height, tls):     

            height_27 = uf.Percent(27)(height)
            height_54 = uf.Percent(54)(height)
            height_37 = uf.Percent(37)(height)
            arc_70 = uf.pct70(360)
            arc_30 = uf.pct30(360)

            geo_fix = uf.sine(20) - uf.sine(272)
            radius = height_27

            (
                tls
                . rt(90)
                . fd_inv(height_54)
                . lt(90)
                . fd_inv(height_54 + geo_fix * radius)
                . lt(20)
                . circle(radius, arc_70)
                . circle(-radius, arc_70)
                . pu()
                . circle(-radius, arc_30)
                . rt(2)
                . fd(height_37)
                . lt(90)
                . bk(height_54)
                . pd()
            )


        # ⚓ T anchor: [[Letters-T-anchor|T()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def T(height, tls):     

            height_45 = uf.Percent(45)(height)    
            height_90 = uf.pct90(height)
            height_10 = uf.pct10(height)    
            (
                tls
                . rt(90)
                . fd_inv(height_45)
                . lt(90)
                . fd(height)
                . lt(90)
                . fd(height_45)
                . bk(height_90)
                . bk_inv(height_10)
                . rt(90)
                . bk_inv(height)
            )


        # ⚓ U anchor: [[Letters-U-anchor|U()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def U(height, tls):     

            height_70 = uf.pct70(height)    
            height_30 = uf.pct30(height)        
            height_10 = uf.pct10(height)    
            (
                tls
                . fd_inv(height)
                . rt(180)
                . fd(height_70)
                . circle(height_30, 180)
                . fd(height_70)
                . rt(90)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height)
            )


        # ⚓ V anchor: [[Letters-V-anchor|V()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def V(height, tls):     

            height_10 = uf.pct10(height)    
            diagonal = height / uf.sine(65)
            (
                tls
                . fd_inv(height)
                . rt(155)
                . fd(diagonal)
                . lt(130)
                . fd(diagonal)
                . rt(65)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height)
            )


        # ⚓ W anchor: [[Letters-W-anchor|W()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def W(height, tls):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    

            side_a = height / uf.sine(75)
            side_c = height_50 / uf.sine(75)

            (
                tls
                . fd_inv(height)
                . rt(165)
                . fd(side_a)
                . lt(150)

                . fd(side_c)
                . rt(150)
                . fd(side_c)
                . lt(150)
                . fd(side_a)

                . rt(75)
                . fd_inv(height_10)
                . lt(90)
                . bk_inv(height)
            )


        # ⚓ X anchor: [[Letters-X-anchor|X()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def X(height, tls):     

            height_50 = uf.pct50(height)    
            height_10 = uf.pct10(height)    

            a_half = height_50 / uf.sine(55)
            a_full = a_half * 2
            side_b = math.sqrt(a_half ** 2 - height_50 ** 2)
            (
                tls
                . rt(35)
                . fd(a_full)
                . lt(125)
                . fd_inv(side_b * 2)
                . lt(125)
                . fd(a_full)
                . lt(55)
                . fd_inv(height_10)
                . lt(90)
            )


        # ⚓ Y anchor: [[Letters-Y-anchor|Y()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def Y(height, tls):     

            height_40 = uf.pct40(height)    
            height_60 = uf.pct60(height)    
            height_10 = uf.pct10(height)    

            side = height_40 / uf.sine(55)
            width = math.sqrt(side ** 2 - height_40 ** 2)

            (
                tls
                . rt(90)
                . fd_inv(width)
                . lt(90)
                . fd(height_60)
                . rt(35)
                . fd(side)

                .bk(side)
                .lt(70)
                .fd(side)
                .rt(35)
                .bk_inv(height)
                .rt(90)
                .fd_inv(2 * width + height_10)
                .lt(90)
            )


        # ⚓ Z anchor: [[Letters-Z-anchor|Z()]] 
        @staticmethod
        @eng_vls.alphabets_deco
        def Z(height, tls):     

            height_10 = uf.pct10(height)    

            side_a = height / uf.sine(50)
            side_b = math.sqrt(side_a ** 2 - height ** 2)

            (
                tls
                . fd_inv(height)
                . rt(90)
                . fd(side_b)
                . rt(130)
                . fd(side_a)
                . lt(130)
                . fd(side_b)
                . fd_inv(height_10)
                . lt(90)
            )