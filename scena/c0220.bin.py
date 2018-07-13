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
        "Function_4_22C7",         # 04, 4
        "Function_5_3904",         # 05, 5
        "Function_6_3A4E",         # 06, 6
        "Function_7_3BE8",         # 07, 7
        "Function_8_3C85",         # 08, 8
        "Function_9_3E20",         # 09, 9
        "Function_10_3FC7",        # 0A, 10
        "Function_11_4DBA",        # 0B, 11
        "Function_12_506E",        # 0C, 12
        "Function_13_57B0",        # 0D, 13
        "Function_14_7925",        # 0E, 14
        "Function_15_7970",        # 0F, 15
        "Function_16_79BB",        # 10, 16
        "Function_17_7A06",        # 11, 17
        "Function_18_7A51",        # 12, 18
        "Function_19_7A9C",        # 13, 19
        "Function_20_7AE7",        # 14, 20
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
    Jump("loc_22C3")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93D")

    ChrTalk(
        0xFE,
        (
            "#02200FIt's all of you... Did you\x01",
            "see Mr. Dieter's address?\x02",
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
            "sudden turn of events...\x01",
            "Is that what you're trying to say?\x02\x03",
            "#02203FA majority of the citizens\x01",
            "must be feeling the same way.\x02\x03",
            "#02201FHowever, the "secret feud" between the\x01",
            "two major powers is the absolute truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F...Those "accidents"\x01",
            ""uncle" spoke of, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FYes...\x02\x03",
            "#02201FHowever, we pretend not\x01",
            "to notice this truth and\x01",
            "enjoy our happiness.\x02\x03",
            "This is the sin Dieter spoke of, \x01",
            "borne by everyone living in\x01",
            "Crossbell.\x02\x03",
            "#02203FState independence\x01",
            "is aso needed to\x01",
            "face that too.\x02",
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
            "affected me and I got\x01",
            "carried away.\x02\x03",
            "#02200FWhich will it be... \x01",
            "The dice have already been cast.\x02\x03",
            "#02203FWhere do we go from here?\x01",
            "That's a problem each citizen\x01",
            "must consider individually.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 1)
    Jump("loc_9C6")

    label("loc_93D")


    ChrTalk(
        0xFE,
        (
            "#02203FThe dice have already been cast.\x02\x03",
            "#02200FWhere do we go from here?\x01",
            "That's a problem each citizen\x01",
            "must consider individually.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C6")

    Jump("loc_22C3")

    label("loc_9CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA7")

    ChrTalk(
        0xFE,
        (
            "#02203F*sigh*... That\x01",
            "visitor's company\x01",
            "materials...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLawyer Ian... You\x01",
            "seem rather busy.\x02",
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
            "what he had in that attack.\x02\x03",
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
            "#02203FHmm... But it\x01",
            "can't be helped.\x02\x03",
            "#02200FMany people have lost\x01",
            "meeting places or their\x01",
            "very workplace itself.\x02\x03",
            "As a lawyer, \x01",
            "I must do all I\x01",
            "can for them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, that's our Mr.\x01",
            "Beardy-Bear for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FB-But... How are you\x01",
            "doing with drafting\x01",
            "the constitution?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02200FYeah, I managed to complete it.\x01",
            "I just submitted it to the\x01",
            "autonomous state government.\x02\x03",
            "#02202FWe can do it if we try, I suppose. Thanks\x01",
            "to that, I haven't had time to sleep, lately.\x02",
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
            "#10100FUmm, please don't\x01",
            "overdo it, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02202FUh uh, sorry to worry you.\x02\x03",
            "#02203FI plan to fit as many\x01",
            "appointment in as possible\x01",
            "today, and sleep well tonight.\x02\x03",
            "#02200F...Well then. My client is\x01",
            "waiting, so I'll excuse myself.\x02\x03",
            "You guys too must have\x01",
            "a lot of requests. Please\x01",
            "do your best on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSure, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_F31")

    label("loc_EA7")


    ChrTalk(
        0xFE,
        (
            "#02200FAs a lawyer, I plan\x01",
            "to do all I can for\x01",
            "the citizens.\x02\x03",
            "You guys too must have\x01",
            "a lot of requests. Please\x01",
            "do your best on them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F31")

    Jump("loc_22C3")

    label("loc_F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1111")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(
        0xFE,
        (
            "#02200FThe attack on\x01",
            "Mainz delayed the\x01",
            "referendum...\x02\x03",
            "There are citizens who think the attack was\x01",
            "a ploy by the Empire or Republic to get us\x01",
            "to withdraw the independence proposal.\x02\x03",
            "#02203F...I too wouldn't have\x01",
            "imagined they could\x01",
            "cause all this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_110C")

    label("loc_104D")


    ChrTalk(
        0xFE,
        (
            "#02200FIt is believed this incident is a ploy by\x01",
            "the Empire or Republic to make us\x01",
            "withdraw the independence proposal.\x02\x03",
            "#02203F...I too wouldn't have\x01",
            "imagined they could\x01",
            "cause all this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_110C")

    Jump("loc_22C3")

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_16FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F1")

    ChrTalk(
        0xFE,
        "#02200FOh, you all...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12C1")

    ChrTalk(
        0x101,
        (
            "#00004FLawyer Ian...\x01",
            "Thank you for your\x01",
            "help yesterday.\x02\x03",
            "#00000FThat evidence you\x01",
            "discovered proved useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FYes, I've heard about things\x01",
            "from Pete. It seems Minneth\x01",
            "is now a wanted man.\x02\x03",
            "#02202FHa ha, though you say that,\x01",
            "I only helped you a little bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FNo, you were a big help.\x02\x03",
            "#00000FEven though you're busy\x01",
            "drafting the constitution...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131E")

    label("loc_12C1")


    ChrTalk(
        0x101,
        (
            "#00000FLawyer Ian...\x01",
            "It's been awhile.\x02\x03",
            "It seems you're busy\x01",
            "drafting the constitution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131E")


    ChrTalk(
        0xFE,
        (
            "#02200FYes, and it's come\x01",
            "together a little.\x02\x03",
            "I was thinking of making some\x01",
            "coffee and taking a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FOh... Then we're\x01",
            "intruding on your\x01",
            "break time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02202FDon't mention it. Having a\x01",
            "chat with all of you should\x01",
            "make a nice change of pace.\x02\x03",
            "#02205FBy the way. It seems you\x01",
            "all were assigned to\x01",
            "yesterday's derailment...\x02",
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
            "#00305FLawyer Ian...\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203F...No, I was just thinking it's\x01",
            "a relief that no one died.\x02\x03",
            "#02200FAnyway, things are more dangerous\x01",
            "lately. You all should be careful too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 0)
    Jump("loc_16F9")

    label("loc_15F1")


    ChrTalk(
        0xFE,
        (
            "#02200FThe constitution draft is coming along,\x01",
            "but there's still room for improvement.\x02\x03",
            "#02203FIt's very stamina draining,\x01",
            "but it's for Crossbell's future,\x01",
            "so I can't complain.\x02\x03",
            "#02200FI will settle for nothing less than\x01",
            "the greatest constitution draft ever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F9")

    Jump("loc_22C3")

    label("loc_16FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_17BD")

    ChrTalk(
        0x8,
        (
            "#02200FRegarding this incident...\x01",
            "I've helped you as much\x01",
            "as my schedule allows.\x02\x03",
            "#02202FUh uh, I'll show my face\x01",
            "sometimes, so please do your\x01",
            "best with the investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C3")

    label("loc_17BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_187C")

    ChrTalk(
        0x8,
        (
            "#02200FRegarding this incident...\x01",
            "I've helped you as much\x01",
            "as my schedule allows.\x02\x03",
            "#02202FUh uh, I'll show my face\x01",
            "sometimes, so please do your\x01",
            "best with the investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C3")

    label("loc_187C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_188A")
    Jump("loc_22C3")

    label("loc_188A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1898")
    Jump("loc_22C3")

    label("loc_1898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1B1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A84")

    ChrTalk(
        0xFE,
        (
            "#02205FOh, it's you all. That's unusual\x01",
            "for you to come at night.\x02\x03",
            "#02200FAnd since Dudley is with you too... \x01",
            "Could a problem or something have arised\x01",
            "related to tomorrow's conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603FWe're just going to\x01",
            "confirm that now.\x02\x03",
            "#00600FTo achieve perfection, \x01",
            "there's nothing like crushing\x01",
            "imperfect elements in advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02203FHm, there's nothing like\x01",
            "being too much prepared.\x02\x03",
            "#02200FI don't know the details, but...\x01",
            "Do your very best about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B16")

    label("loc_1A84")


    ChrTalk(
        0xFE,
        (
            "#02200FWell then... I'd say that these\x01",
            "preparations are enough.\x02\x03",
            "#02203FIn preparation for tomorrow, \x01",
            "today I'll go rest earlier than usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B16")

    Jump("loc_22C3")

    label("loc_1B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2B")

    ChrTalk(
        0xFE,
        (
            "#02200FIt seems the heads of state\x01",
            "are visiting Crossbell.\x02\x03",
            "#02203FI feel city security has been\x01",
            "raised even higher for the\x01",
            "first day of the conference.\x02\x03",
            "#02200FIt's at times like this\x01",
            "that trouble occurs. \x01",
            "Please be careful too, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CEA")

    label("loc_1C2B")


    ChrTalk(
        0xFE,
        (
            "#02203FCrossbell City's security has\x01",
            "been increased even more for\x01",
            "the heads of state visiting now.\x02\x03",
            "#02200FIt's at times like this\x01",
            "that trouble occurs. \x01",
            "Please be careful too, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEA")

    Jump("loc_22C3")

    label("loc_1CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1EEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E45")

    ChrTalk(
        0xFE,
        (
            "#02200FThe Trade Conference\x01",
            "finally opens tomorrow.\x02\x03",
            "The heads of state from each country are planning\x01",
            "to attend the inauguration ceremony, but...\x02\x03",
            "If by any chance something happens to any of\x01",
            "them, it will cause an international incident.\x02\x03",
            "As police, you must do your very\x01",
            "best to ensure that doesn't happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EEA")

    label("loc_1E45")


    ChrTalk(
        0xFE,
        (
            "#02200FIf you are ever concerned about anything, please\x01",
            "feel free to consult with me about it anytime.\x02\x03",
            "If you're fine with me,\x01",
            "I'll help you as much\x01",
            "as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EEA")

    Jump("loc_22C3")

    label("loc_1EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_212C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208F")

    ChrTalk(
        0xFE,
        (
            "#02203FIt seems the "Heiyue" acquisition of \x01",
            "Revache's old site is proceeding steadily.\x02\x03",
            "#02201FI don't want to think about what would\x01",
            "happen if that place fell into their hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FI see... That\x01",
            "would a problem.\x02",
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
    Jump("loc_2127")

    label("loc_208F")


    ChrTalk(
        0xFE,
        (
            "#02200FIt's only a matter of\x01",
            "time before Heiyue buys\x01",
            "up the Revache's old site.\x02\x03",
            "Good grief... Crossbell\x01",
            "certainly has its fair\x01",
            "share of problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2127")

    Jump("loc_22C3")

    label("loc_212C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_22C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2233")

    ChrTalk(
        0xFE,
        (
            "#02203FIt seems the citizens have\x01",
            "great expectations of the\x01",
            "Special Support Section.\x02\x03",
            "#02202FAlthough you'll have more\x01",
            "requests than before, please\x01",
            "do your best on them.\x02\x03",
            "As you pile them up,\x01",
            "I'm sure you'll become\x01",
            "Crossbell hope.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22C3")

    label("loc_2233")


    ChrTalk(
        0xFE,
        (
            "#02200FNaturally, I too am expecting great\x01",
            "things from the Special Support Section.\x02\x03",
            "#02202FPlease, live up to the\x01",
            "citizens' expectations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22C3")

    TalkEnd(0xFE)
    Return()

    # Function_3_599 end

    def Function_4_22C7(): pass

    label("Function_4_22C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E9")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_22E9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23E2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Read Ian's Letter\x01",      # 1
            "Quit\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2362")
    Call(0, 11)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23DD")

    label("loc_2362")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2376")
    Jump("loc_23DD")

    label("loc_2376")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23DD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(
        0xFE,
        "Everyone... Thank you so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please... Take care\x01",
            "of Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DD")

    Jump("loc_22F3")

    label("loc_23E2")

    Jump("loc_3900")

    label("loc_23E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23F5")
    Jump("loc_3900")

    label("loc_23F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2489")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood drafted\x01",
            "the constitution for\x01",
            "Crossbell's independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a leading figure,\x01",
            "he must consider\x01",
            "various things...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3900")

    label("loc_2489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_25B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_252D")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood\x01",
            "seems very busy.\x02",
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
    Jump("loc_25B4")

    label("loc_252D")


    ChrTalk(
        0xFE,
        (
            "...Anyway, for now, I'm doing\x01",
            "all I can to assist him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to get some rest too, I have\x01",
            "to hurry and finish up my work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B4")

    Jump("loc_3900")

    label("loc_25B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_26F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267B")

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
            "The people there have committed \x01",
            "no crime. How awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we citizens can\x01",
            "do anything about it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26EF")

    label("loc_267B")


    ChrTalk(
        0xFE,
        (
            "It seems Mr. Grimwood is\x01",
            "worried about this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if we citizens can\x01",
            "do anything about it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26EF")

    Jump("loc_3900")

    label("loc_26F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0C")

    ChrTalk(
        0xFE,
        (
            "I've got to settle yesterday's\x01",
            "incident in Armorica...\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2876")

    ChrTalk(
        0x101,
        (
            "#00000FHa ha... But I'm glad you\x01",
            "were able to resolve it.\x02\x03",
            "Thanks for all\x01",
            "your help.\x02",
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
            "The Special Support Section\x01",
            "did a nice job on that case too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_2876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_END)), "loc_2918")

    ChrTalk(
        0x101,
        (
            "#00003F(An incident in Armorica...\x01",
            "Could it have anything to\x01",
            "do with that Minneth?)\x02\x03",
            "(...I knew we should have\x01",
            "stuck with it until the end...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A04")

    label("loc_2918")


    ChrTalk(
        0x101,
        (
            "#00005FAn incident in Armorica...\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, you see there was this corrupt trader...\x02",
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
            "#00000FI-I see... Well I'm\x01",
            "glad you were able\x01",
            "to resolve it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A04")

    SetScenarioFlags(0x16C, 2)
    Jump("loc_2A55")

    label("loc_2A0C")


    ChrTalk(
        0xFE,
        (
            "In any case, I'm glad\x01",
            "we could help the people\x01",
            "of Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A55")

    Jump("loc_3900")

    label("loc_2A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A75")
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A75")

    label("loc_2A75")

    Jump("loc_3900")

    label("loc_2A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6D")

    ChrTalk(
        0xFE,
        (
            "The Armorica Village incident brought\x01",
            "to light a prior, similar case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can find clues in the\x01",
            "most unlikely of places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for Mr. Grimwood,\x01",
            "he went to Mr. Harold's house.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C00")

    label("loc_2B6D")


    ChrTalk(
        0xFE,
        (
            "The Armorica Village incident brought\x01",
            "to light a prior, similar case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're looking for Mr. Grimwood,\x01",
            "he went to Mr. Harold's house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C00")

    Jump("loc_2DF0")

    label("loc_2C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_END)), "loc_2D65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CEA")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is going to be extremely\x01",
            "busy drafting the constitution, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just for that reason, we can't\x01",
            "overlook an incident like this.\x02",
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
    Jump("loc_2D60")

    label("loc_2CEA")


    ChrTalk(
        0xFE,
        (
            "Because he's busy, please allow\x01",
            "me to help as much as I can.\x02",
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

    label("loc_2D60")

    Jump("loc_2DF0")

    label("loc_2D65")


    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is holed up on\x01",
            "2F drafting the constitution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He'll be very busy today as well.\x01",
            "I need to do my best to support him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF0")

    Jump("loc_3900")

    label("loc_2DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_33B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_332E")

    ChrTalk(
        0xFE,
        "Ah, the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood\x01",
            "is holed up on\x01",
            "2F, working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FDoesn't it seem like he's\x01",
            "been very busy lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FIs that so?\x02",
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
            "It seems he was asked by the\x01",
            "mayor to write the constitution\x01",
            "draft for the independent state.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F52")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2F52")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F78")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2F78")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F9E")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2F9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC4")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_2FC4")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007FEEH!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FA "constitution"...\x01",
            "Not an autonomous state law?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FA "constitution" is the fundamental\x01",
            "law that establishes the basic\x01",
            "conditions of a state's existence.\x02\x03",
            "#00100FIt doesn't allow other states interference in\x01",
            "the supreme laws that establish a nation's\x01",
            "sovereignty, structure and fundamental principles.\x02\x03",
            "It's something absolutely indispensable\x01",
            "for having the appearance of a state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F...Right...\x01",
            "Another complicated thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204FHowever, I think that someone like\x01",
            "Lawyer Ian is truly suited for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, it seems like Mr. Beardy-Bear,\x01",
            "who is active in the neighboring states too,\x01",
            "could do well in this matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I'm sure he will create\x01",
            "a fine constitution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThen, will you say\x01",
            "to lawyer Ian to do\x01",
            "his best for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will. I think Mr. Grimwood\x01",
            "will be encouraged by it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 1)
    Jump("loc_33B2")

    label("loc_332E")


    ChrTalk(
        0xFE,
        (
            "It seems the mayor asked\x01",
            "Mr. Grimwood to draft\x01",
            "the constitution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure he will be\x01",
            "able to create a fine\x01",
            "constitution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B2")

    Jump("loc_3900")

    label("loc_33B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3445")

    ChrTalk(
        0xFE,
        (
            "If you're looking for Mr.\x01",
            "Grimwood, he left on business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you have a message for him,\x01",
            "I'll deliver it to him later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3900")

    label("loc_3445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_34CC")

    ChrTalk(
        0xFE,
        (
            "Oh, this file...\x01",
            "It was put away in the wrong place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly, Mr. Grimwood...\x01",
            "This is a sloppy side of him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3900")

    label("loc_34CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B9")

    ChrTalk(
        0xFE,
        (
            "Huh? The last client's consultation fee... \x01",
            "It seems it's rather small.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Mr. Grimwood must be\x01",
            "arbitrarily reducing\x01",
            "the fees again.\x02",
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
    Jump("loc_361F")

    label("loc_35B9")


    ChrTalk(
        0xFE,
        (
            "...Mr. Grimwood must be\x01",
            "arbitrarily reducing\x01",
            "the fees again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Goodness gracious. *mumble*...\x02",
    )

    CloseMessageWindow()

    label("loc_361F")

    Jump("loc_3900")

    label("loc_3624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36EB")

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
            "Because the Trade Conference is near,\x01",
            "he's been having more consultations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must do all I can\x01",
            "to support him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_376B")

    label("loc_36EB")


    ChrTalk(
        0xFE,
        (
            "Because the Trade Conference is near, he's\x01",
            "been having more consultations lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must do all I can\x01",
            "to support him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376B")

    Jump("loc_3900")

    label("loc_3770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_380F")

    ChrTalk(
        0xFE,
        (
            "More customers have\x01",
            "been coming for\x01",
            "consultations lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood has been working non-stop.\x01",
            "He's got to take a break sometime...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3900")

    label("loc_380F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B2")

    ChrTalk(
        0xFE,
        (
            "Ah, the Special Support\x01",
            "Section... It's been awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is at his desk. Please\x01",
            "speak with him if you need anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3900")

    label("loc_38B2")


    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood is at his desk. Please\x01",
            "speak with him if you need anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3900")

    TalkEnd(0xFE)
    Return()

    # Function_4_22C7 end

    def Function_5_3904(): pass

    label("Function_5_3904")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C6")

    ChrTalk(
        0xFE,
        (
            "The company I work for\x01",
            "was in the destroyed\x01",
            "IBC building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With our workplace gone, all\x01",
            "our activities are suspended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... What are\x01",
            "we going to do now?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3A4A")

    label("loc_39C6")


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
            "*sigh*... What are\x01",
            "we going to do now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A4A")

    TalkEnd(0xFE)
    Return()

    # Function_5_3904 end

    def Function_6_3A4E(): pass

    label("Function_6_3A4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A67")
    TalkEnd(0xFE)
    Call(0, 10)
    Return()

    label("loc_3A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B70")

    ChrTalk(
        0xFE,
        (
            "His "Plan"... \x01",
            "It's certain he's spent a\x01",
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
        "...Please be careful, everyone.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B68")

    ChrTalk(
        0x10A,
        (
            "#00600FHmm... You handle\x01",
            "this place, Emma.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B68")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3BE4")

    label("loc_3B70")


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
        "...Please be careful, everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_3BE4")

    TalkEnd(0xFE)
    Return()

    # Function_6_3A4E end

    def Function_7_3BE8(): pass

    label("Function_7_3BE8")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "We're currently searching\x01",
            "the Grimwood Law\x01",
            "Office premises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've succeeded in unlocking the door at 2F.\x01",
            "I hope we find some clue up there.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_3BE8 end

    def Function_8_3C85(): pass

    label("Function_8_3C85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8C")

    ChrTalk(
        0xFE,
        (
            "We've found materials relating\x01",
            "to Middle Ages alchemy and the\x01",
            "Ancient Zemurian civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're very old...\x01",
            "It must've taken many years to\x01",
            "amass a collection this big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just when did suspect Ian start\x01",
            "planning all of this?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E1C")

    label("loc_3D8C")


    ChrTalk(
        0xFE,
        (
            "They're very old...\x01",
            "It must've taken many years to\x01",
            "amass a collection this big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just when did suspect Ian start\x01",
            "planning all of this?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E1C")

    TalkEnd(0xFE)
    Return()

    # Function_8_3C85 end

    def Function_9_3E20(): pass

    label("Function_9_3E20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0E")

    ChrTalk(
        0xFE,
        (
            "On this terminal, we found evidence of\x01",
            "frequent communications with Orchis Tower.\x02",
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
    Jump("loc_3FC3")

    label("loc_3F0E")


    ChrTalk(
        0xFE,
        (
            "Most likely, he manipulated Mr. Crois\x01",
            "and the others from this location...\x01",
            "Or perhaps I should say he ordered them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We have to carefully proceed with the investigation...\x02",
    )

    CloseMessageWindow()

    label("loc_3FC3")

    TalkEnd(0xFE)
    Return()

    # Function_9_3E20 end

    def Function_10_3FC7(): pass

    label("Function_10_3FC7")

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
        "#11P#00005FPete...?\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x9, 0x5A, 0x1F4)

    ChrTalk(
        0x9,
        "#6PE-Everyone...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4187")

    ChrTalk(
        0xB,
        (
            "#5PMr. Dudley...\x01",
            "And the Support Section too.\x01",
            "Good work out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#11P#00603F...Thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_41AB")

    label("loc_4187")


    ChrTalk(
        0xB,
        (
            "#5PNice work,\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41AB")


    ChrTalk(
        0x101,
        (
            "#11P#00001FGood work yourself, Detective Emma.\x01",
            "Are you searching the premises?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYes... Section One is looking for\x01",
            "any possible material witnesses.\x02",
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
            "#6P*sob*... \x01",
            "No, I too am requesting you to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PMr. Grimwood... Before he disappeared,\x01",
            "he said something concerning,\x01",
            "and I wanted to check it out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_END)), "loc_43EA")

    ChrTalk(
        0x104,
        (
            "#11P#00308FYeah... He asked you to\x01",
            "clean the desk or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FThat is indeed concerning.\x01",
            "Why would he ask you that\x01",
            "all of a sudden...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4693")

    label("loc_43EA")


    ChrTalk(
        0x102,
        "#11P#00105FConcerning...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P...Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6POnce this state of emergency with\x01",
            "those "magic soldiers" is lifted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PHe asked me to return to this\x01",
            "office and clean his desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00005FCleaning...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PYes. From the start, I thought\x01",
            "he left in a hurry, but...\x02",
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
            "#11P#00108FLawyer Ian... It seems like he was\x01",
            "really concerned about that...\x02\x03",
            "#00106FI don't get why he\x01",
            "would ask you to clean\x01",
            "the desk now, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4693")


    ChrTalk(
        0x9,
        (
            "#6PThe answer to that...\x01",
            "Came out from Mr. Grimwood's dest just before.\x02",
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
            "Pete held out an unsealed letter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_4726():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4726)
    Sleep(50)

    def lambda_4736():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4736)
    Sleep(50)

    def lambda_4746():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4746)
    Sleep(50)

    def lambda_4756():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_4756)
    Sleep(50)

    def lambda_4766():
        TurnDirection(0xF5, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_4766)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4837")

    ChrTalk(
        0x105,
        "#11P#10401FThat's...a letter he left?\x02",
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_4837")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4876")

    ChrTalk(
        0x109,
        "#11P#10101FIs it...a letter he left?\x02",
    )

    CloseMessageWindow()
    Jump("loc_48B2")

    label("loc_4876")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48B2")

    ChrTalk(
        0x106,
        "#11P#10701FIs that...a letter he left?\x02",
    )

    CloseMessageWindow()

    label("loc_48B2")


    ChrTalk(
        0x101,
        "#11P#00001F...Can we read it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6P......(*nods*)\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_495D")

    ChrTalk(
        0x101,
        "#11P#00008F............\x02",
    )

    CloseMessageWindow()
    Jump("loc_49BC")

    label("loc_495D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_498F")

    ChrTalk(
        0x109,
        "#11P#10108F............\x02",
    )

    CloseMessageWindow()
    Jump("loc_49BC")

    label("loc_498F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49BC")

    ChrTalk(
        0x105,
        "#11P#10408F............\x02",
    )

    CloseMessageWindow()

    label("loc_49BC")


    ChrTalk(
        0xB,
        (
            "#5P...We've taken custody\x01",
            "of the other documents\x01",
            "on his desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PA giant memo of how\x01",
            "to deal with all his\x01",
            "clients from now on...\x02",
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
            "#6POoh, Mr. Grimwood... \x01",
            "Why did you have to do this...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4AD5():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4AD5)
    Sleep(50)

    def lambda_4AE5():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4AE5)
    Sleep(50)

    def lambda_4AF5():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4AF5)
    Sleep(50)

    def lambda_4B05():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4B05)
    Sleep(50)

    def lambda_4B15():
        TurnDirection(0xF4, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_4B15)
    Sleep(50)

    def lambda_4B25():
        TurnDirection(0xF5, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_4B25)
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
            "#6PThere's no way I could ever\x01",
            "be happy forgetting what\x01",
            "Mr. Grimwood did for me...!\x02",
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
        "#11P#00208F...Lawyer Ian is a big idiot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00306FYeah, I shouldn't be on a position to tell him, but...\x01",
            "The people he left behind won't ever\x01",
            "been convinced with such a letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F...Exactly right.\x02\x03",
            "#00008FPete, we intend to go see\x01",
            "Lawyer Ian right away.\x02\x03",
            "#00001FThere, we'll learn the truth... And bring\x01",
            "Lawyer Ian and the others back with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PE-Everyone... \x01",
            "*sob*, thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PPlease... Take care\x01",
            "of Mr. Grimwood.\x02",
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

    # Function_10_3FC7 end

    def Function_11_4DBA(): pass

    label("Function_11_4DBA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(18, 0, 40, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Dear Pete. First of all, I want to\x01",
            "apologize for suddenly leaving your\x01",
            "side. I once accepted your\x02\x01",
            "guardianship, and once I put you\x01",
            "to work in my office, I lived many,\x01",
            "happy days. One fateful day, I became\x02\x01",
            "ruled by grief and sorrow, and ever\x01",
            "since then I have lived only to\x01",
            "complete a certain plan.\x07\x00\x02",
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
            "Because of you, I was troubled for\x01",
            "awhile, but this plan cannot be\x02\x01",
            "stopped. You cannot forgive me for\x01",
            "going back on my word. Pete,\x02\x01",
            "please... I want you to forget about\x01",
            "me, and live a happy life. From a\x02\x01",
            "far-off place, I pray to the Goddess\x01",
            "that your wisdom will make you into\x02\x01",
            "a fine adult. ──Ian Grimwood.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_4DBA end

    def Function_12_506E(): pass

    label("Function_12_506E")

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
        "#00000FIt's been awhile, Lawyer Ian.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02200FHa ha, it sure has. I heard\x01",
            "you temporarily suspended\x01",
            "your activities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThat's right. We've resumed our duties. \x01",
            "I'm looking forward to working with you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02200FUh uh, I see. And you've\x01",
            "added new members for\x01",
            "your fresh start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FYou're the famous "Mr. Beardy-Bear",\x01",
            "if I'm not mistaken?\x02\x03",
            "#10304FHu hu, I'm looking forward to working with you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5P#02205FOh, how polite.\x02\x03",
            "#02203FUmm, I know I have a business\x01",
            "card here somewhere...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_539F")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_539F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53C5")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_53C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53EB")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_53EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5411")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5411")

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
            "#12P#00100FWell, Lawyer Ian is\x01",
            "easy to get along with.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5P#02202FHa ha, no, no... When it comes\x01",
            "to personal relationships,\x01",
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
            "──*ahem*. Allow me to \x01",
            "introduce myself formally.\x02\x03",
            "My name is Ian Grimwood.\x01",
            "I am a lawyer, and I work\x01",
            "as head of this law office.\x02\x03",
            "Ladies and gentlemen of the Special\x01",
            "Support Section, I look forward to\x01",
            "working with all of you once again.\x02",
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
            "#10100FSame here. It's good to\x01",
            "be working with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe might have various things\x01",
            "to discuss with you again.\x02\x03",
            "#00004FWhen that time comes,\x01",
            "please lend us your aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#02200FSure, feel free to\x01",
            "stop by anytime.\x02\x03",
            "I'd be happy to give you advice\x01",
            "whenever the need arises.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x12C, 4)
    OP_CC(0x1, 0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_506E end

    def Function_13_57B0(): pass

    label("Function_13_57B0")

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
        "#02205FOh...?\x02",
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
            "#00204FThank goodness... \x01",
            "So you are in the office today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FYes, I'm taking a break\x01",
            "just now, but...\x02\x03",
            "#02201F...Hmm, do you need a\x01",
            "consultation on something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSo you already can tell...\x01",
            "As expected from Mr. Grimwood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FUh uh. If it's the face of\x01",
            "someone with a request, I've\x01",
            "seen thousands of them already.\x02\x03",
            "#02200FHave a seat there.\x01",
            "I'm busy too, but\x01",
            "I'll hear you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004FExcuse us...and thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others explained Minneth's profile they\x01",
            "had learned the previous day as well as his actions...\x02\x03",
            "They also mentioned the confirmation\x01",
            "Minneth was collecting the Armorica\x01",
            "land deeds they obtained earlier today.\x07\x00\x02",
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
            "#02200FHmm... I see. I understand\x01",
            "the general situation.\x02\x03",
            "Ordinarily, I would have liked to\x01",
            "take a case like this one, but...\x02\x03",
            "#02203FAs I'm sure you are aware, I have\x01",
            "important constitution drafting\x01",
            "work to handle right now.\x02\x03",
            "#02203FI'm sorry, but it doesn't look like I\x01",
            "can spare the time to look into this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FToo bad... It can't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FEven only consulting\x01",
            "with us like this\x01",
            "helps us out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FSorry... I'll give\x01",
            "you whatever advice\x01",
            "I can right now.\x02",
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
            "Empire once told me about\x01",
            "a very similar case of his.\x02\x03",
            "Although I can't say the\x01",
            "circumstances are exactly the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Right now, we're just looking for\x01",
            "anything that would make a good\x01",
            "starting point in our investigation.\x02\x03",
            "#00003FThat idea... \x01",
            "Will you tell us about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200F...Hmm, very well. It is none other\x01",
            "than you all who is asking, after all.\x02\x03",
            "#02203F*ahem*, then...\x02",
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
            "#02203F──Several years ago... \x01",
            "A single man visited the house\x01",
            "of a certain Erebonian Baron.\x02\x03",
            "#02201FThe man's name was "Ridner"...\x01",
            "He called himself a master businessman\x01",
            "working for a certain brewing company.\x02\x03",
            "To the baron, Ridner presented a\x01",
            "certain way to make it big, fast.\x02\x03",
            "The great barley fields that had been passed down\x01",
            "in the baron's family for generations... They would\x01",
            "be used to expand his company's business.\x02\x03",
            "#02203FA brewery would be constructed in the Baron's\x01",
            "territory, and the management thereof left\x01",
            "to his family... That was the general idea.\x02",
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
            "#10300FHu hu... The more I\x01",
            "hear, the more similar\x01",
            "it sounds to our case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F──Accepting the deal,\x01",
            "the Baron signed on\x01",
            "to Ridner's contract.\x02\x03",
            "#02200FThen, under the pretexts of management,\x01",
            "and brewery construction, some of the land\x01",
            "was temporarily transferred to Ridner.\x02\x03",
            "Also, some of the Baron's fortune was\x01",
            "converted into stock in preparation\x01",
            "for starting the business...\x02\x03",
            "#02203FBut then... Ridner took\x01",
            "the deeds and fortune\x01",
            "and disappeared.\x02",
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
            "#02203FHaving suddenly lost contact with Ridner,\x01",
            "the Baron's people were flustered...\x02\x03",
            "It was then the Baron realized\x01",
            "the gravity of the situation.\x02\x03",
            "#02201FThe strangest thing happened. \x01",
            "Ridner sold the deeds \x01",
            "to a third party.\x02\x03",
            "As prime real estate for building villas.\x02\x03",
            "#02203F──In the end, the Baron was left only\x01",
            "with an enormous debt... Before long,\x01",
            "he ended up losing his entire territory.\x02\x03",
            "Having lost his territory, he was\x01",
            "stripped of his rank. No one knows\x01",
            "what happened to him after that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWow... \x01",
            "That's an insane story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FHe just went off and sold someone else's property...\x02\x03",
            "That's too cruel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203F──That case was the first that came\x01",
            "to mind, based on what you told me.\x02\x03",
            "Lie and gain their trust. Then, at the\x01",
            "very end, make off with a huge fortune...\x02\x03",
            "#02201FIt is said to be a technique\x01",
            "for committing "fraud."\x02",
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
        "#00105FFraud...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIn other words, Minneth isn't an\x01",
            "employee of the Quincy Company.\x02\x03",
            "#00200FYou are saying it is possible\x01",
            "he is just a fraudster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FYes... Though not definite,\x01",
            "I would say it's likely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThere're a large number of points\x01",
            "similar to that case you mentioned...\x02\x03",
            "#00001FI think it's best if we\x01",
            "investigate this incident\x01",
            "as a case of fraud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FIn that case, what\x01",
            "kinds of things should\x01",
            "we be looking at?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh, yes. There're two \x01",
            "main things that are\x01",
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
            "#00001FFirstly, that plan of his...\x01",
            "We need to look into whether that \x01",
            ""Armorica Honey Company" really exists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FWe might be able to\x01",
            "find out about that by\x01",
            "following the mira.\x02\x03",
            "#10300FTo start a business in\x01",
            "Crossbell, you'd need\x01",
            "to get a loan at IBC.\x02\x03",
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
            "#00001FQuincy is headquartered out of state,\x01",
            "so it'll be hard to look into that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00103FIt might not be\x01",
            "too useful, but...\x02\x03",
            "#00100FThere might be a reference\x01",
            "regarding that in my home.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)

    ChrTalk(
        0x103,
        "#00205FA reference...?\x02",
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
            "#00300FA Quincy Company pamphlet... \x01",
            "Why do you have such a thing, milady?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    ChrTalk(
        0x102,
        (
            "#00113FYes, well, you see...\x01",
            "I like to make candy, but...\x02\x03",
            "#00100FAwhile back, I had an intense\x01",
            "interest in the Quincy Company, and\x01",
            "so I ordered one of their pamphlets.\x02\x03",
            "It should be on the shelf in\x01",
            "my room in my parents' home...\x02\x03",
            "#00106F...No, I suppose it's no good. There's no way such\x01",
            "a pamphlet would have what we're looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02203FWell, it's possible there's something there.\x02\x03",
            "#02200FThat pamphlet is official Quincy Company\x01",
            "material. You might find something in there\x01",
            "that contradicts what Minneth has said.\x02\x03",
            "Don't you think it would be good\x01",
            "to check it out, just in case?\x02",
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
            "let's head for Elie's house.\x02\x03",
            "#00000FYou've given us valuable\x01",
            "advice, Lawyer Ian.\x02\x03",
            "Thanks to you, our\x01",
            "investigation plan is set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FHmm, I'm just glad I was\x01",
            "able to be of some use.\x02\x03",
            "If I recall, you're investigating\x01",
            "using Harold's house as base?\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYes, that's right, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02200FRegarding this case...\x01",
            "I'll help you as much\x01",
            "as time will permit.\x02\x03",
            "#02203FI'm a busy man. I'm afraid\x01",
            "I can't help you that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FNo, don't mention it...\x01",
            "You really encouraged us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FIt's good to rely on the help of a\x01",
            "professional every once in awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02202FUh uh, I'll show my face\x01",
            "later, so please do your\x01",
            "best with the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, thank you very much.\x02\x03",
            "#00003F...Alright, shall\x01",
            "we get started?\x02",
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
            "Then, we'll go to the MacDowell residence,\x01",
            "review the Quincy materials, and try to find\x01",
            "where it differs from what Minneth has said.\x02\x03",
            "Those are the two points we need to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FRoger... We'll uncover that\x01",
            "evidence no matter what it takes!\x02",
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

    # Function_13_57B0 end

    def Function_14_7925(): pass

    label("Function_14_7925")


    def lambda_792A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_792A)

    def lambda_793B():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_793B)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3290, 30, 900, 2000, 0x0)
    TurnDirection(0x101, 0x8, 500)
    Return()

    # Function_14_7925 end

    def Function_15_7970(): pass

    label("Function_15_7970")


    def lambda_7975():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7975)

    def lambda_7986():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7986)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 2330, 30, 1420, 2000, 0x0)
    TurnDirection(0x102, 0x8, 500)
    Return()

    # Function_15_7970 end

    def Function_16_79BB(): pass

    label("Function_16_79BB")


    def lambda_79C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_79C0)

    def lambda_79D1():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_79D1)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 3210, 30, -360, 2000, 0x0)
    TurnDirection(0x103, 0x8, 500)
    Return()

    # Function_16_79BB end

    def Function_17_7A06(): pass

    label("Function_17_7A06")


    def lambda_7A0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7A0B)

    def lambda_7A1C():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7A1C)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2300, 30, 80, 2000, 0x0)
    TurnDirection(0x104, 0x8, 500)
    Return()

    # Function_17_7A06 end

    def Function_18_7A51(): pass

    label("Function_18_7A51")


    def lambda_7A56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7A56)

    def lambda_7A67():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A67)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 1960, 30, -1080, 2000, 0x0)
    TurnDirection(0x109, 0x8, 500)
    Return()

    # Function_18_7A51 end

    def Function_19_7A9C(): pass

    label("Function_19_7A9C")


    def lambda_7AA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7AA1)

    def lambda_7AB2():
        OP_98(0xFE, 0xE10, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7AB2)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1200, 0, 350, 2000, 0x0)
    TurnDirection(0x105, 0x8, 500)
    Return()

    # Function_19_7A9C end

    def Function_20_7AE7(): pass

    label("Function_20_7AE7")

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

    # Function_20_7AE7 end

    SaveToFile()

Try(main)
