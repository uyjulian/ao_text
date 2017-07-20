from ScenarioHelper import *

def main():
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
        "Erie",                 # 1
        "Tio",                 # 2
        "Randy",               # 3
        "Keya",                 # 4
        "Franc",                 # 5
        "Ilia",                 # 6
        "Lisha",               # 7
        "Shuri",                 # 8
        "Marsun",               # 9
        "corona",                 # 10
        "Lima",                   # 11
        "MWL staff",         # 12
        "tourist",                 # 13
        "tourist",                 # 14
        "tourist",                 # 15
        "tourist",                 # 16
        "dummy",                 # 17
        "Misee",               # 18
        "Directions to Wonderland entrance square",# 19
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

    PlaceName(-0.17000000178813934, 0.0, -65.44999694824219, 0x0000, 0x0000, "Directions to Wonderland entrance square")

    ChipFrameInfo(936, 0)                                        # 0

    ScpFunction((
        "Function_0_3A8",          # 00, 0
        "Function_1_460",          # 01, 1
        "Function_2_4F1",          # 02, 2
        "Function_3_531",          # 03, 3
        "Function_4_624",          # 04, 4
        "Function_5_716",          # 05, 5
        "Function_6_7FD",          # 06, 6
        "Function_7_8D3",          # 07, 7
        "Function_8_9F4",          # 08, 8
        "Function_9_BA3",          # 09, 9
        "Function_10_D01",         # 0A, 10
        "Function_11_DA0",         # 0B, 11
        "Function_12_E66",         # 0C, 12
        "Function_13_EF7",         # 0D, 13
        "Function_14_FC4",         # 0E, 14
        "Function_15_1101",        # 0F, 15
        "Function_16_11F4",        # 10, 16
        "Function_17_12E0",        # 11, 17
        "Function_18_1347",        # 12, 18
        "Function_19_13DB",        # 13, 19
        "Function_20_146B",        # 14, 20
        "Function_21_15CA",        # 15, 21
        "Function_22_2B94",        # 16, 22
        "Function_23_2BBD",        # 17, 23
        "Function_24_2BE6",        # 18, 24
        "Function_25_3B44",        # 19, 25
        "Function_26_4228",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)

    label("loc_52A")

    Sound(944, 0, 100, 0)
    Return()

    # Function_2_4F1 end

    def Function_3_531(): pass

    label("Function_3_531")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54A")
    Jump("loc_620")

    label("loc_54A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D")
    Call(0, 19)
    Jump("loc_5DE")

    label("loc_56D")


    ChrTalk(
        0x8,
        (
            "#00106FHa\x01",
            "It is not good for you, is not it?\x02\x03",
            "#00111FMaybe\x01",
            "Just for Bell to threaten me\x01",
            "Maybe I made it ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DE")

    Jump("loc_620")

    label("loc_5E3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_620")

    label("loc_5F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60F")
    Jump("loc_620")

    label("loc_60F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_620")

    label("loc_620")

    TalkEnd(0xFE)
    Return()

    # Function_3_531 end

    def Function_4_624(): pass

    label("Function_4_624")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63D")
    Jump("loc_712")

    label("loc_63D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_653")
    Jump("loc_712")

    label("loc_653")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_669")
    Jump("loc_712")

    label("loc_669")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_701")

    ChrTalk(
        0x9,
        (
            "#00203FEven from here, screaming and screaming\x01",
            "You hear clearly.\x02\x03",
            "#00204FListening to that,\x01",
            "I'm scared and excited at the same time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_712")

    label("loc_701")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_712")

    label("loc_712")

    TalkEnd(0xFE)
    Return()

    # Function_4_624 end

    def Function_5_716(): pass

    label("Function_5_716")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72F")
    Jump("loc_7F9")

    label("loc_72F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_752")
    Call(0, 19)
    Jump("loc_7B7")

    label("loc_752")


    ChrTalk(
        0xA,
        (
            "#00309FHa ha, she is also afraid.\x02\x03",
            "#00304FWell, like this type\x01",
            "I want to try it on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B7")

    Jump("loc_7F9")

    label("loc_7BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D2")
    Jump("loc_7F9")

    label("loc_7D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E8")
    Jump("loc_7F9")

    label("loc_7E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F9")

    label("loc_7F9")

    TalkEnd(0xFE)
    Return()

    # Function_5_716 end

    def Function_6_7FD(): pass

    label("Function_6_7FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_816")
    Jump("loc_8CF")

    label("loc_816")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82C")
    Jump("loc_8CF")

    label("loc_82C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_842")
    Jump("loc_8CF")

    label("loc_842")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_858")
    Jump("loc_8CF")

    label("loc_858")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF")

    ChrTalk(
        0xB,
        (
            "#01106FKa au do what is good at the end\x01",
            "I'm thinking, but ….\x02\x03",
            "#01109FYou can also ride with Iria\x01",
            "Sounds fun!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CF")

    TalkEnd(0xFE)
    Return()

    # Function_6_7FD end

    def Function_7_8D3(): pass

    label("Function_7_8D3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC")
    Jump("loc_9F0")

    label("loc_8EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_902")
    Jump("loc_9F0")

    label("loc_902")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_918")
    Jump("loc_9F0")

    label("loc_918")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DF")

    ChrTalk(
        0xC,
        (
            "#06402FBuilding of this attraction,\x01",
            "The mansion which originally existed in Mishram\x01",
            "It seems that IBC has rebuilt it.\x02\x03",
            "#06409FWell, it is reasonably authentic ~ is not it?\x01",
            "Sighs come out somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F0")

    label("loc_9DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F0")

    label("loc_9F0")

    TalkEnd(0xFE)
    Return()

    # Function_7_8D3 end

    def Function_8_9F4(): pass

    label("Function_8_9F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7A")

    ChrTalk(
        0xD,
        (
            "#01702FHu ♪\x01",
            "The atmosphere is out!\x02\x03",
            "#01709FWell, I'm getting excited.\x01",
            "I want to ride quickly!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_AB4")

    label("loc_A7A")


    ChrTalk(
        0xD,
        (
            "#01709FWell, I'm getting excited.\x01",
            "I want to ride quickly!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB4")

    Jump("loc_B9F")

    label("loc_AB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACF")
    Jump("loc_B9F")

    label("loc_ACF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    Jump("loc_B9F")

    label("loc_AE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFB")
    Jump("loc_B9F")

    label("loc_AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(
        0xD,
        (
            "#01702FIt is the last, in any case\x01",
            "Why do not you step on a guy that makes you scary?\x02\x03",
            "#01700FIf only you\x01",
            "It will be stuck with the limit,\x01",
            "You should be fine if I am there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9F")

    TalkEnd(0xFE)
    Return()

    # Function_8_9F4 end

    def Function_9_BA3(): pass

    label("Function_9_BA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C56")

    ChrTalk(
        0xE,
        (
            "#01805FTo be able to see it ……\x01",
            "Could it be a ride?\x01",
            "Is it a course?\x02\x03",
            "#01806FTo go out like that,\x01",
            "There seems to be considerable thrill.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CA5")

    label("loc_C56")


    ChrTalk(
        0xE,
        (
            "#01802FCourse like that\x01",
            "To go out,\x01",
            "There seems to be considerable thrill.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA5")

    Jump("loc_CFD")

    label("loc_CAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC0")
    Jump("loc_CFD")

    label("loc_CC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD6")
    Jump("loc_CFD")

    label("loc_CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEC")
    Jump("loc_CFD")

    label("loc_CEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFD")

    label("loc_CFD")

    TalkEnd(0xFE)
    Return()

    # Function_9_BA3 end

    def Function_10_D01(): pass

    label("Function_10_D01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1A")
    Jump("loc_D9C")

    label("loc_D1A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    Jump("loc_D9C")

    label("loc_D30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D46")
    Jump("loc_D9C")

    label("loc_D46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5C")
    Jump("loc_D9C")

    label("loc_D5C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9C")

    ChrTalk(
        0xF,
        "#14006FHmm, I can do whatever else ……\x02",
    )

    CloseMessageWindow()

    label("loc_D9C")

    TalkEnd(0xFE)
    Return()

    # Function_10_D01 end

    def Function_11_DA0(): pass

    label("Function_11_DA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB9")
    Jump("loc_E62")

    label("loc_DB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCF")
    Jump("loc_E62")

    label("loc_DCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3B")

    ChrTalk(
        0x10,
        (
            "Fuu …\x01",
            "It was a terrible thrill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "But, good place for Lima\x01",
            "It was nice to be shown.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E62")

    label("loc_E3B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E51")
    Jump("loc_E62")

    label("loc_E51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E62")

    label("loc_E62")

    TalkEnd(0xFE)
    Return()

    # Function_11_DA0 end

    def Function_12_E66(): pass

    label("Function_12_E66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7F")
    Jump("loc_EF3")

    label("loc_E7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E95")
    Jump("loc_EF3")

    label("loc_E95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECC")

    ChrTalk(
        0x11,
        (
            "Whatching\x01",
            "Good work, you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF3")

    label("loc_ECC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE2")
    Jump("loc_EF3")

    label("loc_EE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF3")

    label("loc_EF3")

    TalkEnd(0xFE)
    Return()

    # Function_12_E66 end

    def Function_13_EF7(): pass

    label("Function_13_EF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F10")
    Jump("loc_FC0")

    label("loc_F10")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F26")
    Jump("loc_FC0")

    label("loc_F26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F99")

    ChrTalk(
        0x12,
        "Dad, it was sooo cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "A lot of monsters\x01",
            "He blew me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC0")

    label("loc_F99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAF")
    Jump("loc_FC0")

    label("loc_FAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC0")

    label("loc_FC0")

    TalkEnd(0xFE)
    Return()

    # Function_13_EF7 end

    def Function_14_FC4(): pass

    label("Function_14_FC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10FD")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Horror coaster, calling people\x01",
            "Welcome to \"Lunatic Zone\" ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a monster house where you live\x01",
            "You can run through with just one conductive gun,\x01",
            "It is an attraction of fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Mika and hide and seek in … …\x01",
            "What I am playing at attractions now\x01",
            "Let's stop it. )\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1100")

    label("loc_10FD")

    Call(0, 21)

    label("loc_1100")

    Return()

    # Function_14_FC4 end

    def Function_15_1101(): pass

    label("Function_15_1101")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118A")
    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x14,
        (
            "Ha, ha ha ha, ha …\x01",
            "To be scared,\x01",
            "There is nothing I can do ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "(Obviously I am scared … …)\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    Jump("loc_11F0")

    label("loc_118A")


    ChrTalk(
        0x14,
        (
            "While I was riding again and again,\x01",
            "Passing scary things\x01",
            "It has become fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Ha ha ha, now let's ride again!\x02",
    )

    CloseMessageWindow()

    label("loc_11F0")

    TalkEnd(0xFE)
    Return()

    # Function_15_1101 end

    def Function_16_11F4(): pass

    label("Function_16_11F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1248")

    ChrTalk(
        0x15,
        (
            "All right? If you do not want it\x01",
            "You do not have to ride by force.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12DC")

    label("loc_1248")


    ChrTalk(
        0x15,
        (
            "He got on a tone\x01",
            "Many times to a horror coaster\x01",
            "You are about to ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haa, and more\x01",
            "Various attractions\x01",
            "I want to play, but I do not know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DC")

    TalkEnd(0xFE)
    Return()

    # Function_16_11F4 end

    def Function_17_12E0(): pass

    label("Function_17_12E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1343")

    ChrTalk(
        0x16,
        (
            "Yeah, shouting yelled!\x01",
            "Screaming attractions are\x01",
            "After all it was fun!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1343")

    label("loc_1343")

    TalkEnd(0xFE)
    Return()

    # Function_17_12E0 end

    def Function_18_1347(): pass

    label("Function_18_1347")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D7")

    ChrTalk(
        0x17,
        (
            "When I was a father,\x01",
            "Also forget to shoot with a gun\x01",
            "I only screamed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "Next time you ride\x01",
            "I gotta let the gun shoot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13D7")

    label("loc_13D7")

    TalkEnd(0xFE)
    Return()

    # Function_18_1347 end

    def Function_19_13DB(): pass

    label("Function_19_13DB")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "#00309FOkay, girl.\x01",
            "Let's go in as soon as you enter ~ ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00106FWait a moment.\x01",
            "Prepare for a little more … ….\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_19_13DB end

    def Function_20_146B(): pass

    label("Function_20_146B")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B3")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_15C9")

    label("loc_14B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14DD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    Jump("loc_15C9")

    label("loc_14DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1507")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_15C9")

    label("loc_1507")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157F")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_155F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_1551")
    SetChrFlags(0x9, 0x80)
    Jump("loc_155F")

    label("loc_1551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_155F")
    SetChrFlags(0xC, 0x80)

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157A")
    ClearChrFlags(0x19, 0x80)

    label("loc_157A")

    Jump("loc_15C9")

    label("loc_157F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C9")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2310, 0, -3270, 180)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_15C9")

    Return()

    # Function_20_146B end

    def Function_21_15CA(): pass

    label("Function_21_15CA")

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
            "Horror coaster, calling people\x01",
            "Welcome to \"Lunatic Zone\" ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "This is a monster house where you live\x01",
            "You can run through with just one conductive gun,\x01",
            "It is an attraction of fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If it's okay, with someone\x01",
            "Although we recommend you to enter the entrance … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P(Who to invite..)\x02",
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
            "#1KWho invites you?\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Erie")
    MenuCmd(1, 0, "Tio")
    MenuCmd(1, 0, "Randy")
    MenuCmd(1, 0, "Noel")
    MenuCmd(1, 0, "Waji")
    MenuCmd(1, 0, "Keya")
    MenuCmd(1, 0, "Franc")
    MenuCmd(1, 0, "Cecil")
    MenuCmd(1, 0, "Ilia")
    MenuCmd(1, 0, "Lisha")
    MenuCmd(1, 0, "Shuri")
    MenuCmd(1, 0, "quit")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1801")
    MenuCmd(3, 0, 0x0)

    label("loc_1801")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1813")
    MenuCmd(3, 0, 0x1)

    label("loc_1813")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1825")
    MenuCmd(3, 0, 0x2)

    label("loc_1825")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1837")
    MenuCmd(3, 0, 0x3)

    label("loc_1837")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1849")
    MenuCmd(3, 0, 0x4)

    label("loc_1849")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_185B")
    MenuCmd(3, 0, 0x5)

    label("loc_185B")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_186D")
    MenuCmd(3, 0, 0x6)

    label("loc_186D")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_187F")
    MenuCmd(3, 0, 0x7)

    label("loc_187F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1891")
    MenuCmd(3, 0, 0x8)

    label("loc_1891")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18A3")
    MenuCmd(3, 0, 0x9)

    label("loc_18A3")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18B5")
    MenuCmd(3, 0, 0xA)

    label("loc_18B5")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B2B")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_193B"),
        (1, "loc_1ABB"),
        (2, "loc_1C1D"),
        (3, "loc_1DBD"),
        (4, "loc_1F0C"),
        (5, "loc_2085"),
        (6, "loc_2217"),
        (7, "loc_2385"),
        (8, "loc_24FD"),
        (9, "loc_268D"),
        (10, "loc_27E2"),
        (SWITCH_DEFAULT, "loc_2963"),
    )


    label("loc_193B")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Ok let's invite Elie)\x02",
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
        "Erie",
        (
            "#00106F#6PHorror coaster ……\x01",
            "Huh, you really enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PHaha, I got it on\x01",
            "It's okay.\x02\x03",
            "#00002FFirmly escort\x01",
            "Because I will do it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Erie",
        "#00100F#12PYeah, I'll be counting on you\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_1ABB")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Tio.\x02",
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
            "#00204F#6PRumor new attraction ……\x01",
            "I am looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PIt seems a bit scary,\x01",
            "Tio seems to be fine.\x02\x03",
            "#00000FWhy do not you go in?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Tio",
        "#00200F#12PYeah, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_1C1D")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Randy.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x2)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CA4")
    SetChrFlags(0xA, 0x8)

    label("loc_1CA4")

    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Randy",
        (
            "#00303F#6PHmm, the horror system\x01",
            "I am going to enter with a girl I want\x01",
            "I wish I was a regular stone.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#5PWell, even two men\x01",
            "It might be fun.\x02\x03",
            "#00000FLet's get in right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Randy",
        (
            "#00300F#12PWell, I came all the way\x01",
            "I suppose you go out with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_1DBD")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Okay … let's invite Noel.\x02",
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
        "Noel",
        (
            "#10100F#6PMonster ruining …\x01",
            "Somehow it will burn!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00009F#5PHaha, I'm sorry.\x02\x03",
            "#00000FWell then, let's enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Noel",
        "#10100F#12PYeah, let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_1F0C")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Okay … let's invite Wazi.)\x02",
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
        "Waji",
        (
            "#10304F#6PHorror coaster ……\x01",
            "Hoff, while screaming\x01",
            "Would you like to embrace it?\x02",
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
            "#00006F#5PI do not expect such a thing.\x02\x03",
            "#00000FOh well, let's try entering.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Waji",
        "#10300F#12PHuh, I understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_2085")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Ka'a.)\x02",
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
        "Keya",
        (
            "#01109F#6PYou got a gig here?\x01",
            "It's exciting!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00012F#5PAs expected, the real thing\x01",
            "It will not come out, though …\x01",
            "I think that the atmosphere can be enjoyed.\x02\x03",
            "#00000FWell then, let's enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Keya",
        "#01109F#12PBarely!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_2217")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite the franc.\x02",
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
        "Franc",
        (
            "#06409F#6PRumor new attraction ……\x01",
            "I have been excited.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PHaha, though it is a horror group\x01",
            "It is quite lively.\x02\x03",
            "#00000FAlright, are you going to get it soon?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Franc",
        "#06400F#12PHehe, thank you ~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_2385")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Cecil 's older sister.\x02",
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
            "#05902F#6PIt is a rumored new attraction.\x01",
            "Hehe, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#5PAlthough it is a horror, it is quite affordable.\x02\x03",
            "#00000FCecil elder sister I firmly\x01",
            "I will escort you.\x02",
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
    Jump("loc_2963")

    label("loc_24FD")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Iria.\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2586")
    SetChrFlags(0xD, 0x8)

    label("loc_2586")

    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Ilia",
        (
            "#01709F#6PSuch a screaming guy\x01",
            "I was looking forward to it ~!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00009F#5PHello, everyone Mr. Iria\x01",
            "It is an attraction you like.\x02\x03",
            "#00000FWell then, shall we go?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Ilia",
        "#01700F#12PYeah, go ahead now!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_268D")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Leisha.\x02",
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
        "Lisha",
        (
            "#01802F#6PHehu, there is always atmosphere\x01",
            "It sounds like an attraction.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#5PHaha, I guess you can afford it well.\x02\x03",
            "#00000FWell then, let's enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Lisha",
        "#01809F#12PYes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_27E2")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        "#00000F#6P(Alright … let's invite Sri.)\x02",
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
        "Shuri",
        (
            "#14004F#6PFun\x01",
            "Why is not there anything wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PHow is it?\x01",
            "Surprisingly scared … …\x02\x03",
            "#00000FOkay, then it's time to enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x18)
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Shuri",
        (
            "#14011F#12PWait a moment.\x01",
            "Ready for the mind …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2963")

    label("loc_2963")


    ChrTalk(
        0x13,
        "Well then I'll take your tickets\x02",
    )

    CloseMessageWindow()

    def lambda_298E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_298E)
    Sleep(50)

    def lambda_299E():
        OP_93(0x18, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_299E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x18, 0)
    SubItemNumber('米修拉姆·奇幻乐园游乐券', 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Gave one ticket to the staff member\x07\x00\x02",
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
            "Conductive gun to defeat monster\x01",
            "It is installed in the ride.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Giggle\x01",
            "I hope to return home safely.\x02",
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

    def lambda_2AB7():
        OP_98(0xFE, 0xFFFFFA88, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2AB7)
    OP_93(0x13, 0x5A, 0x1F4)
    WaitChrThread(0x13, 1)
    Sleep(300)
    FadeToDark(1000, 0, -1)

    def lambda_2AE9():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AE9)
    Sleep(50)

    def lambda_2B01():
        OP_9B(0x0, 0x18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2B01)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x18, 0)
    OP_0D()
    NewScene("t1360", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B79")

    label("loc_2B2B")


    ChrTalk(
        0x13,
        "Huh, will you stop it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Welcoming your visit\x01",
            "I will be waiting …\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2B79")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 400, -350, 180)
    EventEnd(0x5)
    Return()

    # Function_21_15CA end

    def Function_22_2B94(): pass

    label("Function_22_2B94")

    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xF, 0x8)
    Return()

    # Function_22_2B94 end

    def Function_23_2BBD(): pass

    label("Function_23_2BBD")

    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xF, 0x8)
    Return()

    # Function_23_2BBD end

    def Function_24_2BE6(): pass

    label("Function_24_2BE6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("chr/ch03000.itc", 0x1F)
    LoadChrToIndex("chr/ch07500.itc", 0x20)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x18, 0x80)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2C58"),
        (1, "loc_2C61"),
        (2, "loc_2C6A"),
        (3, "loc_2C73"),
        (4, "loc_2C7C"),
        (5, "loc_2C85"),
        (6, "loc_2C8E"),
        (7, "loc_2C97"),
        (8, "loc_2CA0"),
        (9, "loc_2CA9"),
        (10, "loc_2CB2"),
        (SWITCH_DEFAULT, "loc_2CBB"),
    )


    label("loc_2C58")

    SetChrChipByIndex(0x18, 0x0)
    Jump("loc_2CBB")

    label("loc_2C61")

    SetChrChipByIndex(0x18, 0x1)
    Jump("loc_2CBB")

    label("loc_2C6A")

    SetChrChipByIndex(0x18, 0x2)
    Jump("loc_2CBB")

    label("loc_2C73")

    SetChrChipByIndex(0x18, 0x1E)
    Jump("loc_2CBB")

    label("loc_2C7C")

    SetChrChipByIndex(0x18, 0x1F)
    Jump("loc_2CBB")

    label("loc_2C85")

    SetChrChipByIndex(0x18, 0x3)
    Jump("loc_2CBB")

    label("loc_2C8E")

    SetChrChipByIndex(0x18, 0x4)
    Jump("loc_2CBB")

    label("loc_2C97")

    SetChrChipByIndex(0x18, 0x20)
    Jump("loc_2CBB")

    label("loc_2CA0")

    SetChrChipByIndex(0x18, 0x5)
    Jump("loc_2CBB")

    label("loc_2CA9")

    SetChrChipByIndex(0x18, 0x6)
    Jump("loc_2CBB")

    label("loc_2CB2")

    SetChrChipByIndex(0x18, 0x7)
    Jump("loc_2CBB")

    label("loc_2CBB")

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
        (0, "loc_2D77"),
        (1, "loc_2EA8"),
        (2, "loc_2FBB"),
        (3, "loc_30CC"),
        (4, "loc_31E5"),
        (5, "loc_32EC"),
        (6, "loc_33F5"),
        (7, "loc_3515"),
        (8, "loc_3638"),
        (9, "loc_3770"),
        (10, "loc_388F"),
        (SWITCH_DEFAULT, "loc_39CE"),
    )


    label("loc_2D77")


    NpcTalk(
        0x18,
        "Erie",
        (
            "#00106F#12PHaa …… Obake is like that\x01",
            "To come closer,\x01",
            "I was surprised.\x02\x03",
            "#00100FHehe, well than I thought\x01",
            "I was not scared,\x01",
            "It is certain that it was fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, if you enjoyed it\x01",
            "It was nice to invite me.\x02\x03",
            "#00000FWell then see you later\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Erie",
        "#00100F#12PYes, later\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_2EA8")


    NpcTalk(
        0x18,
        "Tio",
        (
            "#00204F#12PAppealing obsession … …\x01",
            "There was quite a thrill.\x02\x03",
            "#00200FAs expected it is a new attraction.\x01",
            "It also nods that it is extremely popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, he enjoyed it.\x01",
            "I'm glad that it looks like.\x02\x03",
            "#00000FWell then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Tio",
        "#00200F#12PWell, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_2FBB")


    NpcTalk(
        0x18,
        "Randy",
        (
            "#00300F#12PHaha, for the horror system\x01",
            "It was pretty good.\x02\x03",
            "#00306FThe other party is not a beautiful older sister\x01",
            "I'm sorry I was you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, it was a lot of fun\x01",
            "It's fine, is not it.\x02\x03",
            "#00000FWell then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Randy",
        "#00300F#12POh, I see you again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_30CC")


    NpcTalk(
        0x18,
        "Noel",
        (
            "#10100F#12PIt was a lot of fun.\x02\x03",
            "#10109FShooting training at the guard, too,\x01",
            "In this game formula\x01",
            "I feel like I'm getting better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, indeed …\x01",
            "Someday such an era has come.\x02\x03",
            "#00000FWell then see you later\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Noel",
        "#10100F#12PYes, but also!\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_31E5")


    NpcTalk(
        0x18,
        "Waji",
        (
            "#10304F#12PHuh, quite\x01",
            "It was a great attraction.\x02\x03",
            "#10302FWhat I've done with you\x01",
            "I was pretty crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FI also got caught up … ….\x01",
            "I hope you enjoyed it.\x02\x03",
            "#00000FWell then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Waji",
        "#10300F#12PHuh, and more.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_32EC")


    NpcTalk(
        0x18,
        "Keya",
        (
            "#01109F#12PHaha, it was fun!\x02\x03",
            "Run through the dark,\x01",
            "The wind hit the buunbun\x01",
            "It was awesome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, to that extent\x01",
            "If you enjoyed it\x01",
            "It was nice to invite me.\x02\x03",
            "#00000FWell then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Keya",
        "#01100F#12PYes, I do not have to!\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_33F5")


    NpcTalk(
        0x18,
        "Franc",
        (
            "#06400F#12PHaha, it was a thrilling score!\x02\x03",
            "#06409FMr. Lloyd\x01",
            "Good luck fighting for you\x01",
            "I have been saved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FThat number of opponents is against\x01",
            "It was quite difficult, though ….\x01",
            "It was nice to have fun.\x02\x03",
            "#00000FWell then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Franc",
        "#06400F#12PYes, again ~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_3515")


    NpcTalk(
        0x18,
        "Cecil",
        (
            "#05900F#12PHehe, it was a lot of fun.\x02\x03",
            "#05909FLloyd's shooting figure also\x01",
            "It was quite dependable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHahaha, indeed it is an actual gun\x01",
            "It seems that the treatment is completely different ….\x01",
            "Well, I'm glad you enjoyed it.\x02\x03",
            "#00000FWell then see you later\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Cecil",
        "#05900F#12PWell, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_3638")


    NpcTalk(
        0x18,
        "Ilia",
        (
            "#01704F#12PWell, this is as expected\x01",
            "It was an attraction!\x02\x03",
            "#01702FHugh, more tuck\x01",
            "I could have gotten a gig.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FSurely, that is\x01",
            "I think it's too hard … ….\x01",
            "Well, it was nice to have fun.\x02\x03",
            "#00000FWell then see you later\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Ilia",
        "#01700F#12PYeah, see you ~.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_3770")


    NpcTalk(
        0x18,
        "Lisha",
        (
            "#01802F#12PHaa, it was quite fun.\x02\x03",
            "#01806FA monster moves swiftly,\x01",
            "Mr. Lloyd shooting\x01",
            "It seemed to be very difficult, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, it was a bit tough but\x01",
            "I also enjoyed it quite well.\x02\x03",
            "#00000FWell then see you later\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Lisha",
        "#01802F#12PYes, again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_388F")


    NpcTalk(
        0x18,
        "Shuri",
        (
            "#14006F#12PHuh …… The vehicle is fast,\x01",
            "Although I could not open my eyes at all\x01",
            "The thrill was pretty good.\x02\x03",
            "#14002FEven so,\x01",
            "It looked like fun.\x01",
            "I also wanted to shoot them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha …… even this\x01",
            "It was pretty tough, though.\x02\x03",
            "#00000FWell then, see you later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Shuri",
        "#14000F#12PSounds like that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_39CE")


    def lambda_39D3():

        label("loc_39D3")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_39D3")

    QueueWorkItem2(0x101, 2, lambda_39D3)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_39EC():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_39EC)
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
        (0, "loc_3A69"),
        (1, "loc_3A77"),
        (2, "loc_3A85"),
        (3, "loc_3A93"),
        (4, "loc_3AA1"),
        (5, "loc_3AAF"),
        (6, "loc_3ABD"),
        (7, "loc_3ACB"),
        (8, "loc_3AD9"),
        (9, "loc_3AE7"),
        (10, "loc_3AF5"),
        (SWITCH_DEFAULT, "loc_3B03"),
    )


    label("loc_3A69")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3A77")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3A85")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3A93")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AA1")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AAF")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3ABD")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3ACB")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AD9")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AE7")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3AF5")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B03")

    label("loc_3B03")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B29")
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_3B29")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 0, -2000, 180)
    EventEnd(0x5)
    Return()

    # Function_24_2BE6 end

    def Function_25_3B44(): pass

    label("Function_25_3B44")

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
        "#00002FGot you!\x02",
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
            "Y-you got me!\x07\x00\x02",
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
            "Well, so sooner\x01",
            "I found it four times,\x01",
            "I can not believe it ~.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Miserable, Nomorous\x01",
            "With Michio io\x01",
            "It is a big difference Yo ~ ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_3D66")
    OP_63(0x153, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_3D7E")

    label("loc_3D66")

    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3D7E")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Misoshi, Misiwa\x01",
            "I'm pretty strict …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Ehehe, well next time is the last\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Well, in the end it's a more difficult place\x01",
            "I'm hiding, so do your best and find out!\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E3D():

        label("loc_3E3D")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_3E3D")

    QueueWorkItem2(0x101, 1, lambda_3E3D)

    def lambda_3E4F():

        label("loc_3E4F")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_3E4F")

    QueueWorkItem2(0xEF, 1, lambda_3E4F)
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
            "#00006FFinally this is gonna be over\x02\x03",
            "#00000FBecause it's only in the theme park\x01",
            "Although it seems not to be difficult up to that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_3F97")

    ChrTalk(
        0x102,
        (
            "#00100FWell then,\x01",
            "Let's go looking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_3F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_3FD5")

    ChrTalk(
        0x103,
        (
            "#00200FThen,\x01",
            "Let's go looking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_3FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4011")

    ChrTalk(
        0x104,
        (
            "#00300FWell then,\x01",
            "Why do not you go looking for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_4011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4051")

    ChrTalk(
        0x109,
        (
            "#10100FWell then,\x01",
            "Let's go looking!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_4051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_4095")

    ChrTalk(
        0x105,
        (
            "#10300FWell then,\x01",
            "Let's go looking for something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_4095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_40C8")

    ChrTalk(
        0x153,
        "#01100FWell then it's time to look for!\x02",
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_40C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_410A")

    ChrTalk(
        0x156,
        (
            "#06400FWell then,\x01",
            "Let's go looking ~!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_410A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_414E")

    ChrTalk(
        0x14C,
        (
            "#05900FHuhu, then\x01",
            "Let's go looking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_414E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4192")

    ChrTalk(
        0x134,
        (
            "#01700FHuh, then,\x01",
            "Let's go looking!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_4192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_41D0")

    ChrTalk(
        0x135,
        (
            "#01802FThen,\x01",
            "Let's go looking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FC")

    label("loc_41D0")


    ChrTalk(
        0x166,
        (
            "#14000FThen,\x01",
            "Do you go looking for something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41FC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xE)
    SetScenarioFlags(0x1C9, 6)
    SetChrPos(0x0, 160, 0, -12030, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_3B44 end

    def Function_26_4228(): pass

    label("Function_26_4228")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Of the theme park\x01",
            "A sketch is drawn.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_26_4228 end

    SaveToFile()

Try(main)
