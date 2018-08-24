from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Sigmund",                # 1
        "Shirley",                # 2
        "Jaeger Gareth",          # 3
        "Manager",                # 4
        "食器",                   # 5
        "食器",                   # 6
        "食器",                   # 7
        "食器",                   # 8
        "食器",                   # 9
        "Clyde",                  # 10
        "Mrs. Margaret",          # 11
        "Vice Chief Pierre",      # 12
        "Jaeger Sachs",           # 13
        "Clerk",                  # 14
        "Clerk",                  # 15
        "Hostess",                # 16
        "Hostess",                # 17
        "Customer",               # 18
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
        "Function_12_2DB6",        # 0C, 12
        "Function_13_5744",        # 0D, 13
        "Function_14_5768",        # 0E, 14
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
        (
            "#12P#00001FSo there was a place\x01",
            "like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FHmph... Best place in\x01",
            "town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHaha, it's near the host club I frequent.\x02\x03",
            "#10300FCome to think of it... Before, this club used\x01",
            "to entertain a lot of congressmen. But lately,\x01",
            "it seems they have a lot of foreign guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#04605FYeah, seems like it.\x02\x03",
            "#04609FBut I got a reservation\x01",
            "for you guys today, so\x01",
            "make yourselves at home.\x02\x03",
            "#04602FCome on in♪\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 8)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FH-Hey...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)

    ChrTalk(
        0x105,
        (
            "#6P#10302FShe just does whatever\x01",
            "she wants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F...Gareth. Thanks for\x01",
            "taking care of her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHaha, perish the\x01",
            "thought.\x02",
        )
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

    def lambda_BF5():
        OP_97(0xA, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_BF5)
    Sleep(100)

    def lambda_C12():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C12)
    Sleep(100)

    def lambda_C2F():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C2F)
    Sleep(100)

    def lambda_C4C():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C4C)
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
        "Husky Voice",
        "#3835V#30W─Randolph, you came.\x02",
    )

    CloseMessageWindow()
    OP_24(0xEFB)
    OP_C9(0x1, 0x80000000)
    OP_68(-600, 1000, 23500, 2500)
    MoveCamera(321, 17, 0, 2500)
    SetCameraDistance(18000, 2500)
    OP_6F(0x79)
    SetChrFlags(0xA, 0x80)

    def lambda_D27():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4F4C, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D27)
    Sleep(100)

    def lambda_D44():
        OP_96(0xFE, 0x1F4, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D44)
    Sleep(50)

    def lambda_D61():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D61)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x104,
        (
            "#6P#00303FUncle... What's this all\x01",
            "of a sudden?\x02\x03",
            "#00301FWe met two weeks ago...\x01",
            "But I never got any\x01",
            "news.\x02",
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
            "We've been busy with this and that,\x01",
            "you see.\x02\x03",
            "But taking your friends to a place\x01",
            "like this...\x02\x03",
            "The you of two years ago would\x01",
            "never have done that.\x02",
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
            "#6P#00306FHmph. Our leader has a\x01",
            "strong sense of duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#N#00003F─Nice to meet you.\x02\x03",
            "#00001FLloyd Bannings,\x01",
            "Crossbell Police Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWazy Hemisphere, of the\x01",
            "same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PSigmund Orlando, Crimson\x01",
            "& Co. representative.\x02\x03",
            "#04500FThanks for going out of\x01",
            "your way to come. Relax\x01",
            "and have a drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#N#00003F...We'll take you up on\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#10302FSpeaking of going out of\x01",
            "your way, how 'bout that\x01",
            "Old Mine incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#11PHehe, I wonder.\x02\x03",
            "#04504FYou're hungry too, right?\x01",
            "I'll get something for\x01",
            "you right away.\x02",
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
            "#04609F*gulp gulp*... Ahhh,\x01",
            "another parfait, please!\x02",
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
            "#04503F#11PNow then, we have a lot\x01",
            "to discuss.\x02\x03",
            "#04500FFirst of all, I'd like\x01",
            "to answer our guests'\x01",
            "questions.\x02\x03",
            "You have one in\x01",
            "particular, don't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FYes. I'll make this quick.\x02\x03",
            "#00008FI'll be straight with you.\x01",
            "Crossbell Police has taken\x01",
            "notice of your actions.\x02\x03",
            "#00013FIn particular─ We want to\x01",
            "know why you've come to\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#11PHaha, how direct.\x02\x03",
            "#04504FWe're here for several\x01",
            "reasons, but...\x02\x03",
            "#04500FOur primary reason is of\x01",
            "course to close a\x01",
            ""contract".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FRegarding that... Is it\x01",
            "with the Imperial\x01",
            "government?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHaha, no comment.\x02\x03",
            "Confidentiality is\x01",
            "critical in my line of\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FThen, what's your\x01",
            "relationship with Secretary\x01",
            "Lechter of Erebonia?\x02\x03",
            "They helped you acquire the\x01",
            "old Revache building,\x01",
            "didn't they?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHehe, that joker, huh.\x02\x03",
            "Being the right-hand man of\x01",
            "that Blood and Iron, he's a\x01",
            "pretty interesting fellow.\x02\x03",
            "#04500FHe might be a good match\x01",
            "for the likes of Cao.\x02",
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
            "#5P#00301FUncle... You know that\x01",
            "glasses guy too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04500F#11PWe fought when we were\x01",
            "rooting around "their"\x01",
            "turf last year.\x02\x03",
            "Honestly, I don't like\x01",
            "those sorts of jobs, but\x01",
            "his troops hung in there.\x02\x03",
            "#04504FHaha, but to think we'd\x01",
            "meet again in Crossbell\x01",
            "City, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04606F*gulp, gulp*... But in\x01",
            "the end, we didn't get to\x01",
            "meet the rumored Yin...\x02\x03",
            "It seems he was on\x01",
            "another job... We just\x01",
            "barely missed each other.\x02\x03",
            "#04600FIf I'm not mistaken, he\x01",
            "was in Crossbell until\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FYeah. After Revache\x01",
            "disappeared we haven't\x01",
            "heard from him.\x02\x03",
            "#00301FDon't change the subject.\x01",
            "We asked about your\x01",
            "relationship with Lechter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#11PHehe. In short, no\x01",
            "comment.\x02\x03",
            "Figure out the rest on\x01",
            "your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00301FTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FIt's fine, Randy.\x02\x03",
            "#00008FBy the way, if you don't\x01",
            "mind my asking...\x02\x03",
            "#00001FHow much is this\x01",
            ""contract" worth?\x02",
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
        "#04505F#11POhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04602FAhaha. You sure know\x01",
            "what you're looking for.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 9)

    ChrTalk(
        0x105,
        (
            "#6P#10306FI see. So it's an amount\x01",
            "that would elicit that\x01",
            "kind of reaction.\x02\x03",
            "#10302FCould it be around 100\x01",
            "million mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PNo comment. ─That's all\x01",
            "I can say.\x02\x03",
            "#04502FWell, I guess you could\x01",
            "say it's about that\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FA contract worth 100\x01",
            "million mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FHehe, how bold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306F...I'm sure it's for\x01",
            "nothing good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04500F#11PHaha, that's all you're\x01",
            "getting for free.\x02\x03",
            "#04503FThen... Shall we get\x01",
            "down to business?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#04503F#11P─Randolph. I said it\x01",
            "before, but your\x01",
            "vacation's over.\x02\x03",
            "#04501FWe'll have you become\x01",
            "the next War God before\x01",
            "too long.\x02",
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
        "#5P#00310F#4S...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10301FWar God... Your old\x01",
            "man's nickname?\x02",
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
            "#5P#00307FDon't fuck with me! What\x01",
            "is this bullshit!?\x02\x03",
            "Are you drunk out of\x01",
            "your mind!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHaha, it's simple.\x02\x03",
            "The War God must lead\x01",
            "Red Constellation.\x02\x03",
            "#04500FAnd, as his only son,\x01",
            "you have a duty to\x01",
            "succeed him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FW-Why me...\x02\x03",
            "#00307FIf you need a War God,\x01",
            "why don't you do it!?\x02\x03",
            "Even Shirley could!\x01",
            "There's no reason it\x01",
            "can't be a woman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04503F#11PIn the end, I'm the Battle\x01",
            "Ogre... I exist only to run\x01",
            "through the battlefield.\x02\x03",
            "I can't be like my brother.\x01",
            "Furthermore, I don't think\x01",
            "I want to be like him.\x02\x03",
            "#04500FIt's the same for her...\x01",
            "No, maybe it's even more\x01",
            "true for her.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)

    ChrTalk(
        0x9,
        (
            "#12P#04604FYeah. Shirley isn't cut\x01",
            "out to be the War God\x01",
            "either.\x02",
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
        "#5P#00310FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04503F#11P─I'm sure you understand,\x01",
            "Randolph.\x02\x03",
            "Just why my brother decided\x01",
            "to settle the score with a\x01",
            "longtime enemy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_225A():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_225A)
    WaitChrThread(0x104, 2)
    Sleep(500)

    ChrTalk(
        0x104,
        "#5P#00308F#40W#2SAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04501F#11PBrother once gave you a "test".\x02\x03",
            "Having cleared it, it shows you have\x01",
            "the ability to succeed him as a fine\x01",
            "War God.\x02\x03",
            "#04504F─You must've realized that yourself.\x01",
            "I'll not hear that "other people's\x01",
            "problems" excuse any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00311F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FA War God succession\x01",
            "trial...\x02",
        )
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
            "#12P#04609FEhehe. He's kind of lame\x01",
            "now, but in past, Randy\x01",
            "was totally awesome!\x02\x03",
            "#04602FEspecially when, to crush\x01",
            "that Zephyr battalion, we\x01",
            "took out that villa─\x02",
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
            "#5P#00313F#30W#4S─Shut up.\x02\x03",
            "#50W#3SI'm begging you. Not\x01",
            "another word.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    def lambda_2525():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2525)
    WaitChrThread(0x104, 2)
    Sleep(500)

    def lambda_2545():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2545)
    WaitChrThread(0x104, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005FRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04601FYeah... It was a bit\x01",
            "shocking.\x02\x03",
            "#04606FBut even so, I looked up\x01",
            "to the old Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHehe. Let's leave it at\x01",
            "that.\x02\x03",
            "#04500FWe're going home for\x01",
            "tonight, Shirley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#04600FOh, okay.\x02",
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

    def lambda_26D7():
        OP_95(0xFE, -2200, 0, 24800, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_26D7)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_6F(0x1)
    SetCameraDistance(13500, 15000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#11P#04503F#3836V#30WThink hard on what my brother would\x01",
            "think if he saw you like this.\x02\x03",
            "#3837VDecide if you're going to look even\x01",
            "more pitiful before me, if you're going\x01",
            "to run, or if you'll fight against me.\x02\x03",
            "#04502F#3838V#40W─Otherwise, die.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEFE)
    OP_C9(0x1, 0x80000000)
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x101,
        "#00013F...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00314F#40W............\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x9,
        (
            "#04609F#12P#N#3947V#30WHaha, 'night Randy♪\x02\x03",
            "#04602F#3948VYou guys too. Later!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF6C)
    OP_C9(0x1, 0x80000000)
    OP_68(-700, 1300, 20300, 4000)
    SetCameraDistance(17500, 4000)
    OP_93(0x9, 0x2, 0xBE)

    def lambda_28DE():
        OP_95(0xFE, 2500, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_28DE)
    Sleep(300)

    def lambda_28FB():
        OP_95(0xFE, -2300, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28FB)
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
            "#11P#00316F#40WDamn. Thank goodness we\x01",
            "didn't bring the girls\x01",
            "along.\x02\x03",
            "#00315FThat was way too\x01",
            "uncool...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(250)

    ChrTalk(
        0x101,
        "#6P#00008FRandy...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#11P#00306F#30W...Sorry.\x02\x03",
            "#00308FIt seems I've showed you\x01",
            "my pitiful side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FDon't say things like\x01",
            "that.\x02\x03",
            "#00013FNo matter how you look\x01",
            "at it, they're the\x01",
            "strange ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHehe, but seeing you\x01",
            "that depressed...\x02\x03",
            "#10300FIt looks like they were\x01",
            "right on the mark.\x02",
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
        (
            "#11P#00312F#40WHehe... I hate you\x01",
            "sometimes.\x02",
        )
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
            "#11P#00313F#40W#25ABut you're right.\x02\x03",
            "#50W#30AThey were right on the\x01",
            "mark... And stabbed my\x01",
            "weak spot.\x02",
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
            "After that, Lloyd and the others\x01",
            "declined the car the manager had\x01",
            "arranged and returned home.\x02\x03",
            "They greeted the girls and\x01",
            "Sergei, who were worried about\x01",
            "them...\x02\x03",
            "And, after putting a sleepy KeA\x01",
            "to bed, Lloyd and the others\x01",
            "gave their report.\x02",
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

    def Function_12_2DB6(): pass

    label("Function_12_2DB6")

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
            "#1P#00303F...So that's how it is.\x01",
            "We want permission to\x01",
            "enter.\x02\x03",
            "#00301FKeep it a secret from\x01",
            "Shirley and uncle, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "...Just when I thought I hadn't\x01",
            "seen you for a while, you show\x01",
            "up with some minor business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Hehe, Captain Randolph...\x01",
            "Are you really the fool\x01",
            "the girl says you are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1P#00303F...Stop calling me that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_END)), "loc_30EA")

    ChrTalk(
        0x101,
        (
            "#00001F(This Red Constellation jaeger...\x01",
            "Looks like he's the same one we saw\x01",
            "in front of Crimson & Co. before.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3135")

    label("loc_30EA")


    ChrTalk(
        0x101,
        (
            "#00001F(This Red Constellation\x01",
            "jaeger... Looks like\x01",
            "Randy knows him.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3135")


    ChrTalk(
        0x13,
        "(*g-gulp*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "...Hehe, this is just a\x01",
            "favor. I'll help you\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "But we can't turn a\x01",
            "blind eye to any trouble\x01",
            "you cause inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I won't say a word to the\x01",
            "vice commander or that girl\x01",
            "either. ...That good enough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1P#00303F...That's plenty.\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x10E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x104,
        (
            "#1P#00300FAnd so, the stage is set.\x02\x03",
            "#00300FIt looks like the Mrs. and that guy haven't\x01",
            "come yet. But if we're going to ambush\x01",
            "them, we should enter ahead of them.\x02\x03",
            "#00303FDon't mind if I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it seems best to\x01",
            "go in with a minimum\x01",
            "number of people, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'm going, of course.\x01",
            "Decide amongst yourselves\x01",
            "who's staying behind!\x02",
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

    def lambda_343F():
        TurnDirection(0x101, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_343F)
    Sleep(50)

    def lambda_344F():
        TurnDirection(0x102, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_344F)
    Sleep(50)

    def lambda_345F():
        TurnDirection(0x103, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_345F)
    Sleep(50)

    def lambda_346F():
        TurnDirection(0x109, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_346F)
    Sleep(50)

    def lambda_347F():
        TurnDirection(0x105, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_347F)

    ChrTalk(
        0x109,
        (
            "#10111F(What's gotten into\x01",
            "him?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(Having come this far,\x01",
            "we can't back down now,\x01",
            "but...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10304FHaha, then I wonder if I\x01",
            "can go.\x02\x03",
            "#10300FThe Vice Chief, Lloyd and\x01",
            "myself. Will we be ok\x01",
            "with just those three?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1P#00300FYeah, that'll work.\x02",
    )

    CloseMessageWindow()

    def lambda_359E():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_359E)
    Sleep(50)

    def lambda_35AE():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_35AE)
    Sleep(50)

    def lambda_35BE():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_35BE)

    ChrTalk(
        0x102,
        (
            "#00100FThen, we'll stand by\x01",
            "here.\x02\x03",
            "If anything happens,\x01",
            "contact us via ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, understood.\x02\x03",
            "#00000FAlright then, let's head\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Yes... Let's go,\x01",
            "everyone!!\x02",
        )
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
            "#00000FIf the Mrs. and that guy\x01",
            "come, we'll have them shown\x01",
            "to that seat over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "A-Alright. That'll be\x01",
            "fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If he's some corrupt\x01",
            "real estate agent...\x01",
            "I'll arrest him myself!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1194)

    ChrTalk(
        0x105,
        (
            "#10309FHaha, someone's excited.\x02\x03",
            "#10305FWhoops. Looks like\x01",
            "they're here.\x02",
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

    def lambda_39C7():
        OP_9B(0x0, 0x11, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_39C7)
    Sleep(300)

    def lambda_39DF():
        OP_9B(0x0, 0x12, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_39DF)
    WaitChrThread(0x11, 1)

    def lambda_39F8():
        OP_95(0x11, -2000, 0, -5940, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_39F8)
    WaitChrThread(0x12, 1)

    def lambda_3A16():
        OP_93(0x12, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3A16)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0x10E, 0x1F4)
    OP_6F(0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "Umm, I'm Clyde. I have a\x01",
            "reservation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Right this way, sir.\x02",
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
        (
            "Haha, this is a nice\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Oh, Mrs. Margaret... Is\x01",
            "this your first time\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Because your husband is with the\x01",
            "police, you must have visited a\x01",
            "lot of different places.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x1)

    ChrTalk(
        0x12,
        (
            "Ohoho, you can stop with\x01",
            "the jokes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Just because he's the vice\x01",
            "chief, it doesn't mean his\x01",
            "salary is all that much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "To be perfectly honest, rather than take\x01",
            "me to a restaurant, he'd rather drink\x01",
            "with a hostess at a bar on the outskirts.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    ChrTalk(
        0x11,
        (
            "Haha, well excuse me,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    ChrTalk(
        0x11,
        (
            "Although it is noon, allow me to\x01",
            "put some life into the proceedings\x01",
            "by buying you a drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Haha... Don't mind if I\x01",
            "do.\x02",
        )
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
            "#00012F(V-Vice Chief. Please\x01",
            "don't worry about\x01",
            "this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "(Q-Quiet, you... Don't\x01",
            "you worry about me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "(Hmph. Yes, that's right. This\x01",
            "is such a high class place, I\x01",
            "can't afford it with my salary.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "(Bars in the outskirts\x01",
            "suit me better. And what's\x01",
            "wrong with that...!?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10300F(It's a total\x01",
            "inferiority complex.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-I really wonder if\x01",
            "he's all right...)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-5840, 1500, 14140, 2000)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "Then, let's get down to\x01",
            "business.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Clyde took what appears\x01",
            "to be a contract out of\x01",
            "his briefcase.\x07\x00\x02",
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
            "It's as you've requested. A\x01",
            "contract for the villa in\x01",
            "Michelam residential district.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "If you just sign here,\x01",
            "the residence will be\x01",
            "yours.\x02",
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
            "Hoho... So the time has\x01",
            "finally come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "I'll sign it, of course.\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00001F(As I thought. Looks\x01",
            "like it's a contract for\x01",
            "a Michelam property...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Now then. What do we do?)\x02\x03",
            "#10304F(Even though we did this\x01",
            "infiltration, we heard only a\x01",
            "little more of the story...)\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x13)

    ChrTalk(
        0x13,
        "...I... I...\x02",
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
            "#4SI'll have you stop\x01",
            "deceiving my wife!!\x02",
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
        "What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...Dear!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F(W-Whoa...!?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306F(And, there he goes.)\x02",
    )

    CloseMessageWindow()

    def lambda_4366():
        OP_95(0x101, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4366)
    Sleep(200)

    def lambda_4383():
        OP_95(0x105, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4383)
    WaitChrThread(0x101, 1)

    def lambda_43A1():
        OP_95(0x101, -1590, 0, 11760, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43A1)
    WaitChrThread(0x105, 1)

    def lambda_43BF():
        OP_95(0x105, -1710, 0, 13690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43BF)
    WaitChrThread(0x105, 1)

    def lambda_43DD():
        TurnDirection(0x105, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43DD)
    Sleep(100)
    WaitChrThread(0x101, 1)

    def lambda_43F1():
        TurnDirection(0x101, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43F1)
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
        (
            "Dear... What are you\x01",
            "doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SMargaret!! Cancel the\x01",
            "deal!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SThis corrupt real estate\x01",
            "agent is trying to trick\x01",
            "you!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "Whaaaat!? W-Wait just a\x01",
            "second here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Corrupt...? I haven't\x01",
            "done anything wrong!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SSilence! And cut the\x01",
            "crap!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...Dear...\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SYou deceived my wife with\x01",
            "flattery, and created a\x01",
            "ridiculous loan, didn't you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...Dear...\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SBut, you'll not drop\x01",
            "something like that on\x01",
            "us! Over my dead body!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...Oh, dear...\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SYes, stay quiet! As vice\x01",
            "chief of police...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x1450)

    ChrTalk(
        0x12,
        "#400W#5SS-I-L-E-N-C-E.\x02",
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
        "#2S...I'm sorry.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 500)
    Sleep(50)

    ChrTalk(
        0x101,
        "#00011F(H-He's that weak!?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F(Ahaha, she completely\x01",
            "shut him up.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Goodness... I really\x01",
            "don't know what to do\x01",
            "with people like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You're vice chief of police! How\x01",
            "could you jump to conclusions and\x01",
            "treat this man as a criminal!?\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x12,
        "#4SHave you no shame!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Eek!! I'm sorry! Really\x01",
            "sorry!\x02",
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
        "Wait, I'm wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12, 500)
    Sleep(50)

    ChrTalk(
        0x101,
        "#00011FWhaaaat!!??\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FMadame, would you\x01",
            "explain the full\x01",
            "situation for us?\x02",
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
        "#3P*sigh*... If I must.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PFirst of all, Clyde here is a\x01",
            "respectable real estate agent\x01",
            "that deals in luxury properties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PYou had it wrong right off\x01",
            "the bat. There's no way\x01",
            "he's some corrupt merchant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "B-But, if that's true...\x01",
            "We haven't the mira for\x01",
            "a luxury property...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PActually, I made a large profit\x01",
            "off a new stock offering to\x01",
            "kill time a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PNaturally, an amount\x01",
            "that would take you many\x01",
            "years to save up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "S-Stock!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PTo be quite honest...\x01",
            "You've exhausted my\x01",
            "patience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PEven though you received a position you\x01",
            "shouldn't have due to connections and luck,\x01",
            "you're pitiful and don't do anything at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PI don't know if our home is a hard place to be,\x01",
            "but your night-long drinking whenever you get\x01",
            "the chance really puts a strain on our finances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Ooh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PYou were happy for a while, thinking\x01",
            "you'd be the next chief after the\x01",
            "previous one was thrown out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PBut in the end, another\x01",
            "vice chief ended up\x01",
            "taking the post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PAnd you were so depressed by that\x01",
            "that it's been nothing but complaints\x01",
            "from you this whole time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FM-Mrs... I think\x01",
            "that's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PTo be honest, I think\x01",
            "it's impossible to live\x01",
            "with you any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PThat's why I discussed using my\x01",
            "profits from stock trading to buy\x01",
            "a home for after our separation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PI was planning on living\x01",
            "there awhile, and then filing\x01",
            "for divorce eventually.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        "#4S*crushed*!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FAhaha. She's ruthless.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(B-But he really is\x01",
            "pitiful...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FHuh, but... Didn't you\x01",
            "say "was"...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "...Huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3P...Haha, that's right. After all,\x01",
            "you were worried about me and did\x01",
            "all this for me, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PYou've been nervous and haven't\x01",
            "wanted to come home, but that\x01",
            "was a good performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PCome home this evening,\x01",
            "and let's talk it over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "M-Margaret...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)
    Sleep(50)

    ChrTalk(
        0x12,
        (
            "#3P...And there you have it,\x01",
            "Clyde. I think I'll hold\x01",
            "off on buying the villa.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)
    Sleep(50)

    ChrTalk(
        0x11,
        (
            "#3PT-This can't be! I was\x01",
            "this close...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PIt's just "on hold"\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PIt was wrong of me to negotiate\x01",
            "with you on this alone. I look\x01",
            "forward to our future discussions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PDon't worry. Although we're not\x01",
            "separating, I'm still interested in the\x01",
            "property. I'm sure I'll buy it eventually.\x02",
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
            "#3P*sigh*. If possible, I'd like a\x01",
            "reply before the end of the day,\x01",
            "but... I suppose it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#3PAllow me to excuse\x01",
            "myself, then...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-5570, -600, 15480, 2000)

    def lambda_541B():
        OP_95(0x11, -2680, 0, 14150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_541B)
    Sleep(500)

    def lambda_5438():
        OP_93(0x12, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5438)

    def lambda_5445():
        OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5445)
    Sleep(100)

    def lambda_545D():
        OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_545D)
    Sleep(100)

    def lambda_5475():
        OP_9B(0x1, 0x13, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5475)
    WaitChrThread(0x11, 1)
    OP_6F(0x1)
    Sleep(50)

    def lambda_5493():
        OP_9B(0x0, 0x11, 0x5A, 0x2710, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5493)
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
            "#00001FHmm. So in the end, that\x01",
            "guy wasn't guilty at\x01",
            "all...\x02\x03",
            "#00006FI feel like we've done\x01",
            "something terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, it's fine, right? With this,\x01",
            "it looks like the case between the\x01",
            "Vice Chief and his wife is closed.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 500)
    Sleep(50)

    ChrTalk(
        0x12,
        (
            "#3P...And dear. I'm heading\x01",
            "home for today.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_562F():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_562F)
    Sleep(50)

    def lambda_563F():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_563F)
    Sleep(50)

    def lambda_564F():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_564F)

    ChrTalk(
        0x12,
        (
            "#3PWe have a lot to talk about,\x01",
            "so head straight home once\x01",
            "work's over. ...Understand?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x13,
        "...Y-Yes!!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(...I wonder if he'll be\x01",
            "all right...)\x02",
        )
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

    # Function_12_2DB6 end

    def Function_13_5744(): pass

    label("Function_13_5744")

    Fade(500)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7060, 0, 13990, 90)
    Return()

    # Function_13_5744 end

    def Function_14_5768(): pass

    label("Function_14_5768")

    Fade(500)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7490, 0, 13110, 90)
    Return()

    # Function_14_5768 end

    SaveToFile()

Try(main)
