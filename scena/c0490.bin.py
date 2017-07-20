from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0490.bin",                # FileName
        "c0490",                    # MapName
        "c0490",                    # Location
        0x0036,                     # MapIndex
        "ed7151",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 54, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0490",                  # 0
        "Sigmund",             # 1
        "Charlie",             # 2
        "Hunting soldier Gareth",             # 3
        "Manager",                 # 4
        "Dishes",                   # 5
        "Dishes",                   # 6
        "Dishes",                   # 7
        "Dishes",                   # 8
        "Dishes",                   # 9
        "Clyde",               # 10
        "Mrs. Margaret",       # 11
        "Pierre deputy director",         # 12
        "Hunter Sachs",           # 13
        "Clerk",                   # 14
        "Clerk",                   # 15
        "hostess",               # 16
        "hostess",               # 17
        "A customer",                     # 18
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(712, 0)                                        # 0

    ScpFunction((
        "Function_0_2C8",          # 00, 0
        "Function_1_378",          # 01, 1
        "Function_2_3A2",          # 02, 2
        "Function_3_3D2",          # 03, 3
        "Function_4_409",          # 04, 4
        "Function_5_440",          # 05, 5
        "Function_6_470",          # 06, 6
        "Function_7_4A0",          # 07, 7
        "Function_8_4D0",          # 08, 8
        "Function_9_558",          # 09, 9
        "Function_10_577",         # 0A, 10
        "Function_11_5EF",         # 0B, 11
        "Function_12_2C34",        # 0C, 12
        "Function_13_541B",        # 0D, 13
        "Function_14_543F",        # 0E, 14
    ))


    def Function_0_2C8(): pass

    label("Function_0_2C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_300"),
        (1, "loc_30C"),
        (2, "loc_318"),
        (3, "loc_324"),
        (4, "loc_330"),
        (5, "loc_33C"),
        (6, "loc_348"),
        (SWITCH_DEFAULT, "loc_354"),
    )


    label("loc_300")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_30C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_318")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_324")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_330")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_33C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_348")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_354")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_360")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_377")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_360")

    label("loc_377")

    Return()

    # Function_0_2C8 end

    def Function_1_378(): pass

    label("Function_1_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_38F")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 11)
    Jump("loc_3A1")

    label("loc_38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3A1")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 12)

    label("loc_3A1")

    Return()

    # Function_1_378 end

    def Function_2_3A2(): pass

    label("Function_2_3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3BC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x162), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_3D1")

    label("loc_3BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3D1")

    Return()

    # Function_2_3A2 end

    def Function_3_3D2(): pass

    label("Function_3_3D2")


    def lambda_3D7():
        OP_95(0xFE, 99300, 0, -2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D7)

    def lambda_3F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_3_3D2 end

    def Function_4_409(): pass

    label("Function_4_409")


    def lambda_40E():
        OP_95(0xFE, 100700, 0, -2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40E)

    def lambda_428():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_428)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_4_409 end

    def Function_5_440(): pass

    label("Function_5_440")


    def lambda_445():
        OP_95(0xFE, 101000, 0, -6100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_445)

    def lambda_45F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_45F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_5_440 end

    def Function_6_470(): pass

    label("Function_6_470")


    def lambda_475():
        OP_95(0xFE, 100000, 0, -5700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_475)

    def lambda_48F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_6_470 end

    def Function_7_4A0(): pass

    label("Function_7_4A0")


    def lambda_4A5():
        OP_95(0xFE, 99000, 0, -6100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A5)

    def lambda_4BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_7_4A0 end

    def Function_8_4D0(): pass

    label("Function_8_4D0")

    OP_92(0x9, 0x186A0, 0x14B4, 0x1F4)

    def lambda_4E2():
        OP_95(0xFE, 100000, 0, 5300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E2)
    WaitChrThread(0x9, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)

    def lambda_51B():
        OP_95(0xFE, 100000, 0, 7300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_51B)

    def lambda_535():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_535)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_8_4D0 end

    def Function_9_558(): pass

    label("Function_9_558")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_576")
    SetChrSubChip(0x9, 0x0)
    Sleep(250)
    SetChrSubChip(0x9, 0x1)
    Sleep(250)
    Jump("Function_9_558")

    label("loc_576")

    Return()

    # Function_9_558 end

    def Function_10_577(): pass

    label("Function_10_577")

    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x20)
    SetChrPos(0x9, 900, 0, 25200, 180)
    OP_0D()

    def lambda_5B0():
        OP_95(0xFE, 2500, 0, 25200, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5B0)
    WaitChrThread(0x9, 1)

    def lambda_5CE():
        OP_95(0xFE, 2500, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5CE)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x13B, 0x1F4)
    Return()

    # Function_10_577 end

    def Function_11_5EF(): pass

    label("Function_11_5EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("chr/ch42900.itc", 0x1F)
    LoadChrToIndex("chr/ch03300.itc", 0x20)
    LoadChrToIndex("chr/ch00002.itc", 0x22)
    LoadChrToIndex("chr/ch00302.itc", 0x23)
    LoadChrToIndex("chr/ch03002.itc", 0x24)
    LoadChrToIndex("apl/ch51201.itc", 0x25)
    LoadChrToIndex("apl/ch51202.itc", 0x26)
    LoadChrToIndex("apl/ch51203.itc", 0x27)
    LoadChrToIndex("apl/ch51204.itc", 0x28)
    LoadChrToIndex("chr/ch25800.itc", 0x29)
    LoadChrToIndex("apl/ch50091.itc", 0x2A)
    LoadChrToIndex("apl/ch50092.itc", 0x2B)
    SoundLoad(3835)
    SoundLoad(3836)
    SoundLoad(3837)
    SoundLoad(3838)
    SoundLoad(3947)
    SoundLoad(3948)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 100500, 0, -9000, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 99500, 0, -9000, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 107600, 0, -1000, 270)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x0, -10000, 0, -7000, 0)
    SetChrPos(0x1, -10000, 0, -7000, 0)
    SetChrPos(0x2, -10000, 0, -7000, 0)
    SetChrPos(0x3, -10000, 0, -7000, 0)
    SetChrPos(0x101, 100500, 0, -9000, 0)
    SetChrPos(0x104, 100000, 0, -9000, 0)
    SetChrPos(0x105, 99500, 0, -9000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(101420, 1300, -1100, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26240, 0)
    SetCameraDistance(22440, 6000)
    FadeToBright(1500, 0)
    OP_0D()
    PlaceName2(340, 50, "c_plac67", 0x0, 0)
    BeginChrThread(0xA, 3, 0, 3)
    Sleep(600)
    BeginChrThread(0x9, 3, 0, 4)
    Sleep(1200)
    BeginChrThread(0x104, 3, 0, 6)
    Sleep(600)
    BeginChrThread(0x101, 3, 0, 5)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 7)
    OP_6F(0x79)
    Fade(500)
    OP_68(100000, 2600, -3500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16149, 0)
    OP_68(100000, 1600, -3500, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#12P#00001FWas there such a place …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FHun …\x01",
            "Even in downtown area it is superb location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, I'm on the look out\x01",
            "The host club is also nearby.\x02\x03",
            "#10300FBy the way, this store …\x01",
            "Previously it was a witness of Professor Mr.\x01",
            "Recently there are many foreign guests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#04605FOh, it looks like that.\x02\x03",
            "#04609FBy the way it's a reservation today\x01",
            "You can relax without hesitation.\x02\x03",
            "#04602FSure, I entered it ♪\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 8)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FHey ….\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)

    ChrTalk(
        0x105,
        "#6P#10302FHe is a freaky child.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F…… Gareth.\x01",
            "Amulet, sorry to bother you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHaha, nothing.\x02",
    )

    CloseMessageWindow()
    OP_68(100000, 1300, -2500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x101, 500, 0, -8100, 0)
    SetChrPos(0x104, -500, 0, -6800, 0)
    SetChrPos(0x105, -1000, 0, -8100, 0)
    SetChrPos(0xA, -500, 0, -5000, 0)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, 900, 50, 25800, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x9, 3, 0, 9)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -700, 50, 25800, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1500, -4000, 0)
    MoveCamera(305, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24500, 0)

    def lambda_BBA():
        OP_97(0xA, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_BBA)
    Sleep(100)

    def lambda_BD7():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BD7)
    Sleep(100)

    def lambda_BF4():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BF4)
    Sleep(100)

    def lambda_C11():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C11)
    OP_68(0, 1500, 6000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(100, 1500, 13380, 0)
    MoveCamera(305, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    WaitChrThread(0xA, 0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x8,
        "Sturdy voice",
        "#3835V#30WYou came, Randall\x02",
    )

    CloseMessageWindow()
    OP_24(0xEFB)
    OP_C9(0x1, 0x80000000)
    OP_68(-600, 1000, 23500, 2500)
    MoveCamera(321, 17, 0, 2500)
    SetCameraDistance(18000, 2500)
    OP_6F(0x79)
    SetChrFlags(0xA, 0x80)

    def lambda_CEC():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4F4C, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CEC)
    Sleep(100)

    def lambda_D09():
        OP_96(0xFE, 0x1F4, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D09)
    Sleep(50)

    def lambda_D26():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D26)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x104,
        (
            "#6P#00303FUncle Takashi ……\x01",
            "Is not it abrupt?\x02\x03",
            "#00301FTwo weeks since I saw you before ……\x01",
            "It's due to a habit I did not hear anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "Huh, here too\x01",
            "There are various things to do.\x02\x03",
            "But you are here\x01",
            "To bring along a bush … …\x02\x03",
            "Two years ago you would have never done that\x02",
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
        0x104,
        (
            "#6P#00306FHun …\x01",
            "My leader is legal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#N#00003FNice to meet you\x02\x03",
            "#00001FCrossbell Police, Special Affairs Support Division,\x01",
            "It is called Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#10304FAlso Associate Members of the Support Division,\x01",
            "It's Wadi Himisphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11P\"Crimson Shokai\" representative,\x01",
            "It's Sigmund Orlando.\x02\x03",
            "#04500FThere are also inconvenient lenders.\x01",
            "You should drink slowly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#N#00003FWell then we will accept\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#10302FBy the way, you said that you bothered me\x01",
            "Is it OK with one of the old mines?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#11PHaha, I wonder\x02\x03",
            "#04504FYou're hungry, are not you?\x01",
            "Let's bring food right away.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x3)
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x9,
        (
            "#04609FMunching …\x01",
            "Oh, I added another parfait!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x104, -2900, 50, 24950, 135)
    SetChrPos(0x101, -3100, 50, 23300, 90)
    SetChrPos(0x105, -3100, 50, 21800, 90)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1400, 200, 23900, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x2A)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -1400, 200, 22800, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x2A)
    SetChrSubChip(0xE, 0x5)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1400, 200, 21700, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xF, 0x8)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -600, 300, 21700, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x5)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 900, 200, 24100, 0)
    BeginChrThread(0x9, 3, 0, 9)
    OP_68(-700, 1400, 24300, 0)
    MoveCamera(319, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15100, 0)
    SetCameraDistance(15600, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#04503F#11PNow then, we have a lot to discuss\x02\x03",
            "#04500FFirst of all, guests.\x01",
            "Let's answer questions from you.\x02\x03",
            "I'm sure you have plenty\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F……Yes.\x01",
            "The story is early and it is saved.\x02\x03",
            "#00008FFrankly speaking, Crossbell Police\x01",
            "I am paying attention to your trend.\x02\x03",
            "#00013FEspecially for what purpose\x01",
            "Whether you are staying in a crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#11PHa, that's frank\x02\x03",
            "#04504FThe reason why we are here\x01",
            "There are some … …\x02\x03",
            "#04500FOf course the greatest purpose is\x01",
            "It is because I signed a \"contract\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001Fthat is……\x01",
            "Is it a contract with the Imperial Government?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHah, no comment\x02\x03",
            "Towards the industry of Uchiha\x01",
            "You conflict with confidentiality obligation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI see..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWell then, Elebonia's\x01",
            "What is the relationship with Captain Rector?\x02\x03",
            "With the acquisition of Rubathe's site\x01",
            "You seem to have been indebted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PKuku, that cheek#4RInnocent#Use it.\x02\x03",
            "There is only the \"Kokoro\" of \"Iron Blood\"\x01",
            "It is quite a funny kid.\x02\x03",
            "#04500FUnexpectedly, Tsao Even\x01",
            "It might be a good match.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011FHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00301FUncle Takashi ……\x01",
            "Do you even know that glasses guy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04500F#11PLast year, \"Troll\" Turf\x01",
            "I met with each other when stirring.\x02\x03",
            "Honestly, it was a lukewarm job\x01",
            "You are being touched by the power of the guy.\x02\x03",
            "#04504FHuh, no doubt even in this town\x01",
            "I did not expect to face her face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04606FMogmog …\x01",
            "Rumor's \"Silver#2RIn#\"What is it\x01",
            "I did not see you after all.\x02\x03",
            "I wish you could do another job\x01",
            "It was like a near miss.\x02\x03",
            "#04600FSurely a while ago\x01",
            "You were in the crossbell, were not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FOh, since Rubache is gone\x01",
            "It seems that there is no sound, but ……\x02\x03",
            "#00301F─ ─, do not devil it.\x01",
            "That Rector is with Yatsu\x01",
            "I heard that relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#11PWell, that is\x01",
            "That is a no comment.\x02\x03",
            "That's enough \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00301FTch\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt's fine Randy\x02\x03",
            "#00008FBy the way it should be safe\x01",
            "Is it okay?\x02\x03",
            "#00001FThis \"contract\" is\x01",
            "How much is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)

    ChrTalk(
        0x8,
        "#04505F#11PWoah\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04602FHaha, older brother.\x01",
            "It is good to see eyes ~.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 9)

    ChrTalk(
        0x105,
        (
            "#6P#10306FI see, such a reaction\x01",
            "It's about the amount that comes out.\x02\x03",
            "#10302FCould it be 100 million mira or more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PNo comment ──\x01",
            "Although it is okay to let it go.\x02\x03",
            "#04502FWell, regarding this contract\x01",
            "Let's say that amount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FA-around a 100 million mira contract\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FHaha, well that's quite grand\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306F…… I do not care about it either\x01",
            "I guess you are trying to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04500F#11PHah, well that's all you're getting for free\x02\x03",
            "#04503FWell then……\x01",
            "Let's say it's time to get into the main subject.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04503F#11P── Randolph.\x01",
            "Even though I said before, the vacation is over.\x02\x03",
            "#04501FTo you soon\x01",
            "The next \"fighting spirit#4RAn eggplant#\"To be succeeded.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#5P#00310F#4STch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10301F\"Fighting spirit\" ……\x01",
            "Is it my father 's alias?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    SetCameraDistance(14000, 50000)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    Sound(802, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0x104, 0x1)
    Sound(811, 0, 100, 0)
    Sound(886, 0, 50, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x104,
        (
            "#5P#00307F── Zaken!\x01",
            "What are you going to do with your mouth!\x02\x03",
            "No drink or drunk\x01",
            "I guess it will not get rid of it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHah, it's a simple story\x02\x03",
            "I am leading the \"red constellation\"\x01",
            "It must be a \"fighting spirit\".\x02\x03",
            "#04500FAnd to succeed it\x01",
            "It is your duty to be your brother's son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FW-why me\x02\x03",
            "#00307FIf you need \"fighting spirit\"\x01",
            "You guys are going around! Is it?\x02\x03",
            "Whatever Shirley can do!\x01",
            "There must be no reason why you should not be a woman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04503F#11PI 'm to the last \"demon\" ……\x01",
            "Only exist to overrun the battlefield#4RMono#.\x02\x03",
            "As a brother is a good-natured kid,\x01",
            "I also do not want to become.\x02\x03",
            "#04500FThat is my daughter#2RA guy#It is the same …\x01",
            "No, in a sense it would be more than me.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)

    ChrTalk(
        0x9,
        (
            "#12P#04604FYes, yeah, Charlie too\x01",
            "What a \"fighting spirit\"#2RGala#Is not it.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 9)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x1)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)

    ChrTalk(
        0x104,
        "#5P#00310FUgh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04503F#11P── Randolph.\x01",
            "You ought to know.\x02\x03",
            "Big brother why, with long years nemesis\x01",
            "Did you feel like attaching a settlement?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_2153():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2153)
    WaitChrThread(0x104, 2)
    Sleep(500)

    ChrTalk(
        0x104,
        "#5P#00308F#40W#2SAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04501F#11POnce the older brother\x01",
            "I gave you a \"trial\".\x02\x03",
            "And you get over it,\x01",
            "I showed a superb instrument that succeeded the \"fighting spirit\".\x02\x03",
            "#04504F─ ─ You should be aware.\x01",
            "Do not become a \"other thing\" anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00311FUgh…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FSucceeding the Toushin\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x1)
    Sound(857, 0, 100, 0)
    Sound(856, 0, 50, 0)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#12P#04609FEh, now I'm stubborn\x01",
            "Old Randy's older brother was amazing.\x02\x03",
            "#04602FA large unit of \"Nishiwaze\"\x01",
            "To defeat that village ----\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x104,
        (
            "#5P#00313F#30W#4SShut up\x02\x03",
            "#50W#3SI'm begging. Don't say anymore\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    def lambda_23C9():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_23C9)
    WaitChrThread(0x104, 2)
    Sleep(500)

    def lambda_23E9():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_23E9)
    WaitChrThread(0x104, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005FRandy…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04601FDasa ……\x01",
            "It's a little shocking.\x02\x03",
            "#04606FOnce again this time to Randy's older brother\x01",
            "Although there was something I was admiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11P…… Kuku.\x01",
            "Keep it for that.\x02\x03",
            "#04500FWe're going home for tonight, Shirley\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#04600FOh, got it\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x9, 3, 0, 10)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    SetChrPos(0x8, -700, 0, 25200, 180)
    OP_0D()
    Sleep(300)
    OP_68(-1560, 1400, 24280, 2500)
    MoveCamera(323, 15, 0, 2500)
    OP_6E(550, 2500)

    def lambda_259C():
        OP_95(0xFE, -2200, 0, 24800, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_259C)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_6F(0x1)
    SetCameraDistance(13500, 15000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#11P#04503F#3836V#30WThat figure, if my brother saw it\x01",
            "Think carefully what you think.\x02\x03",
            "#3837VBefore further exposing the nuisance\x01",
            "Follow or flee,\x01",
            "Decide whether to defend it.\x02\x03",
            "#04502F#3838V#40WOtherwise, die.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEFE)
    OP_C9(0x1, 0x80000000)
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x101,
        "#00013F…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00314F#40W….\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#04609F#12P#N#3947V#30WEheh, night then, Randy-nii!\x02\x03",
            "#04602F#3948VThe older brothers also ~!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF6C)
    OP_C9(0x1, 0x80000000)
    OP_68(-700, 1300, 20300, 4000)
    SetCameraDistance(17500, 4000)
    OP_93(0x9, 0x2, 0xBE)

    def lambda_277E():
        OP_95(0xFE, 2500, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_277E)
    Sleep(300)

    def lambda_279B():
        OP_95(0xFE, -2300, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_279B)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x105, 0x0)
    Sleep(700)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x105, 0x2)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Fade(500)
    SetCameraDistance(15300, 0)
    OP_68(-2900, 1100, 24950, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    OP_6F(0x79)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    OP_0D()
    Sound(2374, 255, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#11P#00316F#40WI want your ladies\x01",
            "I'm glad I did not bring her … …\x02\x03",
            "#00315FIt was way too lame here\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(250)

    ChrTalk(
        0x101,
        "#6P#00008FRandy…\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#11P#00306F#30WSorry\x02\x03",
            "#00308FA place that is not uniform\x01",
            "It seems like I showed you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FDon't say that\x02\x03",
            "#00013FWhatever you think …\x01",
            "Are they funny?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, but that far\x01",
            "Looking at where he is going\x02\x03",
            "#10300FIt might have been a bulls eye\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#11P#00007FWazy!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(2375, 255, 100, 0)

    ChrTalk(
        0x104,
        "#11P#00312F#40WYou're really dirty\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetCameraDistance(13800, 12500)
    Fade(250)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    OP_0D()
    Sleep(800)

    ChrTalk(
        0x104,
        (
            "#11P#00313F#40W#25ABut it's true.\x02\x03",
            "#50W#30AIt is none other than this … …\x01",
            "I was hit by a painful place.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── After that, Lloyd's\x01",
            "Manager of the manager trying to arrange a car\x01",
            "I returned home after refusing the offer.\x02\x03",
            "With women who were anxiously waiting\x01",
            "Show us yourself in a safe place … Sergei\x02\x03",
            "After sleeping sleepy Ka'a\x01",
            "Lloyd's a story of things#4RBamboo shoots#Reported.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 3)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_5EF end

    def Function_12_2C34(): pass

    label("Function_12_2C34")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch47500.itc", 0x1E)
    LoadChrToIndex("chr/ch44000.itc", 0x1F)
    LoadChrToIndex("chr/ch06400.itc", 0x20)
    LoadChrToIndex("chr/ch42800.itc", 0x21)
    LoadChrToIndex("chr/ch25800.itc", 0x22)
    LoadChrToIndex("chr/ch25900.itc", 0x23)
    LoadChrToIndex("chr/ch26802.itc", 0x24)
    LoadChrToIndex("chr/ch43402.itc", 0x25)
    LoadChrToIndex("chr/ch27702.itc", 0x26)
    LoadChrToIndex("chr/ch47502.itc", 0x27)
    LoadChrToIndex("chr/ch44002.itc", 0x28)
    SoundLoad(812)
    SoundLoad(896)
    OP_68(104870, 3100, -2210, 0)
    MoveCamera(46, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x101, 103450, 0, -1770, 90)
    SetChrPos(0x102, 103840, 0, -3240, 45)
    SetChrPos(0x103, 103720, 0, 140, 135)
    SetChrPos(0x104, 105010, 0, -1570, 90)
    SetChrPos(0x109, 102060, 0, -780, 90)
    SetChrPos(0x105, 104660, 0, -4160, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 101610, 0, -2300, 90)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 107620, 0, -1610, 270)
    OP_68(104870, 1500, -2210, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()

    ChrTalk(
        0x104,
        (
            "#1P#00303F…… That's it.\x01",
            "Entering us\x01",
            "I want to have permission.\x02\x03",
            "#00301FOf course, my uncle\x01",
            "It is a secret to Charlie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "…… If you think that you have matched your face for the first time in a while\x01",
            "I do not seek to ask such a poor life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Kuku, Captain Randolph … …\x01",
            "As you are saying\x01",
            "Is not she getting through?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1P#00303F… … Stop that way.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_END)), "loc_2F3C")

    ChrTalk(
        0x101,
        (
            "#00001F(A hunter of 'Red constellation' … …\x01",
            "I saw him in front of the Crimson Shopping Association\x01",
            "It looks like the same person. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F82")

    label("loc_2F3C")


    ChrTalk(
        0x101,
        (
            "#00001F(A red constellation hunter … …\x01",
            "It looks like Randy's face knows. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F82")


    ChrTalk(
        0x13,
        "(Go, go crazy … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "…… Kuku, well\x01",
            "It is a request of nothing else.\x01",
            "I will cooperate with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "However, it happens inside the store\x01",
            "A little trouble\x01",
            "It is a degree to close your eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Even that you came,\x01",
            "I will keep silent on deputy headmen and young ladies.\x01",
            "…… Is that okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1P#00303F… It's enough.\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#1P#00300FFor a while, the preparation was completed.\x02\x03",
            "#00300FMy wife is still here,\x01",
            "If you're going to ambush\x01",
            "You'd better enter first.\x02\x03",
            "#00303FI will not let you hold back to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, the number to a minimum\x01",
            "It seems better to squeeze … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Well, as I enter, of course,\x01",
            "Decide the rest with you guys!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_326F():
        TurnDirection(0x101, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_326F)
    Sleep(50)

    def lambda_327F():
        TurnDirection(0x102, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_327F)
    Sleep(50)

    def lambda_328F():
        TurnDirection(0x103, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_328F)
    Sleep(50)

    def lambda_329F():
        TurnDirection(0x109, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_329F)
    Sleep(50)

    def lambda_32AF():
        TurnDirection(0x105, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_32AF)

    ChrTalk(
        0x109,
        "#10111F(I'm pretty clinging … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(To be honest, come this far.\x01",
            "It will not be possible to retract later … …)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10304FHuh, then I guess I'll join you.\x02\x03",
            "#10300FDeputy Director, Mr. Lloyd and I.\x01",
            "Are these 3 people OK?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1P#00300FOh, it is probably such a place.\x02",
    )

    CloseMessageWindow()

    def lambda_33D6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33D6)
    Sleep(50)

    def lambda_33E6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_33E6)
    Sleep(50)

    def lambda_33F6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_33F6)

    ChrTalk(
        0x102,
        (
            "#00100FWell then,\x01",
            "We are on standby.\x02\x03",
            "If there should be any chance\x01",
            "Please call me with Enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, I understand.\x02\x03",
            "#00000FWell then\x01",
            "Let's suppose to enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Well … Well, let's go! It is!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -7010, 0, -3490, 90)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -3410, 0, -5940, 90)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -4740, 0, -2140, 225)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x2)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 7220, 0, -990, 225)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x1)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 6220, 0, -1000, 180)
    SetChrPos(0x101, -3560, 0, 18530, 180)
    SetChrPos(0x105, -4460, 0, 18910, 180)
    SetChrPos(0x13, -3870, 0, 19520, 180)
    OP_68(-2710, 1500, -5230, 0)
    MoveCamera(307, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19130, 0)
    OP_68(3930, 1500, -3640, 6000)
    MoveCamera(307, 18, 0, 6000)
    OP_6E(440, 6000)
    SetCameraDistance(19130, 6000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()
    OP_68(-4560, 1500, 16460, 8000)
    MoveCamera(305, 17, 0, 8000)
    OP_6E(440, 8000)
    SetCameraDistance(17710, 8000)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000FOnce, when the wife comes\x01",
            "Have them guide you in the seat there immediately\x01",
            "I am at my disposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Well, yes.\x01",
            "I guess it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "A vice broker … …\x01",
            "I will absolutely catch it!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1194)

    ChrTalk(
        0x105,
        (
            "#10309FHuh, what?\x01",
            "I'm getting excited.\x02\x03",
            "#10305F…… っ て.\x01",
            "While doing so\x01",
            "It seems they came.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 0x1E)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x11, -480, 0, -8690, 0)
    SetChrPos(0x12, 790, 0, -8960, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(360, 1500, -6110, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20150, 0)
    Sleep(100)
    OP_68(780, 1500, -8090, 2500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)

    def lambda_3821():
        OP_9B(0x0, 0x11, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3821)
    Sleep(300)

    def lambda_3839():
        OP_9B(0x0, 0x12, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3839)
    WaitChrThread(0x11, 1)

    def lambda_3852():
        OP_95(0x11, -2000, 0, -5940, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3852)
    WaitChrThread(0x12, 1)

    def lambda_3870():
        OP_93(0x12, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3870)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0x10E, 0x1F4)
    OP_6F(0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "Um, I had a reservation.\x01",
            "It's Clyde, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Please go over there.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5840, 1500, 14140, 0)
    MoveCamera(298, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20470, 0)
    SetChrChipByIndex(0x11, 0x27)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x11, 0x2)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, -7450, 100, 14400, 135)
    SetChrPos(0x12, -8000, 100, 13110, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x12,
        "Huh, it's quite a nice shop.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Mother, Margaret …\x01",
            "Are these places first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Clearly with the husband of the police career\x01",
            "I wonder if she is showing her face in various places.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x1)

    ChrTalk(
        0x12,
        "Okho, please stop joke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Taka is like the deputy director of the police.\x01",
            "I know a salary ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Rather than going to a fashionable store with me,\x01",
            "How to drink with hostess at the end of the bar\x01",
            "It fits that person's sex.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    ChrTalk(
        0x11,
        "Hahaha, this was rude.\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x11,
        (
            "Well then, in the daytime\x01",
            "Even cocktails for business\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Huh … I will have you.\x02",
    )

    CloseMessageWindow()
    OP_68(-5050, 1500, 16160, 2000)
    OP_6F(0x1)
    Sleep(500)
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x13)

    ChrTalk(
        0x101,
        (
            "#00012F(Fu, deputy director.\x01",
            "The way you do not mind ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "(Well, noisy ……\x01",
            "Please do not mind. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "(Huh, oh yes.\x01",
            "Anyway, my thin salary\x01",
            "I can not come to such an exclusive shop. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "(For me the bar at the end suits you.\x01",
            "What's wrong with that … ….! )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10300FI was totally injured.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Oh, it's okay, really … ….)\x02",
    )

    CloseMessageWindow()
    OP_68(-5840, 1500, 14140, 2000)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x11,
        "Well then, although it is quickly, here.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Clyde wrote documents that might be contracts\x01",
            "I took it out of the attache case.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(18, 0, 50, 0)
    Sleep(200)

    ChrTalk(
        0x11,
        (
            "The wife is wanting,\x01",
            "It is in the prime location of Michelin\x01",
            "It is a contract of a villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "The rest is here\x01",
            "If you can sign,\x01",
            "That mansion belongs to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "Ho ho …\x01",
            "At last this time came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Of course I will sign.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00001F(After all, Michelin's\x01",
            "It looks like it was a villa deal … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Well, what are you going to do from here?)\x02\x03",
            "#10304F(Even if you step in,\x01",
            "Even hearing a little more … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x13)

    ChrTalk(
        0x13,
        "… … Wow … …\x02",
    )

    CloseMessageWindow()
    OP_68(-6600, 0, 15210, 500)
    MoveCamera(305, 18, 1, 500)
    OP_6E(500, 500)
    SetCameraDistance(20950, 500)
    OP_95(0x13, -2060, 0, 19090, 5000, 0x0)
    OP_95(0x13, -2360, 0, 12830, 5000, 0x0)
    TurnDirection(0x13, 0x12, 1000)
    Sleep(50)
    OP_6F(0x1)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4STo deceive my wife is\x01",
            "Let's stop it! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)

    ChrTalk(
        0x11,
        "eh……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……you……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F(I understand …… !?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306F(Ah-hah.)\x02",
    )

    CloseMessageWindow()

    def lambda_4122():
        OP_95(0x101, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4122)
    Sleep(200)

    def lambda_413F():
        OP_95(0x105, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_413F)
    WaitChrThread(0x101, 1)

    def lambda_415D():
        OP_95(0x101, -1590, 0, 11760, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_415D)
    WaitChrThread(0x105, 1)

    def lambda_417B():
        OP_95(0x105, -1710, 0, 13690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_417B)
    WaitChrThread(0x105, 1)

    def lambda_4199():
        TurnDirection(0x105, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4199)
    Sleep(100)
    WaitChrThread(0x101, 1)

    def lambda_41AD():
        TurnDirection(0x101, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41AD)
    WaitChrThread(0x101, 1)
    Sound(812, 0, 100, 0)
    BeginChrThread(0x12, 1, 0, 14)
    Sleep(300)
    Sound(812, 0, 100, 0)
    BeginChrThread(0x11, 1, 0, 13)
    Sleep(1000)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x13)

    ChrTalk(
        0x12,
        "You … what does this mean?\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SMargaret! It is!\x01",
            "Please stop this transaction!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SThis evil real estate agent,\x01",
            "I'm trying to trick you!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "Eeeeeee! Is it?\x01",
            "Wait a moment, please! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Vice and … …,\x01",
            "Wow, what did I do ……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SYeah, keep silent!\x01",
            "The story is going up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……you……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SI cheated my wife with three tips,\x01",
            "It seems to be making a loose loan\x01",
            "I wonder what I was doing! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "……you……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SHowever, wholesale is not wholesome!\x01",
            "While my eyes are black ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "… … If you are … …\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SEh, you are skimpy!\x01",
            "I am the deputy director of the police … …\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x1450)

    ChrTalk(
        0x12,
        "#800W#5SStay silent.\x02",
    )

    Sleep(4800)
    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(896, 0, 60, 0)
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x13,
        "#2S……I'm sorry.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 500)
    Sleep(50)

    ChrTalk(
        0x101,
        "#00011F(Yo, weak!?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309F(Ahaha, I was completely silenced.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Absolutely …\x01",
            "The person you say is really\x01",
            "People who can not help it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "A person who is also deputy director of the police,\x01",
            "Hurry up and innocent people\x01",
            "It's like being a criminal … …\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x12,
        "#4SI do not think it's embarrassing! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Huh! It is!\x01",
            "I'm sorry I will not do it anymore!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x13)
    OP_64(0x101)
    OP_64(0x105)

    ChrTalk(
        0x13,
        "What's the misunderstanding …?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 500)
    Sleep(50)

    ChrTalk(
        0x101,
        "#00011FEeeeeee! It is! Is it? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FMadam, preferably if possible\x01",
            "Can you tell me the circumstances?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-6950, -600, 15800, 0)
    MoveCamera(328, 22, 1, 0)
    OP_6E(500, 0)
    SetCameraDistance(20840, 0)
    SetChrPos(0x11, -6060, 0, 13990, 90)
    OP_0D()
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)

    ChrTalk(
        0x12,
        "#3PFuu … Well, that would be nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PFirst of all,\x01",
            "This Clyde deals with luxury properties\x01",
            "You are a real estate agent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PAs you say,\x01",
            "I'm never an evil dealer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "But, even if so ……\x01",
            "Fund to buy a high class property in my place … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PActually, I, the stock that I started to kill time the other day\x01",
            "I got a considerable profit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PThat's what it takes you years\x01",
            "I finally got Mira to save.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "Kaku, turnip …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PTo be honest……\x01",
            "…… To the person you say,\x01",
            "My sociability was exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PI happened to have gotten with Conn and Luck\x01",
            "While stepping back to the position,\x01",
            "In my house I can not raise my head … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PI do not know if I have difficulty at home,\x01",
            "If it is ski, go drinking all night\x01",
            "It is unplanned to put pressure on households.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Uu …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PWhen the director general has failed\x01",
            "You, yourself becoming the next Director\x01",
            "I was in a good mood for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PBut, eventually, I will be another deputy director\x01",
            "I will take that post and work on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PMoreover, becoming so sick with that\x01",
            "Only complaints ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FOh, in that neighborhood ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3P…… so honestly,\x01",
            "I'm living together no more\x01",
            "I felt it was impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PSo, with Mira you got in stock\x01",
            "Trying to buy a house for a living,\x01",
            "That was why I was consulting Mr. Clyde.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PFor a while I lived there,\x01",
            "Eventually getting divorced\x01",
            "I was going to have a decision.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        "#4SKern! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FAhaha, I do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Sorry, you are too poor at all … …)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FOh, but …\x01",
            "\"What was it\" …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "……Huh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3P… … Hehe, well.\x01",
            "Well, I worry about me so far\x01",
            "Let's buy what you've done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PAll I do is beckoning\x01",
            "I was avoiding going home,\x01",
            "It is good for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PToday I got home,\x01",
            "Let's discuss it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Ma, Margaret ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)
    Sleep(50)

    ChrTalk(
        0x12,
        (
            "#3P……, that's why Mr. Clyde.\x01",
            "The case of buying this villa this time\x01",
            "I wonder if you could put it on hold.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)
    Sleep(50)

    ChrTalk(
        0x11,
        (
            "#3PWell, Margaret!\x01",
            "Keep up the negotiations so far …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#3PTo the end \"Pending\".\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PI also do it on my own\x01",
            "It was bad to be working,\x01",
            "I thought about talking over again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PIt's okay, I will not be living separately\x01",
            "Because it is true that I liked the property\x01",
            "I'm sure I will buy it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            "#3PWell, if possible today\x01",
            "I wanted to get a good reply ……\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#3PWell then I will excuse myself ……\x02",
    )

    CloseMessageWindow()
    OP_68(-5570, -600, 15480, 2000)

    def lambda_5123():
        OP_95(0x11, -2680, 0, 14150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5123)
    Sleep(500)

    def lambda_5140():
        OP_93(0x12, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5140)

    def lambda_514D():
        OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_514D)
    Sleep(100)

    def lambda_5165():
        OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5165)
    Sleep(100)

    def lambda_517D():
        OP_9B(0x1, 0x13, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_517D)
    WaitChrThread(0x11, 1)
    OP_6F(0x1)
    Sleep(50)

    def lambda_519B():
        OP_9B(0x0, 0x11, 0x5A, 0x2710, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_519B)
    Sleep(1000)
    OP_93(0x12, 0x5A, 0x1F4)
    Sleep(100)
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(100)
    TurnDirection(0x105, 0x11, 500)
    Sleep(100)
    TurnDirection(0x13, 0x11, 500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0x12, 0x87, 0x1F4)
    Sleep(100)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(100)
    OP_93(0x13, 0xB4, 0x1F4)
    Sleep(100)
    OP_93(0x105, 0xB4, 0x1F4)
    WaitChrThread(0x11, 1)
    SetChrFlags(0x11, 0x80)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00001FWell, after all,\x01",
            "It was innocent ……\x02\x03",
            "#00006FI did something wrong somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, that's okay.\x01",
            "For deputy director and wife\x01",
            "It seems I'm falling for a while.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 500)
    Sleep(50)

    ChrTalk(
        0x12,
        (
            "#3P… Well then, you.\x01",
            "I will also go home today.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5313():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5313)
    Sleep(50)

    def lambda_5323():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5323)
    Sleep(50)

    def lambda_5333():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5333)

    ChrTalk(
        0x12,
        (
            "#3PBecause I would like to talk a lot,\x01",
            "Tonight is coming home straight.\x01",
            "… That was obvious.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x13,
        "……, Yes! It is!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F(… … Is it OK? …)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c1160", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2C34 end

    def Function_13_541B(): pass

    label("Function_13_541B")

    Fade(500)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7060, 0, 13990, 90)
    Return()

    # Function_13_541B end

    def Function_14_543F(): pass

    label("Function_14_543F")

    Fade(500)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7490, 0, 13110, 90)
    Return()

    # Function_14_543F end

    SaveToFile()

Try(main)
