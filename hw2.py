#!/usr/bin/env python
# -*- coding: utf-8 -*-
store=5000
money=input('How much will you want to withdraw:')
balance=store-money
if balance<0:
	print u' 您的餘額不足!'
elif balance==0:
	print u' 您的存款無剩餘存款'
else:
	print u' 您的存款還剩%d元'%balance
f=open("ATM.txt","a")
f.write("餘額剩下:%d\n"%balance)

u s a g e :   g i t   [ - - v e r s i o n ]   [ - - h e l p ]   [ - C   < p a t h > ]   [ - c   n a m e = v a l u e ]  
                       [ - - e x e c - p a t h [ = < p a t h > ] ]   [ - - h t m l - p a t h ]   [ - - m a n - p a t h ]   [ - - i n f o - p a t h ]  
                       [ - p   |   - - p a g i n a t e   |   - - n o - p a g e r ]   [ - - n o - r e p l a c e - o b j e c t s ]   [ - - b a r e ]  
                       [ - - g i t - d i r = < p a t h > ]   [ - - w o r k - t r e e = < p a t h > ]   [ - - n a m e s p a c e = < n a m e > ]  
                       < c o m m a n d >   [ < a r g s > ]  
  
 T h e s e   a r e   c o m m o n   G i t   c o m m a n d s   u s e d   i n   v a r i o u s   s i t u a t i o n s :  
  
 s t a r t   a   w o r k i n g   a r e a   ( s e e   a l s o :   g i t   h e l p   t u t o r i a l )  
       c l o n e             C l o n e   a   r e p o s i t o r y   i n t o   a   n e w   d i r e c t o r y  
       i n i t               C r e a t e   a n   e m p t y   G i t   r e p o s i t o r y   o r   r e i n i t i a l i z e   a n   e x i s t i n g   o n e  
  
 w o r k   o n   t h e   c u r r e n t   c h a n g e   ( s e e   a l s o :   g i t   h e l p   e v e r y d a y )  
       a d d                 A d d   f i l e   c o n t e n t s   t o   t h e   i n d e x  
       m v                   M o v e   o r   r e n a m e   a   f i l e ,   a   d i r e c t o r y ,   o r   a   s y m l i n k  
       r e s e t             R e s e t   c u r r e n t   H E A D   t o   t h e   s p e c i f i e d   s t a t e  
       r m                   R e m o v e   f i l e s   f r o m   t h e   w o r k i n g   t r e e   a n d   f r o m   t h e   i n d e x  
  
 e x a m i n e   t h e   h i s t o r y   a n d   s t a t e   ( s e e   a l s o :   g i t   h e l p   r e v i s i o n s )  
       b i s e c t           F i n d   b y   b i n a r y   s e a r c h   t h e   c h a n g e   t h a t   i n t r o d u c e d   a   b u g  
       g r e p               P r i n t   l i n e s   m a t c h i n g   a   p a t t e r n  
       l o g                 S h o w   c o m m i t   l o g s  
       s h o w               S h o w   v a r i o u s   t y p e s   o f   o b j e c t s  
       s t a t u s           S h o w   t h e   w o r k i n g   t r e e   s t a t u s  
  
 g r o w ,   m a r k   a n d   t w e a k   y o u r   c o m m o n   h i s t o r y  
       b r a n c h           L i s t ,   c r e a t e ,   o r   d e l e t e   b r a n c h e s  
       c h e c k o u t       S w i t c h   b r a n c h e s   o r   r e s t o r e   w o r k i n g   t r e e   f i l e s  
       c o m m i t           R e c o r d   c h a n g e s   t o   t h e   r e p o s i t o r y  
       d i f f               S h o w   c h a n g e s   b e t w e e n   c o m m i t s ,   c o m m i t   a n d   w o r k i n g   t r e e ,   e t c  
       m e r g e             J o i n   t w o   o r   m o r e   d e v e l o p m e n t   h i s t o r i e s   t o g e t h e r  
       r e b a s e           F o r w a r d - p o r t   l o c a l   c o m m i t s   t o   t h e   u p d a t e d   u p s t r e a m   h e a d  
       t a g                 C r e a t e ,   l i s t ,   d e l e t e   o r   v e r i f y   a   t a g   o b j e c t   s i g n e d   w i t h   G P G  
  
 c o l l a b o r a t e   ( s e e   a l s o :   g i t   h e l p   w o r k f l o w s )  
       f e t c h             D o w n l o a d   o b j e c t s   a n d   r e f s   f r o m   a n o t h e r   r e p o s i t o r y  
       p u l l               F e t c h   f r o m   a n d   i n t e g r a t e   w i t h   a n o t h e r   r e p o s i t o r y   o r   a   l o c a l   b r a n c h  
       p u s h               U p d a t e   r e m o t e   r e f s   a l o n g   w i t h   a s s o c i a t e d   o b j e c t s  
  
 ' g i t   h e l p   - a '   a n d   ' g i t   h e l p   - g '   l i s t   a v a i l a b l e   s u b c o m m a n d s   a n d   s o m e  
 c o n c e p t   g u i d e s .   S e e   ' g i t   h e l p   < c o m m a n d > '   o r   ' g i t   h e l p   < c o n c e p t > '  
 t o   r e a d   a b o u t   a   s p e c i f i c   s u b c o m m a n d   o r   c o n c e p t .  
 