from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0350.bin",                # FileName
        "c0350",                    # MapName
        "c0350",                    # Location
        0x002D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0350",                  # 0
        "Yuri",                   # 1
        "Sykes",                  # 2
        "Reggie",                 # 3
        "Hostess",                # 4
        "Hostess",                # 5
        "Hostess",                # 6
        "Hostess",                # 7
    ))

    AddCharChip((
        "chr/ch44100.itc",                   # 00
        "chr/ch47500.itc",                   # 01
        "chr/ch23600.itc",                   # 02
        "chr/ch44102.itc",                   # 03
        "chr/ch26802.itc",                   # 04
        "chr/ch26900.itc",                   # 05
    ))

    DeclNpc(7989,    200,     1600,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5699,    0,       469,     45,   261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7780,    0,       4294966486, 0,    261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(7989,    200,     2200,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(2309,    0,       3529,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(6270,    0,       1580,    1000,    7990,    1500,    2200,    0x007E, 0,  11, 0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_2CB",          # 02, 2
        "Function_3_6FA",          # 03, 3
        "Function_4_7B2",          # 04, 4
        "Function_5_164F",         # 05, 5
        "Function_6_1837",         # 06, 6
        "Function_7_195B",         # 07, 7
        "Function_8_21FB",         # 08, 8
        "Function_9_2293",         # 09, 9
        "Function_10_24AA",        # 0A, 10
        "Function_11_2CC5",        # 0B, 11
        "Function_12_2CC9",        # 0C, 12
        "Function_13_2D3F",        # 0D, 13
        "Function_14_2DC6",        # 0E, 14
        "Function_15_3C9E",        # 0F, 15
        "Function_16_50E3",        # 10, 16
        "Function_17_5127",        # 11, 17
        "Function_18_517F",        # 12, 18
        "Function_19_51CA",        # 13, 19
        "Function_20_5222",        # 14, 20
        "Function_21_526D",        # 15, 21
        "Function_22_529D",        # 16, 22
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CA")
    OP_94(0xFE, 0x334, 0x2904, 0xFFFFF31C, 0x3804, 0x3E8)
    Sleep(300)
    Jump("Function_1_2A0")

    label("loc_2CA")

    Return()

    # Function_1_2A0 end

    def Function_2_2CB(): pass

    label("Function_2_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_320")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_31B")

    Jump("loc_6B8")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_367")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_6B8")

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_397")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_6B8")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3DE")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_6B8")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_442")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 8119, 0, -2400, 135)
    Jump("loc_6B8")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_45F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47C")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CB")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -2370, 4000, 13480, 90)
    SetChrPos(0xA, -840, 4000, 13480, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C6")
    SetChrFlags(0xFE, 0x10)

    label("loc_4C6")

    Jump("loc_6B8")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_516")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 1000, 0, 3700, 270)
    SetChrPos(0xA, -500, 0, 3700, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    Jump("loc_6B8")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BD")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_569")
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_5B8")

    label("loc_569")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B8")
    SetChrPos(0x8, 7140, 4500, 5660, 180)
    SetChrPos(0x9, 7910, 0, -1840, 90)
    SetChrPos(0xA, 5410, 4000, 5440, 90)
    Jump("loc_5B8")

    label("loc_5B8")

    Jump("loc_6B8")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5DA")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_69B")

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_69B")

    label("loc_61D")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65D")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_65D")

    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0x8, 0x2)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x9, 1000, 0, 3730, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68A")
    SetChrFlags(0x9, 0x10)

    label("loc_68A")

    SetChrPos(0xA, 8060, 0, -2310, 135)

    label("loc_69B")

    Jump("loc_6B8")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6B8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_6B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6CC")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F9")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_6F9")

    Return()

    # Function_2_2CB end

    def Function_3_6FA(): pass

    label("Function_3_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73F")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_73F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_77A")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79E")
    Jump("loc_7B1")

    label("loc_79E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AD")
    Jump("loc_7B1")

    label("loc_7AD")

    OP_66(0x0, 0x1)

    label("loc_7B1")

    Return()

    # Function_3_6FA end

    def Function_4_7B2(): pass

    label("Function_4_7B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7C3")
    Jump("loc_164B")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_824")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DE")
    Call(0, 5)
    Jump("loc_81F")

    label("loc_7DE")


    ChrTalk(
        0xFE,
        (
            "Damn... Why did\x01",
            "something like this have\x01",
            "to happen to us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F")

    Jump("loc_164B")

    label("loc_824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93E")

    ChrTalk(
        0xFE,
        (
            "We did get a notice from the\x01",
            "Republican government to leave\x01",
            "Crossbell and hurry back, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. As if we'd return\x01",
            "with the trains jammed\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll wait for our driving\x01",
            "license suspensions to clear and\x01",
            "leisurely make our way back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9D5")

    label("loc_93E")


    ChrTalk(
        0xFE,
        (
            "As if we'd return with\x01",
            "the trains jammed like\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll wait for our driving\x01",
            "license suspensions to clear and\x01",
            "leisurely make our way back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D5")

    Jump("loc_164B")

    label("loc_9DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B39")

    ChrTalk(
        0xFE,
        (
            "I heard a lot of police\x01",
            "and CGF were injured in\x01",
            "the attack the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehehe... Serves 'em right. They\x01",
            "so rudely gave us that community\x01",
            "service punishment, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(...Let's just go. We\x01",
            "don't have time to care\x01",
            "about people like him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Anything said to a fool\x01",
            "will be wasted, after\x01",
            "all.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BA9")

    label("loc_B39")


    ChrTalk(
        0xFE,
        (
            "I heard a lot of police\x01",
            "and CGF were injured in\x01",
            "the attack the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehehe... Serves 'em\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA9")

    Jump("loc_164B")

    label("loc_BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E07")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D18")

    ChrTalk(
        0xFE,
        (
            "Hmph, a punishment's a\x01",
            "punishment. I'll just\x01",
            "shut up and do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I've got to get out of\x01",
            "here. I don't have time\x01",
            "to worry about you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Seems like they're\x01",
            "dealing with Officer\x01",
            "Kate's anger pretty well.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F(Yeah... I don't think we'll\x01",
            "have to worry about their\x01",
            "stupid behavior for a while.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFF")

    label("loc_D18")


    ChrTalk(
        0xFE,
        "...Whaddya want.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't have time to worry\x01",
            "about any coppers. ...I've\x01",
            "gotta get outta here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Could something have\x01",
            "happened...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(Come to think of it,\x01",
            "the orbal car that's\x01",
            "usually here is gone...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFF")

    SetScenarioFlags(0x0, 0)
    Jump("loc_E57")

    label("loc_E07")


    ChrTalk(
        0xFE,
        (
            "...I've got to get out of\x01",
            "here. I don't have time\x01",
            "to worry about you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E57")

    Jump("loc_164B")

    label("loc_E5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E6A")
    Jump("loc_164B")

    label("loc_E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EE6")

    ChrTalk(
        0xFE,
        (
            "Tch, that Reggie is slow\x01",
            "at everything except\x01",
            "driving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've gotta get me some\x01",
            "black tea right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164B")

    label("loc_EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_EF4")
    Jump("loc_164B")

    label("loc_EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F02")
    Jump("loc_164B")

    label("loc_F02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_102D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE8")

    ChrTalk(
        0xFE,
        (
            "Today we tried to go to\x01",
            "Noue Blan or whatever in\x01",
            "Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. You commoners\x01",
            "needn't concern yourselves\x01",
            "with a place like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(I-I don't think that's\x01",
            "the case...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1028")

    label("loc_FE8")


    ChrTalk(
        0xFE,
        (
            "...Even so, they're\x01",
            "slow. What are Sykes and\x01",
            "Reggie doing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1028")

    Jump("loc_164B")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1289")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F9")

    ChrTalk(
        0xFE,
        (
            "...Whaddya need with us\x01",
            "in the middle of the\x01",
            "night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't tell you that I\x01",
            "forgot... what you did\x01",
            "to us today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00605F(Did... Something happen\x01",
            "with them?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Well, you see, it's\x01",
            "like we didn't have a\x01",
            "choice...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F(Honestly... Causing stupid\x01",
            "trouble in this delicate\x01",
            "time...)\x02\x03",
            "#00600F(Absolutely never let your guard\x01",
            "down until tomorrow's conference\x01",
            "is over. ...Understood?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(R-Roger.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 3)
    Jump("loc_1284")

    label("loc_11F9")


    ChrTalk(
        0xFE,
        (
            "I won't tell you that I\x01",
            "forgot... what you did\x01",
            "to us today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll make you regret it\x01",
            "one day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(So damn persistent...)\x02",
    )

    CloseMessageWindow()

    label("loc_1284")

    Jump("loc_164B")

    label("loc_1289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1335")

    ChrTalk(
        0xFE,
        (
            "With the way you treated\x01",
            "me... Don't think you'll\x01",
            "get away with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The state police\x01",
            "shouldn't get carried\x01",
            "away, you know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_137E")

    label("loc_1335")


    ChrTalk(
        0xFE,
        (
            "With the way you treated\x01",
            "me... Don't think you'll\x01",
            "get away with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137E")

    Jump("loc_15AD")

    label("loc_1383")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150A")

    ChrTalk(
        0xFE,
        (
            "...Damn... Treating me\x01",
            "like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys... Don't think\x01",
            "you'll get away with\x01",
            "this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FAhaha. And you're so weak,\x01",
            "too. Look at you,\x01",
            "pretending to be all tough.\x02\x03",
            "#04604FWell, if you wanna go, feel\x01",
            "free to bring it anytime.\x02\x03",
            "#04611FBe prepared to die, of\x01",
            "course♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Dammit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F...Enough already. Let's\x01",
            "go, Shirley.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_154B")

    label("loc_150A")


    ChrTalk(
        0xFE,
        (
            "...Damn... Treating me\x01",
            "like this... I'll never\x01",
            "forgive you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_154B")

    Jump("loc_15AD")

    label("loc_1550")


    ChrTalk(
        0xFE,
        (
            "Hehe, it barged into our\x01",
            "castle uninvited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A suitable punishment\x01",
            "was only fitting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AD")

    Jump("loc_164B")

    label("loc_15B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_15C0")
    Jump("loc_164B")

    label("loc_15C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1642")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E3")
    Call(0, 6)
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_15E3")


    ChrTalk(
        0xFE,
        "Oh, you guys came back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, you finished?\x01",
            "Hurry up and leave\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_1642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_164B")

    label("loc_164B")

    TalkEnd(0xFE)
    Return()

    # Function_4_7B2 end

    def Function_5_164F(): pass

    label("Function_5_164F")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "Whoa! It's full of\x01",
            "monsters outside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Could they be after us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Y-Yuri! What do we do!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I-I'm thinking. Shaddap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Damn... Why did\x01",
            "something like this have\x01",
            "to happen to us...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_181C")

    ChrTalk(
        0x101,
        (
            "#00005F(The Highbloods... So\x01",
            "they're still in\x01",
            "Crossbell, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Looks like they missed\x01",
            "their chance to return\x01",
            "to the Republic.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Well, as long as they stay\x01",
            "here, they should be ok even\x01",
            "if we leave them alone.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181C")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_5_164F end

    def Function_6_1837(): pass

    label("Function_6_1837")


    ChrTalk(
        0xB,
        (
            "Even so, you're all so\x01",
            "young and you live in this\x01",
            "big mansion. Amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha, it's no big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Compared to that of our\x01",
            "parents in the Republic,\x01",
            "this is a dog house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(T-They said "dog\x01",
            "house"...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Haha, they've really\x01",
            "gotten carried away.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_1837 end

    def Function_7_195B(): pass

    label("Function_7_195B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_196C")
    Jump("loc_21F7")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1A01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1987")
    Call(0, 5)
    Jump("loc_19FC")

    label("loc_1987")


    ChrTalk(
        0xFE,
        (
            "Ah, enough already. Why\x01",
            "is this happening!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we're attacked, who's\x01",
            "going to take\x01",
            "responsibility for it!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FC")

    Jump("loc_21F7")

    label("loc_1A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1AB1")

    ChrTalk(
        0xFE,
        (
            "A declaration of independence,\x01",
            "huh. People have been making a\x01",
            "fuss about it for ages, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, Yuri said it'll be\x01",
            "all right so it probably\x01",
            "will be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_1AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B65")

    ChrTalk(
        0xFE,
        (
            "Ah, it's all gloomy\x01",
            "around Downtown lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright, I think I'll go\x01",
            "for a drive around here,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, but... I don't\x01",
            "have a car...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BCD")

    label("loc_1B65")


    ChrTalk(
        0xFE,
        "*sigh*... My car broke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanted to go for a\x01",
            "recreational drive, but\x01",
            "I'll have to do without.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCD")

    Jump("loc_21F7")

    label("loc_1BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C47")

    ChrTalk(
        0xFE,
        (
            "Aww, man... That orbal\x01",
            "car had the best ride...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like I'm gonna be\x01",
            "bored for a while...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_1C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C55")
    Jump("loc_21F7")

    label("loc_1C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1CD9")

    ChrTalk(
        0xFE,
        (
            "Hehe, the drive course\x01",
            "I've been using lately\x01",
            "is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I knew the highways were\x01",
            "better than city roads.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_1CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CE7")
    Jump("loc_21F7")

    label("loc_1CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CF5")
    Jump("loc_21F7")

    label("loc_1CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBC")

    ChrTalk(
        0xFE,
        (
            "That Yuri. Because of last\x01",
            "night's drive, he's\x01",
            "completely over his bad mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, that guy sure is a\x01",
            "handful. ...I'd never say\x01",
            "that to his face, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    TalkEnd(0xFE)
    SetChrFlags(0xFE, 0x10)
    Return()

    label("loc_1DBC")


    ChrTalk(
        0xFE,
        (
            "Alright, let's get ready\x01",
            "to go to Noue Blan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...What's wrong, Reggie?\x01",
            "You look kinda sleepy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_1E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1E39")
    Call(0, 9)
    Jump("loc_21F7")

    label("loc_1E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2165")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED3")

    ChrTalk(
        0xFE,
        "Eek!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Say, that redhead\x01",
            "isn't here anymore,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...H-Hmph! Don't get\x01",
            "carried away, you hear!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F28")

    label("loc_1ED3")


    ChrTalk(
        0xFE,
        (
            "I wasn't scared or\x01",
            "anything! Got that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't get carried away,\x01",
            "you hear!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F28")

    Jump("loc_2160")

    label("loc_1F2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2089")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    ChrTalk(
        0xFE,
        (
            "Eek... You're here\x01",
            "again!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "G-Get away from me!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04606FHmm~? Shirley isn't\x01",
            "interested in you guys,\x01",
            "though.\x02\x03",
            "#04609FC'mon. Let's hurry and\x01",
            "look for Mary♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FY-Yeah... Sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FThat bloodlust she just\x01",
            "had was just her being\x01",
            "innocent.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20DB")

    label("loc_2089")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "D-Don't come any\x01",
            "closer!! Get the hell\x01",
            "out of here!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DB")

    Jump("loc_2160")

    label("loc_20E0")


    ChrTalk(
        0xFE,
        (
            "Haha, I saw her earlier.\x01",
            "When we threatened her a\x01",
            "little, she ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who knew bullying the\x01",
            "weak could be this fun?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2160")

    Jump("loc_21F7")

    label("loc_2165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2173")
    Jump("loc_21F7")

    label("loc_2173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_21EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218E")
    Call(0, 8)
    Jump("loc_21E9")

    label("loc_218E")


    ChrTalk(
        0xFE,
        (
            "...What's with you guys?\x01",
            "New members or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, don't get carried\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E9")

    Jump("loc_21F7")

    label("loc_21EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21F7")

    label("loc_21F7")

    TalkEnd(0xFE)
    Return()

    # Function_7_195B end

    def Function_8_21FB(): pass

    label("Function_8_21FB")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        (
            "C'mon. Sit there\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've got some good wine\x01",
            "ready. Let's drink it\x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uhuhu, then allow me to\x01",
            "pour.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_8_21FB end

    def Function_9_2293(): pass

    label("Function_9_2293")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2436")

    ChrTalk(
        0x9,
        (
            "That Yuri is in a really\x01",
            "bad mood...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even if we went to the Entertainment District\x01",
            "for a change of pace, it seems there're plenty\x01",
            "of officers due to VIP security or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, then... How about\x01",
            "we go for a night drive\x01",
            "on the mountain path?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There will be few passerbys at\x01",
            "this hour and we could go all\x01",
            "out at our hearts' content...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ohh, that might be a\x01",
            "good idea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24A1")

    label("loc_2436")


    ChrTalk(
        0x9,
        (
            "Alright, that being the\x01",
            "case, let's go propose\x01",
            "it to Yuri.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Reggie, prepare the car.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Got it.\x02",
    )

    CloseMessageWindow()

    label("loc_24A1")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_2293 end

    def Function_10_24AA(): pass

    label("Function_10_24AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24BB")
    Jump("loc_2CC1")

    label("loc_24BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_253C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D6")
    Call(0, 5)
    Jump("loc_2537")

    label("loc_24D6")


    ChrTalk(
        0xFE,
        (
            "I knew it. We should have tried\x01",
            "to return to the Republic when\x01",
            "independence was declared...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2537")

    Jump("loc_2CC1")

    label("loc_253C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_25B9")

    ChrTalk(
        0xFE,
        (
            "Yuri seems calm, but...\x01",
            "W-Will we be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we miss our timing,\x01",
            "we won't be able to\x01",
            "return...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC1")

    label("loc_25B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2652")

    ChrTalk(
        0xFE,
        (
            "(Yuri said that, but...\x01",
            "As expected, he's being\x01",
            "unreasonable.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Because we said we're\x01",
            "not concerned, he's not\x01",
            "concerned either.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC1")

    label("loc_2652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_27C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2714")

    ChrTalk(
        0xFE,
        (
            "...Achoo!! I might have\x01",
            "caught a cold...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's because I\x01",
            "fell in the pond\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*, maybe this is\x01",
            "what I deserve. I can't\x01",
            "do anything!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27C1")

    label("loc_2714")


    ChrTalk(
        0xFE,
        (
            "*sniff, sniff*... Maybe I'll\x01",
            "go to St. Ursula Hospital\x01",
            "for some medicine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard something terrible\x01",
            "happened at Mainz. I wonder if\x01",
            "the buses are on schedule...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C1")

    Jump("loc_2CC1")

    label("loc_27C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27D4")
    Jump("loc_2CC1")

    label("loc_27D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2896")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2861")

    ChrTalk(
        0xFE,
        (
            "Huh? I thought I heard\x01",
            "sirens just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, whatever. Let's\x01",
            "see, Yuri's favorite\x01",
            "black tea is...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2891")

    label("loc_2861")


    ChrTalk(
        0xFE,
        (
            "Let's see, Yuri's\x01",
            "favorite black tea is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2891")

    Jump("loc_2CC1")

    label("loc_2896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28A4")
    Jump("loc_2CC1")

    label("loc_28A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28B2")
    Jump("loc_2CC1")

    label("loc_28B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_29F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2975")

    ChrTalk(
        0xFE,
        (
            "From last night until this\x01",
            "morning, I made a lot of trips\x01",
            "through the mountain path...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, so sleepy... I\x01",
            "wanted Yuri and Sykes to\x01",
            "help with the driving.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29ED")

    label("loc_2975")


    ChrTalk(
        0xFE,
        (
            "Thank goodness Yuri's\x01",
            "mood has improved,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, so sleepy... I\x01",
            "gotta sleep before going\x01",
            "for drinks...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29ED")

    Jump("loc_2CC1")

    label("loc_29F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2A03")
    Call(0, 9)
    Jump("loc_2CC1")

    label("loc_2A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C21")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A8A")

    ChrTalk(
        0xFE,
        (
            "I-I swear! We didn't\x01",
            "tease that cat at all!\x01",
            "Ya gotta believe us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that brat comes\x01",
            "again... Hmph.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C1C")

    label("loc_2A8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B94")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    ChrTalk(
        0xFE,
        "Uwah! Again!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#4S#04602F...Wah!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eeeek!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FAhahaha, what're you so\x01",
            "scared of, hmm?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A3, 500)

    ChrTalk(
        0x102,
        (
            "#00106F(*sigh*... Her innocence\x01",
            "is wicked, in a certain\x01",
            "way...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BCA")

    label("loc_2B94")


    ChrTalk(
        0xFE,
        (
            "C-Cut it out... We\x01",
            "didn't tease that cat at\x01",
            "all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BCA")

    Jump("loc_2C1C")

    label("loc_2BCF")


    ChrTalk(
        0xFE,
        (
            "Hehe, what a\x01",
            "masterpiece~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it was small and\x01",
            "looked pathetic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1C")

    Jump("loc_2CC1")

    label("loc_2C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C2F")
    Jump("loc_2CC1")

    label("loc_2C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CB8")

    ChrTalk(
        0xFE,
        (
            "Now then, I gotta make\x01",
            "the side dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I think I'll open\x01",
            "this expensive wine I\x01",
            "brought from the Republic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC1")

    label("loc_2CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CC1")

    label("loc_2CC1")

    TalkEnd(0xFE)
    Return()

    # Function_10_24AA end

    def Function_11_2CC5(): pass

    label("Function_11_2CC5")

    Call(0, 12)
    Return()

    # Function_11_2CC5 end

    def Function_12_2CC9(): pass

    label("Function_12_2CC9")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CDE")
    Call(0, 6)
    Jump("loc_2D37")

    label("loc_2CDE")


    ChrTalk(
        0xB,
        (
            "(It's been a while, you\x01",
            "guys☆)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "(Haha. It's good to be\x01",
            "able to earn a living.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D37")

    TalkEnd(0xB)
    SetChrSubChip(0xB, 0x1)
    Return()

    # Function_12_2CC9 end

    def Function_13_2D3F(): pass

    label("Function_13_2D3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D54")
    Call(0, 8)
    Jump("loc_2DC2")

    label("loc_2D54")

    OP_4B(0xFE, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Huh? That car outside's\x01",
            "yours!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe, nice, isn't it.\x01",
            "Wanna ride with us next\x01",
            "time?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0x9, 0xFF)

    label("loc_2DC2")

    TalkEnd(0xFE)
    Return()

    # Function_13_2D3F end

    def Function_14_2DC6(): pass

    label("Function_14_2DC6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch47502.itc", 0x1E)
    LoadChrToIndex("chr/ch26800.itc", 0x1F)
    LoadChrToIndex("chr/ch26900.itc", 0x20)
    LoadChrToIndex("chr/ch44102.itc", 0x21)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5700, 200, 4900, 180)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 7900, 200, 2450, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5700, 0, 470, 360)
    OP_4B(0xA, 0xFF)
    OP_68(5030, 1500, 1370, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24150, 0)
    SetCameraDistance(23150, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0x8,
        (
            "#5PMan, what a thrill, that\x01",
            "drive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PHehe, the rain today's\x01",
            "just perfect for drift\x01",
            "racing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, my heart's still\x01",
            "pounding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way Reggie, I wonder\x01",
            "if that girl you called\x01",
            "this morning's coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12POh yeah, any minute\x01",
            "now...\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x105, 0x80)
    OP_68(2670, 1400, -1580, 0)
    MoveCamera(19, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 1500, 50, -2250, 45)
    SetChrPos(0x109, 500, 50, -2500, 45)
    SetChrPos(0x102, 1500, 50, -3500, 45)
    SetChrPos(0x105, 500, 50, -3750, 45)
    OP_0D()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_308E():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_308E)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)

    ChrTalk(
        0xA,
        "Oh here she is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHaha, perfect timing!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3409")
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Hey─ Aren't you those\x01",
            "cops from yesterday!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Why the hell are you\x01",
            "guys here!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105F...Wait, so you're the\x01",
            "ones who were driving\x01",
            "like maniacs yesterday?\x02\x03",
            "#00103FWhat exactly is going on\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FIs this is a robbery or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FIf that's the case, then\x01",
            "we caught them red-\x01",
            "handed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "D-Don't be stupid!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If we were robbers,\x01",
            "would we just stick\x01",
            "around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnyway, what the hell do\x01",
            "cops like you need from\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou've got some nerve\x01",
            "barging into our house\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FThen that means...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah. Looks like these\x01",
            "guys are the new\x01",
            "residents.\x02\x03",
            "#00000FGuys, we're actually today\x01",
            "here on official police\x01",
            "business.\x02\x03",
            "We won't take much of your\x01",
            "time, but we do need to\x01",
            "ask you a few questions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_362E")

    label("loc_3409")

    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Oh, they're quite the\x01",
            "pretty ones aren't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, even better than\x01",
            "expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105F...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FWhat are you talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, thanks for bringing\x01",
            "them over. Hang on, I'll\x01",
            "get you guys a tip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FOh brother. I bet those guys\x01",
            "think they're the hostesses\x01",
            "they called to their house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FI'll get right to the\x01",
            "point.\x02\x03",
            "#00000FWe're with the Crossbell\x01",
            "Police, Special Support\x01",
            "Section.\x02\x03",
            "We won't take much of your\x01",
            "time, but we do need to\x01",
            "ask you a few questions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -700, 0, 3250, 180)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 300, 0, 3250, 180)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -1700, 0, 3250, 180)
    SetChrPos(0x101, -1260, 0, -250, 0)
    SetChrPos(0x102, -100, 0, -250, 0)
    SetChrPos(0x109, -1260, 0, -1800, 0)
    SetChrPos(0x105, -100, 0, -1800, 0)
    OP_68(-890, 1400, 510, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(190, 0)
    SetCameraDistance(42740, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00003FSo you three came to Crossbell to\x01",
            "study the culture here.\x02\x03",
            "And, while looking for a place to\x01",
            "stay, you happened to find this house\x01",
            "for sale and Yuri here bought it...\x02\x03",
            "#00001FIs that how it went?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYeah. Understand?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FBy the way─ What does\x01",
            "the name "Highbloods"\x01",
            "refer to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHehe, you want to know?\x01",
            "That's the name of our\x01",
            "3-man group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PThose of Noble Blood─ It's\x01",
            "just perfect for we who\x01",
            "are loved by the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PActually, all of our\x01",
            "fathers are higher ups\x01",
            "at that Verne Company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAnd Yuri's dad is a board\x01",
            "member. So we're the ones\x01",
            "you need to suck up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHeh, that's exactly\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_68(-580, 1400, -640, 3000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xD, 1260, 0, -4800, 0)
    SetChrPos(0xE, 1260, 0, -6000, 0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3A0C():
        OP_95(0xD, 1260, 0, -2000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3A0C)
    Sleep(50)

    def lambda_3A29():
        OP_95(0xE, 1260, 0, -3000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3A29)
    Sleep(50)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xD, 1)
    Sound(104, 0, 100, 0)

    def lambda_3A7A():
        OP_93(0xD, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3A7A)
    Sleep(50)
    WaitChrThread(0xE, 1)

    def lambda_3A8E():
        OP_93(0xE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3A8E)
    Sleep(50)

    def lambda_3A9E():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A9E)
    Sleep(50)

    def lambda_3AAE():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3AAE)
    Sleep(50)

    def lambda_3ABE():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3ABE)
    Sleep(50)

    def lambda_3ACE():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ACE)

    ChrTalk(
        0xA,
        (
            "#5PAh, finally! Sure took\x01",
            "them long enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5POh, now they're the real\x01",
            "deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PUmm... Which of you is\x01",
            "Mr. High Bloods?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PHmm, it looks like\x01",
            "you're a little busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh don't worry, we're\x01",
            "all done with these\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, can you guys get\x01",
            "out of here already?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C02():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C02)
    Sleep(50)

    def lambda_3C12():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C12)
    Sleep(50)

    def lambda_3C22():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C22)
    Sleep(50)

    def lambda_3C32():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C32)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00003FYou don't have to tell\x01",
            "us twice.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(128, 2000, 40)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c0300", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2DC6 end

    def Function_15_3C9E(): pass

    label("Function_15_3C9E")

    EventBegin(0x0)
    LoadChrToIndex("apl/ch51269.itc", 0x1E)
    SoundLoad(3975)
    SoundLoad(3976)
    SoundLoad(3977)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5700, 200, 4900, 180)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 950, 0, 700, 180)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5700, 0, 470, 360)
    OP_68(1710, 2500, -380, 0)
    MoveCamera(24, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23750, 0)
    SetChrPos(0x101, 980, 0, -6650, 0)
    SetChrPos(0x102, 980, 0, -6650, 0)
    SetChrPos(0x109, 980, 0, -6650, 0)
    SetChrPos(0x105, 980, 0, -6650, 0)
    SetChrPos(0x104, 980, 0, -6650, 0)
    SetChrPos(0x1A3, 980, 0, -6650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(1710, 1400, -380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(103, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 20)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 18)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 21)
    WaitChrThread(0x1A3, 3)
    OP_6F(0x1)

    ChrTalk(
        0x9,
        "Oh... What's this?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    TurnDirection(0xA, 0x101, 500)
    WaitChrThread(0xA, 1)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Hey! You're those\x01",
            "coppers from before!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmph... The Special\x01",
            "Support Section, I think\x01",
            "they said.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00003FThanks for your help\x01",
            "back then.\x02\x03",
            "#6P#00000FWe want to ask you a\x01",
            "little something. Is it\x01",
            "alright?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0x8, -700, 0, 3250, 180)
    SetChrPos(0xA, 300, 0, 3250, 180)
    SetChrPos(0x9, -1700, 0, 3250, 180)
    OP_68(-1040, 1400, 630, 0)
    MoveCamera(38, 26, 0, 0)
    OP_6E(190, 0)
    SetCameraDistance(42740, 0)
    SetChrPos(0x101, -1240, 0, 500, 0)
    SetChrPos(0x102, 160, 0, 200, 0)
    SetChrPos(0x109, -1180, 0, -900, 0)
    SetChrPos(0x105, 120, 120, -1080, 0)
    SetChrPos(0x104, -1140, 120, -2300, 0)
    SetChrPos(0x1A3, 90, 0, -2500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        "Wow, a cat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe... So that's how it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FDo you have any idea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FWe're wasting time. How\x01",
            "'bout answering already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hmm, what should we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yuri, what do we do?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4264")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆What about the Runaway\x01",
            "Crackdown 1? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",        # 0
            "[Cleared]\x01",          # 1
            "[Not Cleared]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4250")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_4264")

    label("loc_4250")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4264")
    OP_29(0x69, 0x3, 0x10)

    label("loc_4264")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4337")

    ChrTalk(
        0x8,
        "Hehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have you to thank for\x01",
            "putting a stop to that\x01",
            "prank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Accordingly, I want a\x01",
            "show of "good faith"\x01",
            "from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How about getting on\x01",
            "your knees or stripping?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4401")

    label("loc_4337")


    ChrTalk(
        0x8,
        "Hehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You've showed a certain\x01",
            "lack of respect during\x01",
            "this interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Accordingly, I want a\x01",
            "show of "good faith"\x01",
            "from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How about getting on\x01",
            "your knees or stripping?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4401")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xA,
        "#11PHaha! That's great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So there you have it.\x01",
            "Which'll it be, kneeling\x01",
            "or stripping?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ah, the guys don't need\x01",
            "to strip, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F(T-These guys...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106F(They're worse than we\x01",
            "thought.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306F(Seriously. Seems like\x01",
            "they're misunderstanding,\x01",
            "somehow.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F(Tch. As if they're\x01",
            "gonna bully us.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F(Yeah, leave this to me─\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1A3,
        (
            "#12P#04605F#3975VHey guys.\x02\x03",
            "#3976VYou're having this much\x01",
            "trouble?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF88)
    OP_C9(0x1, 0x80000000)

    def lambda_46B1():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46B1)
    Sleep(50)

    def lambda_46C1():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_46C1)
    Sleep(50)

    def lambda_46D1():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_46D1)
    Sleep(50)

    def lambda_46E1():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_46E1)
    Sleep(50)

    def lambda_46F1():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_46F1)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_68(-1220, 1400, 1530, 1000)
    SetChrChip(0x0, 0x1A3, 0x1E, 0x12C)
    Sound(809, 0, 100, 0)
    OP_95(0x1A3, -440, 0, -330, 8000, 0x0)
    OP_95(0x1A3, -660, 0, 2440, 8000, 0x0)
    SetChrChip(0x1, 0x1A3, 0x0, 0x0)
    OP_0D()
    SetChrChipByIndex(0x1A3, 0x1E)
    SetChrSubChip(0x1A3, 0x0)
    SetChrFlags(0x1A3, 0x2)
    OP_0D()
    SetChrPos(0x8, -700, 0, 3000, 180)
    Sleep(300)
    Sound(802, 0, 100, 0)
    Sound(811, 0, 30, 0)
    SetChrSubChip(0x1A3, 0x1)
    SetChrPos(0x8, -700, 200, 3000, 180)
    BeginChrThread(0x8, 3, 0, 22)
    OP_6F(0x1)

    def lambda_47B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47B0)
    Sleep(50)

    def lambda_47C0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47C0)
    Sleep(50)

    def lambda_47D0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_47D0)
    Sleep(50)

    def lambda_47E0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_47E0)
    Sleep(50)

    def lambda_47F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_47F0)
    Sleep(50)

    def lambda_4800():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4800)
    Sleep(50)

    def lambda_4810():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4810)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5PUgh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04609FAlrighty then. Time to\x01",
            "spit it out, wouldn't\x01",
            "you say?\x02\x03",
            "#04611FPerhaps you'd like to\x01",
            "resist so I can rip your\x01",
            "brains out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PUgh... Ah...\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_49C5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_49C5)
    Sleep(50)

    def lambda_49E2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_49E2)
    WaitChrThread(0x9, 1)

    def lambda_4A00():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4A00)
    WaitChrThread(0xA, 1)

    def lambda_4A11():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4A11)
    Sleep(300)

    ChrTalk(
        0xA,
        "#11PH-Hey! What're you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThis brat! What are you\x01",
            "doing to Yur─\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1A3,
        (
            "#12P#04611F#3977V─You're annoying. I'll\x01",
            "kill this guy, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF89)
    OP_C9(0x1, 0x80000000)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5PWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FW-Wait a second!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FT-That would be a\x01",
            "little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F*sigh*... Seriously.\x02\x03",
            "#00301F─Guys. Do as she says.\x02\x03",
            "She's dangerous. The\x01",
            "truth. Without\x01",
            "hesitation. Now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PF-Fine... I'll talk!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PT-There was a cat. Just\x01",
            "before you came!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWe teased her a bit and\x01",
            "she left immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PShe's got to be around\x01",
            "here somewhere, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P―That should be good\x01",
            "right? Let Yuri go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04604FOh, you teased a cute\x01",
            "kitty, did you?\x02\x03",
            "#04609FKind of like this?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A3, 0x2)
    SetChrPos(0x9, -1500, 0, 2400, 90)
    Sleep(300)
    Sound(802, 0, 100, 0)
    Sound(811, 0, 30, 0)
    SetChrSubChip(0x1A3, 0x3)
    SetChrPos(0x9, -1500, 200, 2400, 90)
    BeginChrThread(0x9, 3, 0, 22)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#5PUgh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAh!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A3, 0x4)

    ChrTalk(
        0x1A3,
        "#6P#04611FWanna join him?\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xA, 0xB4, 0x1F4, 0x7D0, 0x0)

    ChrTalk(
        0xA,
        "#11P*shiver*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#6P#04609FAhaha, so you get it\x01",
            "then.\x02\x03",
            "#04604FWell then─\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrSubChip(0x1A3, 0x0)
    ClearChrFlags(0x1A3, 0x2)
    SetChrPos(0x8, -700, 0, 3250, 180)
    SetChrPos(0x9, -1700, 0, 2400, 90)
    Sleep(100)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0xB4, 0x0)

    def lambda_4F0D():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4F0D)
    Sleep(50)

    def lambda_4F25():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F25)

    ChrTalk(
        0x8,
        "Buha... Ha ha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yeah, yeah!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)

    ChrTalk(
        0x1A3,
        (
            "#5P#04600FSo it seems like Mary's\x01",
            "around.\x02\x03",
            "#04609FLet's hurry㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FR-Right...\x02\x03",
            "#12P#00003FUmm... Thanks for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHaha. By the way, she\x01",
            "has no connection with\x01",
            "the police at all.\x02\x03",
            "#10309FI think you got bitten\x01",
            "by a cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PShut up! Just get out of\x01",
            "here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou guys... You won't\x01",
            "get away with this!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c0300", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_15_3C9E end

    def Function_16_50E3(): pass

    label("Function_16_50E3")


    def lambda_50E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50E8)

    def lambda_50F9():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50F9)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 920, 0, -1940, 2000, 0x0)
    Return()

    # Function_16_50E3 end

    def Function_17_5127(): pass

    label("Function_17_5127")


    def lambda_512C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_512C)

    def lambda_513D():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_513D)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -100, 0, -3320, 2000, 0x0)
    OP_95(0x102, -100, 0, -1870, 2000, 0x0)
    Return()

    # Function_17_5127 end

    def Function_18_517F(): pass

    label("Function_18_517F")


    def lambda_5184():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5184)

    def lambda_5195():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5195)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2210, 0, -3320, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_18_517F end

    def Function_19_51CA(): pass

    label("Function_19_51CA")


    def lambda_51CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_51CF)

    def lambda_51E0():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_51E0)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 2210, 0, -3320, 2000, 0x0)
    OP_95(0x109, 2210, 0, -1870, 2000, 0x0)
    Return()

    # Function_19_51CA end

    def Function_20_5222(): pass

    label("Function_20_5222")


    def lambda_5227():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5227)

    def lambda_5238():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5238)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -100, 0, -3320, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_20_5222 end

    def Function_21_526D(): pass

    label("Function_21_526D")


    def lambda_5272():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_5272)

    def lambda_5283():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_5283)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_21_526D end

    def Function_22_529D(): pass

    label("Function_22_529D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52CD")

    def lambda_52AD():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_52AD)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_22_529D")

    label("loc_52CD")

    Return()

    # Function_22_529D end

    SaveToFile()

Try(main)
