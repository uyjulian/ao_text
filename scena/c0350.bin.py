from ScenarioHelper import *

def main():
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
        "Yuri",                 # 1
        "Sykes",               # 2
        "Reggie",                 # 3
        "hostess",               # 4
        "hostess",               # 5
        "hostess",               # 6
        "hostess",               # 7
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
        "Function_5_150D",         # 05, 5
        "Function_6_16D5",         # 06, 6
        "Function_7_17E7",         # 07, 7
        "Function_8_2061",         # 08, 8
        "Function_9_2112",         # 09, 9
        "Function_10_22D1",        # 0A, 10
        "Function_11_2AD1",        # 0B, 11
        "Function_12_2AD5",        # 0C, 12
        "Function_13_2B4B",        # 0D, 13
        "Function_14_2BEC",        # 0E, 14
        "Function_15_3A0D",        # 0F, 15
        "Function_16_4E17",        # 10, 16
        "Function_17_4E5B",        # 11, 17
        "Function_18_4EB3",        # 12, 18
        "Function_19_4EFE",        # 13, 19
        "Function_20_4F56",        # 14, 20
        "Function_21_4FA1",        # 15, 21
        "Function_22_4FD1",        # 16, 22
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
    Jump("loc_1509")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_810")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DE")
    Call(0, 5)
    Jump("loc_80B")

    label("loc_7DE")


    ChrTalk(
        0xFE,
        (
            "Damn it …\x01",
            "Why are we looking like this …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80B")

    Jump("loc_1509")

    label("loc_810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_995")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_900")

    ChrTalk(
        0xFE,
        (
            "As soon as you leave the crossbell\x01",
            "There was a notice from the republic government … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hun, on a crowded train\x01",
            "I got maddled and got home, etc.\x01",
            "I was completely sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Waiting for the disqualification to be solved,\x01",
            "With the car we procured\x01",
            "I will go back to my country gradually.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_990")

    label("loc_900")


    ChrTalk(
        0xFE,
        (
            "On a crowded train\x01",
            "I got maddled and got home, etc.\x01",
            "I was completely sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Waiting for the disqualification to be solved,\x01",
            "With the car we procured\x01",
            "I will go back to my country gradually.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_990")

    Jump("loc_1509")

    label("loc_995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACC")

    ChrTalk(
        0xFE,
        (
            "In the attack incident during this time,\x01",
            "Quite a lot of damage to the police and guards\x01",
            "It seems like it came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kukuku … It is kind of nice.\x01",
            "The punishment that worked rudely on us\x01",
            "Did not she go down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F(……let's go.\x01",
            "I do not have time to be on these people. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Well, to a fool\x01",
            "It does not matter what you say. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B36")

    label("loc_ACC")


    ChrTalk(
        0xFE,
        (
            "In the attack incident during this time,\x01",
            "Quite a lot of damage to the police and guards\x01",
            "It seems like it came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Kukuku … It is kind of nice.\x02",
    )

    CloseMessageWindow()

    label("loc_B36")

    Jump("loc_1509")

    label("loc_B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C7A")

    ChrTalk(
        0xFE,
        (
            "Hun, penalties are penalties.\x01",
            "I will keep it quiet for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … Go quickly somewhere.\x01",
            "I do not have time to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Kate was angry at Mr.\x01",
            "It seems pretty durable. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F(Ah……\x01",
            "Imitate a fool for a while\x01",
            "There seems to be no worry. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D43")

    label("loc_C7A")


    ChrTalk(
        0xFE,
        "…… For what purpose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To police human beings\x01",
            "I have no leisure.\x01",
            "… … Go out quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(Did something happen……?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(That reminds me, where I always stayed\x01",
            "It seems like there was no power guide car … …)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D43")

    SetScenarioFlags(0x0, 0)
    Jump("loc_D8E")

    label("loc_D4B")


    ChrTalk(
        0xFE,
        (
            "… … Go quickly somewhere.\x01",
            "I do not have time to tell you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8E")

    Jump("loc_1509")

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DA1")
    Jump("loc_1509")

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E0B")

    ChrTalk(
        0xFE,
        (
            "ちっ、Reggieの奴は\x01",
            "Norma other than driving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About a cup of tea\x01",
            "I want you to put it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1509")

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E19")
    Jump("loc_1509")

    label("loc_E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E27")
    Jump("loc_1509")

    label("loc_E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFC")

    ChrTalk(
        0xFE,
        (
            "Today is the entertainment district\x01",
            "In the place like \"Neue-Blanc\"\x01",
            "Do you want to go there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kuku, for the common people like you\x01",
            "I guess it is a store with no connection at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F(Well, it is not quite and it is not so …).\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F3D")

    label("loc_EFC")


    ChrTalk(
        0xFE,
        (
            "…… Even so, it is late.\x01",
            "SykesとReggieは何をやってる……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3D")

    Jump("loc_1509")

    label("loc_F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_117F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EE")

    ChrTalk(
        0xFE,
        "… … for what purpose for such a night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What you did during the day … …\x01",
            "I will not say that I forgot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00605F(you……\x01",
            "Was there something with them? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(No, well\x01",
            "I could not help it ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F(At all … in this subtle period\x01",
            "Do not cause troubles. )\x02\x03",
            "#00600F(Until tomorrow's plenary session ends,\x01",
            "Never mind clearly.\x01",
            "… … nice. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(Ryo, OK.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 3)
    Jump("loc_117A")

    label("loc_10EE")


    ChrTalk(
        0xFE,
        (
            "What you did during the day … …\x01",
            "I will not say that I forgot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will regret it someday.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(I'm sorry I'm sorry … …)\x02",
    )

    CloseMessageWindow()

    label("loc_117A")

    Jump("loc_1509")

    label("loc_117F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1463")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_125C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121A")

    ChrTalk(
        0xFE,
        (
            "What you guys did to me ……\x01",
            "I will not do it for free.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Autonomous state police like\x01",
            "Do not ride the figure … are not you?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1257")

    label("loc_121A")


    ChrTalk(
        0xFE,
        (
            "What you guys did to me ……\x01",
            "I will not do it for free.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1257")

    Jump("loc_145E")

    label("loc_125C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1400")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B9")

    ChrTalk(
        0xFE,
        (
            "……Damn it …\x01",
            "This worked on me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "you……\x01",
            "… … I do not think you can do with free things …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FHaha, weak\x01",
            "It is strengthening to.\x02\x03",
            "#04604FWell, if it comes down\x01",
            "Come at any time.\x02\x03",
            "#04611FOf course, at the preparedness to be killed ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Ku … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F…… Alright, let's go, Charlie.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FB")

    label("loc_13B9")


    ChrTalk(
        0xFE,
        (
            "……Damn it …\x01",
            "This worked on me … …\x01",
            "I will never forgive you …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FB")

    Jump("loc_145E")

    label("loc_1400")


    ChrTalk(
        0xFE,
        (
            "Well, my own way to our castle\x01",
            "I came in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That much punishment\x01",
            "It will be natural given.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145E")

    Jump("loc_1509")

    label("loc_1463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1471")
    Jump("loc_1509")

    label("loc_1471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1500")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1494")
    Call(0, 6)
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_1494")


    ChrTalk(
        0xFE,
        "What are you still there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huh, have you finished your work?\x01",
            "Would you please accept it quickly?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_1500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1509")

    label("loc_1509")

    TalkEnd(0xFE)
    Return()

    # Function_4_7B2 end

    def Function_5_150D(): pass

    label("Function_5_150D")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        "Hey, outside is full of creatures! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Maybe they are,\x01",
            "We're attacking us ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "ど、どうしようYuri！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yes, I am thinking right now, keep silent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Damn it …\x01",
            "Why are we looking like this …?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16BA")

    ChrTalk(
        0x101,
        (
            "#00005F(\"Hybrads\" ……\x01",
            "Have you been in Crossbell yet? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(The timing to return to the Republic\x01",
            "You seem to have missed it. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Well, beyond being at home\x01",
            "It's okay to leave it alone. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BA")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_5_150D end

    def Function_6_16D5(): pass

    label("Function_6_16D5")


    ChrTalk(
        0xB,
        (
            "Even so, everyone is young\x01",
            "On such a large mansion\x01",
            "It is amazing to live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Huh, there's nothing serious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Compared to parents in the Republic\x01",
            "It looks like a kennel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F(Yes, kennels … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Ha ha, really\x01",
            "I wish I was in a good mood. )\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_16D5 end

    def Function_7_17E7(): pass

    label("Function_7_17E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_17F8")
    Jump("loc_205D")

    label("loc_17F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1813")
    Call(0, 5)
    Jump("loc_1872")

    label("loc_1813")


    ChrTalk(
        0xFE,
        "Oh no, what's going on! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When we are attacked,\x01",
            "Who is responsible! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1872")

    Jump("loc_205D")

    label("loc_1877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1910")

    ChrTalk(
        0xFE,
        (
            "Independence declaration hey.\x01",
            "By the way, what?\x01",
            "It seems that I was making a noise from before ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ま、Yuriが大丈夫って言ってるし\x01",
            "Perhaps it will be okay though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205D")

    label("loc_1910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D5")

    ChrTalk(
        0xFE,
        (
            "Ahh, recently\x01",
            "Atmosphere that inside of town got bored\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, here we go\x01",
            "Even on a drive ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haa, but …\x01",
            "I did not have a car ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A50")

    label("loc_19D5")


    ChrTalk(
        0xFE,
        (
            "Ha\x01",
            "The car broke down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even in a drive for distraction\x01",
            "I wanted to go ……\x01",
            "Do you only have to go for gaming?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A50")

    Jump("loc_205D")

    label("loc_1A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1ABE")

    ChrTalk(
        0xFE,
        (
            "Oh, that guided car\x01",
            "The ride was the best ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm afraid I will be bored for a while … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_205D")

    label("loc_1ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1ACC")
    Jump("loc_205D")

    label("loc_1ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B33")

    ChrTalk(
        0xFE,
        (
            "Hehe he is using it recently\x01",
            "Drive course is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a little better than the city.\x02",
    )

    CloseMessageWindow()
    Jump("loc_205D")

    label("loc_1B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B41")
    Jump("loc_205D")

    label("loc_1B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B4F")
    Jump("loc_205D")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0B")

    ChrTalk(
        0xFE,
        (
            "Yuriのやつ、昨晩の夜のドライブで\x01",
            "It seems like I'm completely in a good mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, it's going to have extraordinary hands.\x01",
            "…… I absolutely will not say it before himself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    TalkEnd(0xFE)
    SetChrFlags(0xFE, 0x10)
    Return()

    label("loc_1C0B")


    ChrTalk(
        0xFE,
        (
            "Now, on \"Neue-Blanc\"\x01",
            "Be prepared to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……どした、Reggie。\x01",
            "Somewhat sleepy though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205D")

    label("loc_1C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1C89")
    Call(0, 9)
    Jump("loc_205D")

    label("loc_1C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FD1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D24")

    ChrTalk(
        0xFE,
        "Hit …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… That redhead brat is\x01",
            "Is not there anymore ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … Ha, Han!\x01",
            "Do not get on tone! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D7A")

    label("loc_1D24")


    ChrTalk(
        0xFE,
        "I'm bibbitly from something else … Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……ちょ、Do not get on tone! Is it?\x02",
    )

    CloseMessageWindow()

    label("loc_1D7A")

    Jump("loc_1FCC")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE9")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    ChrTalk(
        0xFE,
        "Him … have you come again! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, do not go any further! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04606FHmm, Shirley is already\x01",
            "I am not interested in your older brothers.\x02\x03",
            "#04609FHey, let's go looking for Mary soon ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FOh, oh … That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FThe murder of the moment ago\x01",
            "Innocent like a lie.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F3C")

    label("loc_1EE9")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, do not go any further! It is!\x01",
            "Go out! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3C")

    Jump("loc_1FCC")

    label("loc_1F41")


    ChrTalk(
        0xFE,
        (
            "Have you seen it before?\x01",
            "It was a bit of a threat\x01",
            "I flew away and ran away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Weak people bullying\x01",
            "I wonder why it is so much fun ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCC")

    Jump("loc_205D")

    label("loc_1FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FDF")
    Jump("loc_205D")

    label("loc_1FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2054")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFA")
    Call(0, 8)
    Jump("loc_204F")

    label("loc_1FFA")


    ChrTalk(
        0xFE,
        (
            "…… What are you guys,\x01",
            "Do you want me to join your company?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Kuku, there your fingers too.\x02",
    )

    CloseMessageWindow()

    label("loc_204F")

    Jump("loc_205D")

    label("loc_2054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_205D")

    label("loc_205D")

    TalkEnd(0xFE)
    Return()

    # Function_7_17E7 end

    def Function_8_2061(): pass

    label("Function_8_2061")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        "Sit, sit and sit there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I have a nice wine,\x01",
            "Let 's have a sister together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Uhufu, then\x01",
            "Let's consider it.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_8_2061 end

    def Function_9_2112(): pass

    label("Function_9_2112")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225F")

    ChrTalk(
        0x9,
        (
            "Yuriのやつ、\x01",
            "It is truly a bad mood … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To try refreshing in the entertainment district,\x01",
            "With VIP security and so on\x01",
            "It seems that policemen are pretty good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well then, then …\x01",
            "On the mountain road with a car\x01",
            "How about a night drive?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Passengers also\x01",
            "It will be few, and to my utmost\x01",
            "It seems to be burning me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, it's a pretty good idea.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22C8")

    label("loc_225F")


    ChrTalk(
        0x9,
        (
            "Okay, if you decide so\x01",
            "Yuriに提案してみるか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Reggie、お前車の準備しとけよ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "OK.\x02",
    )

    CloseMessageWindow()

    label("loc_22C8")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_2112 end

    def Function_10_22D1(): pass

    label("Function_10_22D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22E2")
    Jump("loc_2ACD")

    label("loc_22E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2350")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FD")
    Call(0, 5)
    Jump("loc_234B")

    label("loc_22FD")


    ChrTalk(
        0xFE,
        (
            "After all, when declaring independence,\x01",
            "To the Republic even if impossible\x01",
            "I suppose I should have returned home …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_234B")

    Jump("loc_2ACD")

    label("loc_2350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23EB")

    ChrTalk(
        0xFE,
        (
            "Yuriは余裕を見せてるけど……\x01",
            "……, is it okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you miss this timing,\x01",
            "To poor country, to the Republic\x01",
            "You will not be able to return home ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACD")

    label("loc_23EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2490")

    ChrTalk(
        0xFE,
        (
            "（Yuriはあんな事言ってるけど……\x01",
            "It is truly a hide. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(From us\x01",
            "Because I say casually,\x01",
            "Do not mind me so much. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACD")

    label("loc_2490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_25DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2546")

    ChrTalk(
        0xFE,
        (
            "…… Hekushon! It is!\x01",
            "I guess I caught a cold … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed yesterday,\x01",
            "I wonder if I fell into the pond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Ha, is it self-suicide?\x01",
            "Do not do it …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_25DA")

    label("loc_2546")


    ChrTalk(
        0xFE,
        (
            "Snob.\x01",
            "Go to Ursula Hospital\x01",
            "I wonder if I get medicine ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow in Mainz\x01",
            "It seems that there was a serious thing,\x01",
            "I wonder if I go out like a bus or something ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DA")

    Jump("loc_2ACD")

    label("loc_25DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25ED")
    Jump("loc_2ACD")

    label("loc_25ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_26AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267E")

    ChrTalk(
        0xFE,
        (
            "That, somehow,\x01",
            "It sounds like you heard the sound of a siren …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……whatever.\x01",
            "えーっと、Yuriの好きな紅茶は……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26A6")

    label("loc_267E")


    ChrTalk(
        0xFE,
        "えーっと、Yuriの好きな紅茶は……\x02",
    )

    CloseMessageWindow()

    label("loc_26A6")

    Jump("loc_2ACD")

    label("loc_26AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_26B9")
    Jump("loc_2ACD")

    label("loc_26B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_26C7")
    Jump("loc_2ACD")

    label("loc_26C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2765")

    ChrTalk(
        0xFE,
        (
            "From last night until this morning,\x01",
            "I was letting you back and forth on the mountain road ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "F aa, sleepy …\x01",
            "YuriもSykesも、\x01",
            "I want you to become a person who drives.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27CB")

    label("loc_2765")


    ChrTalk(
        0xFE,
        (
            "Yuriの機嫌が直ったのは\x01",
            "Although it was good …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "F aa, sleepy …\x01",
            "Let me sleep before going out for drinks ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CB")

    Jump("loc_2ACD")

    label("loc_27D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_27E1")
    Call(0, 9)
    Jump("loc_2ACD")

    label("loc_27E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A2C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2872")

    ChrTalk(
        0xFE,
        (
            "Even now,\x01",
            "I do not bully cats ……\x01",
            "I have to abide by that absolutely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that girl comes again ……\x01",
            "…… Burbo.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A27")

    label("loc_2872")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2988")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    ChrTalk(
        0xFE,
        "Wow, again …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#4S#04602F… Wow! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huge! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#04609FHaha, what is it, Bibbit?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A3, 500)

    ChrTalk(
        0x102,
        (
            "#00106F(Fu … … this innocence is\x01",
            "In a way it is a bad guy ….)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29CD")

    label("loc_2988")


    ChrTalk(
        0xFE,
        (
            "Do not give up already ……\x01",
            "I do not want to catch any more cats anymore! Is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CD")

    Jump("loc_2A27")

    label("loc_29D2")


    ChrTalk(
        0xFE,
        "It was a hard work, it was a masterpiece.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it was a little\x01",
            "It's a little poor though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A27")

    Jump("loc_2ACD")

    label("loc_2A2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A3A")
    Jump("loc_2ACD")

    label("loc_2A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2AC4")

    ChrTalk(
        0xFE,
        (
            "Let me see .. cha\x01",
            "I wonder if I make something like a knob.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, I brought it from the Republic\x01",
            "Will you also open up high-end wine?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACD")

    label("loc_2AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2ACD")

    label("loc_2ACD")

    TalkEnd(0xFE)
    Return()

    # Function_10_22D1 end

    def Function_11_2AD1(): pass

    label("Function_11_2AD1")

    Call(0, 12)
    Return()

    # Function_11_2AD1 end

    def Function_12_2AD5(): pass

    label("Function_12_2AD5")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AEA")
    Call(0, 6)
    Jump("loc_2B43")

    label("loc_2AEA")


    ChrTalk(
        0xB,
        "(It 's been a while since I was a long time no ☆)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "(Huff, Jean Jean\x01",
            "I gotta get it earned. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B43")

    TalkEnd(0xB)
    SetChrSubChip(0xB, 0x1)
    Return()

    # Function_12_2AD5 end

    def Function_13_2B4B(): pass

    label("Function_13_2B4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B60")
    Call(0, 8)
    Jump("loc_2BE8")

    label("loc_2B60")

    OP_4B(0xFE, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Well then, it was outside.\x01",
            "That car is also yours! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wow, great!\x01",
            "Would you like me to take it this time?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0x9, 0xFF)

    label("loc_2BE8")

    TalkEnd(0xFE)
    Return()

    # Function_13_2B4B end

    def Function_14_2BEC(): pass

    label("Function_14_2BEC")

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
            "#5PWell, but this morning's drive\x01",
            "It was awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PHello. Take advantage of rain today.\x01",
            "I decided to drift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, indeed\x01",
            "It was quite a thrill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5Pそれより、Reggie。\x01",
            "The older sister who asked me this morning\x01",
            "I wonder if it will come properly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12POh, wait a moment.\x01",
            "Maybe about -\x02",
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

    def lambda_2EDE():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2EDE)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)

    ChrTalk(
        0xA,
        "O, came came ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHuh, it's a good timing.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_31CA")
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "What are you guys yesterday! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Why are you in such a place …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105F…… It is a three-person group of yesterday's runaway vehicle.\x02\x03",
            "#00103FWhat on earth is it like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FMaybe it is a thief?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FIf so, you are arresting the current crime.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Bahahahaha … say!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If it was a thief\x01",
            "At last it's Tonslowa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POr rather,\x01",
            "What on earth are you visiting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn our house, without permission\x01",
            "It is good grade to get up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FThat means … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FOh, apparently they\x01",
            "It seems like a new inhabitant of this house.\x02\x03",
            "#00000FI wish you guys came here today\x01",
            "It is for the work of the police who is not even other.\x02\x03",
            "I will not have time\x01",
            "I will get involved in listening to circumstances.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B9")

    label("loc_31CA")

    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        "Hello, it's pretty cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "All right, this guy is more than I expected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105F… Well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, people who pick up and transfer are also having trouble.\x01",
            "I will tip and come get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FWhew … apparently\x01",
            "自宅に呼んだhostessか何かと\x01",
            "You seem to misunderstand me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F…… Let's go straight to this place.\x02\x03",
            "#00000FI am sorry,\x01",
            "They are cross-police\x01",
            "It is a person who is a mercantile support department.\x02\x03",
            "I will not have time\x01",
            "I will get involved in listening to circumstances.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B9")

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
            "#12P#00003FIn other words, you three\x01",
            "The purpose of entering the crossbell is social study …\x02\x03",
            "If you are looking for a place to stay, by chance\x01",
            "I found this house which was put out for sale\x01",
            "そちらのYuri君が購入した……\x02\x03",
            "#00001F…… That kind of situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh, did you understand?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FBy the way -\x01",
            "The name \"Hybrads\" is\x01",
            "What on earth are you talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHello, would you like to ask?\x01",
            "That guy is the team name of three of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P\"Noble blood\" -\x01",
            "To the gods loved by the goddess\x01",
            "Perfect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PWell, actually it's ours\x01",
            "All my fathers are that Vernue company\x01",
            "He is a great man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P中でもYuriの親父さんは取締役――\x01",
            "If you sell cobbies, why inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHuhun, that's it.\x02",
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

    def lambda_377A():
        OP_95(0xD, 1260, 0, -2000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_377A)
    Sleep(50)

    def lambda_3797():
        OP_95(0xE, 1260, 0, -3000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3797)
    Sleep(50)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xD, 1)
    Sound(104, 0, 100, 0)

    def lambda_37E8():
        OP_93(0xD, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_37E8)
    Sleep(50)
    WaitChrThread(0xE, 1)

    def lambda_37FC():
        OP_93(0xE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_37FC)
    Sleep(50)

    def lambda_380C():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_380C)
    Sleep(50)

    def lambda_381C():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_381C)
    Sleep(50)

    def lambda_382C():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_382C)
    Sleep(50)

    def lambda_383C():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_383C)

    ChrTalk(
        0xA,
        "#5POh, I've been waiting ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PHa, this time it's real genuine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PEr …\x01",
            "\"Hybrads\" is\x01",
            "I wonder which way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PLike what?\x01",
            "It seems to be loading … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POh, older sisters.\x01",
            "It's okay as it's over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThat's why you,\x01",
            "I wish to take over immediately.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_396C():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_396C)
    Sleep(50)

    def lambda_397C():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_397C)
    Sleep(50)

    def lambda_398C():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_398C)
    Sleep(50)

    def lambda_399C():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_399C)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00003FOh, even if not told\x01",
            "I intend to do so.\x02",
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

    # Function_14_2BEC end

    def Function_15_3A0D(): pass

    label("Function_15_3A0D")

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
        "Oops … What is it?\x02",
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
            "Well,\x01",
            "I guess it was the last visit! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHun …\x01",
            "Did you say \"Special Affairs Support Division\"?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00003FThanks for that section.\x02\x03",
            "#6P#00000FTalk a little\x01",
            "I'd like to ask, is it OK?\x02",
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
        "Oh, cat … hey …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Powered by Translate\x01",
            "Is that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FThere is something in mind, does not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FWhat also takes time with each other,\x01",
            "Can you tell me the end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hey, what should I do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yuri、どうするよ？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FB9")
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
            "◆ Crackdown Runaway Control 1? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",            # 0
            "【I am clearing】\x01",        # 1
            "【Not clear】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FA5")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_3FB9")

    label("loc_3FA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB9")
    OP_29(0x69, 0x3, 0x10)

    label("loc_3FB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_406C")

    ChrTalk(
        0x8,
        "Huhun, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In an example of joking regulation\x01",
            "It's been taken care of … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A reasonable \"sincerity\"\x01",
            "I want you to show me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Dogasha or nakedo dance.\x02",
    )

    CloseMessageWindow()
    Jump("loc_410A")

    label("loc_406C")


    ChrTalk(
        0x8,
        "Huhun, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With lots of licking attitude\x01",
            "I've listened to it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A reasonable \"sincerity\"\x01",
            "I want you to show me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Dogasha or nakedo dance.\x02",
    )

    CloseMessageWindow()

    label("loc_410A")

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
        "#11PHa ha, that's good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That 's why -\x01",
            "Decided on Dogashite or naked dancing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, I do not need nakedness of a dude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101F(These people … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00106F(It's the lowest I thought … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306F(Okay, something misunderstood\x01",
            "You seem to be doing it. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F(Chick ……\x01",
            "I do not want to threaten anything. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000F(Oh, leave it to me here ---)\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1A3,
        (
            "#12P#04605F#3975VHey, older brothers.\x02\x03",
            "#3976VWhy is this\x01",
            "Is he getting into trouble?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF88)
    OP_C9(0x1, 0x80000000)

    def lambda_43B7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43B7)
    Sleep(50)

    def lambda_43C7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43C7)
    Sleep(50)

    def lambda_43D7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43D7)
    Sleep(50)

    def lambda_43E7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43E7)
    Sleep(50)

    def lambda_43F7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43F7)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005FWhat……\x02",
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

    def lambda_44B5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44B5)
    Sleep(50)

    def lambda_44C5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44C5)
    Sleep(50)

    def lambda_44D5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_44D5)
    Sleep(50)

    def lambda_44E5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_44E5)
    Sleep(50)

    def lambda_44F5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_44F5)
    Sleep(50)

    def lambda_4505():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4505)
    Sleep(50)

    def lambda_4515():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4515)
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
        "#5PUg ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04609FYes it is.\x01",
            "Let's vomit quickly.\x02\x03",
            "#04611FOr resist it\x01",
            "Whole heart in the stomach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PUg … it is …\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_46B0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_46B0)
    Sleep(50)

    def lambda_46CD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_46CD)
    WaitChrThread(0x9, 1)

    def lambda_46EB():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_46EB)
    WaitChrThread(0xA, 1)

    def lambda_46FC():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_46FC)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#11PHey, hey!\x01",
            "Suddenly what … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PThis brat!\x01",
            "Yuriに何をしやが──\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x1A3,
        (
            "#12P#04611F#3977V── It's useless.\x01",
            "I'll kill him.\x02",
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
        "#5PI mean …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FWait a moment!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FSure, that is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FWhew … … well.\x02\x03",
            "#00301F── you guys.\x01",
            "Do as I say it.\x02\x03",
            "That is a jerk.\x01",
            "I will do it without hesitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5PWell …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PI know … … because I say!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PRight, if it is a cat, I came!\x01",
            "It is a while before you come!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POr if you threaten lightly\x01",
            "I jumped out quickly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PSo, are you still nearby?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P- Here, this is OK! Is it?\x01",
            "ユ、Yuriを放してやってくれ！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04604FOh, I threatened the cute kitten.\x02\x03",
            "#04609FIs it like this?\x02",
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
        "#5PUughu … …!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5POh no!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A3, 0x4)

    ChrTalk(
        0x1A3,
        "#6P#04611FDoes your older brother want to be like this too?\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xA, 0xB4, 0x1F4, 0x7D0, 0x0)

    ChrTalk(
        0xA,
        "#11PBuzz blinking …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#6P#04609FHaha, I know well.\x02\x03",
            "#04604FWell then\x02",
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

    def lambda_4C2E():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4C2E)
    Sleep(50)

    def lambda_4C46():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C46)

    ChrTalk(
        0x8,
        "Puff … … Ha, ha!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "… …. Ze, Ze!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)

    ChrTalk(
        0x1A3,
        (
            "#5P#04600FApparently Mary\x01",
            "It seems to be nearby?\x02\x03",
            "#04609FLet's hurry to go search\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FOh, ah ……\x02\x03",
            "#12P#00003FEr …\x01",
            "We appreciate your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, by the way she is\x01",
            "Because I have nothing to do with the police.\x02\x03",
            "#10309FI think that it was bitten by a cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PU, noisy …!\x01",
            "Let's finally be going …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5Pyou……\x01",
            "…… I do not think you can do with free things ……\x02",
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

    # Function_15_3A0D end

    def Function_16_4E17(): pass

    label("Function_16_4E17")


    def lambda_4E1C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E1C)

    def lambda_4E2D():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E2D)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 920, 0, -1940, 2000, 0x0)
    Return()

    # Function_16_4E17 end

    def Function_17_4E5B(): pass

    label("Function_17_4E5B")


    def lambda_4E60():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E60)

    def lambda_4E71():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E71)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -100, 0, -3320, 2000, 0x0)
    OP_95(0x102, -100, 0, -1870, 2000, 0x0)
    Return()

    # Function_17_4E5B end

    def Function_18_4EB3(): pass

    label("Function_18_4EB3")


    def lambda_4EB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4EB8)

    def lambda_4EC9():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4EC9)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2210, 0, -3320, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_18_4EB3 end

    def Function_19_4EFE(): pass

    label("Function_19_4EFE")


    def lambda_4F03():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4F03)

    def lambda_4F14():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4F14)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 2210, 0, -3320, 2000, 0x0)
    OP_95(0x109, 2210, 0, -1870, 2000, 0x0)
    Return()

    # Function_19_4EFE end

    def Function_20_4F56(): pass

    label("Function_20_4F56")


    def lambda_4F5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4F5B)

    def lambda_4F6C():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F6C)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -100, 0, -3320, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_20_4F56 end

    def Function_21_4FA1(): pass

    label("Function_21_4FA1")


    def lambda_4FA6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_4FA6)

    def lambda_4FB7():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_4FB7)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_21_4FA1 end

    def Function_22_4FD1(): pass

    label("Function_22_4FD1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5001")

    def lambda_4FE1():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4FE1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_22_4FD1")

    label("loc_5001")

    Return()

    # Function_22_4FD1 end

    SaveToFile()

Try(main)
