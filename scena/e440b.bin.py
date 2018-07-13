from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e440b.bin",                # FileName
        "e440b",                    # MapName
        "e440b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e440b",                  # 0
        "Rixia",                  # 1
        "Divine Wolf Zeit",       # 2
        "Elie",                   # 3
        "Tio",                    # 4
        "Randy",                  # 5
        "Noｱl",                  # 6
        "Wazy",                   # 7
        "SE制御",                 # 8
    ))

    AddCharChip((
        "chr/ch03200.itc",                   # 00
        "chr/ch02708.itc",                   # 01
    ))

    DeclNpc(2589,    0,       4294967267, 90,   453,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294965747, 0,       4294966337, 180,  405,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(456, 0)                                        # 0

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_278",          # 01, 1
        "Function_2_311",          # 02, 2
        "Function_3_385",          # 03, 3
        "Function_4_A86",          # 04, 4
        "Function_5_EDA",          # 05, 5
        "Function_6_1941",         # 06, 6
        "Function_7_1E3A",         # 07, 7
        "Function_8_3907",         # 08, 8
        "Function_9_3946",         # 09, 9
        "Function_10_5A4B",        # 0A, 10
        "Function_11_5A68",        # 0B, 11
        "Function_12_5AC9",        # 0C, 12
        "Function_13_5AE6",        # 0D, 13
        "Function_14_8259",        # 0E, 14
        "Function_15_8275",        # 0F, 15
        "Function_16_9F58",        # 10, 16
        "Function_17_C61D",        # 11, 17
        "Function_18_E942",        # 12, 18
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_200"),
        (1, "loc_20C"),
        (2, "loc_218"),
        (3, "loc_224"),
        (4, "loc_230"),
        (5, "loc_23C"),
        (6, "loc_248"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_200")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_20C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_218")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_224")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_230")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_23C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_248")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_277")

    Return()

    # Function_0_1C8 end

    def Function_1_278(): pass

    label("Function_1_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0")
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x40)

    label("loc_29B")

    ClearChrFlags(0x9, 0x80)

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_310")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_2C0")
    Event(0, 7)
    Jump("loc_310")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_2D1")
    Event(0, 9)
    Jump("loc_310")

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_2E2")
    Event(0, 13)
    Jump("loc_310")

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_2F3")
    Event(0, 15)
    Jump("loc_310")

    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_304")
    Event(0, 16)
    Jump("loc_310")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_310")
    Event(0, 17)

    label("loc_310")

    Return()

    # Function_1_278 end

    def Function_2_311(): pass

    label("Function_2_311")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF0A070D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    SetMapObjFrame(0x0, "door_l1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_l2", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r2", 0x0, 0x1)
    Sound(132, 1, 70, 0)
    Sound(497, 1, 40, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_384")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_384")

    Return()

    # Function_2_311 end

    def Function_3_385(): pass

    label("Function_3_385")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6A), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A8")
    Call(0, 5)
    Jump("loc_443")

    label("loc_3A8")


    ChrTalk(
        0x8,
        (
            "#10704F...I want to feel the\x01",
            "wind here for awhile.\x02\x03",
            "#10702FThere is no need to rush. Please take you time,\x01",
            "and come when you have finished preparing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_443")

    Jump("loc_A82")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D9")
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#10708F...It's finally tomorrow... Our\x01",
            "infiltration of Crossbell City.\x02\x03",
            "#10702FI haven't been away that\x01",
            "long, so why am I getting\x01",
            "this nostalgic feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see...\x02\x03",
            "#00006FThey said the "Aions" are focusing on city\x01",
            "defense now that the barrier's down, but...\x02\x03",
            "#00008FI wonder how the people of\x01",
            "Arc-en-ciel are doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704FProbably... they're continuing\x01",
            "to practice, even now.\x02\x03",
            "No matter what happens, or when, to\x01",
            "enhance the degree of perfection of a play,\x01",
            "you only must look forward and not waver...\x02\x03",
            "#10710FThat's Miss Ilya's will... \x01",
            "The way of life at Arc-en-ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHa ha, that might actually be true.\x02\x03",
            "#00000F...When we liberate Crossbell\x01",
            "City and solve this incident...\x01",
            "What do you plan to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F...I want to see Miss Ilya, and\x01",
            "continue to dance at Arc-en-ciel \x01",
            "as an artist as I did before...\x02\x03",
            "That will exists, but even\x01",
            "now, I don't understand it.\x02\x03",
            "#10708FWhen I reunite with Miss Ilya\x01",
            "and Sully, what should I say...?\x01",
            "No words come to mind even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...I see.\x02\x03",
            "#00000FBut, I'm sure Miss Ilya and\x01",
            "everyone at Arc-en-ciel\x01",
            "will accept you.\x02\x03",
            "Maybe you shouldn't think too hard about it,\x01",
            "and focus on what's in front of you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10704F...Ha ha, you're certainly right about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, none of that will happen\x01",
            "if we don't liberate Crossbell City.\x02\x03",
            "#00000FWe must both do our best tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10702FRight...!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_A82")

    label("loc_9D9")

    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#10704FStaring lazily at the moon\x01",
            "tonight, I feel my heart calm.\x02\x03",
            "#10710FTo liberate Crossbell City\x01",
            "and Arc-en-ciel, I must do\x01",
            "my very best tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_A82")

    TalkEnd(0xFE)
    Return()

    # Function_3_385 end

    def Function_4_A86(): pass

    label("Function_4_A86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5D")

    ChrTalk(
        0x9,
        (
            "#01200F#3CThe Crossbell City liberation operation\x01",
            "tomorrow... I plan to disembark in\x01",
            "Crossbell City as a scout.\x02\x03",
            "#01203FI will not be where you all are, but I\x01",
            "will come rushing if anything happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I'm counting on you.\x02\x03",
            "#00004FCome to think of it, will the\x01",
            "Divine Wolves in the mountain\x01",
            "region be helping us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3CYes. I told them\x01",
            "to support the\x01",
            "CGF Resistance.\x02\x03",
            "If they use the terrain to their\x01",
            "advantage, they should provide an\x01",
            "even match for "Red Constellation".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see... It looks like we'll be counting\x01",
            "on them to support 2nd Lt. Mireille\x01",
            "and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3CWell, that's all the assistance\x01",
            "we can provide you.\x02\x03",
            "In the end, it will be your\x01",
            "duty to take back KeA.\x02\x03",
            "#01203FVarious difficulties await you\x01",
            "before reaching her, but I'm\x01",
            "sure you know that already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... But, I will take back\x01",
            "KeA no matter what happens.\x02\x03",
            "#00000FPlease, watch over us too, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3CHm...\x01",
            "I shall.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 6)
    Jump("loc_ED6")

    label("loc_E5D")


    ChrTalk(
        0x9,
        (
            "#01200F#3CIn the end, it will be your\x01",
            "duty to take back KeA.\x02\x03",
            "Can you succeed? I shall\x01",
            "watch that with my own eyes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED6")

    TalkEnd(0xFE)
    Return()

    # Function_4_A86 end

    def Function_5_EDA(): pass

    label("Function_5_EDA")

    EventBegin(0x0)
    Fade(500)
    OP_68(3230, 200, 1330, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11810, 0)
    SetChrPos(0x101, 1070, 0, 280, 90)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_END)), "loc_F34")
    OP_93(0x8, 0x10E, 0x0)

    label("loc_F34")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A1")

    ChrTalk(
        0x101,
        (
            "#6P#00005FRixia... What are\x01",
            "you doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#10712FAh... Mr. Lloyd.\x02\x03",
            "#10710F...Yes, I've finished preparing for tomorrow, \x01",
            "so I was doing a little thinking.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#11P#10708F#5P...It's finally tomorrow... Our\x01",
            "infiltration of Crossbell City.\x02\x03",
            "#10702FI haven't been away that\x01",
            "long, so why am I getting\x01",
            "this nostalgic feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FI see...\x02\x03",
            "#00006FThey said the "Aions" are focusing on city\x01",
            "defense now that the barrier's down, but...\x02\x03",
            "#00008FI wonder how the people of\x01",
            "Arc-en-ciel are doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10704F#5PProbably... They're continuing\x01",
            "to practice, even now.\x02\x03",
            "No matter what happens, or when, to\x01",
            "enhance the degree of perfection of a play,\x01",
            "you only must look forward and not waver...\x02\x03",
            "#10710FThat's Miss Ilya's way of life...\x01",
            "And the Arc-en-ciel way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FHa ha, that might actually be true.\x02\x03",
            "#00000F...When we liberate Crossbell\x01",
            "City and solve this incident...\x01",
            "What do you plan to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#10704F...I want to see Miss Ilya, and\x01",
            "continue to dance at Arc-en-ciel \x01",
            "as an artist as I did before...\x02\x03",
            "That will exists, but even\x01",
            "now, I don't understand it.\x02\x03",
            "#10708FWhen I reunite with Miss Ilya\x01",
            "and Sully, what should I say...?\x01",
            "No words come to mind even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F...I see.\x02\x03",
            "#00000FBut, I'm sure Miss Ilya and\x01",
            "everyone at Arc-en-ciel\x01",
            "will accept you.\x02\x03",
            "Maybe you should just be\x01",
            "yourself, and not think\x01",
            "too hard about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#10712F...Be myself...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#10703F...Um, Mr. Lloyd?\x02\x03",
            "#10701FLater...may I take just\x01",
            "a bit of your time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10704FUh uh. Even if I say so myself, I\x01",
            "think I've been too guarded lately...\x02\x03",
            "#10710FBefore tomorrow's operation,\x01",
            "I would like to chat with\x01",
            "you for a little while.\x02\x03",
            "When you're through preparing,\x01",
            "would you care to come to the deck\x01",
            "once more, and speak with me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_1768")

    label("loc_16A1")


    ChrTalk(
        0x8,
        (
            "#11P#10704FBefore tomorrow's operation,\x01",
            "I would like to chat with\x01",
            "you for a little while.\x02\x03",
            "#10710FWhen you're through preparing,\x01",
            "would you care to come to the deck\x01",
            "once more, and speak with me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1768")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Rixia's Invitation\x01",      # 0
            "Decline\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A5")

    ChrTalk(
        0x101,
        "#6P#00002FYeah, if you're ok with me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10709FUh uh, thank you very much.\x02\x03",
            "#10704F...I want to feel the\x01",
            "wind here for awhile.\x02\x03",
            "#10702FThere is no need to rush. Please take you time,\x01",
            "and come when you have finished preparing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 6)
    SetScenarioFlags(0x1AB, 0)
    Jump("loc_192E")

    label("loc_18A5")


    ChrTalk(
        0x8,
        (
            "#11P#10704F...I see.\x02\x03",
            "#10702FUh uh. If you change your mind, that's\x01",
            "fine. Please speak with me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, got it.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_192E")

    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_5_EDA end

    def Function_6_1941(): pass

    label("Function_6_1941")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_1A09")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Elie for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Elie for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 3)
    Jump("loc_1E39")

    label("loc_1A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_1AC4")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Tio for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Tio for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 4)
    Jump("loc_1E39")

    label("loc_1AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_1B83")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Randy for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Randy for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 5)
    Jump("loc_1E39")

    label("loc_1B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_1C40")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Noｱl for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Noｱl for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 6)
    Jump("loc_1E39")

    label("loc_1C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_1CFD")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Wazy for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Wazy for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 7)
    Jump("loc_1E39")

    label("loc_1CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_1DBC")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to apologize to\x01",
            "Rixia for not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Rixia for not\x01",
            "being able to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AB, 0)
    Jump("loc_1E39")

    label("loc_1DBC")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F(...I'll head to the deck once\x01",
            "my preparations for tomorrow\x01",
            "are complete at the nap room.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1E39")

    Return()

    # Function_6_1941 end

    def Function_7_1E3A(): pass

    label("Function_7_1E3A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00100.itc", 0x1E)
    LoadChrToIndex("apl/ch51800.itc", 0x1F)
    LoadChrToIndex("apl/ch5180A.itc", 0x20)
    LoadChrToIndex("apl/ch5180B.itc", 0x21)
    SoundLoad(3411)
    SoundLoad(3412)
    SoundLoad(3413)
    SoundLoad(3414)
    SoundLoad(3415)
    SoundLoad(3416)
    SoundLoad(3417)
    SoundLoad(3418)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_63(0xA, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(2000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    OP_64(0xA)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00108F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0xA, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_200F():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_200F)

    def lambda_2024():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2024)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00002F#5PAh, Elie. You got\x01",
            "here first, huh.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2072():

        label("loc_2072")

        TurnDirection(0xA, 0x101, 500)
        Yield()
        Jump("loc_2072")

    QueueWorkItem2(0xA, 2, lambda_2072)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xA,
        (
            "#3411V#30WYes... Lloyd,\x01",
            "good work today.\x02\x03",
            "#3412VAre you finished\x01",
            "preparing for tomorrow?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD54)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0xF, 1, 0, 8)

    def lambda_219C():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_219C)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_68(350, 1000, -3890, 50000)
    MoveCamera(44, 14, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16880, 50000)

    ChrTalk(
        0x101,
        (
            "#00000F#5PYeah, I'm all set.\x02\x03",
            "#00006FAs expected... I can't say I'm \x01",
            "really fully prepared, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2179, 255, 100, 0)

    ChrTalk(
        0xA,
        "#00109F#11P#30W*giggle*...\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0xB4, 0x190)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00104F#5P#30W...It's strange... \x01",
            "This is a critical situation, and yet...\x02\x03",
            "I don't know why, \x01",
            "but my heart is calm.\x02\x03",
            "#00108FBell, "uncle"\x01",
            "and KeA...\x02\x03",
            "#00102FThere's a lot of things I'm anxious\x01",
            "and worried about, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00004F#5PMe too... I feel the same.\x02\x03",
            "#00008FMaybe because I've resolved myself,\x01",
            "or because I can see what I have to do.\x02\x03",
            "#00002FThis too, is thanks to\x01",
            "everyone, Elie included.\x02\x03",
            "#00009FThank you, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00102F#5P*giggle*...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00104F#11PI'm the one who should be thanking you.\x02\x03",
            "#00108FEven though normally, I would\x01",
            "be beside myself with worry...\x02\x03",
            "#00102FIt's because you were there\x01",
            "for me that I can stand\x01",
            "here today like this...\x02\x03",
            "#00104F...Thank you. I'm so\x01",
            "glad you were there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#6PElie...\x02\x03",
            "#00012FHa ha... If I was of use\x01",
            "to you, I'm honored.\x02\x03",
            "#00004FI guess I was able to grow up to\x01",
            "at least be counted on a little\x01",
            "as a leader...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#11P*giggle*, you've been our leader\x01",
            "for a long time already.\x02\x03",
            "Without you, I don't think all of us\x01",
            "would have been able to come this far.\x02\x03",
            "#00108FBut── That's not what \x01",
            "I wanted to say to you.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#00106F#5P...This incident.\x02\x03",
            "No matter how it ends, it will\x01",
            "spell big trouble for Crossbell.\x02\x03",
            "#00108FProbably, our Support Section won't\x01",
            "continue to exist as it is now...\x02\x03",
            "We all will have to do our best\x01",
            "in different positions to use\x01",
            "our abilities to the maximum.\x02\x03",
            "#00101FTo rebuild Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P...Yeah.\x02\x03",
            "#00008FI'll remain a police officer...\x02\x03",
            "Randy will probably want to\x01",
            "cooperate with the CGF after they\x01",
            "revert from being the State Guard.\x02\x03",
            "#00003FTio might want to return to the Foundation\x01",
            "in the orbal networking field...\x02\x03",
            "#00001F...And you, Elie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#5P...The administration and diplomacy\x01",
            "fields of crisis management.\x02\x03",
            "I think what I desire most\x01",
            "is knowledge and ability.\x02\x03",
            "#00108FAnd, I've accumulated a lot of\x01",
            "that through my studies abroad.\x02\x03",
            "#00102FNaturally, I want to obtain the power\x01",
            "to deal with incidents like this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P#30W...I see...\x02\x03",
            "#00006F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00104F#5P*giggle*... Thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P...Huh...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00102F#5PIt seems like you feel a bit\x01",
            "sad thinking about that.\x02\x03",
            "#00106FIf you said something like "It's all right, \x01",
            "you can do it, Elie", I don't know how\x01",
            "I would have reacted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PHa ha...\x02\x03",
            "#00006F...Normally, I'd have to\x01",
            "say it like that, but...\x02\x03",
            "#00008FIt seems it's not that easy to part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#5PWhat do you mean by that...?\x02\x03",
            "#00100FIs it because I'm leaving,\x01",
            "just like Tio and Randy...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00113F#5P──Answer me, Lloyd.\x02\x03",
            "If I'm worried about anything right\x01",
            "now, it's how you will answer...\x02\x03",
            "#00108FYou...already know, right?\x02\x03",
            "#00116FAbout why...\x01",
            "I said I wanted to talk to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P...Elie...\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_93(0x101, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -4250, 180)
    SetChrPos(0xA, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#5PAt first, you see... \x01",
            "It was just admiration.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x514, 0x5, 0x0, 0x1, 0x2, 0x1, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        "#00105F#11PEh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PThis girl was lovely, commanding\x01",
            "and yet she was broad-minded too...\x02\x03",
            "#00000FAnd ever since I met her, I thought she\x01",
            "was a beautiful person in many ways.\x02\x03",
            "#00002FEven so, at first, I spoke to\x01",
            "her, pretending to be cool but...\x02\x03",
            "#00012FI'll confess... My heart had been\x01",
            "beating fast the entire time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x4, 0x5, 0x6)
    Sleep(300)

    ChrTalk(
        0xA,
        "#00112F#11P#30WL-Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5POf course within a month I\x01",
            "realized she was a milady\x01",
            "living in a world beyond my reach.\x02\x03",
            "Even so, this whole time...\x01",
            "I was secretly proud of the\x01",
            "fact she was my co-worker.\x02\x03",
            "#00002FShe received advices from me,\x01",
            "and I was happy to be helpful\x01",
            "to her, if only a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00102F#11P............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x6, 0x7, 0x8)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#6POne year passed, and we got\x01",
            "through things both happy\x01",
            "and painful together...\x02\x03",
            "We got split up for awhile\x01",
            "but finally reunited...\x02\x03",
            "#00008FEven now I'm like when we met...\x02\x03",
            "#00002FNo, my heart is racing even more than then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00116F#11P...Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P──I love you, Elie.\x02\x03",
            "As a comrade and as family,\x01",
            "but not just that.\x02\x03",
            "#00000FYou are my one and only girl.\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 70, 0)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0xB, 0xC, 0xD)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#00106F#3413V#11PLloyd...\x02",
    )

    CloseMessageWindow()
    OP_A1(0xA, 0x640, 0x4, 0xD, 0xE, 0xF, 0x10)

    def lambda_33F9():

        label("loc_33F9")

        OP_A0(0xFE, 1000, 0x10, 0x12)
        Yield()
        Jump("loc_33F9")

    QueueWorkItem2(0xA, 3, lambda_33F9)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00116F#3414V#11PI too── I love you.\x02",
    )

    CloseMessageWindow()
    OP_24(0xD56)
    Sleep(300)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    OP_68(400, 1000, -4250, 1200)

    def lambda_3462():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3462)
    Sleep(50)

    def lambda_347A():
        OP_A0(0xFE, 1000, 0x1, 0x5)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_347A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(812, 0, 100, 0)

    def lambda_34B0():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_34B0)

    def lambda_34BD():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_34BD)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Fade(800)
    SetCameraDistance(15000, 1000)

    def lambda_34E0():
        OP_A0(0xFE, 1000, 0x9, 0xC)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_34E0)
    OP_A0(0xA, 1000, 0x9, 0xC)
    Sleep(300)
    OP_A0(0xA, 1000, 0x19, 0x1E)
    Sleep(300)

    ChrTalk(
        0xA,
        "#3415V#11P#40W#2S...Mmm...\x02",
    )

    CloseMessageWindow()
    OP_24(0xD57)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    Sound(812, 0, 100, 0)

    def lambda_3533():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3533)

    def lambda_3540():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3540)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3668")

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WHa ha...\x02\x03",
            "#00002F...I guess we were finally able to\x01",
            "continue what we started back then...?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        (
            "#00104F#3416V#11P#40W...Yes...\x02\x03",
            "#00116F#3417VI've waited this whole, whole time...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD59)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        "#00012F#6P#40WSorry to keep you waiting.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36C3")

    label("loc_3668")


    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WThis is how I've felt\x01",
            "this whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00104F#11P#40W...Me too...\x02",
    )

    CloseMessageWindow()

    label("loc_36C3")

    Sleep(300)

    def lambda_36CB():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_36CB)
    Sleep(50)

    def lambda_36DB():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_36DB)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W──Even if we cannot follow\x01",
            "the same career paths...\x02\x03",
            "#00004FWe'll always need each other, and\x01",
            "continue to support each other...\x02\x03",
            "#00002FAre you fine with that kind of relationship?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xA, 1300, 0x12, 0x17)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00109F#3418V#11P#40W...Yes...!\x02",
    )

    CloseMessageWindow()
    OP_24(0xD5A)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x157C)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_382D")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_382D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_383F")
    Jump("loc_38E4")

    label("loc_383F")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Elie learned\x01",
            "Star Blast III.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Elie's "Star Blast" \x01",
            "has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x1, 0x1AE)
    AddCraft(0x0, 0x1AE)

    label("loc_38E4")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x28, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 1)
    OP_29(0xB1, 0x1, 0x1)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1E3A end

    def Function_8_3907(): pass

    label("Function_8_3907")

    OP_25(0x84, 0x41)
    OP_25(0x1F1, 0x23)
    Sleep(300)
    OP_25(0x84, 0x3C)
    OP_25(0x1F1, 0x1E)
    Sleep(300)
    OP_25(0x84, 0x37)
    OP_25(0x1F1, 0x19)
    Sleep(300)
    OP_25(0x84, 0x32)
    OP_25(0x1F1, 0x14)
    Sleep(300)
    OP_25(0x84, 0x2D)
    Sleep(300)
    OP_25(0x84, 0x28)
    Sleep(300)
    OP_25(0x84, 0x23)
    Return()

    # Function_8_3907 end

    def Function_9_3946(): pass

    label("Function_9_3946")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00200.itc", 0x1E)
    LoadChrToIndex("apl/ch51801.itc", 0x1F)
    LoadChrToIndex("apl/ch51802.itc", 0x20)
    SoundLoad(2698)
    SoundLoad(2699)
    SoundLoad(2700)
    SoundLoad(2701)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00202.itp")
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xB, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_3A74():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A74)

    def lambda_3A89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3A89)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5P(Huh, Tio...?)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 250, 0, 1250, 180)
    SetChrPos(0xB, 500, 0, -3750, 180)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7500, 0)
    OP_68(500, 2300, -3750, 3000)
    MoveCamera(125, -5, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(8500, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xB,
        "#00208F#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00000F#6P#N──Tio?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_68(320, 1000, -2950, 5000)
    MoveCamera(115, 15, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9000, 5000)

    def lambda_3C09():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF92A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C09)
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_0D()

    def lambda_3C51():

        label("loc_3C51")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3C51")

    QueueWorkItem2(0xB, 2, lambda_3C51)
    Sleep(1500)
    OP_64(0xB)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xB, 500)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xB,
        "#2698V#40WMr.... Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA8A)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha, you don't see that every day.\x02\x03",
            "#00002FYou didn't notice me until\x01",
            "I called out to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        "#00204F#2699V#11P#40WUh uh... You are right.\x02",
    )

    CloseMessageWindow()
    OP_24(0xA8B)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -3750, 3000)
    MoveCamera(135, 20, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(9000, 3000)
    OP_95(0x101, -500, 0, -3750, 1200, 0x0)
    TurnDirection(0x101, 0xB, 500)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#12PI've finished preparing for tomorrow.\x02\x03",
            "#00000FI can't say I'm fully prepared, but considering\x01",
            "what everyone else is dealing with, \x01",
            "I think this is the best I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F#5PYes...\x02\x03",
            "We have to do our best to meet\x01",
            "with KeA, Chief and the others.\x02\x03",
            "#00202FI am worried about Koppe too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PI see...\x02\x03",
            "#00005F...Come to think of it, Jona\x01",
            "has been sent to Michelam.\x02\x03",
            "I wonder how the Foundation's\x01",
            "Chief Roberts is doing.\x02\x03",
            "#00008FThe situation being what it is... Maybe he \x01",
            "returned to the autonomous state of Leman?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00206F#5PNo. It seems Chief Roberts\x01",
            "didn't comply with the\x01",
            "evacuation order.\x02\x03",
            "#00208FIt seems he stayed behind in the city\x01",
            "to check the status of the orbal net that\x01",
            "Miss Mariabell and the others took control of...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x1, 0x3)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#00206F#5PWell considering who it is,\x01",
            "I think he will evasively\x01",
            "avoid capture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PI see... I'm a little worried, though.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1200, 0x3, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00202F#5PYes...\x01",
            "Just a little, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(1000)
    SetChrSubChip(0xB, 0x4)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xB, 500, 0, -4250, 270)
    OP_68(0, 1100, -4250, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 25, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16000, 50000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00206F#11P──Mr. Lloyd.\x02\x03",
            "#00208FCan you give me some advice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, of course.\x02\x03",
            "#00001FCould it be about that letter\x01",
            "you were looking at before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00206F#11PSo you noticed...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x4, 0x6)
    Sleep(500)
    Sound(802, 0, 100, 0)
    OP_A0(0xB, 1000, 0x7, 0x8)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00203F#11PMr. Abbas delivered it\x01",
            "to me yesterday...\x02\x03",
            "#00201FIt is from my parents who came\x01",
            "to the Republic's Altair City.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#6PWhat...!?\x02\x03",
            "#00002FThen, they came all the way\x01",
            "from Remiferia to see you...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00206F#11PYes. They couldn't get in contact via\x01",
            "letters or communications ever since\x01",
            "independence was declared...\x02\x03",
            "It seems they relied on information from\x01",
            "the Foundation and came to the border city.\x02\x03",
            "#00208FRight now, coming and going is\x01",
            "completely restricted aside from cargo,\x01",
            "so they ended up being induced to stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see...\x02\x03",
            "#00000F...If that's the case, then tell me sooner!\x01",
            "This ship can go to Altair City and──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1300, 0x8, 0xA)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#00204F#11PThat is unnecessary.\x02\x03",
            "I have already told them I am safe,\x01",
            "the same way I got their letter.\x02\x03",
            "#00208FAnd, if I see them now, I will lose my\x01",
            "composure and be a hindrance tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P...B-But...\x02\x03",
            "#00006F#30W............\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 800, 0xA, 0x8)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00209F#11PUh uh... \x01",
            "Please don't make that face.\x02\x03",
            "#00202FI will definitely see my parents\x01",
            "after this incident is resolved.\x02\x03",
            "#00204FBecause of you, Mr. Lloyd,\x01",
            "I was a little homesick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0xB, 1000, 0xD, 0xB)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00208F#5P#30W...Everyone was separated...\x02\x03",
            "I was anxious and lonely, and\x01",
            "when I heard you were wanted, I\x01",
            "was so worried my heart ached...\x02\x03",
            "#00206F...Honestly, I was really happy...\x02\x03",
            "That I got to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30WOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F#5P#30WThat time, I thought..\x02\x03",
            ""Yes── I am alive".\x02\x03",
            "#00208FI thought that among people I know,\x01",
            "I have some I hold very dear.\x02\x03",
            "#00202F...How should I live,\x01",
            "and for what reason...\x02\x03",
            "#00209FI felt like I understood the\x01",
            "answers to the questions I tried\x01",
            "asking Mr. Guy three years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6P#30W...Tio...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 1300, 0xB, 0xD)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00206F#11P#30WSince then, I have met Miss Elie,\x01",
            "Mr. Randy and the others...\x02\x03",
            "#00208FAnd we have all done our very best\x01",
            "to come this far for KeA's sake...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(812, 0, 60, 0)
    OP_A0(0xB, 1200, 0xD, 0x10)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00212F#11P#30W...And when I read this\x01",
            "letter, my real feelings \x01",
            "gushed forth.\x02\x03",
            "#00213FIt has been awhile... Since I have \x01",
            "wanted to see my father and mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(400, 1000, -4250, 1200)
    OP_9A(0x101, 0xB, 0x258, 0x1F4, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)

    def lambda_4C29():
        OP_A0(0xFE, 1000, 0x10, 0x13)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_4C29)

    def lambda_4C36():
        OP_A0(0xFE, 1000, 0x20, 0x23)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4C36)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sound(898, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 10)
    BeginChrThread(0x101, 3, 0, 12)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0xB,
        "#00216F#11P#40W#2S...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W...Thank goodness.\x01",
            "Really, thank goodness...\x02\x03",
            "I'll take this opportunity and, well, \x01",
            "maybe it's a little awkward, but...\x02\x03",
            "#00002FTio, the fact that you've become\x01",
            "able to feel that way makes\x01",
            "me happier than anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x5, 0x13, 0x18, 0x19, 0x18, 0x13)
    Sleep(300)

    ChrTalk(
        0xB,
        "#00215F#11P#30W...Mr. Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    Fade(1000)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 0, 0, -3750, 90)
    SetChrPos(0xB, 500, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(140, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 20, 0, 50000)
    SetCameraDistance(9000, 50000)

    def lambda_4E27():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E27)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_A1(0xB, 0x320, 0x3, 0x1, 0x2, 0x3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00204F#5P#30W...I have two requests.\x02\x03",
            "Will you hear them?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00002F#12PYeah── Ask me anything you want.\x02\x03",
            "#00009FAnd don't hold back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00208F#5P#30WThen, firstly...\x02\x03",
            "#00208FI really love it when\x01",
            "you pat my head, but...\x02\x03",
            "#00201FOn a beautiful night like this,\x01",
            "I feel it is too childlike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#12PR-Really?\x02\x03",
            "#00012FWait, when my big brother\x01",
            "or Randy did it to me, it\x01",
            "made me feel like a kid...\x02\x03",
            "#00000FUmm, then...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 11)
    Sleep(1500)
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 1950, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#12PT-Tio...?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_A1(0xB, 0x3E8, 0x5, 0x1E, 0x2B, 0x2C, 0x2B, 0x1E)
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            "#40WY-You know...\x02\x03",
            "When we reunited, \x01",
            "I ran and hugged you...\x01",
            "You looked in pain a little...\x02\x03",
            "...It should be fine like this, \x01",
            "right?\x02",
        )
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
            "#00000F#12P#30WY-Yeah...\x02\x03",
            "#00004F............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(250, 1000, -3750, 1000)
    OP_96(0x101, 0xFFFFFF9C, 0x0, 0xFFFFF15A, 0x1F4, 0x0)
    Fade(250)
    Sound(898, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_5212():
        OP_A0(0xFE, 1000, 0x1E, 0x22)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_5212)

    def lambda_521F():
        OP_A0(0xFE, 1000, 0x36, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_521F)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        (
            "#05524F#2700V#5P#40WUh uh... How warm...\x02\x03",
            "#05526F#2701VI am sorry it doesn't\x01",
            "feel as good as when\x01",
            "Miss Elie does it, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA8D)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00012F#12P#30WW-Well, it is what it is...\x02\x03",
            "#00008F(Or rather, this is bad...\x01",
            "Tio's sweet smell is...)\x02\x03",
            "#00011F(──No, I mustn't!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 60, 0)

    def lambda_5359():
        OP_A0(0xFE, 1000, 0x22, 0x25)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_5359)

    def lambda_5366():
        OP_A0(0xFE, 1000, 0x39, 0x3C)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5366)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00012F#12P*ahhem*... \x01",
            "And, your other request?\x02\x03",
            "#00000FSince we're here, might\x01",
            "as well get on with it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x5, 0x25, 0x2E, 0x2F, 0x2E, 0x25)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#05524F#5PYes, the other one is...\x02\x03",
            "#05522FWhen this incident is settled and\x01",
            "my parents come to Crossbell, \x01",
            "I want to see them with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00009F#12PYes, of course. I was just thinking\x01",
            "of greeting them sometime.\x02\x03",
            "#00002FBut, I guess you shouldn't even\x01",
            "ask for something like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05526F#5PNo, not just a greeting...\x02\x03",
            "#05528FI want to explain simply my reason\x01",
            "for remaining in Crossbell.\x02\x03",
            "#05521FIf I don't, they will\x01",
            "never accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05524F#5PEveryone is here, Michey is\x01",
            "here, there is the orbal net\x01",
            "too and I love Crossbell...\x02\x03",
            "#05528FBut above all, how should I\x01",
            "live, and for what reason...\x02\x03",
            "#05522FI want to live forevermore by the side of the\x01",
            "important person who gave me that answer──\x02\x03",
            "#05529FThat is what I want to try to tell them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00007F#12P#4SWhaaat!?#3S\x02\x03",
            "#00011FW-Wait just a minute here!\x01",
            "That's just like...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x2E)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#05531F#5PYou said to ask you "anything"...\x01",
            "Am I not right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#00012F#12P──Yeah, okay, I get it!\x02\x03",
            "#00002FOnce this incident is resolved,\x01",
            "I'll meet your parents with you!\x02\x03",
            "#00006F*sigh*, I'll have to start\x01",
            "thinking of excuses now...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x3E)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0xB,
        (
            "#05529F#5PUh uh...\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(812, 0, 60, 0)
    SetChrSubChip(0xB, 0x2E)
    Sleep(50)
    SetChrSubChip(0xB, 0x25)
    Sleep(200)
    SetCameraDistance(10500, 3500)

    def lambda_591F():
        OP_A0(0xFE, 1000, 0x26, 0x29)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_591F)

    def lambda_592C():
        OP_A0(0xFE, 1000, 0x3C, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_592C)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_5970")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_5970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5982")
    Jump("loc_5A28")

    label("loc_5982")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Tio learned\x01",
            "Omega Strike III.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Tio's "Omega Strike"\x01",
            "has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1AF)

    label("loc_5A28")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x29, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 2)
    OP_29(0xB1, 0x1, 0x2)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_3946 end

    def Function_10_5A4B(): pass

    label("Function_10_5A4B")

    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_10_5A4B end

    def Function_11_5A68(): pass

    label("Function_11_5A68")

    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A0(0xFE, 900, 0x0, 0x3)
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 900, 0x4, 0xC)
    Sleep(300)
    OP_A0(0xFE, 1000, 0xC, 0xF)
    Sound(318, 0, 100, 0)
    Sleep(200)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x10, 0x14)
    Sleep(500)
    Sound(812, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x14, 0x1B)
    Sleep(300)
    OP_A0(0xFE, 1000, 0x1B, 0x1E)
    Return()

    # Function_11_5A68 end

    def Function_12_5AC9(): pass

    label("Function_12_5AC9")

    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    SetChrSubChip(0xFE, 0x23)
    Return()

    # Function_12_5AC9 end

    def Function_13_5AE6(): pass

    label("Function_13_5AE6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("apl/ch51804.itc", 0x1F)
    LoadChrToIndex("apl/ch51805.itc", 0x20)
    SoundLoad(2778)
    SoundLoad(2779)
    SoundLoad(2780)
    SoundLoad(2781)
    SoundLoad(2782)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis266.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis267.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis268.itp")
    CreatePortrait(4, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis316.itp")
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_5C97():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C97)

    def lambda_5CAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5CAC)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        "#00300F#2778V#12P#N#30WYo, you came.\x02",
    )

    CloseMessageWindow()
    OP_24(0xADA)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00002F#5PRandy.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 500, 0, 1250, 180)
    SetChrPos(0xC, 500, 0, -3750, 0)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    OP_68(500, 1600, -3750, 5000)
    MoveCamera(125, 1, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9500, 5000)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xC,
        (
            "#2779V#40WHonestly, alright, I did invite\x01",
            "you.\x02\x03",
            "But on a night like tonight,\x01",
            "have you really got time to\x01",
            "spare for a dude?\x02\x03",
            "#2780VDon't you have someone with\x01",
            "whom to talk about amorous stuff?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xADC)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(630, 1000, -3200, 3000)
    MoveCamera(120, 10, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10000, 3000)
    Sound(100, 0, 100, 0)

    def lambda_5F3B():

        label("loc_5F3B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5F3B")

    QueueWorkItem2(0xC, 2, lambda_5F3B)
    OP_95(0x101, 250, 0, -1750, 1200, 0x0)
    TurnDirection(0x101, 0xC, 500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...None of your business.\x02\x03",
            "#00001FAlso, it's before the operation... I don't\x01",
            "have time to think about stuff like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#11PDummy. It's precisely because of times\x01",
            "like this that you have to let loose.\x02\x03",
            "#00308F①"Lloyd, I'm worried..."\x02\x03",
            "#00301F②"It's all right, I'm with you..."\x02\x03",
            "#00309F③"*hug*" That's the golden\x01",
            "combo you can use right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PThat last part was a bit of a jump...\x02\x03",
            "#00012FRandy, I'm getting the impression\x01",
            "that your popular attitude is fake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00310F#11POh, really now?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(110, 1000, -4070, 4000)
    MoveCamera(135, 15, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(10000, 30000)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(500)
    EndChrThread(0xC, 0x2)
    OP_93(0xC, 0xB4, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xC,
        "#00300F#5P...Are you done preparin' for tomorrow?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah. Honestly, I can't say\x01",
            "I'm fully prepared, but...\x02\x03",
            "#00001FWhen I think about 2nd Lt. Mireille and\x01",
            "the others, I shouldn't complain at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5PI guess...\x02\x03",
            "#00303FThey'll likely send large numbers of jaegers\x01",
            "to the Resistance and Heiyue areas.\x02\x03",
            "#00308FUncle and Shirley won't come\x01",
            "out that easily, though...\x02\x03",
            "#00301FBut if someone like Gareth appears,\x01",
            "it'll be a pretty tough fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PIs that so...?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    EndChrThread(0xC, 0x2)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6PThe "Red Constellation"... Their battle\x01",
            "power is more than what I've heard.\x02\x03",
            "#00000FI feel like I agree with those who say\x01",
            "they're the strongest in West Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5PWell, if we talk only about history, \x01",
            "it goes back to the Dark Ages.\x02\x03",
            "#00301FBerserker Orlando...\x02\x03",
            "It seems it was a household of warriors,\x01",
            "well known since those times.\x02\x03",
            "#00308FBy constantly adoptin' the latest combat techniques \x01",
            "and strengthenin' their bodies with special training\x01",
            "methods, they have continued to be called the \x01",
            ""strongest" of the warrior corps...\x02\x03",
            "#00303FIn present days, they became a jaeger corps\x01",
            "and took up the name of the red scorpion\x01",
            "that was on the household's coat of arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PSo that's what happened...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xC, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#12PCould it be...\x02\x03",
            "#00001FThat the race in Downtown we did\x01",
            "before was in that form because...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#00309F#5PHa ha, you noticed.\x02\x03",
            "#00300FThat's an arrangement the "Red Constellation"\x01",
            "uses for combat training.\x02\x03",
            "#00306FAlthough originally it's something way closer to\x01",
            "actual combat, so dyin' in it wouldn't be strange.\x02\x03",
            "When I was a kid, I was made to do it\x01",
            "every day until I coughed up blood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00000F#12P...And the one who trained you like that\x01",
            "was your father, the "War God", huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5PYeah──\x01",
            "Balder Orlando.\x02\x03",
            "#00308FHe was a strict and merciless\x01",
            "old man like a steel lion.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_93(0xC, 0xB4, 0x190)
    Fade(1000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#00303F#5P#30W──Three years ago...\x02\x03",
            "I got a certain mission\x01",
            "from that "War God".\x02\x03",
            "#00308FTwo companies of "Zephyr", a jaeger\x01",
            "corps we were longtime enemies with...\x02\x03",
            "#00311FThe mission was to annihilate\x01",
            "them with my own unit.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    SetCameraDistance(15000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30WThe enemy's strength was twice mine...\x02\x03",
            "Thinkin' about goin' up against them,\x01",
            "honestly, it was too severe a difference.\x02\x03",
            "But surprise attacks and use of\x01",
            "terrain advantage were our forte.\x02\x03",
            "And I...\x02\x03",
            "...There was this village I\x01",
            "usually went to for supplies.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30WUsin' a surprise attack as a diversion,\x01",
            "we drew one company into the village...\x02\x03",
            "And by decidin' to cause a landslide,\x01",
            "the other company was utterly crushed.\x02\x03",
            "By explodin' a barn on the outskirts,\x01",
            "we caused the enemy to panic...\x02\x03",
            "Readin' their escape route out of the village,\x01",
            "we concentrated our firepower and crushed them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30W...I intended to sacrifice not\x01",
            "a single one of the villagers.\x02\x03",
            "But, probabilities in battle\x01",
            "are fluid and unreliable.\x02\x03",
            "In the end, the point at which we opened\x01",
            "fire was about 50 arge close to the village...\x02\x03",
            "And one house, the general store, got wrapped up in it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x7D0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#40W...I think I could say he was my\x01",
            "first friend, jaegers excluded.\x02\x03",
            "When I didn't have a mission, I'd drank at the bar\x01",
            "with him, made noise and picked up ladies...\x02\x03",
            "He was saying that his dream was to leave\x01",
            "the town before long and open his own bar.\x02\x03",
            "That dream, and life. All of it was stolen by me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(858, 0, 100, 0)
    Sleep(1500)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    Sleep(1300)
    SetMessageWindowPos(280, 170, -1, -1)
    SetChrName("Shirley")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WWah! You're pretty\x01",
            "good, Randy bro♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Ogre Sigmund")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WHehe── You pass, Randolph.\x02\x03",
            "Because of this "test", it's decided\x01",
            "that you'll be the next "War God".\x02\x03",
            "You should work from now on to be worth\x01",
            "of following in big bro's footsteps.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P#30W...Unsatisfactory, right?\x02\x03",
            "#00308FI didn't particularly want to leave\x01",
            "the battlefield because of his death.\x02\x03",
            "It's more like I was sick and\x01",
            "tired of the life of a jaeger.\x02\x03",
            "#00303FI still don't\x01",
            "understand...\x02\x03",
            "The modest dream of that guy, \x01",
            "who wanted his own bar someday...\x02\x03",
            "And my life of becomin' the "War God" one\x01",
            "day and continue to fight until I die...\x02\x03",
            "#00311FI wonder which of those had meanin'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P#30W...Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00303F#5P#30WThat's probably the\x01",
            ""karma" I'm burdened with.\x02\x03",
            "For bein' born into the Orlando household, but\x01",
            "not becomin' able to be a full warrior, and\x01",
            "livin' on the battlefield in a superficial way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6PRandy, do you intend\x01",
            "to break that "karma"...\x02\x03",
            "#00001FBy surpassin' your uncle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P...I guess.\x02\x03",
            "#00308FThough now that my old man's dead,\x01",
            "there's no way of breaking that "karma."\x02\x03",
            "If I could overcome that monster\x01",
            "with my current strength...\x02\x03",
            "#00300FI feel like I'd finally settle\x01",
            "the score from three years ago.\x02\x03",
            "#00304FThat's all──\x01",
            "So there you have it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_76C7")

    ChrTalk(
        0x101,
        (
            "#00004F#6P...I see...\x02\x03",
            "#00000FOf course, you'll allow me to\x01",
            "assist as your buddy, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_773A")

    label("loc_76C7")


    ChrTalk(
        0x101,
        (
            "#00004F#6P...I see...\x02\x03",
            "#00000FIf you say it like that, then you'll allow\x01",
            "me to assist as your partner, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_773A")

    TurnDirection(0xC, 0x101, 400)
    Sleep(250)

    ChrTalk(
        0xC,
        (
            "#00302F#11PYeah, I'm countin' on you.\x02\x03",
            "#00306FIf possible I'd have liked to settle the score with\x01",
            "my own power, but that opponent is just too much.\x02\x03",
            "#00300FSorry but, can I count on you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7883")

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, of course.\x02\x03",
            "#00002FI feel lucky to be your buddy...\x01",
            "And I'm happy you're relying on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78F1")

    label("loc_7883")


    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, of course.\x02\x03",
            "#00002FI feel lucky to be your friend...\x01",
            "And I'm happy you're relying on me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78F1")


    ChrTalk(
        0xC,
        (
            "#00315F#11PHehe... That's why I always tell you\x01",
            "to stop sayin' sweet words to me.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(1000)
    SetChrPos(0x101, -600, 0, -3750, 90)
    SetChrPos(0xC, 600, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(135, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 15, 0, 70000)
    SetCameraDistance(9000, 70000)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x1)
    OP_0D()
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x1, 0x2, 0x2, 0x2)
    Sound(854, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x2, 0x3, 0x3, 0x3)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0xC, 0x4)
    OP_0D()
    Sleep(300)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#00005FIs that...a bottle of liquor?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xC,
        (
            "#00304F#5PIt's rum. The good stuff.\x02\x03",
            "#00300FIt's the one he and I were\x01",
            "bottle keepin' at the village bar.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00000F#12P...I see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 100, 0)
    Sound(857, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x5, 0x4, 0x5, 0x6, 0x6, 0x6)

    ChrTalk(
        0xC,
        (
            "#00300F#5PI left it with the rifle and\x01",
            "somehow couldn't touch it.\x02\x03",
            "#00304FBut now, I feel like\x01",
            "drinkin' down the rest.\x02\x03",
            "#00302FIt'll liven up this night before battle. \x01",
            "Care to join me for a shot?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#00002F#12PYeah── I'd love to.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_7C41():
        OP_A0(0xFE, 1000, 0x7, 0x8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7C41)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_7C57():
        OP_A0(0xFE, 1000, 0x1, 0x2)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7C57)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0x9)
    OP_0D()
    Sleep(1000)
    Sleep(1000)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0xA)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(1000)
    Sleep(300)

    def lambda_7C9C():
        OP_A0(0xFE, 800, 0xA, 0xC)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7C9C)
    Sleep(100)

    def lambda_7CAC():
        OP_A0(0xFE, 1000, 0x4, 0x6)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7CAC)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#00304F#5P...It was just enough, huh?\x02\x03",
            "#00300FDon't push yourself, ok? \x01",
            "Just a little shoud be plenty intense.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xC, 0x8)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00004F#12PWell, I'm already an adult,\x01",
            "so I'll be fine with this much.\x02\x03",
            "#00000FCheers, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00302F#5PYeah.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7DC7():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7DC7)

    def lambda_7DE0():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7DE0)
    Fade(250)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0xC, 0xD)
    Sleep(50)
    Sound(856, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0xC, 3)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0xC, 0xE)
    SetChrSubChip(0x101, 0x8)
    OP_0D()
    Sleep(1000)

    def lambda_7E2C():
        OP_A0(0xFE, 1000, 0xE, 0x10)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7E2C)
    Sound(2030, 255, 60, 0)
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    WaitChrThread(0xC, 3)
    OP_A1(0xC, 0x3E8, 0x8, 0x10, 0x11, 0x12, 0x12, 0x13, 0x14, 0x13, 0x12)
    OP_A0(0x101, 1000, 0x9, 0xB)

    ChrTalk(
        0x101,
        (
            "#00015F#12P#40W*cough*...\x02\x01",
            "#00008F#30W...It packs a punch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00309F#5PHa ha, told you so.\x02\x03",
            "#00302FWell, this stuff has an\x01",
            "adult flavor, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7F0D():
        OP_A0(0xFE, 1000, 0x15, 0x16)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7F0D)

    def lambda_7F1A():
        OP_A0(0xFE, 1000, 0xC, 0xD)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7F1A)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00013F#12PGuh... Don't consider only\x01",
            "yourself an adult, jeez.\x02\x03",
            "#00004F──Say, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00305F#5PHm, what is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(802, 0, 80, 0)
    OP_A0(0x101, 1000, 0xD, 0xE)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00002F#12PLet's go to the Back Street\x01",
            "jazz bar once all this is over.\x02\x03",
            "There, we can set up a new\x01",
            "bottle keep. Sounds good?\x02\x03",
            "#00012FIf possible, something a\x01",
            "a little less strong, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1950, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x8, 0x16, 0x17, 0x18, 0x18, 0x19, 0x1A, 0x19, 0x18)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        "#00302F#2781V#5P#40WHa ha...right.\x02",
    )

    CloseMessageWindow()
    OP_24(0xADD)
    OP_57(0x0)
    OP_5A()
    OP_A1(0xC, 0x3E8, 0x3, 0x18, 0x19, 0x1A)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        "#00315F#2782V#5P#40WYeah── Let's go there!\x02",
    )

    CloseMessageWindow()
    OP_24(0xADE)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(10500, 3000)
    FadeToDark(2000, 0, -1)
    OP_A1(0xC, 0x3E8, 0x3, 0x1A, 0x19, 0x18)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1194)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_817A")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_817A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_818C")
    Jump("loc_8236")

    label("loc_818C")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Randy learned\x01",
            "Burning Rage III.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Randy's "Burning Rage"\x01",
            "has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x3, 0x1B0)
    AddCraft(0x0, 0x1B0)

    label("loc_8236")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x2A, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 3)
    OP_29(0xB1, 0x1, 0x3)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_5AE6 end

    def Function_14_8259(): pass

    label("Function_14_8259")

    OP_95(0x101, -500, 0, -3750, 1000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_14_8259 end

    def Function_15_8275(): pass

    label("Function_15_8275")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("apl/ch51020.itc", 0x1F)
    LoadChrToIndex("apl/ch51806.itc", 0x20)
    LoadChrToIndex("apl/ch51807.itc", 0x21)
    SoundLoad(3532)
    SoundLoad(3533)
    SoundLoad(3534)
    SoundLoad(3535)
    SoundLoad(4110)
    SoundLoad(3536)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis337.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis338.itp")
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xD, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    BeginChrThread(0xF, 1, 0, 8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        (
            "#10106F#3532V#40W...*sigh*... \x01",
            "...What should I do...\x02\x03",
            "#10108F#3533VAt a time like this...#800W...\x01",
            "#10101F#40WHmm, but if I let this chance go...!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCD)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0xD, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_8511():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8511)

    def lambda_8526():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8526)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        "#00002F#5PNoｱl, you got here first.\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)

    def lambda_8598():

        label("loc_8598")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8598")

    QueueWorkItem2(0xD, 2, lambda_8598)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        (
            "#10112F#3534V#12P#40WM-Mr. Lloyd! \x01",
            "Good work today!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCE)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(35, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_8623():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8623)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xD, 500)
    EndChrThread(0xD, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#6PHa ha, same to you.\x02\x03",
            "#00000FIt looks like you're finished\x01",
            "contacting Commander Sonya?\x02",
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
        0xD,
        (
            "#30WAh, yes.\x02\x03",
            "She said she'll have units\x01",
            "from Bellguard and Tangram\x01",
            "gates standby until noon.\x02\x03",
            "She said she can't intervene\x01",
            "any more than that, though...\x02",
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
        0x101,
        (
            "#00006F#6PI see... Well, even a\x01",
            "temporary standby is helpful.\x02\x03",
            "#00013FIf that's the case, then I think\x01",
            "our duty is even more important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10103F#11PYes......\x02\x03",
            "#10108F#30W............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P...The State Guard in the city will\x01",
            "likely be assigned to city defense.\x02\x03",
            "#00001FI think we can avoid fighting\x01",
            "them in urban areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10106F#11PNo, I'm already\x01",
            "prepared for that.\x02\x03",
            "#10108FIt's just, I was thinking\x01",
            "I'm kind of pathetic.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xD, 500, 0, -3750, 270)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10108F#5P#30WI honestly thought state independence\x01",
            "and the State Guard were mistakes.\x02\x03",
            "#10106FBut I...didn't have the spirit to\x01",
            "join senior Mireille's Resistance\x01",
            "and just went with the flow...\x02\x03",
            "It made me realize that, in a way,\x01",
            "I've been living only within the\x01",
            "small world of the CGF.\x02\x03",
            "#10113FEven though the Commander gave me that\x01",
            "opportunity for a temporary transfer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PEveryone is like that, Noｱl.\x02\x03",
            "#00008FEven me. Were it not for KeA and everyone, I\x01",
            "would have been swept up by that flow as well.\x02\x03",
            "#00012FFor starters, I don't have the personality\x01",
            "to do great things, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#10112F#5PUmm... I don't really\x01",
            "think you're like that.\x02\x03",
            "#10114FIf not, then how could you ever say\x01",
            "something like "You'll be mine"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10112F#5PN-No!\x01",
            "It's nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12P???\x02\x03",
            "#00004FIn any case, what's important\x01",
            "is whether there's a chance.\x02\x03",
            "And you seized that chance\x01",
            "and are here with us.\x02\x03",
            "#00008FIt's not the case that I decide\x01",
            "whether that's right or not, but...\x02\x03",
            "#00002FYou're a great help to us.\x01",
            "──That makes me happiest of all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#10114F#5PM-Mr. Lloyd...\x02\x03",
            "#10106F............\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10108F#11P#30W(C-Calm down,\x01",
            "Noｱl Seeker...!)\x02\x03",
            "#10103F(Just like in training, you have\x01",
            "to quickly assess the situation\x01",
            "and control your morale...!)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12POh right, you said you had\x01",
            "something to ask me...\x02\x03",
            "#00002FUmm, what is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 500)

    ChrTalk(
        0xD,
        (
            "#10105F#5PAh, right!\x01",
            "About that──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0xD,
        (
            "#10106F#5P...Umm... Ah...\x02\x03",
            "#10108FI'm going to ask you\x01",
            "something weird but...\x02\x03",
            "#10101FA-Are you going out with\x01",
            "anyone Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#12PHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10112F#5PN-No! There's no\x01",
            "deep meaning!\x02\x03",
            "#10102FUmm, yeah, Fran and I\x01",
            "were wondering about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#12PO-Oh, I see.\x02\x03",
            "#00012FHa ha. Girls like\x01",
            "stuff like that, eh?\x02\x03",
            "#00006FHmm. I'm sorry to say I don't right now.\x02\x03",
            "#00000FI'm a little disappointed because\x01",
            "there's so many good girls around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10112F#5P#30WA-Ahaha... No way. \x01",
            "(He's not doing this on purpose, right...?)\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(1200)

    ChrTalk(
        0xD,
        "#10103F#5P#30W*ahem*...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xD, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16500, 2000)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    OP_68(0, 1000, -4250, 70000)
    MoveCamera(35, 20, 0, 70000)
    OP_6E(500, 70000)
    SetCameraDistance(14500, 70000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        "#10103F#3535V#11P#40W──Umm, in that case.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xD, 0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#10101F#4110V#11P#40WWill you hold on to\x01",
            "this for me for awhile?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100E)
    OP_C9(0x1, 0x80000000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00005FThis is...\x02\x03",
            "#00001FYour dogtag from the Crossbell Guard Force?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xD,
        (
            "#10104F#11PYes. I didn't need it after changing\x01",
            "over to the State Guard, but...\x02\x03",
            "#10100FSomehow, I couldn't throw it away,\x01",
            "so I've held on to it this whole time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see...\x02\x03",
            "#00005FBut, why me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10106F#11P...Honestly, I think tomorrow's\x01",
            "plan will be difficult.\x02\x03",
            "#10101FIf something happens to me...\x02\x03",
            "#10112FNo── It's to complete the mission. In other words,\x01",
            "I want you to hold on to it for me for good luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PNoｱl...\x02\x03",
            "#00004FGot it. I'll gladly\x01",
            "hold on to it for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(800)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10109F#11POh... \x01",
            "Thank you very much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHa ha, it's not really something\x01",
            "you have to thank me for, though.\x02\x03",
            "#00008FAnd you'll be working\x01",
            "with all of us too...\x02\x03",
            "#00000FSo please, when you're in a pinch,\x01",
            "don't think of sacrificing \x01",
            "yourself for us, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10111F#11P#30WW-Why do you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI just know these things.\x02\x03",
            "#00001FLike I said before, you don't\x01",
            "have to worry about the time\x01",
            "you captured us at all.\x02\x03",
            "#00002FIn the end, I want you to come with us\x01",
            "as a member of the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10114F#11P#30W...Mr. Lloyd...\x02\x03",
            "#10116F*sob*... \x01",
            "...Roger, understood!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6PHa ha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#6PStill, giving your own\x01",
            "dogtag to someone...\x02\x03",
            "#00012FHa ha, it's kind of like\x01",
            "what lovers would do.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10114F#11P......!\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(300)

    def lambda_9A4F():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_9A4F)
    WaitChrThread(0xD, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#6PHuh──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10106F#5P#40W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PNoｱl...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(250)
    Sound(812, 0, 60, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    OP_A1(0x101, 0x320, 0x7, 0x0, 0x1, 0x2, 0x1, 0x2, 0x1, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00011F#6PUmm, ah...\x02\x03",
            "#00012FIs that really\x01",
            "its meaning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10106F#5P#40W............(*nod*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WI-I see...\x02\x03",
            "#00000F............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6PUmm... I don't know if\x01",
            "this is an answer but...\x02\x03",
            "#00000FCould you please hang on to this for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10114F#5P#30WEh...\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x1F4)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x3)
    OP_0D()
    Sleep(150)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)

    AnonymousTalk(
        0xD,
        (
            "#10105F#11PThis is... from the\x01",
            "Crossbell Police?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00002F#6PI really should wear this\x01",
            "as an officer on duty, but...\x02\x03",
            "#00004FUntil this case is solved, I want\x01",
            "you to hang on to it, Noｱl.\x02\x03",
            "#00000FAfter that...\x01",
            "I'll give you a proper answer.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)

    ChrTalk(
        0xD,
        "#10116F#11P#30W#2S...Ah...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        "#10117F#3536V#11P#30WYes── I'd love to!\x02",
    )

    CloseMessageWindow()
    OP_24(0xDD0)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(16000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_9E7B")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_9E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E8D")
    Jump("loc_9F35")

    label("loc_9E8D")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Noｱl learned\x01",
            "Brave Hearts II.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Noｱl's "Brave Hearts" \x01",
            "has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A0)
    AddCraft(0x8, 0x1A0)

    label("loc_9F35")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x25, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 4)
    OP_29(0xB1, 0x1, 0x4)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_8275 end

    def Function_16_9F58(): pass

    label("Function_16_9F58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03100.itc", 0x1E)
    LoadChrToIndex("apl/ch51808.itc", 0x1F)
    LoadChrToIndex("apl/ch51813.itc", 0x20)
    SoundLoad(2926)
    SoundLoad(2927)
    SoundLoad(2928)
    SoundLoad(2929)
    SoundLoad(2930)
    SoundLoad(2430)
    SoundLoad(2431)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10401.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis325.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis349.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis326.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis327.itp")
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xE, 500, 0, -4250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(18500, 2000)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_A125():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A125)

    def lambda_A13A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A13A)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        "#10402F#2926V#11P#30WHey, you came.\x02",
    )

    CloseMessageWindow()
    OP_24(0xB6E)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        "#00000F#5PYeah...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_A1D9():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A1D9)

    def lambda_A1F3():

        label("loc_A1F3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_A1F3")

    QueueWorkItem2(0xE, 2, lambda_A1F3)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xE, 500)
    EndChrThread(0xE, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6PSince you dropped such a tantalizing hint,\x01",
            "I think I had no choice but to come.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xE,
        (
            "#2927V#30WHu hu, although you say it like\x01",
            "that, I like you for having\x01",
            "come out of consideration.\x02\x03",
            "#2928VI don't think it'd be too\x01",
            "much to say I love you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB70)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PLet's leave that aside.\x02\x03",
            "#00001F...It's about KeA, right?\x01",
            "Tell me that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#11PHu hu, roger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9500, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 50000)

    ChrTalk(
        0xE,
        (
            "#10408F#5PI really shouldn't tell\x01",
            "this to an outsider, but...\x02\x03",
            "#10400FWhen it comes to dealing with the\x01",
            ""Sept-Terrion of Zero", the Church has\x01",
            "taken a basically hands-off position.\x02\x03",
            "#10403F──No matter how\x01",
            "this case ends.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#11PSeriously!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10406F#5PYeah. The "Snake"'s guys have retreated,\x01",
            "and now that the original Sept-Terrion is lost, \x01",
            "there's no motive for an active intervention.\x02\x03",
            "#10400FIn that sense, even the option to\x01",
            "take KeA away has disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PI see... Thank you\x01",
            "for letting me know.\x02\x03",
            "#00005FBut Wazy, is there any problem with\x01",
            "you continuing to cooperate with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10403F#5PThe "Fool" and the 7th Anguis have left, however,\x01",
            "withdrawal of the 6th Anguis hasn't been confirmed.\x02\x03",
            "#10408FAlso, starting with those dolls, the technology\x01",
            "the Society gave to the Crois clan will still\x01",
            "have a significant influence...\x02\x03",
            "#10400FUntil that influence is gone, we'll keep\x01",
            "intervening, to a minimum level, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see... \x02\x03",
            "#00001FIt seems like, the more I hear,\x01",
            "the more this fight has gone\x01",
            "afar from our common sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10404F#5PHu hu. The society you all live in is defined by the\x01",
            "interaction of the worlds you can and can't see.\x02\x03",
            "#10402FAnd── I guess the conclusion of\x01",
            "my two-year infiltration mission\x01",
            "to Crossbell will be a big one.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#11PCome to think of it...\x01",
            "You're 17, aren't you Wazy.\x02\x03",
            "#00003FThat means you were assigned a mission\x01",
            "two years ago, when you were 15...\x02\x03",
            "#00001FBut, isn't a "Dominion" a\x01",
            "pretty important position?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10405F#5PWell, a "Dominion" is something you\x01",
            "don't become through achievements.\x02\x03",
            "#10400FOnly those on which the "mark" appears can\x01",
            "become one, and becoming one is preordained...\x02\x03",
            "#10409FWell, it's just an occult\x01",
            "and dubious position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PDon't say that yourself...\x02\x03",
            "#00001F...But this "mark",\x01",
            "could it be that thing I can\x01",
            "see sometimes in battle...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#5PYeah...\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x190)
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xE, 500, 0, -4250, 180)
    OP_68(430, 1000, -4460, 0)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(40, 20, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(15000, 30000)
    OP_0D()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#10403F#5P#30W"Stigma"── That's the\x01",
            "name of this "mark".\x02\x03",
            "#10408FA seal engraved on one's soul...\x01",
            "A detestable source of power.\x02\x03",
            "#10400FIt's been about seven years\x01",
            "since it appeared on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PSeven years ago...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10404F#5PThis doesn't have anything to\x01",
            "do with the D∴G Cult. But...\x02\x03",
            "#10402FWanna hear about it just to kill time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PWell... If you don't\x01",
            "mind, then yes.\x02\x03",
            "#00000FWhen I think about it, I know almost\x01",
            "nothing about your past, Wazy.\x02\x03",
            "#00012FI understand your personality and\x01",
            "behaviors pretty well, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#5PHu hu... Very well.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    SetCameraDistance(15000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C──I was born in a certain\x01",
            "remote region of Zemuria.\x02\x03",
            "Contact with the outside world was\x01",
            "prohibited...a so-called "hidden village."\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, 155, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3CIn that village, a "God", who opposed the Goddess\x01",
            "had been worshipped since ancient times.\x02\x03",
            "When I was very young, I bore the role of a\x01",
            ""medium", one who can hear the voice of "God".\x02\x03",
            "It wasn't voluntary, of course, I was\x01",
            "forced ever since I can remember.\x02\x03",
            "Honestly, ever since I learned that "God"'s\x01",
            "true from was a mysterious and ancient magical\x01",
            "tool, I couldn't help but think it ridiculous.\x02\x03",
            "I always wanted to be free\x01",
            "from that worthless role.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C...Before long, strange things\x01",
            "started to occur in the village.\x02\x03",
            "The villagers, one after the\x01",
            "next, slipped into comas.\x02\x03",
            "From what I could see, the "God" went\x01",
            "berserk and through Septium veins, \x01",
            "sucked up their life force into itself...\x02\x03",
            "I requested to seal it, but the\x01",
            "village elders did not allow it, and\x01",
            "even spoke of offering a sacrifice.\x02\x03",
            "Well, actually, the tool had such terrific power\x01",
            "that sealing it would have been impossible...\x02\x03",
            "──That's when the Church\x01",
            "Knights came from the outside.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    SetMessageWindowPos(180, 160, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C──When I made contact with them, I learned\x01",
            "the "God" was a kind of ancient artifact...\x02\x03",
            "Knowing it was not an absolute\x01",
            "existence, I took drastic action.\x02\x03",
            "I dropped the "God", an azure stone tablet,\x01",
            "from the top of a cliff and tried to destroy it.\x02\x03",
            "I wanted with my whole heart to liberate the village \x01",
            "from the ancient curse, I wanted to be free──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    SetMessageWindowPos(10, 150, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3CBut the "God"'s resistance was fierce,\x01",
            "and it tried to steal all my power.\x02\x03",
            "The Knights' assistance was not in time, and\x01",
            "just when my life force was about to run out──\x02\x03",
            "That "seal" appeared on my chest.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    FadeToDark(2500, 16777215, -1)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_0D()
    OP_68(-360, 2100, -3950, 0)
    MoveCamera(150, -49, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5667730, 0)
    Sleep(1500)
    FadeToBright(1500, 16777215)
    OP_0D()
    Sleep(800)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C──My "Stigma", conversely,\x01",
            "stole all that "God"'s power...\x02\x03",
            "The "God" turned to an ordinary stone\x01",
            "tablet, and was smashed to pieces.\x02\x03",
            "Then I obtained my freedom── And was\x01",
            "happy to be banished from the village.\x02\x03",
            "As the sinner who "killed" the\x01",
            ""God" the villagers worshipped.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x1)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(16000, 3000)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(150)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    OP_6F(0x79)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00008F#6P#30W...So that's what happened...\x02\x03",
            "#00006F............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10409F#5P#30WHu hu...\x01",
            "Quite the absurd story, no?\x02\x03",
            "#10400FI guess a modern kid who grew up\x01",
            "in a city'd never believe it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PNo. Just by seeing your power,\x01",
            "I understand that it was real.\x02\x03",
            "#00000FAnd I also saw Zeit who you\x01",
            "could say is a living legend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10402F#5PHa ha, that's true too.\x02\x03",
            "#10404FAnd so, invited by the Knights, I\x01",
            "went to the Holy Nation of Arteria...\x02\x03",
            "And, as the possessor of one of only twelve\x01",
            ""Stigma", I was greeted as a "Dominion".\x02\x03",
            "#10400FI guess I've been \x01",
            "with Abbas ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PI see...\x02\x03",
            "#00006F...But, after that, have you ever\x01",
            "been back to your hometown?\x02\x03",
            "#00001FYou wouldn't have been able to see your family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10405F#5P#30WYeah── Isn't that obvious?\x02\x03",
            "#10403FI smashed the villagers'\x01",
            "foundations to pieces.\x02\x03",
            "I just wanted to be free with my whole heart... \x01",
            "I didn't think about what would have come after.\x02\x03",
            "#10400FThat's my punishment.\x02\x03",
            "#10404FI'm hated by my family too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10406F#5P#30WWell, according to what I've heard,\x01",
            "the Church went in the village and\x01",
            "took care of many things.\x02\x03",
            "#10404FThe "God"'s curse will\x01",
            "eventually fade into the past.\x02\x03",
            "I want to go back someday,\x01",
            "after things have cooled down.\x02\x03",
            "#10402FYou don't have to worry that much about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#30WWazy...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00008F#6PThen Wazy... You're leaving\x01",
            "Crossbell after this case wraps up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10400F#5PYeah. I have my mission\x01",
            "as a Knight, after all.\x02\x03",
            "#10409FHu hu, what? Are you starting\x01",
            "to feel lonely already?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        "#00001F#6PYeah, isn't that obvious?\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 400)
    Sleep(150)

    ChrTalk(
        0xE,
        "#10405F#11PHuh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    Sleep(500)
    OP_6F(0x79)
    SetCameraDistance(9000, 30000)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30WWald ended up like that, but I'm\x01",
            "sure he'll be back to normal.\x02\x03",
            "All of the Testaments\x01",
            "will remain in Crossbell.\x02\x03",
            "#00008FAnd this is just speculations, but all\x01",
            "of our friends will be here too...\x02\x03",
            "#00000FSo── Please come\x01",
            "to visit us anytime.\x02\x03",
            "#00009FBecause Crossbell is already your\x01",
            "second hometown. Isn't that right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(300)

    ChrTalk(
        0xE,
        "#10405F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()

    def lambda_C239():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_C239)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        "#10404F#2430V#5P#40W#12A...Hehe...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetChrSubChip(0xE, 0x3)

    def lambda_C291():
        OP_A6(0xFE, 0x0, 0x1E, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_C291)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xE,
        "#10409F#2431V#50W#5P#4S#15AAhhahahahaha!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30WI know that was lame.\x02\x03",
            "#00000FBut, I'm 100% serious, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10411F#5P#40W...Hu hu, got it. I go out of\x01",
            "tune when I talk with you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    OP_A0(0xE, 1000, 0x7, 0x5)
    OP_0D()
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#10402F#2929V#5P#40W──I'll be sure to visit whenever\x01",
            "I'm feeling homesick.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB71)
    Sleep(150)
    OP_A0(0xE, 1000, 0x5, 0x7)
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#10404F#2930V#5P#40WNot as a replacement for my hometown\x01",
            "I'm unable to return to, but as a place\x01",
            "where I have attachment to you guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB72)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x1770, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-360, 2100, -3950, 8000)
    MoveCamera(128, 27, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(40590, 8000)
    Sleep(500)
    OP_A0(0xE, 1000, 0x7, 0x5)
    Sleep(2500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_C53B")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_C53B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C551")
    Jump("loc_C5FA")

    label("loc_C551")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Wazy learned\x01",
            "Strike Heaven II.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Wazy's "Strike Heaven"\x01",
            "has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A1)
    AddCraft(0x4, 0x1A1)

    label("loc_C5FA")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x26, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 5)
    OP_29(0xB1, 0x1, 0x5)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_9F58 end

    def Function_17_C61D(): pass

    label("Function_17_C61D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x40)
    LoadChrToIndex("chr/ch03200.itc", 0x1E)
    LoadChrToIndex("apl/ch51809.itc", 0x1F)
    LoadChrToIndex("apl/ch51810.itc", 0x20)
    SoundLoad(3265)
    SoundLoad(3266)
    SoundLoad(3267)
    SoundLoad(3268)
    SoundLoad(3269)
    SoundLoad(3270)
    SoundLoad(2634)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10701.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis321.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis322.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis323.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis324.itp")
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -250, 120, 2750, 180)
    SetChrPos(0x8, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(125, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8000, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(115, 15, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    Sleep(800)

    ChrTalk(
        0x101,
        "#00002F#6P#30W#N...What a beautiful full moon.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()

    def lambda_C85F():

        label("loc_C85F")

        TurnDirection(0xFE, 0x101, 400)
        Yield()
        Jump("loc_C85F")

    QueueWorkItem2(0x8, 2, lambda_C85F)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        "#3265V#11P#40WMr. Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_24(0xCC1)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4200, 4500)
    MoveCamera(130, 20, 0, 4500)
    OP_6E(800, 4500)
    SetCameraDistance(10000, 4500)
    Sound(100, 0, 100, 0)

    def lambda_C951():
        OP_95(0xFE, -500, 0, -3750, 1600, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C951)
    WaitChrThread(0x101, 1)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    SetCameraDistance(9500, 30000)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WSomehow, I always feel the moon is\x01",
            "beautiful when I'm talking with you.\x02\x03",
            "#00002FNot for nothing you star\x01",
            "as the "Moon Princess".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#10709F#2634V#5P#30WUh uh...\x02",
    )

    CloseMessageWindow()
    OP_24(0xA4A)
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0xB4, 0x190)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10704F#3266V#40W#5PThe moon, a shadow in its light...\x02\x03",
            "#3267VI think it might be because my very\x01",
            "existence is like the moon itself.\x02\x03",
            "#10708F#3268VNormally, I wouldn't have ever showed\x01",
            "myself anywhere the sun can reach...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCC4)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30WBut, here in Crossbell, you\x01",
            "were able to grasp the light...\x02\x03",
            "#00001FThat's true, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A1(0x8, 0x3E8, 0x5, 0x2, 0x25, 0x26, 0x25, 0x2)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30WYes, I don't intend to\x01",
            "deny that anymore.\x02\x03",
            "#10708FBut I... The flow that\x01",
            "created my existence\x01",
            "is something very deep.\x02\x03",
            "#10711FThe flow of secrets that is "Yin"...\x02\x03",
            "#10703FThe underground path I inherited from my father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12P#30WYou said that before too...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30W...If you don't mind,\x01",
            "can I ask you about it?\x02\x03",
            "#00008FAbout the you before you came to Crossbell.\x02\x03",
            "#00001FThe Rixia Mao I don't know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30W...Yes.\x02\x03",
            "#10710FSomehow, I felt like I would\x01",
            "have ended up telling you about\x01",
            "it sooner or later, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    OP_93(0x8, 0xB4, 0x12C)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)
    OP_63(0x8, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10708F#5P#30W──As far back as I can remember,\x01",
            "I was with my father.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(9000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C──I have no memories of my mother.\x02\x03",
            "I believe my father kept\x01",
            "her away so that I would\x01",
            "inherit the path of "Yin".\x02\x03",
            "But to me, that was normal...\x02\x03",
            "Harsh discipline, dark tools and talisman training.\x01",
            "I mastered them dispassionately.\x02\x03",
            "While going from place to place, I attended Sunday School,\x01",
            "and thereby obtained the skills to connect with people.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CFather was neither strict nor kind,\x01",
            "He was only there to teach.\x02\x03",
            "That is because the things "Yin" \x01",
            "must inherit are too vast.\x02\x03",
            "The memories of generations of past "Yin"...\x02\x03",
            "To kill─ No matter the situation, no matter\x01",
            "the means and no matter the target...\x02\x03",
            "To keep the "Yin" the same over\x01",
            "generations, it was necessary\x01",
            "to inherit roughly all of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CAnd when I inherited all...\x01",
            "I became "Yin" itself.\x02\x03",
            "Though I say that, one does not become\x01",
            ""Yin" while their father is alive.\x02\x03",
            ""Yin" is but a single person...\x01",
            "That will never change.\x02\x03",
            "For some time, I spent quiet days,\x01",
            "while waiting for father to return home.\x02\x03",
            "Then, when he returned, he explained the gist \x01",
            "of the jobs so they wouldn't be a problem\x01",
            "when I would have succeeded him as "Yin"...\x02\x03",
            "It was already a stage face,\x01",
            "but to me, that was my entire world.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(20, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C──What shattered that world was when\x01",
            "my father fell to an incurable illness.\x02\x03",
            "My father was particularly strong even\x01",
            "among the many "Yin"... But disease\x01",
            "was a foe from which he could not run.\x02\x03",
            "He did not fight it, and refused\x01",
            "life-extension surgery...\x02\x03",
            "One day, he called and ordered me...\x02\x03",
            "To kill him and to succeed "Yin".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C──I could not do it.\x02\x03",
            "I had never gone against my\x01",
            "father's word before, but\x01",
            "for some reason I couldn't.\x02\x03",
            "...I became scared for the first time.\x02\x03",
            "I wondered if my father thought the me/Yin\x01",
            "he had diligently constructed was a failure.\x02\x03",
            "I wondered if had disappointed my father on his deathbed.\x02\x03",
            "...I was in agony. My father\x01",
            "cracked a wry smile and said:\x02\x03",
            ""──That is also you."\x02\x03",
            ""You should decide how your Yin will be."\x02\x03",
            "...And one month later, my father left this world.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CThen I became "Yin".\x02\x03",
            "I inherited my father's connections, used black\x01",
            "clothes and neigong to manipulate my figure...\x02\x03",
            "Though my skills were not as great as my\x01",
            "father's, I resumed work immediately.\x02\x03",
            ""You should decide how your Yin will be"...\x02\x03",
            "Without understanding their meaning,\x01",
            "I dispassionately went with the flow...\x02\x03",
            "──Then, two years passed and I accepted\x01",
            "a long-term contract with Heiyue.\x02\x03",
            "To help unseat the hegemony\x01",
            "in Crossbell, a trade city on\x01",
            "the western edge of Calvard.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(1000)
    SetMessageWindowPos(250, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CI arrived in Crossbell and prepared for battle. \x01",
            "As I was getting the lay of the land in the city, I\x01",
            "entered a certain theater in Entertainment District.\x02\x03",
            "Just then, a public training\x01",
            "session was being held...\x02\x03",
            "...From then on is as you\x01",
            "already know, Mr. Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 40000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30W...I see...\x02\x03",
            "#00000FSo that's when you\x01",
            "caught Miss Ilya's eye?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10702F#5P#30WUh uh. At first, I tried to refuse to\x01",
            "join the troupe making up a reason.\x02\x03",
            "#10704FBut Miss Ilya was extremely overbearing...\x02\x03",
            "Finally, I ran out of patience\x01",
            "and ended up joining.\x02\x03",
            "I was confident in my physical strength and\x01",
            "disguise, so I thought it would be good cover.\x02\x03",
            "#10710F...But the training was harder than expected,\x01",
            "and it was tough to be both Rixia and "Yin".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11P#30WHa ha...\x02\x03",
            "#00004F──Thank you, Rixia.\x02\x03",
            "#00000FI'm happy you told me all of this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30WUh uh. I don't think it was\x01",
            "that interesting a story...\x02\x03",
            "#10703FBut── This is the "path" I inherited\x01",
            "from my father and ancestors.\x02\x03",
            "#10708FEven if I have obtained the\x01",
            "light called Arc-en-ciel...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A0(0x8, 1000, 0x2, 0x5)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30WThat "path" is something I don't\x01",
            "think I can ever completely abandon.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30WI see...\x02\x03",
            "#00008F............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(1000)
    SetChrSubChip(0x8, 0x6)
    SetChrPos(0x101, -1000, 0, -4250, 90)
    SetChrPos(0x8, 0, 0, -4250, 270)
    OP_68(-300, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(-300, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7575", 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00003F#6P#30W"You should decide how your Yin will be"...\x02",
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x3E8, 0x5, 0x6, 0x29, 0x2A, 0x29, 0x6)

    ChrTalk(
        0x8,
        "#10712F#11P#30W...Eh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W..."Yin" inherits everything.\x02\x03",
            "Now that you've discovered\x01",
            "the light of Arc-en-ciel...\x02\x03",
            "#00002FIs it not also time for "Yin"\x01",
            "to take up the side of light?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10717F#11P#30WW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30WTimes change everything,\x01",
            "even the way to do things...\x02\x03",
            "#00003FNo, they have to change.\x02\x03",
            "#00008FAnd people inherit history,\x01",
            "and move forward...\x02\x03",
            "#00001FI wonder if there's also that meaning\x01",
            "in what your father said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10708F#11P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WAs a police officer, I can't\x01",
            "recommend criminal acts, but...\x02\x03",
            "Even so, I think you should\x01",
            "aim to be your own "Yin".\x02\x03",
            "#00000FIn a way, it would be a path to completely\x01",
            "cut ties will the "Yins" up until now.\x02\x03",
            "#00002FIf you did that... I think your\x01",
            "father wouldn't care, probably?\x02\x03",
            "#00009F"──That is also you", he would say, and smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10717F#11P#40W#2S......Oh......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W...What a good father.\x02\x03",
            "#00008FYours was a bit different from normal families,\x01",
            "but he loved his daughter...\x02\x03",
            "#00002FThat's what I think anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10718F#11P#50W...Fa...ther...\x02",
    )

    CloseMessageWindow()
    OP_68(-100, 1000, -4250, 1200)
    SetChrFlags(0x8, 0x20)

    def lambda_E4B8():
        OP_A0(0xFE, 1000, 0x6, 0x9)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_E4B8)
    OP_96(0x8, 0x96, 0x0, 0xFFFFEF66, 0x1F4, 0x0)
    Sound(812, 0, 60, 0)
    ClearChrFlags(0x8, 0x20)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A1(0x8, 0x3E8, 0x6, 0x1A, 0x1E, 0x1F, 0x20, 0x21, 0x22)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_63(0x8, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(812, 0, 60, 0)
    OP_A0(0x8, 1000, 0xA, 0xC)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10719F#11P#50WWhy...\x02\x03",
            "Even when my\x01",
            "father died...\x02\x03",
            "#10720FI didn't shed... a single\x01",
            "tear... like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WYou might have changed after spending\x01",
            "day after day with Miss Ilya and the others...\x02\x03",
            "#00008FI don't know what path you'll\x01",
            "follow going forward, but...\x02\x03",
            "#00000FIf possible, I'd like to watch\x01",
            "over you in place of your father.\x02\x03",
            "#00002FTo see how you'll change now\x01",
            "that you've found your light.\x02",
        )
    )

    CloseMessageWindow()
    OP_A0(0x8, 1000, 0xC, 0xF)
    Sleep(300)

    ChrTalk(
        0x8,
        "#10718F#11P#50W...Mr. Lloyd...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(1000)
    OP_68(100, 1000, -4250, 1200)
    SetCameraDistance(15000, 1200)
    OP_9A(0x101, 0x8, 0x1F4, 0x258, 0x0)
    Sleep(300)
    Fade(250)
    Sound(898, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_E75E():
        OP_A0(0xFE, 1000, 0x14, 0x16)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_E75E)

    def lambda_E76B():
        OP_A0(0xFE, 1000, 0x5, 0x7)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E76B)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x101, 3)
    OP_0D()
    MoveCamera(44, 23, 0, 15000)
    SetCameraDistance(70000, 15000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#10720F#11P#3269V#70W#20A...Ooh... Ahhh...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#10713F#11P#3270V#90W#30A#4S...Waaaaaah...!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1770)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_E851")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_E851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E863")
    Jump("loc_E91F")

    label("loc_E863")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Rixia learned\x01",
            "True Double Dragon Strike.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Rixia's "Double Dragon Strike" \x01",
            "has been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)

    label("loc_E91F")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x27, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 6)
    OP_29(0xB1, 0x1, 0x6)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_C61D end

    def Function_18_E942(): pass

    label("Function_18_E942")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E95C")
    OP_A0(0xFE, 1000, 0x10, 0x12)
    Sleep(300)
    Jump("Function_18_E942")

    label("loc_E95C")

    Return()

    # Function_18_E942 end

    SaveToFile()

Try(main)
