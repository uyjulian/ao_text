from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1380.bin",                # FileName
        "t1380",                    # MapName
        "t1380",                    # Location
        0x00BA,                     # MapIndex
        "ed7304",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 186, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1380",                  # 0
        "Elie",                   # 1
        "Tio",                    # 2
        "Noｱl",                  # 3
        "Wazy",                   # 4
        "Fran",                   # 5
        "Rixia",                  # 6
        "Michey",                 # 7
        "Apprentice",             # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Tourist",                # 11
        "Tourist",                # 12
        "Tourist",                # 13
        "Dummy",                  # 14
        "Fortune Teller",         # 15
        "Zeit",                   # 16
        "Miichie",                # 17
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch02900.itc",                   # 02
        "chr/ch03000.itc",                   # 03
        "chr/ch08500.itc",                   # 04
        "chr/ch05200.itc",                   # 05
        "chr/ch10200.itc",                   # 06
        "chr/ch20500.itc",                   # 07
        "chr/ch22802.itc",                   # 08
        "chr/ch22102.itc",                   # 09
        "chr/ch21102.itc",                   # 0A
        "chr/ch24502.itc",                   # 0B
        "chr/ch34302.itc",                   # 0C
        "chr/ch45400.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(4294966337, 0,       4294964197, 0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294965747, 0,       4294964796, 45,   389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294966796, 0,       4294967046, 90,   389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1500,    0,       4294964947, 90,   389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(500,     0,       4294967046, 270,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       4294967046, 0,    389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1700,    0,       5940,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       6500,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4800,    100,     4400,    270,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4800,    100,     3599,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294962496, 100,     4000,    90,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294962496, 100,     4294966796, 90,   389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294962496, 100,     4294965796, 90,   389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294960796, 0,       2609,    180,  389,  0x0, 0,   13,  0,   0,   0,   255, 255, 255,  0)

    DeclEvent(0x0040, 0, 38,  0.0,                   8.0,                   -1.0,                  4.0,                   [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -2.0,                  0.25,                  1.0])

    DeclActor(4294962246, 0,       2700,    1000,    4294960796, 1500,    2610,    0x007E, 0,  36, 0x0000)
    DeclActor(4294965426, 0,       5380,    1200,    4294965426, 1500,    5380,    0x007C, 0,  37, 0x0000)

    ChipFrameInfo(1068, 0)                                       # 0

    ScpFunction((
        "Function_0_42C",          # 00, 0
        "Function_1_4E4",          # 01, 1
        "Function_2_561",          # 02, 2
        "Function_3_58B",          # 03, 3
        "Function_4_706",          # 04, 4
        "Function_5_8FC",          # 05, 5
        "Function_6_9A3",          # 06, 6
        "Function_7_B17",          # 07, 7
        "Function_8_BCE",          # 08, 8
        "Function_9_D3A",          # 09, 9
        "Function_10_E29",         # 0A, 10
        "Function_11_F28",         # 0B, 11
        "Function_12_1083",        # 0C, 12
        "Function_13_1163",        # 0D, 13
        "Function_14_12FB",        # 0E, 14
        "Function_15_1353",        # 0F, 15
        "Function_16_13BD",        # 10, 16
        "Function_17_1458",        # 11, 17
        "Function_18_160C",        # 12, 18
        "Function_19_1F8A",        # 13, 19
        "Function_20_2E55",        # 14, 20
        "Function_21_2F09",        # 15, 21
        "Function_22_3DCC",        # 16, 22
        "Function_23_3E11",        # 17, 23
        "Function_24_3E5B",        # 18, 24
        "Function_25_3E6B",        # 19, 25
        "Function_26_4F48",        # 1A, 26
        "Function_27_5F1E",        # 1B, 27
        "Function_28_6FAA",        # 1C, 28
        "Function_29_7EB5",        # 1D, 29
        "Function_30_8A76",        # 1E, 30
        "Function_31_9973",        # 1F, 31
        "Function_32_A6EA",        # 20, 32
        "Function_33_B56F",        # 21, 33
        "Function_34_C540",        # 22, 34
        "Function_35_D424",        # 23, 35
        "Function_36_E43D",        # 24, 36
        "Function_37_ECF7",        # 25, 37
        "Function_38_ED7F",        # 26, 38
    ))


    def Function_0_42C(): pass

    label("Function_0_42C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_46C"),
        (1, "loc_478"),
        (2, "loc_484"),
        (3, "loc_490"),
        (4, "loc_49C"),
        (5, "loc_4A8"),
        (6, "loc_4B4"),
        (SWITCH_DEFAULT, "loc_4C0"),
    )


    label("loc_46C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_478")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_484")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_490")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_49C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4E3")

    Return()

    # Function_0_42C end

    def Function_1_4E4(): pass

    label("Function_1_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_4F2")
    Jump("loc_560")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_500")
    Jump("loc_560")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_50E")
    Jump("loc_560")

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_51F")
    Call(0, 17)
    Jump("loc_560")

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_52D")
    Jump("loc_560")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_53B")
    Jump("loc_560")

    label("loc_53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_549")
    Jump("loc_560")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_557")
    Jump("loc_560")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_560")

    label("loc_560")

    Return()

    # Function_1_4E4 end

    def Function_2_561(): pass

    label("Function_2_561")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A")
    OP_66(0x0, 0x1)

    label("loc_58A")

    Return()

    # Function_2_561 end

    def Function_3_58B(): pass

    label("Function_3_58B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A4")
    Jump("loc_702")

    label("loc_5A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA")
    Jump("loc_702")

    label("loc_5BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D0")
    Jump("loc_702")

    label("loc_5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E6")
    Jump("loc_702")

    label("loc_5E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_686")

    ChrTalk(
        0x8,
        (
            "#00100FHmm, I wonder where I\x01",
            "should spend my last\x01",
            "ticket.\x02\x03",
            "#00104FIf possible, I'd like it\x01",
            "to be something\x01",
            "memorable...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_702")

    label("loc_686")


    ChrTalk(
        0x8,
        (
            "#00100FIf possible, I'd like to\x01",
            "use my last ticket on\x01",
            "something memorable...\x02\x03",
            "#00104FHmm, I wonder what I\x01",
            "should pick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_702")

    TalkEnd(0xFE)
    Return()

    # Function_3_58B end

    def Function_4_706(): pass

    label("Function_4_706")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71F")
    Jump("loc_8F8")

    label("loc_71F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_735")
    Jump("loc_8F8")

    label("loc_735")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83E")

    ChrTalk(
        0x9,
        (
            "#00200FI've been following Mishy for a\x01",
            "while now...\x02\x03",
            "He actually goes all around the\x01",
            "park, not just to the main\x01",
            "attractions.\x02\x03",
            "#00204FIt means he's doing his best to\x01",
            "meet as many visitors as possible.\x01",
            "...That's Mishy for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8CC")

    label("loc_83E")


    ChrTalk(
        0x9,
        (
            "#00200FEven so, I haven't\x01",
            "spotted Mishy's little\x01",
            "sister "Mishette", yet.\x02\x03",
            "#00204FCould it be that she\x01",
            "shows up only at certain\x01",
            "hours...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CC")

    Jump("loc_8F8")

    label("loc_8D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E7")
    Jump("loc_8F8")

    label("loc_8E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F8")

    label("loc_8F8")

    TalkEnd(0xFE)
    Return()

    # Function_4_706 end

    def Function_5_8FC(): pass

    label("Function_5_8FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_922")
    Call(0, 16)
    Jump("loc_947")

    label("loc_922")


    ChrTalk(
        0xA,
        "#10106FT-That's enough, Fran...\x02",
    )

    CloseMessageWindow()

    label("loc_947")

    Jump("loc_99F")

    label("loc_94C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_962")
    Jump("loc_99F")

    label("loc_962")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_978")
    Jump("loc_99F")

    label("loc_978")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98E")
    Jump("loc_99F")

    label("loc_98E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99F")

    label("loc_99F")

    TalkEnd(0xFE)
    Return()

    # Function_5_8FC end

    def Function_6_9A3(): pass

    label("Function_6_9A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BC")
    Jump("loc_B13")

    label("loc_9BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D2")
    Jump("loc_B13")

    label("loc_9D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E8")
    Jump("loc_B13")

    label("loc_9E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB3")

    ChrTalk(
        0xB,
        (
            "#10300FHehe, this place's sofas\x01",
            "are great.\x02\x03",
            "#10304FI think I'll rest here\x01",
            "until I decide where to\x01",
            "go next.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FWhoa, hey now...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_AFD")

    label("loc_AB3")


    ChrTalk(
        0xB,
        (
            "#10304FHehe, I think I'll rest\x01",
            "here until I decide\x01",
            "where to go next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AFD")

    Jump("loc_B13")

    label("loc_B02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B13")

    label("loc_B13")

    TalkEnd(0xFE)
    Return()

    # Function_6_9A3 end

    def Function_7_B17(): pass

    label("Function_7_B17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3D")
    Call(0, 16)
    Jump("loc_B72")

    label("loc_B3D")


    ChrTalk(
        0xC,
        (
            "#06409FI'll have Noｱl's love\x01",
            "fortune divined～!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B72")

    Jump("loc_BCA")

    label("loc_B77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8D")
    Jump("loc_BCA")

    label("loc_B8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA3")
    Jump("loc_BCA")

    label("loc_BA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB9")
    Jump("loc_BCA")

    label("loc_BB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCA")

    label("loc_BCA")

    TalkEnd(0xFE)
    Return()

    # Function_7_B17 end

    def Function_8_BCE(): pass

    label("Function_8_BCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE7")
    Jump("loc_D36")

    label("loc_BE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C78")

    ChrTalk(
        0xD,
        (
            "#01805F(A fortune teller of\x01",
            "Eastern origin...)\x02\x03",
            "#01803F(It's not that I don't\x01",
            "have an idea, but...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xD, 0x10)
    Jump("loc_CF4")

    label("loc_C78")


    ChrTalk(
        0xD,
        (
            "#01805FAh, Lloyd. H-How long\x01",
            "have you been there?\x02\x03",
            "#01809FAhaha... I was once\x01",
            "again impressed by how\x01",
            "long the line is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF4")

    Jump("loc_D36")

    label("loc_CF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0F")
    Jump("loc_D36")

    label("loc_D0F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D25")
    Jump("loc_D36")

    label("loc_D25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D36")

    label("loc_D36")

    TalkEnd(0xFE)
    Return()

    # Function_8_BCE end

    def Function_9_D3A(): pass

    label("Function_9_D3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D53")
    Jump("loc_E25")

    label("loc_D53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D69")
    Jump("loc_E25")

    label("loc_D69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFE")

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "The fortune teller here\x01",
            "is incredibly capable.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "Mishishi, you can have\x01",
            "all kinds of things\x01",
            "divined, you know?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E14")
    Jump("loc_E25")

    label("loc_E14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E25")

    label("loc_E25")

    TalkEnd(0xFE)
    Return()

    # Function_9_D3A end

    def Function_10_E29(): pass

    label("Function_10_E29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F24")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Welcome to the Fortune\x01",
            "House.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Here, you can have\x01",
            "anything read by our\x01",
            "master fortune teller!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I'm playing hide-and-seek with\x01",
            "Mishette... I'll refrain from\x01",
            "visiting the attractions for now.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F27")

    label("loc_F24")

    Call(0, 18)

    label("loc_F27")

    Return()

    # Function_10_E29 end

    def Function_11_F28(): pass

    label("Function_11_F28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FDB")

    ChrTalk(
        0x10,
        (
            "Looking around, there's\x01",
            "a whole lot of female\x01",
            "visitors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "I'm glad I came with my\x01",
            "girlfriend... If I were alone,\x01",
            "I'd probably be uncomfortable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_107F")

    label("loc_FDB")


    ChrTalk(
        0x10,
        (
            "The compatibility reading had a\x01",
            "good result and my girlfriend's\x01",
            "mood improved a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If the result had been\x01",
            "strange... It would've\x01",
            "probably been awkward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107F")

    TalkEnd(0xFE)
    Return()

    # Function_11_F28 end

    def Function_12_1083(): pass

    label("Function_12_1083")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E4")

    ChrTalk(
        0x11,
        (
            "Uhuhu, what should I have\x01",
            "divined? As expected, our\x01",
            "compatibility?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_115F")

    label("loc_10E4")


    ChrTalk(
        0x11,
        (
            "When I had it divined,\x01",
            "she said we're bound by\x01",
            "a thread of fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Uhuhuhu... My eyes\x01",
            "weren't wrong to choose\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115F")

    TalkEnd(0xFE)
    Return()

    # Function_12_1083 end

    def Function_13_1163(): pass

    label("Function_13_1163")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11FC")

    ChrTalk(
        0x12,
        (
            "I came to have the place I\x01",
            "lost my wedding ring divined\x01",
            "without telling my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "I wonder when it'll be\x01",
            "my turn...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F7")

    label("loc_11FC")


    ChrTalk(
        0x12,
        (
            "Thinking I had dropped my wedding ring, I had\x01",
            "her divine its location, but... Goodness! To\x01",
            "think it was in my pocket the whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            ""It is hard to see what is under your\x01",
            "nose", huh? I'm glad I found it, but\x01",
            "I feel pathetic for some reason.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F7")

    TalkEnd(0xFE)
    Return()

    # Function_13_1163 end

    def Function_14_12FB(): pass

    label("Function_14_12FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134F")

    ChrTalk(
        0x13,
        (
            "I hope I receive a hint\x01",
            "about an amazing\x01",
            "encounter...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_134F")

    label("loc_134F")

    TalkEnd(0xFE)
    Return()

    # Function_14_12FB end

    def Function_15_1353(): pass

    label("Function_15_1353")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B9")

    ChrTalk(
        0x14,
        (
            "I couldn't care less\x01",
            "about men. I'll have her\x01",
            "read my economic fortune.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B9")

    label("loc_13B9")

    TalkEnd(0xFE)
    Return()

    # Function_15_1353 end

    def Function_16_13BD(): pass

    label("Function_16_13BD")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#06400FC'mon Noｱl, c'mon!\x01",
            "Quick, let's get in\x01",
            "line.\x02\x03",
            "#06409FLet's have your love\x01",
            "fortune read!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#10111FI-I told you I'm fine!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_13BD end

    def Function_17_1458(): pass

    label("Function_17_1458")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14A4")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_14A4")

    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x8)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0xC)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    SetChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1546")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_160B")

    label("loc_1546")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1570")
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156B")
    SetChrFlags(0xD, 0x10)

    label("loc_156B")

    Jump("loc_160B")

    label("loc_1570")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1590")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_160B")

    label("loc_1590")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EB")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15CB")
    SetChrFlags(0xB, 0x80)

    label("loc_15CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15E6")
    ClearChrFlags(0x18, 0x80)

    label("loc_15E6")

    Jump("loc_160B")

    label("loc_15EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160B")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_160B")

    Return()

    # Function_17_1458 end

    def Function_18_160C(): pass

    label("Function_18_160C")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1000, 5750, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x101, 0, 0, 5000, 0)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "Welcome to the Fortune\x01",
            "House.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Here, you can have\x01",
            "anything read by our\x01",
            "master fortune teller!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Two people may enter.\x01",
            "What do you say, sir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P(Who should I\x01",
            "invite...?)\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWho will you invite?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Elie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noｱl")
    MenuCmd(1, 0, "Wazy")
    MenuCmd(1, 0, "KeA")
    MenuCmd(1, 0, "Fran")
    MenuCmd(1, 0, "Cecil")
    MenuCmd(1, 0, "Ilya")
    MenuCmd(1, 0, "Rixia")
    MenuCmd(1, 0, "Sully")
    MenuCmd(1, 0, "Cancel")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_17D3")
    MenuCmd(3, 0, 0x0)

    label("loc_17D3")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_17E5")
    MenuCmd(3, 0, 0x1)

    label("loc_17E5")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_17F7")
    MenuCmd(3, 0, 0x2)

    label("loc_17F7")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1809")
    MenuCmd(3, 0, 0x3)

    label("loc_1809")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_181B")
    MenuCmd(3, 0, 0x4)

    label("loc_181B")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_182D")
    MenuCmd(3, 0, 0x5)

    label("loc_182D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_183F")
    MenuCmd(3, 0, 0x6)

    label("loc_183F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1851")
    MenuCmd(3, 0, 0x7)

    label("loc_1851")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1863")
    MenuCmd(3, 0, 0x8)

    label("loc_1863")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1875")
    MenuCmd(3, 0, 0x9)

    label("loc_1875")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1887")
    MenuCmd(3, 0, 0xA)

    label("loc_1887")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F28")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_190D"),
        (1, "loc_1949"),
        (2, "loc_1984"),
        (3, "loc_19C1"),
        (4, "loc_19FD"),
        (5, "loc_1A39"),
        (6, "loc_1A74"),
        (7, "loc_1AB0"),
        (8, "loc_1AED"),
        (9, "loc_1B29"),
        (10, "loc_1B66"),
        (SWITCH_DEFAULT, "loc_1BA3"),
    )


    label("loc_190D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Elie.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_1949")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Tio.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_1984")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Randy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_19C1")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Noｱl.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_19FD")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Wazy.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_1A39")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "KeA.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_1A74")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Fran.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_1AB0")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Cecil.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_1AED")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Ilya.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_1B29")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Rixia.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_1B66")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Sully.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA3")

    label("loc_1BA3")

    FadeToDark(500, 0, -1)
    OP_0D()
    LoadEffect(0x0, "event/ev13000.eff")
    LoadChrToIndex("chr/ch14202.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00300.itc", 0x21)
    LoadChrToIndex("chr/ch08200.itc", 0x22)
    LoadChrToIndex("chr/ch07500.itc", 0x23)
    LoadChrToIndex("chr/ch05100.itc", 0x24)
    LoadChrToIndex("chr/ch10100.itc", 0x25)
    LoadChrToIndex("chr/ch02710.itc", 0x26)
    LoadChrToIndex("chr/ch02702.itc", 0x27)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 0, 50, 104800, 180)
    ClearChrFlags(0x15, 0x80)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C67"),
        (1, "loc_1C76"),
        (2, "loc_1C85"),
        (3, "loc_1C94"),
        (4, "loc_1CA3"),
        (5, "loc_1CB2"),
        (6, "loc_1CC1"),
        (7, "loc_1CD0"),
        (8, "loc_1CDF"),
        (9, "loc_1CEE"),
        (10, "loc_1CFD"),
        (SWITCH_DEFAULT, "loc_1D0C"),
    )


    label("loc_1C67")

    LoadChrToIndex("chr/ch00102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_1D0C")

    label("loc_1C76")

    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_1D0C")

    label("loc_1C85")

    LoadChrToIndex("chr/ch00302.itc", 0x20)
    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_1D0C")

    label("loc_1C94")

    LoadChrToIndex("chr/ch02902.itc", 0x20)
    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_1D0C")

    label("loc_1CA3")

    LoadChrToIndex("chr/ch03002.itc", 0x20)
    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_1D0C")

    label("loc_1CB2")

    LoadChrToIndex("chr/ch08202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_1D0C")

    label("loc_1CC1")

    LoadChrToIndex("chr/ch08502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_1D0C")

    label("loc_1CD0")

    LoadChrToIndex("chr/ch07502.itc", 0x20)
    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_1D0C")

    label("loc_1CDF")

    LoadChrToIndex("chr/ch05102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_1D0C")

    label("loc_1CEE")

    LoadChrToIndex("chr/ch05202.itc", 0x20)
    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_1D0C")

    label("loc_1CFD")

    LoadChrToIndex("chr/ch10102.itc", 0x20)
    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_1D0C")

    label("loc_1D0C")

    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x101, -500, 0, 5000, 0)
    SetChrPos(0x15, 500, 0, 5000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xF,
        (
            "I'll hold on to your\x01",
            "ticket, then.\x02",
        )
    )

    CloseMessageWindow()
    SubItemNumber(0x35D, 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gave the staffer a\x01",
            "ticket.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xF,
        (
            "Very well then. Please,\x01",
            "enter!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 19)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x15, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1E5D"),
        (1, "loc_1E6B"),
        (2, "loc_1E79"),
        (3, "loc_1E87"),
        (4, "loc_1E95"),
        (5, "loc_1EA3"),
        (6, "loc_1EB1"),
        (7, "loc_1EBF"),
        (8, "loc_1ECD"),
        (9, "loc_1EDB"),
        (10, "loc_1EE9"),
        (SWITCH_DEFAULT, "loc_1EF7"),
    )


    label("loc_1E5D")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1E6B")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1E79")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1E87")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1E95")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1EA3")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1EB1")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1EBF")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1ECD")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1EDB")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1EE9")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1EF7")

    label("loc_1EF7")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F23")
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_1F23")

    Jump("loc_1F72")

    label("loc_1F28")


    ChrTalk(
        0xF,
        "My, are you giving up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We'll be waiting for\x01",
            "your next visit!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1F72")

    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 0, 0, 4000, 180)
    EventEnd(0x5)
    Return()

    # Function_18_160C end

    def Function_19_1F8A(): pass

    label("Function_19_1F8A")

    SoundLoad(852)
    SetChrPos(0x101, -500, 0, 93000, 0)
    SetChrPos(0x15, 500, 0, 93000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 900, 97500, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 900, 100000, 3000)
    Sleep(500)

    def lambda_2015():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2015)

    def lambda_2026():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2026)

    def lambda_2037():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2037)
    Sleep(0)

    def lambda_204F():
        OP_9B(0x0, 0x15, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_204F)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x15, 2)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295B")

    ChrTalk(
        0x16,
        "#5PHaha, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PPlease sit here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PO-Ok.\x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    ChrTalk(
        0x101,
        (
            "#00003F#6P(She's just like we\x01",
            "heard... Exotic and\x01",
            "mysterious...)\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2162"),
        (1, "loc_21BA"),
        (2, "loc_2218"),
        (3, "loc_227B"),
        (4, "loc_22D4"),
        (5, "loc_235D"),
        (6, "loc_23AB"),
        (7, "loc_240C"),
        (8, "loc_2467"),
        (9, "loc_24BB"),
        (10, "loc_2516"),
        (SWITCH_DEFAULT, "loc_257A"),
    )


    label("loc_2162")


    NpcTalk(
        0x15,
        "Elie",
        (
            "#00100F#12P(Yes. Although her face\x01",
            "is hidden, she seems\x01",
            "very beautiful.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_21BA")


    NpcTalk(
        0x15,
        "Tio",
        (
            "#00200F#12P(Yes, and... Although\x01",
            "her face is hidden, she\x01",
            "seems quite beautiful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_2218")


    NpcTalk(
        0x15,
        "Randy",
        (
            "#00300F#12P(Yeah, and... Though she's\x01",
            "hidin' her face, she seems\x01",
            "quite the beauty.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_227B")


    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10100F#12P(Yes, and... Her face is\x01",
            "hidden, but she seems\x01",
            "very beautiful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_22D4")


    NpcTalk(
        0x15,
        "Wazy",
        "#10305F#12P(...Wow...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P(...Wazy?)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10304F#12P(Hehe. She's so\x01",
            "beautiful. I'm a little\x01",
            "surprised.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_235D")


    NpcTalk(
        0x15,
        "KeA",
        (
            "#01100F#12P(Yeah. She's hiding her\x01",
            "face, but she seems\x01",
            "pretty.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_23AB")


    NpcTalk(
        0x15,
        "Fran",
        (
            "#06400F#12P(Yes, and although her\x01",
            "face is hidden, she seems\x01",
            "amazingly beautiful.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_240C")


    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12P(Yes, and although her\x01",
            "face is hidden, she\x01",
            "looks quite lovely.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_2467")


    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01700F#12P(Yes. Her face is\x01",
            "hidden, but she seems\x01",
            "quite beautiful.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_24BB")


    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01802F#12P(Yes... She's hiding her\x01",
            "face, but she seems very\x01",
            "beautiful...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_2516")


    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000F#12P(Yeah, and... She's hiding\x01",
            "her face, but she seems\x01",
            "amazingly beautiful.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257A")

    label("loc_257A")


    ChrTalk(
        0x16,
        (
            "#5PHaha, what seems to be\x01",
            "the matter? Both of you\x01",
            "are staring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThere are others\x01",
            "waiting, so I'd like to\x01",
            "begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6POh, sorry. Umm, please\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha. Before that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWill you first tell me\x01",
            "your blood types?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_26E0"),
        (1, "loc_2711"),
        (2, "loc_2741"),
        (3, "loc_2768"),
        (4, "loc_278E"),
        (5, "loc_27B4"),
        (6, "loc_27D9"),
        (7, "loc_2808"),
        (8, "loc_283A"),
        (9, "loc_287B"),
        (10, "loc_28AD"),
        (SWITCH_DEFAULT, "loc_28D4"),
    )


    label("loc_26E0")


    NpcTalk(
        0x15,
        "Elie",
        "#00105F#12PBlood type... you say?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_2711")


    NpcTalk(
        0x15,
        "Tio",
        "#00205F#12PBlood type... you say?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_2741")


    NpcTalk(
        0x15,
        "Randy",
        "#00305F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_2768")


    NpcTalk(
        0x15,
        "Noｱl",
        "#10105F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_278E")


    NpcTalk(
        0x15,
        "Wazy",
        "#10305F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_27B4")


    NpcTalk(
        0x15,
        "KeA",
        "#01105F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_27D9")


    NpcTalk(
        0x15,
        "Fran",
        "#06405F#12PBlood type, you say?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_2808")


    NpcTalk(
        0x15,
        "Cecil",
        "#05905F#12PBlood type... you say?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_283A")


    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01705F#12PBlood type? What do you\x01",
            "need that for?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_287B")


    NpcTalk(
        0x15,
        "Rixia",
        "#01805F#12PBlood type... you say?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_28AD")


    NpcTalk(
        0x15,
        "Sully",
        "#14005F#12PBlood type?\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_28D4")


    ChrTalk(
        0x16,
        (
            "#5PYes. It's needed for a\x01",
            "proper reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5POf course, I won't force\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PNo, I don't mind. I'm\x01",
            "type O.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A81")

    label("loc_295B")


    ChrTalk(
        0x16,
        (
            "#5PMy, you're the one from\x01",
            "earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha, welcome. Please\x01",
            "sit here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PRight.\x02",
    )

    CloseMessageWindow()
    Call(0, 20)

    ChrTalk(
        0x16,
        (
            "#5PThat you have come again\x01",
            "makes me happier than\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen, would you tell me\x01",
            "your blood types?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P...You were type O,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PYes, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_2A81")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2ACC"),
        (1, "loc_2AF7"),
        (2, "loc_2B1D"),
        (3, "loc_2B44"),
        (4, "loc_2B6A"),
        (5, "loc_2B9F"),
        (6, "loc_2C0E"),
        (7, "loc_2C59"),
        (8, "loc_2C85"),
        (9, "loc_2CAB"),
        (10, "loc_2D06"),
        (SWITCH_DEFAULT, "loc_2D3C"),
    )


    label("loc_2ACC")


    NpcTalk(
        0x15,
        "Elie",
        "#00100F#12PUmm, I'm type A.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2AF7")


    NpcTalk(
        0x15,
        "Tio",
        "#00200F#12PI'm type AB.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2B1D")


    NpcTalk(
        0x15,
        "Randy",
        "#00300F#12PI'm type B.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2B44")


    NpcTalk(
        0x15,
        "Noｱl",
        "#10100F#12PI'm type A.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2B6A")


    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10300F#12PHehe. I think I'm type\x01",
            "AB?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2B9F")


    NpcTalk(
        0x15,
        "KeA",
        "#01109F#12PUmm, I think I'm type B.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYeah. You had that exam\x01",
            "at St. Ursula, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2C0E")


    NpcTalk(
        0x15,
        "Fran",
        "#06409F#12PI-I'm also type O!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6PHaha, a match.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2C59")


    NpcTalk(
        0x15,
        "Cecil",
        "#05900F#12PUmm, I'm type A.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2C85")


    NpcTalk(
        0x15,
        "Ilya",
        "#01700F#12PI'm type B.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2CAB")


    NpcTalk(
        0x15,
        "Rixia",
        "#01802F#12PAh... I'm also type O.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha. What a\x01",
            "coincidence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2D06")


    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000F#12PUmm... I guess I'm type\x01",
            "A.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2D3C")


    ChrTalk(
        0x16,
        "#5PHaha... Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen, what will I be\x01",
            "reading this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHmm, let's see...\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2DF3"),
        (1, "loc_2DFB"),
        (2, "loc_2E03"),
        (3, "loc_2E0B"),
        (4, "loc_2E13"),
        (5, "loc_2E1B"),
        (6, "loc_2E23"),
        (7, "loc_2E2B"),
        (8, "loc_2E33"),
        (9, "loc_2E3B"),
        (10, "loc_2E43"),
        (SWITCH_DEFAULT, "loc_2E4B"),
    )


    label("loc_2DF3")

    Call(0, 25)
    Jump("loc_2E4B")

    label("loc_2DFB")

    Call(0, 26)
    Jump("loc_2E4B")

    label("loc_2E03")

    Call(0, 27)
    Jump("loc_2E4B")

    label("loc_2E0B")

    Call(0, 28)
    Jump("loc_2E4B")

    label("loc_2E13")

    Call(0, 29)
    Jump("loc_2E4B")

    label("loc_2E1B")

    Call(0, 30)
    Jump("loc_2E4B")

    label("loc_2E23")

    Call(0, 31)
    Jump("loc_2E4B")

    label("loc_2E2B")

    Call(0, 32)
    Jump("loc_2E4B")

    label("loc_2E33")

    Call(0, 33)
    Jump("loc_2E4B")

    label("loc_2E3B")

    Call(0, 34)
    Jump("loc_2E4B")

    label("loc_2E43")

    Call(0, 35)
    Jump("loc_2E4B")

    label("loc_2E4B")

    OP_24(0x354)
    Call(0, 17)
    Call(0, 21)
    Return()

    # Function_19_1F8A end

    def Function_20_2E55(): pass

    label("Function_20_2E55")

    OP_68(0, 900, 103500, 3000)
    SetCameraDistance(15000, 3000)

    def lambda_2E74():
        OP_9B(0x0, 0xFE, 0xFFF6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E74)

    def lambda_2E89():
        OP_9B(0x0, 0xFE, 0xA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2E89)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x15, 1)

    def lambda_2EA6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EA6)

    def lambda_2EB3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2EB3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x15, 2)
    OP_6F(0x79)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -630, 50, 101950, 0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 630, 50, 101950, 0)
    OP_0D()
    Return()

    # Function_20_2E55 end

    def Function_21_2F09(): pass

    label("Function_21_2F09")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2F5C"),
        (1, "loc_2F65"),
        (2, "loc_2F6E"),
        (3, "loc_2F77"),
        (4, "loc_2F80"),
        (5, "loc_2F89"),
        (6, "loc_2F92"),
        (7, "loc_2F9B"),
        (8, "loc_2FA4"),
        (9, "loc_2FAD"),
        (10, "loc_2FB6"),
        (SWITCH_DEFAULT, "loc_2FBF"),
    )


    label("loc_2F5C")

    SetChrChipByIndex(0x15, 0x0)
    Jump("loc_2FBF")

    label("loc_2F65")

    SetChrChipByIndex(0x15, 0x1)
    Jump("loc_2FBF")

    label("loc_2F6E")

    SetChrChipByIndex(0x15, 0x21)
    Jump("loc_2FBF")

    label("loc_2F77")

    SetChrChipByIndex(0x15, 0x2)
    Jump("loc_2FBF")

    label("loc_2F80")

    SetChrChipByIndex(0x15, 0x3)
    Jump("loc_2FBF")

    label("loc_2F89")

    SetChrChipByIndex(0x15, 0x22)
    Jump("loc_2FBF")

    label("loc_2F92")

    SetChrChipByIndex(0x15, 0x4)
    Jump("loc_2FBF")

    label("loc_2F9B")

    SetChrChipByIndex(0x15, 0x23)
    Jump("loc_2FBF")

    label("loc_2FA4")

    SetChrChipByIndex(0x15, 0x24)
    Jump("loc_2FBF")

    label("loc_2FAD")

    SetChrChipByIndex(0x15, 0x5)
    Jump("loc_2FBF")

    label("loc_2FB6")

    SetChrChipByIndex(0x15, 0x25)
    Jump("loc_2FBF")

    label("loc_2FBF")

    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -600, 0, 5000, 90)
    SetChrPos(0x15, 600, 0, 5000, 270)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3013")
    SetChrPos(0x17, 1700, 0, 4040, 270)

    label("loc_3013")

    OP_68(0, 1500, 5750, 0)
    OP_68(0, 1000, 5750, 3000)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_30A9"),
        (1, "loc_31E2"),
        (2, "loc_330D"),
        (3, "loc_3441"),
        (4, "loc_3562"),
        (5, "loc_3686"),
        (6, "loc_37E7"),
        (7, "loc_391F"),
        (8, "loc_3A32"),
        (9, "loc_3B7B"),
        (10, "loc_3CB4"),
        (SWITCH_DEFAULT, "loc_3DCB"),
    )


    label("loc_30A9")


    NpcTalk(
        0x15,
        "Elie",
        (
            "#00100F#11P*sigh*... Somehow that was\x01",
            "all very mysterious.\x02\x03",
            "#00104FBased on how that fortune\x01",
            "teller acted, it honestly\x01",
            "seemed like she was right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah... She doesn't seem\x01",
            "like anyone ordinary.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        "#00100F#11PYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_31E2")


    NpcTalk(
        0x15,
        "Tio",
        (
            "#00202FThat fortune teller's\x01",
            "reading had quite the\x01",
            "aura.\x02\x03",
            "#00204FJust from the rumors, I\x01",
            "could tell she wasn't\x01",
            "someone ordinary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYou said it... She\x01",
            "seemed like an an\x01",
            "amazing person.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00200FYes, see you later,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_330D")


    NpcTalk(
        0x15,
        "Randy",
        (
            "#00309F...*sigh*, but even so,\x01",
            "she was a beautiful\x01",
            "lady, huh.\x02\x03",
            "#00304FThat mysterious air of\x01",
            "hers was simply\x01",
            "irresistible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha... You said it. And\x01",
            "seemed like the reading\x01",
            "itself made a lot of sense.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Randy",
        "#00300FYeah, later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_3441")


    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10100F*sigh*. That was all very\x01",
            "mysterious, wasn't it.\x02\x03",
            "#10104FAnd the reading itself was\x01",
            "very persuasive. I got this\x01",
            "strange feeling, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... It was quite\x01",
            "interesting.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        "#10100FYes, later then!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_3562")


    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10300FHehe, what an\x01",
            "interesting lady.\x02\x03",
            "#10304FI would've liked to chat\x01",
            "with her a bit more,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, certainly. It seemed\x01",
            "like she's experienced a\x01",
            "lot of different things.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        "#10300FYeah, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_3686")


    NpcTalk(
        0x15,
        "KeA",
        (
            "#01109FThat reading was super\x01",
            "interesting, you know?\x02\x03",
            "#01111FHow does she know all\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHmm. I don't know,\x01",
            "but... I'm sure she\x01",
            "trained quite a bit.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "KeA",
        "#01100FYeah, later!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D8")

    ChrTalk(
        0x17,
        "#01200F...Woof.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    EndChrThread(0x17, 0x0)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xB4, 0x1F4)

    def lambda_37B6():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_37B6)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x15, 3)
    SetChrFlags(0x17, 0x80)
    Jump("loc_37E2")

    label("loc_37D8")

    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)

    label("loc_37E2")

    Jump("loc_3DCB")

    label("loc_37E7")


    NpcTalk(
        0x15,
        "Fran",
        (
            "#06402F*sigh*, what a mysterious\x01",
            "lady, right?\x02\x03",
            "#06409FCool women like my sister\x01",
            "are great, but I also admire\x01",
            "people like that, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha... There aren't\x01",
            "many people like that in\x01",
            "Crossbell, are there.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Fran",
        "#06400FYes, see you!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_391F")


    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909FHaha... What a\x01",
            "mysterious woman.\x02\x03",
            "#05904FIt seemed like she has a\x01",
            "complicated past, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah... I wonder what\x01",
            "circumstances brought\x01",
            "her to Crossbell.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Cecil",
        "#05900FYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_3A32")


    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01702FMan, there's all kinds of\x01",
            "amazing people in the\x01",
            "world, isn't there.\x02\x03",
            "#01703FI've never met her before,\x01",
            "but it felt like she saw\x01",
            "through me top to bottom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, indeed... She\x01",
            "doesn't seem like anyone\x01",
            "ordinary.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilya",
        "#01700FYeah, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_3B7B")


    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01803F(Such masterful\x01",
            "divination... Could she\x01",
            "be...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FRixia, what's wrong?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01805FAh, nothing.\x02\x03",
            "#01802FHaha. That was a\x01",
            "mysterious yet fun\x01",
            "experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha. I feel the same.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        "#01803FYes, see you later.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_3CB4")


    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000FThat fortune teller was\x01",
            "amazing.\x02\x03",
            "#14006FI don't believe in readings\x01",
            "that much, but I'll make an\x01",
            "exception just this once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... It was an\x01",
            "amazing reading, too.\x02\x03",
            "#00000FWell then, I'll take off\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        "#14000FYeah, see ya.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 22)
    WaitChrThread(0x15, 3)
    Jump("loc_3DCB")

    label("loc_3DCB")

    Return()

    # Function_21_2F09 end

    def Function_22_3DCC(): pass

    label("Function_22_3DCC")


    def lambda_3DD1():

        label("loc_3DD1")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_3DD1")

    QueueWorkItem2(0x101, 2, lambda_3DD1)
    OP_93(0x15, 0xB4, 0x1F4)

    def lambda_3DEA():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3DEA)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x15, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_22_3DCC end

    def Function_23_3E11(): pass

    label("Function_23_3E11")

    Fade(500)
    Sound(895, 0, 50, 0)
    Sound(852, 2, 70, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 900, 103300, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Return()

    # Function_23_3E11 end

    def Function_24_3E5B(): pass

    label("Function_24_3E5B")

    Fade(500)
    StopSound(852, 1000, 40)
    StopEffect(0x0, 0x2)
    OP_0D()
    Return()

    # Function_24_3E5B end

    def Function_25_3E6B(): pass

    label("Function_25_3E6B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Elie\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4801")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Elie",
        "#00112F#12PL-Lloyd!?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PWell, we came here together,\x01",
            "and we won't have many\x01",
            "chances like this, you see.\x02\x03",
            "#00000FWant to give it a try?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00106F#12PA-A try, you say... Now\x01",
            "look, you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PUmm... Is something\x01",
            "wrong?\x02\x03",
            "#00003FIf you're that against\x01",
            "it we can stop, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00105F#12PI-It's not that I'm\x01",
            "against it...\x02\x03",
            "#00113FHonestly, what I am\x01",
            "going to do with you...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00111F#12P...*sigh*, nevermind.\x02\x03",
            "#00100FI apologize. Please do\x01",
            "our compatibility\x01",
            "reading.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHaha, very well then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Elie",
        "#00101F#12P(*gulp*...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man and a\x01",
            "talented woman brimming with\x01",
            "diligence and tolerance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs comrades with the same goals,\x01",
            "you overcame many hardships\x01",
            "together and formed a solid bond...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_43FF")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5PMy... And it developed greatly through\x01",
            "some kind of extreme situation you\x01",
            "went through previously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt is not yet definite, but if you\x01",
            "continue to nurture these feelings,\x01",
            "you will eventually become close.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_44BD")

    label("loc_43FF")


    ChrTalk(
        0x16,
        (
            "#5PThough your circumstances differ,\x01",
            "you each acknowledge and complement\x01",
            "the other's strengths...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you continue to nurture\x01",
            "these feelings, you may\x01",
            "eventually become close.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_44BD")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Elie",
        "#00112F#12PC-Close!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. Well then... It\x01",
            "was rude of me to say\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever, the key is your\x01",
            "future actions and\x01",
            "choices...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PM-Mine?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAt the very least, work\x01",
            "to sense each other's\x01",
            "feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs for you, though unconcious, you have\x01",
            "a devilish nature that charms those\x01",
            "around you─ That is the hint I see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F#6PD-Devilish, you say...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00106F#12P(I feel it was very\x01",
            "accurate...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PStill, a fortune is just\x01",
            "a fortune. It's not a\x01",
            "prediction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P"Fate", based on the\x01",
            "principle of causality, is\x01",
            "ever-changing, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt can change greatly,\x01",
            "depending on your future\x01",
            "actions... Remember that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PR-Right. I'll keep that\x01",
            "in mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F3C")

    label("loc_4801")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PElie, is there something\x01",
            "you want to have read?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00105F#12PMy, I get to decide?\x02\x03",
            "#00103FHmm, let me think...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00100F#12PIn that case, why don't you\x01",
            "read the future of Crossbell\x01",
            "State for us?\x02\x03",
            "#00103FWhat will happen with the\x01",
            "independence proposal...\x01",
            "Aren't you worried about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#6PYeah, I guess I am.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00000F#6P...Then, if you please?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Elie",
        "#00101F#12P(*gulp*...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P...Before long, you both\x01",
            "will be swallowed up in\x01",
            "a great fate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThe despair of facing a\x01",
            "heretofore unseen great\x01",
            "Barrier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYou will experience it.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PWhat!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        "#00105F#12PW-What does that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...That I do not know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever, I sense its\x01",
            "footsteps drawing steadily\x01",
            "closer to both of you...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...That is all I am able\x01",
            "to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00103F#12PW-What in the world was\x01",
            "that just now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PA great Barrier... And\x01",
            "the despair of facing\x01",
            "it...\x02\x03",
            "#00008FNo way. Could it be\x01",
            "related to the mayor's\x01",
            "independence proposal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI do not know the\x01",
            "details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the end, my readings are\x01",
            "merely my interpretation of\x01",
            "the hints I receive.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Elie",
        (
            "#00106F#12PHmm. I am worried about it,\x01",
            "but... I suppose we can only\x01",
            "think about what it means.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt seems I have stirred\x01",
            "up an excessive amount\x01",
            "of worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PStill, a fortune is just\x01",
            "a fortune. It's not a\x01",
            "prediction...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P"Fate", based on the\x01",
            "principle of causality, is\x01",
            "ever-changing, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt can change greatly,\x01",
            "depending on your future\x01",
            "actions... Remember that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6P...Alright, we'll keep\x01",
            "that in mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F3C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_25_3E6B end

    def Function_26_4F48(): pass

    label("Function_26_4F48")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Tio\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58A5")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6P...I mean, what do you\x01",
            "think? Since we're here,\x01",
            "let's give it a try.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00203F#12PHmm. How interesting.\x02\x03",
            "#00200FIt seems I'll be able to\x01",
            "think about my future plans\x01",
            "depending on the result.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI'm not sure I get your\x01",
            "meaning.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00203F#12PWell, it's fine even if\x01",
            "you don't understand.\x02\x03",
            "#00200FThen, the reading, if\x01",
            "you please?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHaha, very well then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00205F#12P(...I sense a mysterious\x01",
            "aura... What could it\x01",
            "be...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and a girl hiding\x01",
            "superior abilities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThough apart in age, you\x01",
            "trust each other as\x01",
            "friends and equals...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_541A")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5PMy... And it developed greatly through\x01",
            "some kind of extreme situation you\x01",
            "went through previously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThough there will be obstacles, I\x01",
            "get the impression that it is quite\x01",
            "likely you will become close.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_54DF")

    label("loc_541A")


    ChrTalk(
        0x16,
        (
            "#5PThough your circumstances differ,\x01",
            "you each acknowledge and complement\x01",
            "the other's strengths...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI think there will be\x01",
            "obstacles, but there is a good\x01",
            "chance you will become close.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_54DF")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00204F#12PHmm... An interesting\x01",
            "result, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PUmm, I don't get it,\x01",
            "but...\x02\x03",
            "#00000FYou said "obstacles".\x01",
            "What could you be\x01",
            "talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. If I had to say, social\x01",
            "taboos and the stares of\x01",
            "others. That sort of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you both are prepared\x01",
            "to surmount such things,\x01",
            "then it's possible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PUmm...? I don't know if I'm\x01",
            "prepared or anything...\x02\x03",
            "#00003FI have a deep friendship with\x01",
            "Tio already. I don't mind the\x01",
            "stares of others at all...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00211F#12PAn unexpected bombshell\x01",
            "statement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuuuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha. How interesting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI can only pray to the Goddess that\x01",
            "that personality of yours does not\x01",
            "invite disaster in the future.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00206F#12PYes, my thoughts\x01",
            "exactly.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PU-Umm... Could you talk\x01",
            "without leaving me\x01",
            "behind...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F12")

    label("loc_58A5")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWhat do you want to have\x01",
            "read, Tio?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00205F#12PIs it okay for me to\x01",
            "decide?\x02\x03",
            "#00203F...Let me think...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00200F#12PCould you read my\x01",
            "compatibility with\x01",
            "Mishy?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PWith Mishy?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00202F#12PYes, whether I'll be able to live\x01",
            "in contact with Mishy... That's\x01",
            "what I'd like you to read.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PHmm, this request is\x01",
            "rather unique. ...Very\x01",
            "well, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00205F#12P(...I sense a mysterious\x01",
            "aura... What could it\x01",
            "be...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PYour compatibility with\x01",
            "Mishy is... It appears\x01",
            "to be quite good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs long as you love him,\x01",
            "Mishy will be sure to\x01",
            "answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PMany Mishy goods and encounters\x01",
            "at the theme park await you in\x01",
            "the future as well...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        "#00202F#12PThank you very much.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PW-Well, that's great.\x01",
            "She said Mishy will\x01",
            "surely answer you.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00204F#12PYes. As a fan, there\x01",
            "could be nothing better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5POh, and one more thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBefore long, a great trial\x01",
            "to test your feelings\x01",
            "toward Mishy will appear...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI get that sort of\x01",
            "impression. ...Be\x01",
            "careful, all right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Tio",
        (
            "#00200F#12P...That's exactly what I\x01",
            "wish for.\x02\x03",
            "#00201FNo matter what kind of\x01",
            "trial appears, my love for\x01",
            "Mishy will never fade...\x02\x03",
            "#00204FI will prove it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. I'll be rooting\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6P(I-It's no use. There's\x01",
            "so many retorts, I can't\x01",
            "deal with them all!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F12")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_26_4F48 end

    def Function_27_5F1E(): pass

    label("Function_27_5F1E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Randy\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6841")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00306F#12PNow look here... Do that\x01",
            "stuff with a girl you're\x01",
            "interested in, alright?\x02\x03",
            "#00301FJust what's so fun about\x01",
            "checkin' compatibility\x01",
            "between dudes?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, well isn't it fine?\x02\x03",
            "#00000FSpeaking of compatibility,\x01",
            "it also exists between\x01",
            "male friends, right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00306F#12PHmm... Well, whatever.\x02\x03",
            "#00300FAlright then, miss. Do\x01",
            "your thing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHaha. Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00305F#12P(Oh... This is the real\x01",
            "deal, huh.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and a young man with\x01",
            "hidden inner passion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAlways taking the lead as a unifying force,\x01",
            "a strong ally who encourages and guides his\x01",
            "friends with his cheerfulness...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6431")
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5PMy... And it developed greatly through\x01",
            "some kind of extreme situation you\x01",
            "went through previously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAnd from now on, the better you\x01",
            "understand each other, the more\x01",
            "solid a bond that will form.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_64FC")

    label("loc_6431")


    ChrTalk(
        0x16,
        (
            "#5PThough your circumstances differ,\x01",
            "you each acknowledge and complement\x01",
            "the other's strengths...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFrom now on, the better you\x01",
            "understand each other, the more\x01",
            "solid a bond that will form.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_64FC")

    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00305F#12POh... That's a pretty\x01",
            "good result, isn't it.\x02\x03",
            "#00304FMilady, PeTiote... Noｱl\x01",
            "too... I'm sorry.\x02\x03",
            "#00302FLooks like Lloyd's mine.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Stop blurting out\x01",
            "inappropriate stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI should mention that I did\x01",
            "not get a hint that you two\x01",
            "will become close at present.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PHowever, fate can be\x01",
            "changed if you both\x01",
            "strongly wish it to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you were to ask if such\x01",
            "a thing was impossible, I\x01",
            "cannot rule it out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PU-Um, if possible, I'd\x01",
            "like you to deny it,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00309F#12PNow, now, don't be shy.\x02\x03",
            "#00304FIf you wish it, I'll\x01",
            "even be your big bro─\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00011F#6PI'm not being shy or\x01",
            "anything!!\x02\x03",
            "#00006F*sigh*. Just cut me some\x01",
            "slack already...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F9E")

    label("loc_6841")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWhat to you want to have\x01",
            "read, Randy?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00305F#12PHmm, I get to pick?\x02\x03",
            "#00303FLet's see...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00309F#12PHmm, in that case... Why\x01",
            "don't you read my luck\x01",
            "pickin' up girls from now on?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F#6PY-You sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn short, the probability that\x01",
            "an unfamiliar woman accepts\x01",
            "your invitation... Is that it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00309F#12PThen, if you could,\x01",
            "please!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00305F#12P(Oh... This is the real\x01",
            "deal, huh.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P...Regarding your seduction\x01",
            "skills... the success rate\x01",
            "is around 50/50.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt seems many women feel the charm of your\x01",
            "bright personality and handsome looks. However,\x01",
            "there are many who are vigilant as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBy the way, even if you are successful,\x01",
            "in your case, the chance of reaching\x01",
            "true love can be said to be almost zero.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0x15,
        "Randy",
        "#00306F#12P#4SACK!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00306F#12PL-Lloyd... I'm done\x01",
            "for...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00012F#6PN-Now, now... Don't be\x01",
            "so hard on yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha, that's right. If I could\x01",
            "give a word of advice... Do not\x01",
            "let the love near you escape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PVery near to you is one of the opposite\x01",
            "sex who thinks of you as precious... I\x01",
            "got that kind of impression.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    NpcTalk(
        0x15,
        "Randy",
        "#00305F#12PS-Seriously!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould she mean... 2nd\x01",
            "Lt. Mire─\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Randy",
        (
            "#00303F#12P─Alright!! That bein' the\x01",
            "case...\x02\x03",
            "#00309FI can only keep pickin' up\x01",
            "girls 'til I find the cutie\x01",
            "who thinks of me as precious!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00006F#6PH-How can you reach that\x01",
            "conclusion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P(...Pretending to not notice, I\x01",
            "wonder. Haha. That has nothing\x01",
            "to do with me, though.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F9E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_27_5F1E end

    def Function_28_6FAA(): pass

    label("Function_28_6FAA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Noｱl\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77D9")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Noｱl",
        "#10105F#12PL-Lloyd!?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha. Well since we're\x01",
            "here, I thought why not\x01",
            "try it?\x02\x03",
            "#00000FWe can stop if you don't\x01",
            "want to...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10111F#12PN-No!! It's not\x01",
            "troublesome or anything,\x01",
            "but...\x02\x03",
            "#10116F(Or rather, is he saying\x01",
            "this because he's an\x01",
            "airhead too?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PUmm, what is it?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10106F#12PN-Nevermind.\x02\x03",
            "#10100F...Umm, then please do\x01",
            "the reading.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHaha. Very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12P(Wow... Is it some kind\x01",
            "of technique...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and a girl with a sincere\x01",
            "will hidden in her eyes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYour assignments differ, but through\x01",
            "cooperating to protect something, you\x01",
            "have built a strong relationship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf either of you steps\x01",
            "forward to deepen it, it\x01",
            "could become more intimate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12PA step forward, you\x01",
            "said. I'm not good at\x01",
            "that sort of thing.\x02\x03",
            "#10106FRather, I'm one who\x01",
            "draws lines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. From what I can see, you\x01",
            "are the cautious type, so I\x01",
            "don't think it can be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you don't become at least\x01",
            "somewhat proactive, will you not\x01",
            "lose that which you have gained?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10103F#12PYou might be right about\x01",
            "that, but...\x02\x03",
            "#10101FBut one of these days,\x01",
            "I'm going to work up the\x01",
            "courage and...!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PU-Umm, Noｱl? Aren't you\x01",
            "getting a little too\x01",
            "serious?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12P*sigh*...\x02\x03",
            "#10106FY-You're right. After\x01",
            "all, we're just trying\x01",
            "it out...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12PWait, no! I'm not feeling\x01",
            "regret or anything! It's\x01",
            "not like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI-I know that, so just\x01",
            "calm down already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P(Haha. They make an\x01",
            "unexpectedly good\x01",
            "combination.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EA9")

    label("loc_77D9")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWhat would you like to\x01",
            "have read, Noｱl?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12PI get to decide?\x02\x03",
            "#10103FHmm, let's see...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10100F#12PThen, the future of the CGF...\x01",
            "How about something like that?\x02\x03",
            "#10104FI'll return to the CGF at some\x01",
            "point, so I'd like to prepare\x01",
            "myself for when it happens.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#6PSure, why not?\x02\x03",
            "#00000FUmm, then, if you\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10105F#12P(Wow... Is it some kind\x01",
            "of technique...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5P...I sense change.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBefore long, the organization\x01",
            "to which you are assigned will\x01",
            "undergo some kind of change...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhen that happens, you\x01",
            "will be forced into some\x01",
            "kind of big decision...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10103F#12PChange... and a\x01",
            "decision, you said.\x02\x03",
            "#10101FUmm, what could they\x01",
            "mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI am sorry, but I cannot\x01",
            "see that clearly at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFor better or worse, I\x01",
            "will say that the future\x01",
            "depends on your actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PHmm. Indeed, based on the current\x01",
            "situation, both of those\x01",
            "predictions are possible.\x02\x03",
            "#00000FBased on the result of the\x01",
            "independence proposal, the Guardian\x01",
            "Force itself could change.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10100F#12PWill it mean progress\x01",
            "for the CGF or decline?\x02\x03",
            "#10103FI pray for progress,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf I could just say one\x01",
            "thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt will be a decision the likes of which\x01",
            "you have not faced before, nor will again.\x01",
            "Make a decision you will not regret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the end, a reading is just a reading...\x01",
            "Depending on your determination, the\x01",
            "future could be very different.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Noｱl",
        (
            "#10100F#12PYes, you're right...\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EA9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_28_6FAA end

    def Function_29_7EB5(): pass

    label("Function_29_7EB5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Wazy\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8597")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10302F#12PHehe, well this is rare.\x01",
            "You approaching me, I\x01",
            "mean.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00003F#6PN-No, that's not it.\x02\x03",
            "#00000FWe're here, so I was\x01",
            "thinking of trying it\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        "#10309F#12PHehe, no need to be shy.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        "#00006F#6PA-Anyway, if you please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha, sure, why not.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5P(...I see...)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10309F#12PHehe. What's wrong,\x01",
            "fortune-teller lady?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...Haha, it is nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and a boy who wittily\x01",
            "wanders the world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhile your personalities are exactly\x01",
            "opposite, by recognizing each other's good\x01",
            "points you have built a certain trust...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you deepen that trust and forgive\x01",
            "each other for deeds past and\x01",
            "present, a solid bond will form.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PPast and present, you\x01",
            "say...\x02\x03",
            "#00003FIt's true that I've\x01",
            "heard hardly anything\x01",
            "about your past, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10309F#12PHehe, come on. Things might\x01",
            "look like this, but I told\x01",
            "you everything.\x02\x03",
            "#10304FAnd, don't you think things\x01",
            "are more exciting with a\x01",
            "few secrets between us?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PI always knew you had a\x01",
            "few secrets...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. Well, your\x01",
            "relationship will\x01",
            "require patience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAfter all, this type of\x01",
            "person hardly ever reveals\x01",
            "their true motives.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10304F#12PHehe, you said it.\x02\x03",
            "#10309FI would love it if you\x01",
            "used a patient approach\x01",
            "with me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00006F#6POh man...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A6A")

    label("loc_8597")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWhat would you like to\x01",
            "have read, Wazy?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10305F#12POh, I get to pick?\x02\x03",
            "#10304FHmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10300F#12PIn that case, how about\x01",
            "this?\x02\x03",
            "#10304FWhether I'll be able to get\x01",
            "what I want in this land...\x01",
            "I want you to read that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PWhat you want?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10304F#12PHehe, it's a secret.\x02\x03",
            "#10300FHow about it, lady? Can\x01",
            "you read that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha, how interesting.\x01",
            "...I shall try.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)

    ChrTalk(
        0x16,
        "#5P(...I see...)\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10309F#12PHehe. What's wrong,\x01",
            "fortune-teller lady?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P...Haha, it is nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PThe thing you seek...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAlthough it is extremely\x01",
            "close by, you cannot\x01",
            "reach it at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFor now you need only\x01",
            "wait... That's the\x01",
            "impression I'm getting.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10304F#12P...I see. Just knowing\x01",
            "that much is plenty for\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00006F#6PI have no idea what's\x01",
            "what, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Wazy",
        (
            "#10300F#12PHehe. For now, that's just\x01",
            "fine.\x02\x03",
            "#10304FAnd, don't you think things\x01",
            "are more exciting with a\x01",
            "few secrets between us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P*sigh*, honestly...\x02",
    )

    CloseMessageWindow()

    label("loc_8A6A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_7EB5 end

    def Function_30_8A76(): pass

    label("Function_30_8A76")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to KeA\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914F")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01110F#12P"Compatibility" says if\x01",
            "you're well-matched or\x01",
            "not, right?\x02\x03",
            "#01109FKeA really hopes to be\x01",
            "well-matched with you,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha, yeah. I'd be happy\x01",
            "if that were the case.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6PUmm, then, the reading,\x01",
            "if you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha. Understood.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "KeA",
        "#01110F#12P(Wah, it's pretty...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and a girl who brings\x01",
            "light with her smile...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHer existence gives you all\x01",
            "courage, and your strong will to\x01",
            "protect her creates your bond...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs long as you all\x01",
            "protect her, your bond\x01",
            "will never break.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01106F#12P...KeA might be a little\x01",
            "disappointed.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00005F#6PHuh? Why? That was a\x01",
            "good result, wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01108F#12PHmm... That is right,\x01",
            "but it's not what I\x01",
            "wanted, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5P...Haha. Young lady, this\x01",
            "reading is not everything.\x01",
            "There is no need to be sad.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PAlso, even if your relationship is now\x01",
            "like that of a chick and its parent\x01",
            "bird... Chicks eventually grow up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen... Their parents notice,\x01",
            "you know. That their children\x01",
            "have become able to fly.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01105F#12P...Oh yeah, that's\x01",
            "right.\x02\x03",
            "#01109FAlright, KeA's going to\x01",
            "hurry and grow up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHmm. I don't really get\x01",
            "it, but at least she's\x01",
            "happy, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9866")

    label("loc_914F")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWhat would you like to\x01",
            "have read, KeA?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01105F#12PCan KeA pick?\x02\x03",
            "#01111FHmm, then...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01110F#12PAh, that's right! I want\x01",
            "you to read KeA and\x01",
            "Zeit's compatibility!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#5PZeit?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PU-Umm... He's a dog who\x01",
            "lives with us at our\x01",
            "workplace.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#5PHaha, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PVery well, young lady.\x01",
            "Bring that Zeit here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI'll perform your\x01",
            "reading immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PHuuuh!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01110F#12PReally!?\x02\x03",
            "#01109FThen, I'll bring him\x01",
            "here!!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 1500, 0, 101500, 270)
    OP_0D()
    OP_93(0x15, 0xB4, 0x1F4)
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)

    def lambda_93E8():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_93E8)
    WaitChrThread(0x15, 1)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PS-Sorry. That was\x01",
            "weird...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. Do not worry. It\x01",
            "seems rather\x01",
            "interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P(She's pretty strange,\x01",
            "isn't she...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 630, 50, 101950, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x27)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 0, 0, 0)
    SetChrPos(0x17, 2000, 0, 101000, 315)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x17,
        "#01200F#12PGrrowl... Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "KeA",
        "#01110F#12P(Wah, it's pretty...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PA girl who brings light with\x01",
            "her smile and a proud wolf who\x01",
            "watches over his comrades...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYou can understand each other's\x01",
            "feelings. I sense a bond of\x01",
            "mutual respect between you two...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PNo matter what may happen in\x01",
            "the future, the wolf will\x01",
            "continue to watch over you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x2)

    NpcTalk(
        0x15,
        "KeA",
        (
            "#01100F#12PZeit, we'll be together\x01",
            "forever!\x02\x03",
            "#01109FEhehe. Aren't you happy,\x01",
            "Zeit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#01203F#12PGrrowl... Woof.\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha... Thank you very\x01",
            "much. Although her\x01",
            "request was a bit much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. I was able to perform an\x01",
            "unusual reading, so it was a\x01",
            "good experience for me as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9866")

    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P(And... I was able to\x01",
            "see a very interesting\x01",
            "impression.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P(I would say only the\x01",
            "Goddess knows what will\x01",
            "happen next.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PMiss...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha... Nevermind.\x01",
            "Please come again...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_30_8A76 end

    def Function_31_9973(): pass

    label("Function_31_9973")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Fran\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0A5")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06405F#12POh, Lloyd! You're\x01",
            "interested in your\x01",
            "compatibility with me!?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00002F#6PHaha. Well since we have\x01",
            "the opportunity, why not\x01",
            "try it, I thought, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06409F#12PHaha, that's right!\x01",
            "Miss, if you please!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PHaha. Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06405F#12P(Waah~... It's somehow\x01",
            "amazing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and a girl who supports him\x01",
            "from behind the scenes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThrough working together countless\x01",
            "times, you have formed a solid trusting\x01",
            "relationship and formed a bond...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#5PAh, however... It seems\x01",
            "the girl has someone\x01",
            "dear to her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAs long as that feeling remains,\x01",
            "there is little chance yours will\x01",
            "become that kind of relationship.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06409F#12POh! Right on the money!\x01",
            "You're as masterful as\x01",
            "I've heard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha, thank you.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha. I can picture it\x01",
            "now.\x02\x03",
            "#00000FUmm, Fran. I'll ask this\x01",
            "for reference, but the\x01",
            "person dear to you is...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06409F#12P#4SOf course, it's my\x01",
            "sister!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHmm, so it is as I imagined.\x02\x03",
            "#00000FAs I thought, it's still too\x01",
            "early for you to be talking about\x01",
            "these sorts of things, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. But on the\x01",
            "contrary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you become better than\x01",
            "her sister, there is a\x01",
            "possibility, is there not?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06409F#12PThat's right. Please do\x01",
            "your best, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PWell, even if you tell\x01",
            "me to...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6DE")

    label("loc_A0A5")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PIs there something you\x01",
            "want to have read, Fran?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06405F#12PAh, you're letting me\x01",
            "decide?\x02\x03",
            "#06404FHmm, let me see...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06405F#12PAh, come to think of\x01",
            "it...!\x02\x03",
            "#06401FMiss, will you find Ban\x01",
            "Ban for me!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PBan Ban?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYour precious stuffed\x01",
            "animal, right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06400F#12PYes. I actually wanted to\x01",
            "bring him to Michelam,\x01",
            "but...\x02\x03",
            "#06406FHe disappeared when my mom\x01",
            "cleaned my room the day\x01",
            "before, and I couldn't!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#6PI-I see...\x02\x03",
            "#00000FUmm, could you please?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06405F#12P(Waah~... It's somehow\x01",
            "amazing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PThe lost stuffed\x01",
            "animal... Could it be a\x01",
            "bear?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06405F#12PT-That's it!! You know\x01",
            "that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. It is distinctive,\x01",
            "I knew immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYour stuffed animal, at\x01",
            "present... is hidden in the\x01",
            "shadows under your bed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06403F#12PU-Under the bed? That's\x01",
            "odd, I already looked\x01",
            "there, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYou most likely overlooked\x01",
            "it because it is a place\x01",
            "you immediately thought of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you look carefully,\x01",
            "you will surely find it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06409F#12PI will, thank you very\x01",
            "much!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PHaha, that's great,\x01",
            "Fran.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Fran",
        (
            "#06406F#12PYes, it really is! I've\x01",
            "been really sad without\x01",
            "Ban Ban.\x02\x03",
            "#06409FI'll look for him\x01",
            "tomorrow when we get\x01",
            "back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. I am glad I could\x01",
            "be of help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6DE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_31_9973 end

    def Function_32_A6EA(): pass

    label("Function_32_A6EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Cecil\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE69")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12PMy, Lloyd...\x02\x03",
            "#05909FHaha. Even if you have something\x01",
            "like that read specifically, I'm\x01",
            "sure our compatibility is perfect.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha. Well this is a\x01",
            "great opportunity, so\x01",
            "let's try it out.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#6P...And so, if you\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, understood.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12P(My... She seems really\x01",
            "amazing somehow.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and a woman overflowing\x01",
            "with a kind spirit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn the feelings that have\x01",
            "grown since childhood\x01",
            "lies a unique bond...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PHowever, a certain\x01",
            "feeling remains in the\x01",
            "woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PA strong feeling,\x01",
            "towards her lost\x01",
            "lover...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05904F#12PHaha. To think it would\x01",
            "be this close to the\x01",
            "mark.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...Sorry, Cecil. For\x01",
            "asking her to read\x01",
            "something like that.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12PMy, there's no need to\x01",
            "apologize. I'm really happy we\x01",
            "have such good compatibility.\x02\x03",
            "#05904FAnd, I'm glad to again confirm\x01",
            "that I haven't forgotten Guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5POur feelings towards those\x01",
            "we love continue eternally,\x01",
            "no matter what happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAnd, it is precisely because\x01",
            "you have them that you stand\x01",
            "where you are now...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12PMiss, could you possibly\x01",
            "have someone...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PIt seems I have said too\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PA mere fortune teller\x01",
            "such as myself should\x01",
            "not have intruded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PNo, thank you for those\x01",
            "words. I'll keep them in\x01",
            "mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha... You're welcome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B563")

    label("loc_AE69")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PIs there something you\x01",
            "want to have read,\x01",
            "Cecil?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12PHuh, can I decide?\x02\x03",
            "#05904FHaha. Hmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909F#12PThen... I wonder if we can ask\x01",
            "her to read the kind of wife\x01",
            "you'll have in the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#00011F#6P#4SHUH.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PW-Wait, Cecil! As you\x01",
            "can imagine, it's too\x01",
            "embarrassing...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909F#12PMy, isn't it fine? Your\x01",
            "sister wants to know,\x01",
            "after all.\x02\x03",
            "#05900FHaha. If you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05900F#12P(My... She seems really\x01",
            "amazing somehow.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and his female partner\x01",
            "for life, that is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P............\x01",
            "............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05905F#12PMy... Is something the\x01",
            "matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI am terribly sorry, but...\x01",
            "At the present time, there\x01",
            "is nothing I can say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI have been asked for\x01",
            "similar readings countless\x01",
            "times, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5POnce in a while, there are\x01",
            "too many possible women and\x01",
            "I cannot narrow it down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYours is one such case.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05909F#12PHmm... I see. I didn't\x01",
            "expect that.\x02\x03",
            "#05908FI'm proud of Lloyd. I\x01",
            "didn't think he would\x01",
            "leave girls alone, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P(I-I feel like she's\x01",
            "talking about me like I\x01",
            "have no morals at all...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Cecil",
        (
            "#05903F#12PUmm, Lloyd? Your sister\x01",
            "is getting a little\x01",
            "worried about you, but...\x02\x03",
            "#05901FTake care not to make a\x01",
            "girl sad one of these\x01",
            "days, alright?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00012F#6PI-I'm telling you, I\x01",
            "won't!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B563")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_A6EA end

    def Function_33_B56F(): pass

    label("Function_33_B56F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Ilya\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB58")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6P...Wait, I decided on my\x01",
            "own, but are you ok with\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01709F#12PAhaha, how interesting. Let's do it☆\x02\x03",
            "#01704FHuhu. Cecil will hate me for this,\x01",
            "but I guess I'll take little bro for\x01",
            "myself if there's a good result.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PW-Well, let's give it a\x01",
            "try.\x02\x03",
            "#00000FThen, if you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, understood.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01705F#12P(Wow... This is the real\x01",
            "thing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and the dancer who burns\x01",
            "with passion on stage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHer earnest feelings\x01",
            "towards her goals attract\x01",
            "and charm others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThere is a good chance it can become\x01",
            "a much deeper relationship if he, who\x01",
            "supports her, does so wholeheartedly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever... In the end, the stage\x01",
            "is what is precious to her. It\x01",
            "will be difficult to change that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHaha. So the stage is\x01",
            "number one for you,\x01",
            "isn't it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01700F#12PHuhu, that's just how it is.\x02\x03",
            "#01709FEven so, miss. I never\x01",
            "thought you'd show me a\x01",
            "reading like that.\x02\x03",
            "#01700FI don't think it's a skill\x01",
            "mastered in one day... Then,\x01",
            "you've trained somewhere?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Jump("loc_C3C5")

    label("loc_BB58")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PIs there something you\x01",
            "want to have read, Ilya?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01705F#12PMy, I'm deciding?\x02\x03",
            "#01703FHmm, let's see...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01709F#12PThen, whether Rixia or Sully\x01",
            "will surpass me in the\x01",
            "future! ...How about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PThose two...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01704F#12PWell honestly, maybe\x01",
            "this isn't something to\x01",
            "have read, but...\x02\x03",
            "#01702FI'll do it as a way to\x01",
            "confirm that my eyes\x01",
            "don't deceive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYour disciples'\x01",
            "future... Would reading\x01",
            "that be alright?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01700F#12PYes, something like\x01",
            "that. Can you?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01705F#12P(Wow... This is the real\x01",
            "thing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PTwo young dancers discovered\x01",
            "by the dancer who burns with\x01",
            "passion on stage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThey have bottomless talent\x01",
            "hidden within them, but it seems\x01",
            "that each has their own worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHow to overcome them?\x01",
            "...The future holds the\x01",
            "key to that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01703F#12PRixia and Sully are both\x01",
            "worried, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PIlya, any ideas?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01703F#12PI did notice that those two\x01",
            "are worried about something\x01",
            "but...\x02\x03",
            "#01700FTo be honest, I haven't asked\x01",
            "them the details.\x02\x03",
            "#01704FBut well, worries are\x01",
            "something everyone has, some\x01",
            "more than others. Right?\x02\x03",
            "Everyone has their own way of\x01",
            "getting through them too...\x01",
            "It's not my place to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PHaha. You're quite harsh, or\x01",
            "should I say... In a way,\x01",
            "that's very like you, Ilya.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01700F#12PHuhu. I have faith that\x01",
            "those two will able to\x01",
            "get through them, though.\x02\x03",
            "#01703FAnd the moment they do,\x01",
            "my greatest rivals will\x01",
            "be born, I'm sure.\x02\x03",
            "#01709FOoh, I'm so excited just\x01",
            "thinking about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThat positivity of\x01",
            "yours... It could be said\x01",
            "to be a kind of talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. I'm a little\x01",
            "jealous.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01702F#12PHuhu. You're welcome.\x02\x03",
            "#01709FEven so, miss. I never\x01",
            "thought you'd show me a\x01",
            "reading like that.\x02\x03",
            "#01700FI don't think it's a skill\x01",
            "mastered in one day... Then,\x01",
            "you've trained somewhere?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    label("loc_C3C5")


    ChrTalk(
        0x16,
        (
            "#5P...A long time ago, I joined a\x01",
            "certain traveling troupe and\x01",
            "performed many kinds of arts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI can do this by\x01",
            "applying them. ...And I\x01",
            "will leave it at that.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Ilya",
        (
            "#01705F#12PA traveling troupe... In\x01",
            "other words, a circus?\x02\x03",
            "#01709FHmm. I would have liked\x01",
            "to see your performance\x01",
            "at least once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PHaha, seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha. Thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_B56F end

    def Function_34_C540(): pass

    label("Function_34_C540")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Rixia\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD4F")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Rixia",
        "#01805F#12PL-Lloyd?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00009F#6PHaha. I never come to\x01",
            "places like this, so I\x01",
            "wanted to try it.\x02\x03",
            "#00000FWe can stop if you don't\x01",
            "want to...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01804F#12PHaha, no.\x02\x03",
            "#01802FYou're right. This could\x01",
            "be interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha, well then...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Rixia",
        "#01801F#12P(...This is...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man,\x01",
            "and a girl whose eyes are\x01",
            "tinged with sorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PTrust between you has\x01",
            "blossomed ever since a\x01",
            "certain incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf that emotion grows, it\x01",
            "is quite possible you will\x01",
            "deepen your relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHowever... For that to happen\x01",
            "the darkness afflicting the\x01",
            "girl's heart must be removed...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PA darkness afflicting\x01",
            "Rixia's heart?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PBeats me... I myself do\x01",
            "not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PI can only read the\x01",
            "impressions I get from the\x01",
            "crystal ball, you see.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01802F#12PUmm, it's probably my concern over\x01",
            "the renewal performance.\x02\x03",
            "#01809FWhether I can dance properly with\x01",
            "Sully during her big moment... I've\x01",
            "been worried about that lately.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6POh, so that's it.\x02\x03",
            "#00003FBut you've been practicing so\x01",
            "hard for all this time... I\x01",
            "think you'll be just fine.\x02\x03",
            "#00009FI was moved by your performance\x01",
            "before... I don't think there's\x01",
            "any need to worry.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        "#01805F#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha, you're good.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        (
            "#5PFor my advice to be\x01",
            "immediately put to use is all\x01",
            "a fortune teller can ask for.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PT-That's not it, Rixia!\x02\x03",
            "That was never my\x01",
            "intention!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01809F#12PHaha, I know.\x02\x03",
            "#01802FThank you, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D418")

    label("loc_CD4F")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWhat do you want to have\x01",
            "read, Rixia?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01805F#12PUmm, can I decide?\x02\x03",
            "#01803FL-Let's see...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01803F#12PThat Shirley I met the\x01",
            "other day while working\x01",
            "on the lost cat case...\x02\x03",
            "#01801FCould you read whether\x01",
            "we're fated to meet\x01",
            "again?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PRixia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf that is all, it is an\x01",
            "easy request.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Rixia",
        "#01801F#12P(...This is...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PYou and the girl named\x01",
            "Shirley...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYou will meet again in\x01",
            "Crossbell. That's the\x01",
            "impression I'm getting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhen it will happen, and in what\x01",
            "kind of situation I do not know...\x01",
            "But that time will definitely come.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01802F#12PI see. Thank you very\x01",
            "much.\x02\x03",
            "#01803F(Bloody Shirley.... As I\x01",
            "feared, I'll have to be\x01",
            "on guard.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWow, I didn't expect that.\x02\x03",
            "You only saw her for a short\x01",
            "time during the Mary case. Are\x01",
            "you that interested in her?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Rixia",
        (
            "#01802F#12PAh, no... It's because I\x01",
            "could think of something else\x01",
            "to have read.\x02\x03",
            "#01804FAnd she's a very sweet girl.\x01",
            "If there's a chance, I'd like\x01",
            "to speak with her again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PH-Hmm... She seemed\x01",
            "quite dangerous to me,\x01",
            "though.\x02\x03",
            "#00006FIn Elie's case, she's\x01",
            "dangerous in a different\x01",
            "way, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Rixia",
        "#01805F#12PElie's case?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PA-Ah, no. Nevermind.\x02\x03",
            "#00003F(I-I just pictured a\x01",
            "amazing scene for a\x01",
            "bit...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha, young lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIf you like, I will read\x01",
            "for you what this man\x01",
            "was thinking.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00012F#6PG-Give me a break,\x01",
            "please!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D418")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_C540 end

    def Function_35_D424(): pass

    label("Function_35_D424")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhat would you like to have read?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Our compatibility\x01",      # 0
            "Leave it to Sully\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB79")

    ChrTalk(
        0x101,
        (
            "#00000F#6PCould you tell us about\x01",
            "our compatibility?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PAn easy task.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14011F#12PH-Hey! What the hell are\x01",
            "you thinking!?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00005F#6PHuh? Are you that flustered about\x01",
            "it?\x02\x03",
            "#00009FWe're not together that often, so I\x01",
            "wanted take this chance to read\x01",
            "whether our friendship will deepen.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14006F#12P(Is it normal to say\x01",
            "that stuff to someone's\x01",
            "face!?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha. What would you\x01",
            "like to do? I am fine\x01",
            "with anything.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000F#12P...Ah, jeez, it's fine\x01",
            "already. Just do your\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PYes, well then...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        "#14005F#12P(...W-What the...?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn honest-eyed young man\x01",
            "and a girl with hidden\x01",
            "potential...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D877")

    ChrTalk(
        0x16,
        (
            "#5PYour meeting could not have been\x01",
            "worse, but the girl seems to\x01",
            "have noticed the man's kindness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8BC")

    label("loc_D877")


    ChrTalk(
        0x16,
        (
            "#5PThe girl seems to have\x01",
            "noticed the man's\x01",
            "boundless kindness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8BC")


    ChrTalk(
        0x16,
        (
            "#5PIf an honest heart blossoms with the\x01",
            "passage of time, your relationship could\x01",
            "become that of brother and sister...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I am\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14011F#12PW-W-W-W-W-Wh... What's\x01",
            "with that reading!?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PHaha, indeed. It's a\x01",
            "little embarrassing.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14006F#12P"A little embarrassing"\x01",
            "doesn't even begin to cover\x01",
            "it!\x02\x03",
            "#14012FWhy do I have to be in a\x01",
            "brother-sister relationship\x01",
            "with a guy like him!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHaha... You seem to get\x01",
            "along quite well even\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x0)
    OP_63(0x15, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        "#14011F#12PW-We don't!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P(Haha. She's not fooling\x01",
            "anyone, huh.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E431")

    label("loc_DB79")

    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        (
            "#00000F#6PWhat would you like to\x01",
            "have read, Sully?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x15, 0x1)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14005F#12PHuh, can I decide?\x02\x03",
            "#14003FHmm...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x15, 0x0)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14003F#12PThen let me ask you this...\x02\x03",
            "#14000FIn the future, will I be able to\x01",
            "properly perform my role in Arc-en-\x01",
            "Ciel? ...Can you read that for me?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PSully?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14008F#12PI mean, if there's a\x01",
            "good result, then...\x02\x03",
            "#14008FI'll never have to go\x01",
            "back to slums like that\x01",
            "for sure, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P...Very well, I will\x01",
            "read that for you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x16,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 23)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x15, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(
        0x15,
        "Sully",
        "#14005F#12P(...W-What the...?)\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5P...It seems the path on\x01",
            "which you walk branches\x01",
            "in many directions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWill you continue chasing your\x01",
            "dreams, or suffer setbacks and\x01",
            "return from whence you came...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFate has not yet decided\x01",
            "this question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAt the present time, I cannot\x01",
            "say for certain whether it\x01",
            "will be all right.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x101, 3, 0, 24)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x16,
        (
            "#5P...This is what I was\x01",
            "able to see.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x15)

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14003F#12P...I see...\x02\x03",
            "#14008FIf you said "You'll make\x01",
            "it for sure", I would have\x01",
            "felt relieved, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PSully...\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x16)

    ChrTalk(
        0x16,
        (
            "#5PAn acquaintance of mine\x01",
            "was also a kid from the\x01",
            "slums.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        "#14005F#12PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PAround when we met, that\x01",
            "girl's facial expression was\x01",
            "completely desperate, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWe lived together for a\x01",
            "long time and she became\x01",
            "a bright and strong girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PThen, she met an excellent\x01",
            "mentor and now works as a\x01",
            "top-class bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PWhat made that girl grow was,\x01",
            "without a doubt, encounters\x01",
            "with other people.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        "#14005F#12PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PEarlier, I got the impression that\x01",
            "you have already met a certain\x01",
            "person you can respect, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIn that case, the rest is up\x01",
            "to you... That is merely my\x01",
            "personal opinion, though.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x15,
        "Sully",
        (
            "#14000F#12P...Up to me, huh.\x02\x03",
            "#14003FYou might be right. I don't\x01",
            "know if I can ever be as strong\x01",
            "as that bracer lady, but...\x02\x03",
            "#14002FAnyway, for now I'll do the\x01",
            "best I can. Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#5PHaha... You're welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P(Haha... I'm really glad\x01",
            "I invited her.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E431")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_35_D424 end

    def Function_36_E43D(): pass

    label("Function_36_E43D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-7780, -1100, 4820, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x101, -3580, 0, 2100, 270)
    SetChrPos(0xEF, -3200, 0, 3370, 270)
    OP_4B(0x18, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00000FAh, found you!\x02",
    )

    CloseMessageWindow()
    OP_9C(0x18, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    OP_93(0x18, 0x5A, 0x1F4)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Eek! You found me☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5450, -1100, 5050, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x18, -3530, 0, 2710, 90)
    SetChrPos(0x101, -1850, 0, 2040, 270)
    SetChrPos(0xEF, -1850, 0, 3400, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you sure are\x01",
            "lucky, mister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "To think you found me\x01",
            "twice in a row. That's\x01",
            "pretty good!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FI-Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, that was just\x01",
            "a little test.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "You won't be that lucky\x01",
            "so many times in a row!☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E687():

        label("loc_E687")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_E687")

    QueueWorkItem2(0x101, 1, lambda_E687)

    def lambda_E699():

        label("loc_E699")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_E699")

    QueueWorkItem2(0xEF, 1, lambda_E699)
    SetChrFlags(0x18, 0x1000)
    OP_95(0x18, -3310, 0, 340, 5000, 0x0)
    OP_95(0x18, -240, 0, -2920, 5000, 0x0)

    def lambda_E6D8():
        OP_95(0xFE, -80, 0, -8710, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_E6D8)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(310, 1200, -870, 0)
    MoveCamera(323, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14850, 0)
    SetChrPos(0x101, -780, 0, 180, 180)
    SetChrPos(0xEF, 850, 0, 160, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_E7C7")

    ChrTalk(
        0x102,
        (
            "#00105F...And there she went.\x02\x03",
            "#00104FShe was easier to find\x01",
            "than I thought,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_E7C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_E82A")

    ChrTalk(
        0x103,
        (
            "#00205FAnd... she's gone.\x02\x03",
            "#00204FShe was easier to find\x01",
            "than I thought, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_E82A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_E88F")

    ChrTalk(
        0x104,
        (
            "#00305FThere she went, huh.\x02\x03",
            "#00304FShe was easier to find\x01",
            "than I thought, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_E88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_E8F6")

    ChrTalk(
        0x109,
        (
            "#10105FThere she went, eh?\x02\x03",
            "#10104FShe was easier to find\x01",
            "than I thought,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_E8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_E95F")

    ChrTalk(
        0x105,
        (
            "#10304FHehe, there she went.\x02\x03",
            "#10302FShe was easier to find\x01",
            "than I thought,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_E95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_E9AD")

    ChrTalk(
        0x153,
        (
            "#01105FThere she wentー\x02\x03",
            "#01102FShe was easy to find,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_E9AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_EA13")

    ChrTalk(
        0x156,
        (
            "#06405FThere she went, huh.\x02\x03",
            "#06404FShe was easier to find\x01",
            "than I thought, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_EA13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_EA76")

    ChrTalk(
        0x14C,
        (
            "#05905FThere she went.\x02\x03",
            "#05904FShe was easier to find\x01",
            "than I thought,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_EA76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_EADB")

    ChrTalk(
        0x134,
        (
            "#01705FSeems she's gone.\x02\x03",
            "#01706FShe was easier to find\x01",
            "than I thought,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_EADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_EB42")

    ChrTalk(
        0x135,
        (
            "#01805FThere she went, eh?\x02\x03",
            "#01803FShe was easier to find\x01",
            "than I thought,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB9C")

    label("loc_EB42")


    ChrTalk(
        0x166,
        (
            "#14005FThere she went, huh.\x02\x03",
            "#14006FShe was easier to find\x01",
            "than I thought,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_EC33")

    ChrTalk(
        0x101,
        (
            "#00003FY-Yeah. Maybe she just\x01",
            "loves hide and seek and\x01",
            "isn't good at it...\x02\x03",
            "#00000FAnyway, let's keep up\x01",
            "this pace and look for\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ECC2")

    label("loc_EC33")


    ChrTalk(
        0x101,
        (
            "#00003FY-Yeah. Maybe she just\x01",
            "loves hide and seek and\x01",
            "isn't good at it...\x02\x03",
            "#00000FAnyway, let's keep up\x01",
            "this pace and and find\x01",
            "her again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECC2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xB)
    SetScenarioFlags(0x1C9, 3)
    OP_65(0x0, 0x1)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x0, 130, 0, -70, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_E43D end

    def Function_37_ECF7(): pass

    label("Function_37_ECF7")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　 ～Fortune-telling House～ 　　\x01",
            "We predict your fortune concerning\x01",
            "love, finance and other subjects.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_37_ECF7 end

    def Function_38_ED7F(): pass

    label("Function_38_ED7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE9F")
    EventBegin(0x1)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xF,
        (
            "Welcome to the Fortune\x01",
            "House.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Here, you can have\x01",
            "anything read by our\x01",
            "master fortune teller!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(I'm playing hide-and-seek with\x01",
            "Mishette... I'll refrain from\x01",
            "visiting the attractions for now.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -70, 0, 4080, 180)
    OP_4C(0xF, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    EventEnd(0x4)
    Jump("loc_EEA2")

    label("loc_EE9F")

    Call(0, 18)

    label("loc_EEA2")

    Return()

    # Function_38_ED7F end

    SaveToFile()

Try(main)
