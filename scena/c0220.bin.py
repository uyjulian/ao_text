from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0220.bin",                # FileName
        "c0220",                    # MapName
        "c0220",                    # Location
        0x000D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 13, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0220",                  # 0
        "Lawyer Ian",             # 1
        "Pete",                   # 2
        "Salaryman",              # 3
        "Detective Emma",         # 4
        "Policeman",              # 5
        "Detective",              # 6
        "Detective",              # 7
    ))

    AddCharChip((
        "chr/ch05900.itc",                   # 00
        "chr/ch05902.itc",                   # 01
        "chr/ch22200.itc",                   # 02
        "chr/ch27802.itc",                   # 03
        "chr/ch30500.itc",                   # 04
        "chr/ch30000.itc",                   # 05
        "chr/ch27600.itc",                   # 06
        "chr/ch27800.itc",                   # 07
    ))

    DeclNpc(4510,    1169,    15779,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(12869,   1000,    4809,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(2259,    140,     5500,    90,   453,  0x0, 0,   3,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(5289,    1019,    16959,   225,  389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(1370,    29,      1990,    180,  389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294958786, 0,       45979,   0,    389,  0x0, 0,   6,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294966727, 29,      39380,   90,   389,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(14350,   1000,    4294967226, 2000,    14350,   2500,    4294967226, 0x007C, 0,  20, 0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_4F7",          # 02, 2
        "Function_3_599",          # 03, 3
        "Function_4_2209",         # 04, 4
        "Function_5_3818",         # 05, 5
        "Function_6_3962",         # 06, 6
        "Function_7_3AFB",         # 07, 7
        "Function_8_3B8F",         # 08, 8
        "Function_9_3D19",         # 09, 9
        "Function_10_3EB0",        # 0A, 10
        "Function_11_4C70",        # 0B, 11
        "Function_12_4F1B",        # 0C, 12
        "Function_13_564B",        # 0D, 13
        "Function_14_77B5",        # 0E, 14
        "Function_15_7800",        # 0F, 15
        "Function_16_784B",        # 10, 16
        "Function_17_7896",        # 11, 17
        "Function_18_78E1",        # 12, 18
        "Function_19_792C",        # 13, 19
        "Function_20_7977",        # 14, 20
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1F0 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D8")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 5510, 1020, 16030, 225)
    Jump("loc_4C9")

    label("loc_2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_4C9")

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30F")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_349")
    SetChrPos(0x8, 3150, 1020, 12920, 0)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4C9")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_368")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_387")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_39F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_4C9")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_408")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C3")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DA")
    SetChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_3FE")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_403")

    label("loc_3FE")

    SetChrFlags(0x8, 0x80)

    label("loc_403")

    Jump("loc_4C9")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4C9")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_42E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4C9")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_452")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x10)
    Jump("loc_4C9")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_471")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_490")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4AF")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jump("loc_4C9")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C9")
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_4C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F6")
    SetMapFlags(0x10000000)
    Event(0, 13)

    label("loc_4F6")

    Return()

    # Function_1_2A0 end

    def Function_2_4F7(): pass

    label("Function_2_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_540")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_57F")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_598")
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x0, 0x10)

    label("loc_598")

    Return()

    # Function_2_4F7 end

    def Function_3_599(): pass

    label("Function_3_599")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B3")
    Call(0, 12)
    Jump("loc_2205")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_933")

    ChrTalk(
        0xFE,
        (
            "#02200FIt's all of you... Did\x01",
            "you see Mr. Dieter's\x01",
            "address?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02200FYou're confused as to this\x01",
            "sudden turn of events... Is\x01",
            "that what you're trying to say?\x02\x03",
            "#02203FA majority of the citizens must\x01",
            "be feeling the same way.\x02\x03",
            "#02201FHowever, the "Secret War"\x01",
            "between the major powers is the\x01",
            "absolute truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F...Those "Accidents"\x01",
            ""uncle" spoke of, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FYes...\x02\x03",
            "#02201FHowever, we pretend not to\x01",
            "notice this truth and enjoy\x01",
            "our happiness.\x02\x03",
            "This is the sin Dieter\x01",
            "spoke of, borne by everyone\x01",
            "living in Crossbell.\x02\x03",
            "#02203FAs an independent nation,\x01",
            "we will need to face that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FLawyer Ian...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203F...Sorry, that address\x01",
            "affected me and I got carried\x01",
            "away.\x02\x03",
            "#02200FIn any case... The die have\x01",
            "already been cast.\x02\x03",
            "#02203FWhere do we go from here? That\x01",
            "is a problem each citizen must\x01",
            "consider individually.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 1)
    Jump("loc_9BD")

    label("loc_933")


    ChrTalk(
        0xFE,
        (
            "#02203FThe dice have already been\x01",
            "case.\x02\x03",
            "#02200FWhere do we go from here? That\x01",
            "is a problem each citizen must\x01",
            "consider individually.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9BD")

    Jump("loc_2205")

    label("loc_9C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E84")

    ChrTalk(
        0xFE,
        (
            "#02203F*sigh*... That visitor's\x01",
            "company materials...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLawyer Ian... You seem\x01",
            "rather busy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "#02205FAh, it's all of you.\x02\x03",
            "#02203FIt seems he lost most of\x01",
            "what he had in that\x01",
            "attack.\x02\x03",
            "#02200FI've been consulting with\x01",
            "him for a week and haven't\x01",
            "had time to relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F...Seems tough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FHmm... But it can't be\x01",
            "helped.\x02\x03",
            "#02200FMany people have lost\x01",
            "meeting places or their\x01",
            "very workplace itself.\x02\x03",
            "As a lawyer, I must do\x01",
            "all I can for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, that's our Mr.\x01",
            "Beardy Bear for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FB-But... How are you\x01",
            "doing with drafting the\x01",
            "constitution?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02200FYeah, I managed to complete it. I\x01",
            "just submitted it to the state\x01",
            "government.\x02\x03",
            "#02202FWe can do it if we try, I suppose.\x01",
            "Thanks to that, I haven't had time\x01",
            "to sleep, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FWithout rest, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FUmm, please don't overdo\x01",
            "it, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02202FHaha, sorry to worry you.\x02\x03",
            "#02203FI plan to fit in as many\x01",
            "appointments as possible\x01",
            "today, and sleep well tonight.\x02\x03",
            "#02200F...Well then. My clients are\x01",
            "waiting, so I'll excuse\x01",
            "myself.\x02\x03",
            "You guys must have a lot of\x01",
            "requests. Please do your best\x01",
            "on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSure, and thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_F0A")

    label("loc_E84")


    ChrTalk(
        0xFE,
        (
            "#02200FAs a lawyer, I plan to\x01",
            "do all I can for the\x01",
            "citizens.\x02\x03",
            "You guys must have a lot\x01",
            "of requests. Please do\x01",
            "your best on them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0A")

    Jump("loc_2205")

    label("loc_F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101F")

    ChrTalk(
        0xFE,
        (
            "#02200FThe attack on Mainz delayed the\x01",
            "referendum...\x02\x03",
            "There are citizens who think the attack was\x01",
            "a ploy by the Empire or Republic to get us\x01",
            "to withdraw the independence proposal.\x02\x03",
            "#02203FI didn't think either would do something\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10CF")

    label("loc_101F")


    ChrTalk(
        0xFE,
        (
            "#02200FI believe this incident a ploy by\x01",
            "the Empire or Republic to make us\x01",
            "withdraw the independence proposal.\x02\x03",
            "#02203FI didn't think either would do\x01",
            "something like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CF")

    Jump("loc_2205")

    label("loc_10D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_16AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A3")

    ChrTalk(
        0xFE,
        "#02200FAh, you all are...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_128A")

    ChrTalk(
        0x101,
        (
            "#00004FLawyer Ian... Thank you\x01",
            "for your help yesterday.\x02\x03",
            "#00000FThat evidence you\x01",
            "discovered proved\x01",
            "useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FAh, I take it you heard from\x01",
            "Pete, then. It seems Minneth\x01",
            "is now a wanted man.\x02\x03",
            "#02202FHaha, though you say that, I\x01",
            "only helped you finish him\x01",
            "off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FNo, you were a big help.\x02\x03",
            "#00000FEven though you're busy\x01",
            "drafting the\x01",
            "constitution...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E6")

    label("loc_128A")


    ChrTalk(
        0x101,
        (
            "#00000FLawyer Ian, it's been a\x01",
            "while.\x02\x03",
            "It seems you're busy\x01",
            "drafting the\x01",
            "constitution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E6")


    ChrTalk(
        0xFE,
        (
            "#02200FYeah. Even so, it's\x01",
            "coming together.\x02\x03",
            "I was thinking of making\x01",
            "some coffee and taking a\x01",
            "break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FOh... Sorry to intrude\x01",
            "on your break time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02202FDon't mention it. Chatting\x01",
            "with all of you makes a\x01",
            "nice change of pace.\x02\x03",
            "#02205FBy the way. It seems you\x01",
            "all were assigned to\x01",
            "yesterday's derailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we've already\x01",
            "determined the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FLeaving out the\x01",
            "details... It's certain\x01",
            "the cause is unnatural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02205FHmm, is that so...\x02\x03",
            "#02203F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FLawyer Ian... What's\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203F...No, I was just\x01",
            "thinking it's a relief\x01",
            "that no one died.\x02\x03",
            "#02200FAnyway, things are more\x01",
            "dangerous lately. You\x01",
            "all should be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 0)
    Jump("loc_16A9")

    label("loc_15A3")


    ChrTalk(
        0xFE,
        (
            "#02200FThe constitution draft is\x01",
            "coming along, but there's\x01",
            "still room for improvement.\x02\x03",
            "#02203FThough it's a solemn duty,\x01",
            "I must do my very best, for\x01",
            "the future of Crossbell.\x02\x03",
            "#02200FI will settle for nothing\x01",
            "less than the greatest\x01",
            "constitution draft ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A9")

    Jump("loc_2205")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1768")

    ChrTalk(
        0x8,
        (
            "#02200FRegarding this incident...\x01",
            "I've helped you as much as\x01",
            "my schedule will allow.\x02\x03",
            "#02202FHaha, I'll turn up every\x01",
            "now and then. Good luck\x01",
            "with your investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2205")

    label("loc_1768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1822")

    ChrTalk(
        0x8,
        (
            "#02200FRegarding this incident...\x01",
            "I've helped you as much as\x01",
            "my schedule will allow.\x02\x03",
            "#02202FHaha, I'll turn up every\x01",
            "now and then. Good luck\x01",
            "with your investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2205")

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1830")
    Jump("loc_2205")

    label("loc_1830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_183E")
    Jump("loc_2205")

    label("loc_183E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1AB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A14")

    ChrTalk(
        0xFE,
        (
            "#02205FOh, it's you all. It's unusual for\x01",
            "you to come at night.\x02\x03",
            "#02200FAnd since Dudley is with you... Could\x01",
            "a problem or something have arisen\x01",
            "related to tomorrow's conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FWe're just going to confirm\x01",
            "that now.\x02\x03",
            "#00600FTo achieve perfection, there's\x01",
            "nothing like crushing\x01",
            "imperfect elements in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FHm, there's nothing like\x01",
            "being too prepared.\x02\x03",
            "#02200FI don't know the\x01",
            "details, but... Do your\x01",
            "very best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AB4")

    label("loc_1A14")


    ChrTalk(
        0xFE,
        (
            "#02200FWell then... That about does\x01",
            "it for the preparations, I'd\x01",
            "say.\x02\x03",
            "#02203FIn preparation for tomorrow,\x01",
            "I'll go to bed earlier than\x01",
            "usual this evening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB4")

    Jump("loc_2205")

    label("loc_1AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC4")

    ChrTalk(
        0xFE,
        (
            "#02200FIt seems the heads of state\x01",
            "are visiting Crossbell.\x02\x03",
            "#02203FI feel city security has been\x01",
            "raised even higher for the\x01",
            "first day of the conference.\x02\x03",
            "#02200FIt's at times like this that\x01",
            "trouble occurs. Please be\x01",
            "careful, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C56")

    label("loc_1BC4")


    ChrTalk(
        0xFE,
        (
            "#02203FIt seems the heads of state\x01",
            "are visiting Crossbell.\x02\x03",
            "#02200FIt's at times like this\x01",
            "that trouble occurs. Please\x01",
            "be careful, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C56")

    Jump("loc_2205")

    label("loc_1C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAE")

    ChrTalk(
        0xFE,
        (
            "#02200FThe trade conference finally\x01",
            "opens tomorrow.\x02\x03",
            "The heads of state from each\x01",
            "country are planning to attend\x01",
            "the unveiling ceremony, but...\x02\x03",
            "If by any chance something\x01",
            "happens to any of them, it will\x01",
            "cause an international incident.\x02\x03",
            "As police, you must do your very\x01",
            "best to ensure that doesn't\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E3D")

    label("loc_1DAE")


    ChrTalk(
        0xFE,
        (
            "#02200FIf you are ever concerned about\x01",
            "anything, please feel free to\x01",
            "consult with me about it anytime.\x02\x03",
            "I will help you as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3D")

    Jump("loc_2205")

    label("loc_1E42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_207A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDF")

    ChrTalk(
        0xFE,
        (
            "#02203FIt seems Heiyue's acquisition\x01",
            "of the Revache remnants is\x01",
            "proceeding steadily.\x02\x03",
            "#02201FI don't want to think about\x01",
            "what will happen if that\x01",
            "place falls into their hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FI see... That would a\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203F...Although, we can't do\x01",
            "anything about it. We'll\x01",
            "just have to accept it...\x02\x03",
            "#02200FGood grief... Crossbell\x01",
            "certainly has its fair\x01",
            "share of problems.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2075")

    label("loc_1FDF")


    ChrTalk(
        0xFE,
        (
            "#02200FIt's only a matter of\x01",
            "time before Heiyue buys\x01",
            "up the Revache remnants.\x02\x03",
            "Good grief... Crossbell\x01",
            "certainly has its fair\x01",
            "share of problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2075")

    Jump("loc_2205")

    label("loc_207A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217D")

    ChrTalk(
        0xFE,
        (
            "#02203FIt seems the citizens have\x01",
            "great expectations of the\x01",
            "Special Support Section.\x02\x03",
            "#02202FAlthough you'll have more\x01",
            "requests than before, please\x01",
            "do your best on them.\x02\x03",
            "As each one piles up, so too\x01",
            "do the hopes of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2205")

    label("loc_217D")


    ChrTalk(
        0xFE,
        (
            "#02200FNaturally, I too am\x01",
            "expecting great things\x01",
            "from the Support Section.\x02\x03",
            "#02202FPlease, live up to the\x01",
            "citizens' expectations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2205")

    TalkEnd(0xFE)
    Return()

    # Function_3_599 end

    def Function_4_2209(): pass

    label("Function_4_2209")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_232D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222B")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_222B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2235")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2328")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Read Ian's letter\x01",      # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A6")
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2323")

    label("loc_22A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22BA")
    Jump("loc_2323")

    label("loc_22BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2323")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        (
            "Everyone... Thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please... Take care of\x01",
            "Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2323")

    Jump("loc_2235")

    label("loc_2328")

    Jump("loc_3814")

    label("loc_232D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_233B")
    Jump("loc_3814")

    label("loc_233B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23CF")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood drafted the\x01",
            "constitution for\x01",
            "Crossbell's independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a leading figure, he\x01",
            "must consider various\x01",
            "things...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3814")

    label("loc_23CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2473")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood seems very\x01",
            "busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I were a full-fledged lawyer,\x01",
            "I'd be able to consult with you\x01",
            "instead of Mr. Grimwood, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24F7")

    label("loc_2473")


    ChrTalk(
        0xFE,
        (
            "...Anyway, for now, I'm\x01",
            "doing all I can to\x01",
            "assist him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to get a\x01",
            "vacation, I have to hurry\x01",
            "and finish up my work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24F7")

    Jump("loc_3814")

    label("loc_24FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2636")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25BD")

    ChrTalk(
        0xFE,
        (
            "To think an armed group\x01",
            "is occupying Mainz...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The people there have\x01",
            "committed no crime. How\x01",
            "awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we citizens\x01",
            "can do anything about\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2631")

    label("loc_25BD")


    ChrTalk(
        0xFE,
        (
            "It seems Mr. Grimwood is\x01",
            "worried about this\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we citizens\x01",
            "can do anything about\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2631")

    Jump("loc_3814")

    label("loc_2636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2990")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294B")

    ChrTalk(
        0xFE,
        (
            "I've got to finalize\x01",
            "yesterday's incident in\x01",
            "Armorica...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I left it to Mr. Grimwood,\x01",
            "important materials would get lost\x01",
            "in that mountain of paperwork again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_27B9")

    ChrTalk(
        0x101,
        (
            "#00000FHaha... But I'm glad you\x01",
            "were able to resolve it.\x02\x03",
            "Thanks for all your\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, don't mention it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The Special Support\x01",
            "Section did a nice job\x01",
            "on that case too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2943")

    label("loc_27B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_2855")

    ChrTalk(
        0x101,
        (
            "#00003F(An incident in Armorica...\x01",
            "Could it have anything to\x01",
            "do with Minneth?)\x02\x03",
            "(...I knew we should have\x01",
            "stuck with it 'til the\x01",
            "end...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2943")

    label("loc_2855")


    ChrTalk(
        0x101,
        (
            "#00005FAn incident in\x01",
            "Armorica... What\x01",
            "happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, you see there was\x01",
            "this corrupt merchant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Ah, sorry. I have a\x01",
            "duty of confidentiality\x01",
            "on the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI-I see... Well I'm glad\x01",
            "you were able to resolve\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2943")

    SetScenarioFlags(0x16C, 2)
    Jump("loc_298B")

    label("loc_294B")


    ChrTalk(
        0xFE,
        (
            "In any case, I'm glad I\x01",
            "could help the people of\x01",
            "Armorica.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298B")

    Jump("loc_3814")

    label("loc_2990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_29B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AB")
    SetScenarioFlags(0x0, 1)
    Jump("loc_29AB")

    label("loc_29AB")

    Jump("loc_3814")

    label("loc_29B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A9F")

    ChrTalk(
        0xFE,
        (
            "The Armorica Village\x01",
            "incident brought to light\x01",
            "a prior, similar case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can find clues in\x01",
            "the most unlikely of\x01",
            "places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for\x01",
            "Mr. Grimwood, he went to\x01",
            "Harold's house.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B2E")

    label("loc_2A9F")


    ChrTalk(
        0xFE,
        (
            "The Armorica Village\x01",
            "incident brought to light\x01",
            "a prior, similar case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for\x01",
            "Mr. Grimwood, he went to\x01",
            "Harold's house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2E")

    Jump("loc_2D11")

    label("loc_2B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_END)), "loc_2C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0B")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is going to\x01",
            "be extremely busy drafting\x01",
            "the constitution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For that reason, I can't\x01",
            "overlook an incident\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, allow me to help\x01",
            "you as much as I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C81")

    label("loc_2C0B")


    ChrTalk(
        0xFE,
        (
            "Because he's busy,\x01",
            "please allow me to help\x01",
            "as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, allow me to help\x01",
            "you as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C81")

    Jump("loc_2D11")

    label("loc_2C86")


    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is holed up\x01",
            "on 2F drafting the\x01",
            "constitution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He'll be very busy today\x01",
            "as well. I need to do my\x01",
            "best to support him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D11")

    Jump("loc_3814")

    label("loc_2D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_32CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3235")

    ChrTalk(
        0xFE,
        (
            "Ah, the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is holed up\x01",
            "on 2F, working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FDoesn't it seem like\x01",
            "he's been very busy\x01",
            "lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, actually...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he was asked by the mayor\x01",
            "to write the draft constitution\x01",
            "for state independence.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E6C")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2E6C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E92")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2E92")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EB8")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2EB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EDE")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2EDE")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007FWhaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FA Constitution... Not a\x01",
            "state law?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FA Constitution is the fundamental law\x01",
            "that establishes the basic conditions\x01",
            "of a state's existence.\x02\x03",
            "#00100FAs the supreme law that establishes a\x01",
            "nation's soverignty, government and\x01",
            "fundamental principles, interference\x01",
            "from other nations is not permitted.\x02\x03",
            "It's something that's absolutely\x01",
            "indispensable for having the\x01",
            "appearance of a nation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F...Right... Another\x01",
            "complicated thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FHowever, I think that\x01",
            "someone like Lawyer Ian\x01",
            "is truly suited for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. Our Mr. Beardy Bear is\x01",
            "active in international affairs,\x01",
            "so I think he'll do a great job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I'm sure he'll\x01",
            "create a fine\x01",
            "constitution for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, will you say hello\x01",
            "to Lawyer Ian for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will. I think Mr.\x01",
            "Grimwood will be\x01",
            "encouraged by it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 1)
    Jump("loc_32C7")

    label("loc_3235")


    ChrTalk(
        0xFE,
        (
            "It seems the mayor asked\x01",
            "Mr. Grimwood to draft\x01",
            "the constitution for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure he will be\x01",
            "able to create a fine\x01",
            "constitution for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C7")

    Jump("loc_3814")

    label("loc_32CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_335A")

    ChrTalk(
        0xFE,
        (
            "If you're looking for\x01",
            "Mr. Grimwood, he left on\x01",
            "business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have a message\x01",
            "for him, I'll deliver it\x01",
            "to him later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3814")

    label("loc_335A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_33DF")

    ChrTalk(
        0xFE,
        (
            "Oh, this file... It was\x01",
            "put away in the wrong\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, Mr.\x01",
            "Grimwood... This is a\x01",
            "sloppy side of him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3814")

    label("loc_33DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_352F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C4")

    ChrTalk(
        0xFE,
        (
            "Huh? The last client's\x01",
            "consultation fee... It\x01",
            "was rather small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Mr. Grimwood must be\x01",
            "arbitrarily reducing the\x01",
            "fees again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because he's a lawyer,\x01",
            "he has to be firm on\x01",
            "things like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_352A")

    label("loc_34C4")


    ChrTalk(
        0xFE,
        (
            "...Mr. Grimwood must be\x01",
            "arbitrarily reducing the\x01",
            "fees again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness gracious.\x01",
            "*mumble*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_352A")

    Jump("loc_3814")

    label("loc_352F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3683")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35FE")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood has been\x01",
            "especially busy lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because the trade conference\x01",
            "is drawing near, he's been\x01",
            "having more consultations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must do all I can to\x01",
            "support him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_367E")

    label("loc_35FE")


    ChrTalk(
        0xFE,
        (
            "Because the trade conference\x01",
            "is near, he's been having\x01",
            "more consultations lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must do all I can to\x01",
            "support him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367E")

    Jump("loc_3814")

    label("loc_3683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3722")

    ChrTalk(
        0xFE,
        (
            "More customers have been\x01",
            "coming for consultations\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood has been\x01",
            "working non-stop. He's got\x01",
            "to take a break sometime...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3814")

    label("loc_3722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C6")

    ChrTalk(
        0xFE,
        (
            "Ah, the Special Support\x01",
            "Section... It's been a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is at his\x01",
            "desk. Please speak with\x01",
            "him if you need anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3814")

    label("loc_37C6")


    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is at his\x01",
            "desk. Please speak with\x01",
            "him if you need anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3814")

    TalkEnd(0xFE)
    Return()

    # Function_4_2209 end

    def Function_5_3818(): pass

    label("Function_5_3818")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38DA")

    ChrTalk(
        0xFE,
        (
            "The company I work for\x01",
            "was in the destroyed IBC\x01",
            "building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With our workplace gone,\x01",
            "all our activities are\x01",
            "suspended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... What are we\x01",
            "going to do now?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_395E")

    label("loc_38DA")


    ChrTalk(
        0xFE,
        (
            "My workplace in the IBC\x01",
            "building is gone, and all our\x01",
            "business has been suspended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... What are we\x01",
            "going to do now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_395E")

    TalkEnd(0xFE)
    Return()

    # Function_5_3818 end

    def Function_6_3962(): pass

    label("Function_6_3962")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397B")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_397B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A83")

    ChrTalk(
        0xFE,
        (
            "His "Plan"... It's\x01",
            "certain he's spent a\x01",
            "long time working on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Section One is continuing\x01",
            "to search the Grimwood\x01",
            "Law Office premises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Please be careful,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A7B")

    ChrTalk(
        0x10A,
        (
            "#00600FHmm... You handle this\x01",
            "place, Emma.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A7B")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3AF7")

    label("loc_3A83")


    ChrTalk(
        0xFE,
        (
            "Section One is continuing\x01",
            "to search the Ian Grimwood\x01",
            "Law Office premises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Please be careful,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF7")

    TalkEnd(0xFE)
    Return()

    # Function_6_3962 end

    def Function_7_3AFB(): pass

    label("Function_7_3AFB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We're searching the\x01",
            "Grimwood Law Office\x01",
            "premises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've succeeded in unlocking\x01",
            "the door to 2F. I hope we\x01",
            "find some clues up there.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_3AFB end

    def Function_8_3B8F(): pass

    label("Function_8_3B8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8D")

    ChrTalk(
        0xFE,
        (
            "We've found materials relating\x01",
            "to middle age alchemy and the\x01",
            "Ancient Zemurian civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're very old... It\x01",
            "must've taken many years to\x01",
            "amass a collection this big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just when did Ian start\x01",
            "planning all of this?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D15")

    label("loc_3C8D")


    ChrTalk(
        0xFE,
        (
            "They're very old... It\x01",
            "must've taken many years to\x01",
            "amass a collection this big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just when did Ian start\x01",
            "planning all of this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D15")

    TalkEnd(0xFE)
    Return()

    # Function_8_3B8F end

    def Function_9_3D19(): pass

    label("Function_9_3D19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E07")

    ChrTalk(
        0xFE,
        (
            "On this terminal, we found\x01",
            "evidence of frequent\x01",
            "communications with Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Most likely, he manipulated the President\x01",
            "from this location... Or perhaps I should\x01",
            "say he ordered Mr. Crois and the others.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3EAC")

    label("loc_3E07")


    ChrTalk(
        0xFE,
        (
            "Most likely, he manipulated the Mr.\x01",
            "Crois from this location... Or\x01",
            "perhaps I should say he ordered him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we carefully proceed\x01",
            "with this\x01",
            "investigation...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EAC")

    TalkEnd(0xFE)
    Return()

    # Function_9_3D19 end

    def Function_10_3EB0(): pass

    label("Function_10_3EB0")

    EventBegin(0x0)
    Fade(500)
    OP_68(6060, 2320, 15510, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18770, 0)
    SetChrPos(0x101, 7120, 1020, 15230, 270)
    SetChrPos(0x102, 7010, 1020, 16640, 270)
    SetChrPos(0x103, 7000, 1020, 13880, 315)
    SetChrPos(0x104, 8300, 1000, 14190, 270)
    SetChrPos(0xF4, 8600, 1000, 15690, 270)
    SetChrPos(0xF5, 8400, 1000, 17000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_93(0xB, 0x5A, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    OP_0D()

    ChrTalk(
        0x9,
        "#11P*cry*, ooh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PMr. Grimwood... Why...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FPete?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x1F4)

    ChrTalk(
        0x9,
        "#6PE-Everyone?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_406E")

    ChrTalk(
        0xB,
        (
            "#5PDetective Dudley... And\x01",
            "the Support Section too.\x01",
            "Good work out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#11P#00603FThanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4092")

    label("loc_406E")


    ChrTalk(
        0xB,
        (
            "#5PNice work, Support\x01",
            "Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4092")


    ChrTalk(
        0x101,
        (
            "#11P#00001FGood work yourself,\x01",
            "Detective Emma. Are you\x01",
            "searching the premises?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYes... Section One is\x01",
            "looking for any possible\x01",
            "material witnesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIt may seem unfair, but\x01",
            "as Mr. Grimwood's staff,\x01",
            "we need you to testify.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6P*cry*... No, then please\x01",
            "listen to my request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PMr. Grimwood... Before he disappeared,\x01",
            "he said something interesting, and I\x01",
            "want to check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_END)), "loc_42CC")

    ChrTalk(
        0x104,
        (
            "#11P#00308FYeah... He asked you to\x01",
            "clean the desk or\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FThat is indeed concerning.\x01",
            "Why would he ask you that\x01",
            "all of a sudden?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456F")

    label("loc_42CC")


    ChrTalk(
        0x102,
        "#11P#00105FConcerning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P...Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6POnce this state of\x01",
            "emergency with those Magic\x01",
            "Soldiers is lifted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PHe asked me to return to\x01",
            "this office and clean\x01",
            "his desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FCleaning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PYes. From the start, I\x01",
            "thought he left in a\x01",
            "hurry, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PAlthough I normally do Mr. Grimwood's\x01",
            "cleaning, he regularly tells me to keep\x01",
            "away from his desk as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PHe said to leave it alone since there\x01",
            "are a lot of things on there a helper\x01",
            "such as myself shouldn't see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00108FLawyer Ian... It seems\x01",
            "like he was really\x01",
            "concerned about that...\x02\x03",
            "#00106FI don't get why he would\x01",
            "ask you to clean the\x01",
            "desk now, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_456F")


    ChrTalk(
        0x9,
        (
            "#6PI'm sure the answer will\x01",
            "be found in Ian's desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P...Here.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Pete held out a sealed\x01",
            "letter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_45EB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_45EB)
    Sleep(50)

    def lambda_45FB():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_45FB)
    Sleep(50)

    def lambda_460B():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_460B)
    Sleep(50)

    def lambda_461B():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_461B)
    Sleep(50)

    def lambda_462B():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_462B)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46F5")

    ChrTalk(
        0x105,
        "#11P#10401FDid Ian leave this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4762")

    label("loc_46F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_472E")

    ChrTalk(
        0x109,
        "#11P#10101FDid Ian leave this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4762")

    label("loc_472E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4762")

    ChrTalk(
        0x106,
        "#11P#10701FDid Ian leave this?\x02",
    )

    CloseMessageWindow()

    label("loc_4762")


    ChrTalk(
        0x101,
        "#11P#00001F...Can we read it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P...(*nods*)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    Call(0, 11)

    ChrTalk(
        0x101,
        "#11P#00006F...Lawyer Ian...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_480D")

    ChrTalk(
        0x101,
        "#11P#00008F...............\x02",
    )

    CloseMessageWindow()
    Jump("loc_4872")

    label("loc_480D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4842")

    ChrTalk(
        0x109,
        "#11P#10108F...............\x02",
    )

    CloseMessageWindow()
    Jump("loc_4872")

    label("loc_4842")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4872")

    ChrTalk(
        0x105,
        "#11P#10408F...............\x02",
    )

    CloseMessageWindow()

    label("loc_4872")


    ChrTalk(
        0xB,
        (
            "#5P...We'll take custody of\x01",
            "the other documents on\x01",
            "his desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PIt's a giant memo of how\x01",
            "to deal with all his\x01",
            "current clients...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAnd there are papers\x01",
            "that arrange for formal\x01",
            "guardianship for Pete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6POoh, Mr. Grimwood... Why\x01",
            "did you have to do\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_498A():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_498A)
    Sleep(50)

    def lambda_499A():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_499A)
    Sleep(50)

    def lambda_49AA():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_49AA)
    Sleep(50)

    def lambda_49BA():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_49BA)
    Sleep(50)

    def lambda_49CA():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_49CA)
    Sleep(50)

    def lambda_49DA():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_49DA)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(500)

    ChrTalk(
        0x9,
        (
            "#6PForget about Mr. Grimwood who\x01",
            "did so much for me? There's\x01",
            "no way I can do that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00106FPete...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00208F...Lawyer Ian is a big\x01",
            "idiot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00306FYeah, I won't say anything about the man\x01",
            "himself, but I can't agree with leaving this\x01",
            "kind of letter for everyone he left behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F...Exactly right.\x02\x03",
            "#00008FPete, we intend to go see\x01",
            "Lawyer Ian right away.\x02\x03",
            "#00001FThere, we'll learn the\x01",
            "truth... And bring Lawyer Ian\x01",
            "and the others back with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PE-Everyone... *cry*,\x01",
            "thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PPlease... Take care of\x01",
            "Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x9, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0x9, 0xE1, 0x0)
    OP_93(0xB, 0xE1, 0x0)
    SetScenarioFlags(0x1BD, 6)
    EventEnd(0x5)
    Return()

    # Function_10_3EB0 end

    def Function_11_4C70(): pass

    label("Function_11_4C70")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(18, 0, 40, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─Dear Pete. First of all, I want to apologize for\x01",
            "suddenly leaving your side. I once accepted your\x01",
            "guardianship, and once I put you to work in my\x01",
            "office, I lived many, happy days. One fateful day,\x01",
            "I became ruled by grief and sorrow, and ever since\x01",
            "then, I have lived only to complete a certain plan.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 40, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Because of you I was troubled for a while, but this\x01",
            "plan cannot be stopped. I cannot be forgiven for\x01",
            "going back on my word. Pete, please... I want you to\x01",
            "forget about me, and live a happy life. From a far-\x01",
            "off place, I pray to the Goddess that your wisdom\x01",
            "will make you into a fine adult. ──Ian Grimwood.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_4C70 end

    def Function_12_4F1B(): pass

    label("Function_12_4F1B")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    OP_68(4790, 1920, 14330, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20480, 0)
    SetChrPos(0x101, 4830, 1020, 12570, 0)
    SetChrPos(0x102, 3990, 1020, 12720, 0)
    SetChrPos(0x109, 5650, 1000, 11990, 0)
    SetChrPos(0x105, 2910, 1000, 11990, 0)
    SetChrSubChip(0x8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5P#02205FOh, it's you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt's been a while,\x01",
            "Lawyer Ian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02200FHaha, it sure has. I heard\x01",
            "you temporarily suspended\x01",
            "your activities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's right. We've resumed our\x01",
            "duties. I'm looking forward to\x01",
            "working with you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02200FHaha, I see. And you've\x01",
            "added new members for\x01",
            "your fresh start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FYou're the famous Mr.\x01",
            "Beardy Bear, if I'm not\x01",
            "mistaken?\x02\x03",
            "#10304FHaha, I'm looking\x01",
            "forward to working with\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5P#02205FOh, how polite.\x02\x03",
            "#02203FUmm, I know I have a\x01",
            "business card here\x01",
            "somewhere...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5247")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5247")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_526D")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_526D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5293")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5293")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52B9")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_52B9")

    Sleep(1000)
    TurnDirection(0x109, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x109,
        (
            "#10106FW-Wazy... Respect for\x01",
            "your superiors is a\x01",
            "thing, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FWell, Lawyer Ian is easy\x01",
            "to get along with.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5P#02202FHaha, no, no... When it comes to\x01",
            "personal relationships,\x01",
            "introductions are very important.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x109, 0x0, 0x1F4)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "─Ahem. Allow me to introduce\x01",
            "myself once again.\x02\x03",
            "My name is Ian Grimwood. I am an\x01",
            "attorney, and I work as head of\x01",
            "this law office.\x02\x03",
            "Ladies and gentlemen of the\x01",
            "Support Section, I look forward to\x01",
            "working with all of you once\x02\x03",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x109,
        (
            "#10100FSame here. Good to be\x01",
            "working with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe might have various\x01",
            "things to discuss with\x01",
            "you again.\x02\x03",
            "#00004FWhen that time comes,\x01",
            "please lend us your aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02200FSure, feel free to stop\x01",
            "by anytime.\x02\x03",
            "I'd be happy to give you\x01",
            "advice whenever the need\x01",
            "arises.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x12C, 4)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_4F1B end

    def Function_13_564B(): pass

    label("Function_13_564B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 6600, 140, 5500, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03002.itc", 0x23)
    OP_68(-940, 1300, -180, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, -2710, 0, -490, 90)
    SetChrPos(0x102, -2710, 0, -490, 90)
    SetChrPos(0x103, -2710, 0, -490, 90)
    SetChrPos(0x104, -2710, 0, -490, 90)
    SetChrPos(0x109, -2710, 0, -490, 90)
    SetChrPos(0x105, -2710, 0, -490, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 16)
    Sleep(700)
    OP_68(2570, 1300, 1440, 5000)
    MoveCamera(65, 23, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(20900, 5000)
    BeginChrThread(0x104, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 18)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 19)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)

    ChrTalk(
        0x8,
        "#02205FOh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FLawyer Ian!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FThank goodness... So you\x01",
            "are in the office today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FYes, I taking a break\x01",
            "just now, but...\x02\x03",
            "#02201FHmm, do you need a\x01",
            "consultation on\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSo you already know...\x01",
            "You're quite sharp, Mr.\x01",
            "Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FHaha. If it's the face of\x01",
            "someone with a request, I've\x01",
            "seen thousands of them already.\x02\x03",
            "#02200FHave a seat there. I'm busy\x01",
            "too, but I'll hear you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FExcuse us... and thank\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others explained Minneth's\x01",
            "profile they had learned the previous day\x01",
            "as well as his actions...\x02\x03",
            "They also mentioned the confirmation that\x01",
            "Minneth was collecting Armorica land\x01",
            "deeds they obtained earlier that day.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x1)
    SetChrSubChip(0x8, 0x0)
    OP_68(5320, 500, 6810, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21670, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 2310, 200, 5400, 90)
    SetChrPos(0x102, 2310, 200, 4570, 90)
    SetChrPos(0x103, 2260, 200, 6070, 90)
    SetChrPos(0x104, 4530, 200, 7520, 180)
    SetChrPos(0x109, 3780, 200, 7520, 180)
    SetChrPos(0x105, 5160, 200, 7520, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#02200FHmm... I see. I understand the\x01",
            "general situation.\x02\x03",
            "Ordinarily, I would have liked to\x01",
            "take a case like this one, but...\x02\x03",
            "#02203FAs I'm sure you are aware, I have\x01",
            "important constitution drafting\x01",
            "work to handle right now.\x02\x03",
            "#02203FI'm sorry, but it doesn't look\x01",
            "like I can spare the time to look\x01",
            "into this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FToo bad... It can't be\x01",
            "helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FEven if you could just\x01",
            "give us some advice, it\x01",
            "would be a great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FSorry... I'll give you\x01",
            "whatever advice I can\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThank you very much.\x02\x03",
            "#00001FSo... What do you think?\x02\x03",
            "Minneth's actions up to the\x01",
            "present... Can you sense any\x01",
            "sign of a crime behind them?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#02203FI do have one idea.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00309FWhoa, seriously!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FYes... A friend in the\x01",
            "Empire once told me about a\x01",
            "very similar case of his.\x02\x03",
            "Although I can't say the\x01",
            "circumstances are exactly\x01",
            "the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Right now, we're just looking for\x01",
            "anything that would make a good\x01",
            "starting point in our investigation.\x02\x03",
            "#00003FThat idea... Will you tell us about\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FHmm, very well. It is\x01",
            "none other than you all\x01",
            "who is asking, after all.\x02\x03",
            "#02203FAhem, then...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0x8,
        (
            "#02203F─Several years ago... A single man visited\x01",
            "the house of a certain Erebonian Baron.\x02\x03",
            "#02201FThe man's name was Littner... He called\x01",
            "himself a master businessman working for a\x01",
            "certain brewing company.\x02\x03",
            "To the baron, Littner presented a certain way\x01",
            "to make it big, fast.\x02\x03",
            "The great barley fields that had been passed\x01",
            "down in the baron's family for generations...\x01",
            "They would be used to used to expand his\x01",
            "company's business.\x02\x03",
            "#02203FA brewery would be constructed in the baron's\x01",
            "territory, and the management thereof left to\x01",
            "his family... That was the general idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F!! That sounds like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha... The more I hear,\x01",
            "the more similar it\x01",
            "sounds to our case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F─Accepting the deal, the baron signed on\x01",
            "to Littner's contract.\x02\x03",
            "#02200FThen, under the pretexts of management and\x01",
            "brewery construction, some of the land was\x01",
            "temporarily transferred to Littner.\x02\x03",
            "Also, some of the baron's fortune was\x01",
            "converted into stock in preparation for\x01",
            "starting the business...\x02\x03",
            "#02203FBut then... Littner took the deeds and\x01",
            "fortune and disappeared.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305FWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FHaving suddenly lost contact with\x01",
            "Littner, the baron's people were\x01",
            "flustered...\x02\x03",
            "It was then the baron realized the\x01",
            "gravity of the situation.\x02\x03",
            "#02201FThe strangest thing happened. Littner\x01",
            "sold the deeds to a third party.\x02\x03",
            "As prime real estate for building\x01",
            "villas.\x02\x03",
            "#02203F─In the end, the baron was left only\x01",
            "with an enormous debt... Before long, he\x01",
            "ended up losing his entire territory.\x02\x03",
            "Having lost his territory, he was\x01",
            "stripped of his rank. No one knows what\x01",
            "happened to him after that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWow... I can't believe\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FHe just went off and\x01",
            "sold someone else's\x01",
            "property...\x02\x03",
            "That's too cruel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F─That case was the first\x01",
            "that came to mind, based on\x01",
            "what you told me.\x02\x03",
            "Lie and gain their trust.\x01",
            "Then, at the very end, make\x01",
            "off with a huge fortune...\x02\x03",
            "#02201FIt is said to be a\x01",
            "technique for committing\x01",
            ""fraud".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FFraud!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIn other words, Minneth\x01",
            "isn't an employee of the\x01",
            "Quincy Company.\x02\x03",
            "#00200FYou're saying it's\x01",
            "possible he's just a\x01",
            "fraudster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FYes... Though not\x01",
            "definite, I would say\x01",
            "it's likely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThere are a large number\x01",
            "of points similar to that\x01",
            "case you mentioned...\x02\x03",
            "#00001FI think it's best if\x01",
            "investigate this incident\x01",
            "as a case of fraud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FIn that case, what kinds\x01",
            "of things should we be\x01",
            "looking at?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, yes. There two main\x01",
            "things that are\x01",
            "suspicious about Minneth.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001FFirstly, that plan of his... We\x01",
            "need to look into whether "Armorica\x01",
            "Honey Company" really exists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FWe might be able to find\x01",
            "out about that by\x01",
            "following the mira.\x02\x03",
            "#10300FTo start a business in\x01",
            "Crossbell, you'd need to\x01",
            "get a loan at IBC.\x02\x03",
            "If his plan is a lie,\x01",
            "maybe there will be some\x01",
            "evidence of that at IBC?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnd the other point of course,\x01",
            "is whether Minneth really is an\x01",
            "employee of "Quincy Company".\x02\x03",
            "#00001FQuincy is headquartered out of\x01",
            "state, so it'll be hard to look\x01",
            "into that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00103FIt might not be too\x01",
            "useful, but...\x02\x03",
            "#00100FThere might be a\x01",
            "reference regarding that\x01",
            "in my home.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)

    ChrTalk(
        0x103,
        "#00205FA reference?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FThere's a Quincy Company\x01",
            "pamphlet there, you see.\x02\x03",
            "It details the general outline\x01",
            "of their company. There might be\x01",
            "something we can use in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FA Quincy Company pamphlet...\x01",
            "Is there anything you don't\x01",
            "have, milady?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00113FYes, well, you see... I like making\x01",
            "candy, but...\x02\x03",
            "#00100FA while back, I had an intense\x01",
            "interest in the Quincy Company, and\x01",
            "so, I ordered one of their pamphlets.\x02\x03",
            "It should be on the shelf in my room\x01",
            "in my parents' home.\x02\x03",
            "#00106F...No, I suppose it's no good.\x01",
            "There's no way such a pamphlet would\x01",
            "have what we're looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FWell, it is possible there's something\x01",
            "there.\x02\x03",
            "#02200FThat pamphlet is official Quincy Company\x01",
            "material. You might find something in there\x01",
            "that contradicts what Minneth has said.\x02\x03",
            "Don't you think it would be good to check\x01",
            "it out, just in case?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003FYou're right... For now,\x01",
            "let's head for Elie's\x01",
            "house.\x02\x03",
            "#00000FYou've given us valuable\x01",
            "advice, Lawyer Ian.\x02\x03",
            "Thanks to you, our\x01",
            "investigation plan is\x01",
            "set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FHmm, I'm just glad I was\x01",
            "able to be of some use.\x02\x03",
            "If I recall, you're using\x01",
            "Harold's house as base\x01",
            "for your investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYes, that's right,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FRegarding this case... I\x01",
            "think I've helped you as\x01",
            "much as time will permit.\x02\x03",
            "#02203FI am a busy man. I'm\x01",
            "afraid I can help you no\x01",
            "further.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FNo, don't mention it...\x01",
            "And thank you very much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FIt's good to rely on the\x01",
            "help of a professional\x01",
            "every once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02202FHaha, I'll turn up every\x01",
            "now and then. Good luck\x01",
            "with your investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, thank you very\x01",
            "much.\x02\x03",
            "#00003FAlright, shall we get\x01",
            "started?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x109, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001FWe need to look into IBC financing to see if\x01",
            "we can find anything about Minneth's plan...\x02\x03",
            "And, we'll go to the MacDowell residence,\x01",
            "review the Quincy materials, and try to find\x01",
            "where it differs from what Minneth has said.\x02\x03",
            "Those are the two points we need to\x01",
            "investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FRoger... We'll uncover\x01",
            "that evidence no matter\x01",
            "what it takes!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x87, 0x1, 0x1)
    SetScenarioFlags(0x177, 3)
    ClearMapFlags(0x10000000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    SetChrPos(0x0, 2400, 30, 1120, 225)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_13_564B end

    def Function_14_77B5(): pass

    label("Function_14_77B5")


    def lambda_77BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77BA)

    def lambda_77CB():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77CB)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3290, 30, 900, 2000, 0x0)
    TurnDirection(0x101, 0x8, 500)
    Return()

    # Function_14_77B5 end

    def Function_15_7800(): pass

    label("Function_15_7800")


    def lambda_7805():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7805)

    def lambda_7816():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7816)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 2330, 30, 1420, 2000, 0x0)
    TurnDirection(0x102, 0x8, 500)
    Return()

    # Function_15_7800 end

    def Function_16_784B(): pass

    label("Function_16_784B")


    def lambda_7850():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7850)

    def lambda_7861():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7861)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 3210, 30, -360, 2000, 0x0)
    TurnDirection(0x103, 0x8, 500)
    Return()

    # Function_16_784B end

    def Function_17_7896(): pass

    label("Function_17_7896")


    def lambda_789B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_789B)

    def lambda_78AC():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_78AC)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2300, 30, 80, 2000, 0x0)
    TurnDirection(0x104, 0x8, 500)
    Return()

    # Function_17_7896 end

    def Function_18_78E1(): pass

    label("Function_18_78E1")


    def lambda_78E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_78E6)

    def lambda_78F7():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_78F7)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 1960, 30, -1080, 2000, 0x0)
    TurnDirection(0x109, 0x8, 500)
    Return()

    # Function_18_78E1 end

    def Function_19_792C(): pass

    label("Function_19_792C")


    def lambda_7931():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7931)

    def lambda_7942():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7942)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1200, 0, 350, 2000, 0x0)
    TurnDirection(0x105, 0x8, 500)
    Return()

    # Function_19_792C end

    def Function_20_7977(): pass

    label("Function_20_7977")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_20_7977 end

    SaveToFile()

Try(main)
