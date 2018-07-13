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
        "Function_5_1668",         # 05, 5
        "Function_6_185E",         # 06, 6
        "Function_7_1984",         # 07, 7
        "Function_8_2244",         # 08, 8
        "Function_9_22DC",         # 09, 9
        "Function_10_24F9",        # 0A, 10
        "Function_11_2D09",        # 0B, 11
        "Function_12_2D0D",        # 0C, 12
        "Function_13_2D8E",        # 0D, 13
        "Function_14_2E16",        # 0E, 14
        "Function_15_3D17",        # 0F, 15
        "Function_16_51B8",        # 10, 16
        "Function_17_51FC",        # 11, 17
        "Function_18_5254",        # 12, 18
        "Function_19_529F",        # 13, 19
        "Function_20_52F7",        # 14, 20
        "Function_21_5342",        # 15, 21
        "Function_22_5372",        # 16, 22
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
    Jump("loc_1664")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_824")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DE")
    Call(0, 5)
    Jump("loc_81F")

    label("loc_7DE")


    ChrTalk(
        0xFE,
        (
            "Damn... Why did something like\x01",
            "this have to happen to us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81F")

    Jump("loc_1664")

    label("loc_824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93E")

    ChrTalk(
        0xFE,
        (
            "We did get a notice from the Republican government\x01",
            "to leave Crossbell and hurry back, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. As if we'd\x01",
            "return with the trains\x01",
            "jammed like this.\x02",
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
            "As if we'd return\x01",
            "with the trains\x01",
            "jammed like this.\x02",
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

    Jump("loc_1664")

    label("loc_9DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B40")

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
            "Hehehe... Serves 'em right. \x01",
            "They so rudely gave us that community\x01",
            "service punishment, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(...Let's just go. We don't have\x01",
            "time to care about people like him.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Well, anything said to a fool\x01",
            "will be wasted, after all.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BB0")

    label("loc_B40")


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
        "Hehehe... Serves 'em right.\x02",
    )

    CloseMessageWindow()

    label("loc_BB0")

    Jump("loc_1664")

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E01")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D15")

    ChrTalk(
        0xFE,
        (
            "Hmph, a punishment's a punishment.\x01",
            "I'll just behave for some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Scram away. I don't have time\x01",
            "to be concerned about you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Seems like having been scolded by\x01",
            "Miss Kate had quite the effect.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F(Yeah... I don't think we'll\x01",
            "have to worry about his\x01",
            "stupid behavior for awhile.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF9")

    label("loc_D15")


    ChrTalk(
        0xFE,
        "...What do you want.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't have time to worry\x01",
            "about any coppers...\x01",
            "...Scram outta here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(Could something have happened...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(Come to think of it, the orbal car\x01",
            "that's usually here is gone...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF9")

    SetScenarioFlags(0x0, 0)
    Jump("loc_E47")

    label("loc_E01")


    ChrTalk(
        0xFE,
        (
            "...Scram away. I don't have time\x01",
            "to be concerned about you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E47")

    Jump("loc_1664")

    label("loc_E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E5A")
    Jump("loc_1664")

    label("loc_E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EC0")

    ChrTalk(
        0xFE,
        (
            "Tch, that Reggie is slow\x01",
            "except at driving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want some black\x01",
            "tea right away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1664")

    label("loc_EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_ECE")
    Jump("loc_1664")

    label("loc_ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_EDC")
    Jump("loc_1664")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_100E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCA")

    ChrTalk(
        0xFE,
        (
            "Today we'll try to go to\x01",
            ""Neue-Blanc" or whatever in\x01",
            "the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. You commoners needn't concern\x01",
            "yourselves with a place like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(I-I don't think that's the case...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1009")

    label("loc_FCA")


    ChrTalk(
        0xFE,
        (
            "...Even so, they're late.\x01",
            "What're Sykes and Reggie doing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1009")

    Jump("loc_1664")

    label("loc_100E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1277")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DE")

    ChrTalk(
        0xFE,
        "...What do you want in the dead of night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't tell you that I forgot...\x01",
            "What you did to us during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00605F(Did...\x01",
            "Anything happen with them?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Well, you see, it's like we\x01",
            "couldn't avoid it happening...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F(Honestly...causing stupid trouble\x01",
            "in this delicate time...)\x02\x03",
            "#00600F(Don't absolutely let your guard down\x01",
            "until tomorrow's conference is over.\x01",
            "...Understood?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(R-Roger.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 3)
    Jump("loc_1272")

    label("loc_11DE")


    ChrTalk(
        0xFE,
        (
            "I won't tell you that I forgot...\x01",
            "What you did to us during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll make you regret it one day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(So damn persistent...)\x02",
    )

    CloseMessageWindow()

    label("loc_1272")

    Jump("loc_1664")

    label("loc_1277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1373")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1324")

    ChrTalk(
        0xFE,
        (
            "With the way you treated me... \x01",
            "Don't think you'll get away with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The state police shouldn't\x01",
            "get carried away, you know?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_136E")

    label("loc_1324")


    ChrTalk(
        0xFE,
        (
            "With the way you treated me... \x01",
            "Don't think you'll get away with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136E")

    Jump("loc_15AF")

    label("loc_1373")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FB")

    ChrTalk(
        0xFE,
        (
            "...Damn... \x01",
            "Treating me like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys... Don't think\x01",
            "you'll get away with this...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FAhaha, you're so weak and look\x01",
            "at you, pretending to be all tough.\x02\x03",
            "#04604FWell, if you wanna go, feel\x01",
            "free to bring it anytime.\x02\x03",
            "#04611FBe prepared to die, of course♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Dammit...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F...Enough already. Let's go, Shirley.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1541")

    label("loc_14FB")


    ChrTalk(
        0xFE,
        (
            "...Damn... \x01",
            "Treating me like this... \x01",
            "I'll never forgive you...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1541")

    Jump("loc_15AF")

    label("loc_1546")


    ChrTalk(
        0xFE,
        (
            "Hehe, it barged into\x01",
            "our castle uninvited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's only fitting to give\x01",
            "it a suitable punishment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AF")

    Jump("loc_1664")

    label("loc_15B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_15C2")
    Jump("loc_1664")

    label("loc_15C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_165B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E5")
    Call(0, 6)
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_15E5")


    ChrTalk(
        0xFE,
        "Oh, you guys were still here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph, you finished your job, right? \x01",
            "Hurry up and leave already.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_165B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1664")

    label("loc_1664")

    TalkEnd(0xFE)
    Return()

    # Function_4_7B2 end

    def Function_5_1668(): pass

    label("Function_5_1668")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        "Whoa! It's full of monsters outside!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "What if they come\x01",
            "after us too...?\x02",
        )
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
            "Damn... Why did something like\x01",
            "this have to happen to us...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1843")

    ChrTalk(
        0x101,
        (
            "#00005F(The "High Bloods"... \x01",
            "So they're still in Crossbell, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Looks like they missed their\x01",
            "chance to return to the Republic.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Well, as long as they stay here, they\x01",
            "should be ok even if we leave 'em alone.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1843")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_5_1668 end

    def Function_6_185E(): pass

    label("Function_6_185E")


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
        "Hu hu, it's no big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Compared to that of our parents in\x01",
            "the Republic, this is a dog house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F(T-They said "dog house"...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Ha ha, they've really\x01",
            "gotten carried away.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_185E end

    def Function_7_1984(): pass

    label("Function_7_1984")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1995")
    Jump("loc_2240")

    label("loc_1995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1A2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B0")
    Call(0, 5)
    Jump("loc_1A26")

    label("loc_19B0")


    ChrTalk(
        0xFE,
        "Aah, enough already. Why is this happening!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we're attacked, who's going\x01",
            "to take responsibility for it!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A26")

    Jump("loc_2240")

    label("loc_1A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1ADC")

    ChrTalk(
        0xFE,
        (
            "A declaration of independence, huh. \x01",
            "People have been making a\x01",
            "fuss about it for ages, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, Yuri said it'll be all\x01",
            "right so it probably will be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2240")

    label("loc_1ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B90")

    ChrTalk(
        0xFE,
        (
            "*sigh*, recently\x01",
            "the whole city\x01",
            "is gloomy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright, I think I'll go for\x01",
            "a drive around here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, but... \x01",
            "I don't have a car...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C06")

    label("loc_1B90")


    ChrTalk(
        0xFE,
        (
            "*sigh*... \x01",
            "The car...we broke it, eh?\x02",
        )
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

    label("loc_1C06")

    Jump("loc_2240")

    label("loc_1C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C7F")

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
        "Looks like I'm gonna be bored for awhile...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2240")

    label("loc_1C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C8D")
    Jump("loc_2240")

    label("loc_1C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D12")

    ChrTalk(
        0xFE,
        (
            "Hehe, the drive course we've\x01",
            "been using lately is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I knew the highways were better than city roads.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2240")

    label("loc_1D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D20")
    Jump("loc_2240")

    label("loc_1D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D2E")
    Jump("loc_2240")

    label("loc_1D2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DF6")

    ChrTalk(
        0xFE,
        (
            "That Yuri. Because of last night's drive,\x01",
            "he's completely over his bad mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, that guy is sure a handful. \x01",
            "...I'd never say that to his face, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    TalkEnd(0xFE)
    SetChrFlags(0xFE, 0x10)
    Return()

    label("loc_1DF6")


    ChrTalk(
        0xFE,
        (
            "Alright, let's get ready\x01",
            "to go to "Neue-Blanc".\x02",
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
    Jump("loc_2240")

    label("loc_1E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1E76")
    Call(0, 9)
    Jump("loc_2240")

    label("loc_1E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21AF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1C")

    ChrTalk(
        0xFE,
        "Eek...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, that redheaded brat\x01",
            "is not here anymore, huh...\x02",
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
    Jump("loc_1F73")

    label("loc_1F1C")


    ChrTalk(
        0xFE,
        "I wasn't scared or anything! Got that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "D-Don't get carried away, you hear!?\x02",
    )

    CloseMessageWindow()

    label("loc_1F73")

    Jump("loc_21AA")

    label("loc_1F78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_212C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D5")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    ChrTalk(
        0xFE,
        "Eek... You're here again!?\x02",
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
            "#04606FHmm... Shirley isn't interested\x01",
            "in you guys, though.\x02\x03",
            "#04609FC'mon. Let's hurry and look for Mary♪\x02",
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
            "#10302FThat bloodlust she just had\x01",
            "was just her being innocent.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2127")

    label("loc_20D5")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "D-Don't come any closer!!\x01",
            "Get the hell out of here!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2127")

    Jump("loc_21AA")

    label("loc_212C")


    ChrTalk(
        0xFE,
        (
            "Ha ha, did you see that?\x01",
            "When we threatened\x01",
            "it a little, it ran away.\x02",
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

    label("loc_21AA")

    Jump("loc_2240")

    label("loc_21AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21BD")
    Jump("loc_2240")

    label("loc_21BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2237")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D8")
    Call(0, 8)
    Jump("loc_2232")

    label("loc_21D8")


    ChrTalk(
        0xFE,
        (
            "...So what's with you guys?\x01",
            "Wanna join or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, you look so envious.\x02",
    )

    CloseMessageWindow()

    label("loc_2232")

    Jump("loc_2240")

    label("loc_2237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2240")

    label("loc_2240")

    TalkEnd(0xFE)
    Return()

    # Function_7_1984 end

    def Function_8_2244(): pass

    label("Function_8_2244")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        "C'mon. Sit there already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've got some good wine ready.\x01",
            "Let's drink it together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uhuhu, then allow\x01",
            "me to pour.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_8_2244 end

    def Function_9_22DC(): pass

    label("Function_9_22DC")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2485")

    ChrTalk(
        0x9,
        (
            "That Yuri is in a\x01",
            "really bad mood...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even if we went to the Entertainment District\x01",
            "for a change of pace, it seems there're plenty\x01",
            "of officers due to VIPs security or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, then...\x01",
            "What about we go for a drive\x01",
            "at night on the mountain path?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "There will be few passersby at\x01",
            "this hour and we could go all\x01",
            "out at our heart's' content...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ooh, that could be a nice idea.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24F0")

    label("loc_2485")


    ChrTalk(
        0x9,
        (
            "Alright, being this the case,\x01",
            "let's go propose it to Yuri.\x02",
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

    label("loc_24F0")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_22DC end

    def Function_10_24F9(): pass

    label("Function_10_24F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_250A")
    Jump("loc_2D05")

    label("loc_250A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2589")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2525")
    Call(0, 5)
    Jump("loc_2584")

    label("loc_2525")


    ChrTalk(
        0xFE,
        (
            "I knew it. We should've tried\x01",
            "to return to the Republic when\x01",
            "independence was declared...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2584")

    Jump("loc_2D05")

    label("loc_2589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2605")

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
            "If we miss our chance\x01",
            "we won't be able\x01",
            "to return...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D05")

    label("loc_2605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_269F")

    ChrTalk(
        0xFE,
        (
            "(Yuri said that, but... \x01",
            "As expected, he's being unreasonable.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(Because we said we're\x01",
            "not concerned, he's\x01",
            "not concerned either.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D05")

    label("loc_269F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275A")

    ChrTalk(
        0xFE,
        (
            "...*achoo*!! I might\x01",
            "have caught a cold...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe it's because I fell\x01",
            "in the pond yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*, maybe this is what\x01",
            "I deserve. How dreary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_280D")

    label("loc_275A")


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
            "the buses are regularly working...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280D")

    Jump("loc_2D05")

    label("loc_2812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2820")
    Jump("loc_2D05")

    label("loc_2820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_28E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AD")

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
            "...Well, whatever. Let's see,\x01",
            "Yuri's favorite black tea is...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28DD")

    label("loc_28AD")


    ChrTalk(
        0xFE,
        "Let's see, Yuri's favorite black tea is...\x02",
    )

    CloseMessageWindow()

    label("loc_28DD")

    Jump("loc_2D05")

    label("loc_28E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28F0")
    Jump("loc_2D05")

    label("loc_28F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28FE")
    Jump("loc_2D05")

    label("loc_28FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C2")

    ChrTalk(
        0xFE,
        (
            "From last night until this morning, I made a\x01",
            "lot of trips through the mountain path...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, so sleepy...\x01",
            "I wish Yuri and Sykes too\x01",
            "helped with the driving.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A3A")

    label("loc_29C2")


    ChrTalk(
        0xFE,
        (
            "Thank goodness Yuri's\x01",
            "mood has improved, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, so sleepy... I gotta\x01",
            "sleep before going for drinks...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3A")

    Jump("loc_2D05")

    label("loc_2A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2A50")
    Call(0, 9)
    Jump("loc_2D05")

    label("loc_2A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C66")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2AC7")

    ChrTalk(
        0xFE,
        (
            "I-I swear! \x01",
            "We won't ever tease\x01",
            "a cat again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that brat comes\x01",
            "again... *shivers*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C61")

    label("loc_2AC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD4")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    ChrTalk(
        0xFE,
        "Uwah! Again...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#4S#04602F...Boo!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eeeek!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#04609FAhahaha, what're you so scared of, hmm?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A3, 500)

    ChrTalk(
        0x102,
        (
            "#00106F(*sigh*... Her innocence is\x01",
            "wicked, in a certain way...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C0A")

    label("loc_2BD4")


    ChrTalk(
        0xFE,
        (
            "C-Cut it out... We won't\x01",
            "ever tease a cat again!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C0A")

    Jump("loc_2C61")

    label("loc_2C0F")


    ChrTalk(
        0xFE,
        "Hehe, what a masterpiece.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it was small and\x01",
            "looked a bit pathetic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C61")

    Jump("loc_2D05")

    label("loc_2C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C74")
    Jump("loc_2D05")

    label("loc_2C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2CFC")

    ChrTalk(
        0xFE,
        (
            "Now then, I gotta\x01",
            "make the side dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I think I'll open an expensive\x01",
            "wine we brought from the Republic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D05")

    label("loc_2CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2D05")

    label("loc_2D05")

    TalkEnd(0xFE)
    Return()

    # Function_10_24F9 end

    def Function_11_2D09(): pass

    label("Function_11_2D09")

    Call(0, 12)
    Return()

    # Function_11_2D09 end

    def Function_12_2D0D(): pass

    label("Function_12_2D0D")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D22")
    Call(0, 6)
    Jump("loc_2D86")

    label("loc_2D22")


    ChrTalk(
        0xB,
        "(It's been awhile since I had good customers☆)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "(Uh uh, I'll have to\x01",
            "earn lots and lots.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D86")

    TalkEnd(0xB)
    SetChrSubChip(0xB, 0x1)
    Return()

    # Function_12_2D0D end

    def Function_13_2D8E(): pass

    label("Function_13_2D8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA3")
    Call(0, 8)
    Jump("loc_2E12")

    label("loc_2DA3")

    OP_4B(0xFE, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Huh? That car\x01",
            "outside's yours!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe, nice, isn't it. \x01",
            "Wanna ride with us next time?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0x9, 0xFF)

    label("loc_2E12")

    TalkEnd(0xFE)
    Return()

    # Function_13_2D8E end

    def Function_14_2E16(): pass

    label("Function_14_2E16")

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
            "#5PMan, what a thrill,\x01",
            "this morning drive was!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PHehe, the rain today's just\x01",
            "perfect for drift racing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, my heart's\x01",
            "still pounding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBy the way Reggie, I wonder\x01",
            "if those girls you called\x01",
            "this morning're coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12POh yeah, any\x01",
            "minute now...\x02",
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

    def lambda_30ED():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_30ED)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)

    ChrTalk(
        0xA,
        "Oh here they're♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHu hu, perfect timing!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_346E")
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Hey── Aren't you those cops from yesterday!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "W-Why the hell are you guys here!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105F...Wait, you're the ones who were\x01",
            "driving like maniacs yesterday?\x02\x03",
            "#00103FWhat exactly is going on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FIs this a robbery or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FIf that's the case, then we caught them red-handed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "D-Don't be stupid...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If we were robbers, would\x01",
            "we just stick around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAnyway, what the hell do\x01",
            "cops like you need from us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou've got some nerve barging\x01",
            "into our house like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FSo this means that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah. Looks like these guys\x01",
            "are the new residents.\x02\x03",
            "#00000FGuys, we're actually today here\x01",
            "on official police business.\x02\x03",
            "We won't take much of your time, but\x01",
            "we do need to ask you a few questions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_368F")

    label("loc_346E")

    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Eh eh, quite the pretty ones, aren't they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yeah, even better than expected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105F...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FWhat are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, thanks for bringing 'em over.\x01",
            "Hang on, I'll get you guys a tip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FOh boy... I bet these guys\x01",
            "think they're the hostesses\x01",
            "they called to their house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...I'll get right to the point.\x02\x03",
            "#00000FWe're with the Crossbell\x01",
            "Police, Special Support\x01",
            "Section.\x02\x03",
            "We won't take much of your time, but\x01",
            "we do need to ask you a few questions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368F")

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
            "#12P#00003FSo you three came to Crossbell\x01",
            "to study the culture here.\x02\x03",
            "And, while looking for a place to stay, \x01",
            "you happened to find this house for\x01",
            "sale and Yuri there bought it...\x02\x03",
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
            "#12P#00105FBy the way── What does\x01",
            "the name "High Bloods"\x01",
            "refer to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHehe, you want to know? That's\x01",
            "the name of our 3-man group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P"Those of Noble Blood"...\x01",
            "It's just perfect for we who\x01",
            "are loved by the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PActually, all of our\x01",
            "fathers are higher ups\x01",
            "at that Verne Corp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PAnd Yuri's father is a board member.\x01",
            "So we're the ones you need to suck up to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHeh, that's exactly right.\x02",
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

    def lambda_3A75():
        OP_95(0xD, 1260, 0, -2000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3A75)
    Sleep(50)

    def lambda_3A92():
        OP_95(0xE, 1260, 0, -3000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3A92)
    Sleep(50)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xD, 1)
    Sound(104, 0, 100, 0)

    def lambda_3AE3():
        OP_93(0xD, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3AE3)
    Sleep(50)
    WaitChrThread(0xE, 1)

    def lambda_3AF7():
        OP_93(0xE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3AF7)
    Sleep(50)

    def lambda_3B07():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3B07)
    Sleep(50)

    def lambda_3B17():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3B17)
    Sleep(50)

    def lambda_3B27():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B27)
    Sleep(50)

    def lambda_3B37():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B37)

    ChrTalk(
        0xA,
        "#5PAh, finally! Sure took you long enough♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5POh, now these are the real deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PUmm... Which\x01",
            "one of you is Mr.\x01",
            ""High Bloods"?\x02",
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
            "#5POh don't worry, we're all\x01",
            "done with these guys.\x02",
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

    def lambda_3C73():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C73)
    Sleep(50)

    def lambda_3C83():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C83)
    Sleep(50)

    def lambda_3C93():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C93)
    Sleep(50)

    def lambda_3CA3():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CA3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah, you don't have\x01",
            "to tell us twice...\x02",
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

    # Function_14_2E16 end

    def Function_15_3D17(): pass

    label("Function_15_3D17")

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
            "#11PHmph... The "Special Support\x01",
            "Section" I think they said.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00003FThanks for your help back them.\x02\x03",
            "#6P#00000FWe want to ask you a little\x01",
            "something. Is it alright?\x02",
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
            "Hehe... \x01",
            "So that's how it is.\x02",
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
            "#12P#00300FWe're wastin' each other's time.\x01",
            "How 'bout answerin' already?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F5")
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
            "◆What about the Runaway Vehicle Crackdown 1? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",         # 0
            "[Cleared]\x01",           # 1
            "[Didn't clear]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E1")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_42F5")

    label("loc_42E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F5")
    OP_29(0x69, 0x3, 0x10)

    label("loc_42F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_43BF")

    ChrTalk(
        0x8,
        "Hehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have you to thank for\x01",
            "that absurd crackdown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want a moderate show\x01",
            "of "good faith" from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "How about getting on your knees or stripping?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4485")

    label("loc_43BF")


    ChrTalk(
        0x8,
        "Hehe, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You've showed a certain lack of\x01",
            "respect during this interview.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I want a moderate show\x01",
            "of "good faith" from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "How about getting on your knees or stripping?\x02",
    )

    CloseMessageWindow()

    label("loc_4485")

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
        "#11PHa ha! That's great!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So there you have it. Which'll\x01",
            "it be, kneeling or stripping?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ah, the guys don't need to strip, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F(T-These guys...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106F(They're worse than we thought...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306F(Oh boy, seems like they're\x01",
            "misunderstanding, somehow.)\x02",
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
        "#12P#00000F(Yeah, leave this to me──)\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1A3,
        (
            "#12P#04605F#3975VHey, hey misters.\x02\x03",
            "#3976VWhy're you taking\x01",
            "this much time?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF88)
    OP_C9(0x1, 0x80000000)

    def lambda_4741():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4741)
    Sleep(50)

    def lambda_4751():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4751)
    Sleep(50)

    def lambda_4761():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4761)
    Sleep(50)

    def lambda_4771():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4771)
    Sleep(50)

    def lambda_4781():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4781)
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

    def lambda_4840():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4840)
    Sleep(50)

    def lambda_4850():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4850)
    Sleep(50)

    def lambda_4860():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4860)
    Sleep(50)

    def lambda_4870():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4870)
    Sleep(50)

    def lambda_4880():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4880)
    Sleep(50)

    def lambda_4890():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4890)
    Sleep(50)

    def lambda_48A0():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_48A0)
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
        "#5PUgh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04609FAll righty then. Time to spit\x01",
            "it out, wouldn't you say?\x02\x03",
            "#04611FOr perhaps you'd like to resist\x01",
            "so I can rip your brains out?\x02",
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

    def lambda_4A5D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4A5D)
    Sleep(50)

    def lambda_4A7A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4A7A)
    WaitChrThread(0x9, 1)

    def lambda_4A98():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4A98)
    WaitChrThread(0xA, 1)

    def lambda_4AA9():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4AA9)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#11PH-Hey! \x01",
            "What're you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PDamn brat! What're\x01",
            "you doing to Yuri──\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1A3,
        (
            "#12P#04611F#3977V──Shut it.\x01",
            "I'll kill this guy, you know.\x02",
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
        "#12P#00101FT-That would be a little...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F*sigh*... Seriously.\x02\x03",
            "#00301F──Guys. \x01",
            "Do as she says.\x02\x03",
            "She's dangerous.\x01",
            "She'll do it for real.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P............\x02",
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
            "#11PA-A cat came here!\x01",
            "Just before you came!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWe teased it a bit and\x01",
            "it left immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PIt's got to be around here somewhere, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P―T-That should be good right? \x01",
            "L-Let Yuri go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04604FOh, you teased a cute kitty, did you?\x02\x03",
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
        "#5PUgh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAaah...!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A3, 0x4)

    ChrTalk(
        0x1A3,
        "#6P#04611FWanna join them?\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xA, 0xB4, 0x1F4, 0x7D0, 0x0)

    ChrTalk(
        0xA,
        "#11P*shiver shiver shiver*...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#6P#04609FAhaha, so you get it then.\x02\x03",
            "#04604FWell then──\x02",
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

    def lambda_4FBA():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4FBA)
    Sleep(50)

    def lambda_4FD2():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4FD2)

    ChrTalk(
        0x8,
        "Bwah...*pant pant*!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...*haah, haah*!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)

    ChrTalk(
        0x1A3,
        (
            "#5P#04600FSo it seems like\x01",
            "Mary's around.\x02\x03",
            "#04609FLet's hurry and look for her㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FR-Right...\x02\x03",
            "#12P#00003FUmm... Thanks for\x01",
            "your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu. By the way, she has no\x01",
            "connection with the police at all.\x02\x03",
            "#10309FI think you just got bitten by a cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PS-Shut up! \x01",
            "Just get out of here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou guys... \x01",
            "...You won't get away with this!\x02",
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

    # Function_15_3D17 end

    def Function_16_51B8(): pass

    label("Function_16_51B8")


    def lambda_51BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_51BD)

    def lambda_51CE():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51CE)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 920, 0, -1940, 2000, 0x0)
    Return()

    # Function_16_51B8 end

    def Function_17_51FC(): pass

    label("Function_17_51FC")


    def lambda_5201():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5201)

    def lambda_5212():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5212)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -100, 0, -3320, 2000, 0x0)
    OP_95(0x102, -100, 0, -1870, 2000, 0x0)
    Return()

    # Function_17_51FC end

    def Function_18_5254(): pass

    label("Function_18_5254")


    def lambda_5259():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5259)

    def lambda_526A():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_526A)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2210, 0, -3320, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_18_5254 end

    def Function_19_529F(): pass

    label("Function_19_529F")


    def lambda_52A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_52A4)

    def lambda_52B5():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_52B5)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 2210, 0, -3320, 2000, 0x0)
    OP_95(0x109, 2210, 0, -1870, 2000, 0x0)
    Return()

    # Function_19_529F end

    def Function_20_52F7(): pass

    label("Function_20_52F7")


    def lambda_52FC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_52FC)

    def lambda_530D():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_530D)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -100, 0, -3320, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_20_52F7 end

    def Function_21_5342(): pass

    label("Function_21_5342")


    def lambda_5347():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_5347)

    def lambda_5358():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_5358)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_21_5342 end

    def Function_22_5372(): pass

    label("Function_22_5372")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53A2")

    def lambda_5382():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5382)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_22_5372")

    label("loc_53A2")

    Return()

    # Function_22_5372 end

    SaveToFile()

Try(main)
