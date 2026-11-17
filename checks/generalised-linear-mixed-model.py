"""Independent calculations and generated-output checks."""
from pathlib import Path
import re,sys
import numpy as np
import sympy as s
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
SLUG='generalised-linear-mixed-model'
NEEDLES=['6.846293', '4.278242', '0.624899']

import io,zlib,base64,hashlib
from scipy.special import expit
from scipy.optimize import minimize
# Public dataset: https://raw.githubusercontent.com/cran/mlmRev/master/data/Contraception.rda
# Numeric columns: useY, urbanY, livingChild, centredAge, districtCode. No private reference text.
PUBLIC_DATA_B85='c-p;P%Wq`aT{h}Q8pf7rTej6*vMXhGy<M_gezdFos#7jM+HE@`LLfy#iblyKEFuzS5Q|BWN=UOtfi)6Rc7WJq!!B3w53oZ>Y-WcDNWIAL*kwA!ZS$SFzw>?P-ka$S0zUoD`Mtj1<6PJL#aDml{<psVYjb}*_k-5AKK%HbAGMBZt&?vLTD@B9+u!@>k3Ra~55DoekG}Qc+yDF32jBhp!!Q2tAOHRb-~aH7|GnLRxwqe|9dvrNKdI&W_x>FGdoxV`=O3QF|Ia`E{;r$L{Fmb9<~F|a^Y8xd>1q<jy&1lhcKZH*4;k*WPnQ4g`m-86_ecNv!{I@7D`B{=eEPGm{e87X@2BbeW_W(~Z~yYQpDa*$#q9F%|BusSZf<(N$Kw5#DDEFWZ~xw({lf~i%WwSeUw!8%|Nhxe!+NCh7IVhctUUGHsk{o+_XlsokNP*g-x9_B=r=!k@i*1y^xR*%_tQs?>7n9O|4#F*=UDt@+i&*V?EJ9q$Nl^15C7>WU;q4neyYW@dOtNks?@(z`)#^%cun<(E^nG|&s@H^SN*2yp~n3zZp!zKoP1^JQBCsYQT{lc>d~U|w7QVmxhdAmPD%NZ))^Kr7Ek8)M|RxjkJD+qth;>tlE2@W>ai`JyHv1lJ>bLf@_-AU>&vTCdEvVMfD89m5C5{`+0vsb%G;vyrhGL|^_cdPd#;@OvHtntpXRp|$IlJ(ns1j!PK%dXNjR&&dNa&>ZkP{zoK<IH?V|ea&9L*ush_w1b(k;DXYZ%xTX+tLkC!mtGdo-Uct-Wjwx1O*b*J5r$4hqI&(Ei7zG?o|<7&!lJEigcRNr=Kyb+$`<N03m+uYo={yr9YceSKCGdCB<&-10_ui8hTyf?!zAEb79Gt~Sx+i%9n^Xs%N59_au!#J>U$XBs;VLW8Z%hrSO0rN+T+8KGxmiJ3{ysHbgzBs28j~7jzZoh21(0z#+htoc1gW&u*<vpkEkpei#-}jt058CpuE->7BX*k>y+Bn=Z*f>?+Y&%<Z`mrI;n#<mET0d!@i+dUyhjrh^A+OoE?6_jQ8;~d3d8%(Wr@piI3&)k!zt}iUkCfLMNj^I>z6#)A-eU1rO&D)X_a!MmKN0ijiPQELPn^~dJ#kw7cp~N{lh-2hRGiQEPsF&7J(tB_QJkM|wmjT(JrVgd_FUFq71tO0D|YTPr^WLlem}@x``l?>ZcrT7k0&CJ7tNzsTvg1YRi2m7huL<X+ONZT2>7`;4(DHn>r=mBePjI6bj5h+;e0%Ine@A994w3d-?9tu<x@SDo%XI_%R}B+7W?95(|*(WXf<ItwDYnV&lsmnUYp(z^N7i-5qW++S{CD!*{@3PhrGK?_<51yvi+7<k91D1P(85D#KsHDbNhbC_sb&h#_DU?d5PKu`-5dt-?}_bp{~Zpvn6jMDd${EU)H}Yi*<(igXdeAPp$dGKKDP~wnIPTd8FA{<tv^4@LgkB>?4>zc3fF{#Ob?~l*LzCoLcdhAE(8OZWlGKvg3ulTP=(GgV;LA_M*%#+fL)tI*ohm+wF6)&O8<U@l>?SQ<9fkR37^GsmQxeiGS0*#Z$3PKQ;S5v@^3yh2pS(c`DAU#r4I0&6byK=e%*H`pvI1PwhQF$Xhe#1>}P@^M3fgwMOD)(`BD)@%@@ux7Nh`SQF!!-LE3vuaz))IKQolefFBT2Vr_t#rv($`(eJtp3C+TYhr&|+;6H~)VRmIWN})_c`lnP*!`Z1cBzPY)TZ~-_{Hx#*9bqeJo4-68tD@kO0tU;r>s9+Bm10G-<pX-J?!sV(atroZq-B{uZecH<)Qs*Vt-H*``DT|PuED?*Qx!m9@WHts3!Kiwmhu+Opoo7^ziF+QJl}G#p6%4ANB_|aUR?h<7!i^3!9|=&O3&~KGwb;){jjwUN*%(J64`$=RHx6w&;&eLUF)DDy}Z>hw5U!)y4QLdTxXsU_Tp&aZubY7zegItTV;!jP;`~_U(0%59(rnQ2c&zalmm{w_@Ye`g@!-&zhuv*`+x2Z_}KU@!iFihjGR3*LT_HT61!f#A!8QILwcxSQqT?ZgDPaiuI^T_Cu?QcE1%W5A&!g&X-LwkD4NH*#1?|)%0a?Z}mA%GVd?Ca{TM}O-+&4V*SRxhij7gZHeYD+OKWk{P=5=`R$nt<NSR@+q@sv-?lgp2J`^Fw{aNvZPCANao%r>`-8TaZ*9^a@cUtZ+7|16Til1WNgrEx45!KS^EcMcY+h)K{L&`*+org<cuxD+uDBoXl6+HfE%DqIm524HYwC;pAsdJO?TUR)SLCZM;i1Q(zVnXB({PrZ*>_)E!uJg-597H@`crN{H4d~mRrT=eLYLIbns~nsm4|ah?ENf%^k`gRJ?e_}yr?`qPSyOtI?eL8k~4qV?=IN5|9We_cXc{8?k#_;(0t40KQ@Q5a~DPbZYAa5toWPFH<>r0^1SV|ynHU^W!-(*^|BcM6^+wH5w}j`S><~*&*i$B>EGG=sXUooe^p+~u#4z7l@D;A6U%>A9`(fjV5zjafb)@!E8Bi*{NY?-$Dev`b{?sEWbmnEKfTYveNIt5V*8<{E5{#d-0S_bHh<{-hL%Tq9n|_EeGXOQPwnee`>AtnT;EhHSO=|rY?tg+th(UiDijy)udIDeSKMQE$==NJo3-EVitjF6vPbVEn!J8V{!q_NzZYoG`-St!dI#&0eS2Tz$+VvL2>+%1z5Tn4_}xuU?00+S{qQ@P9;rurj^WVGJu+V|CD}MD?tA22@;Slz`OzbJzUbKfkk@+RyHHQuKifF`e!M5<QIF*1615-Z2RpYR`uDMTzttozp0~yNyG{6|lM`q0X`?)O;E!!_-@YyK+O`<?+hQKs@>ILT;kFWXKjbT>Z{3v>FMj=vjTiP^GqX#&FWC`!W5+xf^KD0rKZaXz;rsdh)sD!!JK}rZ4tZBw%4xs+_d}j6danO>v&<jsPP5-8^{=Lfj>G(ojZ@Vh>^+p(rJ2)yvwb4&$NS<wtS|PHHV)^MKG_#PPuTsiKkbvbwwlm$f!F%tKBrIm_U)YaWBUV!<MzY)+ZXwuFV+txuR(BrpV%jT`v$q6|MwbwG0*M$h2x%`%j#-htTW6XtD?NNV>s;VV$Ws27sT#Y%XvRm7y4q~Y5OhA2Y!FLm6UZqHU3n)X!)z-un#NF8`w9obJxXq*>Q|F!hB`@_iT2_UbIDVSTA?Q_kdk-Uf31)qPrqb?h?OM=>71WX;<ur7_LWg7^l19erQ+RzwC;6v}?v6@{4_LcD%5CCyRr5S1#_6)9kXEl!eQ-ANx+QXuSCOyC=r|9_e4wJl_-Za!;(6MbGtla!>Tzo|xx*;=W{0+~?Rh>^EZNvAD8v;drs$b@#=6`@UE|_Rac+eXM;h?%Qn~@-xG=DGvE`U+fR|&3MNCYG2$V?Th~17yG|`ao=w1fxNpf@`f!hTVFQkF@L0e_JKH89FTr@&xLWmKMq7a4oDm<Q5^E_0oijcP<i+}vj<|GIS}V=8;5(O1F>E*JGXM$&pP)R#bJLCi(`3tAo774S1-gp$P4k@7a|Y65a*~DV!qip{Qb!nq(7)Trf)Wm#UDGjM$g4M6MHUu*ND9zi<d(Z2MZL3_4iQB-$T(Zhax{8iac~E?$MdNMXCq#(4n{wI~4bchazt<eYcHst^M;rd^Z@7eaQlqhkckW5BX(4_TH&~8Lmcg*f$N#{uFu5)&uLzK->=v#CMHY9Q(d*Aim?Ua~lb>ANH{<{;Gx^);???^4dVGmjkh{vvJ{kvv^}5^2R{y6N}@*`D@i9Ti<YgSp3ZVyDHjw#ZkXy#xwgJs)1N%Y<a4kabHqA?y=4c#QkJ(J7?ppIDJIrVV}tC*GkHYKkO3+;yX$4{0P?%mLK`~5BEL;@@~NMGF-P}^TYpr<$?H~G7#sU*tp8?4>jLZziIKT^Gm)we<{j)Db}r*VqU%!_azMXoZ$Sv>7_Vdz7*r-r5Fb<#d#t2ezE6TbHEXqD^ht!raX-2BYQs%{x~A@LeFKN>+d%zNf_tv<&Q*vFkGGDuwF8GTwmPB9*O(9SUuS9K^489KbIBtn~uZp^pC{;>WI|eO{d|wf3g2#`Zf|RKUBZ<bH)LCpJsY&<@7ImcVTf~qy7l<pS52*66*)c-$ib}Og_!eFWK>I;hG{}?Up7l%xl)~6&%}p5XkdmB5%`^$M!kL;=Fn+*7IZ2F8F?QEc)YE<h8Qo)hRCQ4|czzdh8LLUq6mbp2Yo7to<1O+47M8m|dDBovZ5W^VPA)r^n(vb4==BHOc2+%Wpe0{;<z3p6A)}^2U{ZF3x#H^T^^q*54P^L-nuUUojr4QGKy)F?scp?5FdFst5M%u{^};>WMjrV&8N^=Ek;TIGm^Lb5Rdl9@^!^oPW{3C*uD8MC_kW#CSdt^W#L^hn<LVa3c19_WiKGIuY~egzQC^63rjajrg<jt*AUdFHc0?JrV0d?ETbuVe=r1(-xJd<%d6SorruIE04V!*t~)HaZ30q?Q>4QG<g_*rzVf%dy0+2@9XSy|N2kAcJr6-;`vnM-B@|Ee2;Nu%fo)d#uby7aX;Yky#BR#_f+IvTORVMEf4$2Q;~;G$sF*E%L9Hn6?vEGTM^}Liuc<h@~k+p_^L{A+4f`e`Kh=^KPB~-+fR)v)xX*Diu$cZ?HuL<Yah$}TcPKM>w+H#>pTvio)?!Ft}~1e*gR9zZ~lL;=v17K*tv})pPlpDrP%%Q;?z8{;-2mKWAn|LLsPywGv_zVw==OXv2p0%GxL79Z#pCWK`Y6|S#~}nJhV%3_`YyPc(+>G{V)#B#QccGvAnePnD)DmMS1g7UUpouKH^N|zcX>3X1HESe)D<!Oyr^1_+$NKaXqv=()G~dIW}HeiI(SS91Kl)IL{2l`whkYF2gNQ9R6PJknH7Ed2PpVxW6BYJjCwD?UH?NetDReLlVy|Di6Qc8;X7GP>kmxnR^yX@|!<*56OGVBZ|w8gIGPR_i1PLC8)0x`<DO?=0->MNGU%%algTE&s_Goe*86zb1lAd;y%`iyynQ9x0Gn-?$UF!?LvN6eBwy|T=Q_``#)2jw{N27*6Fzrf6?+RT$AF!zZ0kN<iu%xVgQ$IzgZmYV?+1*|8vyDX>}oRu8LFjfI1z0F6kozxa@c)b(Q+}5!DxXXyUZG5ReDFOYPSr_VeDsXuNE?vh1hgvUyF_SM>+^{gMD*VVxP7{DSks$mCPpTa4`Y3V6R9iF<~?{h)s-s)t{<M&h2v))(LNM&i5Li0o<lE}y)-IRAG^irUZLE00Kjuu0`%-^t=?%ZLN3&mM{IA0yI_&x`UZRGz9wIIgUIZ6xmNM&iC{WY+y``?0xkMEVVm!@ccD+`o*pIv9|LbI(ZQ@#uJAdzFzm*N#X%ujI_5y!Z3xK_;(9<%R2qANM=deqo&P9odBO<p0fO6UJ)|184QwB5zE@yrj4VdM?Dvg!yBS;vnB9B40(zBXK$r<8LC?nSdVHkF)$;rSg!k&c!@GC+DVnhI6sboQrkgT#G*w=kG<&3BPPQW*6kibMZapT<jyxMZP*0-(Aj0AC}Iw=Y-d`JsjEBP1w0y9?p5^+ME*51Nr4#<e_uz9b&@bpp$6l?uhs6yK?0D`?Yg%4?HIGU^<tL#rFV)>lx=h{KI{*jl;d|*sdR<JnVPJV&55i?(9GOJBP8@hmA$Px6ehsAB%lwtUuWMTWnmhetazQ_*k49$KssA>|CYi;=4g0KcLQxNx!jf*u{9qnH0xiA2ud^amuG-vd>wfIP7EDxeX%Ee-9Xwx>cp}u#dHIvL3+qV{M-pI2Zf-vGzU~hy%@j{+@MA-j6mCO^-$DH&tKkhwS^|+&CtC(TzmAAJ+rlk7D&u{lWUlv9@QOu)4Kq$g}3qvACBPdAG1Ui?2u>oQQo>;C|Ro+Vvxw|ExNw>cQh4_m~$2asKatUTAxPcR2DcL~(VB!~W`m%(WW{lZWp@7vdi7Lfk)Jh<(I`76$<w_Cpt9|IE&9Qh(q+!uAL5BQCUgFmP_Roh`epCe*)~c42=X&(5tRTHM#DopDcN=Q;LG7o;D0?BU4!(ZoI%dECa~p4E;6n0qG7e(4^B;hGeOeb@!53p-RE_6N3|kxws4-=4<RrRiVHk4rLtq;t=u=HI}%m>-v7ow+3a{UeG)9=g=xFJNb!&o9Z|te;a4(#J;o*P6GQPSdwzoNLv~OL6~vY36yhJc|#u=>3rIFHL^Vju*Bcx6j4B-lbUIF2()JC3#QT5YKJov>*GP|B}oByA+3gqOAwk=}WC2kB+PS@t5s4*2gkjg~qd*m)U$}>Dv<Zty6j7dSvYNCStryn7%uX$;1BTQriOuaJbhK?LyC8r}|?5VxNoquvj~jJ#gTD*bl|pC9l4^U2u-K<-z+x0EhFweJ=213GtjAFZuPwc_CI`_I(7i^Qs}w`hCJHZLj<e$G+FQ68laYhkeAA*hgH6^SO;v<>CBsWyVX`&Q?9TB5}1q?}zU=4A<v&fxhWVoa3)ZKeXr=PPKD(yr}mhd*HzRuuc~}*MA@U^8Asl2isq<JZjN%)%?Kz?~3r>5<M6D;w!O#z9Ri!r!>CO;@;mM<h`Hu_f}VAZ?Rq)4*MKd7t(htyKZIU$X>vd=l8o;WdGMl^4W##n*#E}_cQjVlPmF^iN$j(VdvsIG2@qoMAM^A^~jDZOWt-#cJcSIjMr96vWx!?E7sqM$oCVm&d_tMxHtA(fpc+gEUJh9ZW`-1E3P)3mPd`8{<Z8fpVKa6e-&-N{Beczo1JgC2PsP)%S*4WhImMfQ<V?Gbt|ub*WIsH-@Lr5`&X@R+3}n|KX6~d{97rB@BQyBipLA?>x%PGwjTN8O4T>Jk0o<sY5Z4B@|{cG1ETrfn#($+^$}WJ>2+1*Nwq)FaNhfBG{4N^vhBj&C9la`mcEl*oAU?Gjn`yON$2xxvj3|j+Wl(A{fzoMBhQ+DueH21&-M31*P4F==W4ig|Htiue=l^c@qNG_SdXs7x%=9jLot7^$y}Sx6-?f062_%_{yvq5eciRTr#5l^ci{p10bkkjG=2TLCFXD7e#k@Y+)YuBs&THxf7jZ+eZul%+l6udyBd?%6XkWNzWDv=HR+4z>ABhVWBZM3v0gGgnxY<$9J6ycfBpWiMeQ8sp;(;1uVZy)#cB5IQM;)A4fBT8Ux{_FuskcSNFL3-66^FUBCkPk{&!@r#Ja_B>lBB4`bw-buf+M1={xTj4*OW<j}3Z1?4MtW@$yQX_g|4Xtxz29V`KFt?<v&IRvcLM?Ul&mVjj)ltlvevF>%;u-)Q|+0Eh3`H>6MG@^D^=#m%0J^N}qNdF_Ved4tMR{ekl!^GB7~+5g^*>D!|EX8X<RV><@U=&vZQMsU`-v-yVqeW4p|&qdE|QF-{^)4U<?5KB~#IQ!KdlZW3&*f{)7f$32#%^%r$#J=CPajHLXKEDzBoLIYL@D=dAoo~3$7Wr>d{9NpFZp3*yR-VO^HOJ1yJvBSGMfJcrK&)@nA02u>>=SRqewWp)ju;0UqCe`Qe;bCKt@jj`N2^4hzdvBS_MDt+>B069H{$*vRu9526S2Mpa5&d8d5=pv*Pj=}x<LKWb@}3teQ&|)w3Q$6aUaf0>%GU8hjSjQgL_W1%QKfR-`M`8ggh$w++y~d{fFOsv->r3#vj}N#l{Pp_ha*j&F44bUL{uF*}96~UB5Q#+w^{E|7YW{AAc>*tFOg5{x#`ex)g_VfQ`fN+h1$%LIIp6&wD=#+z<Qg*W#RP-!B`N*DiB&IDfnr_Z!U4l_V@rjZ;6*ZFyLKnY=~EaF~~`#do!$dieQqYxmDE=iS=<u8M=b#Vz53MiRcC&j+?1xZk)H<M~#5M-1qJ-?uY6Z_xYUJNvE3r#241XDE)t{Z*_UYWy+&WAU=$ipewTZvcmN@K$^O2;lI)w|J|~GbYZ;OSTWYHTxm_I~!Xb?zwKoeV8o|>m}2-Rg!=Gzk9kR{p3n%_rv|^t@bWN<FxIlzM1lhp1Ud9r9tIo#~<l)CX6@IdVWjl`8>tpcLlfNoOdg}OWu;XY?sQzzNGm5uy11VlFqBPyx;!yAOHE$yLt7N>{TiW(?hn4q=#j{ynge)zhZTvF50D<l;t<o&iEZl(KyiK1^ePyJ!bn@oEz`RJiX)L$X-5#gMR2v>|^f;5AC_KaM|aQ-*FAd%f^xS3aUq+;;{d_6YJoew(m6M`M;lYN9yIaW9Me$R6W@5Bi)I8-JRH9-HH7W!*wVw+rMOgAHZpG;O}4VG#(Gw5BE()aem)^r`3IGmz1CH#CjQ!2k%j${U&$fp7l<fd!psBcMYaTliCIQ(>t=aP3M$*GRLR!cW=tWJh~V6!1v-F<X+tS+>?5_LG@M7MP9SzA#dDkew#V>0f*m>+>`#k?-&lhE4|nH)4=_Z*O<QR<XnGWcdxx`1mxk|$Z%UpKD$_Te@Q&I#c@!7i^}us0*k91(as&}H#H8z{KDdo{4Uc(<iE*1;nPmSaLD)U+?sc;st5ZnsHh(P--+C7a{#rA<qvCqyVv?tDsROx9M<1^(kDKq=i=Ng=4AjEjw?TZ_oyCWzxj5lxqSMvcWjaWCSpCJ_G9w=@1TmuOE}LB9uLUV?C1Z!9=l)9<%=u!{Y&vYQtyX<2UJv^*FRHv5B1|0T+?g)'
A=np.load(io.BytesIO(zlib.decompress(base64.b85decode(PUBLIC_DATA_B85))));y=A[:,0];urb=A[:,1];ch=A[:,2];age=A[:,3]/10;group=A[:,-1].astype(int);X=np.c_[np.ones(len(y)),age,age**2,urb,ch];J=group.max()+1;N=np.bincount(group).max();mask=np.zeros((J,N));Ys=np.zeros((J,N));Xs=np.zeros((J,N,5));Us=np.zeros((J,N))
for j in range(J):
 ix=group==j;n=ix.sum();mask[j,:n]=1;Ys[j,:n]=y[ix];Xs[j,:n]=X[ix];Us[j,:n]=urb[ix]
def objective(par,k):
 beta=par[:5]
 if k==1:L=np.array([[np.exp(par[5])]])
 else:
  s0,s1=np.exp(par[5:7]);r=np.tanh(par[7]);L=np.array([[s0,0],[r*s1,s1*np.sqrt(1-r*r)]])
 Z=np.ones((J,N,k));
 if k==2:Z[:,:,1]=Us
 V=Z@L;eta0=Xs@beta;u=np.zeros((J,k))
 for it in range(40):
  eta=eta0+np.einsum('jni,ji->jn',V,u);p=expit(eta);w=p*(1-p)*mask
  grad=np.einsum('jni,jn->ji',V,(Ys-p)*mask)-u
  H=np.einsum('jni,jn,jnk->jik',V,w,V)+np.eye(k)
  step=np.linalg.solve(H,grad[...,None])[...,0];u+=step
  if np.max(np.abs(step))<1e-10:break
 eta=eta0+np.einsum('jni,ji->jn',V,u);p=expit(eta);w=p*(1-p)*mask
 H=np.einsum('jni,jn,jnk->jik',V,w,V)+np.eye(k)
 ll=np.sum((Ys*eta-np.logaddexp(0,eta))*mask)-.5*np.sum(u*u)-.5*np.linalg.slogdet(H)[1].sum()
 return -ll

assert A.shape==(1934,5) and J==60
results={}
for k in [1,2]:
 initial=np.array([-1,.063,-.464,.693,.860,np.log(.474)] if k==1 else [-1,.063,-.464,.770,.860,np.log(.6),np.log(.74),np.arctanh(-.79)])
 opt=minimize(objective,initial,args=(k,),method='BFGS',options={'gtol':1e-5,'maxiter':200});par=opt.x
 # Finite-difference precision can end BFGS before its requested tolerance; verify stationarity directly.
 h=1e-4;grad=np.array([(objective(par+np.eye(len(par))[i]*h,k)-objective(par-np.eye(len(par))[i]*h,k))/(2*h) for i in range(len(par))])
 assert np.max(np.abs(grad))<.002,(k,grad)
 results[k]=(-opt.fun,par)
beta=results[1][1][:5]*[1,.1,.01,1,1]
assert np.allclose(beta,[-1.006,.0063,-.00464,.693,.860],atol=.0005)
assert np.isclose(np.exp(results[1][1][5]),.474,atol=.0001)
assert np.isclose(results[2][1][3],.770,atol=.0005)
assert np.isclose(np.exp(results[2][1][6]),.74,atol=.002)
assert np.isclose(np.tanh(results[2][1][7]),-.79,atol=.005)
assert np.isclose(results[1][0],-1186.59284819728,atol=.00001)
assert np.isclose(results[2][0],-1180.48800322357,atol=.00001)
assert np.isclose(2*(results[2][0]-results[1][0]),12.2096899474)
assert np.isclose(np.exp(.693),1.9997056605411638)
assert np.isclose(np.exp(.860),2.3631606937057947)
assert np.isclose(np.exp(.770),2.159766253784915)
mean=2*np.exp(.25);cov=4*np.exp(.5)*(np.exp(.5)-1);var=mean+cov
assert np.isclose(mean,2.568050833375483) and np.isclose(cov,4.2782422310356685)
assert np.isclose(var,6.846293064411151) and np.isclose(cov/var,.6248990790761072)
assert np.isclose(-.07/ .055,-1.2727272727272727)
assert np.allclose([-.07-1.96*.055,-.07+1.96*.055],[-.1778,.0378])

# Independent Gaussian quadrature checks marginal count moments.
nodes,weights=np.polynomial.hermite.hermgauss(60);weights=weights/np.sqrt(np.pi)
intensity=2*np.exp(nodes)  # sqrt(2*Var(b))=1
qm=weights@intensity;ql2=weights@(intensity**2)
assert np.isclose(qm,mean)
assert np.isclose(ql2-qm*qm,cov)
assert np.isclose(weights@(intensity+intensity**2)-qm*qm,var)

# Numerical Hessians independently reproduce the legacy standard errors and z values.
se_by_k={}
for k in [1,2]:
 par=results[k][1];dim=len(par);H=np.zeros((dim,dim));delta=1e-4;f0=objective(par,k)
 for i in range(dim):
  ei=np.eye(dim)[i]*delta;H[i,i]=(objective(par+ei,k)-2*f0+objective(par-ei,k))/delta**2
  for j in range(i):
   ej=np.eye(dim)[j]*delta
   H[i,j]=H[j,i]=(objective(par+ei+ej,k)-objective(par+ei-ej,k)-objective(par-ei+ej,k)+objective(par-ei-ej,k))/(4*delta**2)
 assert np.linalg.eigvalsh(H).min()>0
 se_by_k[k]=np.sqrt(np.diag(np.linalg.inv(H)))[:5]*[1,.1,.01,1,1]
assert np.all(np.abs(se_by_k[1]-[.169,.0079,.00072,.121,.148])<[.0005,.00005,.000005,.0005,.0005])
assert np.allclose(beta/se_by_k[1],[-5.95,.79,-6.43,5.74,5.80],atol=.006)
assert np.isclose(results[2][1][3]/se_by_k[2][3],4.69,atol=.005)
assert any(np.all(urb[group==j]==1) for j in range(J))
# Expit of the common concave quadratic is not globally concave on the response scale.
def second_probability(a,urban):
 eta=-1.006+.0063*a-.00464*a*a+.693*urban+.860;p=expit(eta)
 return p*(1-p)*(-.00928+(1-2*p)*(.0063-.00928*a)**2)
assert second_probability(0,0)<0 and second_probability(50,0)>0

if '--math-only' not in sys.argv:
 source=(ROOT/'research/content'/f'{SLUG}.md').read_text()
 article=(ROOT/"articles"/f'{SLUG}.qmd').read_text().split('## See also',1)[0]
 for needle in NEEDLES:assert needle in article,(SLUG,needle)
 assert len(re.findall(r'\{\{cite:[^}]+\}\}',source))>=5
 assert len(set(re.findall(r'\{\{cite:([^}]+)\}\}',source)))>=2
 assert 'Your turn' in article and 'collapse="true" title="Answer"' in article
 assert '## Check yourself {#check-yourself}' in article
 section=article.split('## Check yourself {#check-yourself}',1)[1].split('\n## ',1)[0]
 ids=re.findall(r'(?m)^### .*\{#self-check-([^}]+)\}',section)
 assert len(ids) in (2,3) and section.count('collapse="true" title="Answer"')==len(ids),(SLUG,ids)
 for qid in ids:assert (ROOT/'questions'/f'{qid}.qmd').exists()
 for ans in re.findall(r'::: \{[^\n]*title="Answer"[^\n]*\}\n(.*?)\n:::',article,re.S):assert 'cite-ref' not in ans
print(SLUG+': independent calculations and article checks passed')
