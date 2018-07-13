from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3800.bin",                # FileName
        "e3800",                    # MapName
        "e3800",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3800",                  # 0
        "Ashley",                 # 1
        "Jingo",                  # 2
        "Demon Wald",             # 3
        "Abbas",                  # 4
        "Kientz",                 # 5
        "Veysset",                # 6
        "Luganov",                # 7
        "Jed",                    # 8
        "Huey",                   # 9
        "Slash",                  # 10
        "Kｷki",                  # 11
        "Dino",                   # 12
        "Demon Wald",             # 13
        "SE制御",                 # 14
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(600, 0)                                        # 0

    ScpFunction((
        "Function_0_258",          # 00, 0
        "Function_1_268",          # 01, 1
        "Function_2_269",          # 02, 2
        "Function_3_1BA8",         # 03, 3
        "Function_4_1BDB",         # 04, 4
        "Function_5_1C42",         # 05, 5
        "Function_6_1CF4",         # 06, 6
        "Function_7_1DA6",         # 07, 7
        "Function_8_1E52",         # 08, 8
        "Function_9_1EFD",         # 09, 9
        "Function_10_1FAF",        # 0A, 10
        "Function_11_1FD8",        # 0B, 11
        "Function_12_2001",        # 0C, 12
        "Function_13_202A",        # 0D, 13
        "Function_14_204F",        # 0E, 14
    ))


    def Function_0_258(): pass

    label("Function_0_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_267")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_267")

    Return()

    # Function_0_258 end

    def Function_1_268(): pass

    label("Function_1_268")

    Return()

    # Function_1_268 end

    def Function_2_269(): pass

    label("Function_2_269")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    LoadChrToIndex("chr/ch23900.itc", 0x1E)
    LoadChrToIndex("chr/ch30900.itc", 0x1F)
    LoadChrToIndex("chr/ch31800.itc", 0x20)
    LoadChrToIndex("chr/ch06800.itc", 0x21)
    LoadChrToIndex("chr/ch09200.itc", 0x23)
    LoadChrToIndex("apl/ch51512.itc", 0x24)
    LoadChrToIndex("chr/ch06700.itc", 0x28)
    LoadChrToIndex("apl/ch51511.itc", 0x29)
    LoadChrToIndex("chr/ch30800.itc", 0x2D)
    LoadChrToIndex("chr/ch31700.itc", 0x2E)
    LoadChrToIndex("apl/ch51510.itc", 0x2F)
    LoadEffect(0x0, "battle/ms00000.eff")
    LoadEffect(0x1, "event/ev15030.eff")
    LoadEffect(0x2, "battle/bs880000.eff")
    LoadEffect(0x3, "event/ev14006.eff")
    LoadEffect(0x4, "battle/ms00064.eff")
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(868)
    SoundLoad(825)
    SoundLoad(3576)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0x11, 0x2D)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x2D)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0xF, 0x2E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x2E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_A7(0x14, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0xA, 0xA)
    OP_49()
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_68(32970, -4310, -31970, 0)
    MoveCamera(32, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29000, 0)
    MoveCamera(35, 35, 0, 5000)
    SetCameraDistance(33000, 5000)
    Sound(868, 2, 80, 0)
    BeginChrThread(0x15, 1, 0, 14)
    BeginChrThread(0xA, 0, 0, 13)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-13550, 1000, -13650, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(34500, 0)
    OP_68(-13550, 1000, -13650, 5000)
    MoveCamera(40, 30, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(36500, 5000)
    OP_0D()
    OP_6F(0x79)
    Sound(834, 0, 100, 0)
    EndChrThread(0xA, 0x0)
    Fade(500)
    OP_68(4000, 6500, -26500, 0)
    MoveCamera(45, -5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_68(4000, 3250, -26500, 500)
    MoveCamera(45, 30, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(21000, 500)
    SetChrPos(0xA, 4470, 5400, -26160, 225)
    OP_D5(0xA, 0x0, 0x36EE8, 0x0, 0x0)
    SetChrPos(0x14, 4470, 4900, -26160, 0)
    OP_71(0xA, 0x145, 0x154, 0x1, 0x8)
    OP_9D(0xA, 0x1176, 0x578, 0xFFFF99D0, 0x3E8, 0x2710)
    OP_82(0xC8, 0x0, 0xBB8, 0x5DC)
    Sound(833, 0, 100, 0)
    Sound(196, 0, 100, 0)
    Sound(880, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(1000)
    OP_79(0xA)
    OP_6F(0x79)
    Sleep(1000)
    OP_68(4000, 5250, -26500, 1000)
    MoveCamera(45, 25, 0, 1000)
    OP_71(0xA, 0x155, 0x168, 0x1, 0x8)
    OP_79(0xA)
    OP_0D()
    OP_6F(0x79)
    OP_74(0xA, 0x14)
    OP_71(0xA, 0x4B0, 0x500, 0x1, 0x8)
    SetCameraDistance(19000, 3500)
    OP_68(4000, 5450, -26500, 3500)
    MoveCamera(65, 25, 0, 1500)
    OP_6F(0x40)
    MoveCamera(25, 20, 5, 2000)
    OP_6F(0x79)
    OP_79(0xA)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    Sound(3573, 255, 100, 0)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#30W#NEh eh eh...\x01",
            "...Ain't this a nice spectacle...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#30W#NAn "offering" to keep gettin'\x01",
            "stronger from now on too...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#4S#NGwah ha ha...\x01",
            "Not a bad advice...!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18000, 1300)
    OP_68(4000, 4250, -26500, 1300)
    MoveCamera(25, 30, 5, 1300)
    Sound(892, 0, 100, 0)
    OP_71(0xA, 0x104, 0x122, 0x1, 0x8)
    OP_79(0xA)
    OP_6F(0x79)
    Sound(833, 0, 100, 0)
    Sound(251, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    MoveCamera(25, -10, 5, 300)
    OP_68(4000, 5250, -26500, 300)
    OP_71(0xA, 0x123, 0x12C, 0x1, 0x8)
    OP_9D(0xA, 0x1176, 0x3C28, 0xFFFF99D0, 0x3A98, 0x1F40)
    Fade(500)
    OP_68(50000, 72500, 50000, 0)
    MoveCamera(45, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(110000, 0)
    OP_F0(0x0, 0x1)
    OP_68(50000, 82500, 50000, 1500)
    MoveCamera(45, -10, 0, 1500)
    Sound(834, 0, 100, 0)
    SetChrPos(0xA, 45000, 20000, 45000, 225)
    OP_D5(0xA, 0x0, 0x36EE8, 0x0, 0x0)
    OP_9D(0xA, 0x2710, 0x11170, 0x2710, 0xC544, 0x1388)
    OP_71(0xA, 0x140, 0x145, 0x1, 0x8)

    def lambda_950():
        OP_96(0xFE, 0xFFFF3CB0, 0xAFC8, 0xFFFF3CB0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_950)
    Sound(990, 0, 100, 0)
    Sleep(800)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sleep(500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0xA, 0x1)
    SetChrPos(0xA, 12450, 20500, -23000, 70)
    OP_D5(0xA, 0x0, 0x11170, 0x0, 0x0)
    OP_68(12450, 26700, -23000, 0)
    MoveCamera(60, 40, -10, 0)
    OP_6E(500, 0)
    SetCameraDistance(15500, 0)
    OP_68(26730, 8700, -18670, 500)
    MoveCamera(30, 30, -10, 500)
    SetCameraDistance(28000, 500)
    SetChrPos(0xA, 12450, 20500, -23000, 70)
    OP_96(0xA, 0x55F0, 0x157C, 0xFFFFB3D4, 0x9C40, 0x0)
    Sound(196, 0, 100, 0)
    Sound(876, 0, 100, 0)
    Sound(3549, 255, 100, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    PlayEffect(0x4, 0xFF, 0xA, 0x5, 0, 4500, 1500, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_6F(0x79)
    OP_68(31150, 2500, -15500, 500)
    MoveCamera(45, 20, 0, 500)
    SetCameraDistance(23000, 500)
    Sound(200, 0, 100, 0)
    Sound(880, 0, 100, 0)

    def lambda_AE1():
        OP_96(0xFE, 0x79AE, 0xFFFFFE0C, 0xFFFFC374, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AE1)
    OP_71(0xA, 0x145, 0x154, 0x1, 0x8)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x5DC)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sound(833, 0, 100, 0)
    OP_71(0x9, 0x0, 0x3C, 0x0, 0x8)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 30000, 0, -14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_79(0x9)
    OP_0D()
    OP_6F(0x79)
    OP_68(31150, 3500, -15500, 1500)
    MoveCamera(30, 30, 10, 1500)
    SetCameraDistance(20000, 1500)
    SetChrPos(0x14, 31150, 3500, -15500, 0)
    Sound(892, 0, 100, 0)

    def lambda_BB4():
        OP_D5(0xFE, 0x0, 0x2BF20, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BB4)
    OP_71(0xA, 0x154, 0x168, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)
    Sleep(500)
    BeginChrThread(0xA, 0, 0, 4)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3576V#5P#N#4S#40AEh eh eh...\x01",
            "#5SGwah ha ha ha ha ha ha ha ha ha!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDF8)
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0xA, 0)
    SetChrPos(0xE, 41750, -2500, -22700, 270)
    SetChrPos(0x11, 40100, -2500, -24600, 315)
    SetChrPos(0x10, 41450, -2500, -24450, 315)
    SetChrPos(0xF, 40950, -2500, -21550, 270)
    SetChrPos(0x12, 43350, -2500, -22000, 270)
    SetChrPos(0x13, 49950, -2100, -22500, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(
        0x11,
        "Voice",
        "T-The hell is that!?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(41000, 0, -22050, 0)
    MoveCamera(22, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(39150, -700, -22050, 2000)
    MoveCamera(13, 15, 0, 2000)
    SetCameraDistance(16000, 2000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x11,
        "#12PA r-run down apartment...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "It's totally crashhhhhhed!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "What's that monster...!?\x02",
    )

    CloseMessageWindow()
    OP_68(37000, 1000, -22150, 2000)
    MoveCamera(345, 5, 0, 2000)
    SetCameraDistance(17500, 2000)
    Sleep(1000)
    Fade(250)

    def lambda_DD6():
        OP_D5(0xFE, 0x0, 0x20F58, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_DD6)
    OP_71(0xA, 0x277, 0x280, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#NHa ha...\x01",
            "Came just at the right moment, huh?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_71(0xA, 0x104, 0x122, 0x1, 0x8)
    OP_79(0xA)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    OP_68(38750, 700, -23450, 3000)
    MoveCamera(50, 35, 0, 3000)
    SetCameraDistance(11000, 3000)

    def lambda_EA8():

        label("loc_EA8")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_EA8")

    QueueWorkItem2(0xE, 2, lambda_EA8)

    def lambda_EBA():

        label("loc_EBA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_EBA")

    QueueWorkItem2(0x11, 2, lambda_EBA)

    def lambda_ECC():

        label("loc_ECC")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_ECC")

    QueueWorkItem2(0x10, 2, lambda_ECC)

    def lambda_EDE():

        label("loc_EDE")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_EDE")

    QueueWorkItem2(0xF, 2, lambda_EDE)

    def lambda_EF0():

        label("loc_EF0")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_EF0")

    QueueWorkItem2(0x12, 2, lambda_EF0)
    Sound(833, 0, 70, 0)
    Sound(251, 0, 100, 0)

    def lambda_F0E():
        OP_9D(0xFE, 0x8D68, 0xFFFFF63C, 0xFFFFA81C, 0x2710, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F0E)
    OP_71(0xA, 0x122, 0x154, 0x1, 0x8)
    WaitChrThread(0xA, 1)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sound(833, 0, 100, 0)
    Sound(196, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    EndChrThread(0xE, 0x2)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x10, 0x2)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x12, 0x2)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x12, 0x20)

    def lambda_F96():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F96)
    Sleep(50)

    def lambda_FAE():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_FAE)
    Sleep(50)

    def lambda_FC6():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_FC6)
    Sleep(50)

    def lambda_FDE():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_FDE)
    Sleep(50)

    def lambda_FF6():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_FF6)
    OP_79(0xA)
    Sleep(500)
    SetChrPos(0x14, 36200, -2500, -22500, 0)

    def lambda_1022():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1022)
    OP_71(0xA, 0x154, 0x168, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x12, 1)

    ChrTalk(
        0x10,
        "Uwhoo...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "Uwaaah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#NEh eh...you'll become\x01",
            "sacrifices for me here...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#NYou, the weaknesses of my past...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#NThe symbol of the "unnecessary\x01",
            "things" I must protect, huuh...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xE,
        "Huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "N-No way...\x01",
            "Mr. Wa──\x02",
        )
    )

    CloseMessageWindow()
    Sound(892, 0, 100, 0)
    OP_71(0xA, 0x82, 0x8C, 0x1, 0x8)
    OP_79(0xA)
    Sleep(500)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#5S#N#10AHAAAAAAAAAAAH!!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(253, 0, 100, 0)
    Sound(893, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_74(0xA, 0xF)
    OP_71(0xA, 0x96, 0x9B, 0x1, 0x8)
    PlayEffect(0x2, 0xFF, 0xA, 0x5, 0, -6000, 0, 180, 160, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    ChrTalk(
        0xE,
        "#11P#10ANOOOoooh...!!\x02",
    )

    OP_68(41120, 800, -23590, 1000)
    MoveCamera(52, 23, 0, 1000)
    SetCameraDistance(19000, 1000)
    Sound(833, 0, 100, 0)
    Sound(545, 0, 100, 0)
    BeginChrThread(0x11, 3, 0, 5)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 6)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 8)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 9)
    Sleep(300)
    Sound(880, 0, 100, 0)
    Sound(288, 0, 100, 0)
    Sound(876, 0, 100, 0)
    Sound(116, 0, 100, 0)
    OP_71(0x3, 0x0, 0x14, 0x1, 0x8)
    OP_79(0xA)
    CancelBlur(500)
    WaitChrThread(0xE, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x12, 3)
    Sleep(300)

    ChrTalk(
        0xF,
        "#12A#60W#2S...uh...ah......\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x10,
        "#12A#60W#2S............(*twitch twitch*)\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    NpcTalk(
        0x13,
        "Young Boy's Voice",
        "#1PS-Seniors!?\x02",
    )

    CloseMessageWindow()
    OP_68(47600, -1100, -22500, 1000)
    MoveCamera(55, 30, 0, 1000)
    OP_6E(500, 1000)
    SetCameraDistance(20000, 1000)

    def lambda_138C():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_138C)

    def lambda_13A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_13A1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x13, 3)
    TurnDirection(0x13, 0xF, 500)
    Sleep(300)
    TurnDirection(0x13, 0xE, 500)
    Sleep(300)
    TurnDirection(0x13, 0x11, 500)
    Sleep(300)
    TurnDirection(0x13, 0x10, 500)
    Sleep(300)
    TurnDirection(0x13, 0x12, 500)

    ChrTalk(
        0x13,
        "Everyone!? Mr. Kｷki!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Please, h-hang in there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#60W#2S...It's...useless...\x01",
            "At least you...get aw...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W#NEh eh...you were here too...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    OP_68(43180, -600, -22820, 1500)
    MoveCamera(65, 24, 0, 1500)
    SetCameraDistance(19750, 1500)

    def lambda_14EB():
        OP_A6(0xFE, 0x0, 0x14, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_14EB)
    OP_93(0x13, 0x10E, 0x64)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x13,
        (
            "EEEEK!?\x01",
            "A m-monster──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W#NPerfect...\x01",
            "...You too...with my hands...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0xB,
        "Low Voice",
        "──That's enough.\x02",
    )

    CloseMessageWindow()
    OP_64(0x13)
    Fade(500)
    SetChrPos(0xB, 24800, -2500, -22000, 90)
    SetChrPos(0x8, 24200, -2500, -23850, 90)
    SetChrPos(0x9, 23000, -2500, -23450, 90)
    SetChrPos(0xC, 23450, -2500, -21500, 90)
    SetChrPos(0xD, 22100, -2500, -22150, 90)
    OP_68(25350, -400, -23090, 0)
    MoveCamera(50, 3, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(14000, 1000)
    OP_D5(0xA, 0x0, 0x33450, 0x0, 0x0)

    def lambda_1646():
        OP_D5(0xFE, 0x0, 0x41EB0, 0x0, 0x2EE)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1646)
    OP_74(0xA, 0x14)
    OP_71(0xA, 0x277, 0x280, 0x1, 0x8)
    OP_79(0xA)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    WaitChrThread(0xA, 2)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#6POoh, that's huge, huh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6PT-The heck is that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#6PA demon...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#04100F......You, extinguish the\x01",
            "fire in the environs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6PU-Understood...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PJingo, make the people\x01",
            "around here take refuge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#6PYes, I'm on it.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 3, 0, 10)
    BeginChrThread(0xC, 3, 0, 11)
    BeginChrThread(0xD, 3, 0, 12)
    Sleep(300)
    OP_68(31950, -100, -23600, 3000)
    MoveCamera(320, 23, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18500, 3000)

    def lambda_17C6():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17C6)
    Sleep(200)

    def lambda_17DE():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_17DE)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    SetMessageWindowPos(300, 140, -1, -1)

    AnonymousTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W#NBaldy and the weapons dealer...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#30W#NEh eh...will you show\x01",
            "me "power" too...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xB,
        "#04100F#5P──If you so desire.\x02",
    )

    CloseMessageWindow()
    OP_68(25250, -1500, -21850, 1500)
    MoveCamera(315, 25, 0, 1500)
    SetCameraDistance(15500, 1500)
    Sleep(1000)
    Sound(534, 0, 50, 0)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x29)
    OP_A0(0xB, 1500, 0x0, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#04100F#5PI have Wazy's permission, so I'll\x01",
            "fight you as much as you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PMy my, using guns directly\x01",
            "is not in my style, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_68(24580, -1500, -22730, 800)
    MoveCamera(315, 25, 0, 800)
    OP_6E(600, 800)
    SetCameraDistance(15500, 800)
    Sleep(300)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)
    OP_A0(0x8, 1500, 0x0, 0x2)
    Sound(531, 0, 70, 0)
    Sound(358, 0, 70, 0)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PI'll have to make you pay compensation\x01",
            "for having done whatever you want near\x01",
            "my shop, you know?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 140, -1, -1)

    AnonymousTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#30W#NEh eh eh...fine.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(32500, 0, -22700, 2500)
    MoveCamera(315, 20, 0, 2500)
    SetCameraDistance(14000, 2500)
    Sleep(2000)
    Sound(893, 0, 100, 0)
    Sound(892, 0, 100, 0)
    Sound(825, 2, 100, 0)
    Sound(195, 0, 100, 0)
    Sound(212, 0, 100, 0)
    OP_71(0xA, 0xD3, 0xE1, 0x1, 0x8)
    PlayEffect(0x3, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_79(0xA)
    BeginChrThread(0xA, 3, 0, 3)
    SetMessageWindowPos(300, 150, -1, -1)

    AnonymousTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#30W#NSavor aplenty to the marrow\x01",
            "of your bones...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#5S#NWald Wales' "poweeeeeeeeer"!!\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopSound(825, 1000, 90)
    StopSound(868, 1000, 70)
    SetCameraDistance(16500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_269 end

    def Function_3_1BA8(): pass

    label("Function_3_1BA8")

    OP_74(0xA, 0x5)

    label("loc_1BAC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BDA")
    OP_71(0xA, 0xE1, 0xDF, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0xDF, 0xE1, 0x1, 0x8)
    OP_79(0xA)
    Jump("loc_1BAC")

    label("loc_1BDA")

    Return()

    # Function_3_1BA8 end

    def Function_4_1BDB(): pass

    label("Function_4_1BDB")

    OP_82(0x14, 0x14, 0xBB8, 0x7D0)
    Sleep(1500)
    OP_74(0xA, 0x14)
    OP_71(0xA, 0x5B, 0x64, 0x1, 0x8)
    OP_79(0xA)
    OP_71(0xA, 0x65, 0x78, 0x1, 0x20)
    OP_82(0x64, 0x64, 0xBB8, 0xCE4)
    Sleep(3000)
    OP_71(0xA, 0x79, 0x82, 0x1, 0x8)
    OP_79(0xA)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0xB, 0x32, 0x1, 0x20)
    Return()

    # Function_4_1BDB end

    def Function_5_1C42(): pass

    label("Function_5_1C42")

    OP_93(0x11, 0x0, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0x11, 0xA122, 0xFFFFFB1E, 0xFFFF8EEA, 0x9C4, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0x11, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0x11, 0xA122, 0xFFFFFA24, 0xFFFF8EEA, 0x1D4C, 0x0)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x2F)
    SetChrSubChip(0x11, 0x2)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_1C42 end

    def Function_6_1CF4(): pass

    label("Function_6_1CF4")

    OP_93(0x10, 0x13B, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0x10, 0xBD42, 0x0, 0xFFFF98AE, 0xDAC, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(815, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0x10, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0x10, 0xB7CA, 0xFFFFFBE6, 0xFFFF9494, 0x1D4C, 0x0)
    SetChrChipByIndex(0x10, 0x2F)
    SetChrSubChip(0x10, 0x3)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    Return()

    # Function_6_1CF4 end

    def Function_7_1DA6(): pass

    label("Function_7_1DA6")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0x12, 0xBDD8, 0xFFFFFA24, 0xFFFFA4FC, 0x7D0, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(501, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0x12, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0x12, 0xB95A, 0xFFFFF7CC, 0xFFFFA402, 0x1D4C, 0x0)
    OP_93(0x12, 0x5A, 0x0)
    SetChrChipByIndex(0x12, 0x2F)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_1DA6 end

    def Function_8_1E52(): pass

    label("Function_8_1E52")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xE, 0xB9F0, 0x1F4, 0xFFFFBC08, 0xFA0, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(815, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0xE, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0xE, 0xB734, 0xFFFFFF38, 0xFFFFB758, 0x1D4C, 0x0)
    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xE, 0x2)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    Return()

    # Function_8_1E52 end

    def Function_9_1EFD(): pass

    label("Function_9_1EFD")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xF, 0xAB18, 0xFFFFFE0C, 0xFFFFBD02, 0xBB8, 0x1D4C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(196, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    OP_A6(0xF, 0x0, 0x32, 0x12C, 0xBB8)
    OP_96(0xF, 0xA8F2, 0xFFFFF63C, 0xFFFFB820, 0x1D4C, 0x0)
    OP_93(0xF, 0x2D, 0x0)
    SetChrChipByIndex(0xF, 0x2F)
    SetChrSubChip(0xF, 0x1)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    Return()

    # Function_9_1EFD end

    def Function_10_1FAF(): pass

    label("Function_10_1FAF")

    OP_95(0x9, 21960, -2500, -25110, 4000, 0x0)
    OP_95(0x9, 21890, -6130, -34350, 4000, 0x0)
    Return()

    # Function_10_1FAF end

    def Function_11_1FD8(): pass

    label("Function_11_1FD8")

    OP_95(0xC, 21870, -2500, -25020, 4000, 0x0)
    OP_95(0xC, 21270, -6030, -34120, 4000, 0x0)
    Return()

    # Function_11_1FD8 end

    def Function_12_2001(): pass

    label("Function_12_2001")

    OP_95(0xD, 19770, -2500, -21590, 4000, 0x0)
    OP_95(0xD, 13770, -1130, -16129, 4000, 0x0)
    Return()

    # Function_12_2001 end

    def Function_13_202A(): pass

    label("Function_13_202A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_204E")
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1000)
    Jump("Function_13_202A")

    label("loc_204E")

    Return()

    # Function_13_202A end

    def Function_14_204F(): pass

    label("Function_14_204F")

    Sleep(500)
    Sound(891, 0, 100, 0)
    Sleep(2000)
    Sound(880, 0, 100, 0)
    Sound(200, 0, 60, 0)
    Sleep(2000)
    Sound(880, 0, 100, 0)
    Sound(200, 0, 50, 0)
    Sleep(1500)
    Sound(880, 0, 100, 0)
    Sound(833, 0, 60, 0)
    Sleep(2000)
    Sound(880, 0, 100, 0)
    Sound(200, 0, 60, 0)
    Return()

    # Function_14_204F end

    SaveToFile()

Try(main)
