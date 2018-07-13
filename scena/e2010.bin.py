from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e2010.bin",                # FileName
        "e2010",                    # MapName
        "e2010",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e2010",                  # 0
        "Chief Sergei",           # 1
        "Scenery",                # 2
        "Yuri",                   # 3
        "Sykes",                  # 4
        "Reggie",                 # 5
        "Minneth",                # 6
        "Black Clothes",          # 7
        "Black Clothes",          # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(440, 0)                                        # 0

    ScpFunction((
        "Function_0_1B8",          # 00, 0
        "Function_1_2C1",          # 01, 1
        "Function_2_327",          # 02, 2
        "Function_3_34C",          # 03, 3
        "Function_4_7E7",          # 04, 4
        "Function_5_BFF",          # 05, 5
        "Function_6_1257",         # 06, 6
        "Function_7_1984",         # 07, 7
        "Function_8_2A11",         # 08, 8
        "Function_9_3686",         # 09, 9
        "Function_10_3B14",        # 0A, 10
        "Function_11_3EF2",        # 0B, 11
        "Function_12_4D91",        # 0C, 12
        "Function_13_6EB6",        # 0D, 13
        "Function_14_721C",        # 0E, 14
        "Function_15_73D5",        # 0F, 15
        "Function_16_750E",        # 10, 16
    ))


    def Function_0_1B8(): pass

    label("Function_0_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1CF")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 3)
    Jump("loc_2C0")

    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1E3")
    ClearScenarioFlags(0x22, 1)
    Event(0, 4)
    Jump("loc_2C0")

    label("loc_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1F7")
    ClearScenarioFlags(0x22, 2)
    Event(0, 5)
    Jump("loc_2C0")

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_20B")
    ClearScenarioFlags(0x22, 3)
    Event(0, 6)
    Jump("loc_2C0")

    label("loc_20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_21F")
    ClearScenarioFlags(0x22, 4)
    Event(0, 7)
    Jump("loc_2C0")

    label("loc_21F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_233")
    ClearScenarioFlags(0x22, 5)
    Event(0, 8)
    Jump("loc_2C0")

    label("loc_233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_24A")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 2)
    Event(0, 9)
    Jump("loc_2C0")

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_261")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x0, 3)
    Event(0, 10)
    Jump("loc_2C0")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_275")
    ClearScenarioFlags(0x23, 0)
    Event(0, 11)
    Jump("loc_2C0")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_289")
    ClearScenarioFlags(0x23, 1)
    Event(0, 12)
    Jump("loc_2C0")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_29D")
    ClearScenarioFlags(0x23, 3)
    Event(0, 13)
    Jump("loc_2C0")

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_2B1")
    ClearScenarioFlags(0x23, 4)
    Event(0, 14)
    Jump("loc_2C0")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_2C0")
    ClearScenarioFlags(0x23, 6)
    Event(0, 16)

    label("loc_2C0")

    Return()

    # Function_0_1B8 end

    def Function_1_2C1(): pass

    label("Function_1_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_326")

    label("loc_2DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 2)
    Jump("loc_326")

    label("loc_2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)
    Jump("loc_326")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_326")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_326")

    Return()

    # Function_1_2C1 end

    def Function_2_327(): pass

    label("Function_2_327")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_2_327")

    label("loc_34B")

    Return()

    # Function_2_327 end

    def Function_3_34C(): pass

    label("Function_3_34C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x8000000)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(-1110, 500, 3290, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14280, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 1200, 100, -1900, 180)
    SetChrPos(0x102, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x105, 1200, 100, -400, 180)
    SetChrPos(0x8, 200, 100, 1000, 180)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x3C, 0x3E8)
    FadeToBright(1000, 0)
    OP_68(-570, 500, 500, 3000)
    MoveCamera(323, 22, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14280, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#10109F#11P*haah*, I love a new car smell...\x02\x03",
            "#10102FAnd the wheel turns like butter. \x01",
            "What an amazing car!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PThe seats are comfy and the\x01",
            "design inside isn't bad either.\x02\x03",
            "#10302FHu hu, I'm sold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PHa ha...\x01",
            "It really does seem a good car.\x02\x03",
            "#00002FNot to mention the fact that we can\x01",
            "fit about eight people comfortably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5P*giggle*, so we'll be fine even\x01",
            "when Tio and Randy get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11POk, let's head out.\x02\x03",
            "#01002FLet's save our final judgements\x01",
            "until after we test it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F#11PRight, let's go then!\x02",
    )

    CloseMessageWindow()
    Sound(470, 0, 100, 0)
    OP_82(0xF, 0x23, 0xBB8, 0x1F4)
    Sleep(500)
    Sound(460, 2, 80, 0)
    BeginChrThread(0x101, 3, 0, 2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    StopSound(460, 1000, 80)
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("t6000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_34C end

    def Function_4_7E7(): pass

    label("Function_4_7E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(-720, 500, 200, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 1200, 100, -1900, 180)
    SetChrPos(0x102, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x105, 1200, 100, -400, 180)
    SetChrPos(0x8, 200, 100, 1000, 180)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x109,
        "#10109F#5P.........♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#12PThis is heavenly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PYes. It's quite fast,\x01",
            "but it also feels so safe...\x02\x03",
            "#00102FAnd I can hardly hear the engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#12PI don't feel many\x01",
            "bumps either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01004F#11PThat's ZCF for you.\x02\x03",
            "#01002FI'd like to try taking\x01",
            "her for a spin sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#5P*haah*, I like the CGF's\x01",
            "armored vehicles too, but...\x02\x03",
            "#10106FIt feels a bit like I'm\x01",
            "being unfaithful to them...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    ChrTalk(
        0x101,
        "#00012F#12PHa ha, is that how it is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#12PHu hu, you're a real car\x01",
            "maniac, aren't you Noｱl?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r4000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_7E7 end

    def Function_5_BFF(): pass

    label("Function_5_BFF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(99290, 600, 1470, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14280, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 98950, 150, 1900, 0)
    SetChrPos(0x102, 101000, 150, 250, 0)
    SetChrPos(0x109, 101000, 150, 1800, 0)
    SetChrPos(0x105, 98950, 150, 250, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 300, 100, 1100, 180)
    SetChrPos(0x8, 100000, 150, -1350, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13280, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    Sleep(300)

    ChrTalk(
        0x8,
        "#01003F#6P──A big red-haired man with one eye?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#5PYeah... We've already\x01",
            "contacted Section One.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, we have no idea who he is, \x01",
            "but he's definitely not an ordinary guy.\x02\x03",
            "#10301FI get the feeling that he's even\x01",
            "stronger than what he let us see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01001F#6P...Therein lies the problem.\x02\x03",
            "#01003FTerrorists and jaegers tend to\x01",
            "hide their own battle strength.\x02\x03",
            "#01000FEven if we come across them in Crossbell directly,\x01",
            "we don't have any laws to investigate them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5PYou're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#12PNot to mention the strange behavior we've\x01",
            "seen in Heiyue and the Imperial government.\x02\x03",
            "#00101FFrom the shadows, something seems to be starting in\x01",
            "the void created by the disappearance of Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#01006F#6P"From the shadows" might\x01",
            "be a bit too blunt.\x02\x03",
            "#01000FAnd there's that Trade Conference\x01",
            "at the end of the month.\x02\x03",
            "You guys are about to get really busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PRight. We're prepared for that.\x02\x03",
            "#00001F...But for now, I think it's imperative\x01",
            "we look into that guy's background.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12PYeah... I wonder\x01",
            "where is he staying?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(12780, 2000)
    OP_6F(0x79)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_BFF end

    def Function_6_1257(): pass

    label("Function_6_1257")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(-720, 500, 200, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
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
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, 1200, 100, -1900, 180)
    SetChrPos(0x101, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x104, 1200, 100, -400, 180)
    SetChrPos(0x105, 0, 100, 1000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sound(2367, 255, 80, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 4)), scpexpr(EXPR_END)), "loc_1489")

    ChrTalk(
        0x104,
        (
            "#00309F#11PI thought this on the way here\x01",
            "too, but what a great car!\x02\x03",
            "#00302FDon't you think I'd be a real\x01",
            "lady killer if this was my car?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F8")

    label("loc_1489")


    ChrTalk(
        0x104,
        (
            "#00309F#11PStill, what a great car!\x02\x03",
            "#00302FDon't you think I'd be a real\x01",
            "lady killer if this was my car?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F8")

    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00012F#5PNow look here...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#10302F#5PHu hu, you still have a ways to go if you're\x01",
            "relying on an "assistant", don't you think?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00301F#11PTch. Actin' so arrogant\x01",
            "even though you're younger.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00109F#6P*giggle*...\x01",
            "The odds are against you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5PCompared to Wazy, senior Randy doesn't even\x01",
            "come close when it comes to the ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#11PCome on Noｱl! We're both from\x01",
            "the CGF! Don't be cold-hearted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#5PUh uh, sorry.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 4)), scpexpr(EXPR_END)), "loc_18C9")

    ChrTalk(
        0x101,
        (
            "#00005F#5POh yeah, Randy.\x02\x03",
            "#00000FYou received a spare key\x01",
            "from the Chief, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PWhen did you learn how\x01",
            "to drive an orbal car?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11POh, it was during\x01",
            "my recent training.\x02\x03",
            "#00300FYou should all learn too. It's a\x01",
            "useful skill to have, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PHa ha, that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#6PThere's no downside to learning. \x01",
            "We might find it handy in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PHmm, if given the choice, I'd\x01",
            "prefer to be driven than to learn.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C9")

    Sleep(150)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10101F#11PAh...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)
    SetCameraDistance(15000, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1257 end

    def Function_7_1984(): pass

    label("Function_7_1984")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(150500, 700, 250, 0)
    MoveCamera(307, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14270, 0)
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
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 150400, 100, -1100, 90)
    SetChrPos(0x102, 151900, 100, 900, 90)
    SetChrPos(0x109, 151900, 100, -1100, 90)
    SetChrPos(0x105, 148800, 100, -100, 90)
    SetChrPos(0x104, 150400, 100, 900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    SetCameraDistance(13770, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00008F#5P...I wonder who could\x01",
            "have done such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PI think it would be quite\x01",
            "strange if they had no motive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#6PThose explosives too... \x01",
            "Where did they get them from?\x02\x03",
            "It's something not often\x01",
            "used even by the CGF...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PCould it have been a blasting charge\x01",
            "that was laying around in the old mine?\x02\x03",
            "#10300FWell, I don't have much knowledge on explosives,\x01",
            "so I can only guess at what it could be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#5PNo, that's not it.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10305F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PDo you know something?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00301F#11PBased on the smell of the gunpowder\x01",
            "smoke near the entrance...\x02\x03",
            "It was a new model explosive\x01",
            "from around 1-2 years ago.\x02\x03",
            "A rather high-performance one at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PI-Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#6PBut, I'm surprised you're so well versed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#11PIt's not like gunpowder weapons\x01",
            "are completely obsolete.\x02\x03",
            "The regular army doesn't use them often,\x01",
            "but even now, some people prefer 'em.\x02\x03",
            "#00303F...Especially jaegers.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#6PCould it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#12PS-So then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PWell, I'm just talkin' hypothetically, of course.\x02\x03",
            "#00300FBy the way, Erebonia is the\x01",
            "biggest user of gunpowder weapons.\x02\x03",
            "Even now they have a large\x01",
            "stock of old Reinford models.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#6PIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHu hu, you seem to know a lot\x01",
            "about it, just as I suspected.\x02\x03",
            "#10303FBut Erebonia, huh... \x01",
            "That makes me feel a little uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PYeah... There was also\x01",
            "what happened yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PWhat, something happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PYeah, actually──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Elie explained the details of their\x01",
            "meeting with Secretary Lechter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00301F#11P──That playboy is\x01",
            "an Erebonian spy?\x02\x03",
            "Though I always knew he\x01",
            "wasn't just your regular guy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PRather than a spy, perhaps you could\x01",
            "say he's an intelligence officer.\x02\x03",
            "He might just be here to\x01",
            "scope out the city before\x01",
            "the Trade Conference, but...\x02\x03",
            "#00008F...I'm quite concerned about that\x01",
            "redheaded girl that was with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#12P...*sigh*, that girl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#5PHu hu, looks like that\x01",
            "hit you pretty hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#11PWhat happened?\x01",
            "Any juicy story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#6PUh, well....\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Noｱl explained about the red\x01",
            "haired girl with Lechter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305F#11P....Wow.........\x02\x03",
            "............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#12PL-Let's stop talking about that girl.\x02\x03",
            "#00113FSeriously... I feel like I\x01",
            "understand how Miss Rixia feels\x01",
            "when she's with Miss Ilya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha, it really is similar, isn't it.\x02\x03",
            "#00008F...But, it seems like she\x01",
            "might come into play soon...\x02\x03",
            "#00001FShe's definitely not just\x01",
            "an ordinary civilian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PThat reminds me... That man we\x01",
            "met on West Crossbell Highway\x01",
            "was from the Empire region too.\x02\x03",
            "#10105FOh, come to think of it, he had\x01",
            "red hair too, didn't he...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    ChrTalk(
        0x105,
        "#10305F#5PYeah, now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PCaptain Lechter and that girl are both\x01",
            "redheads but his is a different tint...\x02\x03",
            "#00001FThinking about it again, that girl and the\x01",
            "one-eyed man had the same hair color exactly.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#12PC-Could it be...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(2374, 255, 100, 0)

    ChrTalk(
        0x104,
        (
            "#00304F#11P#30WHa ha....\x02\x03",
            "#00311F#30W──Basically, my red\x01",
            "hair looks like theirs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#5P...You have some idea about\x01",
            "all of this, don't you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)
    Sound(2375, 255, 100, 0)
    Sleep(1300)

    ChrTalk(
        0x104,
        (
            "#00304F#5P#40W...You got me.\x02\x03",
            "#00312F#40W──Looks like they've finally come.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(13520, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1984 end

    def Function_8_2A11(): pass

    label("Function_8_2A11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xBE, 0xBE, 0xBE, 0x0, 0x0)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("apl/ch50011.itc", 0x23)
    SoundLoad(460)
    SoundLoad(803)
    SoundLoad(3451)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(150500, 700, 250, 0)
    MoveCamera(307, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14270, 0)
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
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 150400, 100, -1100, 90)
    SetChrPos(0x102, 151900, 100, 900, 90)
    SetChrPos(0x109, 151900, 100, -1100, 90)
    SetChrPos(0x105, 148800, 100, -100, 90)
    SetChrPos(0x104, 150400, 100, 900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    PlayBGM("ed7516", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13770, 1000)
    OP_0D()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00001F#6PHey, Randy──\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00006F#5PUgh, at a time like this....\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Fade(250)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x9)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(2084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00001F#3PYes, this is Lloyd\x01",
            "Bannings, of the SSS.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3451V#40W──Bannings, it's me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD7B)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FOh, Mr. Dudley.\x02\x03",
            "#00000FI heard you were out on business, \x01",
            "did you just get back?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, this afternoon.\x02\x03",
            "I heard from Emma.\x01",
            "You were a big help to her.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004FNo, it was nothing.\x02\x03",
            "#00001FMore importantly...\x01",
            "Anything happened?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah. I figured I'd\x01",
            "let you guys know.\x02\x03",
            "──The old Revache\x01",
            "building has a new owner.\x02\x03",
            "A company known as "Crimson & Co.".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F"Crimson & Co."...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FHuh!? \x01",
            "Not the "Heiyue"?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems they made a quick deal and\x01",
            "snatched it out from under their noses.\x02\x03",
            "They have shady dealings\x01",
            "in the Empire, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FFrom the Empire...\x02\x03",
            "#00013FWhat kind of corporation are they?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They run a high-class club known as\x01",
            ""Neue-Blanc" in the Imperial capital.\x02\x03",
            "They opened a branch office in\x01",
            "Crossbell City about a year ago, too.\x02\x03",
            "They're launching a full-scale\x01",
            "expansion into Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FB-But of course, it's not just\x01",
            "any regular corporation right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well...\x02\x03",
            "...Is Orlando there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FRandy? Yeah, we just\x01",
            "met up with him...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Dudley's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You should ask him about\x01",
            "this "Crimson & Co.."\x02\x03",
            "──I'll contact you again tonight.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 80, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011FAh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(804, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)

    ChrTalk(
        0x102,
        "#00108F#11PW-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#5PIt was quite the conversation\x01",
            "you were having.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5P──I see. So they were after the\x01",
            "Revache old building, huh.\x02\x03",
            "#00300F#11PNoｱl, when we get back, mind\x01",
            "dropping by Entertainment District?\x02\x03",
            "Right by the Back Street entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#6PT-That's fine but...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)
    SetChrSubChip(0x105, 0x0)

    ChrTalk(
        0x101,
        (
            "#00003F#6P...Randy.\x02\x03",
            "#00013FWhat kind of corporation\x01",
            "is the "Crimson & Co."?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00306F#5P#30WWell...\x02\x03",
            "#00303FThey're an Imperial corporation that\x01",
            "manages the high class club "Neue-Blanc"...\x02\x03",
            "#00311FBut in reality── it's a front used \x01",
            "by the "Red Constellation"\x01",
            "jaeger corps for fundraising.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14270, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_24(0x323)
    SetScenarioFlags(0x22, 0)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2A11 end

    def Function_9_3686(): pass

    label("Function_9_3686")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
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
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 151950, 100, 950, 90)
    SetChrPos(0x102, 150400, 100, -1050, 90)
    SetChrPos(0x109, 151750, 170, -1150, 90)
    SetChrPos(0x103, 150400, 100, 950, 90)
    SetChrPos(0x104, 148850, 100, -950, 90)
    SetChrPos(0x105, 148850, 100, 750, 90)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x1, 0x9)
    OP_49()
    SetChrPos(0x9, 150000, 0, 0, 270)
    OP_D5(0x9, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0x1, "main", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x46, 0x3E8)
    OP_68(150000, 750, 0, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00008F#5PThose were...\x01",
            "Ambulances heading to the hospital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F#5PYes, those are vehicles \x01",
            "registered at St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303F#5PAnd even three of them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PCould they be carrying the wounded\x01",
            "from the derailment accident...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#5PWell, considering the timing,\x01",
            "I think there's no doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...It seems that sister Cecil\x01",
            "and the others will be busy.\x02\x03",
            "#00001FLet's go to the scene too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PRoger!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetScenarioFlags(0x162, 6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21410100), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC8")
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    SetScenarioFlags(0x22, 1)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_3B13")

    label("loc_3AC8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21302000), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AED")
    VolumeBGM(0x64, 0x3E8)
    Sleep(1000)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_3B13")

    label("loc_3AED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21410000), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B13")
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    NewScene("r1000", 99, 0, 0)
    IdleLoop()

    label("loc_3B13")

    Return()

    # Function_9_3686 end

    def Function_10_3B14(): pass

    label("Function_10_3B14")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    OP_68(-440, 750, 140, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, 1100, 180)
    SetChrPos(0x105, 1300, 100, 1100, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x4, 0x9)
    OP_49()
    SetChrPos(0x9, -8000, 0, 4000, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFrame(0x4, "main", 0x2, "stop")
    SetMapObjFrame(0x4, "obj00", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x46, 0x3E8)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00001F#12PThose buses just now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#11PThey looked like those the travellers\x01",
            "use to go to and from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11PMaybe they were transfer transports for\x01",
            "the passengers who rode the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#11POh boy, that's bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12P...I wonder about the\x01",
            "accident scale...?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetChrFlags(0x104, 0x1)
    SetChrFlags(0x103, 0x1)
    SetScenarioFlags(0x162, 7)
    SetScenarioFlags(0x22, 0)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3B14 end

    def Function_11_3EF2(): pass

    label("Function_11_3EF2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SoundLoad(468)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    OP_68(100040, 950, 320, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15750, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 98800, 100, 1700, 0)
    SetChrPos(0x102, 98800, 100, 100, 0)
    SetChrPos(0x109, 101000, 100, 1700, 0)
    SetChrPos(0x105, 101000, 100, -1400, 0)
    SetChrPos(0x104, 98800, 100, -1400, 0)
    SetChrPos(0x103, 101000, 100, 100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    VolumeBGM(0x46, 0x3E8)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x109,
        "#5P#10110FT-This is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F#5PHow...awful...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00010FKh, at any rate, we must\x01",
            "confirm how's the situation...\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 60, 0)
    Sleep(300)
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...It's Sergei, can you hear me?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x2)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00007FChief...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00101FAre you all right!?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah, somehow.\x02\x03",
            "Since the police HQ was attacked,\x01",
            "I'm at the Support Section in charge\x01",
            "of contacting every place.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#5P#00013FThe police HQ was...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10107FQ-Quick, we must go there...!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, Sonya's unit is already\x01",
            "heading over there.\x02\x03",
            "If possible, go to the\x01",
            "Waterfront Area.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#5P#00005FThe...Waterfront Area?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems that just some time ago, some\x01",
            "jaegers blew up the Heiyue branch office.\x02\x03",
            "And after that, it seems they\x01",
            "marched into the IBC building.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "At present, the main enemy force\x01",
            "is attacking Orchis Tower.\x02\x03",
            "It seems that Arios and Dudley\x01",
            "are holding out, but they'll \x01",
            "probably need the CGF help.\x02\x03",
            "As for the other Bracers...\x01",
            "It seems they have their hands full since \x01",
            "they're clearing out military monsters\x01",
            "that were released in the city areas.\x02\x03",
            "You're the only ones who\x01",
            "can rush to the place.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x102,
        "#5P#00108FH-However....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201F...Is everything fine at\x01",
            "the Support Section?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I made passers-by take refuge\x01",
            "inside the Support Section.\x02\x03",
            "Because Zeit is keeping watch,\x01",
            "the military monsters don't come close.\x02\x03",
            "KeA is here too, so,\x01",
            "well, don't worry.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#6P#00206F...Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10301FThings seem fine somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013F──Understood. We'll head to\x01",
            "the Waterfront Area now.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah...\x01",
            "Be very careful.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    ChrTalk(
        0x105,
        (
            "#6P#10308FThe IBC building...\x01",
            "Could mira be their purpose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FI don't know, but...\x01",
            "In any case, we should make haste.\x02\x03",
            "#00008FActually, I'm worried about the\x01",
            "police HQ that was attacked, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F...Yes...\x01",
            "However, let's hurry.\x02\x03",
            "#10101FThere're people you know\x01",
            "in the IBC building, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00106FYes...\x01",
            "It's very likely Bell is there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208FJona and Chief Roberts too...\x01",
            "I think they should be in the Foundation's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#5P...At any rate, I think we\x01",
            "should leave the car as soon\x01",
            "as we reach the Waterfront Area.\x02\x03",
            "#00301FIf we carelessly approached in the car,\x01",
            "we could be fired at with panzer faust, \x01",
            "anti-tank missiles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00011FThere's that danger too...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FRoger.\x01",
            "I'll hurry up to the Waterfront Area entrance.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    StopSound(468, 2000, 100)
    OP_68(100000, 850, -3500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Some time later, after departing with the CGF \x01",
            "vehicle heading to the Governmental District...\x02\x03",
            "The orbal car Lloyd and the others were\x01",
            "riding avoided fights and arrived at the\x01",
            "Waterfront Area via the East Street.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7150", "ed7544")
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 2)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_3EF2 end

    def Function_12_4D91(): pass

    label("Function_12_4D91")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03102.itc", 0x23)
    LoadChrToIndex("chr/ch03202.itc", 0x24)
    LoadChrToIndex("chr/ch00902.itc", 0x25)
    OP_68(-610, 700, 50, 0)
    MoveCamera(321, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14400, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E41")
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)

    label("loc_4E41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E59")
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)

    label("loc_4E59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E71")
    SetChrChipByIndex(0x106, 0x24)
    SetChrSubChip(0x106, 0x0)

    label("loc_4E71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E89")
    SetChrChipByIndex(0x10A, 0x25)
    SetChrSubChip(0x10A, 0x0)

    label("loc_4E89")

    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0xF4, 0x4)
    SetChrFlags(0xF5, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x103, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0xF4, 0x1)
    ClearChrFlags(0xF5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FB4")
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x104, -700, 100, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F50")
    SetChrPos(0x105, 300, 100, 1100, 180)
    Jump("loc_4F97")

    label("loc_4F50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F76")
    SetChrPos(0x106, 200, 100, 1100, 180)
    Jump("loc_4F97")

    label("loc_4F76")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F97")
    SetChrPos(0x10A, 300, 100, 1100, 180)

    label("loc_4F97")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x101, 0x2)
    Jump("loc_5099")

    label("loc_4FB4")

    SetChrPos(0x101, -800, 100, -1700, 180)
    SetChrPos(0x102, 1300, 100, -1900, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, -400, 180)
    ClearScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_501F")
    SetChrPos(0x10A, -700, 100, 1100, 180)
    SetScenarioFlags(0x0, 0)

    label("loc_501F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5060")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_504F")
    SetChrPos(0x105, -700, 100, 1100, 180)
    Jump("loc_5060")

    label("loc_504F")

    SetChrPos(0x105, 300, 100, 1100, 180)

    label("loc_5060")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5081")
    SetChrPos(0x106, 200, 100, 1100, 180)

    label("loc_5081")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x102, 0x2)

    label("loc_5099")

    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    VolumeBGM(0x3C, 0x3E8)
    FadeToBright(1000, 0)
    SetCameraDistance(13800, 2000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F72")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51D3")

    ChrTalk(
        0x106,
        (
            "#10702F#11PWow... It's the first time I'm riding in it.\x01",
            "The interior is lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00009FHa ha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FKeA too liked\x01",
            "this car, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52FB")

    ChrTalk(
        0x10A,
        (
            "#00605F#11PHm, the ZCF newest orbal car, eh?\x02\x03",
            "#00603FIt really seems to be easy to use.\x01",
            "I was thinking of using them at\x01",
            "Section One too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FConsidering the entire Zemuria situation, \x01",
            "I think that maybe it would be difficult to \x01",
            "import them from Liberl...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52FB")

    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    ChrTalk(
        0x109,
        (
            "#10104F#5PWell, its design is nice and\x01",
            "it runs without problem.\x02\x03",
            "#10100FWith her, I'm sure that even forcing our way\x01",
            "through things could be done easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FWe could confirm that it can be\x01",
            "used to ram vehicles...\x02\x03",
            "#00200FShould we go back to the Chief\x01",
            "and the others for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00103FRight, I'd like to hear\x01",
            "the final plans too...\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 80, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00013FThat's...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55B8")

    ChrTalk(
        0x10A,
        (
            "#00601F#11PThe on-board communication device.\x01",
            "Must be a call from somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_560B")

    label("loc_55B8")


    ChrTalk(
        0x104,
        (
            "#11P#00301FIt's the on-board communicator.\x01",
            "Seems to be a call from somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_560B")


    ChrTalk(
        0x109,
        (
            "#10113F#5PM-Mr. Lloyd.\x01",
            "What do we do...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FYeah...\x01",
            "Try turning it ON.\x02\x03",
            "#00001FEveryone, just in case, \x01",
            "don't raise your voices.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(500)
    Sound(853, 0, 100, 0)
    Sleep(300)
    Sound(899, 0, 50, 0)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──It's been a long time,\x01",
            "Special Support Section.\x02\x03",
            "It's Kilika.\x01",
            "Kilika Rouran.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0x101,
        "#12P#00011FEEH....!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00307FMiss Kilika!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_584B")

    ChrTalk(
        0x106,
        "#10701F#11P(Taito's "Crimson Swallow"...)\x02",
    )

    CloseMessageWindow()

    label("loc_584B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58B5")

    ChrTalk(
        0x10A,
        (
            "#00601F#11PThe Rocksmith Agency's head of office...\x01",
            "She was still in Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_58B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5932")

    ChrTalk(
        0x105,
        (
            "#10403F#11PThe Calvardian intelligence\x01",
            "agency's lady...?\x02\x03",
            "#10400FTo think she was still in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5932")


    ChrTalk(
        0x109,
        (
            "#10101F#5PB-But how can she\x01",
            "contact us here...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00101F...Has she catched all\x01",
            "of our movements?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kilika's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I only predicted how you would\x01",
            "have acted in such a situation.\x02\x03",
            "You're busy and I am very sorry\x01",
            "for taking up your time, however...\x02\x03",
            "Would you feel inclined about\x01",
            "an "information exchange"?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00008FWell...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B77")

    ChrTalk(
        0x10A,
        (
            "#00603F#11P(...Bannings.\x01",
            "You decide.)\x02\x03",
            "#00601F(We at Section One haven't been able\x01",
            "to create connections with her, yet.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003F#11P(...I understand.)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jump("loc_5B8F")

    label("loc_5B77")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    label("loc_5B8F")


    ChrTalk(
        0x101,
        (
            "#12P#00006F──All right, Miss Kilika.\x02\x03",
            "#00001FWhere should we come to?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kilika's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell Station, 2nd vehicle of the\x01",
            "train stopped at platform No. 3.\x02\x03",
            "There's no one at the station,\x01",
            "so don't worry.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#12P#00004FUnderstood.\x01",
            "2nd vehicle of the train\x01",
            "at platform No. 3...\x02\x03",
            "#00013FBy the way...\x01",
            "Is Mr. Lechter there too?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kilika's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hu hu, how acute.\x01",
            "──Then, we will be waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#12P#00211F...A woman as clairvoyant\x01",
            "as always...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00108FIt also seems that Captain\x01",
            "Lechter is with her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00306FWell, we can only go there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FYeah...\x01",
            "Let's head to Crossbell Station.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F#5PRoger!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EB2")

    ChrTalk(
        0x106,
        (
            "#10701F#11P...Let's prepare in advance in\x01",
            "case something happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F6D")

    label("loc_5EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F15")

    ChrTalk(
        0x105,
        (
            "#10404F#11PJust in case, maybe it would be\x01",
            "better to prepare in advance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F6D")

    label("loc_5F15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F6D")

    ChrTalk(
        0x10A,
        (
            "#00603F#11PJust in case, it would be\x01",
            "better to prepare in advance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F6D")

    Jump("loc_6E11")

    label("loc_5F72")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6024")

    ChrTalk(
        0x106,
        (
            "#10702F#11PWow... It's the first time I'm riding in it.\x01",
            "The interior is lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#5PHa ha, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FKeA too liked\x01",
            "this car, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6024")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6174")

    ChrTalk(
        0x10A,
        (
            "#11P#00605FHm, the ZCF newest orbal car, eh?\x02\x03",
            "#00603FIt really seems to be easy to use.\x01",
            "I was thinking of using them at\x01",
            "Section One too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FConsidering the entire Zemuria situation, \x01",
            "I think that maybe it would be difficult to \x01",
            "import them from Liberl...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6174")

    ChrTalk(
        0x105,
        "#10403FHm, indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_6174")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#5P──Its design is good too and it\x01",
            "seems it runs with no problem.\x02\x03",
            "#00000FWhen we'll do the real break in,\x01",
            "I think it will be better to leave \x01",
            "the driving to Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00302FWell, she's a pro after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FWe could confirm that it can be\x01",
            "used to ram vehicles...\x02\x03",
            "#00200FShould we go back to the Chief\x01",
            "and the others for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FRight, I'd like to hear\x01",
            "the final plans too...\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 80, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5PThat's...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6457")

    ChrTalk(
        0x10A,
        (
            "#11P#00601FThe on-board communication device.\x01",
            "Must be a call from somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64AA")

    label("loc_6457")


    ChrTalk(
        0x104,
        (
            "#11P#00301FIt's the on-board communicator.\x01",
            "Seems to be a call from somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64AA")


    ChrTalk(
        0x102,
        "#12P#00108F...Lloyd, what do we do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah...\x01",
            "Let's turn it ON for now.\x02\x03",
            "#00013FEveryone, just in case, \x01",
            "don't raise your voices.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(500)
    Sound(853, 0, 100, 0)
    Sleep(300)
    Sound(899, 0, 50, 0)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──It's been a long time,\x01",
            "Special Support Section.\x02\x03",
            "It's Kilika.\x01",
            "Kilika Rouran.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    ChrTalk(
        0x101,
        "#00011F#5PEEH....!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00307FMiss Kilika!?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66EA")

    ChrTalk(
        0x106,
        "#10701F#11P(Taito's "Crimson Swallow"...)\x02",
    )

    CloseMessageWindow()

    label("loc_66EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6754")

    ChrTalk(
        0x10A,
        (
            "#11P#00601FThe Rocksmith Agency's head of office...\x01",
            "She was still in Crossbell?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67D1")

    label("loc_6754")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67D1")

    ChrTalk(
        0x105,
        (
            "#11P#10403FThe Calvardian intelligence\x01",
            "agency's lady...?\x02\x03",
            "#10400FTo think she was still in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67D1")


    ChrTalk(
        0x102,
        (
            "#12P#00101F...Has she catched all\x01",
            "of our movements?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kilika's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I only predicted how you would\x01",
            "have acted in such a situation.\x02\x03",
            "You're busy and I am very sorry\x01",
            "for taking up your time, however...\x02\x03",
            "Would you feel inclined about\x01",
            "an "information exchange"?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00008F#5PWell...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69DA")

    ChrTalk(
        0x10A,
        (
            "#11P#00603F(...Bannings.\x01",
            "You decide.)\x02\x03",
            "#00601F(We at Section One haven't been able\x01",
            "to create connections with her, yet.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#5P(...I understand.)\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jump("loc_69F2")

    label("loc_69DA")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    label("loc_69F2")


    ChrTalk(
        0x101,
        (
            "#00006F#5P──All right, Miss Kilika.\x02\x03",
            "#00001FWhere should we come to?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kilika's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Crossbell Station, 2nd vehicle of the\x01",
            "train stopped at platform No. 3.\x02\x03",
            "There's no one at the station,\x01",
            "so don't worry.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00004F#5PUnderstood.\x01",
            "2nd vehicle of the train\x01",
            "at platform No. 3...\x02\x03",
            "#00013FBy the way...\x01",
            "Is Mr. Lechter there too?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Kilika's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hu hu, how acute.\x01",
            "──Then, we will be waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#12P#00211F...A woman as clairvoyant\x01",
            "as always...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FIt also seems that Captain\x01",
            "Lechter is with her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00306FWell, we can only go there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PYeah...\x01",
            "Let's head to Crossbell Station.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CCC")

    ChrTalk(
        0x10A,
        "#11P#00603FRoger.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CFA")

    label("loc_6CCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CFA")

    ChrTalk(
        0x105,
        "#11P#10404FHu hu, roger.\x02",
    )

    CloseMessageWindow()

    label("loc_6CFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D56")

    ChrTalk(
        0x106,
        (
            "#10701F#11P...Let's prepare in advance in\x01",
            "case something happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E11")

    label("loc_6D56")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DB9")

    ChrTalk(
        0x105,
        (
            "#10402F#11PJust in case, maybe it would be\x01",
            "better to prepare in advance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E11")

    label("loc_6DB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E11")

    ChrTalk(
        0x10A,
        (
            "#00601F#11PJust in case, it would be\x01",
            "better to prepare in advance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E11")

    FadeToDark(1000, 0, -1)
    SetCameraDistance(14300, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0xF4, 0x4)
    ClearChrFlags(0xF5, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x103, 0x1)
    SetChrFlags(0x104, 0x1)
    SetChrFlags(0xF4, 0x1)
    SetChrFlags(0xF5, 0x1)
    OP_37()
    SetScenarioFlags(0x1A5, 5)
    OP_29(0xB1, 0x1, 0x8)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    EventEnd(0x5)
    NewScene("c0200", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_12_4D91 end

    def Function_13_6EB6(): pass

    label("Function_13_6EB6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    BeginChrThread(0x101, 3, 0, 2)
    SoundLoad(468)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_701C")

    ChrTalk(
        0x103,
        "#00211FThey outdistanced us...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FW-Well...\x01",
            "I think that prudence\x01",
            "is the best thing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(Uuuh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Did I make an evaluation mistake...?)\x02\x03",
            "#00007F...A-Anyway, let's keep pursuing them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A0")

    label("loc_701C")


    ChrTalk(
        0x103,
        (
            "#00205FCurving at such a speed although the\x01",
            "road condition is bad due to the rain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FB-But wouldn't it be\x01",
            "a little dangerous...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHu hu, with this level of rain,\x01",
            "it's just a piece of cake!\x02\x03",
            "#10107FA runaway vehicle...\x01",
            "I'll never let it get away!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x101,
        "#00012FS-Somehow you're really into it...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    ChrTalk(
        0x101,
        (
            "#00001F...A-At any rate,\x01",
            "let's continue the pursuit!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_71A0")

    Sound(494, 0, 70, 0)
    OP_68(101440, 650, -16510, 3000)
    MoveCamera(311, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11280, 3000)
    Sleep(1000)
    StopSound(468, 1000, 100)
    StopSound(494, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearScenarioFlags(0x178, 5)
    SetScenarioFlags(0x22, 5)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_6EB6 end

    def Function_14_721C(): pass

    label("Function_14_721C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    BeginChrThread(0x101, 3, 0, 2)
    SoundLoad(468)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10110FKh...\x01",
            "They're quite good too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah...\x02\x03",
            "#00000FHowever, if we keep going like this, the pincer \x01",
            "with the District Crime Prevention Section \x01",
            "on standby at the west exit could go well.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)

    ChrTalk(
        0x105,
        (
            "#10305FHm...?\x02\x03",
            "Isn't that car acting\x01",
            "weird somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWhat...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopSound(468, 500, 100)
    SetScenarioFlags(0x22, 6)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_721C end

    def Function_15_73D5(): pass

    label("Function_15_73D5")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(100490, 650, -450, 0)
    MoveCamera(311, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13160, 0)
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
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 99000, 100, 1600, 0)
    SetChrPos(0x102, 99000, 100, 40, 0)
    SetChrPos(0x109, 101100, 100, 1600, 0)
    SetChrPos(0x105, 101100, 100, 40, 0)
    SetChrPos(0x104, 99000, 100, -1420, 0)
    SetChrPos(0x103, 101100, 100, -1420, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Return()

    # Function_15_73D5 end

    def Function_16_750E(): pass

    label("Function_16_750E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SoundLoad(468)
    SoundLoad(469)
    OP_68(-500, 650, 500, 0)
    MoveCamera(324, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13750, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x101, 0x0)
    SetChrBattleFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    EndChrThread(0x102, 0x0)
    SetChrBattleFlags(0x102, 0x4)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    EndChrThread(0x109, 0x0)
    SetChrBattleFlags(0x109, 0x4)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    EndChrThread(0x105, 0x0)
    SetChrBattleFlags(0x105, 0x4)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0x104, 0x0)
    SetChrBattleFlags(0x104, 0x4)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x103, 0x0)
    SetChrBattleFlags(0x103, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x105, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, 1100, 180)
    SetChrPos(0x103, 1300, 100, 1100, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    Sound(469, 2, 60, 0)
    BeginChrThread(0x101, 3, 0, 2)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00010FDamn, because of the grenades we're\x01",
            "restrained and can't get close at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FUuh, I don't want to lose\x01",
            "on car ability but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201F...At this rate, it would be a bother if he\x01",
            "could enter Altair City in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIn that case, trying\x01",
            "to arrest him would be\x01",
            "almost impossible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00310FTch...this looks bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FIn any case...\x01",
            "We can only chase him without giving up!\x02\x03",
            "#00007FPlease, Noｱl!\x01",
            "Stay steadily on him so\x01",
            "he can't shake us off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107FYessir!\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10305F...Oh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(468, 300, 90)
    StopSound(469, 300, 50)
    SetScenarioFlags(0x22, 3)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_750E end

    SaveToFile()

Try(main)
