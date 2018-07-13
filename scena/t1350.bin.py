from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1350.bin",                # FileName
        "t1350",                    # MapName
        "t1350",                    # Location
        0x00B8,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 184, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1350",                  # 0
        "Elie",                   # 1
        "Tio",                    # 2
        "Randy",                  # 3
        "KeA",                    # 4
        "Fran",                   # 5
        "Ilya",                   # 6
        "Rixia",                  # 7
        "Sully",                  # 8
        "Melson",                 # 9
        "Corona",                 # 10
        "Rimah",                  # 11
        "M. W. L. Staff",         # 12
        "Tourist",                # 13
        "Tourist",                # 14
        "Tourist",                # 15
        "Tourist",                # 16
        "Dummy",                  # 17
        "Miichie",                # 18
        "To Wonderland Entrance", # 19
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch00300.itc",                   # 02
        "chr/ch08200.itc",                   # 03
        "chr/ch08500.itc",                   # 04
        "chr/ch05100.itc",                   # 05
        "chr/ch05200.itc",                   # 06
        "chr/ch10100.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch22700.itc",                   # 09
        "chr/ch20700.itc",                   # 0A
        "chr/ch25900.itc",                   # 0B
        "chr/ch20400.itc",                   # 0C
        "chr/ch23700.itc",                   # 0D
        "chr/ch21000.itc",                   # 0E
        "chr/ch24600.itc",                   # 0F
        "chr/ch45400.itc",                   # 10
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

    DeclNpc(4294965796, 0,       4294964997, 270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294964697, 0,       4294957996, 350,  389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294964796, 0,       4294964997, 90,   389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294964386, 0,       4294962827, 45,   389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294965627, 0,       4294957977, 350,  389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294964366, 0,       4294963266, 270,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4294965247, 0,       4294962427, 315,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4294965537, 0,       4294962827, 315,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294964386, 0,       4294964027, 135,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294965537, 0,       4294964027, 225,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294964987, 0,       4294962827, 0,    389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       800,     2250,    180,  389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294965747, 4294963296, 4294942956, 90,   389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4294966746, 4294963296, 4294942956, 270,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3019,    0,       4294962856, 125,  389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(3670,    0,       4294962077, 305,  389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294961296, 0,       4294964126, 270,  389,  0x0, 0,   16,  0,   0,   0,   0,   25,  255,  0)

    DeclActor(4294961676, 0,       2730,    1200,    4294961676, 2000,    2730,    0x007C, 0,  26, 0x0000)

    PlaceName(-0.17000000178813934, 0.0, -65.44999694824219, 0x0000, 0x0000, "To Wonderland Entrance")

    ChipFrameInfo(936, 0)                                        # 0

    ScpFunction((
        "Function_0_3A8",          # 00, 0
        "Function_1_460",          # 01, 1
        "Function_2_4F1",          # 02, 2
        "Function_3_531",          # 03, 3
        "Function_4_61E",          # 04, 4
        "Function_5_713",          # 05, 5
        "Function_6_7FB",          # 06, 6
        "Function_7_8F4",          # 07, 7
        "Function_8_A23",          # 08, 8
        "Function_9_BD8",          # 09, 9
        "Function_10_D3A",         # 0A, 10
        "Function_11_DD9",         # 0B, 11
        "Function_12_EAF",         # 0C, 12
        "Function_13_F3D",         # 0D, 13
        "Function_14_FF8",         # 0E, 14
        "Function_15_1162",        # 0F, 15
        "Function_16_1258",        # 10, 16
        "Function_17_1374",        # 11, 17
        "Function_18_13E8",        # 12, 18
        "Function_19_14A6",        # 13, 19
        "Function_20_153E",        # 14, 20
        "Function_21_169D",        # 15, 21
        "Function_22_2D32",        # 16, 22
        "Function_23_2D5B",        # 17, 23
        "Function_24_2D84",        # 18, 24
        "Function_25_3D1D",        # 19, 25
        "Function_26_4425",        # 1A, 26
    ))


    def Function_0_3A8(): pass

    label("Function_0_3A8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3E8"),
        (1, "loc_3F4"),
        (2, "loc_400"),
        (3, "loc_40C"),
        (4, "loc_418"),
        (5, "loc_424"),
        (6, "loc_430"),
        (SWITCH_DEFAULT, "loc_43C"),
    )


    label("loc_3E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_3F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_400")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_40C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_418")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_424")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_430")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_43C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_448")

    label("loc_45F")

    Return()

    # Function_0_3A8 end

    def Function_1_460(): pass

    label("Function_1_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_46F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_47D")
    Jump("loc_4F0")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_48B")
    Jump("loc_4F0")

    label("loc_48B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_499")
    Jump("loc_4F0")

    label("loc_499")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4AA")
    Call(0, 20)
    Jump("loc_4F0")

    label("loc_4AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4BD")
    ClearChrFlags(0x13, 0x80)
    Jump("loc_4F0")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4CB")
    Jump("loc_4F0")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_4F0")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4E7")
    Jump("loc_4F0")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_4F0")

    label("loc_4F0")

    Return()

    # Function_1_460 end

    def Function_2_4F1(): pass

    label("Function_2_4F1")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)

    label("loc_52A")

    Sound(944, 0, 100, 0)
    Return()

    # Function_2_4F1 end

    def Function_3_531(): pass

    label("Function_3_531")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54A")
    Jump("loc_61A")

    label("loc_54A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D")
    Call(0, 19)
    Jump("loc_5D8")

    label("loc_56D")


    ChrTalk(
        0x8,
        (
            "#00106F*haah*...\x01",
            "I'm not good with things like this.\x02\x03",
            "#00111FMaybe Bell built it\x01",
            "only to scare me...\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D8")

    Jump("loc_61A")

    label("loc_5DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F3")
    Jump("loc_61A")

    label("loc_5F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_609")
    Jump("loc_61A")

    label("loc_609")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61A")

    label("loc_61A")

    TalkEnd(0xFE)
    Return()

    # Function_3_531 end

    def Function_4_61E(): pass

    label("Function_4_61E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_637")
    Jump("loc_70F")

    label("loc_637")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64D")
    Jump("loc_70F")

    label("loc_64D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_663")
    Jump("loc_70F")

    label("loc_663")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FE")

    ChrTalk(
        0x9,
        (
            "#00203FEven from here, you can clearly\x01",
            "hear screams and shrieks.\x02\x03",
            "#00204FHearing those is scary, but\x01",
            "exciting at the same time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70F")

    label("loc_6FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70F")

    label("loc_70F")

    TalkEnd(0xFE)
    Return()

    # Function_4_61E end

    def Function_5_713(): pass

    label("Function_5_713")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    Jump("loc_7F7")

    label("loc_72C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74F")
    Call(0, 19)
    Jump("loc_7B5")

    label("loc_74F")


    ChrTalk(
        0xA,
        (
            "#00309FHa ha, milady is a scaredy cat.\x02\x03",
            "#00304FWell, this is the stuff I\x01",
            "like to have a ride on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B5")

    Jump("loc_7F7")

    label("loc_7BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D0")
    Jump("loc_7F7")

    label("loc_7D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E6")
    Jump("loc_7F7")

    label("loc_7E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F7")

    label("loc_7F7")

    TalkEnd(0xFE)
    Return()

    # Function_5_713 end

    def Function_6_7FB(): pass

    label("Function_6_7FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_814")
    Jump("loc_8F0")

    label("loc_814")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82A")
    Jump("loc_8F0")

    label("loc_82A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_840")
    Jump("loc_8F0")

    label("loc_840")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_856")
    Jump("loc_8F0")

    label("loc_856")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F0")

    ChrTalk(
        0xB,
        (
            "#01106FKeA is thinking hard about what could\x01",
            "be a good attraction for last...\x02\x03",
            "#01109FThis seems it would be\x01",
            "fun to ride with Ilya!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F0")

    TalkEnd(0xFE)
    Return()

    # Function_6_7FB end

    def Function_7_8F4(): pass

    label("Function_7_8F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90D")
    Jump("loc_A1F")

    label("loc_90D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_923")
    Jump("loc_A1F")

    label("loc_923")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_939")
    Jump("loc_A1F")

    label("loc_939")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E")

    ChrTalk(
        0xC,
        (
            "#06402FIt seems that the building of this\x01",
            "attraction was a former Michelam's\x01",
            "mansion that the IBC remodeled.\x02\x03",
            "#06409FWoow, they really went all out with this.\x01",
            "Somehow it makes you sigh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1F")

    label("loc_A0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")

    label("loc_A1F")

    TalkEnd(0xFE)
    Return()

    # Function_7_8F4 end

    def Function_8_A23(): pass

    label("Function_8_A23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA8")

    ChrTalk(
        0xD,
        (
            "#01702F*pheeew*♪\x01",
            "What air it gives!\x02\x03",
            "#01709FYes, now I'm excited.\x01",
            "I want to ride it now!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_AE1")

    label("loc_AA8")


    ChrTalk(
        0xD,
        (
            "#01709FYes, now I'm excited.\x01",
            "I want to ride it now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE1")

    Jump("loc_BD4")

    label("loc_AE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFC")
    Jump("loc_BD4")

    label("loc_AFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B12")
    Jump("loc_BD4")

    label("loc_B12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B28")
    Jump("loc_BD4")

    label("loc_B28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD4")

    ChrTalk(
        0xD,
        (
            "#01702FIt's the last one, so might as well\x01",
            "ride a refreshing one, no?\x02\x03",
            "#01700FWith only you, you'd\x01",
            "probably hit the limit,\x01",
            "but with me it'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD4")

    TalkEnd(0xFE)
    Return()

    # Function_8_A23 end

    def Function_9_BD8(): pass

    label("Function_9_BD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8F")

    ChrTalk(
        0xE,
        (
            "#01805FThe one that can be seen over there...\x01",
            "Could it be a course ride?\x01\x02\x03",
            "#01806FGoing outside like that...\x01",
            "It seems it's quite thrilling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CDE")

    label("loc_C8F")


    ChrTalk(
        0xE,
        (
            "#01802FA course going outside\x01",
            "like that...\x01",
            "It seems it's quite thrilling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDE")

    Jump("loc_D36")

    label("loc_CE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF9")
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

    # Function_9_BD8 end

    def Function_10_D3A(): pass

    label("Function_10_D3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D53")
    Jump("loc_DD5")

    label("loc_D53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D69")
    Jump("loc_DD5")

    label("loc_D69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7F")
    Jump("loc_DD5")

    label("loc_D7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D95")
    Jump("loc_DD5")

    label("loc_D95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD5")

    ChrTalk(
        0xF,
        "#14006FHmm, I'm fine with whatever, so...\x02",
    )

    CloseMessageWindow()

    label("loc_DD5")

    TalkEnd(0xFE)
    Return()

    # Function_10_D3A end

    def Function_11_DD9(): pass

    label("Function_11_DD9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF2")
    Jump("loc_EAB")

    label("loc_DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E08")
    Jump("loc_EAB")

    label("loc_E08")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E84")

    ChrTalk(
        0x10,
        (
            "*phew*...\x01",
            "It was incredibly thrilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Still, I'm glad I could make\x01",
            "Rimah have a good time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAB")

    label("loc_E84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9A")
    Jump("loc_EAB")

    label("loc_E9A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAB")

    label("loc_EAB")

    TalkEnd(0xFE)
    Return()

    # Function_11_DD9 end

    def Function_12_EAF(): pass

    label("Function_12_EAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC8")
    Jump("loc_F39")

    label("loc_EC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDE")
    Jump("loc_F39")

    label("loc_EDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F12")

    ChrTalk(
        0x11,
        (
            "Uh uh...\x01",
            "Good job, dear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F39")

    label("loc_F12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F28")
    Jump("loc_F39")

    label("loc_F28")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F39")

    label("loc_F39")

    TalkEnd(0xFE)
    Return()

    # Function_12_EAF end

    def Function_13_F3D(): pass

    label("Function_13_F3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F56")
    Jump("loc_FF4")

    label("loc_F56")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6C")
    Jump("loc_FF4")

    label("loc_F6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCD")

    ChrTalk(
        0x12,
        "Papa was suuuper cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "He took down a lot of\x01",
            "monsters, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF4")

    label("loc_FCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE3")
    Jump("loc_FF4")

    label("loc_FE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF4")

    label("loc_FF4")

    TalkEnd(0xFE)
    Return()

    # Function_13_F3D end

    def Function_14_FF8(): pass

    label("Function_14_FF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_115E")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Welcome to the Horror Coaster,\x01",
            "popularly called the "Lunatic Zone"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a horror attraction where you\x01",
            "run through a mansion where monsters\x01",
            "dwell armed just with one mere orbal gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(I'm playing hide and seek wih Miichie...\x01",
            "I'll refrain from having a good time with\x01",
            "the attractions for now.)\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1161")

    label("loc_115E")

    Call(0, 21)

    label("loc_1161")

    Return()

    # Function_14_FF8 end

    def Function_15_1162(): pass

    label("Function_15_1162")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D0")
    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x14,
        (
            "H-Ha ha h-ha...\x01",
            "N-No way \x01",
            "that's scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "(He's clearly scared...)\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    Jump("loc_1254")

    label("loc_11D0")


    ChrTalk(
        0x14,
        (
            "Riding it time and time again,\x01",
            "I won over what scared me\x01",
            "and it became fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Ha ha ha, come on, let's go for another ride!\x02",
    )

    CloseMessageWindow()

    label("loc_1254")

    TalkEnd(0xFE)
    Return()

    # Function_15_1162 end

    def Function_16_1258(): pass

    label("Function_16_1258")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C3")

    ChrTalk(
        0x15,
        (
            "Are you all right? If you don't like it,\x01",
            "you don't have to force to ride it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1370")

    label("loc_12C3")


    ChrTalk(
        0x15,
        (
            "My boyfriend, he got in high spirits\x01",
            "and now he wants to ride the \x01",
            "Horror Coaster many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "*haah*, but I'd like to\x01",
            "have fun at the any\x01",
            "other attractions too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1370")

    TalkEnd(0xFE)
    Return()

    # Function_16_1258 end

    def Function_17_1374(): pass

    label("Function_17_1374")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E4")

    ChrTalk(
        0x16,
        (
            "Maaan, I screamed and screamed!\x01",
            "Attractions that makes you\x01",
            "scream are really fun!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E4")

    label("loc_13E4")

    TalkEnd(0xFE)
    Return()

    # Function_17_1374 end

    def Function_18_13E8(): pass

    label("Function_18_13E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14A2")

    ChrTalk(
        0x17,
        (
            "That father of mine,\x01",
            "he even forgot to shoot with the gun\x01",
            "and did nothing but screaming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "The next time we ride this,\x01",
            "I'll be the one shooting the gun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A2")

    label("loc_14A2")

    TalkEnd(0xFE)
    Return()

    # Function_18_13E8 end

    def Function_19_14A6(): pass

    label("Function_19_14A6")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "#00309FAlright, milady.\x01",
            "Let's get inside now♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00106FW-Wait a moment.\x01",
            "Let me mentally prepare a little more...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_19_14A6 end

    def Function_20_153E(): pass

    label("Function_20_153E")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1586")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_169C")

    label("loc_1586")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B0")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    Jump("loc_169C")

    label("loc_15B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15DA")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_169C")

    label("loc_15DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1652")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_1624")
    SetChrFlags(0x9, 0x80)
    Jump("loc_1632")

    label("loc_1624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_1632")
    SetChrFlags(0xC, 0x80)

    label("loc_1632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_164D")
    ClearChrFlags(0x19, 0x80)

    label("loc_164D")

    Jump("loc_169C")

    label("loc_1652")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169C")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2310, 0, -3270, 180)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_169C")

    Return()

    # Function_20_153E end

    def Function_21_169D(): pass

    label("Function_21_169D")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1800, 1650, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(10500, 0)
    OP_4B(0x13, 0xFF)
    SetChrPos(0x101, 0, 800, 1000, 0)
    Call(0, 22)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "Welcome to the Horror Coaster,\x01",
            "popularly called the "Lunatic Zone"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "This is a horror attraction where you\x01",
            "run through a mansion where monsters\x01",
            "dwell armed just with one mere orbal gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I suggest you to enter together\x01",
            "with someone, if you want...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P(...Who should I invite?)\x02",
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
    MenuCmd(1, 0, "Quit")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18D4")
    MenuCmd(3, 0, 0x0)

    label("loc_18D4")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18E6")
    MenuCmd(3, 0, 0x1)

    label("loc_18E6")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18F8")
    MenuCmd(3, 0, 0x2)

    label("loc_18F8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_190A")
    MenuCmd(3, 0, 0x3)

    label("loc_190A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_191C")
    MenuCmd(3, 0, 0x4)

    label("loc_191C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_192E")
    MenuCmd(3, 0, 0x5)

    label("loc_192E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1940")
    MenuCmd(3, 0, 0x6)

    label("loc_1940")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1952")
    MenuCmd(3, 0, 0x7)

    label("loc_1952")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1964")
    MenuCmd(3, 0, 0x8)

    label("loc_1964")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1976")
    MenuCmd(3, 0, 0x9)

    label("loc_1976")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1988")
    MenuCmd(3, 0, 0xA)

    label("loc_1988")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CC9")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A0E"),
        (1, "loc_1B8D"),
        (2, "loc_1D03"),
        (3, "loc_1ED9"),
        (4, "loc_202C"),
        (5, "loc_21AE"),
        (6, "loc_2352"),
        (7, "loc_24E1"),
        (8, "loc_2680"),
        (9, "loc_2806"),
        (10, "loc_2959"),
        (SWITCH_DEFAULT, "loc_2AF8"),
    )


    label("loc_1A0E")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Elie.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x18,
        "Elie",
        (
            "#00106F#6PThe Horror Coaster...\x01",
            "Uuh, we're really going in?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PHa ha, I'll be with you,\x01",
            "so don't worry.\x02\x03",
            "#00002FI'll escort you\x01",
            "properly.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Elie",
        "#00100F#12PYes, I'm counting on that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_1B8D")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Tio.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Tio",
        (
            "#00204F#6PThe rumored new attraction...\x01",
            "I am looking forward a little to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PIt seems a little scary one,\x01",
            "but you seem fine, Tio.\x02\x03",
            "#00000FDo you want to go inside now?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Tio",
        "#00200F#12PYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_1D03")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Randy.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x2)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D8B")
    SetChrFlags(0xA, 0x8)

    label("loc_1D8B")

    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Randy",
        (
            "#00303F#6PUhhm, the horror genre is an\x01",
            "established tactic with the purpose\x01",
            "to enter the attraction with a girl.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#5PHa ha, well, even if we're two men,\x01",
            "it could be fun, you know.\x02\x03",
            "#00000FLet's enter now.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Randy",
        (
            "#00300F#12PWell, since we came here,\x01",
            "I guess I'll keep you company.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_1ED9")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Noｱl.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Noｱl",
        (
            "#10100F#6PA monsters extermination...\x01",
            "Somehow I'm on fire!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00009F#5PHa ha, you're really into it, eh?\x02\x03",
            "#00000FThen, should we enter?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Noｱl",
        "#10100F#12PYes, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_202C")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Wazy.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch03000.itc", 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Wazy",
        (
            "#10304F#6PThe Horror Coaster, eh...?\x01",
            "Hu hu, should I embrace you\x01",
            "while you're screaming?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#5PDon't expect that.\x02\x03",
            "#00000FWell, whatever, let's enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Wazy",
        "#10300F#12PHu hu, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_21AE")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite KeA.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x3)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x18, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    NpcTalk(
        0x18,
        "KeA",
        (
            "#01109F#6PDo ghosts come out here?\x01",
            "So exciting, I really can't wait!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00012F#5PHa ha, as you can imagine, \x01",
            "I don't think real ones will come out...\x01",
            "I think we can enjoy the mood.\x02\x03",
            "#00000FThen, let's enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "KeA",
        "#01109F#12PLet's gooo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_2352")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Fran.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x4)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Fran",
        (
            "#06409F#6PThe rumored new attraction...\x01",
            "My heart is racing!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PHa ha, although it's one from the\x01",
            "horror genre, you seem a lot into it.\x02\x03",
            "#00000FAlright, time to enter then.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Fran",
        "#06400F#12PUh uh, please take good care of me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_24E1")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite sister Cecil.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch07500.itc", 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Cecil",
        (
            "#05902F#6PThe rumored new attraction, eh?\x01",
            "Uh uh, I can't wait.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#5PHa ha, it's horror themed, \x01",
            "but you look completely calm.\x02\x03",
            "#00000FSister Cecil, I'll properly\x01",
            "escort you, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Cecil",
        "#05900F#12PYes, I'm counting on you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_2680")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Miss Ilya.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_270C")
    SetChrFlags(0xD, 0x8)

    label("loc_270C")

    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Ilya",
        (
            "#01709F#6PI was looking forward to\x01",
            "a scream genre one!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00009F#5PHa ha, it indeed seems an attraction\x01",
            "that you would like, Miss Ilya.\x02\x03",
            "#00000FThen, should we go?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Ilya",
        "#01700F#12PYes, let's go at once!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_2806")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Rixia.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x6)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Rixia",
        (
            "#01802F#6PUh uh, it really seems an attraction\x01",
            "with a certain atmosphere.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#5PHa ha, you look perfectly calm.\x02\x03",
            "#00000FThen, should we go in?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Rixia",
        "#01809F#12PYes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_2959")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright...I'll try to invite Sully.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x7)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Sully",
        (
            "#14004F#6PH-Hmph...\x01",
            "It's nothing serious anyway, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PHa ha, who knows?\x01",
            "It could be unexpectedly scary...\x02\x03",
            "#00000FAlright, let's enter then.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x18)
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Sully",
        (
            "#14011F#12PW-Wait a sec.\x01",
            "I've got to mentally prepare myself...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_2AF8")


    ChrTalk(
        0x13,
        "Then, I'll take your ticket.\x02",
    )

    CloseMessageWindow()

    def lambda_2B1F():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B1F)
    Sleep(50)

    def lambda_2B2F():
        OP_93(0x18, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2B2F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x18, 0)
    SubItemNumber(0x35D, 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Handed 1 ticket to the staff.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x13,
        (
            "The orbal gun to defeat the monsters\x01",
            "has been placed inside the vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Hu hu...\x01",
            "Please, come back all in one piece.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x13, 0x0, 0x1F4)
    OP_9B(0x0, 0x13, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(200)
    Sound(121, 0, 100, 0)
    OP_71(0x0, 0x1, 0xA, 0x1, 0x0)
    OP_79(0x0)

    def lambda_2C55():
        OP_98(0xFE, 0xFFFFFA88, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2C55)
    OP_93(0x13, 0x5A, 0x1F4)
    WaitChrThread(0x13, 1)
    Sleep(300)
    FadeToDark(1000, 0, -1)

    def lambda_2C87():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2C87)
    Sleep(50)

    def lambda_2C9F():
        OP_9B(0x0, 0x18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2C9F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x18, 0)
    OP_0D()
    NewScene("t1360", 0, 0, 0)
    IdleLoop()
    Jump("loc_2D17")

    label("loc_2CC9")


    ChrTalk(
        0x13,
        "Hu hu, you aren't going inside?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "We will await\x01",
            "your next visit...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2D17")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 400, -350, 180)
    EventEnd(0x5)
    Return()

    # Function_21_169D end

    def Function_22_2D32(): pass

    label("Function_22_2D32")

    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xF, 0x8)
    Return()

    # Function_22_2D32 end

    def Function_23_2D5B(): pass

    label("Function_23_2D5B")

    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xF, 0x8)
    Return()

    # Function_23_2D5B end

    def Function_24_2D84(): pass

    label("Function_24_2D84")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("chr/ch03000.itc", 0x1F)
    LoadChrToIndex("chr/ch07500.itc", 0x20)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x18, 0x80)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2DF6"),
        (1, "loc_2DFF"),
        (2, "loc_2E08"),
        (3, "loc_2E11"),
        (4, "loc_2E1A"),
        (5, "loc_2E23"),
        (6, "loc_2E2C"),
        (7, "loc_2E35"),
        (8, "loc_2E3E"),
        (9, "loc_2E47"),
        (10, "loc_2E50"),
        (SWITCH_DEFAULT, "loc_2E59"),
    )


    label("loc_2DF6")

    SetChrChipByIndex(0x18, 0x0)
    Jump("loc_2E59")

    label("loc_2DFF")

    SetChrChipByIndex(0x18, 0x1)
    Jump("loc_2E59")

    label("loc_2E08")

    SetChrChipByIndex(0x18, 0x2)
    Jump("loc_2E59")

    label("loc_2E11")

    SetChrChipByIndex(0x18, 0x1E)
    Jump("loc_2E59")

    label("loc_2E1A")

    SetChrChipByIndex(0x18, 0x1F)
    Jump("loc_2E59")

    label("loc_2E23")

    SetChrChipByIndex(0x18, 0x3)
    Jump("loc_2E59")

    label("loc_2E2C")

    SetChrChipByIndex(0x18, 0x4)
    Jump("loc_2E59")

    label("loc_2E35")

    SetChrChipByIndex(0x18, 0x20)
    Jump("loc_2E59")

    label("loc_2E3E")

    SetChrChipByIndex(0x18, 0x5)
    Jump("loc_2E59")

    label("loc_2E47")

    SetChrChipByIndex(0x18, 0x6)
    Jump("loc_2E59")

    label("loc_2E50")

    SetChrChipByIndex(0x18, 0x7)
    Jump("loc_2E59")

    label("loc_2E59")

    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x4)
    SetChrPos(0x101, -600, 800, 1000, 90)
    SetChrPos(0x18, 600, 800, 1000, 270)
    Call(0, 22)
    OP_68(0, 1800, 1650, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(11500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(10500, 2500)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2F15"),
        (1, "loc_304F"),
        (2, "loc_3170"),
        (3, "loc_3299"),
        (4, "loc_33AC"),
        (5, "loc_34AD"),
        (6, "loc_35B3"),
        (7, "loc_36CF"),
        (8, "loc_37FF"),
        (9, "loc_3936"),
        (10, "loc_3A5F"),
        (SWITCH_DEFAULT, "loc_3BA7"),
    )


    label("loc_2F15")


    NpcTalk(
        0x18,
        "Elie",
        (
            "#00106F#12P*haah*... To think the monsters\x01",
            "were coming so close...\x01",
            "How scary.\x02\x03",
            "#00100F*giggle*, well, it wasn't\x01",
            "as scary as I thought,\x01",
            "so it's true that I had fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, if you had fun,\x01",
            "then I'm happy I invited you.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Elie",
        "#00100F#12PYes, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_304F")


    NpcTalk(
        0x18,
        "Tio",
        (
            "#00204F#12PMonsters that draw near...\x01",
            "I had quite a thrill.\x02\x03",
            "#00200FAs expected from a new attraction.\x01",
            "Even the fact it is very popular is convincing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, it seems you had fun.\x01",
            "I'm happy about it.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Tio",
        "#00200F#12PYes, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_3170")


    NpcTalk(
        0x18,
        "Randy",
        (
            "#00300F#12PHa ha, though it's horror themed,\x01",
            "it was quite well made, huh?\x02\x03",
            "#00306FThough it was a bit disappointin' that my\x01",
            "partner was you and not a pretty lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FW-Well, it was fun,\x01",
            "so it's alright, eh?\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Randy",
        "#00300F#12PYeah, laters.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_3299")


    NpcTalk(
        0x18,
        "Noｱl",
        (
            "#10100F#12P*phew*, it was really fun.\x02\x03",
            "#10109FIf training shooting at the CGF\x01",
            "was like this kind of game, \x01",
            "I feel we'd quite improve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, true...\x01",
            "Maybe that time will come one day.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Noｱl",
        "#10100F#12PYes, see you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_33AC")


    NpcTalk(
        0x18,
        "Wazy",
        (
            "#10304F#12PHu hu, it was quite the\x01",
            "massive attraction, eh?\x02\x03",
            "#10302FEven someone like me\x01",
            "was quite absorbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FI ended up being enthusiast too...\x01",
            "I'm happy you had fun.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Wazy",
        "#10300F#12PHu hu, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_34AD")


    NpcTalk(
        0x18,
        "KeA",
        (
            "#01109F#12PWhooah, it was fuuun!\x02\x03",
            "Running through total darkness,\x01",
            "the wind hitting your face...\x01",
            "It felt really good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, if you had\x01",
            "that much fun, I'm\x01",
            "happy I invited you.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "KeA",
        "#01100F#12PYes, later!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_35B3")


    NpcTalk(
        0x18,
        "Fran",
        (
            "#06400F#12P*haah*, it was the perfect thrill!\x02\x03",
            "#06409FIt really helped that\x01",
            "Mr. Lloyd did his\x01",
            "best at shooting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FIt was quite tough against\x01",
            "that number of enemies, but...\x01",
            "I'm happy you had fun.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Fran",
        "#06400F#12PYes, lateeer.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_36CF")


    NpcTalk(
        0x18,
        "Cecil",
        (
            "#05900F#12PUh uh, it was really fun.\x02\x03",
            "#05909FAnd Lloyd's shooting figure\x01",
            "was quite reliable too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, although handling a real gun is\x01",
            "totally different as you can imagine...\x01",
            "Well, I'm happy you had fun.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Cecil",
        "#05900F#12PYes, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_37FF")


    NpcTalk(
        0x18,
        "Ilya",
        (
            "#01704F#12PYeees, this was the attraction\x01",
            "I was expecting to be!\x02\x03",
            "#01702FUh uh, although I'd have preferred\x01",
            "that many more monsters came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FI-I think that would've been\x01",
            "really too tough...\x01",
            "Well, I'm happy you had fun.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Ilya",
        "#01700F#12PYes, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_3936")


    NpcTalk(
        0x18,
        "Rixia",
        (
            "#01802F#12P*haah*, it was quite fun.\x02\x03",
            "#01806FIt seems that Mr. Lloyd had it\x01",
            "very tough shooting the monsters\x01",
            "who were hectically moving around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, it was a little tough,\x01",
            "but I had a lot of fun too.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Rixia",
        "#01802F#12PYes, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_3A5F")


    NpcTalk(
        0x18,
        "Sully",
        (
            "#14006F#12P*haah*...the ride was fast and I\x01",
            "couldn't open my eyes at all,\x01",
            "but the thrill was quite something.\x02\x03",
            "#14002FEven so, it seems you had fun.\x01",
            "I wanted to shoot too, you know.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha...despite the appearances,\x01",
            "it was quite hard.\x02\x03",
            "#00000FThen, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Sully",
        "#14000F#12PHm, bye then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA7")

    label("loc_3BA7")


    def lambda_3BAC():

        label("loc_3BAC")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_3BAC")

    QueueWorkItem2(0x101, 2, lambda_3BAC)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_3BC5():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3BC5)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x18, 1)
    EndChrThread(0x101, 0x2)
    SetChrFlags(0x18, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3C42"),
        (1, "loc_3C50"),
        (2, "loc_3C5E"),
        (3, "loc_3C6C"),
        (4, "loc_3C7A"),
        (5, "loc_3C88"),
        (6, "loc_3C96"),
        (7, "loc_3CA4"),
        (8, "loc_3CB2"),
        (9, "loc_3CC0"),
        (10, "loc_3CCE"),
        (SWITCH_DEFAULT, "loc_3CDC"),
    )


    label("loc_3C42")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3C50")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3C5E")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3C6C")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3C7A")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3C88")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3C96")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3CA4")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3CB2")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3CC0")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3CCE")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3CDC")

    label("loc_3CDC")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D02")
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_3D02")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 0, -2000, 180)
    EventEnd(0x5)
    Return()

    # Function_24_2D84 end

    def Function_25_3D1D(): pass

    label("Function_25_3D1D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3070, 2300, -4040, 0)
    MoveCamera(310, 39, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(8910, 0)
    SetChrPos(0x101, -2970, 0, -3760, 270)
    SetChrPos(0xEF, -2050, 0, -2510, 270)
    OP_4B(0x19, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00002FFound you!\x02",
    )

    CloseMessageWindow()
    OP_9C(0x19, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    OP_93(0x19, 0x5A, 0x1F4)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Eek! You found me☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-630, 2300, -4310, 0)
    MoveCamera(330, 32, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(8910, 0)
    SetChrPos(0x19, -2930, 0, -3100, 90)
    SetChrPos(0x101, -1440, 0, -4040, 270)
    SetChrPos(0xEF, -940, 0, -2450, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Jeez, to think you could find\x01",
            "me so fast for four times too...\x01",
            "Unbelievable.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you're totally different\x01",
            "from my slow big brother, Michey,\x01",
            "you know?☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_3F5C")
    OP_63(0x153, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_3F74")

    label("loc_3F5C")

    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3F74")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Miichie is really severe\x01",
            "with Michey, eh...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "...Mrr, the next time is going to be the last.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Alright, as the last one, I'll hide into a more\x01",
            "difficult place, so do your best and find me!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4056():

        label("loc_4056")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4056")

    QueueWorkItem2(0x101, 1, lambda_4056)

    def lambda_4068():

        label("loc_4068")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4068")

    QueueWorkItem2(0xEF, 1, lambda_4068)
    SetChrFlags(0x19, 0x1000)
    OP_95(0x19, -1430, 0, -8620, 4000, 0x0)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(2740, 4000, -15010, 0)
    MoveCamera(322, 28, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(8039, 0)
    SetChrPos(0x101, -430, 0, -11830, 180)
    SetChrPos(0xEF, 960, 0, -11900, 180)
    SetChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00006FFinally, the last hiding place, eh...?\x02\x03",
            "#00000FBecause it's only inside the theme park,\x01",
            "I don't think it'll be that much difficult...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_41CC")

    ChrTalk(
        0x102,
        (
            "#00100FThen, let's go\x01",
            "look for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_41CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_4203")

    ChrTalk(
        0x103,
        (
            "#00200FThen, let's go\x01",
            "look for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_4203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_423E")

    ChrTalk(
        0x104,
        (
            "#00300FThen, let's go\x01",
            "look for her, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_423E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4275")

    ChrTalk(
        0x109,
        (
            "#10100FThen, let's go\x01",
            "look for her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_4275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_42B0")

    ChrTalk(
        0x105,
        (
            "#10300FThen, let's go\x01",
            "look for her, hm?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_42B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_42E4")

    ChrTalk(
        0x153,
        "#01100FThen, let's go searching!\x02",
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_42E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_431D")

    ChrTalk(
        0x156,
        (
            "#06400FThen, let's go\x01",
            "look for heeer!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_431D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_435D")

    ChrTalk(
        0x14C,
        (
            "#05900FUh uh, then, let's go\x01",
            "search for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_435D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_439B")

    ChrTalk(
        0x134,
        (
            "#01700FUh uh, then, let's go\x01",
            "look for her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_439B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_43D2")

    ChrTalk(
        0x135,
        (
            "#01802FThen, let's go\x01",
            "look for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43F9")

    label("loc_43D2")


    ChrTalk(
        0x166,
        (
            "#14000FSo, let's go\x01",
            "look for her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xE)
    SetScenarioFlags(0x1C9, 6)
    SetChrPos(0x0, 160, 0, -12030, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_3D1D end

    def Function_26_4425(): pass

    label("Function_26_4425")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a sketch map\x01",
            "of the theme park.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_26_4425 end

    SaveToFile()

Try(main)
