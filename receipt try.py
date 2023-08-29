#
txt = "{a:┌<1}{b:─^82}{c:┐>1}"
print(txt.format(a="", b="", c=""))

#
txt1p1 = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
print(
    txt1p1.format(
        a="",
        b="DELIVERED TO  :  ",
        c="",
        c1="",
        d="DATE          :  ",
        e="08/29/2023",
        f="",
    )
)

txt1p2 = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
print(
    txt1p1.format(
        a="",
        b="CUSTOMER NAME :  ",
        c="GEN. T. DE LEON",
        c1="",
        d="PLAN DEL DATE :  ",
        e="",
        f="",
    )
)

txt1p3 = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
print(
    txt1p1.format(
        a="", b="ADDRESS       :  ", c="", c1="", d="ORDER NUMBER  :  ", e="", f=""
    )
)

txt1p4 = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
print(
    txt1p1.format(
        a="", b="CUSTOMER CODE :  ", c="", c1="", d="ORDER DATE    :  ", e="", f=""
    )
)

#
txt2 = "{a:├<1}{b:─^43}{c:┬^1}{d:─^5}{e:┬^1}{f:─^23}{g:┬^1}{h:─^8}{i:┤<1}"
print(txt2.format(a="", b="", c="", d="", e="", f="", g="", h="", i=""))

#
txt3 = "{a:│<1}{b:^43}{c:│>1}{d:^5}{e:│^1}{f:^23}{g:│^1}{h:^8}{i:│<1}"
print(
    txt3.format(
        a="", b="ITEM", c="", d="", e="", f="QUANTITY", g="", h="REMARKS/", i=""
    )
)

#
txt4 = "{a:├<1}{b:─^10}{c:┬^1}{d:─^32}{e:┤^1}{f:^5}{g:├^1}{h:─^11}{i:┬^1}{j:─^11}{k:┤^1}{l:^8}{m:│>1}"
print(
    txt4.format(
        a="", b="", c="", d="", e="", f="", g="", h="", i="", j="", k="", l="", m=""
    )
)

#
txt5 = "{a:│<1}{b:^10}{c:│^1}{d:^32}{e:│^1}{f:^5}{g:│^1}{h:^11}{i:│^1}{j:^11}{k:│^1}{l:^8}{m:│>1}"
print(
    txt5.format(
        a="",
        b="CODE",
        c="",
        d="DESCRIPTION",
        e="",
        f="UNIT",
        g="",
        h="ORDERED",
        i="",
        j="DELIVERED",
        k="",
        l="AMOUNT",
        m="",
    )
)

#
txt6 = "{a:├<1}{b:─^10}{c:┼^1}{d:─^32}{e:┼^1}{f:─^5}{g:┼^1}{h:─^5}{i:┬^1}{j:─^5}{k:┼^1}{l:─^5}{m:┬^1}{n:─^5}{o:┼^1}{p:─^8}{q:┤>1}"
print(
    txt6.format(
        a="",
        b="",
        c="",
        d="",
        e="",
        f="",
        g="",
        h="",
        i="",
        j="",
        k="",
        l="",
        m="",
        n="",
        o="",
        p="",
        q="",
    )
)

#
txt7 = "{a:│<1}{b:^10}{c:│^1}{d:^32}{e:│^1}{f:^5}{g:│^1}{h:^5}{i:│^1}{j:^5}{k:│^1}{l:^5}{m:│^1}{n:^5}{o:│^1}{p:^8}{q:│>1}"
print(
    txt7.format(
        a="",
        b="",
        c="",
        d="",
        e="",
        f="",
        g="",
        h="REG",
        i="",
        j="OBC",
        k="",
        l="ALLO",
        m="",
        n="TOTAL",
        o="",
        p="",
        q="",
    )
)

#
txt8 = "{a:│<1}{b:^10}{c:│^1}{d:^32}{e:│^1}{f:^5}{g:├^1}{h:─^5}{i:┼^1}{j:─^5}{k:┼^1}{l:─^5}{m:┼^1}{n:─^5}{o:┤^1}{p:^8}{q:│>1}"
print(
    txt8.format(
        a="",
        b="",
        c="",
        d="",
        e="",
        f="",
        g="",
        h="",
        i="",
        j="",
        k="",
        l="",
        m="",
        n="",
        o="",
        p="",
        q="",
    )
)

#
txt9 = "{a:│<1}{b:^10}{c:│^1}{d:^32}{e:│^1}{f:^5}{g:│^1}{h:^5}{i:│^1}{j:^5}{k:│^1}{l:^5}{m:│^1}{n:^5}{o:│^1}{p:^8}{q:│>1}"
print(
    txt9.format(
        a="",
        b="3050019",
        c="",
        d="",
        e="",
        f="",
        g="",
        h="1",
        i="",
        j="1",
        k="",
        l="1",
        m="",
        n="1",
        o="",
        p="",
        q="",
    )
)

#
txt10 = "{a:└<1}{b:─^10}{c:┴^1}{d:─^32}{e:┴^1}{f:─^5}{g:┴^1}{h:─^5}{i:┴^1}{j:─^5}{k:┴^1}{l:─^5}{m:┴^1}{n:─^5}{o:┴^1}{p:─^8}{q:┘>1}"
print(
    txt10.format(
        a="",
        b="",
        c="",
        d="",
        e="",
        f="",
        g="",
        h="",
        i="",
        j="",
        k="",
        l="",
        m="",
        n="",
        o="",
        p="",
        q="",
    )
)

#
space = "{a:<84}"
for x in range(2):
    print(space.format(a=""))

#
txt11 = "{a:<20}{b:_^22}{c:^4}{d:<17}{e:_^20}"
print(txt11.format(a="Checked By     :  ", b="", c="", d="PD Officer    :  ", e=""))

#
print(space.format(a=""))

#
txt12 = "{a:<20}{b:_^22}{c:^4}{d:<17}{e:_^20}"
print(txt12.format(a="Receiver/Store :  ", b="", c="", d="T & D Checker :  ", e=""))

#
print(space.format(a=""))