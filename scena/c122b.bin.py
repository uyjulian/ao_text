from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c122b.bin",                # FileName
        "c122b",                    # MapName
        "c122b",                    # Location
        0x0020,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c122b",                  # 0
        "Receptionist Tria",           # 1
        "Grace",               # 2
        "Raines",               # 3
        "Makkenen",             # 4
        "Editor-in-chief",                 # 5
        "Ozel",               # 6
        "Engineer",                   # 7
        "A hunter",                   # 8
        "A hunter",                   # 9
        "bc122b",                 # 10
    ))

    ATBonus("ATBonus_268", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_288", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_30C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_310", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_314", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_318", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_31C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_320", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_328", 0x004A, 3, 6, 45, 3, 3, 30, 0, "bc122b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41900.dat", "ms41900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7544", "ed7453", "ATBonus_268"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch26600.itc",                   # 00
        "chr/ch26602.itc",                   # 01
        "chr/ch06000.itc",                   # 02
        "chr/ch28100.itc",                   # 03
        "chr/ch26700.itc",                   # 04
        "chr/ch20200.itc",                   # 05
        "chr/ch25200.itc",                   # 06
        "chr/ch25202.itc",                   # 07
        "chr/ch26000.itc",                   # 08
    ))

    DeclNpc(5789,    0,       4294966866, 270,  389,  0x0, 0,   1,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(60619,   0,       11819,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(59009,   0,       11810,   90,   389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(5099,    0,       60020,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(65879,   0,       129,     89,   389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(300,     0,       56950,   180,  389,  0x0, 0,   7,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(67139,   0,       4294966977, 90,   389,  0x0, 0,   8,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   8,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    449,  0x0, 0,   8,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 24,  -6.369999885559082,    4.800000190734863,     0.0,                   6.25,                  [0.40000003576278687,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   2.5480000972747803,    -2.4000000953674316,   -0.0,                  1.0])

    DeclActor(4100,    0,       4294966776, 1500,    5500,    1800,    4294966826, 0x007E, 0,  3,  0x0000)

    ChipFrameInfo(1008, 0)                                       # 0

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_4A0",          # 01, 1
        "Function_2_59C",          # 02, 2
        "Function_3_5EF",          # 03, 3
        "Function_4_8B9",          # 04, 4
        "Function_5_A34",          # 05, 5
        "Function_6_B69",          # 06, 6
        "Function_7_E8C",          # 07, 7
        "Function_8_1000",         # 08, 8
        "Function_9_1077",         # 09, 9
        "Function_10_110E",        # 0A, 10
        "Function_11_1C56",        # 0B, 11
        "Function_12_1C90",        # 0C, 12
        "Function_13_1CDE",        # 0D, 13
        "Function_14_1D18",        # 0E, 14
        "Function_15_1D3E",        # 0F, 15
        "Function_16_1D82",        # 10, 16
        "Function_17_1DD0",        # 11, 17
        "Function_18_1E00",        # 12, 18
        "Function_19_1E30",        # 13, 19
        "Function_20_1E4C",        # 14, 20
        "Function_21_1E68",        # 15, 21
        "Function_22_1E84",        # 16, 22
        "Function_23_1EA0",        # 17, 23
        "Function_24_1EBC",        # 18, 24
        "Function_25_21DB",        # 19, 25
        "Function_26_21F0",        # 1A, 26
        "Function_27_2219",        # 1B, 27
        "Function_28_2242",        # 1C, 28
        "Function_29_2C79",        # 1D, 29
        "Function_30_3A3B",        # 1E, 30
        "Function_31_3A96",        # 1F, 31
        "Function_32_3B3E",        # 20, 32
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_428"),
        (1, "loc_434"),
        (2, "loc_440"),
        (3, "loc_44C"),
        (4, "loc_458"),
        (5, "loc_464"),
        (6, "loc_470"),
        (SWITCH_DEFAULT, "loc_47C"),
    )


    label("loc_428")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_434")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_440")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_44C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_458")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_464")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_470")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_47C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_488")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_488")

    label("loc_49F")

    Return()

    # Function_0_3F0 end

    def Function_1_4A0(): pass

    label("Function_1_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AE")
    Jump("loc_55D")

    label("loc_4AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_55D")
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_END)), "loc_528")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0xD, 0x7)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514")
    SetChrFlags(0xA, 0x10)

    label("loc_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523")
    SetChrFlags(0x9, 0x10)

    label("loc_523")

    Jump("loc_55D")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 1)), scpexpr(EXPR_END)), "loc_555")
    SetChrChipByIndex(0x8, 0x0)
    SetChrChipByIndex(0xD, 0x6)
    SetChrPos(0x8, 3450, 20, -20, 270)
    BeginChrThread(0x8, 0, 0, 0)
    Jump("loc_55D")

    label("loc_555")

    SetChrChipByIndex(0x8, 0x0)
    SetChrChipByIndex(0xD, 0x6)

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_578")
    Event(0, 10)
    Jump("loc_59B")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59B")
    Event(0, 28)

    label("loc_59B")

    Return()

    # Function_1_4A0 end

    def Function_2_59C(): pass

    label("Function_2_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B2")
    OP_70(0xB, 0xB)

    label("loc_5B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CD")
    OP_66(0x0, 0x1)
    Jump("loc_5D1")

    label("loc_5CD")

    OP_65(0x0, 0x1)

    label("loc_5D1")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5EE")

    Return()

    # Function_2_59C end

    def Function_3_5EF(): pass

    label("Function_3_5EF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_600")
    Jump("loc_8B5")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_8B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_END)), "loc_730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B5")

    ChrTalk(
        0x8,
        (
            "Please help everyone safely\x01",
            "I'm really thankful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you were not there,\x01",
            "I am still in one corner of the drawing room\x01",
            "It may have been trembling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_72B")

    label("loc_6B5")


    ChrTalk(
        0x8,
        (
            "If you were not there,\x01",
            "I am still in one corner of the drawing room\x01",
            "It may have been trembling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I'm really thankful to you.\x02",
    )

    CloseMessageWindow()

    label("loc_72B")

    Jump("loc_8B5")

    label("loc_730")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "speak\x01",          # 0
            "Rest\x01",      # 1
            "quit\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_785"),
        (1, "loc_80E"),
        (2, "loc_8B0"),
        (SWITCH_DEFAULT, "loc_8B5"),
    )


    label("loc_785")


    ChrTalk(
        0x8,
        (
            "(Since there is an emergency box,\x01",
            "I think that first aid measures can be done. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(About Mr. Grays … ….\x01",
            "Thank you. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B5")

    label("loc_80E")


    ChrTalk(
        0x8,
        (
            "(I understand,\x01",
            "Please stay still. )\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "(About Mr. Grays … ….\x01",
            "Thank you. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B5")

    label("loc_8B0")

    Jump("loc_8B5")

    label("loc_8B5")

    TalkEnd(0x8)
    Return()

    # Function_3_5EF end

    def Function_4_8B9(): pass

    label("Function_4_8B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8CA")
    Jump("loc_A30")

    label("loc_8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_A30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A6")

    ChrTalk(
        0xFE,
        (
            "Whew, things like that\x01",
            "I got involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nobody has been hurt but salvation … …\x01",
            "Grace is also playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's good to be victorious, but that's how it is\x01",
            "No matter how many life there are, it is not enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A30")

    label("loc_9A6")


    ChrTalk(
        0xFE,
        (
            "Nobody has been hurt but salvation … …\x01",
            "Grace is also playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's good to be victorious, but that's how it is\x01",
            "No matter how many life there are, it is not enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A30")

    TalkEnd(0xFE)
    Return()

    # Function_4_8B9 end

    def Function_5_A34(): pass

    label("Function_5_A34")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A45")
    Jump("loc_B65")

    label("loc_A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B02")

    ChrTalk(
        0xFE,
        (
            "As I came to see him here,\x01",
            "The men who were armed men aged\x01",
            "It suddenly came in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Outside is a serious thing,\x01",
            "I have kept it as it is\x01",
            "Will my stalls be okay …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B65")

    label("loc_B02")


    ChrTalk(
        0xFE,
        (
            "To behave noodles with cross bells\x01",
            "My stalls that have been accompanied by pleasure for many years ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I hope it is safe.\x02",
    )

    CloseMessageWindow()

    label("loc_B65")

    TalkEnd(0xFE)
    Return()

    # Function_5_A34 end

    def Function_6_B69(): pass

    label("Function_6_B69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B7A")
    Jump("loc_E88")

    label("loc_B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF7")
    OP_4B(0xA, 0x0)

    ChrTalk(
        0xFE,
        "#02101FRains, you got a camera!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, it is ready!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FMr. Grace ……\x01",
            "Are you going to interview! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FOutside is quite dangerous,\x01",
            "It is better to stop … …\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "#02103FWhat are you saying, this great incident\x01",
            "I can not miss it!\x02\x03",
            "#02101FAs a journalist,\x01",
            "Catch the truth with this eye\x01",
            "There is a mission to tell citizens!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F… … It seems useless to stop it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FFuu … Looks like that.\x02\x03",
            "#00001FIt is a situation I do not know what will happen.\x01",
            "Please take more than enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02102FHuh, you know.\x02\x03",
            "Lloyd, you too\x01",
            "Be careful!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 3)
    OP_4C(0xA, 0x0)
    Jump("loc_E88")

    label("loc_DF7")


    ChrTalk(
        0xFE,
        (
            "#02103FSuch a big incident, absolutely\x01",
            "I can not miss it!\x02\x03",
            "#02101FAs a journalist,\x01",
            "It tells the citizen the truth\x01",
            "Because there is a mission!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E88")

    TalkEnd(0xFE)
    Return()

    # Function_6_B69 end

    def Function_7_E8C(): pass

    label("Function_7_E8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E9D")
    Jump("loc_FFC")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_FFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6D")
    OP_4B(0x9, 0x0)

    ChrTalk(
        0x9,
        (
            "#02102FRains, I beg you to do my best!\x02\x03",
            "#02109FShow me your chest like I was a while ago\x01",
            "Follow me firmly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, that is real,\x01",
            "It is said that the body has just moved ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xFE, 0x10)
    OP_4C(0x9, 0x0)
    Jump("loc_FFC")

    label("loc_F6D")


    ChrTalk(
        0xFE,
        (
            "Well, but it can not be helped.\x01",
            "Being a senior partner,\x01",
            "You can not avoid danger … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When it comes to this,\x01",
            "I will take more pictures!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFC")

    TalkEnd(0xFE)
    Return()

    # Function_7_E8C end

    def Function_8_1000(): pass

    label("Function_8_1000")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1011")
    Jump("loc_1073")

    label("loc_1011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_1073")

    ChrTalk(
        0xFE,
        (
            "The communication device was not destroyed\x01",
            "It is fortunate to be unhappy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "As soon as someone, I have to call for help ……!\x02",
    )

    CloseMessageWindow()

    label("loc_1073")

    TalkEnd(0xFE)
    Return()

    # Function_8_1000 end

    def Function_9_1077(): pass

    label("Function_9_1077")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1088")
    Jump("loc_110A")

    label("loc_1088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_110A")

    ChrTalk(
        0xFE,
        (
            "It happened to come to maintenance of the communication device\x01",
            "I fell for such a scary eye ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, I do not like my luck.\x02",
    )

    CloseMessageWindow()

    label("loc_110A")

    TalkEnd(0xFE)
    Return()

    # Function_9_1077 end

    def Function_10_110E(): pass

    label("Function_10_110E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 1470, 0, -5130, 0)
    SetChrPos(0x1, 1470, 0, -5130, 0)
    SetChrPos(0x2, 1470, 0, -5130, 0)
    SetChrPos(0x3, 1470, 0, -5130, 0)
    SetChrPos(0x4, 1470, 0, -5130, 0)
    SetChrPos(0x5, 1470, 0, -5130, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 8180, 0, 4000, 225)
    OP_68(1600, 1500, -3250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    OP_68(1800, 1500, -1130, 4000)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 1, 0, 11)
    Sleep(500)
    BeginChrThread(0x102, 1, 0, 12)
    Sleep(500)
    BeginChrThread(0x104, 1, 0, 13)
    Sleep(500)
    BeginChrThread(0x103, 1, 0, 14)
    Sleep(500)
    BeginChrThread(0x109, 1, 0, 15)
    Sleep(500)
    BeginChrThread(0x105, 1, 0, 16)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x101,
        "#00013F#5PIt's awfully silent … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PGrace's are\x01",
            "Did he escape to another place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_64(0x104)

    ChrTalk(
        0x103,
        (
            "#00201F#12PNo, from inside the building\x01",
            "There are multiple people 's reactions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6PHowever, this indication ……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 10, -1, -1)
    SetChrName("Female voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1SMi, everyone ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(4180, 1500, -890, 2500)
    MoveCamera(36, 20, 0, 2500)

    def lambda_1444():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1444)
    Sleep(50)

    def lambda_1454():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1454)
    Sleep(50)

    def lambda_1464():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1464)
    Sleep(50)

    def lambda_1474():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1474)
    Sleep(50)

    def lambda_1484():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1484)
    Sleep(50)

    def lambda_1494():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1494)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    SetChrFlags(0x8, 0x40)
    Sleep(1500)
    OP_74(0x0, 0x3)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    Sound(103, 0, 100, 0)
    Sleep(400)
    OP_96(0x8, 0x1FF4, 0x0, 0x9C4, 0x2BC, 0x0)
    OP_79(0x0)

    ChrTalk(
        0x101,
        "#00005F#6PYou are the receptionist …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P(Shu … … quietly.)\x02",
    )

    CloseMessageWindow()
    OP_68(3440, 1500, -1740, 2500)
    MoveCamera(36, 16, 0, 2500)
    OP_6E(400, 2500)
    SetCameraDistance(20500, 2500)
    OP_74(0x0, 0x3)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)

    def lambda_1571():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1571)

    def lambda_157E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_157E)

    def lambda_158B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_158B)

    def lambda_1598():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1598)

    def lambda_15A5():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15A5)

    def lambda_15B2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_15B2)
    BeginChrThread(0x8, 1, 0, 17)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Sleep(1000)
    Sleep(300)
    Sound(104, 0, 70, 0)
    BeginChrThread(0x101, 1, 0, 18)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 20)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 23)
    Sleep(50)
    BeginChrThread(0x102, 1, 0, 19)
    Sleep(60)
    BeginChrThread(0x103, 1, 0, 21)
    Sleep(60)
    BeginChrThread(0x109, 1, 0, 22)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x109,
        "#10101F#6P(No, what happened?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P(Actually ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(As mentioned earlier, people with guns\x01",
            "It suddenly invaded the building. )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105F#6P(Well …… !?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6P(After all ……)\x02\x03",
            "#00301F(Are hunters rampaging outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(And it was because it was sudden\x01",
            "I do not know the detail, but ……\x01",
            "I think it is likely. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(People at the communications company,\x01",
            "In the immediate faced guns\x01",
            "I was restrained. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(I was hiding behind the scenes\x01",
            "I was able to pass through … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6P(It was a happy happiness.)\x02\x03",
            "#10301F(So where are they guys now?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(That's … on the upper floor\x01",
            "It seems there are 2 people left … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(Outside is such a situation,\x01",
            "I can not even call for help ……\x01",
            "What do you think? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6P(… … I understand the circumstances.\x01",
            "For the time being\x01",
            "Please leave it to us. )\x02\x03",
            "(Grace says\x01",
            "I will definitely help out. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P(Oh …… Thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6P(If you decide so, prepare thoroughly\x01",
            "It seems better to prepare. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6P(The opponent is a hunter,\x01",
            "Being too careful is\x01",
            "There will be no. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(If I have something I can do\x01",
            "Please do not hesitate to tell us. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(Since there is an emergency box,\x01",
            "I think that first aid measures can be done. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P(Yes, thank you.)\x02\x03",
            "#00007F(OK, well … when I get ready\x01",
            "We will enter the second floor! )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, 3450, 20, -20, 270)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x8, 0x40)
    OP_74(0x0, 0x1E)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 1250, 0, -1520, 225)
    SetScenarioFlags(0x192, 1)
    OP_29(0xAB, 0x1, 0x1)
    ModifyEventFlags(1, 0, 0x80)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_10_110E end

    def Function_11_1C56(): pass

    label("Function_11_1C56")


    def lambda_1C5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C5B)
    OP_95(0xFE, 1610, 0, -520, 2000, 0x0)
    Sleep(250)
    OP_93(0xFE, 0x13B, 0xFA)
    Sleep(250)
    OP_93(0xFE, 0x2D, 0xFA)
    Return()

    # Function_11_1C56 end

    def Function_12_1C90(): pass

    label("Function_12_1C90")


    def lambda_1C95():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C95)
    OP_95(0xFE, 1000, 0, -2300, 2000, 0x0)
    OP_95(0xFE, 530, 0, -1340, 2000, 0x0)
    Sleep(250)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(250)
    OP_93(0xFE, 0x13B, 0x12C)
    Return()

    # Function_12_1C90 end

    def Function_13_1CDE(): pass

    label("Function_13_1CDE")


    def lambda_1CE3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1CE3)
    OP_95(0xFE, 2000, 0, -2300, 2000, 0x0)
    OP_95(0xFE, 2470, 20, -1230, 2000, 0x0)
    Return()

    # Function_13_1CDE end

    def Function_14_1D18(): pass

    label("Function_14_1D18")


    def lambda_1D1D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1D1D)
    OP_95(0xFE, 1720, 0, -2230, 2000, 0x0)
    Return()

    # Function_14_1D18 end

    def Function_15_1D3E(): pass

    label("Function_15_1D3E")


    def lambda_1D43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1D43)
    OP_95(0xFE, 1000, 0, -3300, 2000, 0x0)
    OP_95(0xFE, 280, 0, -2730, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x12C)
    Return()

    # Function_15_1D3E end

    def Function_16_1D82(): pass

    label("Function_16_1D82")


    def lambda_1D87():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1D87)
    OP_95(0xFE, 1700, 0, -3300, 2000, 0x0)
    OP_95(0xFE, 2270, 0, -3040, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0xC8)
    Sleep(300)
    OP_93(0xFE, 0x2D, 0xC8)
    Return()

    # Function_16_1D82 end

    def Function_17_1DD0(): pass

    label("Function_17_1DD0")

    OP_95(0xFE, 7020, 0, 960, 2000, 0x0)
    OP_95(0xFE, 5640, 0, 320, 2000, 0x0)
    TurnDirection(0xFE, 0x109, 500)
    Return()

    # Function_17_1DD0 end

    def Function_18_1E00(): pass

    label("Function_18_1E00")

    OP_95(0xFE, 2029, 0, 180, 2000, 0x0)
    OP_95(0xFE, 3010, 20, 160, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_18_1E00 end

    def Function_19_1E30(): pass

    label("Function_19_1E30")

    OP_95(0xFE, 1750, 0, 230, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_19_1E30 end

    def Function_20_1E4C(): pass

    label("Function_20_1E4C")

    OP_95(0xFE, 3250, 20, -880, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_20_1E4C end

    def Function_21_1E68(): pass

    label("Function_21_1E68")

    OP_95(0xFE, 2100, 20, -1790, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_21_1E68 end

    def Function_22_1E84(): pass

    label("Function_22_1E84")

    OP_95(0xFE, 2040, 0, -640, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_22_1E84 end

    def Function_23_1EA0(): pass

    label("Function_23_1EA0")

    OP_95(0xFE, 3080, 20, -2350, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_23_1EA0 end

    def Function_24_1EBC(): pass

    label("Function_24_1EBC")

    EventBegin(0x0)
    Fade(500)
    OP_68(-6720, 1520, 2430, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -6560, 0, 3910, 0)
    SetChrPos(0x104, -5880, 20, 3120, 315)
    SetChrPos(0x102, -7120, 20, 2670, 0)
    SetChrPos(0x109, -5320, 0, 2130, 315)
    SetChrPos(0x103, -6570, 0, 1720, 0)
    SetChrPos(0x105, -5760, 0, 1130, 315)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00001F#5P(On this, Grace says\x01",
            "It is bound by a hunter … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#11P(Lloyd, will you soon?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "To rush\x01",                # 0
            "I am not ready\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2034"),
        (SWITCH_DEFAULT, "loc_2111"),
    )


    label("loc_2034")


    ChrTalk(
        0x101,
        "#00007F#5P(Oh … I will go, everyone!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F(Yes, sir!)\x02",
    )

    CloseMessageWindow()
    OP_68(-7710, 2920, 3910, 1500)
    MoveCamera(45, 21, 0, 1500)
    OP_6E(380, 1500)
    SetCameraDistance(15500, 1500)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x101, 1, 0, 25)
    Sleep(50)
    BeginChrThread(0x104, 1, 0, 27)
    Sleep(60)
    BeginChrThread(0x102, 1, 0, 26)
    Sleep(50)
    BeginChrThread(0x109, 1, 0, 27)
    Sleep(60)
    BeginChrThread(0x103, 1, 0, 26)
    Sleep(50)
    BeginChrThread(0x105, 1, 0, 27)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x105, 0x1)
    NewScene("c122B", 104, 0, 0)
    IdleLoop()
    Jump("loc_21DA")

    label("loc_2111")


    ChrTalk(
        0x104,
        (
            "#00303F#11P(Really……)\x02\x03",
            "#00301F(If the rescue is delayed, hunters also\x01",
            "I do not know what to do.\x01",
            "I will finally get ready! )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5P(Ah……!)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -6510, 20, 2640, 180)
    EventEnd(0x5)
    Jump("loc_21DA")

    label("loc_21DA")

    Return()

    # Function_24_1EBC end

    def Function_25_21DB(): pass

    label("Function_25_21DB")

    OP_95(0xFE, -6440, 3730, 7730, 4000, 0x0)
    Return()

    # Function_25_21DB end

    def Function_26_21F0(): pass

    label("Function_26_21F0")

    OP_95(0xFE, -7000, 0, 4000, 4000, 0x0)
    OP_95(0xFE, -7000, 3730, 7730, 4000, 0x0)
    Return()

    # Function_26_21F0 end

    def Function_27_2219(): pass

    label("Function_27_2219")

    OP_95(0xFE, -5800, 0, 4000, 4000, 0x0)
    OP_95(0xFE, -5800, 3730, 7730, 4000, 0x0)
    Return()

    # Function_27_2219 end

    def Function_28_2242(): pass

    label("Function_28_2242")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 30)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xE, 0x40)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrChipByIndex(0xD, 0x6)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrPos(0xE, 67690, 0, 12730, 225)
    SetChrPos(0xB, 67190, 0, 11890, 225)
    SetChrPos(0xD, 67780, 0, 11680, 180)
    SetChrPos(0xC, 66950, 0, 13050, 225)
    SetChrPos(0xA, 66550, 0, 12150, 270)
    SetChrPos(0x9, 66060, 0, 13000, 270)
    SetChrPos(0xF, 63430, 0, 12700, 90)
    SetChrPos(0x10, 67400, 0, 8550, 0)
    OP_68(61700, 1500, 7460, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26000, 0)
    OP_70(0xB, 0x0)
    FadeToBright(2000, 0)
    OP_68(65910, 1500, 11380, 4000)
    MoveCamera(45, 20, 0, 4000)
    OP_6E(400, 0)
    SetCameraDistance(19500, 4000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#02101F#11P……you,\x01",
            "Stop making foolishly!\x02\x03",
            "I attacked the city,\x01",
            "What on earth are you going to be! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We have our aim … …\x01",
            "It has nothing to do with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Do not worry, as long as you are quiet\x01",
            "There is no harm done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If it can not be done ……\x01",
            "I will force you to be quiet.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xE,
        "#5PHi there, …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PSo, I just came to see you\x01",
            "Why is this ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#02104F#11PHun, not superior …!\x02\x03",
            "#02102FWith one or two such threats,\x01",
            "If I think I'm frightened\x01",
            "Because it is a big mistake!\x02\x03",
            "If it can do it\x01",
            "Try it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#11PGrace, not much\x01",
            "What is irritating … …!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0xA, 0x10158, 0x0, 0x307A, 0x5DC, 0x0)

    ChrTalk(
        0xA,
        (
            "#11PWait a moment, please!\x01",
            "Senior, hold down here … …!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        (
            "#11P#4SOh, you!\x01",
            "I will not forgive you for this person!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2701():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2701)

    def lambda_270E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_270E)
    Sleep(50)

    def lambda_271E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_271E)

    def lambda_272B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_272B)
    Sleep(50)

    def lambda_273B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_273B)

    def lambda_2748():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2748)

    ChrTalk(
        0x9,
        "#02105F#5PLes, Rains … …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hun, he's a reporter who settled … …\x01",
            "However, I am not planning to take a provocation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Until the strategy is completed\x01",
            "Let me be grown-up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PStrategy … What on earth are you going to do?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 54080, 0, 12770, 90)
    SetChrPos(0x104, 53960, 0, 11780, 90)
    SetChrPos(0x102, 52770, 0, 12870, 90)
    SetChrPos(0x103, 52610, 0, 11860, 90)
    SetChrPos(0x109, 51500, 0, 12880, 90)
    SetChrPos(0x105, 51610, 0, 11990, 90)
    SetChrChipByIndex(0x101, 0x21)
    SetChrChipByIndex(0x104, 0x27)
    SetChrChipByIndex(0x102, 0x23)
    SetChrChipByIndex(0x103, 0x25)
    SetChrChipByIndex(0x109, 0x29)
    SetChrChipByIndex(0x105, 0x2B)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(0, 200, -1, -1)
    SetChrName("Voice of Lloyd")
    Sound(2090, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4S── That's it there! It is!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_29B9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_29B9)

    def lambda_29C6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_29C6)
    Sleep(50)

    def lambda_29D6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_29D6)

    def lambda_29E3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_29E3)
    OP_68(61890, 1500, 11620, 1800)
    MoveCamera(45, 13, 0, 1800)
    OP_6E(460, 1800)
    SetCameraDistance(19500, 1800)

    def lambda_2A1E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A1E)
    Sleep(50)

    def lambda_2A36():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A36)
    Sleep(50)

    def lambda_2A4E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A4E)
    Sleep(50)

    def lambda_2A66():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A66)
    Sleep(50)

    def lambda_2A7E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A7E)
    Sleep(50)

    def lambda_2A96():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2A96)
    Sleep(600)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0xF,
        "#11PYou guys ……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#02105F#11PLloyd guys! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PCaptain Randolph!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#5PSuppression will start! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#5PYou're gonna go! It is!\x02",
    )

    CloseMessageWindow()

    def lambda_2B70():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B70)

    def lambda_2B85():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B85)

    def lambda_2B9A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B9A)

    def lambda_2BAF():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BAF)

    def lambda_2BC4():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2BC4)

    def lambda_2BD9():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2BD9)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_68(61890, 1500, 11620, 250)
    MoveCamera(45, 15, 0, 250)
    OP_6E(460, 250)
    SetCameraDistance(15300, 250)
    Sleep(250)
    CancelBlur(200)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrChipByIndex(0x101, 0x21)
    SetChrChipByIndex(0x104, 0x27)
    SetChrChipByIndex(0x102, 0x23)
    SetChrChipByIndex(0x103, 0x25)
    SetChrChipByIndex(0x109, 0x29)
    SetChrChipByIndex(0x105, 0x2B)
    Battle("BattleInfo_328", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 29)
    Return()

    # Function_28_2242 end

    def Function_29_2C79(): pass

    label("Function_29_2C79")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 30)
    SetChrChipByIndex(0xF, 0x20)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0xF, 0x3)
    SetChrSubChip(0x10, 0x3)
    SetChrPos(0xF, 63550, 0, 12500, 270)
    SetChrPos(0x10, 64680, 0, 11840, 270)
    SetChrPos(0x101, 61080, 0, 12770, 90)
    SetChrPos(0x104, 60960, 0, 11780, 90)
    SetChrPos(0x102, 59770, 0, 12870, 90)
    SetChrPos(0x103, 59610, 0, 11860, 90)
    SetChrPos(0x109, 58500, 0, 12880, 90)
    SetChrPos(0x105, 58610, 0, 11990, 90)
    SetChrChipByIndex(0x101, 0x21)
    SetChrChipByIndex(0x104, 0x27)
    SetChrChipByIndex(0x102, 0x23)
    SetChrChipByIndex(0x103, 0x25)
    SetChrChipByIndex(0x109, 0x29)
    SetChrChipByIndex(0x105, 0x2B)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0xE, 67690, 0, 12730, 270)
    SetChrPos(0xB, 67190, 0, 11890, 270)
    SetChrPos(0xD, 67780, 0, 11680, 270)
    SetChrPos(0xC, 66950, 0, 13050, 270)
    SetChrPos(0xA, 66300, 0, 12150, 270)
    SetChrPos(0x9, 66060, 0, 13000, 270)
    LoadEffect(0x0, "event\\ev307_00.eff")
    OP_68(62190, 1500, 11630, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(16800, 0)
    FadeToBright(2000, 0)
    SetCameraDistance(16000, 2000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xF,
        "#5PCut …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PYou seem to have no choice but to retreat here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6Pwhat……! Is it?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 31)
    Sleep(200)
    BeginChrThread(0xF, 1, 0, 31)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(300)
    OP_68(65200, 1500, 11630, 2000)
    SetCameraDistance(16300, 2000)
    OP_6F(0x79)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xF, 2)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x10, 2)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    Sleep(1000)
    OP_68(62930, 1500, 11660, 2000)
    SetCameraDistance(17630, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00310F#5PChit … did you let it get away?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PThey want to hear various things\x01",
            "I had it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    OP_0D()
    OP_68(63150, 1600, 11590, 2000)
    MoveCamera(45, 17, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(17430, 2000)

    def lambda_302B():
        OP_9B(0x0, 0xFE, 0x0, 0x6A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_302B)
    Sleep(50)

    def lambda_3043():
        OP_9B(0x0, 0xFE, 0x0, 0x6A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3043)
    Sleep(50)

    def lambda_305B():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_305B)
    Sleep(50)

    def lambda_3073():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3073)
    Sleep(50)

    def lambda_308B():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_308B)
    Sleep(50)

    def lambda_30A3():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_30A3)
    Sleep(50)

    def lambda_30BB():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_30BB)
    Sleep(50)

    def lambda_30D3():
        OP_9B(0x0, 0xFE, 0xFFFB, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_30D3)
    Sleep(50)

    def lambda_30EB():
        OP_9B(0x0, 0xFE, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_30EB)
    Sleep(50)

    def lambda_3103():
        OP_9B(0x0, 0xFE, 0xFFFB, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3103)
    Sleep(50)

    def lambda_311B():
        OP_9B(0x0, 0xFE, 0x0, 0x514, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_311B)
    Sleep(50)

    def lambda_3133():
        OP_9B(0x0, 0xFE, 0xFFFB, 0x514, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3133)
    Sleep(50)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0x9,
        "#02110F#11PLloyd guys, all right! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PMr. Graces …\x01",
            "Are you injured?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11POh, thanks.\x01",
            "Everyone is intact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PIt is a place I am going to call my best friend.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhew, Grace you too\x01",
            "It makes me messy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PHonestly my liver has cooled … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02109F#11PHaha, hey\x01",
            "It got hot.\x02\x03",
            "#02104FAs a professional journalist,\x01",
            "To succumb to violence\x01",
            "I will not go.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#02110FEven so\x01",
            "Rains has also reviewed it!\x02\x03",
            "#02109FIt is said that he will shield me\x01",
            "To be honest, I did not think so?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        (
            "#12POh, haha,\x01",
            "What he is crazy about,\x01",
            "I guess the body has moved ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PNo no …\x01",
            "It was a fine day, youth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5PHuhu, anything\x01",
            "Everyone seems to be safe and what is more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PEven so ……\x01",
            "Why do hunters communicate?\x01",
            "I guess it was aimed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PIt certainly comes to mind.\x02\x03",
            "#00208F\"Black moon\" still,\x01",
            "It seems to be important for them\x01",
            "I can not see it in the place ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3516():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3516)
    Sleep(50)

    def lambda_3526():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3526)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x9,
        (
            "#02106F#11POh, maybe there.\x02\x03",
            "#02101FIt is placed in the far side\x01",
            "Were you aiming for international communication equipment?\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(67640, 1600, -250, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(20820, 0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(30, 200, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013FInternational communication equipment …… as a standalone to foreign countries\x01",
            "Is it a communicator that can let out a conductive wave?\x02\x03",
            "#00008FIntervention from around the Republic\x01",
            "Is it the purpose to prevent …?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10303FHum, that possibility\x01",
            "There may be.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 0, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02101FWell, maybe no doubt.\x02\x03",
            "First and foremost in the port area\x01",
            "It seems I kept down here.\x02\x03",
            "#02106FBecause it was so sudden\x01",
            "To be honest, I was surprised.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(63150, 1600, 11590, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(17430, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00303F#6PThen …\x01",
            "You better be in a hurry.\x02\x03",
            "#00301FNow that I have crushed \"Black Moon\"\x01",
            "They went to IBC\x01",
            "What are you going to do ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5POh …… so far that you are careful\x01",
            "I do not seem to be even just for Mira.\x02\x03",
            "#00013FEveryone stay in the building.\x01",
            "Until things settled,\x01",
            "Please never go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11POh, ah … … I will do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PAre you going to go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02103F#11PPlease be careful!\x02\x03",
            "#02101FIf this incident can be solved,\x01",
            "Surely I will organize a special feature on one side!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#6PHaha ……\x01",
            "I will only accept your feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#5PWell then, everyone go!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19820, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_49()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
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
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_D7(0x2B)
    OP_D7(0x2C)
    SetScenarioFlags(0x192, 2)
    OP_2C(0xAB, 0x2)
    OP_29(0xAB, 0x1, 0x2)
    NewScene("c122B", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_29_2C79 end

    def Function_30_3A3B(): pass

    label("Function_30_3A3B")

    LoadChrToIndex("chr/ch41950.itc", 0x1E)
    LoadChrToIndex("chr/ch41951.itc", 0x1F)
    LoadChrToIndex("chr/ch41953.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x21)
    LoadChrToIndex("chr/ch00051.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00151.itc", 0x24)
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    LoadChrToIndex("chr/ch00251.itc", 0x26)
    LoadChrToIndex("chr/ch00350.itc", 0x27)
    LoadChrToIndex("chr/ch00351.itc", 0x28)
    LoadChrToIndex("chr/ch02950.itc", 0x29)
    LoadChrToIndex("chr/ch02951.itc", 0x2A)
    LoadChrToIndex("chr/ch03050.itc", 0x2B)
    LoadChrToIndex("chr/ch03051.itc", 0x2C)
    Return()

    # Function_30_3A3B end

    def Function_31_3A96(): pass

    label("Function_31_3A96")

    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 66500, 0, 11400, 5000, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)

    label("loc_3AF9")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x2)
    SetChrChip(0x0, 0xFE, 0x32, 0xC8)
    Sound(534, 0, 80, 0)
    OP_9C(0xFE, 0x1388, 0x0, 0x0, 0x514, 0xBB8)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_3A96 end

    def Function_32_3B3E(): pass

    label("Function_32_3B3E")

    Sleep(150)
    OP_74(0xB, 0xF)
    OP_71(0xB, 0x0, 0xB, 0x0, 0x8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 70000, 0, 12500, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(991, 0, 100, 0)
    Return()

    # Function_32_3B3E end

    SaveToFile()

Try(main)
