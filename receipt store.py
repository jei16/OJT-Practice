# input
delTo = input("Delivered to: ")
cusName = input("Customer Name: ")
address = input("Address: ")
cusCode = input("Customer Code: ")
date = input("Date: ")
plndeldate = input("Plan Del date: ")
orderNo = input("Order Number: ")
orderDate = input("Order Date: ")
code = input("Code: ")
# desc = input("Description: ")
unit = input("Unit: ")

w = None
description = [
    ["3190022", "Fluffy Mamon", "pcs", "", "270", "", "270", ""],
    ["3190007", "Chiffon Cake Slice", "pcs", "", "140", "", "140", ""],
    [
        "3190007",
        "Vanilla - Marble Greeting Cake 9 Round",
        "pcs",
        "",
        "140",
        "",
        "140",
        "",
    ],
    [
        "3190007",
        "Brazo De Mercedes Whole Roll 2020",
        "pcs",
        "",
        "140",
        "",
        "140",
        "",
    ],
    ["3190007", "Brazo De Mercedes Whole Roller 2020", "pcs", "1", "", "", "1", ""],
    ["3190007", "Brazo De Mercedes Whole Roller 2021", "pcs", "1", "", "", "1", ""],
    ["3190007", "Brazo De Mercedes Whole Roller 2022", "pcs", "1", "", "", "1", ""],
     [
        "3190007",
        "Chiffon Cake Slices Mercedes Half Roller",
        "pcs",
        "",
        "140",
        "",
        "140",
        "",
    ],
    ["3190007", "Brazo De Mercedes Whole Roller 2023", "pcs", "1", "", "", "1", ""],
    ["3190007", "Chiffon Cake Slicess", "pcs", "", "140", "", "140", ""],
    [
        "3190007",
        "Chiffon Cake Slices Mercedes Whole Roller",
        "pcs",
        "",
        "140",
        "",
        "140",
        "",
    ],
]


#
txt = "{a:┌<1}{b:─^82}{c:┐>1}"
print(txt.format(a="", b="", c=""))

#
xx = len(delTo)
if xx > 32:
    newdelTo = str(delTo[:31] + "-")
    transfer = str(delTo[31 : xx + 1])

    txt1p1 = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
    print(
        txt1p1.format(
            a="",
            b="DELIVERED TO  :  ",
            c=newdelTo,
            c1="",
            d="DATE          :  ",
            e="",
            f="",
        )
    )

    txt1p1ext = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
    print(
        txt1p1ext.format(
            a="",
            b="",
            c=transfer,
            c1="",
            d="",
            e="",
            f="",
        )
    )

else:
    txt1p1 = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
    print(
        txt1p1.format(
            a="",
            b="DELIVERED TO  :  ",
            c=delTo,
            c1="",
            d="DATE          :  ",
            e=date,
            f="",
        )
    )


txt1p2 = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
print(
    txt1p1.format(
        a="",
        b="CUSTOMER NAME :  ",
        c=cusName,
        c1="",
        d="PLAN DEL DATE :  ",
        e=plndeldate,
        f="",
    )
)

txt1p3 = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
print(
    txt1p1.format(
        a="",
        b="ADDRESS       :  ",
        c=address,
        c1="",
        d="ORDER NUMBER  :  ",
        e=orderNo,
        f="",
    )
)

txt1p4 = "{a:│<1}{b:<17}{c:<32}{c1:^4}{d:<17}{e:<12}{f:│>1}"
print(
    txt1p1.format(
        a="",
        b="CUSTOMER CODE :  ",
        c=cusCode,
        c1="",
        d="ORDER DATE    :  ",
        e=orderDate,
        f="",
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
txt9 = "{a:│<1}{b:^10}{c:│^1}{d:<32}{e:│^1}{f:^5}{g:│^1}{h:^5}{i:│^1}{j:^5}{k:│^1}{l:^5}{m:│^1}{n:^5}{o:│^1}{p:^8}{q:│>1}"
for w, x in enumerate(description, start=1):
    if len(x[1]) <= (32 - (len(str(w)) + 2)):
        print(
            txt9.format(
                a="",
                b=x[0],
                c="",
                d=f"{w}. {x[1]}",
                e="",
                f=x[2],
                g="",
                h=x[3],
                i="",
                j=x[4],
                k="",
                l=x[5],
                m="",
                n=x[6],
                o="",
                p=x[7],
                q="",
            )
        )
    else:
        newDesc = str(x[1][: 31 - (len(str(w)) + 2)] + "-")
        newDesc2 = str(x[1][: 32 - (len(str(w)) + 2)])
        transferDesc = str(x[1][31 - (len(str(w)) + 2) : len(x[1]) + 1])
        transferDesc2 = str(x[1][32 - (len(str(w)) + 2) : len(x[1]) + 1])

        if x[1][31 - (len(str(w)) + 2)] != " ":
            print(
                txt9.format(
                    a="",
                    b=x[0],
                    c="",
                    d=f"{w}. {newDesc}",
                    e="",
                    f=x[2],
                    g="",
                    h=x[3],
                    i="",
                    j=x[4],
                    k="",
                    l=x[5],
                    m="",
                    n=x[6],
                    o="",
                    p=x[7],
                    q="",
                )
            )
            txt9ext = "{a:│<1}{b:^10}{c:│^1}{d:<32}{e:│^1}{f:^5}{g:│^1}{h:^5}{i:│^1}{j:^5}{k:│^1}{l:^5}{m:│^1}{n:^5}{o:│^1}{p:^8}{q:│>1}"
            print(
                txt9ext.format(
                    a="",
                    b="",
                    c="",
                    d=transferDesc,
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
        else:
            print(
                txt9.format(
                    a="",
                    b=x[0],
                    c="",
                    d=f"{w}. {newDesc2}",
                    e="",
                    f=x[2],
                    g="",
                    h=x[3],
                    i="",
                    j=x[4],
                    k="",
                    l=x[5],
                    m="",
                    n=x[6],
                    o="",
                    p=x[7],
                    q="",
                )
            )
            txt9ext = "{a:│<1}{b:^10}{c:│^1}{d:<32}{e:│^1}{f:^5}{g:│^1}{h:^5}{i:│^1}{j:^5}{k:│^1}{l:^5}{m:│^1}{n:^5}{o:│^1}{p:^8}{q:│>1}"
            print(
                txt9ext.format(
                    a="",
                    b="",
                    c="",
                    d=transferDesc2,
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
