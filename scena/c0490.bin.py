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
        "Function_12_2E8C",        # 0C, 12
        "Function_13_5851",        # 0D, 13
        "Function_14_5875",        # 0E, 14
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
        "#12P#00001FSo there was a place like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FHmph... Even if it's the business\x01",
            "district, this place is superjock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, it's near the\x01",
            "host club I frequent.\x02\x03",
            "#10300FCome to think of it... Before, this store used\x01",
            "to entertain a lot of congressmen. But lately,\x01",
            "it seems they have a lot of foreign guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#04605FYeah, seems like it.\x02\x03",
            "#04609FBut I got a reservation for you guys\x01",
            "today, so make yourselves at home.\x02\x03",
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
        "#6P#10302FShe just does whatever she wants.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306F...Gareth.\x01",
            "Thanks for lookin' after her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PHa ha, perish the thought.\x02",
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

    def lambda_C20():
        OP_97(0xA, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_C20)
    Sleep(100)

    def lambda_C3D():
        OP_97(0x104, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C3D)
    Sleep(100)

    def lambda_C5A():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C5A)
    Sleep(100)

    def lambda_C77():
        OP_97(0x105, 0x0, 0x0, 0x4E20, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C77)
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
        "Powerful Voice",
        "#3835V#30W──So you've come, Randolph.\x02",
    )

    CloseMessageWindow()
    OP_24(0xEFB)
    OP_C9(0x1, 0x80000000)
    OP_68(-600, 1000, 23500, 2500)
    MoveCamera(321, 17, 0, 2500)
    SetCameraDistance(18000, 2500)
    OP_6F(0x79)
    SetChrFlags(0xA, 0x80)

    def lambda_D5D():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4F4C, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D5D)
    Sleep(100)

    def lambda_D7A():
        OP_96(0xFE, 0x1F4, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D7A)
    Sleep(50)

    def lambda_D97():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x4A38, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D97)
    WaitChrThread(0x105, 1)

    ChrTalk(
        0x104,
        (
            "#6P#00303FUncle... \x01",
            "What's this all of a sudden?\x02\x03",
            "#00301FIt's been two weeks...\x01",
            "But I never got any news.\x02",
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
            "We've been busy with\x01",
            "this and that, you see.\x02\x03",
            "But taking people with you\x01",
            "to a place like this...\x02\x03",
            "Two years ago you\x01",
            "would've never done that.\x02",
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
            "#6P#00306FHmph. Our leader has\x01",
            "a strong sense of duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#N#00003F──Nice to meet you.\x02\x03",
            "#00001FLloyd Bannings, Crossbell\x01",
            "Police Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWazy Hemisphere,\x01",
            "of the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PSigmund Orlando, "Crimson & Co."\x01",
            "representative.\x02\x03",
            "#04500FThanks for going out of your way\x01",
            "to come. Relax and have a drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#N#00003F...We'll take you up on that.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#10302FSpeaking of going out of your way,\x01",
            "how about that old abandoned mine incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#11PHehe, I wonder.\x02\x03",
            "#04504FYou're hungry too, right? \x01",
            "I'll get something for you right away.\x02",
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
            "#04609F*gulp gulp*... \x01",
            "Ah, another parfait, please!\x02",
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
            "#04503F#11PNow then, we have a lot to discuss.\x02\x03",
            "#04500FFirst of all, I'd like to answer\x01",
            "your questions, guests.\x02\x03",
            "You have one in particular, don't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...Yes. \x01",
            "This will save us time.\x02\x03",
            "#00008FI'll be straight with you. Crossbell\x01",
            "Police has taken notice of your actions.\x02\x03",
            "#00013FIn particular── We want to know for\x01",
            "what reason you're staying in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#11PHu hu, how direct.\x02\x03",
            "#04504FWe're here for several\x01",
            "reasons, but...\x02\x03",
            "#04500FOur primary reasons is because\x01",
            "we have undertaken a "contract".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FRegarding that... Is it with\x01",
            "the Imperial government?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHu hu, no comment.\x02\x03",
            "Confidentiality is critical\x01",
            "in our line of work.\x02",
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
            "#6P#10300FThen, what's your relationship with\x01",
            "Captain Lechter of Erebonia?\x02\x03",
            "He helped you acquire the old\x01",
            "Revache building, didn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHehe, that joker, huh.\x02\x03",
            "Being the right-hand man of the "Blood and\x01",
            "Iron", he's a pretty interesting fellow.\x02\x03",
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
            "#5P#00301FUncle... You know\x01",
            "that glasses guy too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04500F#11PWe fought when we were rooting\x01",
            "around "their" turf last year.\x02\x03",
            "Honestly, it was an easy job,\x01",
            "but his troops stood their ground.\x02\x03",
            "#04504FHu hu, to think we'd meet\x01",
            "again in Crossbell City too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04606F*gulp gulp*... But in the\x01",
            "end, we didn't get to\x01",
            "meet the rumored "Yin"...\x02\x03",
            "It seems he was on another job...\x01",
            "We just barely missed each other.\x02\x03",
            "#04600FIf I'm not mistaken, he was\x01",
            "in Crossbell until recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FYeah. After Revache disappeared,\x01",
            "we haven't heard any news about him...\x02\x03",
            "#00301F──Hey, don't change the subject.\x01",
            "We asked about your relationship\x01",
            "with that guy, Lechter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04502F#11PHehe, in other\x01",
            "words, no comment.\x02\x03",
            "Figure out the rest on your own.\x02",
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
            "#00008FBy the way, if you\x01",
            "don't mind me asking...\x02\x03",
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
        "#04505F#11POoh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04602FAhaha. You sure know what\x01",
            "you're looking for, mister.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 9)

    ChrTalk(
        0x105,
        (
            "#6P#10306FI see. So it's an amount that would\x01",
            "elicit that kind of reaction.\x02\x03",
            "#10302FCould it be around 100 million mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PNo comment──\x01",
            "That's all I can say.\x02\x03",
            "#04502FWell, I guess you could\x01",
            "say it's about that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FA contract worth 100 million mira...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FHu hu, how bold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306F...I'm sure it's\x01",
            "for nothing good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04500F#11PHu hu, that's all you're getting for free.\x02\x03",
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
            "#04503F#11P──Randolph. I said it before,\x01",
            "but your vacation's over.\x02\x03",
            "#04501FWe'll have you become the next\x01",
            ""War God" before too long.\x02",
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
        "#5P#00310F#4S......!\x02",
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
            "#6P#10301F"War God"... Isn't it your\x01",
            "late father's nickname?\x02",
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
            "#5P#00307F──Don't fuck with me!\x01",
            "What's with this bullshit!?\x02\x03",
            "Are you drunk out\x01",
            "of your mind!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHu hu, it's simple.\x02\x03",
            "Who must lead the "Red\x01",
            "Constellation" is the "War God".\x02\x03",
            "#04500FAnd, as his only son, you\x01",
            "have a duty to succeed him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FW-Why me...\x02\x03",
            "#00307FIf you need a "War God",\x01",
            "why don't you do it!?\x02\x03",
            "Even Shirley could! There's no\x01",
            "reason it can't be a woman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04503F#11PIn the end, I'm the "Ogre"... I exist\x01",
            "only to run through the battlefield.\x02\x03",
            "I can't be like big bro. Furthermore,\x01",
            "I don't think I want to be like him.\x02\x03",
            "#04500FIt's the same for her... \x01",
            "No, maybe it's even more true for her.\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x2)

    ChrTalk(
        0x9,
        (
            "#12P#04604FYeah. Shirley isn't cut out\x01",
            "for being the "War God".\x02",
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
            "#04503F#11P──I'm sure you understand, Randolph...\x01\x02\x03",
            "Why my big bro decided to settle\x01",
            "the score with a longtime enemy.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_2305():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2305)
    WaitChrThread(0x104, 2)
    Sleep(500)

    ChrTalk(
        0x104,
        "#5P#00308F#40W#2S...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04501F#11PBig bro once gave you a "trial."\x01\x02\x03",
            "Having cleared it, it shows you have the\x01",
            "ability to succeed him as a fine "War God".\x02\x03",
            "#04504F──You must've realized that yourself. I won't hear\x01",
            "that "other people's problems" excuse any longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00311F......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FA "War God" succession trial...\x02",
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
            "#12P#04609FEhehe, he's kind of lame now, but in\x01",
            "the past, Randy bro was totally awesome!\x02\x03",
            "#04602FEspecially when, to crush that "Zephyr"\x01",
            "battalion, he took out that villag──\x02",
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
            "#5P#00313F#30W#4S──Shut up.\x02\x03",
            "#50W#3SI'm beggin' you. Don't say anymore.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    def lambda_25ED():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_25ED)
    WaitChrThread(0x104, 2)
    Sleep(500)

    def lambda_260D():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_260D)
    WaitChrThread(0x104, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F...Randy...\x02",
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
            "#12P#04601FLame... \x01",
            "How shocking.\x02\x03",
            "#04606FBut even so, Shirley looked\x01",
            "up to the old Randy bro.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04504F#11PHehe. \x01",
            "Let's leave it at that.\x02\x03",
            "#04500FWe're going home for tonight, Shirley.\x02",
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

    def lambda_27A5():
        OP_95(0xFE, -2200, 0, 24800, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27A5)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_6F(0x1)
    SetCameraDistance(13500, 15000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        (
            "#11P#04503F#3836V#30WThink hard on what big bro would\x01",
            "think if he saw you like this.\x02\x03",
            "#3837VDecide if you're going to look even more\x01",
            "pitiful before me, if you'll follow me,\x01",
            "run away or if you'll fight against me.\x02\x03",
            "#04502F#3838V#40W───Otherwise, die.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEFE)
    OP_C9(0x1, 0x80000000)
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x101,
        "#00013F...!\x02",
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
            "#04609F#12P#N#3947V#30WHa ha, 'night Randy bro♪\x02\x03",
            "#04602F#3948VYou misters too. Laters!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF6C)
    OP_C9(0x1, 0x80000000)
    OP_68(-700, 1300, 20300, 4000)
    SetCameraDistance(17500, 4000)
    OP_93(0x9, 0x2, 0xBE)

    def lambda_29BB():
        OP_95(0xFE, 2500, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_29BB)
    Sleep(300)

    def lambda_29D8():
        OP_95(0xFE, -2300, 0, 10400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29D8)
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
            "didn't bring the girls along.\x02\x03",
            "#00315F...That was way too uncool...\x02",
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
            "#00308FIt seems I've showed\x01",
            "you my pitiful side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F...Don't say such a thing.\x02\x03",
            "#00013FNo matter how you look at it,\x01",
            "they're the strange ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, but seeing you\x01",
            "that depressed──\x02\x03",
            "#10300FIt looks like they were right on the mark.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#11P#00007FWazy...!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(2375, 255, 100, 0)

    ChrTalk(
        0x104,
        "#11P#00312F#40WHehe... What a jerk.\x02",
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
            "#11P#00313F#40W#25ABut...you're right.\x02\x03",
            "#50W#30AThey were on the mark...\x01",
            "And stabbed my weak spot.\x02",
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
            "──After that, Lloyd and the others\x01",
            "declined the car the manager had\x01",
            "arranged and returned home.\x02\x03",
            "They greeted the girls and Sergei,\x01",
            "who were worried about them...\x02\x03",
            "After putting a sleepy KeA to bed,\x01",
            "Lloyd and the others gave their report.\x02",
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

    def Function_12_2E8C(): pass

    label("Function_12_2E8C")

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
            "We want permission\x01",
            "to enter.\x02\x03",
            "#00301FKeep it secret from uncle\x01",
            "and Shirley, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "...Just when I thought I hadn't seen you for\x01",
            "awhile, you show up with some minor business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Hehe, Captain Randolph...\x01",
            "Are you really the fool\x01",
            "the missus says you are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1P#00303F...Stop calling me that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_END)), "loc_31C1")

    ChrTalk(
        0x101,
        (
            "#00001F(This "Red Constellation" jaeger...\x01",
            "Looks like he's the same one we saw\x01",
            "in front of Crimson & Co. before.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_320C")

    label("loc_31C1")


    ChrTalk(
        0x101,
        (
            "#00001F(This Red Constellation Jaeger...\x01",
            "Looks like Randy knows him.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_320C")


    ChrTalk(
        0x13,
        "(*g-gulp*...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "...Hehe, this is\x01",
            "just a favor. I'll\x01",
            "help you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "But don't cause\x01",
            "any trouble\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "I won't say a word to the\x01",
            "vice leader or the missus\x01",
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
            "#00300FIt looks like the madam and that guy haven't\x01",
            "come yet. But, if we're goin' to ambush them,\x01",
            "we should enter ahead of them.\x02\x03",
            "#00303FDon't mind if I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it's best to keep the number\x01",
            "of personnel to a minimum, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I'm going, of course. Decide amongst\x01",
            "yourselves who's staying behind!\x02",
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

    def lambda_34FB():
        TurnDirection(0x101, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34FB)
    Sleep(50)

    def lambda_350B():
        TurnDirection(0x102, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_350B)
    Sleep(50)

    def lambda_351B():
        TurnDirection(0x103, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_351B)
    Sleep(50)

    def lambda_352B():
        TurnDirection(0x109, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_352B)
    Sleep(50)

    def lambda_353B():
        TurnDirection(0x105, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_353B)

    ChrTalk(
        0x109,
        "#10111F(What's gotten into him?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F(Having come this far, we\x01",
            "can't back down now, but...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, then I wonder if I can go.\x02\x03",
            "#10300FThe Vice Chief, Lloyd and myself.\x01",
            "Will we be ok with just us three?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#1P#00300FYeah, that'll work.\x02",
    )

    CloseMessageWindow()

    def lambda_3658():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3658)
    Sleep(50)

    def lambda_3668():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3668)
    Sleep(50)

    def lambda_3678():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3678)

    ChrTalk(
        0x102,
        (
            "#00100FThen, we'll\x01",
            "standby here.\x02\x03",
            "If anything happens,\x01",
            "contact us via ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, got it.\x02\x03",
            "#00000FAlright then,\x01",
            "let's head inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Hm...l-let's go, everyone!!\x02",
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
            "#00000FIf your wife and that\x01",
            "guy come, we'll guide you\x01",
            "to that seat over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "A-Alright.\x01",
            "That'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If he's some corrupt real estate\x01",
            "agent... I'll arrest him myself!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1194)

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, somehow\x01",
            "I'm thrilled.\x02\x03",
            "#10305FWhoops. \x01",
            "Looks like\x01",
            "they've come.\x02",
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

    def lambda_3A7C():
        OP_9B(0x0, 0x11, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3A7C)
    Sleep(300)

    def lambda_3A94():
        OP_9B(0x0, 0x12, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3A94)
    WaitChrThread(0x11, 1)

    def lambda_3AAD():
        OP_95(0x11, -2000, 0, -5940, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3AAD)
    WaitChrThread(0x12, 1)

    def lambda_3ACB():
        OP_93(0x12, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3ACB)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0x10E, 0x1F4)
    OP_6F(0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "Excuse me, I'm Clyde. \x01",
            "I have a reservation...\x02",
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
        "Hu hu, this is a nice place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Oh, Mrs. Margaret...\x01",
            "Is this your first time here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Because your husband is with the police, you\x01",
            "must have visited a lot of different places...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x1)

    ChrTalk(
        0x12,
        "Oh ho ho, you can stop with the jokes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Just because he's a Vice Chief, it\x01",
            "doesn't mean his salary is all that much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "To be perfectly honest, rather than take\x01",
            "me to a restaurant, he'd drink with a\x01",
            "hostess at a bar on the outskirts.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    ChrTalk(
        0x11,
        "Ha ha, well excuse me, then.\x02",
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
        "Uh uh... I accept.\x02",
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
            "don't worry about this...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "(Q-Quiet, you...\x01",
            "Don't you worry about me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "(Hmph. Yes, that's right.\x01",
            "This is such a high class place\x01",
            "I can't come to with my salary.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "(A bar in the outskirts suits me better.\x01",
            "And what's wrong with that...!)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10300F(It's a total inferiority complex.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(I-It's alright, surely...)\x02",
    )

    CloseMessageWindow()
    OP_68(-5840, 1500, 14140, 2000)
    OP_6F(0x1)
    Sleep(500)

    ChrTalk(
        0x11,
        "Then, let's get down to business.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Clyde took what appears to be a\x01",
            "contract out of his briefcase.\x07\x00\x02",
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
            "It is as you have requested.\x01",
            "A contract for a villa in\x01",
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
            "Ho ho... So the time\x01",
            "has finally come.\x02",
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
            "#00001F(As I thought. Looks like it's a\x01",
            "contract for a Michelam property...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Now then. What do we do?)\x02\x03",
            "#10304F(Even though we did this infiltration,\x01",
            "we heard only a little more of the story...)\x02",
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
        "What...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "...Dear...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F(W-Whoa...!?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10306F(Oh boy.)\x02",
    )

    CloseMessageWindow()

    def lambda_4406():
        OP_95(0x101, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4406)
    Sleep(200)

    def lambda_4423():
        OP_95(0x105, -820, 0, 18700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4423)
    WaitChrThread(0x101, 1)

    def lambda_4441():
        OP_95(0x101, -1590, 0, 11760, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4441)
    WaitChrThread(0x105, 1)

    def lambda_445F():
        OP_95(0x105, -1710, 0, 13690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_445F)
    WaitChrThread(0x105, 1)

    def lambda_447D():
        TurnDirection(0x105, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_447D)
    Sleep(100)
    WaitChrThread(0x101, 1)

    def lambda_4491():
        TurnDirection(0x101, 0x12, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4491)
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
        "Dear... What are you doing here?\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SMargaret!!\x01",
            "Cancel the deal!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0x13,
        (
            "#4SThis corrupt real estate\x01",
            "agent is trying to trick you!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "Whaaaat!? W-Wait\x01",
            "just a second here!\x02",
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
            "#4SEnough, remain silent!\x01",
            "And cut the jokes!\x02",
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
            "#4SYou deceived my wife with flattery, \x01",
            "and tried to have her take a\x01",
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
            "#4SBut, you will not drop something like\x01",
            "that on us! Over my dead body...!\x02",
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
            "#4SEnough, stay quiet!\x01",
            "As a police Vice Chief, I...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x1450)

    ChrTalk(
        0x12,
        "#800W#5SS-I-L-E-N-C-E-.\x02",
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
        "#10309F(Ahaha, she completely shut him up.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Goodness... \x01",
            "I really don't know what\x01",
            "to do with people like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "You're even a police Vice Chief!\x01",
            "How could you jump to a wrong conclusion\x01",
            "and treat this man as a criminal!?\x02",
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
            "Eek!! I'm sorry!\x01",
            "Really sorry!\x02",
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
        "Wait, is it a mistake...?\x02",
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
            "#10300FMadame, would you explain\x01",
            "the full situation for us?\x02",
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
            "#3PFirst of all, Mr. Clyde here is\x01",
            "a respectable real estate agent\x01",
            "who deals in luxury properties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PYou had it wrong right off the bat.\x01",
            "There's no way he's some corrupt agent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "B-But, if that's true... We haven't\x01",
            "the money for a luxury property...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PActually, I made a large profit off\x01",
            "a new stock offering a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PNaturally, an amount that would\x01",
            "take you many years to save up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x13,
        "S-Stock...!?\x02",
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
            "#3PYou were happy for awhile, thinking\x01",
            "you'd be the next Chief after the\x01",
            "previous one was thrown out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PBut in the end, another Vice\x01",
            "Chief ended up taking the post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PAnd you were so depressed by that that it's been\x01",
            "nothing but complaints from you this whole time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012FM-Madam... I think that's...\x02",
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
            "#3PI was planning on living there\x01",
            "for awhile, and then filing\x01",
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
        "#00006F(B-But it's too pitiful...)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FHuh, but... Didn't\x01",
            "you say "was"...?\x02",
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
            "#3P...Uh uh, that's right. After all,\x01",
            "you were worried about me and did\x01",
            "all this for me, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PYou have been so afraid of me that\x01",
            "you have avoided coming home.\x01",
            "Considering how you're, you did good.\x02",
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
            "Mr. Clyde. I think I'll hold\x01",
            "off on buying the villa.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 500)
    Sleep(50)

    ChrTalk(
        0x11,
        (
            "#3PT-This can't be, Mrs. Margaret!\x01",
            "We were just so close...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#3PIt's just on "hold" though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PIt was wrong of me to negotiate\x01",
            "with you on this alone. I look\x01",
            "forward to our future discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#3PDon't worry. Although we're not separating,\x01",
            "I'm still interested in the property. \x01",
            "I'm sure I'll buy it eventually.\x02",
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
            "#3P*sigh*. If possible, I'd have liked a\x01",
            "positive reply before the end of today,\x01",
            "but... I suppose it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#3PAllow me to excuse myself, then...\x02",
    )

    CloseMessageWindow()
    OP_68(-5570, -600, 15480, 2000)

    def lambda_5529():
        OP_95(0x11, -2680, 0, 14150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5529)
    Sleep(500)

    def lambda_5546():
        OP_93(0x12, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5546)

    def lambda_5553():
        OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5553)
    Sleep(100)

    def lambda_556B():
        OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_556B)
    Sleep(100)

    def lambda_5583():
        OP_9B(0x1, 0x13, 0xB4, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5583)
    WaitChrThread(0x11, 1)
    OP_6F(0x1)
    Sleep(50)

    def lambda_55A1():
        OP_9B(0x0, 0x11, 0x5A, 0x2710, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_55A1)
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
            "guy wasn't guilty at all...\x02\x03",
            "#00006FI feel like we've done something terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, it's fine, right? With this,\x01",
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
            "#3P...Well then, dear.\x01",
            "I'm heading home for today.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5745():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5745)
    Sleep(50)

    def lambda_5755():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5755)
    Sleep(50)

    def lambda_5765():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5765)

    ChrTalk(
        0x12,
        (
            "#3PWe have a lot to talk about,\x01",
            "so head straight home tonight.\x01",
            "...Understood?\x02",
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
        "#00006F(...I wonder if he'll be all right...)\x02",
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

    # Function_12_2E8C end

    def Function_13_5851(): pass

    label("Function_13_5851")

    Fade(500)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -7060, 0, 13990, 90)
    Return()

    # Function_13_5851 end

    def Function_14_5875(): pass

    label("Function_14_5875")

    Fade(500)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7490, 0, 13110, 90)
    Return()

    # Function_14_5875 end

    SaveToFile()

Try(main)
