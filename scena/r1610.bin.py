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
        "Function_3_6E1",          # 03, 3
        "Function_4_81B",          # 04, 4
        "Function_5_B54",          # 05, 5
        "Function_6_C19",          # 06, 6
        "Function_7_C72",          # 07, 7
        "Function_8_1424",         # 08, 8
        "Function_9_1D05",         # 09, 9
        "Function_10_3125",        # 0A, 10
        "Function_11_3455",        # 0B, 11
        "Function_12_40D8",        # 0C, 12
        "Function_13_4143",        # 0D, 13
        "Function_14_41D2",        # 0E, 14
        "Function_15_4223",        # 0F, 15
        "Function_16_4271",        # 10, 16
        "Function_17_42D6",        # 11, 17
        "Function_18_42F1",        # 12, 18
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

    Jump("loc_6E0")

    label("loc_64F")

    EventBegin(0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Azure Flowers are blooming.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00000F(What pretty flowers they're.\x01",
            "It seems they're faintly glowing, though...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x168, 3)
    EventEnd(0x3)

    label("loc_6E0")

    Return()

    # Function_2_623 end

    def Function_3_6E1(): pass

    label("Function_3_6E1")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003F(With this we've beaten\x01",
            "two Cryptids, but...\x01",
            "Something's bothering me.)\x02\x03",
            "#00000FEveryone, could we go back\x01",
            "again to the scene to investigate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIndeed, I too feel like there should be\x01",
            "something else we must do here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FThen, let's go back now and investigate.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2120, 0, -3710, 90)
    EventEnd(0x4)
    Return()

    # Function_3_6E1 end

    def Function_4_81B(): pass

    label("Function_4_81B")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84D")
    SetScenarioFlags(0x31, 2)

    label("loc_84D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_893")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_88D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_882")
    Sound(2499, 255, 100, 0)
    Jump("loc_888")

    label("loc_882")

    Sound(3537, 255, 100, 0)

    label("loc_888")

    Jump("loc_893")

    label("loc_88D")

    Sound(3344, 255, 100, 0)

    label("loc_893")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_906")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8E6"),
        (SWITCH_DEFAULT, "loc_8F7"),
    )


    label("loc_8E6")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_901")

    label("loc_8F7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_901")

    Jump("loc_B41")

    label("loc_906")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_938")
    MenuCmd(1, 0, "Rest in Orbal Car")

    label("loc_938")

    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_96A"),
        (1, "loc_A6E"),
        (2, "loc_AFF"),
        (SWITCH_DEFAULT, "loc_B37"),
    )


    label("loc_96A")

    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99B")
    OP_70(0x5, 0x12C)
    OP_71(0x5, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_9AB")

    label("loc_99B")

    OP_70(0x5, 0xF0)
    OP_71(0x5, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_9AB")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A01")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A01")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A24")
    Sound(461, 0, 100, 0)

    label("loc_A24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A44")
    OP_70(0x5, 0x14A)
    OP_71(0x5, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_A54")

    label("loc_A44")

    OP_70(0x5, 0x10E)
    OP_71(0x5, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_A54")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_70(0x5, 0x0)
    Jump("loc_893")

    label("loc_A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_AE0")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_AA3")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_ABB")

    label("loc_AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_AB6")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_ABB")

    label("loc_AB6")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_ABB")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AFA")

    label("loc_AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_AF0")
    OP_AF(0xFB)
    Jump("loc_AFA")

    label("loc_AF0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AFA")

    Jump("loc_B41")

    label("loc_AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B18")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B32")

    label("loc_B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_B28")
    OP_AF(0xFB)
    Jump("loc_B32")

    label("loc_B28")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B32")

    Jump("loc_B41")

    label("loc_B37")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B41")

    Jump("loc_893")

    label("loc_B46")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_81B end

    def Function_5_B54(): pass

    label("Function_5_B54")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
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
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C14")
    OP_E2(0x2)
    MiniGame(0x6, 0xE, 0xF032, 0xFFFFFC18, 0x1AAE, 0x5A, 0x10DE2, 0x0, 0x143C)

    label("loc_C14")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_5_B54 end

    def Function_6_C19(): pass

    label("Function_6_C19")

    Battle("BattleInfo_2E0", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5B")
    OP_90(0x0, 37650, 0, -3750, 90)
    EventEnd(0x5)
    Jump("loc_C71")

    label("loc_C5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6E")
    Jump("loc_C71")

    label("loc_C6E")

    Call(0, 8)

    label("loc_C71")

    Return()

    # Function_6_C19 end

    def Function_7_C72(): pass

    label("Function_7_C72")

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

    def lambda_D4E():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D4E)
    Sleep(0)

    def lambda_D66():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D66)
    Sleep(0)

    def lambda_D7E():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D7E)
    Sleep(0)

    def lambda_D96():
        OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D96)
    Sleep(0)

    def lambda_DAE():
        OP_9B(0x0, 0x109, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DAE)
    Sleep(0)

    def lambda_DC6():
        OP_9B(0x0, 0x105, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DC6)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED9")

    ChrTalk(
        0x109,
        "#10111F#5P(Ah...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(That's a "Cryptid"...!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_F13")

    label("loc_ED9")


    ChrTalk(
        0x105,
        "#10305F#6P(Whoa...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(There it is...!)\x02",
    )

    CloseMessageWindow()

    label("loc_F13")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1232")

    ChrTalk(
        0x104,
        (
            "#00303F#9P(Like the report said, it's quite huge...)\x02\x03",
            "#00301F(peTiote, how about the spatial distortion?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(Time, Space, Mirage... I confirm that\x01",
            "the three higher elements are at work.)\x02\x03",
            "#00201F(Currently, the cause is unknown.)\x02",
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

    def lambda_10F3():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10F3)
    Sleep(0)

    def lambda_1103():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1103)
    Sleep(0)

    def lambda_1113():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1113)
    Sleep(0)

    def lambda_1123():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1123)
    Sleep(0)

    def lambda_1133():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1133)
    Sleep(0)

    def lambda_1143():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1143)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10301F#6P(So...\x01",
            "What do we do?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11P(According to the CGF report,\x01",
            "it seems pretty dangerous...)\x02\x03",
            "#00013F(Let's cautiously prepare to exterminate it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5P(Roger...!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_13EE")

    label("loc_1232")


    ChrTalk(
        0x102,
        (
            "#00101F#9P(Tio...\x01",
            "What about the spatial distortion?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#9P(Likewise, the three higher elements are at work...)\x02\x03",
            "#00201F(As suspected, the cause is unknown.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#9P(As we thought, huh...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#9P(It seems that the Cryptid itself\x01",
            "is not the cause, though...)\x02",
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
            "#10101F#5P(Mr. Lloyd...\x01",
            "Should we prepare now?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5P(Yeah, let's proceed with caution...!)\x02",
    )

    CloseMessageWindow()

    label("loc_13EE")

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

    # Function_7_C72 end

    def Function_8_1424(): pass

    label("Function_8_1424")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FB")

    ChrTalk(
        0x101,
        (
            "#00006F#5PKh...\x01",
            "As expected, it was strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PAlso, it really...vanished\x01",
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

    def lambda_1634():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1634)
    Sleep(50)

    def lambda_1644():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1644)
    Sleep(50)

    def lambda_1654():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1654)
    Sleep(50)

    def lambda_1664():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1664)
    Sleep(50)

    def lambda_1674():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1674)
    Sleep(50)

    def lambda_1684():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1684)
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
            "#10108F#12PTio.\x01",
            "What about the "spatial distortion"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...No good.\x01",
            "The three higher elements are still at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#11PJeez...\x01",
            "What the heck is the cause?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#5PIt seems that the "Cryptid" itself\x01",
            "is not the cause, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00013F#11P...As expected, it seems we need\x01",
            "to check the other one too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5E")

    label("loc_17FB")


    ChrTalk(
        0x105,
        (
            "#10306F#5POh boy...\x01",
            "This one was strong too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PHowever, it vanished in the same way...\x02",
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

    def lambda_18AB():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18AB)
    Sleep(50)

    def lambda_18BB():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_18BB)
    Sleep(50)

    def lambda_18CB():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_18CB)
    Sleep(50)

    def lambda_18DB():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_18DB)
    Sleep(50)

    def lambda_18EB():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18EB)
    Sleep(50)

    def lambda_18FB():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_18FB)
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
            "#00301F#11PAs I'm expectin', the "spatial\x01",
            "distortion" is goin' on, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PYes...\x02\x03",
            "#00201FI feel like there is some kind\x01",
            "of material cause.\x02",
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
            "#00005F#11PA material cause...\x01",
            "What, for instance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#6P...Well...\x01",
            "My senses have been stirred by the\x01",
            ""distortion" since a little while...\x02\x03",
            "#00200FRather, maybe you all could\x01",
            "be able to find out the cause.\x02",
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
            "#00003F#11PAll right...\x01",
            "Let's search the vicinity.\x02\x03",
            "#00000FThere's going to be what is causing\x01",
            "the "spatial distortion" for sure.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B9A():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B9A)
    Sleep(50)

    def lambda_1BAA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1BAA)
    Sleep(50)

    def lambda_1BBA():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1BBA)
    Sleep(50)

    def lambda_1BCA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1BCA)
    Sleep(50)

    def lambda_1BDA():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BDA)
    Sleep(50)

    def lambda_1BEA():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1BEA)
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
        "#00300F#12PLet's investigate whatever we can find!\x02",
    )

    CloseMessageWindow()
    OP_29(0xA6, 0x1, 0x3)

    label("loc_1C5E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Defeated the St. Ursula Byroad Cryptid!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CF5")
    OP_1B(0x0, 0x0, 0x3)

    label("loc_1CF5")

    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_8_1424 end

    def Function_9_1D05(): pass

    label("Function_9_1D05")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2144")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 4)), scpexpr(EXPR_END)), "loc_1F48")

    AnonymousTalk(
        0x102,
        (
            "#00108FIf I remember correctly, they were blooming even\x01",
            "in the marshlands of East Crossbell Highway...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#00305FYeah, we saw 'em there, alright.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2003")

    label("loc_1F48")


    AnonymousTalk(
        0x105,
        (
            "#10302FWeren't they blooming even in the\x01",
            "marshlands of East Crossbell Highway?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        "#00011FI-Is that so?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00108FYes, I'm sure I feel like I\x01",
            "happened to see them too...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2003")


    AnonymousTalk(
        0x109,
        (
            "#10109FWhat very pretty flowers...\x02\x03",
            "#10102F...I don't remember having ever seen them,\x01",
            "I wonder how they're called?\x02",
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
            "#00003F#11P(...I think it's unlikely, but...)\x02\x03",
            "#00001F(Well, could it be worth a try?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x160, 5)
    OP_29(0xA6, 0x1, 0x4)
    Jump("loc_2202")

    label("loc_2144")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    AnonymousTalk(
        0x101,
        (
            "#00003F#11P(...I think it's unlikely, but...)\x02\x03",
            "#00001F(Well, could it be worth a try?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_2202")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Try to Pick Up the Azure Flowers\x01",      # 0
            "Do Not\x01",                                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2264"),
        (1, "loc_30E6"),
        (SWITCH_DEFAULT, "loc_3124"),
    )


    label("loc_2264")

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
            "#10305F#6PWhat, do you want to\x01",
            "pick up these flowers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PYeah...\x01",
            "Although I'm a little sorry for them──\x02",
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
        "#00301F#5PH-Huh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12PThis is...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PUgh...!\x02",
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
        "#00108FSomehow it seems the space warped...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    ChrTalk(
        0x105,
        (
            "#10308F#6P...Tio.\x01",
            "What about the "spatial distortion"?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    ChrTalk(
        0x103,
        (
            "#00203F#12P...The three higher elements\x01",
            "presence has vanished.\x02\x03",
            "#00201FI can't sense any anomaly\x01",
            "in this area anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#5PW-Wait a sec.\x02\x03",
            "#00307FYou want to tell me that those azure\x01",
            "flowers were causin' the anomaly!?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#10304F#6PWell, it's possible.\x02\x03",
            "#10300F...Although I can't think that such \x01",
            "tiny flowers have that kind of power.\x02",
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
            "#10101F#5PW-What kind of\x01",
            "flowers are these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P...I don't sense any strange \x01",
            "presence from those flowers...\x02\x03",
            "#00200FAt any rate, should we have them\x01",
            "investigated somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11PYou're right...\x02\x03",
            "#00003F...It's probably a different field than\x01",
            "that the medical college delves in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FA-At any rate, let's keep them\x01",
            "stored so we don't lose them.\x02\x03",
            "If we come up with some idea,\x01",
            "we'll have them investigated, ok?\x02",
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
        "#10303F#6P...Hm...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_2A52():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A52)
    Sleep(50)

    def lambda_2A62():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2A62)
    Sleep(50)

    def lambda_2A72():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2A72)
    Sleep(50)

    def lambda_2A82():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2A82)
    Sleep(50)

    def lambda_2A92():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A92)
    Sleep(50)

    def lambda_2AA2():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2AA2)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#11PWazy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PDo you have any idea?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PWell...\x01",
            "Maybe it's a faint memory of mine.\x02\x03",
            "#10301FI feel like there was a legend about a mysterious\x01",
            "azure flower in the Church Testaments.\x02",
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
        "#00011F#11PWhat...!?\x02",
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
            "#10306F#6PWell, I feel I happened to see it when\x01",
            "skimming through them a very long time ago...\x02\x03",
            "#10300FElie or anyone else, do you have any idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PAs you can imagine, I haven't\x01",
            "looked at all the Testaments, but...\x02\x03",
            "#00103F...But indeed, I feel like I\x01",
            "read such a passage.\x02\x03",
            "#00108FA legend of an "Azure Flower" which\x01",
            "holds a mysterious power...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    ChrTalk(
        0x109,
        (
            "#10111F#6PI-Isn't that...\x01",
            "Exactly it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#00201F#12PAt least it appears it's worth it to confirm\x01",
            "with someone belonging to the Church.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E69():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E69)
    Sleep(50)

    def lambda_2E79():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E79)
    Sleep(50)

    def lambda_2E89():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2E89)
    Sleep(50)

    def lambda_2E99():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E99)
    Sleep(50)

    def lambda_2EA9():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2EA9)
    Sleep(50)

    def lambda_2EB9():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2EB9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F79")

    ChrTalk(
        0x101,
        (
            "#00003F#11P...Right.\x02\x03",
            "#00000FLet's try asking for advice to\x01",
            "teacher Marble or Miss Ries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes...\x01",
            "They're both suited, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3039")

    label("loc_2F79")


    ChrTalk(
        0x101,
        (
            "#00003F#11P...Right.\x02\x03",
            "#00000FI think that teacher Marble would\x01",
            "be the easiest to consult with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYes, I think she's competent.\x02\x03",
            "#00108F(We could consult with "her" too, but...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3039")


    ChrTalk(
        0x104,
        (
            "#00300F#5POk, then, let's head\x01",
            "to Crossbell Cathedral!\x02",
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
    Jump("loc_3124")

    label("loc_30E6")

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
    Jump("loc_3124")

    label("loc_3124")

    Return()

    # Function_9_1D05 end

    def Function_10_3125(): pass

    label("Function_10_3125")

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
            "#10100FB-By the way...\x02\x03",
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
            "Maybe they'll turn to be\x01",
            "valuable samples.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x103,
        (
            "#00200F...You are right. It seems that when you\x01",
            "pick them up, they lose strength.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        (
            "#00100FHowever...if a Cryptid appears again,\x01",
            "maybe we'll have to pick them up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        "#00300FWell, we'll think about it if it happens.\x02",
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

    # Function_10_3125 end

    def Function_11_3455(): pass

    label("Function_11_3455")

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

    def lambda_3756():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3756)
    Sleep(50)

    def lambda_376E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_376E)
    Sleep(50)

    def lambda_3786():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3786)
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

    def lambda_37F6():
        OP_96(0xFE, 0x927C, 0x7A120, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_37F6)

    def lambda_3810():
        OP_96(0xFE, 0x927C, 0x7A120, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3810)
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
        "#00001FAre they returning airborne for now?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10403FYeah, there's the danger they get discovered\x01",
            "if they keep lingering on the ground.\x02\x03",
            "#10400FWell then──\x02",
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
            "#10403F#5P#40W──In the name of the Goddess of the Sky,\x01",
            "here are the consecrated seven lights.\x07\x00\x02",
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
            "#00005F#5PAh...\x01",
            "(It's similar to teacher Marble's...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        "#01200F#6P#3CHm, the Gral's Thaumaturgy, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10403F#5P#40WAmber of the earth, gold of the sky──\x02\x03",
            "#10401FBy fusing them, form again\x01",
            "a small sacred precinct that\x01",
            "escapes from the great "eye".\x02",
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
        "#00001FThat's...\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10404F#11PA "magic circle" that can fix\x01",
            "the "gap" of the force field.\x02\x03",
            "It also  has invisible charms,\x01",
            "except to us.\x02\x03",
            "#10402FWell, it should hold\x01",
            "out for a little while.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D62():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D62)
    Sleep(50)

    def lambda_3D72():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D72)
    Sleep(50)

    def lambda_3D82():
        TurnDirection(0x107, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3D82)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)

    ChrTalk(
        0x101,
        (
            "#00012F#5PI-I see.\x02\x03",
            "#00002FStill, Wazy... You really are\x01",
            "someone from the Church.\x02\x03",
            "From your speech and conduct until now,\x01",
            "it didn't sink in me very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#11PUh uh, the fact that\x01",
            "I am serious has\x01",
            "never changed, though.\x02\x03",
            "#10400F──So, what do we do?\x02\x03",
            "Should we try going near\x01",
            "St. Ursula Hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PYeah, let's go check the situation.\x02\x03",
            "#00008FAlso...\x01",
            "If we have time, I'd like to look in\x01",
            "the direction of Crossbell City too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CHm, that's fine too.\x02\x03",
            "#01201FHowever, due to Pleroma Grass,\x01",
            "Cryptids are appearing on the highways.\x02\x03",
            "Be very careful.\x02",
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

    # Function_11_3455 end

    def Function_12_40D8(): pass

    label("Function_12_40D8")

    OP_96(0xFE, 0x927C, 0x1D4C, 0xFFFFD508, 0x9C4, 0x1)
    OP_96(0xFE, 0x927C, 0x1B58, 0xFFFFD508, 0x7D0, 0x1)
    OP_96(0xFE, 0x927C, 0x1964, 0xFFFFD508, 0x5DC, 0x1)
    OP_96(0xFE, 0x927C, 0x1770, 0xFFFFD508, 0x3E8, 0x1)
    OP_96(0xFE, 0x927C, 0x157C, 0xFFFFD508, 0x1F4, 0x1)
    BeginChrThread(0xFE, 3, 0, 13)
    Return()

    # Function_12_40D8 end

    def Function_13_4143(): pass

    label("Function_13_4143")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41D1")
    OP_96(0xFE, 0x927C, 0x14B4, 0xFFFFD508, 0x190, 0x1)
    OP_96(0xFE, 0x927C, 0x1450, 0xFFFFD508, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0x927C, 0x14B4, 0xFFFFD508, 0xC8, 0x1)
    OP_96(0xFE, 0x927C, 0x1644, 0xFFFFD508, 0x190, 0x1)
    OP_96(0xFE, 0x927C, 0x16A8, 0xFFFFD508, 0xC8, 0x1)
    Sleep(200)
    OP_96(0xFE, 0x927C, 0x1644, 0xFFFFD508, 0xC8, 0x1)
    Jump("Function_13_4143")

    label("loc_41D1")

    Return()

    # Function_13_4143 end

    def Function_14_41D2(): pass

    label("Function_14_41D2")

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

    # Function_14_41D2 end

    def Function_15_4223(): pass

    label("Function_15_4223")

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

    # Function_15_4223 end

    def Function_16_4271(): pass

    label("Function_16_4271")

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

    # Function_16_4271 end

    def Function_17_42D6(): pass

    label("Function_17_42D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42F0")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_17_42D6")

    label("loc_42F0")

    Return()

    # Function_17_42D6 end

    def Function_18_42F1(): pass

    label("Function_18_42F1")

    SetMapObjFrame(0x6, "Null_fream", 0x2, "start")
    Sleep(20000)
    SetMapObjFrame(0x6, "Null_fream", 0x2, "loop")
    Return()

    # Function_18_42F1 end

    SaveToFile()

Try(main)
