﻿from ScenarioHelper import *

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
        "Function_3_AD7",          # 03, 3
        "Function_4_AF6",          # 04, 4
        "Function_5_B36",          # 05, 5
        "Function_6_B70",          # 06, 6
        "Function_7_BA6",          # 07, 7
        "Function_8_CC1",          # 08, 8
        "Function_9_2DE8",         # 09, 9
        "Function_10_2E3F",        # 0A, 10
        "Function_11_2E96",        # 0B, 11
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
            "#10302F#12POh man... What good\x01",
            "taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#6PIt bein' this elaborate,\x01",
            "I can only let out a\x01",
            "sigh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PE-Even so... It's an\x01",
            "ominous character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P...I will never allow\x01",
            "something like this to\x01",
            "be...\x02\x03",
            "#00201FA replacement for\x01",
            "Mishy...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#6PT-Tio. Calm down...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PBy the way... Where in\x01",
            "the world did KeA─\x02",
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
        (
            "#00207F#12PFrom the left and\x01",
            "right... Something's\x01",
            "coming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PWhat...!?\x02",
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
            "#00310F#6P#NAren't they too serious\x01",
            "to be Horror Coaster\x01",
            "monsters!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00007F#6PGuh... Anyway, let's\x01",
            "beat them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10307F#12P#N─Here they come!\x02",
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

    def Function_3_AD7(): pass

    label("Function_3_AD7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AF5")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_3_AD7")

    label("loc_AF5")

    Return()

    # Function_3_AD7 end

    def Function_4_AF6(): pass

    label("Function_4_AF6")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_B06():
        OP_98(0xFE, 0x0, 0xFFFFFA24, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B06)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_AF6 end

    def Function_5_B36(): pass

    label("Function_5_B36")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)

    def lambda_B50():
        OP_9B(0x0, 0xFE, 0xFFEC, 0xBB8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_5_B36 end

    def Function_6_B70(): pass

    label("Function_6_B70")

    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Sleep(500)

    def lambda_B86():
        OP_9B(0x0, 0xFE, 0x14, 0xBB8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B86)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_B70 end

    def Function_7_BA6(): pass

    label("Function_7_BA6")


    def lambda_BAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BAB)
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

    # Function_7_BA6 end

    def Function_8_CC1(): pass

    label("Function_8_CC1")

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
        "#00106F#6P#30W*pant, pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6PTch, what the heck...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PBut... That reaction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#6PGuh...\x02",
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
            "#00007F#4S#5P─How long are you going\x01",
            "to hide for!?\x02",
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
        "#10301F#12PHuuuh...?\x02",
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
        "Young Man's Voice",
        (
            "#3716V#30A#40WUhuhu─ Well done\x01",
            "figuring it out.\x02",
        )
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

    def lambda_128C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_128C)
    Sleep(50)

    def lambda_129C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_129C)
    Sleep(50)

    def lambda_12AC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_12AC)
    Sleep(50)

    def lambda_12BC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12BC)
    Sleep(50)

    def lambda_12CC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_12CC)
    Sleep(50)

    def lambda_12DC():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_12DC)
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
        (
            "#00201F#12P#NI didn't feel his\x01",
            "presence...\x02",
        )
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1453")

    NpcTalk(
        0x8,
        "Boy",
        (
            "#04804F#5PUhuhu, how cold.\x02\x03",
            "We passed each other once\x01",
            "so we're no strangers,\x01",
            "and yet...\x02\x03",
            "#04802F─Isn't that right, ladies\x01",
            "and gentlemen of the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_151B")

    label("loc_1453")


    NpcTalk(
        0x8,
        "Boy",
        (
            "#04804F#5PUhuhu, how cold.\x02\x03",
            "It's our first meeting,\x01",
            "strictly speaking, but we\x01",
            "are no strangers, and yet...\x02\x03",
            "#04802F─Isn't that right, ladies\x01",
            "and gentlemen of the Special\x01",
            "Support Section?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_151B")

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
        (
            "#00101F#11PCould it be that\x01",
            "you're...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PThe hacker who tried to\x01",
            "catch Lloyd and the others\x01",
            "in a trap at Jona's place...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_176D")

    ChrTalk(
        0x101,
        (
            "#00003F#5P...And also the one who\x01",
            "gave the tower information\x01",
            "to the terrorists, huh.\x02",
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
            "#00013F#5PWe actually passed by each\x01",
            "other before in front to\x01",
            "the Doll Studio, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_17CA")

    label("loc_176D")


    ChrTalk(
        0x101,
        (
            "#00003F#5P...And also the one who\x01",
            "gave the tower information\x01",
            "to the terrorists, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_17CA")

    Fade(500)
    OP_68(-14350, 6950, 1450, 0)
    MoveCamera(330, -13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13250, 0)
    OP_0D()

    NpcTalk(
        0x8,
        "Boy",
        "#04809F#5PUhuhu, right answer.\x02",
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
            "#30WOuroboros Enforcer No. 0──\x01",
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
        "#00010F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00107F#11PThe secret society that\x01",
            "threw Liberl into chaos!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_1AF6")
    OP_29(0xA5, 0x1, 0xB)

    ChrTalk(
        0x104,
        (
            "#00311F#11P#NI thought he was connected to\x01",
            "'em ever since we met him in\x01",
            "front of that studio, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#10306F#11P#NTo think he was\x01",
            "cooperating with the\x01",
            "likes of terrorists...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1B65")

    label("loc_1AF6")

    OP_29(0xA5, 0x1, 0xC)

    ChrTalk(
        0x104,
        (
            "#00311F#11P#NI thought it was suspicious\x01",
            "that the terrorists were using\x01",
            "mechanized dolls, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1B65")

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
            "#04804F#6P#NUhuhu, they were unlucky\x01",
            "too, weren't they.\x02\x03",
            "#04802FHeiyue and Red\x01",
            "Constellation... Some\x01",
            "dangerous guys appeared, eh?\x02\x03",
            "#04806FHow unfortunate, especially\x01",
            "for those guys from the\x01",
            "Empire, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        (
            "#10107F#11PD-Don't joke around!\x02\x03",
            "You were the ally they\x01",
            "were cooperating with,\x01",
            "weren't you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04809F#6P#NAhaha. In the end, they were\x01",
            "merely pawns I used.\x02\x03",
            "#04802FIt seemed they would act in a\x01",
            "pretty interesting way, so I\x01",
            "just helped them out a little.\x02\x03",
            "#04804FI had zero interest in their\x01",
            "opinions and ideology.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x109,
        "#10110F#11PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11P#NHmph, you have quite the\x01",
            "nice personality, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00211F#5P...I think he's on the\x01",
            "same level as you, Wazy.\x02",
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
            "#00003F#5P─Enough with the jokes.\x02\x03",
            "#00001FWhat the heck are you\x01",
            "trying to do in\x01",
            "Crossbell?\x02",
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
            "#00007F#4S#5PAnd above all─ What have\x01",
            "you done with KeA!?\x02\x03",
            "#4SI'll have you tell us by\x01",
            "force!\x02",
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
            "#04804F#5PUhuhu, nice spirit\x01",
            "you've got there.\x02\x03",
            "#04800FBut, I didn't do\x01",
            "anything to your little\x01",
            "princess, you know?\x02\x03",
            "I did see her wander\x01",
            "past here just now,\x01",
            "though.\x02",
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
            "#00307F#12P#NBastard... You playin'\x01",
            "dumb!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#04804F#5PHuhu, but it's true.\x02\x03",
            "#04802FIt's up to you whether\x01",
            "to believe me or not,\x01",
            "though.\x02\x03",
            "I just came to greet you\x01",
            "today.\x02",
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

    def lambda_24D3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24D3)
    Sleep(50)

    def lambda_24E3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_24E3)
    Sleep(50)

    def lambda_24F3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24F3)
    Sleep(50)

    def lambda_2503():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2503)
    Sleep(50)

    def lambda_2513():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2513)
    Sleep(50)

    def lambda_2523():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2523)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00101F#6PAh─\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PIt went back to\x01",
            "normal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#12P...A large-scale trick,\x01",
            "isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PCould it be a kind of\x01",
            "magic...?\x02",
        )
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

    def lambda_272F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_272F)
    Sleep(50)

    def lambda_273F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_273F)
    Sleep(50)

    def lambda_274F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_274F)
    Sleep(50)

    def lambda_275F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_275F)
    Sleep(50)

    def lambda_276F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_276F)
    Sleep(50)

    def lambda_277F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_277F)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#04809F#5PUhuhu. Then, I guess\x01",
            "I'll excuse myself for\x01",
            "now.\x02\x03",
            "#04802FI pray we'll meet again\x01",
            "before long.\x02\x03",
            "#04805F─Oh, your little\x01",
            "princess went towards\x01",
            "the castle further in.\x02\x03",
            "#04804FGo protect her at once,\x01",
            "alright?\x02",
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
        "#00010F#5P#4SThat's Ouroboros!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PWe heard about them from\x01",
            "Estelle and Renne...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5P...They seem like an unthinkable\x01",
            "group, to say nothing of their\x01",
            "hacking skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#11PWhoa, even they came to\x01",
            "Crossbell!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PN-No way... Why is it\x01",
            "always Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#11P#NIt seems they have many\x01",
            "ulterior motives.\x02\x03",
            "#10303F─Well, that aside...\x02\x03",
            "#10301FShouldn't protecting KeA\x01",
            "come first right now?\x02",
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
            "#00011F#5PRight! He said she's at\x01",
            "the castle further\x01",
            "inside!\x02",
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

    # Function_8_CC1 end

    def Function_9_2DE8(): pass

    label("Function_9_2DE8")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F...KeA is in the castle\x01",
            "up ahead. Hurry, after\x01",
            "her!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -10940, 0, 3960, 135)
    EventEnd(0x4)
    Return()

    # Function_9_2DE8 end

    def Function_10_2E3F(): pass

    label("Function_10_2E3F")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F...KeA is in the castle\x01",
            "up ahead. Hurry, after\x01",
            "her!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 10740, 0, 4720, 225)
    EventEnd(0x4)
    Return()

    # Function_10_2E3F end

    def Function_11_2E96(): pass

    label("Function_11_2E96")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001F...KeA is in the castle\x01",
            "up ahead. Hurry, after\x01",
            "her!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 0, -14500, 0)
    EventEnd(0x4)
    Return()

    # Function_11_2E96 end

    SaveToFile()

Try(main)
