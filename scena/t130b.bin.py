from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t130b.bin",                # FileName
        "t130b",                    # MapName
        "t130b",                    # Location
        0x00B6,                     # MapIndex
        "ed7564",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 182, 0, 0, 0, 1],
    )

    BuildStringList((
        "t130b",                  # 0
        "Campanella The Fool",    # 1
        "イベント用モンスター",   # 2
        "イベント用モンスター",   # 3
        "bt130b",                 # 4
        "To Mirror Castle",       # 5
        "To Ferris Wheel",        # 6
        "To Haunted Coaster",     # 7
        "To Hotel Delphinia",     # 8
    ))

    ATBonus("ATBonus_208", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2E8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_308", 0x0052, 3, 6, 45, 3, 3, 30, 0, "bt130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84400.dat", "ms85900.dat", 0, 0, 0, 0, "ms86600.dat", 0, "MonsterBattlePostion_2E8", "MonsterBattlePostion_2C8", "ed7590", "ed7453", "ATBonus_208"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 2,   0.0,                   -15.0,                 -1.0,                  625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  3.0,                   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  0.0,                   -18.5,                 -1.0,                  25.0,                  [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  1.0,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  18.5,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, 30.0, 0x0000, 0x0000, "To Mirror Castle")
    PlaceName(-40.0, 0.0, 10.0, 0x0000, 0x0000, "To Ferris Wheel")
    PlaceName(60.0, 0.0, 10.0, 0x0000, 0x0000, "To Haunted Coaster")
    PlaceName(0.0, 0.0, -80.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ChipFrameInfo(892, 0)                                        # 0

    ScpFunction((
        "Function_0_37C",          # 00, 0
        "Function_1_38C",          # 01, 1
        "Function_2_4C5",          # 02, 2
        "Function_3_AD3",          # 03, 3
        "Function_4_AF2",          # 04, 4
        "Function_5_B32",          # 05, 5
        "Function_6_B6C",          # 06, 6
        "Function_7_BA2",          # 07, 7
        "Function_8_CBD",          # 08, 8
        "Function_9_2DD6",         # 09, 9
        "Function_10_2E3B",        # 0A, 10
        "Function_11_2EA0",        # 0B, 11
    ))


    def Function_0_37C(): pass

    label("Function_0_37C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_38B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)

    label("loc_38B")

    Return()

    # Function_0_37C end

    def Function_1_38C(): pass

    label("Function_1_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3A1")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B9")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_3B9")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E1")
    ModifyEventFlags(1, 1, 0x80)
    OP_10(0x2, 0x1)
    OP_10(0x3, 0x1)
    OP_1B(0x2, 0x0, 0x9)
    OP_1B(0x3, 0x0, 0xA)

    label("loc_3E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_447")
    SetMapObjFrame(0xFF, "face00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "obj11", 0x0, 0x1)
    SetMapObjFrame(0x9, "face00", 0x0, 0x1)
    SetMapObjFrame(0xA, "face00", 0x0, 0x1)
    SetMapObjFrame(0xB, "face00", 0x0, 0x1)
    SetMapObjFrame(0xC, "face00", 0x0, 0x1)
    Jump("loc_49B")

    label("loc_447")

    SetMapObjFrame(0xFF, "face01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "fool11", 0x0, 0x1)
    SetMapObjFrame(0x9, "face01", 0x0, 0x1)
    SetMapObjFrame(0xA, "face01", 0x0, 0x1)
    SetMapObjFrame(0xB, "face01", 0x0, 0x1)
    SetMapObjFrame(0xC, "face01", 0x0, 0x1)

    label("loc_49B")

    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x50, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)
    Return()

    # Function_1_38C end

    def Function_2_4C5(): pass

    label("Function_2_4C5")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("monster/ch84450.itc", 0x1E)
    LoadChrToIndex("monster/ch84452.itc", 0x1F)
    LoadChrToIndex("monster/ch85950.itc", 0x20)
    LoadChrToIndex("monster/ch85952.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch03050.itc", 0x27)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, -10000, 0)
    SetChrPos(0x102, -650, 0, -11100, 0)
    SetChrPos(0x103, 750, 0, -10800, 0)
    SetChrPos(0x104, 150, 0, -12000, 0)
    SetChrPos(0x109, -1100, 0, -12300, 0)
    SetChrPos(0x105, 1200, 0, -12500, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -2500, 1500, -7300, 135)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x20)
    BeginChrThread(0x9, 0, 0, 3)
    SetChrChip(0x0, 0x9, 0x64, 0x1F4)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2500, 1500, -7300, 225)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x20)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrChip(0x0, 0xA, 0x64, 0x1F4)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, 0, 0)
    MoveCamera(30, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    FadeToBright(1000, 0)
    MoveCamera(0, 20, 0, 8000)
    SetCameraDistance(18000, 8000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 1000, -8000, 0)
    OP_68(0, 1000, -10000, 3000)
    MoveCamera(0, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#10302F#12POh boy...\x01",
            "What nice taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6PI can only let out a sigh seein'\x01",
            "as it's so much elaborated...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PE-Even so...\x01",
            "It's an eerie character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P...I will never allow\x01",
            "such a thing to be...\x02\x03",
            "#00201FA replacement for Michey...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#6PT-Tio.\x01",
            "Calm down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PBy the way...\x01",
            "Where did KeA go──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#00207F#12PSomething's coming from left and right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PWhat...!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7590", 0)
    OP_68(0, 1400, -8500, 3000)
    MoveCamera(0, 10, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15500, 3000)
    OP_6F(0x79)
    Sound(212, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Sound(817, 0, 70, 0)
    BlurSwitch(0x1F4, 0x77FFFFFF, 0x4, 0x1, 0xF)
    SetCameraDistance(15000, 3000)
    BeginChrThread(0x9, 3, 0, 4)
    BeginChrThread(0xA, 3, 0, 4)
    Sleep(500)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    MoveCamera(0, 7, 0, 20000)
    SetCameraDistance(15000, 20000)
    Sound(2182, 255, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x102,
        "#00115F#6P#4S#13AEeeeeek...!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        "#10111F#6P#NT-Those are...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#6P#NAren't they too serious to be\x01",
            "Horror Coaster's monsters...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00007F#6PKh...\x01",
            "In any case, let's beat them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10307F#12P#N──Here they come!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 800)
    Sleep(700)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Battle("BattleInfo_308", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 8)
    Return()

    # Function_2_4C5 end

    def Function_3_AD3(): pass

    label("Function_3_AD3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF1")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_3_AD3")

    label("loc_AF1")

    Return()

    # Function_3_AD3 end

    def Function_4_AF2(): pass

    label("Function_4_AF2")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_B02():
        OP_98(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B02)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_AF2 end

    def Function_5_B32(): pass

    label("Function_5_B32")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)

    def lambda_B4C():
        OP_9B(0x0, 0xFE, 0xFFEC, 0xBB8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4C)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_5_B32 end

    def Function_6_B6C(): pass

    label("Function_6_B6C")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Sleep(500)

    def lambda_B82():
        OP_9B(0x0, 0xFE, 0x14, 0xBB8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B82)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_B6C end

    def Function_7_BA2(): pass

    label("Function_7_BA2")


    def lambda_BA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA7)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0xA28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0xFE, 2)
    Return()

    # Function_7_BA2 end

    def Function_8_CBD(): pass

    label("Function_8_CBD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("monster/ch84450.itc", 0x1E)
    LoadChrToIndex("monster/ch85950.itc", 0x20)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00150.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch03050.itc", 0x27)
    LoadChrToIndex("apl/ch51326.itc", 0x28)
    LoadChrToIndex("apl/ch51416.itc", 0x29)
    SoundLoad(3716)
    SoundLoad(3717)
    SoundLoad(3718)
    SoundLoad(959)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04800.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis234.itp")
    LoadEffect(0x0, "event\\ev10002.eff")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, -10000, 0)
    SetChrPos(0x102, -650, 0, -11100, 0)
    SetChrPos(0x103, 750, 0, -10800, 0)
    SetChrPos(0x104, 150, 0, -12000, 0)
    SetChrPos(0x109, -1100, 0, -12300, 0)
    SetChrPos(0x105, 1200, 0, -12500, 0)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -2500, 0, -7300, 135)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 3)
    SetChrChip(0x0, 0x9, 0x64, 0x1F4)
    SetChrFlags(0x9, 0x20)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 2500, 0, -7300, 225)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 3)
    SetChrChip(0x0, 0xA, 0x64, 0x1F4)
    SetChrFlags(0xA, 0x20)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -14350, 5950, 1450, 135)
    SetChrFlags(0x8, 0x8)
    BlurSwitch(0x0, 0x77FFFFFF, 0x4, 0x1, 0xF)
    OP_68(0, 1400, -8500, 30)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15500, 3000)
    Sleep(2000)
    Sound(212, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Sound(817, 0, 70, 0)
    SetCameraDistance(16000, 1000)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    BeginChrThread(0x9, 0, 0, 7)
    BeginChrThread(0xA, 0, 0, 7)
    Sleep(500)
    CancelBlur(1500)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    OP_6F(0x79)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Sleep(300)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x102,
        "#00106F#6P#30W*pant pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6PTch, what the heck...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PBut...it was effective.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#6PKh...\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1400, -8200, 1000)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x4B0, 0x0)
    Sound(33, 0, 100, 0)
    Sound(48, 0, 50, 0)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#4S#5P──How long do you\x01",
            "intend to hide!?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#4S#5PCome out already!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10105F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10301F#12PEeeh...?\x02",
    )

    CloseMessageWindow()
    Sound(1008, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x8,
        "Boy's Voice",
        "#3716V#30A#40WUhuhu── You did well in figuring it out.\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    PlayBGM("ed7584", 0)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x6)
    ClearChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x0, 0x20F58, 0x0, 0x0)
    OP_68(-14350, 6950, 1450, 3000)
    MoveCamera(330, -13, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13250, 3000)

    def lambda_1287():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1287)
    Sleep(50)

    def lambda_1297():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1297)
    Sleep(50)

    def lambda_12A7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12A7)
    Sleep(50)

    def lambda_12B7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12B7)
    Sleep(50)

    def lambda_12C7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_12C7)
    Sleep(50)

    def lambda_12D7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_12D7)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x109,
        "#10111F#12P#NWha...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00105F#12P#NA b-boy...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00201F#12P#NI didn't feel his presence...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00311F#12P#NWho the heck are you?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1439")

    NpcTalk(
        0x8,
        "Boy ",
        (
            "#04804F#5PUhuhu, how cold of you.\x02\x03",
            "We passed each other once\x01",
            "so we're no strangers, and yet...\x02\x03",
            "#04802F──Right, ladies and gentlemen of the SSS?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_14EA")

    label("loc_1439")


    NpcTalk(
        0x8,
        "Boy",
        (
            "#04804F#5PUhuhu, how cold of you.\x02\x03",
            "It's our first meeting, strictly speaking,\x01",
            "but we're no strangers, and yet...\x02\x03",
            "#04802F──Right, ladies and gentlemen of the SSS?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_14EA")

    Fade(500)
    OP_68(0, 1000, -9500, 0)
    MoveCamera(130, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15400, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00101F#11PCould it be that you're...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PThe hacker who tried to catch Lloyd and\x01",
            "the others in a trap at Jona's place...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1737")

    ChrTalk(
        0x101,
        (
            "#00003F#5P...And also who passed the tower\x01",
            "information to the terrorists, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00013F#5PWe actually meet since passing each other\x01",
            "in front of the Doll Studio, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_178D")

    label("loc_1737")


    ChrTalk(
        0x101,
        (
            "#00003F#5P...And also who passed the tower\x01",
            "information to the terrorists, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_178D")

    Fade(500)
    OP_68(-14350, 6950, 1450, 0)
    MoveCamera(330, -13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13250, 0)
    OP_0D()

    NpcTalk(
        0x8,
        "Boy",
        "#04809F#5PUhuhu, correct.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetChrName("Boy")

    AnonymousTalk(
        0xFF,
        (
            "#30W"Ouroboros" Enforcer No. 0──\x01",
            "Campanella "The Fool".\x02\x03",
            "#3718VA pleasure to meet you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE86)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(0, 1000, -9500, 0)
    MoveCamera(130, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15400, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00010F#5P......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PThe mysterious secret society\x01",
            "that threw Liberl into turmoil...!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1ABB")
    OP_29(0xA5, 0x1, 0xB)

    ChrTalk(
        0x104,
        (
            "#00311F#11P#NI thought he was related since we\x01",
            "met him in front of that studio, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10306F#11P#NTo think he was cooperating\x01",
            "with the likes of terrorists...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1B2A")

    label("loc_1ABB")

    OP_29(0xA5, 0x1, 0xC)

    ChrTalk(
        0x104,
        (
            "#00311F#11P#NI thought it was suspicious\x01",
            "that the terrorists were\x01",
            "using mechanized dolls, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1B2A")

    Fade(500)
    OP_68(-8730, 4700, -4270, 0)
    MoveCamera(127, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24200, 0)
    SetCameraDistance(26200, 1500)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x4E20, 0x0, 0x0, 0x0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#04804F#6P#NUhuhu, they were really unlucky.\x02\x03",
            "#04802FThe "Heiyue" and the "Red Constellation"...\x01",
            "Some dangerous guys appeared, eh?\x02\x03",
            "#04806FEspecially the people of the Empire,\x01",
            "poor, poor them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10107F#11PD-Don't joke around!\x02\x03",
            "They were comrades you\x01",
            "were cooperating with, right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04809F#6P#NAhaha, they were just \x01",
            "pawns I used until the end.\x02\x03",
            "#04802FI just helped them a little\x01",
            "because it seemed they would\x01",
            "have acted in a pretty interesting way.\x02\x03",
            "#04804FI had zero interest in their\x01",
            "opinions and ideology.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10110F#11PKh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11P#NHmph, you have quite\x01",
            "the nice personality, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00211F#5P...I think it matches nicely\x01",
            "with Mr. Wazy's.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, -9500, 0)
    MoveCamera(130, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15400, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#5P──Enough with the jokes.\x02\x03",
            "#00001FWhat're you trying\x01",
            "to do in Crossbell...?\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    Fade(500)
    SetCameraDistance(15000, 500)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sound(805, 0, 100, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#4S#5PMore importantly──\x01",
            "Where did you take KeA too!?\x02\x03",
            "#4SI'll have you tell us by force!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x23)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(500)
    Fade(500)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x6)
    ClearChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x0, 0x20F58, 0x0, 0x0)
    OP_68(-14350, 6950, 1450, 0)
    MoveCamera(330, -13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13250, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#04804F#5PUhuhu, nice vigor you have there.\x02\x03",
            "#04800FHowever, I didn't do anything\x01",
            "to your little princess, you know?\x02\x03",
            "I just happened to see her passing\x01",
            "by here dizzily some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12P#NHuh...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#12P#NBastard...\x01",
            "Are you playin' dumb!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#04804F#5PHu hu, but it's true.\x02\x03",
            "#04802FIt's up to you believing\x01",
            "me or not, though...\x02\x03",
            "Today, I just came\x01",
            "to greet you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(12750, 500)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x6)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Sound(325, 0, 100, 0)
    SetChrSubChip(0x8, 0xE)
    Sleep(300)
    Fade(500)
    OP_68(0, 800, -20000, 0)
    OP_68(0, 2600, -20000, 6000)
    MoveCamera(0, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(41550, 0)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x4E20, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(1000)
    Sound(212, 0, 100, 0)
    Sound(223, 0, 100, 0)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x4, 0x1, 0xF)
    Sleep(1000)
    CancelBlur(1000)
    Fade(100)
    SetMapObjFrame(0xFF, "obj11", 0x1, 0x1)
    SetMapObjFrame(0xFF, "fool11", 0x0, 0x1)
    SetMapObjFrame(0x9, "face00", 0x1, 0x1)
    SetMapObjFrame(0xA, "face00", 0x1, 0x1)
    SetMapObjFrame(0xB, "face00", 0x1, 0x1)
    SetMapObjFrame(0xC, "face00", 0x1, 0x1)
    SetMapObjFrame(0x9, "face01", 0x0, 0x1)
    SetMapObjFrame(0xA, "face01", 0x0, 0x1)
    SetMapObjFrame(0xB, "face01", 0x0, 0x1)
    SetMapObjFrame(0xC, "face01", 0x0, 0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#5PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6PT-This is...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, 0, 0)
    MoveCamera(30, 35, 0, 0)
    MoveCamera(0, 20, 0, 6000)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(18000, 6000)
    OP_0D()
    Sleep(1500)
    Sound(212, 0, 100, 0)
    Sound(223, 0, 100, 0)
    BlurSwitch(0x7D0, 0xFFFFFFFF, 0x4, 0x1, 0xF)
    Sleep(700)
    Sound(829, 0, 100, 0)
    Sleep(1300)
    CancelBlur(1500)
    Fade(250)
    SetMapObjFrame(0xFF, "face01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "face00", 0x1, 0x1)
    OP_0D()
    OP_6F(0x79)
    OP_68(0, 1000, -9500, 2000)
    MoveCamera(0, 20, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(18000, 2000)
    Sleep(500)

    def lambda_249D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_249D)
    Sleep(50)

    def lambda_24AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_24AD)
    Sleep(50)

    def lambda_24BD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24BD)
    Sleep(50)

    def lambda_24CD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_24CD)
    Sleep(50)

    def lambda_24DD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24DD)
    Sleep(50)

    def lambda_24ED():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_24ED)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00101F#6PAh──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PIt went back to normal...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12P...A very large-scale\x01",
            "trick, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#12PCould it be a kind of magic...?\x02",
    )

    CloseMessageWindow()
    Sound(325, 0, 80, 0)
    Sleep(300)
    Sound(959, 2, 60, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-14350, 6950, 1450, 2000)
    MoveCamera(330, -13, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(13250, 2000)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x6)
    ClearChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x0, 0x20F58, 0x0, 0x0)
    SetChrPos(0x8, -14350, 5950, 1450, 145)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, -700, -1000, 0, 0, 0, 800, 1000, 800, 0xFF, 0, 0, 0, 0)

    def lambda_2700():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2700)
    Sleep(50)

    def lambda_2710():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2710)
    Sleep(50)

    def lambda_2720():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2720)
    Sleep(50)

    def lambda_2730():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2730)
    Sleep(50)

    def lambda_2740():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2740)
    Sleep(50)

    def lambda_2750():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2750)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#04809F#5PUhuhu, then, I believe\x01",
            "I will excuse myself now.\x02\x03",
            "#04802FI pray we will meet\x01",
            "again before long.\x02\x03",
            "#04805F──Ah, your little princess should have\x01",
            "headed towards the castle further in.\x02\x03",
            "#04804FGo protect her at once, alright?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-14350, 6950, 1450, 0)
    MoveCamera(0, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    MoveCamera(315, 5, 0, 3000)
    SetCameraDistance(10000, 3000)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x100)
    OP_D5(0x8, 0x4E20, 0x0, 0x0, 0x0)
    SetChrPos(0x8, -14350, 5900, 1450, 135)
    ClearChrFlags(0x8, 0x1)
    StopEffect(0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_25(0x3BF, 0x46)
    Sound(3703, 255, 100, 0)
    OP_6F(0x79)
    OP_0D()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(10750, 500)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_6F(0x79)
    CancelBlur(1000)
    StopEffect(0x0, 0x2)
    StopSound(959, 1000, 60)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    StopBGM(0x1770)
    Fade(500)
    OP_68(0, 1000, -9500, 0)
    MoveCamera(130, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15400, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x101,
        "#00006F#40W#5P...That's...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        "#00010F#5P#4SThat's "Ouroboros"...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PWe heard about them from \x01",
            "Miss Estelle and Renne...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5P...Not only their hacking skills,\x01",
            "it also seems a peculiar group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11PHey hey, such guys too\x01",
            "came to Crossbell!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PN-No way...\x01",
            "Why it's always Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11P#NIt seems they have many ulterior motives.\x02\x03",
            "#10303F──Well, that aside...\x02\x03",
            "#10301FShouldn't protecting KeA\x01",
            "coming first now?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
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
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00011F#5PYou're right...! He said she's\x01",
            "at the castle further inside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00107F#11PLet's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    PlayBGM("ed7564", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x234), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x20)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    SetChrPos(0x0, 0, 0, -10000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x146, 2)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    OP_10(0x2, 0x1)
    OP_10(0x3, 0x1)
    OP_1B(0x2, 0x0, 0x9)
    OP_1B(0x3, 0x0, 0xA)
    EventEnd(0x5)
    Return()

    # Function_8_CBD end

    def Function_9_2DD6(): pass

    label("Function_9_2DD6")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F...KeA is in the castle further ahead.\x01",
            "Hurry, let's go after her!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -10940, 0, 3960, 135)
    EventEnd(0x4)
    Return()

    # Function_9_2DD6 end

    def Function_10_2E3B(): pass

    label("Function_10_2E3B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F...KeA is in the castle further ahead.\x01",
            "Hurry, let's go after her!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 10740, 0, 4720, 225)
    EventEnd(0x4)
    Return()

    # Function_10_2E3B end

    def Function_11_2EA0(): pass

    label("Function_11_2EA0")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F...KeA is in the castle further ahead.\x01",
            "Hurry, let's go after her!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, -14500, 0)
    EventEnd(0x4)
    Return()

    # Function_11_2EA0 end

    SaveToFile()

Try(main)
