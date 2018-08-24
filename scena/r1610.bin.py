from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1610.bin",                # FileName
        "r1610",                    # MapName
        "r1610",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x33,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 2000, 0, -3700, 0, 0, 1, 96, 0, 0, 0, 1],
    )

    BuildStringList((
        "r1610",                  # 0
        "Cryptid",                # 1
        "メルカバ玖号機",         # 2
        "メルカバ光学迷彩",       # 3
        "メルカバ影",             # 4
        "br1520",                 # 5
    ))

    ATBonus("ATBonus_200", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2C0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2E0", 0x0042, 255, 6, 45, 10, 1, 30, 0, "br1520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2C0", "MonsterBattlePostion_2A0", "ed7454", "ed7453", "ATBonus_200"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0040, 0, 6,   48.400001525878906,    -2.0,                  -2.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   -6.050000190734863,    0.25,                  0.20000000298023224,   1.0])

    DeclActor(48150,   0,       14450,   2000,    48150,   1000,    14450,   0x007C, 0,  2,  0x0000)
    DeclActor(40700,   0,       4294952946, 1200,    40700,   2000,    4294952946, 0x007C, 0,  4,  0x0000)
    DeclActor(61490,   4294966296, 6830,    1200,    69090,   0,       5180,    0x007C, 0,  5,  0x0000)

    ChipFrameInfo(880, 0)                                        # 0

    ScpFunction((
        "Function_0_370",          # 00, 0
        "Function_1_407",          # 01, 1
        "Function_2_623",          # 02, 2
        "Function_3_6D8",          # 03, 3
        "Function_4_7FC",          # 04, 4
        "Function_5_B39",          # 05, 5
        "Function_6_C00",          # 06, 6
        "Function_7_C59",          # 07, 7
        "Function_8_141D",         # 08, 8
        "Function_9_1CCE",         # 09, 9
        "Function_10_30BD",        # 0A, 10
        "Function_11_33E8",        # 0B, 11
        "Function_12_40A2",        # 0C, 12
        "Function_13_410D",        # 0D, 13
        "Function_14_419C",        # 0E, 14
        "Function_15_41ED",        # 0F, 15
        "Function_16_423B",        # 10, 16
        "Function_17_42A0",        # 11, 17
        "Function_18_42BB",        # 12, 18
    ))


    def Function_0_370(): pass

    label("Function_0_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2B, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_386")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39C")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_3CF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CF")
    SetChrPos(0x0, 40700, 0, -14350, 315)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E3")
    SetScenarioFlags(0x0, 0)
    Event(0, 7)

    label("loc_3E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3F7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_406")

    label("loc_3F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_406")
    ClearScenarioFlags(0x22, 1)
    Event(0, 11)

    label("loc_406")

    Return()

    # Function_0_370 end

    def Function_1_407(): pass

    label("Function_1_407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_421")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_454")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_442")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_454")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_454")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_454")

    Sound(136, 1, 80, 0)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 69090, 0, 5180, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BF")
    OP_66(0x0, 0x1)

    label("loc_4BF")

    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_510")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0xB4, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_53A")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_END)), "loc_534")
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFrame(0x4, "flower04", 0x0, 0x1)
    Jump("loc_53A")

    label("loc_534")

    ClearMapObjFlags(0x4, 0x4)

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B1")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_5B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_END)), "loc_5CA")
    SetMapObjFlags(0x0, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_5E4")

    label("loc_5CA")

    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    SetChrPos(0x8, 48390, -1000, -2000, 180)

    label("loc_5E4")

    MiniGame(0x2F, 0xFFFFFFFF, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_622")
    OP_1B(0x0, 0x0, 0x3)

    label("loc_622")

    Return()

    # Function_1_407 end

    def Function_2_623(): pass

    label("Function_2_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_END)), "loc_64F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_END)), "loc_63D")
    Call(0, 10)
    Jump("loc_64A")

    label("loc_63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A")
    Call(0, 9)

    label("loc_64A")

    Jump("loc_6D7")

    label("loc_64F")

    EventBegin(0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Azure flowers are\x01",
            "blooming.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000F(What pretty flowers.\x01",
            "They seem to be faintly\x01",
            "glowing, though...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x168, 3)
    EventEnd(0x3)

    label("loc_6D7")

    Return()

    # Function_2_623 end

    def Function_3_6D8(): pass

    label("Function_3_6D8")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(With this we've beaten\x01",
            "the two Cryptids, but...\x01",
            "Something's bothering me.)\x02\x03",
            "#00000FEveryone, could we go back\x01",
            "to the scene to\x01",
            "investigate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIndeed, I too feel\x01",
            "there's something we\x01",
            "must do here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThen, let's head back\x01",
            "and investigate.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2120, 0, -3710, 90)
    EventEnd(0x4)
    Return()

    # Function_3_6D8 end

    def Function_4_7FC(): pass

    label("Function_4_7FC")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82E")
    SetScenarioFlags(0x31, 2)

    label("loc_82E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_86E")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_863")
    Sound(2499, 255, 100, 0)
    Jump("loc_869")

    label("loc_863")

    Sound(3537, 255, 100, 0)

    label("loc_869")

    Jump("loc_874")

    label("loc_86E")

    Sound(3344, 255, 100, 0)

    label("loc_874")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_8E9")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8C9"),
        (SWITCH_DEFAULT, "loc_8DA"),
    )


    label("loc_8C9")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_8E4")

    label("loc_8DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E4")

    Jump("loc_B26")

    label("loc_8E9")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_91B")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_91B")

    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_94F"),
        (1, "loc_A53"),
        (2, "loc_AE4"),
        (SWITCH_DEFAULT, "loc_B1C"),
    )


    label("loc_94F")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_980")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_990")

    label("loc_980")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_990")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E6")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A09")
    Sound(461, 0, 100, 0)

    label("loc_A09")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A29")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_A39")

    label("loc_A29")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_A39")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_874")

    label("loc_A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_AC5")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_A88")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_AA0")

    label("loc_A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_A9B")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_AA0")

    label("loc_A9B")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_AA0")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADF")

    label("loc_AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_AD5")
    OP_AF(0xFB)
    Jump("loc_ADF")

    label("loc_AD5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ADF")

    Jump("loc_B26")

    label("loc_AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B17")

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_B0D")
    OP_AF(0xFB)
    Jump("loc_B17")

    label("loc_B0D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B17")

    Jump("loc_B26")

    label("loc_B1C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B26")

    Jump("loc_874")

    label("loc_B2B")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_7FC end

    def Function_5_B39(): pass

    label("Function_5_B39")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(64940, 850, 5910, 1500)
    MoveCamera(37, 19, 0, 1500)
    OP_6E(680, 1500)
    SetCameraDistance(17000, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFB")
    OP_E2(0x2)
    MiniGame(0x6, 0xE, 0xF032, 0xFFFFFC18, 0x1AAE, 0x5A, 0x10DE2, 0x0, 0x143C)

    label("loc_BFB")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_5_B39 end

    def Function_6_C00(): pass

    label("Function_6_C00")

    Battle("BattleInfo_2E0", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C42")
    OP_90(0x0, 37650, 0, -3750, 90)
    EventEnd(0x5)
    Jump("loc_C58")

    label("loc_C42")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    Jump("loc_C58")

    label("loc_C55")

    Call(0, 8)

    label("loc_C58")

    Return()

    # Function_6_C00 end

    def Function_7_C59(): pass

    label("Function_7_C59")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(2100, 1000, -3700, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_68(3100, 1000, -3700, 1300)
    SetCameraDistance(18000, 1300)
    SetChrPos(0x101, 2400, 0, -3700, 90)
    SetChrPos(0x102, 1700, 0, -5000, 90)
    SetChrPos(0x103, 1500, 0, -3000, 90)
    SetChrPos(0x104, 700, 0, -4500, 90)
    SetChrPos(0x109, 900, 0, -2500, 90)
    SetChrPos(0x105, -500, 0, -3700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)

    def lambda_D35():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D35)
    Sleep(0)

    def lambda_D4D():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D4D)
    Sleep(0)

    def lambda_D65():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D65)
    Sleep(0)

    def lambda_D7D():
        OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D7D)
    Sleep(0)

    def lambda_D95():
        OP_9B(0x0, 0x109, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D95)
    Sleep(0)

    def lambda_DAD():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DAD)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC1")

    ChrTalk(
        0x109,
        "#10111F#5P(Ah...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#5P(That's a Cryptid,\x01",
            "huh!?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF8")

    label("loc_EC1")


    ChrTalk(
        0x105,
        "#10305F#6P(Whoa...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(There it is!)\x02",
    )

    CloseMessageWindow()

    label("loc_EF8")

    PlayBGM("ed7573", 0)
    OP_68(46900, 1050, -2950, 4000)
    MoveCamera(65, 10, 0, 4000)
    SetCameraDistance(21000, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(46900, 1050, -2950, 0)
    MoveCamera(41, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24310, 0)
    OP_68(47700, 1050, -1800, 6000)
    MoveCamera(127, 30, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(23000, 6000)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121F")

    ChrTalk(
        0x104,
        (
            "#00303F#9P(Like the report said,\x01",
            "it's quite huge...)\x02\x03",
            "#00301F(PeTiote, how about the\x01",
            "spatial distortion?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(Time, Space, Mirage...\x01",
            "Manifestation of the higher\x01",
            "elements confirmed.)\x02\x03",
            "#00201F(The cause is unclear at\x01",
            "present.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#9P(I see...)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(3100, 1000, -3700, 0)
    MoveCamera(45, 22, 0, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    def lambda_10D2():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10D2)
    Sleep(0)

    def lambda_10E2():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10E2)
    Sleep(0)

    def lambda_10F2():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10F2)
    Sleep(0)

    def lambda_1102():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1102)
    Sleep(0)

    def lambda_1112():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1112)
    Sleep(0)

    def lambda_1122():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1122)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x105,
        "#10301F#6P(So... What do we do?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P(According to the CGF\x01",
            "report, it seems pretty\x01",
            "dangerous...)\x02\x03",
            "#00013F(If we're going to\x01",
            "eliminate it, let's make\x01",
            "sure we're ready.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5P(Roger!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E7")

    label("loc_121F")


    ChrTalk(
        0x102,
        (
            "#00101F#9P(Tio... How's the\x01",
            "spatial distortion?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(I've confirmed\x01",
            "manifestation of the higher\x01",
            "elements here as well...)\x02\x03",
            "#00201F(The cause of this\x01",
            "distortion is unknown as\x01",
            "well.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#9P(I knew it...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#9P(It seems the Cryptid\x01",
            "itself isn't causing it,\x01",
            "though...)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(3100, 1000, -3700, 0)
    MoveCamera(45, 22, 0, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10101F#5P(Lloyd... Are we\x01",
            "fighting it\x01",
            "immediately?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#5P(Yeah, let's proceed\x01",
            "with caution!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3400, 0, -3700, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 3)
    EventEnd(0x5)
    Return()

    # Function_7_C59 end

    def Function_8_141D(): pass

    label("Function_8_141D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03050.itc", 0x23)
    OP_68(42650, 1500, -3700, 0)
    MoveCamera(50, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(38650, 1000, -3700, 3000)
    MoveCamera(45, 16, 0, 3000)
    SetCameraDistance(17000, 3000)
    SetChrPos(0x101, 39650, 0, -3700, 90)
    SetChrPos(0x102, 38500, 0, -2850, 90)
    SetChrPos(0x103, 37100, 0, -3850, 90)
    SetChrPos(0x104, 39350, 0, -4900, 90)
    SetChrPos(0x109, 37500, 0, -5150, 90)
    SetChrPos(0x105, 40000, 0, -2000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_29(0xA6, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D7")

    ChrTalk(
        0x101,
        (
            "#00006F#5PGuh... As expected, it\x01",
            "was strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PAnd also... It vanished\x01",
            "in a mysterious way.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_162B():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_162B)
    Sleep(50)

    def lambda_163B():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_163B)
    Sleep(50)

    def lambda_164B():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_164B)
    Sleep(50)

    def lambda_165B():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_165B)
    Sleep(50)

    def lambda_166B():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_166B)
    Sleep(50)

    def lambda_167B():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_167B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10108F#12PTio. How's the "spatial\x01",
            "distortion"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...It's no good. The\x01",
            "higher elements are\x01",
            "still at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PJeez... What the heck is\x01",
            "causin' it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PIt seems the Cryptid\x01",
            "itself isn't the cause,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11PLooks like we need to\x01",
            "check the other one too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C27")

    label("loc_17D7")


    ChrTalk(
        0x105,
        (
            "#10306F#5POh man... This one was\x01",
            "strong too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#6PHowever, it vanished in\x01",
            "the same way...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_1887():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1887)
    Sleep(50)

    def lambda_1897():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1897)
    Sleep(50)

    def lambda_18A7():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_18A7)
    Sleep(50)

    def lambda_18B7():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_18B7)
    Sleep(50)

    def lambda_18C7():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18C7)
    Sleep(50)

    def lambda_18D7():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_18D7)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#00301F#11PThe "spatial distortion"\x01",
            "is still here, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PThat's right...\x02\x03",
            "#00201FIt's just, I feel like\x01",
            "there's some kind of\x01",
            "specific cause.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#11PA specific cause? Like\x01",
            "what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...Well... My senses have been\x01",
            "disturbed by the "distortion"\x01",
            "for some time now...\x02\x03",
            "#00200FInstead, you all may be able\x01",
            "to find the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PAll right... Let's\x01",
            "search the area.\x02\x03",
            "#00000FWhatever's causing the\x01",
            ""spatial distortion" is\x01",
            "definitely nearby.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B5C():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B5C)
    Sleep(50)

    def lambda_1B6C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1B6C)
    Sleep(50)

    def lambda_1B7C():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1B7C)
    Sleep(50)

    def lambda_1B8C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1B8C)
    Sleep(50)

    def lambda_1B9C():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B9C)
    Sleep(50)

    def lambda_1BAC():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1BAC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10100F#6PRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#12PLet's search whatever we\x01",
            "can get our hands on!\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA6, 0x1, 0x3)

    label("loc_1C27")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Defeated the St. Ursula\x01",
            "Byroad Cryptid!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 39650, 0, -3700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 4)
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CBE")
    OP_1B(0x0, 0x0, 0x3)

    label("loc_1CBE")

    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_8_141D end

    def Function_9_1CCE(): pass

    label("Function_9_1CCE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51216.itc", 0x1E)
    SoundLoad(961)
    SoundLoad(828)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis252.itp")
    LoadEffect(0x0, "event/ev14005.eff")
    LoadEffect(0x1, "event/ev14007.eff")
    OP_68(48500, 1000, 14050, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(19000, 1000)
    SetChrPos(0x101, 49400, 0, 14050, 270)
    SetChrPos(0x102, 49600, 0, 15400, 225)
    SetChrPos(0x103, 49200, 0, 12900, 315)
    SetChrPos(0x104, 49200, 0, 16300, 225)
    SetChrPos(0x109, 48000, 0, 16000, 180)
    SetChrPos(0x105, 46200, 0, 14200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2106")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        "#00005FThese flowers...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 4)), scpexpr(EXPR_END)), "loc_1F11")

    AnonymousTalk(
        0x102,
        (
            "#00108FIf I remember correctly, they were\x01",
            "blooming even in the marshlands of\x01",
            "East Crossbell Highway...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00305FYeah, we saw 'em there,\x01",
            "alright.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1FBF")

    label("loc_1F11")


    AnonymousTalk(
        0x105,
        (
            "#10302FWeren't they blooming\x01",
            "even in the marshlands of\x01",
            "East Crossbell Highway?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00011FY-You think so?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00108FYes, I feel like I saw\x01",
            "them there too...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1FBF")


    AnonymousTalk(
        0x109,
        (
            "#10109FThey're very pretty\x01",
            "flowers...\x02\x03",
            "#10102FBut I don't think I've ever\x01",
            "seen them before. I wonder\x01",
            "what they're called.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00001FHmm...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#11P(...I think it's\x01",
            "unlikely, but...)\x02\x03",
            "#00001F(Well, maybe it's worth\x01",
            "a try?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x160, 5)
    OP_29(0xA6, 0x1, 0x4)
    Jump("loc_21C3")

    label("loc_2106")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#00003F#11P(...I think it's\x01",
            "unlikely, but...)\x02\x03",
            "#00001F(Well, maybe it's worth\x01",
            "a try?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_21C3")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Try picking the azure flowers\x01",      # 0
            "Cancel\x01",                             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2222"),
        (1, "loc_307E"),
        (SWITCH_DEFAULT, "loc_30BC"),
    )


    label("loc_2222")

    OP_9B(0x0, 0x101, 0x0, 0x2EE, 0x3E8, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    ChrTalk(
        0x102,
        "#00105FLloyd...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PWhat, you're picking\x01",
            "these flowers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah... Though I feel a\x01",
            "little sorry for them─\x02",
        )
    )

    CloseMessageWindow()
    Sound(929, 0, 40, 0)
    Sound(828, 2, 30, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 48200, 600, 14450, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00301F#5PW-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12PThis is...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PUgh!\x02",
    )

    CloseMessageWindow()
    SetMapObjFrame(0x4, "flower04", 0x0, 0x1)
    StopEffect(0x0, 0x2)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(961, 2, 70, 0)
    Sound(233, 0, 100, 0)
    Sound(929, 0, 60, 0)
    PlayEffect(0x1, 0x1, 0x101, 0x3, 0, 1050, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x5DC)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0xB4, 0x5DC)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    MoveCamera(45, 30, 10, 3000)
    SetCameraDistance(8000, 3000)
    OP_6E(1000, 3000)
    Sleep(2500)
    Sound(829, 0, 100, 0)
    StopSound(961, 2000, 60)
    StopSound(828, 2000, 20)
    FadeToDark(500, 16777215, -1)
    Sleep(800)
    FadeToBright(300, 16777215)
    CancelBlur(300)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x32)
    OP_11(0xA7, 0xDD, 0xFE, 0x1E, 0xB4, 0x32)
    MoveCamera(45, 16, 0, 50)
    SetCameraDistance(19000, 50)
    OP_6E(500, 50)
    StopEffect(0x1, 0x2)
    Sleep(500)
    OP_6F(0x79)
    StopBGM(0x1770)

    ChrTalk(
        0x101,
        "#00013F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#5PT-That was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FIt's almost like the air\x01",
            "was shaking...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10308F#6P...Tio. How's the\x01",
            ""spatial distortion"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00203F#12PPresence of the higher\x01",
            "elements have\x01",
            "disappeared.\x02\x03",
            "#00201FI can't sense any\x01",
            "disturbances in this\x01",
            "entire area any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PW-Wait a sec.\x02\x03",
            "#00307FYou're tellin' me those\x01",
            "azure flowers were\x01",
            "causin' the anomaly!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, that must be it.\x02\x03",
            "#10300FThough I can't think\x01",
            "those tiny flowers have\x01",
            "that kind of power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FU-Unbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#5PW-What kind of flowers\x01",
            "are these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12PI don't sense a strange\x01",
            "presence from those\x01",
            "flowers any longer, but...\x02\x03",
            "#00200FFor now, perhaps we should\x01",
            "have them investigated\x01",
            "somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PRight...\x02\x03",
            "#00003F...It's probably a bit of a\x01",
            "different field than the\x01",
            "medical college specializes in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FA-Anyway, let's hang on to\x01",
            "them so we don't lose them.\x02\x03",
            "If we come up with some\x01",
            "idea about them, we'll have\x01",
            "them investigated, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PYeah, let's.\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0xB4, 0x2EE, 0x3E8, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x105)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0x105,
        "#10303F#6P...Hmm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_2A1C():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A1C)
    Sleep(50)

    def lambda_2A2C():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2A2C)
    Sleep(50)

    def lambda_2A3C():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2A3C)
    Sleep(50)

    def lambda_2A4C():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2A4C)
    Sleep(50)

    def lambda_2A5C():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A5C)
    Sleep(50)

    def lambda_2A6C():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2A6C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#11PWazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PDo you have an idea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PWell... Maybe it's a faint\x01",
            "memory of mine.\x02\x03",
            "#10301FI feel like there's legend\x01",
            "about a mysterious azure flower\x01",
            "in the church Testaments.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#11PWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#5PHey now, for real!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PWell, I feel like I saw\x01",
            "it when I skimmed them a\x01",
            "long time ago, but...\x02\x03",
            "#10300FAny ideas, Elie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PAs you might imagine, I\x01",
            "haven't read through the\x01",
            "entire Testaments, but...\x02\x03",
            "#00103FIndeed, I feel like I\x01",
            "read such a passage.\x02\x03",
            "#00108FA legend of an "azure\x01",
            "flower" with mysterious\x01",
            "powers...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10111F#6PThat's... Bingo, isn't\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00201F#12PIt seems there's value in\x01",
            "confirming it with a\x01",
            "Church official, at least.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DEF():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DEF)
    Sleep(50)

    def lambda_2DFF():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2DFF)
    Sleep(50)

    def lambda_2E0F():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2E0F)
    Sleep(50)

    def lambda_2E1F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E1F)
    Sleep(50)

    def lambda_2E2F():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E2F)
    Sleep(50)

    def lambda_2E3F():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2E3F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F07")

    ChrTalk(
        0x101,
        (
            "#00003F#11P...You're right.\x02\x03",
            "#00000FLet's try asking Miss\x01",
            "Marble or Ries about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes... Either of them\x01",
            "would be qualified, I\x01",
            "think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCB")

    label("loc_2F07")


    ChrTalk(
        0x101,
        (
            "#00003F#11P...You're right.\x02\x03",
            "#00000FI think that Miss Marble\x01",
            "would be the easiest to\x01",
            "consult with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes, I think she's\x01",
            "qualified.\x02\x03",
            "#00108F(We could consult with\x01",
            ""her" too, but...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCB")


    ChrTalk(
        0x104,
        (
            "#00300F#5PAlllright, then let's\x01",
            "head to Crossbell\x01",
            "Cathedral!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 49400, 0, 14050, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    AddItemNumber(0x333, 1)
    SetScenarioFlags(0x160, 6)
    OP_29(0xA6, 0x1, 0x5)
    OP_65(0x0, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7200", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3C1)
    OP_24(0x33C)
    EventEnd(0x5)
    Jump("loc_30BC")

    label("loc_307E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 49400, 0, 14050, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_30BC")

    label("loc_30BC")

    Return()

    # Function_9_1CCE end

    def Function_10_30BD(): pass

    label("Function_10_30BD")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis252.itp")
    OP_68(48500, 1000, 14050, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 49400, 0, 14050, 270)
    SetChrPos(0x102, 49600, 0, 15400, 225)
    SetChrPos(0x103, 49200, 0, 12900, 315)
    SetChrPos(0x104, 49200, 0, 16300, 225)
    SetChrPos(0x109, 48000, 0, 16000, 180)
    SetChrPos(0x105, 46200, 0, 14200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    AnonymousTalk(
        0x109,
        (
            "#10100FN-Now that you mention\x01",
            "it...\x02\x03",
            "Should we pick up these\x01",
            "flowers too?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FNo... Let's wait and see\x01",
            "what happens with these.\x02\x03",
            "They might turn out to\x01",
            "be valuable samples.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#00200FIndeed. It seems they\x01",
            "lose their powers when\x01",
            "picked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00100FHowever... if a Cryptid\x01",
            "appears again, maybe we'll\x01",
            "have to pick them up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00300FWell, we'll deal with\x01",
            "that when it happens.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 49400, 0, 14050, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x160, 7)
    EventEnd(0x5)
    Return()

    # Function_10_30BD end

    def Function_11_33E8(): pass

    label("Function_11_33E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch03154.itc", 0x1E)
    LoadEffect(0x0, "event/ev17025.eff")
    LoadEffect(0x1, "event/ev17026.eff")
    CreatePortrait(0, 67, 20, 413, 252, 0, 0, 512, 256, 0, 0, 346, 232, 0xFFFFFF, 0x0, "c_vis242.itp")
    SoundLoad(497)
    SoundLoad(950)
    SoundLoad(852)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x8, 0x9)
    OP_49()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    OP_75(0x8, 0x1, 0x0)
    OP_71(0x8, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x8, 0x2EE, 0x2EE, 0x2EE)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x1, 0x65, 0xA0, 0x0, 0x20)
    OP_FF(0x1, 0x307, 0x307, 0x307)
    ClearChrFlags(0xB, 0x80)
    OP_78(0xA, 0xB)
    OP_49()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_75(0xA, 0x1, 0x0)
    OP_FF(0xA, 0x2EE, 0x2EE, 0x2EE)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x107, 0x80)
    SetMapObjFlags(0x5, 0x4)
    OP_68(35000, 1850, -1900, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(67500, 0)
    OP_68(37500, 5500, -11350, 8000)
    MoveCamera(45, 30, 0, 8000)
    OP_6E(680, 8000)
    SetCameraDistance(41500, 8000)
    SetChrPos(0x9, 37500, 15250, -11350, 315)
    OP_D5(0x9, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0xA, 37500, 15250, -11350, 315)
    OP_D5(0xA, 0x0, 0x4CE78, 0x0, 0x0)
    SetChrPos(0xB, 37500, 0, -11350, 315)
    OP_D5(0xB, 0x0, 0x4CE78, 0x0, 0x0)
    OP_82(0x64, 0x64, 0xBB8, 0x1F40)
    BeginChrThread(0x9, 0, 0, 14)
    BeginChrThread(0x9, 1, 0, 12)
    BeginChrThread(0xA, 1, 0, 12)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0x0)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x101, 36500, 0, -10050, 315)
    SetChrPos(0x105, 38000, 0, -10200, 315)
    SetChrPos(0x107, 37550, 0, -12100, 315)
    SetChrPos(0x9, 37500, 5500, -11000, 0)
    SetChrPos(0xA, 37500, 5500, -11000, 0)
    BeginChrThread(0x9, 0, 0, 13)
    BeginChrThread(0xA, 0, 0, 13)
    OP_68(36500, 1000, -12500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(16000, 0)
    OP_68(33500, 1000, -8500, 3000)

    def lambda_36E9():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36E9)
    Sleep(50)

    def lambda_3701():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3701)
    Sleep(50)

    def lambda_3719():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3719)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    OP_25(0x1F1, 0x50)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x107, 0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x107, 0x80)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrPos(0x9, 37500, 20250, -11350, 315)
    SetChrPos(0xA, 37500, 20250, -11350, 315)

    def lambda_3789():
        OP_96(0xFE, 0x927C, 0x7A120, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3789)

    def lambda_37A3():
        OP_96(0xFE, 0x927C, 0x7A120, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_37A3)
    BeginChrThread(0x9, 0, 0, 16)
    BeginChrThread(0xA, 0, 0, 15)
    OP_68(36500, 16000, -12500, 0)
    MoveCamera(90, -65, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(1000)
    StopSound(497, 6000, 60)

    AnonymousTalk(
        0x101,
        (
            "#00001FAre they going back to\x01",
            "the skies for now?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10403FRight. If they stayed on\x01",
            "the ground, they could\x01",
            "be discovered.\x02\x03",
            "#10400FWell then─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x107, 0x80)
    SetChrPos(0x101, 38250, 0, -11450, 135)
    SetChrPos(0x105, 38250, 0, -12250, 135)
    SetChrPos(0x107, 36250, 0, -12950, 135)
    SetChrSubChip(0x107, 0x5)
    OP_68(38250, 1000, -12250, 0)
    MoveCamera(70, 20, 0, 0)
    OP_6E(680, 0)
    SetCameraDistance(15500, 0)
    OP_68(39230, 1000, -13300, 1500)
    OP_95(0x105, 39050, 0, -13100, 1000, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    SetCameraDistance(15000, 800)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10403F#5P#40W─In the name of Aidios, I\x01",
            "call upon the consecrated\x01",
            "seven lights.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sound(357, 0, 50, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x105, 0x0, 0, 50, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetCameraDistance(13000, 20000)
    BeginChrThread(0x105, 3, 0, 17)
    BeginChrThread(0x9, 1, 0, 18)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00005F#5PAh... (Just like Mrs.\x01",
            "Marble's...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CHmm... The Gral's\x01",
            "Thaumaturgy, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10403F#5P#40WAmberl of the earth, Goldia of the sky─\x02\x03",
            "#10401FBy fusing them, create form once again...\x01",
            "Establishing a small sacred precinct that\x01",
            "escapes from the great "Eye".\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x105, 0x3)
    SetCameraDistance(13000, 1000)
    Sleep(150)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x105, 0x3)
    Sleep(50)
    Sound(3091, 255, 80, 0)
    SetChrSubChip(0x105, 0x4)
    SetMapObjFrame(0x7, "Null_fream", 0x2, "start")
    Sleep(500)
    Sound(222, 0, 100, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 40700, 100, -14350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    FadeToDark(250, 16777215, -1)
    Sound(928, 0, 100, 0)
    Sound(934, 0, 50, 0)
    OP_0D()
    Sleep(500)
    StopSound(852, 1000, 100)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    FadeToBright(2000, 16777215)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#00001FThis is...\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10404F#11PA "magic circle" that\x01",
            "can fix the "gap" in the\x01",
            "force field.\x02\x03",
            "It is also charmed to be\x01",
            "invisible, except to us,\x01",
            "you know.\x02\x03",
            "#10402FWell, it should hold out\x01",
            "for a little while.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CFD():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3CFD)
    Sleep(50)

    def lambda_3D0D():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D0D)
    Sleep(50)

    def lambda_3D1D():
        TurnDirection(0x107, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3D1D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)

    ChrTalk(
        0x101,
        (
            "#00012F#5PI-I see.\x02\x03",
            "#00002FStill, Wazy... You really\x01",
            "are from the Church, huh.\x02\x03",
            "It's strange seeing you\x01",
            "like this after we've been\x01",
            "together for so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11PHehe. Well being a hard-\x01",
            "ass still isn't my thing,\x01",
            "that much hasn't changed.\x02\x03",
            "#10400F─So, what do we do?\x02\x03",
            "Should we try heading\x01",
            "towards St. Ursula\x01",
            "Hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah, let's go check out the\x01",
            "situation there.\x02\x03",
            "#00008FAlso... If we have time, I'd\x01",
            "like to look in the direction\x01",
            "of Crossbell City too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CHm, that's fine as well.\x02\x03",
            "#01201FHowever, due to Pleroma\x01",
            "Grass, Cryptids are\x01",
            "appearing on the highways.\x02\x03",
            "It'd be wise to tread\x01",
            "carefully.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xD7, 0x1F4)

    ChrTalk(
        0x101,
        "#00013F#5PYeah, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400F#11PThen, shall we?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_37()
    SetChrPos(0x0, 37370, 0, -13400, 270)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x9, 0x80)
    SetMapObjFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x1, 0x4)
    SetChrFlags(0xB, 0x80)
    SetMapObjFlags(0xA, 0x4)
    SetScenarioFlags(0x1A0, 2)
    OP_29(0xAF, 0x1, 0x1)
    OP_24(0x1F1)
    OP_24(0x3B6)
    OP_24(0x354)
    SetScenarioFlags(0x20, 5)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x33), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_33E8 end

    def Function_12_40A2(): pass

    label("Function_12_40A2")

    OP_96(0xFE, 0x927C, 0x1D4C, 0xFFFFD508, 0x9C4, 0x1)
    OP_96(0xFE, 0x927C, 0x1B58, 0xFFFFD508, 0x7D0, 0x1)
    OP_96(0xFE, 0x927C, 0x1964, 0xFFFFD508, 0x5DC, 0x1)
    OP_96(0xFE, 0x927C, 0x1770, 0xFFFFD508, 0x3E8, 0x1)
    OP_96(0xFE, 0x927C, 0x157C, 0xFFFFD508, 0x1F4, 0x1)
    BeginChrThread(0xFE, 3, 0, 13)
    Return()

    # Function_12_40A2 end

    def Function_13_410D(): pass

    label("Function_13_410D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_419B")
    OP_96(0xFE, 0x927C, 0x14B4, 0xFFFFD508, 0x190, 0x1)
    OP_96(0xFE, 0x927C, 0x1450, 0xFFFFD508, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0x927C, 0x14B4, 0xFFFFD508, 0xC8, 0x1)
    OP_96(0xFE, 0x927C, 0x1644, 0xFFFFD508, 0x190, 0x1)
    OP_96(0xFE, 0x927C, 0x16A8, 0xFFFFD508, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0x927C, 0x1644, 0xFFFFD508, 0xC8, 0x1)
    Jump("Function_13_410D")

    label("loc_419B")

    Return()

    # Function_13_410D end

    def Function_14_419C(): pass

    label("Function_14_419C")

    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0x1, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_75(0x8, 0x2, 0x7D0)
    OP_75(0xA, 0x2, 0x7D0)
    Sleep(1000)
    OP_79(0x1)
    OP_71(0x8, 0x65, 0xA0, 0x1, 0x20)
    Return()

    # Function_14_419C end

    def Function_15_41ED(): pass

    label("Function_15_41ED")

    OP_75(0x8, 0x1, 0x7D0)
    OP_75(0xA, 0x1, 0x7D0)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_71(0x1, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 2000, 40)
    OP_79(0x1)
    OP_71(0x1, 0x65, 0xA0, 0x0, 0x20)
    Return()

    # Function_15_41ED end

    def Function_16_423B(): pass

    label("Function_16_423B")

    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x28, 0x28, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x1E, 0x1E, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x14, 0x14, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0xA, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_16_423B end

    def Function_17_42A0(): pass

    label("Function_17_42A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42BA")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_17_42A0")

    label("loc_42BA")

    Return()

    # Function_17_42A0 end

    def Function_18_42BB(): pass

    label("Function_18_42BB")

    SetMapObjFrame(0x6, "Null_fream", 0x2, "start")
    Sleep(20000)
    SetMapObjFrame(0x6, "Null_fream", 0x2, "loop")
    Return()

    # Function_18_42BB end

    SaveToFile()

Try(main)
