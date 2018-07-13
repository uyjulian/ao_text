from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c021b.bin",                # FileName
        "c021b",                    # MapName
        "c021b",                    # Location
        0x000B,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c021b",                  # 0
        "Oscar",                  # 1
        "Morges",                 # 2
        "Bennett",                # 3
        "Tallys",                 # 4
        "Elsa",                   # 5
        "Momo",                   # 6
    ))

    AddCharChip((
        "chr/ch07000.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch24800.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch20700.itc",                   # 08
    ))

    DeclNpc(56290,   0,       2019,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(119120,  0,       4294966636, 275,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(51279,   1000,    12869,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(200,     0,       8500,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(54900,   0,       1720,    1000,    56290,   1500,    2020,    0x007E, 0,  4,  0x0000)
    DeclActor(300,     0,       6960,    1000,    200,     1500,    8500,    0x007E, 0,  9,  0x0000)
    DeclActor(4294894916, 0,       8250,    1200,    4294894916, 2450,    8250,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(516, 0)                                        # 0

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2F0",          # 02, 2
        "Function_3_2F1",          # 03, 3
        "Function_4_3A6",          # 04, 4
        "Function_5_3AA",          # 05, 5
        "Function_6_460",          # 06, 6
        "Function_7_611",          # 07, 7
        "Function_8_6CD",          # 08, 8
        "Function_9_736",          # 09, 9
        "Function_10_73A",         # 0A, 10
        "Function_11_863",         # 0B, 11
        "Function_12_8AE",         # 0C, 12
        "Function_13_9B1",         # 0D, 13
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_23C"),
        (1, "loc_248"),
        (2, "loc_254"),
        (3, "loc_260"),
        (4, "loc_26C"),
        (5, "loc_278"),
        (6, "loc_284"),
        (SWITCH_DEFAULT, "loc_290"),
    )


    label("loc_23C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_248")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_254")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_260")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_26C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_278")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_2B3")

    Return()

    # Function_0_204 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    SetChrFlags(0xA, 0x10)
    SetChrPos(0xC, -68850, 0, -980, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9")
    SetChrFlags(0xC, 0x10)

    label("loc_2D9")

    SetChrPos(0xD, -68700, 0, 340, 180)
    SetChrFlags(0xD, 0x10)
    Return()

    # Function_1_2B4 end

    def Function_2_2F0(): pass

    label("Function_2_2F0")

    Return()

    # Function_2_2F0 end

    def Function_3_2F1(): pass

    label("Function_3_2F1")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""The Kingdom of Sweets Vol.1" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_3A2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Mix Gelato"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3A2")

    TalkEnd(0xFF)
    Return()

    # Function_3_2F1 end

    def Function_4_3A6(): pass

    label("Function_4_3A6")

    Call(0, 5)
    Return()

    # Function_4_3A6 end

    def Function_5_3AA(): pass

    label("Function_5_3AA")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_407")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_407")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_427")
    OP_AF(0xC9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_457")

    label("loc_427")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43B")
    Jump("loc_457")

    label("loc_43B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_457")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_457")

    Jump("loc_3B7")

    label("loc_45C")

    TalkEnd(0x8)
    Return()

    # Function_5_3AA end

    def Function_6_460(): pass

    label("Function_6_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B3")

    ChrTalk(
        0x8,
        (
            "Isn't it rare to see\x01",
            "you loitering around\x01",
            "at such an hour?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, closing time has\x01",
            "already passed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For you, it's ok.\x01",
            "Look all you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks, Oscar. \x01",
            "We'll do that by all m......\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00603F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-If we're going to buy, it seems\x01",
            "it would be better doing it fast.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_610")

    label("loc_5B3")


    ChrTalk(
        0x8,
        (
            "Well, closing time has\x01",
            "already passed, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "For you, it's ok.\x01",
            "Look all you want.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_610")

    Return()

    # Function_6_460 end

    def Function_7_611(): pass

    label("Function_7_611")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well then, it's about\x01",
            "time to tidy up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A bakery preparations start early \x01",
            "in the morning at 3:00, after all.\x01",
            "In preparation for tomorrow,\x01",
            "I'll have to go to rest quickly.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_611 end

    def Function_8_6CD(): pass

    label("Function_8_6CD")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The bread I made\x01",
            "is losing in sales\x01",
            "to Oscar's...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Grrr, tomorrow, for sure, I'll...!!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_6CD end

    def Function_9_736(): pass

    label("Function_9_736")

    Call(0, 10)
    Return()

    # Function_9_736 end

    def Function_10_73A(): pass

    label("Function_10_73A")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_747")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_797")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_797")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B7")
    OP_AF(0x29)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_85A")

    label("loc_7B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CB")
    Jump("loc_85A")

    label("loc_7CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xB,
        (
            "Hey, welcome! \x01",
            "Do you need something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I intend to keep the\x01",
            "store open for a little\x01",
            "more, so take your time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85A")

    Jump("loc_747")

    label("loc_85F")

    TalkEnd(0xB)
    Return()

    # Function_10_73A end

    def Function_11_863(): pass

    label("Function_11_863")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_878")
    Call(0, 12)
    Jump("loc_8AA")

    label("loc_878")


    ChrTalk(
        0xFE,
        (
            "Uh uh, oh Momo, she\x01",
            "really had a lot of fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AA")

    TalkEnd(0xFE)
    Return()

    # Function_11_863 end

    def Function_12_8AE(): pass

    label("Function_12_8AE")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "......And then, and then... \x01",
            "Ryｹ tried to enter\x01",
            "Orchis Tower on his own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "And when he did it, even Henri and\x01",
            "Momo were scolded by an officer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My my... \x01",
            "That was terrible, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "But, but... \x01",
            "It was really fun...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_8AE end

    def Function_13_9B1(): pass

    label("Function_13_9B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C6")
    Call(0, 12)
    Jump("loc_A60")

    label("loc_9C6")


    ChrTalk(
        0xFE,
        (
            "Ryｹ was fun.\x01",
            "He tried to make it seem like\x01",
            "it was all Henri's fault...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But he was found out at\x01",
            "once and scolded even\x01",
            "more. *chuckle chuckle*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A60")

    TalkEnd(0xFE)
    Return()

    # Function_13_9B1 end

    SaveToFile()

Try(main)
