from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Receptionist Tria",      # 1
        "Grace",                  # 2
        "Reins",                  # 3
        "McCunnen",               # 4
        "Editor-in-Chief",        # 5
        "Hauser",                 # 6
        "Engineer",               # 7
        "Jaeger",                 # 8
        "Jaeger",                 # 9
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
        "Function_4_8BB",          # 04, 4
        "Function_5_A7B",          # 05, 5
        "Function_6_BEF",          # 06, 6
        "Function_7_F48",          # 07, 7
        "Function_8_10BB",         # 08, 8
        "Function_9_1157",         # 09, 9
        "Function_10_1208",        # 0A, 10
        "Function_11_1DB3",        # 0B, 11
        "Function_12_1DED",        # 0C, 12
        "Function_13_1E3B",        # 0D, 13
        "Function_14_1E75",        # 0E, 14
        "Function_15_1E9B",        # 0F, 15
        "Function_16_1EDF",        # 10, 16
        "Function_17_1F2D",        # 11, 17
        "Function_18_1F5D",        # 12, 18
        "Function_19_1F8D",        # 13, 19
        "Function_20_1FA9",        # 14, 20
        "Function_21_1FC5",        # 15, 21
        "Function_22_1FE1",        # 16, 22
        "Function_23_1FFD",        # 17, 23
        "Function_24_2019",        # 18, 24
        "Function_25_2345",        # 19, 25
        "Function_26_235A",        # 1A, 26
        "Function_27_2383",        # 1B, 27
        "Function_28_23AC",        # 1C, 28
        "Function_29_2DFD",        # 1D, 29
        "Function_30_3C41",        # 1E, 30
        "Function_31_3C9C",        # 1F, 31
        "Function_32_3D44",        # 20, 32
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
    Jump("loc_8B7")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_8B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 2)), scpexpr(EXPR_END)), "loc_74F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C4")

    ChrTalk(
        0x8,
        (
            "Thank you very much\x01",
            "for having saved everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you all hadn't been here, I would\x01",
            "have been shivering in a corner of\x01",
            "the reception office even now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_74A")

    label("loc_6C4")


    ChrTalk(
        0x8,
        (
            "If you all hadn't been here, I would\x01",
            "have been shivering in a corner of\x01",
            "the reception office even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_74A")

    Jump("loc_8B7")

    label("loc_74F")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Rest\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_79E"),
        (1, "loc_820"),
        (2, "loc_8B2"),
        (SWITCH_DEFAULT, "loc_8B7"),
    )


    label("loc_79E")


    ChrTalk(
        0x8,
        (
            "(There is a first-aid kit so I can\x01",
            "do first-aid treatment here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "(Miss Grace and the others...\x01",
            "Please, help them.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B7")

    label("loc_820")


    ChrTalk(
        0x8,
        (
            "(Understood, please\x01",
            "stay still for me.)\x02",
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
            "(Miss Grace and the others...\x01",
            "Please, help them.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B7")

    label("loc_8B2")

    Jump("loc_8B7")

    label("loc_8B7")

    TalkEnd(0x8)
    Return()

    # Function_3_5EF end

    def Function_4_8BB(): pass

    label("Function_4_8BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8CC")
    Jump("loc_A77")

    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_A77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C6")

    ChrTalk(
        0xFE,
        (
            "Oh boy, what have we\x01",
            "got caught up into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a blessing no one's got injured, but...\x01",
            "Grace is reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's nice to be indomitable, but at that rate,\x01",
            "no matter how many lives she has, they won't be enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A77")

    label("loc_9C6")


    ChrTalk(
        0xFE,
        (
            "It's a blessing no one's got injured, but...\x01",
            "Grace is reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's nice to be indomitable, but at that rate,\x01",
            "no matter how many lives she has, they won't be enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A77")

    TalkEnd(0xFE)
    Return()

    # Function_4_8BB end

    def Function_5_A7B(): pass

    label("Function_5_A7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A8C")
    Jump("loc_BEB")

    label("loc_A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_BEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5F")

    ChrTalk(
        0xFE,
        (
            "When I came to do a delivery,\x01",
            "the armed men from before\x01",
            "suddenly came crushing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Outside the situation is serious...\x01",
            "I wonder if the food cart\x01",
            "I left there is all right...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BEB")

    label("loc_B5F")


    ChrTalk(
        0xFE,
        (
            "The food cart with which I shared many years of\x01",
            "joys and sorrows serving noodles in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I hope it's all in one piece.\x02",
    )

    CloseMessageWindow()

    label("loc_BEB")

    TalkEnd(0xFE)
    Return()

    # Function_5_A7B end

    def Function_6_BEF(): pass

    label("Function_6_BEF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C00")
    Jump("loc_F44")

    label("loc_C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_F44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E94")
    OP_4B(0xA, 0x0)

    ChrTalk(
        0xFE,
        "#02101FReins, you've brought the camera, right!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Y-Yes, it's fully ready!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FMiss Grace...\x01",
            "Don't tell me you want to go collect data!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FIt's pretty dangerous outside,\x01",
            "you should refrain from...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "#02103FWhat're you saying?\x01",
            "No way I could overlook such a big incident!\x02\x03",
            "#02101FAs a journalist, I have a duty\x01",
            "to report to the citizens the\x01",
            "truth I perceive with my eyes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206F...Stopping her looks useless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F*sigh*...seems so.\x02\x03",
            "#00001FI don't know what's going to happen.\x01",
            "Please be very careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#02102FUh uh, I know, I know.\x02\x03",
            "Lloyd, guys, you\x01",
            "be careful too!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 3)
    OP_4C(0xA, 0x0)
    Jump("loc_F44")

    label("loc_E94")


    ChrTalk(
        0xFE,
        (
            "#02103FThere's no way I can\x01",
            "overlook such a big incident!\x02\x03",
            "#02101FAfter all, as a journalist, I have the\x01",
            "duty to report to the citizens the\x01",
            "truth I perceive with my eyes!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F44")

    TalkEnd(0xFE)
    Return()

    # Function_6_BEF end

    def Function_7_F48(): pass

    label("Function_7_F48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F59")
    Jump("loc_10B7")

    label("loc_F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_10B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1023")
    OP_4B(0x9, 0x0)

    ChrTalk(
        0x9,
        (
            "#02102FReins, please!\x02\x03",
            "#02109FPlease stay close to me and\x01",
            "show me your skills like before!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "T-That was, really, just my\x01",
            "body that moved unconsciously...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xFE, 0x10)
    OP_4C(0x9, 0x0)
    Jump("loc_10B7")

    label("loc_1023")


    ChrTalk(
        0xFE,
        (
            "*sigh*, but it can't be helped.\x01",
            "Since I'm senior's partner,\x01",
            "I can't avoid dangers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this case, I'm gonna\x01",
            "take all the pictures I can!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B7")

    TalkEnd(0xFE)
    Return()

    # Function_7_F48 end

    def Function_8_10BB(): pass

    label("Function_8_10BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_10CC")
    Jump("loc_1153")

    label("loc_10CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_1153")

    ChrTalk(
        0xFE,
        (
            "The fact that the receiver hasn't been\x01",
            "destroyed is a blessing in disguise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must quickly call someone to help...!\x02",
    )

    CloseMessageWindow()

    label("loc_1153")

    TalkEnd(0xFE)
    Return()

    # Function_8_10BB end

    def Function_9_1157(): pass

    label("Function_9_1157")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1168")
    Jump("loc_1204")

    label("loc_1168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_1204")

    ChrTalk(
        0xFE,
        (
            "Every now and then I come to do maintenance\x01",
            "on the receiver...to think I got involved in this mess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*haah*, I dislike my lack of luck.\x02",
    )

    CloseMessageWindow()

    label("loc_1204")

    TalkEnd(0xFE)
    Return()

    # Function_9_1157 end

    def Function_10_1208(): pass

    label("Function_10_1208")

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
        "#00013F#5PWhat an awfully deadly silence...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PCould Miss Grace and the others\x01",
            "have escaped to another place?\x02",
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
            "#00201F#12PNo, I feel the response of multiple\x01",
            "people from inside the building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6PStill, this presence...\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 10, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1SE-Everyone...\x02",
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

    def lambda_1574():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1574)
    Sleep(50)

    def lambda_1584():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1584)
    Sleep(50)

    def lambda_1594():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1594)
    Sleep(50)

    def lambda_15A4():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_15A4)
    Sleep(50)

    def lambda_15B4():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_15B4)
    Sleep(50)

    def lambda_15C4():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15C4)
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
        "#00005F#6PYou're the receptionist...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P(*shh*...lower your voices.)\x02",
    )

    CloseMessageWindow()
    OP_68(3440, 1500, -1740, 2500)
    MoveCamera(36, 16, 0, 2500)
    OP_6E(400, 2500)
    SetCameraDistance(20500, 2500)
    OP_74(0x0, 0x3)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x8)

    def lambda_16AF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16AF)

    def lambda_16BC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16BC)

    def lambda_16C9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16C9)

    def lambda_16D6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16D6)

    def lambda_16E3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16E3)

    def lambda_16F0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16F0)
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
        "#10101F#6P(H-Has something happened?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P(A-Actually...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(Some time ago, men with guns\x01",
            "came suddenly inside the building.)\x02",
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
        "#00105F#6P(Eeh...!?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#6P(As I thought...)\x02\x03",
            "#00301F(The jaegers rampagin' outside, huh?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(S-Since it was sudden,\x01",
            "I don't know the details...\x01",
            "But I think you are right.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(Those who were in the building\x01",
            "got guns pointed at them and were\x01",
            "restrained in the blink of an eye.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(I hid myself and was\x01",
            "able to endure, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6P(A blessing in disguise.)\x02\x03",
            "#10301F(So, where are they now?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(Well...it seems at least two\x01",
            "persons remained on the top floor...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(Outside the situation is like that\x01",
            "and I can't even call for help...\x01",
            "W-What should I do?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#6P(...I understand the situation.\x01",
            "Please, leave it\x01",
            "to us for now.)\x02\x03",
            "(We'll save Miss Grace\x01",
            "and the others for sure.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P(Yeah...Thank you very much!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#6P(Now that things are like this, \x01",
            "it would be better to fully prepare.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#6P(The enemies are jaegers,\x01",
            "it doesn't hurt to be too\x01",
            "much cautious.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(If there is something I can do,\x01",
            "please feel free to ask.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P(There is a first-aid kit so I can\x01",
            "do first-aid treatment here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P(Yes, thank you very much.)\x02\x03",
            "#00007F(Alright...when we're ready,\x01",
            "we'll charge to the second floor!)\x02",
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

    # Function_10_1208 end

    def Function_11_1DB3(): pass

    label("Function_11_1DB3")


    def lambda_1DB8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1DB8)
    OP_95(0xFE, 1610, 0, -520, 2000, 0x0)
    Sleep(250)
    OP_93(0xFE, 0x13B, 0xFA)
    Sleep(250)
    OP_93(0xFE, 0x2D, 0xFA)
    Return()

    # Function_11_1DB3 end

    def Function_12_1DED(): pass

    label("Function_12_1DED")


    def lambda_1DF2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1DF2)
    OP_95(0xFE, 1000, 0, -2300, 2000, 0x0)
    OP_95(0xFE, 530, 0, -1340, 2000, 0x0)
    Sleep(250)
    OP_93(0xFE, 0x10E, 0x12C)
    Sleep(250)
    OP_93(0xFE, 0x13B, 0x12C)
    Return()

    # Function_12_1DED end

    def Function_13_1E3B(): pass

    label("Function_13_1E3B")


    def lambda_1E40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E40)
    OP_95(0xFE, 2000, 0, -2300, 2000, 0x0)
    OP_95(0xFE, 2470, 20, -1230, 2000, 0x0)
    Return()

    # Function_13_1E3B end

    def Function_14_1E75(): pass

    label("Function_14_1E75")


    def lambda_1E7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E7A)
    OP_95(0xFE, 1720, 0, -2230, 2000, 0x0)
    Return()

    # Function_14_1E75 end

    def Function_15_1E9B(): pass

    label("Function_15_1E9B")


    def lambda_1EA0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1EA0)
    OP_95(0xFE, 1000, 0, -3300, 2000, 0x0)
    OP_95(0xFE, 280, 0, -2730, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x12C)
    Return()

    # Function_15_1E9B end

    def Function_16_1EDF(): pass

    label("Function_16_1EDF")


    def lambda_1EE4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1EE4)
    OP_95(0xFE, 1700, 0, -3300, 2000, 0x0)
    OP_95(0xFE, 2270, 0, -3040, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0xC8)
    Sleep(300)
    OP_93(0xFE, 0x2D, 0xC8)
    Return()

    # Function_16_1EDF end

    def Function_17_1F2D(): pass

    label("Function_17_1F2D")

    OP_95(0xFE, 7020, 0, 960, 2000, 0x0)
    OP_95(0xFE, 5640, 0, 320, 2000, 0x0)
    TurnDirection(0xFE, 0x109, 500)
    Return()

    # Function_17_1F2D end

    def Function_18_1F5D(): pass

    label("Function_18_1F5D")

    OP_95(0xFE, 2029, 0, 180, 2000, 0x0)
    OP_95(0xFE, 3010, 20, 160, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_18_1F5D end

    def Function_19_1F8D(): pass

    label("Function_19_1F8D")

    OP_95(0xFE, 1750, 0, 230, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_19_1F8D end

    def Function_20_1FA9(): pass

    label("Function_20_1FA9")

    OP_95(0xFE, 3250, 20, -880, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_20_1FA9 end

    def Function_21_1FC5(): pass

    label("Function_21_1FC5")

    OP_95(0xFE, 2100, 20, -1790, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_21_1FC5 end

    def Function_22_1FE1(): pass

    label("Function_22_1FE1")

    OP_95(0xFE, 2040, 0, -640, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_22_1FE1 end

    def Function_23_1FFD(): pass

    label("Function_23_1FFD")

    OP_95(0xFE, 3080, 20, -2350, 2000, 0x0)
    TurnDirection(0xFE, 0x8, 500)
    Return()

    # Function_23_1FFD end

    def Function_24_2019(): pass

    label("Function_24_2019")

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
            "#00001F#5P(Above here, Miss Grace and the others\x01",
            "are being held captive by some jaegers...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#11P(Lloyd, are we chargin' in now?)\x02",
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
            "Charge\x01",                   # 0
            "We Are Not Prepared\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21AA"),
        (SWITCH_DEFAULT, "loc_227E"),
    )


    label("loc_21AA")


    ChrTalk(
        0x101,
        "#00007F#5P(Yeah...let's go, everyone!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F(Yessir!)\x02",
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
    Jump("loc_2344")

    label("loc_227E")


    ChrTalk(
        0x104,
        (
            "#00303F#11P(I see...)\x02\x03",
            "#00301F(If help comes late, I don't know\x01",
            "what those jaegers could do.\x01",
            "Let's get prepared at once!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#5P(Yeah...!)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -6510, 20, 2640, 180)
    EventEnd(0x5)
    Jump("loc_2344")

    label("loc_2344")

    Return()

    # Function_24_2019 end

    def Function_25_2345(): pass

    label("Function_25_2345")

    OP_95(0xFE, -6440, 3730, 7730, 4000, 0x0)
    Return()

    # Function_25_2345 end

    def Function_26_235A(): pass

    label("Function_26_235A")

    OP_95(0xFE, -7000, 0, 4000, 4000, 0x0)
    OP_95(0xFE, -7000, 3730, 7730, 4000, 0x0)
    Return()

    # Function_26_235A end

    def Function_27_2383(): pass

    label("Function_27_2383")

    OP_95(0xFE, -5800, 0, 4000, 4000, 0x0)
    OP_95(0xFE, -5800, 3730, 7730, 4000, 0x0)
    Return()

    # Function_27_2383 end

    def Function_28_23AC(): pass

    label("Function_28_23AC")

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
            "#02101F#11P...Stop this foolish\x01",
            "act right now!\x02\x03",
            "What will you get from\x01",
            "raiding the city!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "We have our own goals...\x01",
            "Nothing that regards you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Be assured, if you stay quiet,\x01",
            "no harm will come to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "If you don't do that...\x01",
            "We'll force you to stay quiet.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(
        0xE,
        "#5PE-Eeek...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#5PI-I only came for a delivery,\x01",
            "why such a thing had to happen...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#02104F#11PHmph, very well...!\x02\x03",
            "#02102FYou're greatly mistaken if you\x01",
            "think that you can make me falter\x01",
            "with one or two threats like those!\x02\x03",
            "If you wanna do something,\x01",
            "just go ahead and try!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#11PGrace, don't\x01",
            "motivate them...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0xA, 0x10158, 0x0, 0x307A, 0x5DC, 0x0)

    ChrTalk(
        0xA,
        (
            "#11PP-Please wait!\x01",
            "Senior, control yourself...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        (
            "#11P#4SY-You guys! If you touch her,\x01",
            "I'll never forgive you!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2889():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2889)

    def lambda_2896():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2896)
    Sleep(50)

    def lambda_28A6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_28A6)

    def lambda_28B3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_28B3)
    Sleep(50)

    def lambda_28C3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_28C3)

    def lambda_28D0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_28D0)

    ChrTalk(
        0x9,
        "#02105F#5PR-Reins...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Hmph, a plucky journalist, eh...\x01",
            "But I won't fall for your provocation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Could you stay quiet until\x01",
            "the plan is completed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11P"Plan"... What do you intend to do?\x02",
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
    SetChrName("Lloyd's Voice")
    Sound(2090, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4S──Freeze!!!#3S\x02",
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

    def lambda_2B4A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2B4A)

    def lambda_2B57():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B57)
    Sleep(50)

    def lambda_2B67():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B67)

    def lambda_2B74():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B74)
    OP_68(61890, 1500, 11620, 1800)
    MoveCamera(45, 13, 0, 1800)
    OP_6E(460, 1800)
    SetCameraDistance(19500, 1800)

    def lambda_2BAF():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BAF)
    Sleep(50)

    def lambda_2BC7():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BC7)
    Sleep(50)

    def lambda_2BDF():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BDF)
    Sleep(50)

    def lambda_2BF7():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BF7)
    Sleep(50)

    def lambda_2C0F():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C0F)
    Sleep(50)

    def lambda_2C27():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2C27)
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
        "#11PYou...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#02105F#11PLloyd!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5PCaptain Randolph!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107F#5PCommencing suppression!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#5PAlright, let's go!!\x02",
    )

    CloseMessageWindow()

    def lambda_2CF4():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CF4)

    def lambda_2D09():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D09)

    def lambda_2D1E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D1E)

    def lambda_2D33():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D33)

    def lambda_2D48():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2D48)

    def lambda_2D5D():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2D5D)
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

    # Function_28_23AC end

    def Function_29_2DFD(): pass

    label("Function_29_2DFD")

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
        "#5PCrap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PSeems we can only withdraw from here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PWhat...!?\x02",
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
        "#00310F#5PTch...they got away, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PThere were many things\x01",
            "I wanted to ask them.\x02",
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

    def lambda_31B8():
        OP_9B(0x0, 0xFE, 0x0, 0x6A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31B8)
    Sleep(50)

    def lambda_31D0():
        OP_9B(0x0, 0xFE, 0x0, 0x6A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_31D0)
    Sleep(50)

    def lambda_31E8():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31E8)
    Sleep(50)

    def lambda_3200():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3200)
    Sleep(50)

    def lambda_3218():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3218)
    Sleep(50)

    def lambda_3230():
        OP_9B(0x0, 0xFE, 0x0, 0x73A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3230)
    Sleep(50)

    def lambda_3248():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3248)
    Sleep(50)

    def lambda_3260():
        OP_9B(0x0, 0xFE, 0xFFFB, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3260)
    Sleep(50)

    def lambda_3278():
        OP_9B(0x0, 0xFE, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3278)
    Sleep(50)

    def lambda_3290():
        OP_9B(0x0, 0xFE, 0xFFFB, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3290)
    Sleep(50)

    def lambda_32A8():
        OP_9B(0x0, 0xFE, 0x0, 0x514, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_32A8)
    Sleep(50)

    def lambda_32C0():
        OP_9B(0x0, 0xFE, 0xFFFB, 0x514, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_32C0)
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
        "#02110F#11PLloyd, guys, are you ok!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PYou too Miss Grace...\x01",
            "Are you hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PNo, thank goodness\x01",
            "we're all unscathed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PFor a hair's breadth, I'd say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POh boy, Grace,\x01",
            "you're reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PHonestly, I was struck with terror...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02109F#11PAhaha, I just\x01",
            "heated up a bit.\x02\x03",
            "#02104FAs a professional journalist,\x01",
            "I can't yield to violence.\x01\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#02110F...Even so, Reins, I've\x01",
            "got a new opinion of you!\x02\x03",
            "#02109FI honestly didn't think you would've\x01",
            "sticked up that much for me, you know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 500)

    ChrTalk(
        0xA,
        (
            "#12PA-Ahaha, what can I say,\x01",
            "I lost myself and my body\x01",
            "unconsciously moved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PNo, no...\x01",
            "That was admirable, young man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5P*giggle*, in any case, \x01",
            "I'm glad you're all safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5PEven so...\x01",
            "Why did jaegers target\x01",
            "the News Service?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PThat is indeed concerning.\x02\x03",
            "#00208FI can't see it as a place of \x01",
            "particular importance to them\x01",
            "rather than the "Heiyue" one...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_36C3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_36C3)
    Sleep(50)

    def lambda_36D3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_36D3)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x9,
        (
            "#02106F#11PAh, maybe it's for...\x02\x03",
            "#02101FThe international receiver\x01",
            "that's over there?\x02",
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
            "#00013FAn international receiver...simply put it,\x01",
            "a receiver that can send orbal waves abroad too?\x02\x03",
            "#00008FCould their objective be to defend against\x01",
            "an intervention from the Republic...?\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10303FHm, that could\x01",
            "be possible.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 0, -1, -1)

    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#02101FYes, I think you're right.\x02\x03",
            "Those guys, when in the Waterfront Area,\x01",
            "seem they made it straight for here.\x02\x03",
            "#02106FIt was so sudden that,\x01",
            "honestly, I was bewildered.\x02",
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
            "#00303F#6PThen...\x01",
            "We should make haste.\x02\x03",
            "#00301FNow that the "Heiyue" are no more,\x01",
            "they could be goin' to the IBC\x01",
            "and plan to do something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PWell...they were that much prepared\x01",
            "that their goal could not be mere mira.\x02\x03",
            "#00013FEveryone, please stay inside.\x01",
            "Please don't go outside by all means\x01",
            "until the situation is under control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PY-Yeah...we'll do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11PGuys, are you going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02103F#11PBe very careful!\x02\x03",
            "#02101FIf you can resolve this case,\x01",
            "I'll put together a front page feature!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#6PAhaha...\x01",
            "We'll just accept the thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#5PWell then, let's go, everyone!\x02",
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

    # Function_29_2DFD end

    def Function_30_3C41(): pass

    label("Function_30_3C41")

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

    # Function_30_3C41 end

    def Function_31_3C9C(): pass

    label("Function_31_3C9C")

    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 66500, 0, 11400, 5000, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CFF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)

    label("loc_3CFF")

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

    # Function_31_3C9C end

    def Function_32_3D44(): pass

    label("Function_32_3D44")

    Sleep(150)
    OP_74(0xB, 0xF)
    OP_71(0xB, 0x0, 0xB, 0x0, 0x8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 70000, 0, 12500, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(991, 0, 100, 0)
    Return()

    # Function_32_3D44 end

    SaveToFile()

Try(main)
