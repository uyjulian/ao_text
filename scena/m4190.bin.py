from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4190.bin",                # FileName
        "m4190",                    # MapName
        "m4190",                    # Location
        0x00C8,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x28,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 200, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4190",                  # 0
        "フェアリードレイク",     # 1
        "Zeit",                   # 2
        "Miner Gantz",            # 3
        "Miner Marlow",           # 4
        "Miner Max",              # 5
        "Mine Captain Hoffman",   # 6
        "Miner Logy",             # 7
        "SE制御",                 # 8
        "bm4120",                 # 9
        "bm4120",                 # 10
    ))

    ATBonus("ATBonus_26C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_28C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_310", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_314", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_318", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_31C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_320", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_324", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_32C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_390", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm4120", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67000.dat", "ms67000.dat", "ms67000.dat", "ms67000.dat", "ms67000.dat", "ms67000.dat", 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_30C", "ed7451", "ed7453", "ATBonus_26C"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_34C", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm4120", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_30C", "ed7454", "ed7000", "ATBonus_26C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch67050.itc",               # 10
        "monster/ch67050.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294966906, 3710,    0,       0x18500B4,    "BattleInfo_390", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 43,  -0.38999998569488525,  3.7100000381469727,    -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   0.04874999821186066,   -0.4637500047683716,   0.25,                  1.0])

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(250, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_49C",          # 00, 0
        "Function_1_4BD",          # 01, 1
        "Function_2_607",          # 02, 2
        "Function_3_2831",         # 03, 3
        "Function_4_28AF",         # 04, 4
        "Function_5_28CB",         # 05, 5
        "Function_6_28E7",         # 06, 6
        "Function_7_2903",         # 07, 7
        "Function_8_291F",         # 08, 8
        "Function_9_29A6",         # 09, 9
        "Function_10_29D0",        # 0A, 10
        "Function_11_2A53",        # 0B, 11
        "Function_12_2B02",        # 0C, 12
        "Function_13_2B12",        # 0D, 13
        "Function_14_2B22",        # 0E, 14
        "Function_15_2B78",        # 0F, 15
        "Function_16_2BCB",        # 10, 16
        "Function_17_2C24",        # 11, 17
        "Function_18_2C91",        # 12, 18
        "Function_19_2CEA",        # 13, 19
        "Function_20_2D40",        # 14, 20
        "Function_21_2D90",        # 15, 21
        "Function_22_2DDD",        # 16, 22
        "Function_23_2DFC",        # 17, 23
        "Function_24_2E1B",        # 18, 24
        "Function_25_2E3A",        # 19, 25
        "Function_26_2E59",        # 1A, 26
        "Function_27_2E97",        # 1B, 27
        "Function_28_2EEC",        # 1C, 28
        "Function_29_2F22",        # 1D, 29
        "Function_30_3020",        # 1E, 30
        "Function_31_30A2",        # 1F, 31
        "Function_32_3228",        # 20, 32
        "Function_33_3244",        # 21, 33
        "Function_34_325E",        # 22, 34
        "Function_35_3330",        # 23, 35
        "Function_36_4300",        # 24, 36
        "Function_37_431F",        # 25, 37
        "Function_38_434B",        # 26, 38
        "Function_39_4386",        # 27, 39
        "Function_40_43B2",        # 28, 40
        "Function_41_43D6",        # 29, 41
        "Function_42_4402",        # 2A, 42
        "Function_43_4426",        # 2B, 43
    ))


    def Function_0_49C(): pass

    label("Function_0_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AD")
    Event(0, 2)

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4BC")
    ClearScenarioFlags(0x22, 0)
    Event(0, 35)

    label("loc_4BC")

    Return()

    # Function_0_49C end

    def Function_1_4BD(): pass

    label("Function_1_4BD")

    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EA")
    ClearChrFlags(0x10, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x10, 0x8000)

    label("loc_4EA")

    Jump("loc_4F9")

    label("loc_4EF")

    SetChrFlags(0x10, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_4F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_540")
    SetMapObjFrame(0xFF, "flower00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "flower01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "flower04", 0x0, 0x1)

    label("loc_540")

    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_4BD end

    def Function_2_607(): pass

    label("Function_2_607")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x4, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x104, 0x8)
    OP_32(0x3, 0x0, 0x38)
    OP_32(0x3, 0x5, 0x64)
    OP_42(0x3, 0x425, 0xFF)
    OP_42(0x3, 0x5DD, 0xFF)
    OP_42(0x3, 0x643, 0xFF)
    RemoveCraft(0x3, 0xFFFF)
    OP_38(0x3, 0x80, 0x2)
    OP_38(0x3, 0x81, 0x1)
    OP_38(0x3, 0x83, 0x1)
    OP_38(0x3, 0x84, 0x1)
    OP_38(0x3, 0x85, 0x1)
    OP_42(0x3, 0xE2, 0x0)
    OP_42(0x3, 0x84, 0x1)
    OP_42(0x3, 0x6C, 0x3)
    OP_42(0x3, 0x70, 0x4)
    OP_42(0x3, 0x64, 0x5)
    AddCraft(0x3, 0xB4)
    AddCraft(0x3, 0xB5)
    AddCraft(0x3, 0xB6)
    AddCraft(0x3, 0xB7)
    AddCraft(0x3, 0xB8)
    AddCraft(0x3, 0x127)
    AddCraft(0x3, 0x128)
    SetChrChipPat(0x3, 0x6, 0x127)
    SetChrChipPat(0x3, 0x6, 0x128)
    SetChrChipPat(0x3, 0x6, 0x12A)
    SetChrChipPat(0x3, 0x6, 0x12B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CE")
    AddCraft(0x3, 0x1B0)
    AddCraft(0x0, 0x1B0)
    Jump("loc_6EC")

    label("loc_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6E4")
    AddCraft(0x3, 0x19C)
    AddCraft(0x0, 0x19C)
    Jump("loc_6EC")

    label("loc_6E4")

    AddCraft(0x3, 0x188)
    AddCraft(0x0, 0x188)

    label("loc_6EC")

    AddCraft(0x1, 0x18A)
    AddCraft(0x3, 0x18A)
    AddCraft(0x0, 0x15E)
    AddCraft(0x1, 0x161)
    AddCraft(0x3, 0x167)
    AddCraft(0x8, 0x176)
    AddCraft(0x4, 0x16A)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00053.itc", 0x20)
    LoadChrToIndex("chr/ch00056.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00153.itc", 0x24)
    LoadChrToIndex("chr/ch00156.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch02953.itc", 0x28)
    LoadChrToIndex("chr/ch02956.itc", 0x29)
    LoadChrToIndex("chr/ch03050.itc", 0x2A)
    LoadChrToIndex("chr/ch03051.itc", 0x2B)
    LoadChrToIndex("chr/ch03053.itc", 0x2C)
    LoadChrToIndex("chr/ch03056.itc", 0x2D)
    LoadChrToIndex("chr/ch00350.itc", 0x2E)
    LoadChrToIndex("chr/ch00351.itc", 0x2F)
    LoadChrToIndex("chr/ch00356.itc", 0x30)
    LoadChrToIndex("chr/ch02750.itc", 0x31)
    LoadChrToIndex("chr/ch02751.itc", 0x32)
    LoadChrToIndex("chr/ch02752.itc", 0x33)
    LoadChrToIndex("chr/ch00352.itc", 0x34)
    LoadEffect(0x0, "event/ev11010.eff")
    LoadEffect(0x1, "battle/bs011_00.eff")
    LoadEffect(0x2, "battle/bs881010.eff")
    LoadEffect(0x3, "event/eva01_01.eff")
    LoadEffect(0x4, "event/eva04_00.eff")
    LoadEffect(0x5, "event/ev11011.eff")
    LoadEffect(0x6, "battle/cr036011.eff")
    LoadEffect(0x7, "event/ev10008.eff")
    LoadEffect(0x8, "event/ev10017.eff")
    SoundLoad(2751)
    SoundLoad(2752)
    SoundLoad(825)
    SoundLoad(931)
    SoundLoad(950)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis234.itp")
    SetChrChipByIndex(0x9, 0x31)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x101, 0, 0, -61500, 0)
    SetChrPos(0x102, 1400, 0, -61500, 0)
    SetChrPos(0x109, 0, 0, -62900, 0)
    SetChrPos(0x105, 1400, 0, -62900, 0)
    SetMapObjFlags(0x0, 0x4)
    OP_68(700, 1800, -58700, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29850, 0)
    OP_68(0, 1300, -52500, 3500)
    SetCameraDistance(28570, 3500)
    FadeToBright(1000, 0)

    def lambda_936():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_936)
    Sleep(50)

    def lambda_94E():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94E)
    Sleep(50)

    def lambda_966():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_966)
    Sleep(50)

    def lambda_97E():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_97E)
    OP_0D()
    MoveCamera(35, 20, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(27500, 2500)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00105F#11PWhat is this place...\x02",
    )

    CloseMessageWindow()
    OP_68(790, 1500, -52520, 2500)
    MoveCamera(10, 12, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(19620, 2500)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001F#6PIt looks like this old\x01",
            "mine's terminus...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_A48():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A48)
    Sleep(50)

    def lambda_A60():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A60)
    Sleep(50)

    def lambda_A78():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A78)
    Sleep(50)

    def lambda_A90():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A90)
    Sleep(700)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrPos(0x101, -700, 0, -41000, 0)
    SetChrPos(0x102, 700, 0, -41000, 0)
    SetChrPos(0x109, -700, 0, -42400, 0)
    SetChrPos(0x105, 700, 0, -42400, 0)
    OP_68(0, 1900, -27500, 0)
    MoveCamera(25, 16, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(26620, 0)
    MoveCamera(25, 24, 0, 7000)
    Fade(500)

    def lambda_B3A():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B3A)
    Sleep(50)

    def lambda_B52():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B52)
    Sleep(50)

    def lambda_B6A():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B6A)
    Sleep(50)

    def lambda_B82():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B82)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    SetChrPos(0x101, -700, 0, -10000, 0)
    SetChrPos(0x102, 700, 0, -10000, 0)
    SetChrPos(0x109, -700, 0, -11400, 0)
    SetChrPos(0x105, 700, 0, -11400, 0)
    OP_68(30, 2300, -8700, 0)
    MoveCamera(120, 8, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13960, 0)
    OP_68(0, 2300, -3200, 5500)
    MoveCamera(50, 12, 0, 5500)
    SetCameraDistance(19670, 5500)
    Fade(500)

    def lambda_C56():
        OP_9B(0x1, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C56)
    Sleep(50)

    def lambda_C6E():
        OP_9B(0x1, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C6E)
    Sleep(50)

    def lambda_C86():
        OP_9B(0x1, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C86)
    Sleep(50)

    def lambda_C9E():
        OP_9B(0x1, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C9E)
    OP_0D()
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(100)
    WaitChrThread(0x102, 1)
    BeginChrThread(0x102, 3, 0, 5)
    Sleep(100)
    WaitChrThread(0x109, 1)
    BeginChrThread(0x109, 3, 0, 6)
    Sleep(100)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x105, 3, 0, 7)
    Sleep(2500)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    OP_68(0, 1200, -3700, 1500)
    MoveCamera(55, 18, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(13700, 1500)

    def lambda_D26():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D26)
    Sleep(350)

    def lambda_D36():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D36)
    Sleep(150)

    def lambda_D46():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D46)
    Sleep(150)

    def lambda_D56():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D56)
    Sleep(350)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#10106F#12P...In the end, we couldn't\x01",
            "find a passage.\x02\x03",
            "#10101FWhat do we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PLet's see...\x02\x03",
            "#00001F...It could be dangerous, but it seems we can \x01",
            "only retrace our steps toward the entrance.\x02\x03",
            "Judging by our search in the tunnels,\x01",
            "it appears there aren't other traps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#11PAt any rate, it's incomprehensible.\x02\x03",
            "#10301FIn the end, what did the culprits\x01",
            "who blew up the entrance and set\x01",
            "the traps wanted to do?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)
    Sleep(200)

    ChrTalk(
        0x102,
        (
            "#00106F#5PRight...\x01",
            "It seems it's not directly connected\x01",
            "to these strange interiors...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_12FB")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#00101F#5PCould it be...\x01",
            "The people who visited the Doll Studio?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1036():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1036)
    Sleep(100)

    def lambda_1046():
        TurnDirection(0x109, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1046)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        "#10111F#12PAh...\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    ChrTalk(
        0x105,
        (
            "#10301F#11PHm, they were some\x01",
            "fishy people for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PYou're right...\x02",
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
            "It Is Very Possible\x01",      # 0
            "It Is Unlikely\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    def lambda_1145():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1145)
    Sleep(100)

    def lambda_1155():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1155)
    Sleep(100)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_117E"),
        (1, "loc_1231"),
        (SWITCH_DEFAULT, "loc_12F6"),
    )


    label("loc_117E")


    ChrTalk(
        0x101,
        (
            "#00006F#6P...Based on the timing,\x01",
            "it could be very possible.\x02\x03",
            "#00001FHowever, we can't say it for sure,\x01",
            "because the motive is not clear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#11PYou're right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_12F6")

    label("loc_1231")

    OP_2C(0xA2, 0x1)

    ChrTalk(
        0x101,
        (
            "#00003F#6PNo. The culprits destroyed a solid gate\x01",
            "and set traps which use explosives.\x02\x03",
            "#00001FTo me, they didn't look like\x01",
            "the type to do such things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#11PYes, indeed...\x02",
    )

    CloseMessageWindow()
    Jump("loc_12F6")

    label("loc_12F6")

    Jump("loc_12FB")

    label("loc_12FB")


    ChrTalk(
        0x109,
        (
            "#10108F#12PHmmm...\x01",
            "I wonder who could've done it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P(They were set yesterday and today\x01",
            "we received a call at the SSS.)\x02\x03",
            "(It just seems like it was\x01",
            "directly aimed at us...)\x02\x03",
            "#00008F(...Could I be really thinking too much?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        "#00105F#11PLloyd, what's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#12PA-Are you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PYes...\x01",
            "Let's go back for now.\x02\x03",
            "#00000FMr. Gantz could've\x01",
            "called for help...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-50, 2400, -3250, 0)
    MoveCamera(304, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8750, 0)
    OP_0D()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#00005F#11P(...Hm...?)\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetCameraDistance(48590, 0)
    OP_68(-20520, 2100, 2420, 0)
    MoveCamera(325, 37, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(46500, 0)
    SetCameraDistance(41350, 3000)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#00001F#5P#N...Those are...\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-50, 2100, -3250, 0)
    MoveCamera(304, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8750, 0)
    OP_68(280, 1800, -3380, 1000)
    OP_0D()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x105, 0x4B, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x105,
        "#10307F#5P#4S──Watch out from above!\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_16A7():
        OP_93(0x101, 0x4B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16A7)
    Sleep(15)

    def lambda_16B7():
        OP_93(0x102, 0x4B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_16B7)
    Sleep(15)

    def lambda_16C7():
        OP_93(0x109, 0x4B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16C7)
    Sleep(15)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#00013FWhat#5P...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    MoveCamera(295, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8750, 0)
    SetChrPos(0x101, -700, 0, -4500, 75)
    SetChrPos(0x102, 700, 0, -4500, 75)
    SetChrPos(0x109, -700, 0, -5900, 75)
    SetChrPos(0x105, 700, 0, -5900, 75)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x1E0, 0x20C, 0x1, 0x20)
    SetChrPos(0x8, 22000, 14000, -1500, 0)
    OP_93(0x8, 0x104, 0x0)
    SetChrFlags(0x8, 0x1)
    ClearChrFlags(0x8, 0x4)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 3, 0, 8)
    BeginChrThread(0xF, 1, 0, 32)
    OP_68(8930, 3500, -2240, 0)
    MoveCamera(47, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(43790, 0)
    SetCameraDistance(42790, 1000)
    Fade(500)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    OP_68(6470, 3600, -3210, 1500)
    MoveCamera(62, -5, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(19830, 1500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(2500)
    WaitChrThread(0x8, 3)
    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    Sound(842, 0, 100, 0)
    Sound(893, 0, 80, 0)
    PlayEffect(0x8, 0x6, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 18)
    BeginChrThread(0x105, 3, 0, 21)
    BeginChrThread(0x101, 3, 0, 19)
    BeginChrThread(0x109, 3, 0, 20)
    WaitChrThread(0x8, 3)
    BeginChrThread(0x8, 3, 0, 10)
    StopEffect(0x6, 0x2)
    Sleep(200)
    OP_68(-1760, 2100, -5530, 800)
    MoveCamera(68, 0, 0, 800)
    OP_6E(700, 800)
    SetCameraDistance(13510, 800)
    Sleep(1500)

    ChrTalk(
        0x109,
        "#10110F#6P#N#8AWha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#6P#N#10AA m-monster...!?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)
    CloseMessageWindow()
    OP_5A()
    OP_6F(0x79)
    OP_68(-910, 2100, -7160, 1500)
    MoveCamera(67, 9, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(17710, 1500)
    BeginChrThread(0x8, 3, 0, 11)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0x101, 3, 0, 22)
    Sleep(50)
    Sound(805, 0, 100, 0)
    BeginChrThread(0x102, 3, 0, 23)
    Sleep(50)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x109, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 25)
    Sleep(50)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00007F#6P#NW-What is this thing!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10310F#6P#NIt's no normal monster!\x01",
            "Please be caref──\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0x8, 3)
    OP_68(3340, 3800, -9280, 0)
    MoveCamera(89, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14230, 0)
    OP_71(0x0, 0x78, 0x8C, 0x1, 0x0)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(2000)
    BeginChrThread(0x8, 2, 0, 12)
    BeginChrThread(0x8, 1, 0, 14)
    Fade(500)
    OP_0D()
    SetCameraDistance(19280, 1200)
    Sleep(1200)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    SetMapObjFrame(0xFF, "m4190:Layer17", 0x0, 0x1)
    OP_68(460, 2400, -8090, 0)
    MoveCamera(340, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(33000, 0)
    MoveCamera(340, 10, 0, 2000)
    SetCameraDistance(23000, 2000)
    Fade(500)
    OP_0D()
    EndChrThread(0x8, 0x1)
    Sleep(500)
    Sleep(100)
    Sound(825, 2, 80, 0)
    Sound(931, 2, 50, 0)
    Sound(950, 2, 60, 0)
    Sleep(300)
    BeginChrThread(0x8, 3, 0, 16)
    Sleep(400)
    SetChrChipByIndex(0x101, 0x20)
    BeginChrThread(0x101, 3, 0, 26)
    PlayEffect(0x5, 0x2, 0x101, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrChipByIndex(0x102, 0x24)
    BeginChrThread(0x102, 3, 0, 26)
    PlayEffect(0x5, 0x3, 0x102, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrChipByIndex(0x105, 0x2C)
    BeginChrThread(0x105, 3, 0, 26)
    PlayEffect(0x5, 0x4, 0x105, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrChipByIndex(0x109, 0x28)
    BeginChrThread(0x109, 3, 0, 26)
    PlayEffect(0x5, 0x5, 0x109, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_6F(0x79)
    SetMapObjFrame(0xFF, "m4190:Layer17", 0x1, 0x1)
    OP_68(-1270, 1800, -7100, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18170, 0)
    Fade(500)
    OP_0D()
    Sleep(200)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(150)
    BeginChrThread(0x102, 3, 0, 27)
    Sleep(150)
    BeginChrThread(0x105, 3, 0, 27)
    Sleep(150)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(150)
    Sleep(400)
    OP_71(0x0, 0x96, 0x9F, 0x1, 0x0)
    BeginChrThread(0x8, 2, 0, 13)
    Sleep(400)

    ChrTalk(
        0x102,
        "#00106F#6P#NEEEEK!?\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        "#10108F#6P#NM-My body...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00010F#6P#NWhat the...I'm losing strength...!?\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10307F#6P#NT-These vibrations are\x01",
            "stealing our energies...!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-1270, 1800, -7100, 4500)
    MoveCamera(145, 13, 0, 4500)
    OP_6E(700, 4500)
    SetCameraDistance(18170, 4500)
    BeginChrThread(0x8, 1, 0, 17)
    Sleep(3000)

    ChrTalk(
        0x105,
        "#10310F#12P#N...Kh...this is bad...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00007F#12P#NCrap...\x01",
            "Elie and Noｱl, at least you two...!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x102,
        "#00107F#6P#ND-Don't say something foolish...!\x01\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10107F#12P#NThat's right...!\x01",
            "We'll have to get away all together...!\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()
    OP_68(-760, 2500, -8580, 1500)
    MoveCamera(147, 1, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(17140, 1500)
    OP_68(-760, 2500, -8580, 0)
    MoveCamera(147, 1, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17140, 0)
    Fade(500)
    OP_71(0x0, 0x78, 0x8C, 0x1, 0x0)
    Sound(842, 0, 100, 0)
    EndChrThread(0x8, 0x1)
    BeginChrThread(0x8, 1, 0, 14)
    BeginChrThread(0x8, 2, 0, 12)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x101,
        "#00015F#12P#NKh...!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(3046, 0, 100, 0)
    Sleep(1000)
    StopSound(931, 1000, 50)
    StopSound(950, 1000, 40)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 1, 0, 15)
    StopEffect(0x2, 0x2)
    PlayEffect(0x6, 0xFF, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(211, 0, 80, 0)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    StopEffect(0x3, 0x2)
    PlayEffect(0x6, 0xFF, 0x102, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    StopEffect(0x4, 0x2)
    PlayEffect(0x6, 0xFF, 0x109, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    StopEffect(0x5, 0x2)
    PlayEffect(0x6, 0xFF, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    Sleep(500)
    StopSound(825, 1000, 90)

    ChrTalk(
        0x109,
        "#10105F#12P#NAh...\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x101,
        "#00011F#12P#NThat now was...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrPos(0x104, 1250, 0, -60500, 352)
    OP_A7(0x104, 0x0, 0x0, 0x0, 0xFF, 0x0)

    def lambda_2196():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_2196)
    OP_68(-2760, 2500, -7990, 0)
    MoveCamera(163, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17140, 0)
    OP_68(-4090, 900, -33450, 2000)
    MoveCamera(153, 9, 0, 2000)
    OP_6E(700, 2000)
    SetCameraDistance(21870, 2000)
    Fade(500)
    BeginChrThread(0x104, 1, 0, 28)
    OP_0D()
    OP_6F(0x79)
    Sound(2765, 255, 100, 0)
    OP_68(-4120, 2100, -31180, 0)
    MoveCamera(95, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13730, 0)
    OP_68(-6300, 1900, -25480, 1400)
    MoveCamera(95, 0, 0, 1400)
    OP_6E(700, 1400)
    SetCameraDistance(13430, 1400)
    Fade(500)
    Sleep(650)
    SetChrChip(0x0, 0x104, 0x32, 0x2EE)
    OP_0D()
    OP_6F(0x79)
    OP_68(-6300, 3000, -5480, 1600)
    MoveCamera(95, 0, 0, 1600)
    OP_6E(700, 1600)
    SetCameraDistance(13430, 1600)
    OP_6F(0x79)
    StopEffect(0x2, 0x0)
    OP_68(-4280, 3300, -6210, 500)
    MoveCamera(134, 10, 0, 500)
    OP_6E(700, 500)
    SetCameraDistance(13210, 500)
    Sleep(200)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    StopEffect(0x1, 0x2)
    EndChrThread(0x8, 0x1)
    OP_70(0x0, 0x294)
    Sleep(500)
    SetChrChip(0x1, 0x104, 0x0, 0x0)
    Sleep(500)
    Sound(591, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Sound(842, 0, 100, 0)
    OP_71(0x0, 0x294, 0x2E5, 0x0, 0x0)
    BeginChrThread(0x8, 2, 0, 13)
    BeginChrThread(0x104, 3, 0, 30)
    OP_68(-2530, 600, -9630, 1500)
    MoveCamera(146, 11, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(15200, 1500)
    WaitChrThread(0x104, 3)
    Sleep(1000)
    Fade(350)

    def lambda_236D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_236D)
    Sleep(50)

    def lambda_2389():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2389)
    Sleep(50)

    def lambda_23A5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_23A5)
    Sleep(50)

    def lambda_23C1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23C1)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x105, 0x2A)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    OP_0D()

    def lambda_241A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_241A)
    Sleep(100)

    def lambda_242A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_242A)
    Sleep(100)

    def lambda_243A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_243A)
    Sleep(100)

    def lambda_244A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_244A)

    ChrTalk(
        0x101,
        "#00002F#6PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#6PSenior Randy...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PY-You're here...!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -10500, 10000, -42000, 0)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-10500, 3500, -38000, 0)
    MoveCamera(217, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27390, 0)
    SetCameraDistance(23390, 0)
    Fade(500)
    SetChrPos(0x101, -5310, 0, -9830, 135)
    SetChrPos(0x109, -6130, 0, -11080, 135)
    SetChrPos(0x105, -6410, 0, -8500, 135)
    SetChrPos(0x102, -4640, 0, -6980, 135)
    TurnDirection(0x104, 0x8, 500)
    BeginChrThread(0x9, 3, 0, 31)
    OP_0D()
    OP_68(0, 1300, -10000, 3500)
    MoveCamera(135, 16, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(18000, 3500)
    OP_6F(0x79)
    WaitChrThread(0x9, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(3049, 255, 100, 0)

    ChrTalk(
        0x9,
        "#01207F#11P#4SWoof!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00002F#6P#NZeit too...!\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10309F#6P#NAhaha!\x01",
            "Isn't your timing just too good!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(2870, 2200, -10980, 3000)
    MoveCamera(100, 0, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(18860, 3000)
    WaitChrThread(0x8, 2)
    ClearMapObjFlags(0x0, 0x20)
    BeginChrThread(0x8, 1, 0, 34)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x104,
        (
            "#00307F#2751V#12P#N#30W──Save the talk for later\x01",
            "and crush this big thing!\x02\x03",
            "#2752VLet's strike it hard with all we've got!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAC0)
    OP_57(0x0)
    OP_5A()

    def lambda_26F5():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_26F5)
    Sleep(50)

    def lambda_2705():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2705)
    Sleep(50)

    def lambda_2715():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2715)
    Sleep(50)

    def lambda_2725():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2725)
    Sleep(50)

    def lambda_2735():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2735)
    Sleep(50)

    def lambda_2745():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2745)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sound(2057, 255, 100, 0)

    ChrTalk(
        0x101,
        "#00007F#6P#N#30WUnderstood...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2099, 255, 100, 0)

    ChrTalk(
        0x102,
        "#00107F#6P#N#30WLeave it to me...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(4118, 255, 100, 0)

    ChrTalk(
        0x109,
        "#10107F#12P#N#30WI'll defeat the target!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0x1016)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_24(0x339)
    OP_24(0x3A3)
    OP_24(0x3B6)
    Battle("BattleInfo_34C", 0x0, 0x0, 0x0, 0x29, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 35)
    Return()

    # Function_2_607 end

    def Function_3_2831(): pass

    label("Function_3_2831")

    SetChrPos(0x101, -4050, 0, -2840, 135)
    SetChrPos(0x102, -6150, 0, -4770, 117)
    SetChrPos(0x109, -7180, 0, -6710, 104)
    SetChrPos(0x105, -5470, 0, -7830, 100)
    SetChrPos(0x104, -4500, 50, -13000, 60)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2A)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x0)
    Return()

    # Function_3_2831 end

    def Function_4_28AF(): pass

    label("Function_4_28AF")

    OP_93(0xFE, 0x13B, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x2D, 0x0)
    Return()

    # Function_4_28AF end

    def Function_5_28CB(): pass

    label("Function_5_28CB")

    OP_93(0xFE, 0x0, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x2D, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_5_28CB end

    def Function_6_28E7(): pass

    label("Function_6_28E7")

    OP_93(0xFE, 0x2D, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x13B, 0x0)
    Return()

    # Function_6_28E7 end

    def Function_7_2903(): pass

    label("Function_7_2903")

    OP_93(0xFE, 0x0, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x2D, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x13B, 0x0)
    Return()

    # Function_7_2903 end

    def Function_8_291F(): pass

    label("Function_8_291F")

    OP_9C(0xFE, 0xFFFFF448, 0xFFFFC950, 0xFFFFFE0C, 0x2EE, 0x5DC)
    Sleep(500)
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
    Sleep(850)
    Return()

    # Function_8_291F end

    def Function_9_29A6(): pass

    label("Function_9_29A6")

    Sound(893, 0, 100, 0)
    OP_71(0x0, 0x20D, 0x222, 0x1, 0x0)
    OP_9C(0xFE, 0xFFFFC568, 0x0, 0xFFFFF63C, 0xFA, 0x4B0)
    Return()

    # Function_9_29A6 end

    def Function_10_29D0(): pass

    label("Function_10_29D0")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1750, 3250, 1750, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x22C, 0x253, 0x1, 0x20)
    Sound(833, 0, 100, 0)
    OP_82(0x12C, 0x1F4, 0xBB8, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(1500)
    OP_9C(0xFE, 0xC8, 0x0, 0x0, 0x1F4, 0x5DC)
    Return()

    # Function_10_29D0 end

    def Function_11_2A53(): pass

    label("Function_11_2A53")


    def lambda_2A58():
        OP_93(0xFE, 0x127, 0x32)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A58)
    Sound(893, 0, 70, 0)
    OP_71(0x0, 0x263, 0x28E, 0x1, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_9D(0xFE, 0x1388, 0x0, 0xFFFFD6FC, 0x6D6, 0x5DC)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(893, 0, 50, 0)
    CancelBlur(1500)
    OP_82(0x64, 0xC8, 0xBB8, 0x2BC)
    Sound(833, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0xA, 0x2F, 0x0, 0x20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_2A53 end

    def Function_12_2B02(): pass

    label("Function_12_2B02")

    OP_79(0x0)
    OP_71(0x0, 0x8D, 0x95, 0x0, 0x20)
    Return()

    # Function_12_2B02 end

    def Function_13_2B12(): pass

    label("Function_13_2B12")

    OP_79(0x0)
    OP_71(0x0, 0xA, 0x2F, 0x0, 0x20)
    Return()

    # Function_13_2B12 end

    def Function_14_2B22(): pass

    label("Function_14_2B22")

    Sleep(650)

    label("loc_2B25")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B77")
    Sound(665, 0, 100, 0)
    Sound(627, 0, 90, 0)
    OP_87(0x1, 0xFF, 0x0, "Null_kuchi", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(800)
    Jump("loc_2B25")

    label("loc_2B77")

    Return()

    # Function_14_2B22 end

    def Function_15_2B78(): pass

    label("Function_15_2B78")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BCA")
    Sound(665, 0, 60, 0)
    Sound(627, 0, 50, 0)
    OP_87(0x2, 0xFF, 0x0, "Null_kuchi", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(800)
    Jump("Function_15_2B78")

    label("loc_2BCA")

    Return()

    # Function_15_2B78 end

    def Function_16_2BCB(): pass

    label("Function_16_2BCB")

    OP_87(0x0, 0x0, 0x0, "Bone_neck02", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)

    label("loc_2BFF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C23")
    OP_82(0x64, 0x64, 0x5DC, 0x1F4)
    Sleep(500)
    Jump("loc_2BFF")

    label("loc_2C23")

    Return()

    # Function_16_2BCB end

    def Function_17_2C24(): pass

    label("Function_17_2C24")

    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    Return()

    # Function_17_2C24 end

    def Function_18_2C91(): pass

    label("Function_18_2C91")

    OP_9B(0x0, 0xFE, 0xD2, 0x5DC, 0xFA0, 0x1)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFF448, 0x0, 0xFFFFF2A4, 0x1F4, 0x5DC)
    Sound(326, 0, 100, 0)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(650)
    Sleep(1000)

    def lambda_2CD5():

        label("loc_2CD5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2CD5")

    QueueWorkItem2(0xFE, 2, lambda_2CD5)
    Sleep(300)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_18_2C91 end

    def Function_19_2CEA(): pass

    label("Function_19_2CEA")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0xC3, 0x5DC, 0xFA0, 0x1)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFEC8C, 0x0, 0xFFFFEC50, 0x1F4, 0x5DC)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(350)
    Sleep(1000)

    def lambda_2D2B():

        label("loc_2D2B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2D2B")

    QueueWorkItem2(0xFE, 2, lambda_2D2B)
    Sleep(300)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_19_2CEA end

    def Function_20_2D40(): pass

    label("Function_20_2D40")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0xB4, 0x5DC, 0xFA0, 0x1)
    OP_9D(0xFE, 0xFFFFE89A, 0x0, 0xFFFFE534, 0x1F4, 0x5DC)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(200)
    Sleep(1000)

    def lambda_2D7B():

        label("loc_2D7B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2D7B")

    QueueWorkItem2(0xFE, 2, lambda_2D7B)
    Sleep(300)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_20_2D40 end

    def Function_21_2D90(): pass

    label("Function_21_2D90")

    OP_9B(0x0, 0xFE, 0xA5, 0x5DC, 0xFA0, 0x1)
    OP_9D(0xFE, 0xFFFFEF52, 0x0, 0xFFFFE11A, 0x1F4, 0x5DC)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(500)
    Sleep(1000)

    def lambda_2DC8():

        label("loc_2DC8")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2DC8")

    QueueWorkItem2(0xFE, 2, lambda_2DC8)
    Sleep(300)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_21_2D90 end

    def Function_22_2DDD(): pass

    label("Function_22_2DDD")

    TurnDirection(0xFE, 0x8, 500)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_2DDD end

    def Function_23_2DFC(): pass

    label("Function_23_2DFC")

    TurnDirection(0xFE, 0x8, 500)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_2DFC end

    def Function_24_2E1B(): pass

    label("Function_24_2E1B")

    TurnDirection(0xFE, 0x8, 500)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_2E1B end

    def Function_25_2E3A(): pass

    label("Function_25_2E3A")

    TurnDirection(0xFE, 0x8, 500)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_2E3A end

    def Function_26_2E59(): pass

    label("Function_26_2E59")

    SetChrSubChip(0xFE, 0x0)
    OP_A6(0xFE, 0x32, 0x0, 0x514, 0xBB8)

    label("loc_2E70")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E96")
    OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
    Sleep(100)
    Jump("loc_2E70")

    label("loc_2E96")

    Return()

    # Function_26_2E59 end

    def Function_27_2E97(): pass

    label("Function_27_2E97")

    SetChrSubChip(0xFE, 0x2)
    OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
    SetChrSubChip(0xFE, 0x3)
    OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)

    label("loc_2EC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EEB")
    OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
    Sleep(100)
    Jump("loc_2EC5")

    label("loc_2EEB")

    Return()

    # Function_27_2E97 end

    def Function_28_2EEC(): pass

    label("Function_28_2EEC")

    OP_9B(0x1, 0xFE, 0x0, 0xABE0, 0x2710, 0x1)
    EndChrThread(0xFE, 0x2)
    BeginChrThread(0xFE, 3, 0, 29)
    SetChrFlags(0xFE, 0x4)
    OP_9D(0xFE, 0xFFFFEDC2, 0xCC6, 0xFFFFE26E, 0xDAC, 0x5DC)
    Return()

    # Function_28_2EEC end

    def Function_29_2F22(): pass

    label("Function_29_2F22")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(844, 0, 100, 0)
    Sound(251, 0, 50, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    Sound(2297, 255, 100, 0)
    PlayEffect(0x8, 0x6, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x12C)
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 0, 500, 500, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    Sound(627, 0, 100, 0)
    Sound(246, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(250)
    CancelBlur(500)
    Sleep(500)
    StopEffect(0x6, 0x2)
    Return()

    # Function_29_2F22 end

    def Function_30_3020(): pass

    label("Function_30_3020")

    ClearChrFlags(0xFE, 0x4)

    def lambda_302A():
        OP_9D(0xFE, 0xFFFFEE6C, 0x32, 0xFFFFCD38, 0xFA, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_302A)
    Sleep(250)
    Sound(809, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(326, 0, 100, 0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_30_3020 end

    def Function_31_30A2(): pass

    label("Function_31_30A2")

    SetChrChipByIndex(0x9, 0x32)
    SetChrChip(0x0, 0x9, 0x32, 0x258)
    ClearChrFlags(0xFE, 0x1)
    Sound(844, 0, 100, 0)

    def lambda_30BE():
        OP_9C(0xFE, 0x0, 0xFFFFE0C0, 0xFA0, 0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30BE)
    WaitChrThread(0xFE, 1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0x9, 0x31)
    Sound(845, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0xF, 1, 0, 33)
    SetChrChipByIndex(0x9, 0x32)

    def lambda_3132():
        OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3132)
    Sleep(300)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xF, 0x1)
    SetChrChip(0x0, 0x9, 0x32, 0x2EE)
    Sound(844, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_319F():
        OP_9D(0xFE, 0x3E8, 0x0, 0xFFFF8EB8, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_319F)
    WaitChrThread(0xFE, 1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xF, 1, 0, 33)

    def lambda_31FD():
        OP_9B(0x0, 0xFE, 0x134, 0x34BC, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31FD)
    Sleep(600)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    Sleep(900)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xF, 0x1)
    SetChrChipByIndex(0x9, 0x31)
    Return()

    # Function_31_30A2 end

    def Function_32_3228(): pass

    label("Function_32_3228")

    Sleep(1200)
    Sound(893, 0, 60, 0)
    Sleep(1200)
    Sound(893, 0, 60, 0)
    Sleep(1200)
    Sound(893, 0, 60, 0)
    Return()

    # Function_32_3228 end

    def Function_33_3244(): pass

    label("Function_33_3244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_325D")
    Sound(845, 0, 100, 0)
    Sleep(400)
    Jump("Function_33_3244")

    label("loc_325D")

    Return()

    # Function_33_3244 end

    def Function_34_325E(): pass

    label("Function_34_325E")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x127, 0x132, 0x64, 0x0)
    OP_79(0x0)
    Sound(914, 0, 100, 0)
    OP_71(0x0, 0x133, 0x142, 0x1, 0x0)

    def lambda_3288():
        OP_93(0xFE, 0x111, 0x46)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3288)
    OP_9D(0xFE, 0x16F8, 0x0, 0xFFFFD5D0, 0x9C4, 0x5DC)
    OP_82(0xC8, 0x12C, 0xBB8, 0x3E8)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(2500)
    Sound(833, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    OP_79(0x0)
    OP_71(0x0, 0x143, 0x14E, 0x1, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2F, 0x0, 0x20)
    Return()

    # Function_34_325E end

    def Function_35_3330(): pass

    label("Function_35_3330")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch03050.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02702.itc", 0x23)
    LoadChrToIndex("chr/ch26200.itc", 0x24)
    LoadChrToIndex("chr/ch26300.itc", 0x25)
    LoadChrToIndex("chr/ch30700.itc", 0x26)
    LoadChrToIndex("chr/ch02750.itc", 0x27)
    LoadEffect(0x1, "battle\\bs000001.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 6190, 200, -2810, 117)
    SetChrPos(0x102, 5160, 200, -4350, 90)
    SetChrPos(0x109, 5730, 0, -6260, 61)
    SetChrPos(0x105, 7720, 0, -6830, 31)
    SetChrPos(0x104, 7240, 200, -4830, 71)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 7450, 100, -8590, 31)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0x8, 14230, 0, -4380, 0)
    OP_93(0x8, 0xFF, 0x0)
    OP_71(0x0, 0x5A, 0x6D, 0x1, 0x20)
    SetChrFlags(0x8, 0x1)
    ClearChrFlags(0x8, 0x4)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(8350, 6800, -4680, 0)
    MoveCamera(69, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34000, 0)
    OP_68(8350, 7200, -4380, 3000)
    MoveCamera(69, 24, 0, 3000)
    SetCameraDistance(30000, 3000)
    Sound(842, 0, 100, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    PlayEffect(0x1, 0x0, 0x8, 0x1, 0, -750, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(667, 0, 80, 0)
    Sound(843, 0, 100, 0)
    OP_6F(0x79)
    OP_75(0x0, 0x1, 0x5DC)

    def lambda_35AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_35AD)
    OP_68(8350, 2300, -4680, 2500)
    MoveCamera(67, 15, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(17320, 2500)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Sleep(500)
    OP_68(8540, 600, -5200, 2000)
    MoveCamera(70, 18, 0, 2000)
    OP_6E(700, 2000)
    SetCameraDistance(15120, 2000)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005F#6PI-It vanished...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#6P...What was that...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    BeginChrThread(0x9, 1, 0, 36)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    def lambda_3694():
        OP_93(0xFE, 0x104, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3694)
    Sleep(300)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_36AC():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_36AC)
    Sleep(100)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)

    def lambda_36C4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_36C4)
    Sleep(100)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_36DC():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36DC)
    Sleep(100)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    def lambda_36F4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_36F4)
    Sleep(100)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)

    def lambda_370C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_370C)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x105, 2)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x104,
        (
            "*phew*, it looks like it wasn't\x01",
            "your run of the mill monster, huh?\x02\x03",
            "Well, I'm glad we \x01",
            "beated it somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x109,
        (
            "#10109F#12PAhaha...\x01",
            "Typical of senior Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12POh boy.\x01",
            "What an impressive fighting power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha...\x01",
            "You really saved us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PBut, why did you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#5PWell, after I completed the rehabilitation\x01",
            "training I was finally dismissed and so I\x01",
            "went back to the SSS in the afternoon.\x02\x03",
            "#00300FThen, I heard you had\x01",
            "headed to Mainz.\x02\x03",
            "When I had finally caught up with you, \x01",
            "you had just gotten in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F#6PThen, even the cave-in\x01",
            "at the entrance has...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#5PYeah, the Mainz miners all\x01",
            "together have removed it.\x02\x03",
            "#00300FSo, I headed out first and when\x01",
            "I was tryin' to locate you...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xD7, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00302F#5PThis guy appeared unexpectedly\x01",
            "and brought me here, you see.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_3B06():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3B06)
    Sleep(100)

    def lambda_3B16():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B16)
    Sleep(100)

    def lambda_3B26():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3B26)
    Sleep(100)

    def lambda_3B36():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B36)
    Sleep(100)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    Sleep(200)
    Sound(3054, 255, 100, 0)

    ChrTalk(
        0x9,
        "#01200F#11PWoof.\x02",
    )

    EndChrThread(0x9, 0x1)
    OP_A6(0x9, 0x0, 0x32, 0xC8, 0xBB8)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    BeginChrThread(0x9, 1, 0, 36)
    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#5PHa ha, I see...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x105, 0x9, 500)

    ChrTalk(
        0x105,
        (
            "#10302F#5POh boy.\x01",
            "Amazing as always, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00104F#5PZeit, thank you.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x109, 0x9, 500)

    ChrTalk(
        0x109,
        (
            "#10109F#6PYes, I'll have to buy him\x01",
            "some meat as thanks...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10000, 2000, -13900, 0)
    OP_A7(0xA, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    NpcTalk(
        0xA,
        "Man's Voice",
        "#1P#2SHeeey, are you okay!?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    Sleep(200)

    def lambda_3D21():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3D21)
    WaitChrThread(0x9, 2)
    Sleep(200)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    Sleep(800)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xA, 1000, 0, -39500, 0)
    SetChrPos(0xD, 300, 0, -41500, 0)
    SetChrPos(0xC, 1700, 0, -42000, 0)
    SetChrPos(0xB, 300, 0, -43750, 0)
    SetChrPos(0xE, 1700, 0, -44500, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_68(1720, 600, -34090, 0)
    MoveCamera(74, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22320, 0)
    OP_68(1280, 1700, -30590, 3000)
    MoveCamera(30, 14, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(20270, 3500)
    Fade(500)

    def lambda_3E15():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3E15)
    Sleep(50)

    def lambda_3E2D():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3E2D)
    Sleep(50)

    def lambda_3E45():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3E45)
    Sleep(50)

    def lambda_3E5D():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3E5D)
    Sleep(50)

    def lambda_3E75():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3E75)
    Sleep(50)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xE, 0x1)
    SetChrPos(0xA, 5000, 0, -15500, 0)
    SetChrPos(0xD, 4300, 0, -17500, 0)
    SetChrPos(0xC, 5700, 0, -18000, 0)
    SetChrPos(0xB, 4300, 0, -19750, 0)
    SetChrPos(0xE, 5700, 0, -20500, 0)
    OP_68(10510, -600, -5950, 0)
    MoveCamera(61, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20410, 0)
    Fade(500)
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x109, 3, 0, 39)
    BeginChrThread(0x105, 3, 0, 40)
    BeginChrThread(0x104, 3, 0, 41)
    BeginChrThread(0x9, 3, 0, 42)

    def lambda_3F53():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F53)
    Sleep(50)

    def lambda_3F6B():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F6B)
    Sleep(50)

    def lambda_3F83():
        OP_9B(0x0, 0xFE, 0x0, 0x1E46, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3F83)
    Sleep(50)

    def lambda_3F9B():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3F9B)
    Sleep(50)

    def lambda_3FB3():
        OP_9B(0x0, 0xFE, 0x0, 0x203A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3FB3)
    Sleep(50)
    OP_0D()

    ChrTalk(
        0x101,
        "#00002F#5PMr. Gantz, and everyone too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PHeya, thanks for earlier.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)

    ChrTalk(
        0xA,
        (
            "#12PGood...\x01",
            "You all look in one piece.\x02",
        )
    )

    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x9, 0x2)
    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304F#5PHu hu, thank goodness we do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#5PThank you very much for\x01",
            "running here in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PNot at all, after all we were the\x01",
            "ones to ask you to do this job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PAt any rate, who could've thought the\x01",
            "old mine would've turned like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThese are tunnels that our\x01",
            "great grandfathers dug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PI hadn't heard they\x01",
            "were like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PA-And first of all, why did the\x01",
            "entrance suddenly caved-in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...Let's go back to\x01",
            "town for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PWe'll explain everything that happened \x01",
            "with our report to the Town Mayor.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_3330 end

    def Function_36_4300(): pass

    label("Function_36_4300")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_431E")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_36_4300")

    label("loc_431E")

    Return()

    # Function_36_4300 end

    def Function_37_431F(): pass

    label("Function_37_431F")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(3500)
    OP_9B(0x0, 0xFE, 0x7, 0xABE, 0x3E8, 0x0)

    def lambda_433D():

        label("loc_433D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_433D")

    QueueWorkItem2(0x101, 2, lambda_433D)
    Return()

    # Function_37_431F end

    def Function_38_434B(): pass

    label("Function_38_434B")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(3000)
    OP_9B(0x0, 0xFE, 0x2D, 0x2EE, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x546, 0x3E8, 0x0)

    def lambda_4378():

        label("loc_4378")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_4378")

    QueueWorkItem2(0x102, 2, lambda_4378)
    Return()

    # Function_38_434B end

    def Function_39_4386(): pass

    label("Function_39_4386")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(5600)
    OP_9B(0x1, 0xFE, 0x10E, 0x320, 0x3E8, 0x0)

    def lambda_43A4():

        label("loc_43A4")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_43A4")

    QueueWorkItem2(0x109, 2, lambda_43A4)
    Return()

    # Function_39_4386 end

    def Function_40_43B2(): pass

    label("Function_40_43B2")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_43C8():

        label("loc_43C8")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_43C8")

    QueueWorkItem2(0x105, 2, lambda_43C8)
    Return()

    # Function_40_43B2 end

    def Function_41_43D6(): pass

    label("Function_41_43D6")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(4000)
    OP_9B(0x1, 0xFE, 0x14A, 0x15E, 0x3E8, 0x0)

    def lambda_43F4():

        label("loc_43F4")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_43F4")

    QueueWorkItem2(0x104, 2, lambda_43F4)
    Return()

    # Function_41_43D6 end

    def Function_42_4402(): pass

    label("Function_42_4402")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(2800)
    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_4418():

        label("loc_4418")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_4418")

    QueueWorkItem2(0x9, 2, lambda_4418)
    Return()

    # Function_42_4402 end

    def Function_43_4426(): pass

    label("Function_43_4426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 5)), scpexpr(EXPR_END)), "loc_4430")
    Return()

    label("loc_4430")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A large monster is wandering about.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Exterminate]\x01",      # 0
            "[Quit]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_450C"),
        (SWITCH_DEFAULT, "loc_4525"),
    )


    label("loc_450C")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -830, 0, -2300, 181)
    EventEnd(0x5)
    Return()

    label("loc_4525")

    Battle("BattleInfo_390", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-830, 1000, -2300, 0)
    OP_90(0x0, -830, 0, -2300, 181)
    OP_90(0x1, -830, 0, -2300, 181)
    OP_90(0x2, -830, 0, -2300, 181)
    OP_90(0x3, -830, 0, -2300, 181)
    OP_90(0x4, -830, 0, -2300, 181)
    OP_90(0x5, -830, 0, -2300, 181)
    OP_90(0x6, -830, 0, -2300, 181)
    OP_90(0x7, -830, 0, -2300, 181)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_45E7"),
        (1, "loc_45EC"),
        (SWITCH_DEFAULT, "loc_45EF"),
    )


    label("loc_45E7")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_45EC")

    OP_B9(0x0)
    Return()

    label("loc_45EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10, 1500, 2730, 0)
    MoveCamera(43, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18570, 0)
    SetChrFlags(0x10, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wanted Monster exterminated!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xF, 1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 5500, 180)
    SetChrPos(0x103, -2000, 0, 3500, 90)
    SetChrPos(0x104, -2000, 0, 1500, 90)
    SetChrPos(0x109, 2000, 0, 3500, 270)
    SetChrPos(0x105, 2000, 0, 1500, 270)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x102,
        (
            "#00104F*giggle*, we got a Craft Book.\x02\x03",
            "#00100FCould this one be geared\x01",
            "to Tio and Miss Noｱl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FMiss Noｱl, do you mind\x01",
            "testing it immediately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FI don't. Let's give it a try!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0x190)
    AddCraft(0x8, 0x190)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio and Noｱl have learned the\x01\x07\x02",
            ""Blast Hammer"\x07\x05",
            " Combi Craft.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By each expending 100 CP, a powerful\x01",
            "combination attack can be unleashed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 5)
    OP_29(0x83, 0x4, 0x10)
    OP_29(0x83, 0x4, 0x2)
    OP_29(0x83, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_43_4426 end

    SaveToFile()

Try(main)
