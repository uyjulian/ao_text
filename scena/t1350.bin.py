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
        "MWL Staff",              # 12
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
        "Function_4_61D",          # 04, 4
        "Function_5_717",          # 05, 5
        "Function_6_7F5",          # 06, 6
        "Function_7_8F3",          # 07, 7
        "Function_8_A13",          # 08, 8
        "Function_9_BC6",          # 09, 9
        "Function_10_D1C",         # 0A, 10
        "Function_11_DBB",         # 0B, 11
        "Function_12_E89",         # 0C, 12
        "Function_13_F16",         # 0D, 13
        "Function_14_FD1",         # 0E, 14
        "Function_15_1125",        # 0F, 15
        "Function_16_1214",        # 10, 16
        "Function_17_1326",        # 11, 17
        "Function_18_1399",        # 12, 18
        "Function_19_1450",        # 13, 19
        "Function_20_14E2",        # 14, 20
        "Function_21_1641",        # 15, 21
        "Function_22_2C17",        # 16, 22
        "Function_23_2C40",        # 17, 23
        "Function_24_2C69",        # 18, 24
        "Function_25_3BAF",        # 19, 25
        "Function_26_42A0",        # 1A, 26
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
    Jump("loc_619")

    label("loc_54A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D")
    Call(0, 19)
    Jump("loc_5D7")

    label("loc_56D")


    ChrTalk(
        0x8,
        (
            "#00106F*sigh*... I'm not good\x01",
            "with things like this.\x02\x03",
            "#00111FMaybe Bell built it just\x01",
            "to scare me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D7")

    Jump("loc_619")

    label("loc_5DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2")
    Jump("loc_619")

    label("loc_5F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_608")
    Jump("loc_619")

    label("loc_608")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_619")

    label("loc_619")

    TalkEnd(0xFE)
    Return()

    # Function_3_531 end

    def Function_4_61D(): pass

    label("Function_4_61D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_636")
    Jump("loc_713")

    label("loc_636")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64C")
    Jump("loc_713")

    label("loc_64C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    Jump("loc_713")

    label("loc_662")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_702")

    ChrTalk(
        0x9,
        (
            "#00203FYou can clearly hear\x01",
            "screams and shrieks even\x01",
            "from here.\x02\x03",
            "#00204FWhen I hear them, It's\x01",
            "scary but at the same\x01",
            "time, exciting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_713")

    label("loc_702")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_713")

    label("loc_713")

    TalkEnd(0xFE)
    Return()

    # Function_4_61D end

    def Function_5_717(): pass

    label("Function_5_717")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_730")
    Jump("loc_7F1")

    label("loc_730")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_753")
    Call(0, 19)
    Jump("loc_7AF")

    label("loc_753")


    ChrTalk(
        0xA,
        (
            "#00309FHaha, milady is a\x01",
            "scaredy cat.\x02\x03",
            "#00304FWell, this is my kind of\x01",
            "ride, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AF")

    Jump("loc_7F1")

    label("loc_7B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CA")
    Jump("loc_7F1")

    label("loc_7CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E0")
    Jump("loc_7F1")

    label("loc_7E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")

    label("loc_7F1")

    TalkEnd(0xFE)
    Return()

    # Function_5_717 end

    def Function_6_7F5(): pass

    label("Function_6_7F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80E")
    Jump("loc_8EF")

    label("loc_80E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824")
    Jump("loc_8EF")

    label("loc_824")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83A")
    Jump("loc_8EF")

    label("loc_83A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_850")
    Jump("loc_8EF")

    label("loc_850")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EF")

    ChrTalk(
        0xB,
        (
            "#01106FKeA is thinking hard about\x01",
            "what would be a good\x01",
            "attraction for last...\x02\x03",
            "#01109FThis seems like it would\x01",
            "be fun to ride with Ilya!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EF")

    TalkEnd(0xFE)
    Return()

    # Function_6_7F5 end

    def Function_7_8F3(): pass

    label("Function_7_8F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90C")
    Jump("loc_A0F")

    label("loc_90C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_922")
    Jump("loc_A0F")

    label("loc_922")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_938")
    Jump("loc_A0F")

    label("loc_938")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FE")

    ChrTalk(
        0xC,
        (
            "#06402FIt seems this attraction\x01",
            "was a former Michelam\x01",
            "mansion that IBC remodeled.\x02\x03",
            "#06409FWooow, they really went all\x01",
            "out with this. It's enough\x01",
            "to take your breath away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0F")

    label("loc_9FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0F")

    label("loc_A0F")

    TalkEnd(0xFE)
    Return()

    # Function_7_8F3 end

    def Function_8_A13(): pass

    label("Function_8_A13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A92")

    ChrTalk(
        0xD,
        (
            "#01702FWhew!♪ What atmosphere!\x02\x03",
            "#01709FMmm, I'm so excited. I\x01",
            "want to ride it now!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_ACA")

    label("loc_A92")


    ChrTalk(
        0xD,
        (
            "#01709FMmm, I'm so excited. I\x01",
            "want to ride it now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACA")

    Jump("loc_BC2")

    label("loc_ACF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    Jump("loc_BC2")

    label("loc_AE5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFB")
    Jump("loc_BC2")

    label("loc_AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B11")
    Jump("loc_BC2")

    label("loc_B11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC2")

    ChrTalk(
        0xD,
        (
            "#01702FIt's the last one, so\x01",
            "might as well ride a\x01",
            "refreshing one, no?\x02\x03",
            "#01700FIt's probably the limit of\x01",
            "what you can do alone, but\x01",
            "with me it'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC2")

    TalkEnd(0xFE)
    Return()

    # Function_8_A13 end

    def Function_9_BC6(): pass

    label("Function_9_BC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C71")

    ChrTalk(
        0xE,
        (
            "#01805FThe one I see over\x01",
            "there... Could it be a\x01",
            "course ride?\x02\x03",
            "#01806FGoing outside like\x01",
            "that... It seems it's\x01",
            "quite thrilling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CC0")

    label("loc_C71")


    ChrTalk(
        0xE,
        (
            "#01802FA course going outside\x01",
            "like that... It seems\x01",
            "it's quite thrilling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC0")

    Jump("loc_D18")

    label("loc_CC5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDB")
    Jump("loc_D18")

    label("loc_CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF1")
    Jump("loc_D18")

    label("loc_CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D07")
    Jump("loc_D18")

    label("loc_D07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D18")

    label("loc_D18")

    TalkEnd(0xFE)
    Return()

    # Function_9_BC6 end

    def Function_10_D1C(): pass

    label("Function_10_D1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D35")
    Jump("loc_DB7")

    label("loc_D35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4B")
    Jump("loc_DB7")

    label("loc_D4B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61")
    Jump("loc_DB7")

    label("loc_D61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77")
    Jump("loc_DB7")

    label("loc_D77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB7")

    ChrTalk(
        0xF,
        (
            "#14006FHmm, I'm fine with\x01",
            "whatever, so...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB7")

    TalkEnd(0xFE)
    Return()

    # Function_10_D1C end

    def Function_11_DBB(): pass

    label("Function_11_DBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD4")
    Jump("loc_E85")

    label("loc_DD4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEA")
    Jump("loc_E85")

    label("loc_DEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5E")

    ChrTalk(
        0x10,
        (
            "Phew! ...That was\x01",
            "incredibly thrilling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Still, I'm glad I showed\x01",
            "Rimah a good time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E85")

    label("loc_E5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E74")
    Jump("loc_E85")

    label("loc_E74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E85")

    label("loc_E85")

    TalkEnd(0xFE)
    Return()

    # Function_11_DBB end

    def Function_12_E89(): pass

    label("Function_12_E89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA2")
    Jump("loc_F12")

    label("loc_EA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB8")
    Jump("loc_F12")

    label("loc_EB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEB")

    ChrTalk(
        0x11,
        "Haha... Good job, dear.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F12")

    label("loc_EEB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F01")
    Jump("loc_F12")

    label("loc_F01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F12")

    label("loc_F12")

    TalkEnd(0xFE)
    Return()

    # Function_12_E89 end

    def Function_13_F16(): pass

    label("Function_13_F16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2F")
    Jump("loc_FCD")

    label("loc_F2F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F45")
    Jump("loc_FCD")

    label("loc_F45")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA6")

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
    Jump("loc_FCD")

    label("loc_FA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBC")
    Jump("loc_FCD")

    label("loc_FBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCD")

    label("loc_FCD")

    TalkEnd(0xFE)
    Return()

    # Function_13_F16 end

    def Function_14_FD1(): pass

    label("Function_14_FD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1121")
    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Welcome to the Horror\x01",
            "Coaster, popularly called\x01",
            "the Lunatic Zone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is a horror attraction where you\x01",
            "run through a mansion where monsters\x01",
            "dwell armed with a mere orbal gun.\x02",
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
    Jump("loc_1124")

    label("loc_1121")

    Call(0, 21)

    label("loc_1124")

    Return()

    # Function_14_FD1 end

    def Function_15_1125(): pass

    label("Function_15_1125")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1193")
    OP_4B(0x15, 0xFF)

    ChrTalk(
        0x14,
        (
            "H-Haha h-ha... N-No way\x01",
            "that's scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "(He's obviously\x01",
            "scared...)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    Jump("loc_1210")

    label("loc_1193")


    ChrTalk(
        0x14,
        (
            "Riding over and over again,\x01",
            "I got over what scared me\x01",
            "and it became fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Hahaha, c'mon, let's go\x01",
            "for another ride!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1210")

    TalkEnd(0xFE)
    Return()

    # Function_15_1125 end

    def Function_16_1214(): pass

    label("Function_16_1214")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127D")

    ChrTalk(
        0x15,
        (
            "Are you all right? If you\x01",
            "don't like it, you don't\x01",
            "have to force yourself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1322")

    label("loc_127D")


    ChrTalk(
        0x15,
        (
            "My boyfriend, has gotten carried\x01",
            "away and now wants to ride the\x01",
            "horror coaster over and over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "*sigh*, I'd like to have\x01",
            "fun at the other\x01",
            "attractions too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1322")

    TalkEnd(0xFE)
    Return()

    # Function_16_1214 end

    def Function_17_1326(): pass

    label("Function_17_1326")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1395")

    ChrTalk(
        0x16,
        (
            "Maaan, I screamed and screamed!\x01",
            "Attractions that make you\x01",
            "scream are really fun!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1395")

    label("loc_1395")

    TalkEnd(0xFE)
    Return()

    # Function_17_1326 end

    def Function_18_1399(): pass

    label("Function_18_1399")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144C")

    ChrTalk(
        0x17,
        (
            "That father of mine, he even\x01",
            "forgot to shoot with the gun\x01",
            "and did nothing but scream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "The next time we ride\x01",
            "this, I'll be the one\x01",
            "with the gun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144C")

    label("loc_144C")

    TalkEnd(0xFE)
    Return()

    # Function_18_1399 end

    def Function_19_1450(): pass

    label("Function_19_1450")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xA,
        (
            "#00309FAlright, milady. Let's\x01",
            "head inside♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00106FW-Wait a moment. Let me\x01",
            "mentally prepare a bit\x01",
            "more...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_19_1450 end

    def Function_20_14E2(): pass

    label("Function_20_14E2")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152A")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1640")

    label("loc_152A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1554")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    Jump("loc_1640")

    label("loc_1554")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157E")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_1640")

    label("loc_157E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F6")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_15C8")
    SetChrFlags(0x9, 0x80)
    Jump("loc_15D6")

    label("loc_15C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_15D6")
    SetChrFlags(0xC, 0x80)

    label("loc_15D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15F1")
    ClearChrFlags(0x19, 0x80)

    label("loc_15F1")

    Jump("loc_1640")

    label("loc_15F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1640")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2310, 0, -3270, 180)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_1640")

    Return()

    # Function_20_14E2 end

    def Function_21_1641(): pass

    label("Function_21_1641")

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
            "Welcome to the Horror\x01",
            "Coaster, popularly called\x01",
            "the Lunatic Zone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "This is a horror attraction where you\x01",
            "run through a mansion where monsters\x01",
            "dwell armed with a mere orbal gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I recommend entering\x01",
            "with someone if you\x01",
            "like, but...\x02",
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
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_186A")
    MenuCmd(3, 0, 0x0)

    label("loc_186A")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_187C")
    MenuCmd(3, 0, 0x1)

    label("loc_187C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_188E")
    MenuCmd(3, 0, 0x2)

    label("loc_188E")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18A0")
    MenuCmd(3, 0, 0x3)

    label("loc_18A0")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18B2")
    MenuCmd(3, 0, 0x4)

    label("loc_18B2")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18C4")
    MenuCmd(3, 0, 0x5)

    label("loc_18C4")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18D6")
    MenuCmd(3, 0, 0x6)

    label("loc_18D6")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18E8")
    MenuCmd(3, 0, 0x7)

    label("loc_18E8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_18FA")
    MenuCmd(3, 0, 0x8)

    label("loc_18FA")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_190C")
    MenuCmd(3, 0, 0x9)

    label("loc_190C")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_191E")
    MenuCmd(3, 0, 0xA)

    label("loc_191E")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BB0")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19A4"),
        (1, "loc_1B16"),
        (2, "loc_1C72"),
        (3, "loc_1E15"),
        (4, "loc_1F6D"),
        (5, "loc_20D5"),
        (6, "loc_226D"),
        (7, "loc_23F4"),
        (8, "loc_2581"),
        (9, "loc_2713"),
        (10, "loc_285D"),
        (SWITCH_DEFAULT, "loc_29EB"),
    )


    label("loc_19A4")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Elie.)\x02",
        )
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
            "We're really going in?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PHaha. I'll be with you,\x01",
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
        (
            "#00100F#12PYes, I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_1B16")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Tio.)\x02",
        )
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
            "#00204F#6PThe rumored new\x01",
            "attraction... I'm looking\x01",
            "forward to this a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PIt seems a little scary,\x01",
            "but you seem fine, Tio.\x02\x03",
            "#00000FShall we enter?\x02",
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
    Jump("loc_29EB")

    label("loc_1C72")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Randy.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x2)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CF4")
    SetChrFlags(0xA, 0x8)

    label("loc_1CF4")

    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Randy",
        (
            "#00303F#6PHmm. Entering a horror\x01",
            "attraction with a girl is a\x01",
            "standard play for getting her.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#5PHaha. It might be fun\x01",
            "with just us guys,\x01",
            "though.\x02\x03",
            "#00000FShall we enter?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Randy",
        (
            "#00300F#12PWell I'm here. Might as\x01",
            "well go along with it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_1E15")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Noｱl.)\x02",
        )
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
            "#10100F#6PMonster extermination...\x01",
            "I'm getting fired up for\x01",
            "some reason!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00009F#5PHaha. You're certainly\x01",
            "excited.\x02\x03",
            "#00000FShall we enter, then?\x02",
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
    Jump("loc_29EB")

    label("loc_1F6D")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Wazy.)\x02",
        )
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
            "#10304F#6PThe Horror Coaster, eh?\x01",
            "Hehe. Will you hug me\x01",
            "when you scream?\x02",
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
            "#00006F#5PDon't count on it.\x02\x03",
            "#00000FWell anyway, let's\x01",
            "enter.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Wazy",
        "#10300F#12PHehe, roger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_20D5")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "KeA.)\x02",
        )
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
            "#01109F#6PAre there ghosts here?\x01",
            "I'm so excited! I can't\x01",
            "wait!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00012F#5PHaha. I'm sure you know real ones\x01",
            "won't appear, but... I think we\x01",
            "can enjoy the atmosphere.\x02\x03",
            "#00000FAlright then, let's enter.\x02",
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
    Jump("loc_29EB")

    label("loc_226D")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Fran.)\x02",
        )
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
            "#06409F#6PThe rumored new\x01",
            "attraction... My heart\x01",
            "is racing!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PHaha. Even though it's a\x01",
            "horror attraction, you're\x01",
            "really excited, aren't you.\x02\x03",
            "#00000FAlright, time to enter\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Fran",
        (
            "#06400F#12PHaha. I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_23F4")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Cecil.)\x02",
        )
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
            "#05902F#6PThe rumored new\x01",
            "attraction, right? Haha.\x01",
            "I can't wait.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#5PHaha. You're awfully\x01",
            "calm, considering this\x01",
            "is a horror attraction.\x02\x03",
            "#00000FI'll escort you\x01",
            "properly, Cecil.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Cecil",
        (
            "#05900F#12PYes, I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_2581")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Ilya.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x18, 0x80)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 600, 800, 1000, 0)
    SetChrPos(0x101, -600, 800, 1000, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2602")
    SetChrFlags(0xD, 0x8)

    label("loc_2602")

    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(
        0x18,
        "Ilya",
        (
            "#01709F#6PI always look forward to\x01",
            "screamers like this, you\x01",
            "know!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00009F#5PHaha. This really seems\x01",
            "like the kind of attraction\x01",
            "you'd like, Ilya.\x02\x03",
            "#00000FAlright then, shall we\x01",
            "enter?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x10E, 0x1F4)

    NpcTalk(
        0x18,
        "Ilya",
        "#01700F#12PYeah, let's go already!\x02",
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_2713")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Rixia.)\x02",
        )
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
            "#01802F#6PHaha. This seems like an\x01",
            "attraction with a lot of\x01",
            "atmosphere.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#5PHaha. You seem quite\x01",
            "calm.\x02\x03",
            "#00000FWell then, shall we\x01",
            "enter?\x02",
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
    Jump("loc_29EB")

    label("loc_285D")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00000F#6P(Alright... I'll invite\x01",
            "Sully.)\x02",
        )
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
            "#14004F#6PH-Hmph... It's no big\x01",
            "deal, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PHaha, I wonder about\x01",
            "that. It might be scarier\x01",
            "than you think...\x02\x03",
            "#00000FAlright, let's enter\x01",
            "then.\x02",
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
            "#14011F#12PW-Wait a minute. I'm not\x01",
            "ready yet...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EB")

    label("loc_29EB")


    ChrTalk(
        0x13,
        (
            "Then, I'll hold on to\x01",
            "your tickets.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A19():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A19)
    Sleep(50)

    def lambda_2A29():
        OP_93(0x18, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2A29)
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
        0x13,
        (
            "The orbal gun to defeat\x01",
            "the monsters is installed\x01",
            "on the vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Hehe... Please return in\x01",
            "one piece.\x02",
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

    def lambda_2B3C():
        OP_98(0xFE, 0xFFFFFA88, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2B3C)
    OP_93(0x13, 0x5A, 0x1F4)
    WaitChrThread(0x13, 1)
    Sleep(300)
    FadeToDark(1000, 0, -1)

    def lambda_2B6E():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B6E)
    Sleep(50)

    def lambda_2B86():
        OP_9B(0x0, 0x18, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2B86)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x18, 0)
    OP_0D()
    NewScene("t1360", 0, 0, 0)
    IdleLoop()
    Jump("loc_2BFC")

    label("loc_2BB0")


    ChrTalk(
        0x13,
        "Hehe, you're giving up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "We'll be waiting for you\x01",
            "next visit...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2BFC")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 400, -350, 180)
    EventEnd(0x5)
    Return()

    # Function_21_1641 end

    def Function_22_2C17(): pass

    label("Function_22_2C17")

    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xF, 0x8)
    Return()

    # Function_22_2C17 end

    def Function_23_2C40(): pass

    label("Function_23_2C40")

    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xF, 0x8)
    Return()

    # Function_23_2C40 end

    def Function_24_2C69(): pass

    label("Function_24_2C69")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("chr/ch03000.itc", 0x1F)
    LoadChrToIndex("chr/ch07500.itc", 0x20)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x18, 0x80)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_2CDB"),
        (1, "loc_2CE4"),
        (2, "loc_2CED"),
        (3, "loc_2CF6"),
        (4, "loc_2CFF"),
        (5, "loc_2D08"),
        (6, "loc_2D11"),
        (7, "loc_2D1A"),
        (8, "loc_2D23"),
        (9, "loc_2D2C"),
        (10, "loc_2D35"),
        (SWITCH_DEFAULT, "loc_2D3E"),
    )


    label("loc_2CDB")

    SetChrChipByIndex(0x18, 0x0)
    Jump("loc_2D3E")

    label("loc_2CE4")

    SetChrChipByIndex(0x18, 0x1)
    Jump("loc_2D3E")

    label("loc_2CED")

    SetChrChipByIndex(0x18, 0x2)
    Jump("loc_2D3E")

    label("loc_2CF6")

    SetChrChipByIndex(0x18, 0x1E)
    Jump("loc_2D3E")

    label("loc_2CFF")

    SetChrChipByIndex(0x18, 0x1F)
    Jump("loc_2D3E")

    label("loc_2D08")

    SetChrChipByIndex(0x18, 0x3)
    Jump("loc_2D3E")

    label("loc_2D11")

    SetChrChipByIndex(0x18, 0x4)
    Jump("loc_2D3E")

    label("loc_2D1A")

    SetChrChipByIndex(0x18, 0x20)
    Jump("loc_2D3E")

    label("loc_2D23")

    SetChrChipByIndex(0x18, 0x5)
    Jump("loc_2D3E")

    label("loc_2D2C")

    SetChrChipByIndex(0x18, 0x6)
    Jump("loc_2D3E")

    label("loc_2D35")

    SetChrChipByIndex(0x18, 0x7)
    Jump("loc_2D3E")

    label("loc_2D3E")

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
        (0, "loc_2DFA"),
        (1, "loc_2F2D"),
        (2, "loc_303C"),
        (3, "loc_3156"),
        (4, "loc_3280"),
        (5, "loc_3373"),
        (6, "loc_3476"),
        (7, "loc_3579"),
        (8, "loc_369B"),
        (9, "loc_37CC"),
        (10, "loc_38EB"),
        (SWITCH_DEFAULT, "loc_3A39"),
    )


    label("loc_2DFA")


    NpcTalk(
        0x18,
        "Elie",
        (
            "#00106F#12P*sigh*... To think those\x01",
            "ghosts were so close to\x01",
            "us. I was so scared!\x02\x03",
            "#00100FWell, it wasn't as scary\x01",
            "as I thought, and I\x01",
            "certainly enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha. If you enjoyed it,\x01",
            "then I'm glad I invited\x01",
            "you.\x02\x03",
            "#00000FSee you later, then.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Elie",
        "#00100F#12PYes, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_2F2D")


    NpcTalk(
        0x18,
        "Tio",
        (
            "#00204F#12PThose looming ghosts... That\x01",
            "was quite a thrill.\x02\x03",
            "#00200FJust what you'd expect from a\x01",
            "new attraction. I understand\x01",
            "why it's so popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, I'm glad you\x01",
            "enjoyed it.\x02\x03",
            "#00000FWell then, see you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Tio",
        "#00200F#12PYes, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_303C")


    NpcTalk(
        0x18,
        "Randy",
        (
            "#00300F#12PHaha. For a horror\x01",
            "attraction, it was very\x01",
            "well made.\x02\x03",
            "#00306FToo bad you rode it with\x01",
            "me rather than some\x01",
            "pretty lady, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FW-Well you enjoyed it,\x01",
            "so isn't that fine?\x02\x03",
            "#00000FAlright then, see you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Randy",
        "#00300F#12PYeah, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_3156")


    NpcTalk(
        0x18,
        "Noｱl",
        (
            "#10100F#12P*phew*, that was really fun.\x02\x03",
            "#10109FIf we included this kind of game in\x01",
            "our CGF shooting training, I feel\x01",
            "like we'd improve quite a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, certainly... It\x01",
            "might actually happen\x01",
            "someday.\x02\x03",
            "#00000FWell then, see you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Noｱl",
        "#10100F#12PYes, see you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_3280")


    NpcTalk(
        0x18,
        "Wazy",
        (
            "#10304F#12PHehe. That was quite the\x01",
            "massive attraction, eh?\x02\x03",
            "#10302FEven someone like me was\x01",
            "hooked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FI loved it too... and\x01",
            "I'm glad you enjoyed it.\x02\x03",
            "#00000FWell then, see you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Wazy",
        "#10300F#12PHehe, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_3373")


    NpcTalk(
        0x18,
        "KeA",
        (
            "#01109F#12PWhooah, that was fuuun!\x02\x03",
            "Travelling through total\x01",
            "darkness, with the wind hitting\x01",
            "your face... It felt really good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, I'm glad you liked\x01",
            "it that much.\x02\x03",
            "#00000FWell then, see you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "KeA",
        "#01100F#12PYeah, later!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_3476")


    NpcTalk(
        0x18,
        "Fran",
        (
            "#06400F#12PWow, that was the\x01",
            "perfect thrill!\x02\x03",
            "#06409FYour shooting made it\x01",
            "even better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FIt was pretty tough with\x01",
            "that many ghosts, but...\x01",
            "I'm glad you enjoyed it.\x02\x03",
            "#00000FWell then, see you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Fran",
        "#06400F#12PYes, lateeer.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_3579")


    NpcTalk(
        0x18,
        "Cecil",
        (
            "#05900F#12PHaha, that was great\x01",
            "fun.\x02\x03",
            "#05909FAnd the image of you\x01",
            "shooting was quite\x01",
            "reassuring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha. Handling a real gun is\x01",
            "totally different you know... But\x01",
            "well, I'm glad you enjoyed it.\x02\x03",
            "#00000FSee you later, then.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Cecil",
        "#05900F#12PYes, see you later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_369B")


    NpcTalk(
        0x18,
        "Ilya",
        (
            "#01704F#12PHmm, that was just as\x01",
            "good as thought!\x02\x03",
            "#01702FHuhu. It would have been\x01",
            "better if more ghosts\x01",
            "appeared, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FO-Obviously that would have\x01",
            "been way too difficult, but...\x01",
            "Well, I'm glad you enjoyed it.\x02\x03",
            "#00000FSee you later, then.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Ilya",
        "#01700F#12PYeah, see you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_37CC")


    NpcTalk(
        0x18,
        "Rixia",
        (
            "#01802F#12P*sigh*, that was quite fun.\x02\x03",
            "#01806FIt looked like you had a hard\x01",
            "time shooting the monsters with\x01",
            "their confusing movements...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha. It was a bit\x01",
            "difficult, but I had fun\x01",
            "all the same.\x02\x03",
            "#00000FSee you later, then.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Rixia",
        "#01802F#12PYes, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_38EB")


    NpcTalk(
        0x18,
        "Sully",
        (
            "#14006F#12P*sigh*... The car was so fast. It\x01",
            "was a pretty good thrill even though\x01",
            "I couldn't open my eyes at all.\x02\x03",
            "#14002FEven so, it looks like you enjoyed\x01",
            "it. I wanted to shoot too, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha... It's harder than\x01",
            "it looks, though.\x02\x03",
            "#00000FWell then, see you\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Sully",
        "#14000F#12PYeah, later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A39")

    label("loc_3A39")


    def lambda_3A3E():

        label("loc_3A3E")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_3A3E")

    QueueWorkItem2(0x101, 2, lambda_3A3E)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_3A57():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3A57)
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
        (0, "loc_3AD4"),
        (1, "loc_3AE2"),
        (2, "loc_3AF0"),
        (3, "loc_3AFE"),
        (4, "loc_3B0C"),
        (5, "loc_3B1A"),
        (6, "loc_3B28"),
        (7, "loc_3B36"),
        (8, "loc_3B44"),
        (9, "loc_3B52"),
        (10, "loc_3B60"),
        (SWITCH_DEFAULT, "loc_3B6E"),
    )


    label("loc_3AD4")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3AE2")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3AF0")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3AFE")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3B0C")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3B1A")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3B28")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3B36")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3B44")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3B52")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3B60")

    OP_D2(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3B6E")

    label("loc_3B6E")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B94")
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_3B94")

    Call(0, 23)
    OP_4C(0x13, 0xFF)
    SetChrPos(0x0, 0, 0, -2000, 180)
    EventEnd(0x5)
    Return()

    # Function_24_2C69 end

    def Function_25_3BAF(): pass

    label("Function_25_3BAF")

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
            "Jeez, to think you found\x01",
            "four times so quickly...\x01",
            "Unbelievable~.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Mishishi, you're totally\x01",
            "different from my stupid big\x01",
            "brother Mishy, you know?☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_3DE2")
    OP_63(0x153, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jump("loc_3DFA")

    label("loc_3DE2")

    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3DFA")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Mishette is pretty\x01",
            "harsh toward Mishy,\x01",
            "huh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "...Mrr, this is the last\x01",
            "time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "Alllright, I'll hide in a more\x01",
            "difficult place for this last one,\x01",
            "so do your best to find me, ok?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3ED1():

        label("loc_3ED1")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_3ED1")

    QueueWorkItem2(0x101, 1, lambda_3ED1)

    def lambda_3EE3():

        label("loc_3EE3")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_3EE3")

    QueueWorkItem2(0xEF, 1, lambda_3EE3)
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
            "#00006FFinally, the last hiding\x01",
            "place, huh...\x02\x03",
            "#00000FBecause it's just inside the\x01",
            "theme park, I don't think\x01",
            "it'll be that difficult...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_4042")

    ChrTalk(
        0x102,
        (
            "#00100FThen, let's go look for\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_4042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_4079")

    ChrTalk(
        0x103,
        (
            "#00200FThen, let's go look for\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_4079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_40B6")

    ChrTalk(
        0x104,
        (
            "#00300FThen, let's go look for\x01",
            "her, yeah?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_40B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_40ED")

    ChrTalk(
        0x109,
        (
            "#10100FThen, let's go look for\x01",
            "her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_40ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_4128")

    ChrTalk(
        0x105,
        (
            "#10300FThen, let's go look for\x01",
            "her, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_4128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_4157")

    ChrTalk(
        0x153,
        "#01100FThen, let's go look!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_4157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_4199")

    ChrTalk(
        0x156,
        (
            "#06400Fそれじゃあ、\x01",
            "探しに行ってみましょう～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_4199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_41D5")

    ChrTalk(
        0x14C,
        (
            "#05900FHaha, then let's go look\x01",
            "for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_41D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4211")

    ChrTalk(
        0x134,
        (
            "#01700FHuhu. Then let's go look\x01",
            "for her!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_4211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4248")

    ChrTalk(
        0x135,
        (
            "#01802FThen, let's go look for\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4274")

    label("loc_4248")


    ChrTalk(
        0x166,
        (
            "#14000FThen let's go look for\x01",
            "her, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4274")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xE)
    SetScenarioFlags(0x1C9, 6)
    SetChrPos(0x0, 160, 0, -12030, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_3BAF end

    def Function_26_42A0(): pass

    label("Function_26_42A0")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's a sketch map of the\x01",
            "theme park.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_26_42A0 end

    SaveToFile()

Try(main)
