from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0510.bin",                # FileName
        "e0510",                    # MapName
        "e0510",                    # Location
        0x00A1,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0510",                  # 0
        "Elie",                   # 1
        "Noｱl",                  # 2
        "Randy",                  # 3
        "Crewman Salsa",          # 4
        "Citizen",                # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Melson",                 # 8
        "Rimah",                  # 9
        "Corona",                 # 10
        "Fran",                   # 11
        "Cecil",                  # 12
        "Ilya",                   # 13
        "Rixia",                  # 14
        "Sully",                  # 15
        "Mariabell",              # 16
        "Zeit",                   # 17
        "SE制御",                 # 18
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch02900.itc",                   # 01
        "chr/ch00302.itc",                   # 02
        "chr/ch28400.itc",                   # 03
        "chr/ch33002.itc",                   # 04
        "chr/ch20402.itc",                   # 05
        "chr/ch22102.itc",                   # 06
        "chr/ch26202.itc",                   # 07
        "chr/ch22702.itc",                   # 08
        "chr/ch20702.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    388,  0x0, 1,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(4294967196, 0,       4294951876, 0,    389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294964846, 150,     4294963497, 180,  453,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4294964846, 150,     4294960847, 180,  453,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4294963846, 150,     4294960847, 180,  453,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4294964247, 150,     4294955946, 180,  389,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(4294963546, 150,     4294955946, 180,  389,  0x0, 0,   9,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4294965046, 150,     4294955946, 180,  389,  0x0, 0,   8,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(844, 0)                                        # 0

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_3FC",          # 01, 1
        "Function_2_4FF",          # 02, 2
        "Function_3_554",          # 03, 3
        "Function_4_914",          # 04, 4
        "Function_5_BA3",          # 05, 5
        "Function_6_F26",          # 06, 6
        "Function_7_10F8",         # 07, 7
        "Function_8_1242",         # 08, 8
        "Function_9_12EC",         # 09, 9
        "Function_10_1384",        # 0A, 10
        "Function_11_157F",        # 0B, 11
        "Function_12_1799",        # 0C, 12
        "Function_13_180B",        # 0D, 13
        "Function_14_2D38",        # 0E, 14
        "Function_15_3D3D",        # 0F, 15
        "Function_16_3D65",        # 10, 16
        "Function_17_3D8D",        # 11, 17
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_384"),
        (1, "loc_390"),
        (2, "loc_39C"),
        (3, "loc_3A8"),
        (4, "loc_3B4"),
        (5, "loc_3C0"),
        (6, "loc_3CC"),
        (SWITCH_DEFAULT, "loc_3D8"),
    )


    label("loc_384")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_390")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_39C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3FB")

    Return()

    # Function_0_34C end

    def Function_1_3FC(): pass

    label("Function_1_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    SetChrPos(0x8, 630, -1000, 9000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 3250, 150, -9100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrSubChip(0x10, 0x2)

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)

    label("loc_4FE")

    Return()

    # Function_1_3FC end

    def Function_2_4FF(): pass

    label("Function_2_4FF")

    Sound(480, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_533")
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553")
    SetChrSubChip(0xA, 0x1)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_553")

    Return()

    # Function_2_4FF end

    def Function_3_554(): pass

    label("Function_3_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B")
    Call(0, 13)
    Return()

    label("loc_56B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_57C")
    Jump("loc_910")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_910")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_598")
    Jump("loc_910")

    label("loc_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5A8")
    Jump("loc_910")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_5B6")
    Jump("loc_910")

    label("loc_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5C4")
    Jump("loc_910")

    label("loc_5C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_5D2")
    Jump("loc_910")

    label("loc_5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5E0")
    Jump("loc_910")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_910")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88A")

    ChrTalk(
        0x8,
        (
            "#00100FWe finally had a vacation so if we\x01",
            "don't enjoy it, it would be a waste.\x02\x03",
            "#00104FI'm sure that Bell said she was\x01",
            "preparing many surprises too...\x02\x03",
            "#00102F*giggle*, when I think about that,\x01",
            "I'm really looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FSurprises, eh...?\x01",
            "I'm a little worried, though.\x02\x03",
            "#00003FIf she did something like the entire\x01",
            "Michelam came to welcome us,\x01",
            "I'd really want to crawl into a hole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00109FE-Even if Bell likes showy things,\x01",
            "preparing something like that...\x02\x03",
            "#00103F...Would not be impossible, I think.\x02\x03",
            "#00102FL-Let's pray the Goddess that\x01",
            "at least it's not something strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(N-Now I'm worried...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_910")

    label("loc_88A")


    ChrTalk(
        0x8,
        (
            "#00103FUhhm, even so, I wonder what kind of\x01",
            "surprises Bell has in store for us...\x02\x03",
            "#00111F...I hope they're not strange, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_910")

    TalkEnd(0xFE)
    Return()

    # Function_3_554 end

    def Function_4_914(): pass

    label("Function_4_914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92B")
    Call(0, 13)
    Return()

    label("loc_92B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_93C")
    Jump("loc_B9F")

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_94A")
    Jump("loc_B9F")

    label("loc_94A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_958")
    Jump("loc_B9F")

    label("loc_958")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_968")
    Jump("loc_B9F")

    label("loc_968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_976")
    Jump("loc_B9F")

    label("loc_976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_984")
    Jump("loc_B9F")

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_992")
    Jump("loc_B9F")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9A0")
    Jump("loc_B9F")

    label("loc_9A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_B9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B8")
    Jump("loc_B9F")

    label("loc_9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0F")

    ChrTalk(
        0x9,
        (
            "#10105FBy the way, it's a pity that Chief\x01",
            "Sergei couldn't come with us.\x02\x03",
            "#10106FHe said to go and have fun,\x01",
            "but I feel very sorry for him...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThe Chief is quite a busy man...\x02\x03",
            "#00002FHa ha, maybe he was simply\x01",
            "embarrassed to be seen how\x01",
            "he is in private...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10109FAhaha, that would be unexpectedly fun.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_B9F")

    label("loc_B0F")


    ChrTalk(
        0x9,
        (
            "#10103FA pity that Chief Sergei\x01",
            "couldn't come with us, eh?\x02\x03",
            "#10102FI guess that about this time he's\x01",
            "smoking alone at the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9F")

    TalkEnd(0xFE)
    Return()

    # Function_4_914 end

    def Function_5_BA3(): pass

    label("Function_5_BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBA")
    Call(0, 14)
    Return()

    label("loc_BBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_BCB")
    Jump("loc_F22")

    label("loc_BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BD9")
    Jump("loc_F22")

    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BE7")
    Jump("loc_F22")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_BF5")
    Jump("loc_F22")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C03")
    Jump("loc_F22")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_C11")
    Jump("loc_F22")

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C1F")
    Jump("loc_F22")

    label("loc_C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_F22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C37")
    Jump("loc_F22")

    label("loc_C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7B")

    ChrTalk(
        0xA,
        (
            "#00303FAck, boring stuff is really\x01",
            "not in my character.\x02\x03",
            "#00301FIn that case, today I'm gonna\x01",
            "enjoy Michelam to the fullest!\x02\x03",
            "#00309FLloyd, you'll come to pick up girls \x01",
            "with me tonight, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha, well if you're fine with me\x01",
            "leaving the picking up entirely to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00306FWhat the, how unmotivated you're.\x02\x03",
            "#00309FYou too are good stuff, so you might\x01",
            "as well grow yourself out that younger\x01",
            "brother character and become popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I don't get what you mean...\x02\x03",
            "#00000F(...However, he seems to have\x01",
            "gone back to his usual self.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_F1A")

    label("loc_E7B")


    ChrTalk(
        0xA,
        (
            "#00305FOh, right, I must buy a\x01",
            "present for her too...\x02\x03",
            "#00304FShe was talkin' about a promotion, so I guess\x01",
            "I'll pick up a congratulation gift somewhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1A")

    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_F22")

    TalkEnd(0xFE)
    Return()

    # Function_5_BA3 end

    def Function_6_F26(): pass

    label("Function_6_F26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_F37")
    Jump("loc_10F4")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_F45")
    Jump("loc_10F4")

    label("loc_F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F53")
    Jump("loc_10F4")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_10F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104F")

    ChrTalk(
        0xB,
        (
            "Thank you very much for\x01",
            "using the water bus today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You are the persons who were\x01",
            "invited by Lady Mariabell, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It takes a very short time to Michelam,\x01",
            "so please enjoy a relaxing trip lulled by the waves.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10F4")

    label("loc_104F")


    ChrTalk(
        0xB,
        (
            "When you are seasick, gazing\x01",
            "at the distant scenery on the deck\x01",
            "is good to distract yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Please rest assured, we also\x01",
            "have remedies for sea sickness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F4")

    TalkEnd(0xFE)
    Return()

    # Function_6_F26 end

    def Function_7_10F8(): pass

    label("Function_7_10F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_123E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CD")

    ChrTalk(
        0xC,
        (
            "I was really surprised by the independence\x01",
            "proposal at the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I wonder at what extent Mr. Dieter\x01",
            "intends to make that a reality...\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_123E")

    label("loc_11CD")


    ChrTalk(
        0xC,
        (
            "I wonder at what extent Mr. Dieter\x01",
            "intends to make the independence a reality...\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123E")

    TalkEnd(0xFE)
    Return()

    # Function_7_10F8 end

    def Function_8_1242(): pass

    label("Function_8_1242")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_12E8")

    ChrTalk(
        0xD,
        (
            "The trip to Crossbell I dreamt of,\x01",
            "the Michelam Health Resort theme park!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Maan, I can't wait.\x01",
            "My girlfriend and I will enjoy it at the fullest!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E8")

    TalkEnd(0xFE)
    Return()

    # Function_8_1242 end

    def Function_9_12EC(): pass

    label("Function_9_12EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1380")

    ChrTalk(
        0xE,
        (
            "Personally, I'd like to go to the\x01",
            "restaurant and the boutique.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uhuhu, today I'll let myself\x01",
            "be spoiled by my boyfriend a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1380")

    TalkEnd(0xFE)
    Return()

    # Function_9_12EC end

    def Function_10_1384(): pass

    label("Function_10_1384")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1395")
    Jump("loc_157B")

    label("loc_1395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_13A3")
    Jump("loc_157B")

    label("loc_13A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_13B1")
    Jump("loc_157B")

    label("loc_13B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_13BF")
    Jump("loc_157B")

    label("loc_13BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_157B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14DA")

    ChrTalk(
        0xF,
        (
            "Crossbell independence...\x01",
            "As expected from Mr. Dieter,\x01",
            "none other would've imagined that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I believe it won't be\x01",
            "an easy path, but...\x01",
            "There's a dream in those words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "The Mayor will make Crossbell\x01",
            "shine brightly for sure.\x01",
            "I have that feeling.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_157B")

    label("loc_14DA")


    ChrTalk(
        0xF,
        (
            "Oops, I've come to have fun\x01",
            "with my family and so maybe\x01",
            "I shouldn't talk about these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Today, I have to have a lot of\x01",
            "fun with Rimah and Corona.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1384 end

    def Function_11_157F(): pass

    label("Function_11_157F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1590")
    Jump("loc_1795")

    label("loc_1590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_159E")
    Jump("loc_1795")

    label("loc_159E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15AC")
    Jump("loc_1795")

    label("loc_15AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_15BA")
    Jump("loc_1795")

    label("loc_15BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1795")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_171B")

    ChrTalk(
        0x11,
        (
            "Since my husband received a bonus after\x01",
            "the Orchis Tower construction was finished,\x01",
            "we came on a family trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I actually wanted to add it to savings, but in the\x01",
            "end I was convinced by my husband who wanted\x01",
            "to do something good for the family once in awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "However, I'm really glad we came.\x01",
            "Rimah is so happy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1795")

    label("loc_171B")


    ChrTalk(
        0x11,
        (
            "Since my husband received a bonus,\x01",
            "we came on a family trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Uh uh, I'm really glad we came.\x01",
            "Rimah is so happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1795")

    TalkEnd(0xFE)
    Return()

    # Function_11_157F end

    def Function_12_1799(): pass

    label("Function_12_1799")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_17AA")
    Jump("loc_1807")

    label("loc_17AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_17B8")
    Jump("loc_1807")

    label("loc_17B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_17C6")
    Jump("loc_1807")

    label("loc_17C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_17D4")
    Jump("loc_1807")

    label("loc_17D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1807")

    ChrTalk(
        0x10,
        (
            "Papaaa, look, look!\x01",
            "A fishie jumped!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1807")

    TalkEnd(0xFE)
    Return()

    # Function_12_1799 end

    def Function_13_180B(): pass

    label("Function_13_180B")

    EventBegin(0x0)
    SoundLoad(3515)
    SoundLoad(3394)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Fade(500)
    OP_68(700, 200, 8350, 0)
    MoveCamera(15, 33, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33390, 0)
    OP_64(0x8)
    OP_64(0x9)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x8, 500, -1000, 9000, 230)
    SetChrPos(0x9, -500, -1000, 9000, 80)
    SetChrPos(0x101, 1500, -1000, 8200, 315)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1919():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1919)
    Sleep(50)

    def lambda_1929():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1929)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x9,
        "#30W#3515VAh...Mr. Lloyd.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x1, 0x80000000)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sound(2189, 255, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        "#30WYou went out on deck?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#00004F#12PYeah, to catch the breeze.\x02\x03",
            "#00005FUhhm, did I disturb you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00108F#5PAh, uhhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10106F#5P...Well, we were talking about what\x01",
            "happened at the Trade Conference...\x02\x03",
            "#10113FAnd also about Mayor\x01",
            "Dieter's proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#12PProposal...\x01",
            "The one to be independent as a state?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00106F#5PYes... I can't...\x01",
            "Afford to be indifferent to that.\x02\x03",
            "#00108FI would've never believed "uncle"\x01",
            "was thinking about such a thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10106F#5PI too, frankly...\x01",
            "Feel that I can't be indifferent.\x02\x03",
            "#10108FIt's something that involves\x01",
            "the CGF continuance too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#12PI see... The Empire and\x01",
            "Republic will demand a\x01",
            "CGF reduction in scale.\x02\x03",
            "#00013FIn exchange, they'll say they'll \x01",
            "station their own troops at the\x01",
            "gates of Tangram and Bellguard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00103F#5PYes...  \x02\x03",
            "#00108FNo matter how I look at it, I can only\x01",
            "regard it as a conspiracy to siphon\x01",
            "out even more wealth from Crossbell.\x02\x03",
            "#00101FThen, if chances permit it, they'll\x01",
            "monopolize the fruits aiming at\x01",
            "each others' weaknesses...\x02\x03",
            "#00106FI can only think they're prepared for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PIndeed...\x02\x03",
            "#00001F...Then, the Mayor's proposal could\x01",
            "also be a plan to counter that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10103F#5PYes, becoming independent as a state,\x01",
            "could also enrich the CGF armaments that\x01",
            "have been pinned down until now by both nations.\x02\x03",
            "#10101FNot only anti-personnel weapons,\x01",
            "but also tanks and military airships\x01",
            "to prevent other nations' invasions.\x02\x03",
            "#10106F...Although, I feel a little bad to\x01",
            "think about it in those terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PNoｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00103F#5PHowever, I don't know if "uncle"'s proposal\x01",
            "can be said to be realistic or not...\x02\x03",
            "#00108FNegative statements were immediately\x01",
            "sent out by the Empire and Republic.\x02\x03",
            "#00100FHowever, the proposal was received\x01",
            "favorably by Liberl, Remiferia, the\x01",
            "Holy Nation of Arteria and others...\x02\x03",
            "#00106FHonestly, it's a tantalizing situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PYou're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10113F#5P...What do you make of\x01",
            "having been invited\x01",
            "today by Miss Mariabell?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#00106F#11PIf I have to say, she seems\x01",
            "to be concentrated on the IBC\x01",
            "management side at present.\x02\x03",
            "#00108FShe doesn't seem to be involved\x01",
            "that much about the proposal.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#10106F#6PI see...\x02\x03",
            "#10108F...Since it's a rare opportunity,\x01",
            "I was thinking to ask her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00103F#11PRight... There're many things\x01",
            "I'd like to ask Bell too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#12P──Say, you two.\x02\x03",
            "#00000FSince we're right in such times...\x01",
            "Don't you think we should enjoy it to the fullest?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_246F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_246F)
    Sleep(50)

    def lambda_247F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_247F)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)

    ChrTalk(
        0x8,
        "#00105F#5PWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10105F#5P......?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PIt's a rare chance to rest and we're\x01",
            "lodging at Michelam Hotel, you know?\x02\x03",
            "Furthermore, she said we can have as much\x01",
            "fun as we want at that theme park...\x02\x03",
            "#00009FWe'll certainly be able\x01",
            "to empty our minds...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00106F#5P#30WB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10108F#5P#30W...After such a thing happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12PIt's because it happened.\x02\x03",
            "#00003FWe don't know what's going to\x01",
            "happen to Crossbell from now on...\x02\x03",
            "It's very likely that our job\x01",
            "will become harder...\x02\x03",
            "#00002FThat's exactly why, how to say it...\x01",
            "I want to make "memories".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#00112F#5PEeh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10114F#5PY-You mean that...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#12P(...Eh? Why are they\x01",
            "reacting that much?)\x02\x03",
            "#00012FHa ha...\x01",
            "Was it too cheesy, as I expected?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10112F#5PRather than too cheesy...\x02\x03",
            "#10108F(Miss Elie...\x01",
            "Is he doing it on purpose?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00111F#5P(N-No...\x01",
            "It's very likely he's doing it spontaneously...)\x02\x03",
            "#00113F──Eehm, Lloyd.\x02\x03",
            "#00112FThose "memories" you say, it's not you want \x01",
            "to do them with someone in particular, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#12P? Of course not...\x02\x03",
            "#00000FIt's so rare to be able to\x01",
            "take a break with everyone.\x02\x03",
            "#00012FHa ha, I'm sorry for the Chief, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#00113F#5P*haaaaah"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10112F#5PY-You're right.\x01",
            "That's typical of Mr. Lloyd...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12POh, could it be that you've been\x01",
            "mistaking something since before?\x02\x03",
            "#00006FBecause I saw you feeling down, I thought \x01",
            "to cheer you up a little─#500W─#30W#00011Fah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#10102F#5PPfft...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        (
            "#00114F#5PAhaha...!\x02\x03",
            "#00116FY-You really are...\x01",
            "A natural...or just clumsy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10109F#5PUh uh, I feel like an idiot\x01",
            "for having worried somehow.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F#12P...I'm sorry.\x01",
            "I will leave you alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00104F#5P*giggle*, don't pout.\x02\x03",
            "#00102F...I'm sorry.\x01",
            "We too couldn't\x01",
            "read the mood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10102F#5PYou're right...\x01",
            "When you go on vacation,\x01",
            "you really must enjoy it to the fullest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12PI see...\x01",
            "(Well, I guess I reached my objective?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x8, 630, -1000, 9000, 270)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 3000, -1000, 6500, 180)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 2)
    EventEnd(0x5)
    Return()

    # Function_13_180B end

    def Function_14_2D38(): pass

    label("Function_14_2D38")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    OP_68(3170, 1300, -9560, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34500, 0)
    OP_64(0xA)
    SetChrPos(0x101, 800, 0, -9770, 90)
    SetCameraDistance(34000, 1500)
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    OP_0D()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(200)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    Sound(2756, 255, 100, 0)

    AnonymousTalk(
        0xA,
        (
            "#30W──Yo, Lloyd.\x02\x03",
            "#20WMan, Milady Mariabell is\x01",
            "a lot generous, huh.\x02\x03",
            "We can have as much fun as we\x01",
            "want at the Michelam resort\x01",
            "hotel and at the theme park too.\x02\x03",
            "What a great feast, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAC4)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x101,
        (
            "#00002F#6P...You're right.\x02\x03",
            "#00008F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00302F#5PHa ha......\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "#00304F#5P──Say, Lloyd.\x02\x03",
            "#00300FIt seems you're mistakin' something,\x01",
            "so I'll tell you this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00303F#5PAbout the killed terrorists...\x02\x03",
            "#00301FYou're thinkin' that since my\x01",
            "relatives did such a thing,\x01",
            "I'm in a shock, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#6PW-Well...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...No, it's a little different.\x02\x03",
            "#00008FI feel like you're dragging along\x01",
            "something on your own, Randy.\x02\x03",
            "#00001FYou're concerned about your\x01",
            "uncle and the others, perhaps?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)
    BeginChrThread(0x19, 1, 0, 15)

    ChrTalk(
        0xA,
        (
            "#00308F#5P...I see.\x02\x03",
            "#00303F#30W............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetChrSubChip(0xA, 0x0)
    Sleep(150)
    SetChrSubChip(0xA, 0x1)
    SetCameraDistance(33000, 20000)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#00304F#5P──I had a friend.\x02\x03",
            "One year younger than me,\x01",
            "he had puppy-like eyes...\x02\x03",
            "#00300FMaybe it was the first existence I could\x01",
            "call a friend outside of the corps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00308F#5PStuff happened\x01",
            "and he died...\x02\x03",
            "Really, stuff happened and I left\x01",
            "the corps and started wandering.\x02\x03",
            "#00303FThen, I reached Crossbell,\x01",
            "joined the CGF...\x01",
            "Met you all...\x02\x03",
            "#00302F...However, it seems I\x01",
            "wasn't myself to the core.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00312F#5P──Like my uncle said, the fact\x01",
            "of those killed terrorists\x01",
            "wasn't something new to me.\x02\x03",
            "Indeed, on the battlefield that level of war\x01",
            "of extermination was everyday occurrence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00303F#5PI snapped then...\x01",
            "Not out of righteous indignation.\x02\x03",
            "Not even because I felt mad towards my uncle,\x01",
            "although I was pityin' those terrorists.\x02\x03",
            "#00308F#30WI── Even if two years had passed,\x01",
            "I didn't change at all...\x02\x03",
            "I was only deeply shocked that I was \x01",
            "nothing more than a jaeger to the core...\x02\x03",
            "#00306FSo I grabbed 'im like in an outburst\x01",
            "of anger and I was knocked down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PI see....\x02\x03",
            "#00006F...That was\x01",
            "indeed lame.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00302F#5PHa ha, I know, right?\x02\x03",
            "#00306FHonestly, me, a cool dandy,\x01",
            "doin' such an unsightly──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P...But, you know.\x01",
            "I guess I'm a little happy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    Sleep(120)
    SetChrSubChip(0xA, 0x2)
    Sleep(250)

    ChrTalk(
        0xA,
        "#00305F#5PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PHow to say it, because\x01",
            "you're an adult I'm\x01",
            "always counting on you.\x02\x03",
            "#00000FBut, that way made me\x01",
            "a little happy as a comrade\x01",
            "you can confess yourself to.\x02\x03",
            "And that's probably not just me...\x01",
            "But all the others think the same too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00305F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PAlso...\x01",
            "Isn't it a mere impression that\x01",
            "you're a jaeger to the core?\x02\x03",
            "#00008FAt least, I can't think you're\x01",
            "the type who undertakes\x01",
            "wars for mira.\x02\x03",
            "#00000FYou're frivolous, like nightlife, and since\x01",
            "you're a little belligerent you tend to heat up,\x01",
            "but you properly know when it's time to quit...\x02\x03",
            "#00002FAlso, you're the senior member\x01",
            "who always helps us juniors...\x02\x03",
            "#00009FThat's the man called Randy\x01",
            "Orlando who I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00305F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PSo you don't need to worry\x01",
            "just because you showed us a\x01",
            "little bit of your lame side.\x02\x03",
            "#00000FRather, Elie, I and\x01",
            "the others prefer──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00303F#5P──I got it, stop what you're sayin'.\x02\x03",
            "#00306FIt seem I was still takin'\x01",
            "lightly your potential...\x02\x03",
            "#00310FHow much of a ladies' man are you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PL-Ladies' man?\x02\x03",
            "#00006FI don't really get it, but did you\x01",
            "say that to snap back at me?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x19, 1, 0, 16)

    ChrTalk(
        0xA,
        (
            "#00315F#5PAh, jeez, I'm feelin' stupid\x01",
            "for bein' depressed...\x02\x03",
            "#00306FIn this case, I'm gonna\x01",
            "fully enjoy Michelam!\x02\x03",
            "#00301FI'll have fun at Michelam until I drop\x01",
            "and tonight I'll hit on babes!\x02\x03",
            "#00307FAnd you'll come too, you damn younger brother!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PR-Roger.\x02\x03",
            "#00002F(I don't really get it, but...\x01",
            "Was I able to cheer him up?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 980, 0, -10170, 270)
    SetChrSubChip(0xA, 0x1)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 3)
    EventEnd(0x5)
    Return()

    # Function_14_2D38 end

    def Function_15_3D3D(): pass

    label("Function_15_3D3D")

    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x28)
    Return()

    # Function_15_3D3D end

    def Function_16_3D65(): pass

    label("Function_16_3D65")

    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x64)
    Return()

    # Function_16_3D65 end

    def Function_17_3D8D(): pass

    label("Function_17_3D8D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08502.itc", 0x1E)
    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    LoadChrToIndex("chr/ch05102.itc", 0x20)
    LoadChrToIndex("chr/ch07502.itc", 0x21)
    LoadChrToIndex("chr/ch10002.itc", 0x22)
    LoadChrToIndex("chr/ch05502.itc", 0x23)
    LoadChrToIndex("chr/ch05602.itc", 0x24)
    LoadChrToIndex("chr/ch00102.itc", 0x25)
    LoadChrToIndex("chr/ch00202.itc", 0x26)
    LoadChrToIndex("chr/ch02902.itc", 0x28)
    LoadChrToIndex("chr/ch03002.itc", 0x29)
    LoadChrToIndex("chr/ch02702.itc", 0x2A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x26)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x2)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x1)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x18, 1, 0, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x2)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0x102, 1000, -800, 7350, 0)
    SetChrPos(0x17, 0, -800, 7350, 0)
    SetChrPos(0x103, -2200, 150, -13850, 180)
    SetChrPos(0x18, -1200, 0, -14850, 270)
    SetChrPos(0x104, -3550, 150, -3850, 180)
    SetChrPos(0x105, -2350, 150, -3850, 180)
    SetChrPos(0x109, 2100, 150, -11350, 180)
    SetChrPos(0x12, 3250, 150, -11350, 180)
    SetChrPos(0x15, -3550, 150, -8850, 180)
    SetChrPos(0x16, -2350, 150, -8850, 180)
    SetChrPos(0x14, 2100, 150, -8850, 180)
    SetChrPos(0x13, 3250, 150, -8850, 180)
    OP_68(0, 1000, -15000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, 10000, 20000)
    Sleep(14000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3D8D end

    SaveToFile()

Try(main)
