from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0100_1.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 7, 0, 8],
    )

    BuildStringList((
        "c0100_1",                # 0
    ))

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_107C",         # 01, 1
        "Function_2_26FD",         # 02, 2
        "Function_3_37BB",         # 03, 3
        "Function_4_3F3D",         # 04, 4
        "Function_5_4C6C",         # 05, 5
        "Function_6_4EAE",         # 06, 6
        "Function_7_51EE",         # 07, 7
        "Function_8_5A4F",         # 08, 8
        "Function_9_5B84",         # 09, 9
        "Function_10_648A",        # 0A, 10
        "Function_11_707E",        # 0B, 11
        "Function_12_733F",        # 0C, 12
        "Function_13_838A",        # 0D, 13
        "Function_14_851E",        # 0E, 14
        "Function_15_86A8",        # 0F, 15
        "Function_16_8826",        # 10, 16
        "Function_17_88D6",        # 11, 17
        "Function_18_8943",        # 12, 18
        "Function_19_89CA",        # 13, 19
        "Function_20_8AF0",        # 14, 20
        "Function_21_A3CC",        # 15, 21
        "Function_22_A9EE",        # 16, 22
        "Function_23_ABAF",        # 17, 23
        "Function_24_B179",        # 18, 24
        "Function_25_B368",        # 19, 25
        "Function_26_B8F7",        # 1A, 26
    ))


    def Function_0_100(): pass

    label("Function_0_100")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1CB")

    ChrTalk(
        0xFE,
        (
            "And just when I thought that I could finally come out...\x01",
            "What the heck is that tree floating in the air?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It won't fall down somewhere, eh?\x01",
            "......What an eternal anxiety it is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_1CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D9")
    Jump("loc_1078")

    label("loc_1D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D")

    ChrTalk(
        0xFE,
        (
            "The incident that happened in the past resulted\x01",
            "from the "secret feud" of the two major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You mean that it's the result of spies from\x01",
            "both countries competing with each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Frankly, I didn't think seriously about it,\x01",
            "but if that's the case, then they're unforgivable.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3EB")

    label("loc_31D")


    ChrTalk(
        0xFE,
        (
            "The incident that happened in the past resulted\x01",
            "from the "secret feud" of the two major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Frankly, I didn't think seriously about it,\x01",
            "but if that's the case, then they're unforgivable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB")

    Jump("loc_1078")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_586")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DA")

    ChrTalk(
        0xFE,
        (
            "There's a rumor saying that the Empire\x01",
            "government hired that armed group...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In a certain sense, you can't know\x01",
            "when they'll come to strike again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Thinking about it, the anxiety is terrific...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_581")

    label("loc_4DA")


    ChrTalk(
        0xFE,
        (
            "There's a rumor saying that the Empire\x01",
            "government hired that armed group...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thinking that they could come to attack\x01",
            "once again, I feel incredibly anxious...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_581")

    Jump("loc_1078")

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_631")

    ChrTalk(
        0xFE,
        (
            "The people of Mainz... I'm sure that\x01",
            "they're going through hardships now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Armed people suddenly\x01",
            "marching into...\x01",
            "I'm scared just picturing it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6B2")

    ChrTalk(
        0xFE,
        "Today mama asked me to do an errand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...She said to go urgently buy buckets\x01",
            "because the roof is leaking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_6B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_71B")

    ChrTalk(
        0xFE,
        (
            "So many ambulances were mobilized...\x01",
            "It seems that quite a serious accident happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_71B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7B7")

    ChrTalk(
        0xFE,
        "...Do I really want to live alone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I really yearn to do it, but\x01",
            "anyway living in a house alone...\x01",
            "I feel I would be quite lonely...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_7B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_906")

    ChrTalk(
        0xFE,
        (
            "Side job, side job... If I want to be in a\x01",
            "safe place, maybe a waitress would do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, if I want to earn a lot, there's \x01",
            "also the option of being a hostess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No no no, dear me, what\x01",
            "on earth am I thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how good the pay is, to pour\x01",
            "liquors to an old man is a big no.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_95E")

    label("loc_906")


    ChrTalk(
        0xFE,
        (
            "If I want to live alone, I have to work...\x01",
            "What kind of job could I be suited for?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95E")

    Jump("loc_1078")

    label("loc_963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_B94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE3")

    ChrTalk(
        0xFE,
        (
            "For living alone, I personally think that\x01",
            "the West Street area is the best place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But thinking realistically about rent and stuff,\x01",
            "in the end, the East Street area is better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Downtown would be even better,\x01",
            "but public safety comes first of all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, if I want to be independent,\x01",
            "first of all I have to find a side job.\x01",
            "...*sigh*.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B8F")

    label("loc_AE3")


    ChrTalk(
        0xFE,
        (
            "For living alone, I personally think that\x01",
            "the West Street area is the best place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Wait, if I want to be independent,\x01",
            "first of all I have to find a side job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8F")

    Jump("loc_1078")

    label("loc_B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_BF1")

    ChrTalk(
        0xFE,
        "My, it's already this late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to go home quickly\x01",
            "and help mama.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CC8")

    ChrTalk(
        0xFE,
        (
            "I was looking at the Crossbell executives\x01",
            "doing their enter and it was over in a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They were all riding in cars\x01",
            "and it wasn't really clear, but...\x01",
            "I got the feeling they were all VIPs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB5")

    ChrTalk(
        0xFE,
        (
            "Because starting tomorrow the Trade Conference\x01",
            "is going to take place, they looked a little showy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just before I was stopped by an\x01",
            "officer on patrol and I got the first\x01",
            "police questioning of my life.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E39")

    label("loc_DB5")


    ChrTalk(
        0xFE,
        (
            "It was my first police questioning,\x01",
            "but I guess it was rude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who would want to be\x01",
            "called "maid" out loud...\x01",
            "How shameful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E39")

    Jump("loc_1078")

    label("loc_E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_EC0")

    ChrTalk(
        0xFE,
        (
            "I hate staying still at home\x01",
            "just because it rains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hold my favorite umbrella\x01",
            "and it's walk time, see♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1078")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F51")

    ChrTalk(
        0xFE,
        (
            "So many patrol cars appeared\x01",
            "and I got surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I guess they were\x01",
            "cool, being police and all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1078")

    label("loc_F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1025")

    ChrTalk(
        0xFE,
        (
            "Honestly, that papa of mine! Why does\x01",
            "he loiter around naked at home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lack of concern towards an adolescent\x01",
            "girl, I'd say... I think it's a crime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, I want to live alooone.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1078")

    label("loc_1025")


    ChrTalk(
        0xFE,
        "*sigh*, I want to live alooone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uuuh, isn't there a\x01",
            "nice house anywhere?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1078")

    TalkEnd(0xFE)
    Return()

    # Function_0_100 end

    def Function_1_107C(): pass

    label("Function_1_107C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AC")

    ChrTalk(
        0xFE,
        (
            "I don't know the details but it\x01",
            "seems that we lost those\x01",
            "weapon, the "Aions".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Putting aside how he did it...\x01",
            "I'm positive that President Dieter had\x01",
            "prepared them to protect Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although as a result he brought big\x01",
            "disorders, I can't condemn him at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_126B")

    label("loc_11AC")


    ChrTalk(
        0xFE,
        (
            "Putting aside how he did it...\x01",
            "I'm positive that President Dieter had\x01",
            "prepared them to protect Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although as a result he brought big\x01",
            "disorders, I can't condemn him at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126B")

    Jump("loc_26F9")

    label("loc_1270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_127E")
    Jump("loc_26F9")

    label("loc_127E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1432")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1379")

    ChrTalk(
        0xFE,
        "Hm...an asset freeze declaration, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I would never thought that Mayor Dieter\x01",
            "could've resorted to such a drastic measure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, like he says, we may not have\x01",
            "another chance to stand up aside from this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_142D")

    label("loc_1379")


    ChrTalk(
        0xFE,
        (
            "I would never thought that Mayor Dieter\x01",
            "could've resorted to such a drastic measure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, like he says, we may not have\x01",
            "another chance to stand up aside from this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142D")

    Jump("loc_26F9")

    label("loc_1432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_163E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1581")

    ChrTalk(
        0xFE,
        (
            "The raid from the other day...\x01",
            "That's definitely the Empire work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lately they were feigning friendliness, but obviously their\x01",
            "true nature is that they'll do anything for their goals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They used foul play indirectly and schemed\x01",
            "an invasion if chances permitted it...\x01",
            "That's what Erebonia is!!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1639")

    label("loc_1581")


    ChrTalk(
        0xFE,
        (
            "The raid from the other day...\x01",
            "That's definitely the Empire work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They used foul play indirectly and schemed\x01",
            "an invasion if chances permitted it...\x01",
            "That's what Erebonia is!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1639")

    Jump("loc_26F9")

    label("loc_163E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_16F3")

    ChrTalk(
        0xFE,
        "There could be the Empire behind this incident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hm, in that case, we won't be\x01",
            "probably able to protect Crossbell\x01",
            "just by obeying like we did until now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26F9")

    label("loc_16F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1701")
    Jump("loc_26F9")

    label("loc_1701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_17F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AA")

    ChrTalk(
        0xFE,
        (
            "In the west direction it appears\x01",
            "that some kind of incident happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Absit omen...\x01",
            "O Aidios, Goddess above, please protect us all!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17ED")

    label("loc_17AA")


    ChrTalk(
        0xFE,
        (
            "Absit omen...\x01",
            "O Aidios, Goddess above, please protect us all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17ED")

    Jump("loc_26F9")

    label("loc_17F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F5")

    ChrTalk(
        0xFE,
        (
            "I can't say it as a rule of fact, but it seems\x01",
            "that many in the young generation approve\x01",
            "the independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A generation that doesn't know strifes...maybe.\x01",
            "I'm worried if they understand the\x01",
            "seriousness of all this or not.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_196D")

    label("loc_18F5")


    ChrTalk(
        0xFE,
        (
            "A generation that doesn't know strifes...maybe.\x01",
            "I'm worried if they understand the\x01",
            "seriousness of all this or not.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196D")

    Jump("loc_26F9")

    label("loc_1972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5E")

    ChrTalk(
        0xFE,
        (
            "Hm, honestly, I'd never thought\x01",
            "that I'd be hearing the word\x01",
            ""independence" at my age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Independence, independence...\x01",
            "It sure is like a dream come true, but \x01",
            "I don't think it'll go well in the end...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AA7")

    label("loc_1A5E")


    ChrTalk(
        0xFE,
        (
            "Independence, independence...\x01",
            "Could it really be a dream come true?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA7")

    Jump("loc_26F9")

    label("loc_1AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C67")

    ChrTalk(
        0xFE,
        (
            "We can't attend the Trade Conference, and it\x01",
            "won't be relayed via orbal communications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, the only way we\x01",
            "have to hear its result is through\x01",
            "the city's PRs and the press.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Needless to say, from the very\x01",
            "popular Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Articles' integrity, equilibrium, speed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whichever you get, there isn't another\x01",
            "one source of information that can\x01",
            "outrival Crossbell Times at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D2A")

    label("loc_1C67")


    ChrTalk(
        0xFE,
        (
            "We can't attend the Trade Conference, and it\x01",
            "won't be relayed via orbal communications.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In other words, the only way we\x01",
            "have to hear its result is through\x01",
            "the city's PRs and the press.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2A")

    Jump("loc_26F9")

    label("loc_1D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1EA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1A")

    ChrTalk(
        0xFE,
        (
            "Oh, now that I notice it, hasn't\x01",
            "it grown completely dark?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ho ho, could I've been too absorbed\x01",
            "by the Trade Conference atmosphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to go home quickly so to \x01",
            "not make my old woman worry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E9D")

    label("loc_1E1A")


    ChrTalk(
        0xFE,
        (
            "Oh, now that I notice it, hasn't\x01",
            "it grown completely dark?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to go home quickly so to \x01",
            "not make my old woman worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E9D")

    Jump("loc_26F9")

    label("loc_1EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_223D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F55")

    ChrTalk(
        0xFE,
        (
            "Some time ago, a young woman with an\x01",
            "eastern air entered in that restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She was a beautiful young woman\x01",
            "with an intellectual face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2238")

    label("loc_1F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2167")

    ChrTalk(
        0xFE,
        (
            "Hm, can the new city\x01",
            "hall finally be seen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Five years have surely passed from its construction\x01",
            "plan announcement. According to rumors, I had heard\x01",
            "it would've taken a minimum of another year, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just after Mayor Crois was elected, he\x01",
            "decided to invest IBC capitals in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to this, construction proceeded smoothly without\x01",
            "being influenced by stupid competitions over interests \x01",
            "and rights, and it was finally completed the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoh ho, Mayor Crois\x01",
            "really did us a favor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2238")

    label("loc_2167")


    ChrTalk(
        0xFE,
        (
            "Five years have surely passed from its construction\x01",
            "plan announcement. According to rumors, I had heard\x01",
            "it would've taken a minimum of another year, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoh ho, Mayor Crois\x01",
            "really did us a favor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2238")

    Jump("loc_26F9")

    label("loc_223D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_23E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2343")

    ChrTalk(
        0xFE,
        (
            "Hm, the Trade Conference is\x01",
            "finally going to start tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor Crois, its advocate,\x01",
            "is at the same time mayor\x01",
            "and president of that IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He'll have to display his leadership at\x01",
            "his heart's content in the conference.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23E1")

    label("loc_2343")


    ChrTalk(
        0xFE,
        (
            "Hm, the Trade Conference is\x01",
            "finally going to start tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mayor Crois will have to\x01",
            "show his leadership at his\x01",
            "heart's content in the conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E1")

    Jump("loc_26F9")

    label("loc_23E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_23F4")
    Jump("loc_26F9")

    label("loc_23F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_26F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2490")

    ChrTalk(
        0xFE,
        (
            "Even from here I could see that\x01",
            "dramatic arrest from some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police are doing quite\x01",
            "their best too, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26F9")

    label("loc_2490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2620")

    ChrTalk(
        0xFE,
        (
            "With the corrupt congressmen of the Imperial and\x01",
            "Republican Factions involved in the Cult incident \x01",
            "gone, even that Revache & Co. disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And yet, the status quo of the Empire\x01",
            "faction congressmen occupying many\x01",
            "parliamentary seats hasn't changed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hear about his strenuous efforts\x01",
            "in speeding up the legal reforms, but...\x01",
            "Mayor Crois has to do much, much more.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26F9")

    label("loc_2620")


    ChrTalk(
        0xFE,
        "...I believe they were the Heiyue?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With Revache gone, it is said\x01",
            "that they've started to throw\x01",
            "their weight around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Making laws so the citizens\x01",
            "can live safely... Mayor Crois\x01",
            "has to do much, much more.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F9")

    TalkEnd(0xFE)
    Return()

    # Function_1_107C end

    def Function_2_26FD(): pass

    label("Function_2_26FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_27A1")

    ChrTalk(
        0xFE,
        (
            "Well then, I'll now go\x01",
            "back to Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "City Hall is probably in chaos\x01",
            "too, but at any rate, nothing\x01",
            "will start if I don't turn up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B7")

    label("loc_27A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_27AF")
    Jump("loc_37B7")

    label("loc_27AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_27BD")
    Jump("loc_37B7")

    label("loc_27BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2940")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A4")

    ChrTalk(
        0xFE,
        "Ha ha, Mimi is so innocent and cute, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, all things considered,\x01",
            "why did the armed group take\x01",
            "away Crossbell bell with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't picture it as something\x01",
            "of such value to steal...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_293B")

    label("loc_28A4")


    ChrTalk(
        0xFE,
        (
            "All things considered,\x01",
            "why did the armed group take\x01",
            "away Crossbell bell with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't picture it as something\x01",
            "of such value to steal...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_293B")

    Jump("loc_37B7")

    label("loc_2940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_29A3")

    ChrTalk(
        0xFE,
        (
            "I'm worried about Mainz's people...\x01",
            "There're probably kids of Mimi's age too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B7")

    label("loc_29A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29FD")

    ChrTalk(
        0xFE,
        "Hey, Mimi, look.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A Mr. Snail is going to\x01",
            "and fro on the handrail.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B7")

    label("loc_29FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2ACB")

    ChrTalk(
        0xFE,
        (
            "It's something obvious, however...\x01",
            "The ambulances were quite in a hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although emergency vehicles like\x01",
            "those have no speed restrictions,\x01",
            "watching them makes you a little nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B7")

    label("loc_2ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0D")

    ChrTalk(
        0xFE,
        "Hmmm, orbal vehicles are really nice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, it can't be helped that common\x01",
            "people can't put their hands on them,\x01",
            "being their market price still too high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although still improbable, if half of them\x01",
            "were to drop in price even just by a 20%,\x01",
            "they would become easier to afford.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2CC3")

    label("loc_2C0D")


    ChrTalk(
        0xFE,
        "Hmmm, orbal vehicles are really nice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's really impossible for me immediately,\x01",
            "but I'd really like to get one no matter what\x01",
            "at least when going towards my retirement.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC3")

    Jump("loc_37B7")

    label("loc_2CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E73")

    ChrTalk(
        0xFE,
        (
            "Lately, it seems that society\x01",
            "is paying attention just to talks\x01",
            "about the independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish that the government didn't forget the \x01",
            "traffic basic law announced just the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the legal reform, in addition to\x01",
            "the current penalty system, a\x01",
            ""suspension of license" was added.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that this way, the incidents caused by\x01",
            "orbal vehicles will go down even if just a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F63")

    label("loc_2E73")


    ChrTalk(
        0xFE,
        (
            "From now on, if you commit certain infractions,\x01",
            "your driving license gets suspended for a period...\x01",
            "In other words, you can't drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I pray that this way, the incidents caused by\x01",
            "orbal vehicles will go down even if just a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F63")

    Jump("loc_37B7")

    label("loc_2F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F76")
    Jump("loc_37B7")

    label("loc_2F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2FCF")

    ChrTalk(
        0xFE,
        (
            "Well then, sorry to have\x01",
            "made you waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "So, let's go at once.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37B7")

    label("loc_2FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2FDD")
    Jump("loc_37B7")

    label("loc_2FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_308F")

    ChrTalk(
        0xFE,
        (
            "As a consequence of City Hall complete\x01",
            "transfer, it was decided that I will be\x01",
            "working at Orchis Tower for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Very well then, I guess I'll be busy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37B7")

    label("loc_308F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_34F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344D")

    ChrTalk(
        0xFE,
        (
            "I happened to see you yesterday...\x01",
            "It seems you ride in quite\x01",
            "a rare orbal car, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, actually it's the\x01",
            "new model by ZCF.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    ChrTalk(
        0xFE,
        "What, an orbal car by that ZCF!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "B-By any chance, do you know its max speed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FWell, we haven't tested it yet, but it\x01",
            "seems that it's set at 1500 selge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "G-Goodness...!!\x01",
            "To think that even the ZCF could reach\x01",
            "such speed with that type of cars!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uuuh, that's amazing.\x01",
            "With this I guess that finally even the orbal car\x01",
            "manufacturers are embarking in a top three era.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm, if that's the case then from now on things\x01",
            "are going to get more and more interesting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FRight?\x02\x03",
            "This way the competition is going to\x01",
            "heat up more, and more terrific cuties\x01",
            "are going to steadily begin to...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x101,
        "#00012FS-She sure is quite fired up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F*giggle*, Miss Noｱl really likes them too, eh?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 0)
    Jump("loc_34EB")

    label("loc_344D")


    ChrTalk(
        0xFE,
        (
            "Who could've thought that that\x01",
            "ZCF was developing orbal cars!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm hm, well, from now on I won't be able to\x01",
            "avert my eyes from each company's trends!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EB")

    Jump("loc_37B7")

    label("loc_34F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_37B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3574")

    ChrTalk(
        0xFE,
        (
            "The traffic laws really need\x01",
            "to be adjusted urgently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd be afraid to let\x01",
            "Mimi play alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B7")

    label("loc_3574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3697")

    ChrTalk(
        0xFE,
        (
            "Just before I saw an orbal\x01",
            "car running through this Central\x01",
            "Square at an incredible speed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it was clearly a dangerous speed,\x01",
            "I immediately reported it to the police, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did they properly catch them, I wonder?\x01",
            "...I'm worried they'd show up again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37B7")

    label("loc_3697")


    ChrTalk(
        0xFE,
        (
            "Although, with the current traffic basic laws,\x01",
            "even if they were to catch them for dangerous\x01",
            "driving, everything would end with just a ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm having high hopes for the future,\x01",
            "since as of late, even in the Congress they're\x01",
            "advancing the strengthening of penal regulations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B7")

    TalkEnd(0xFE)
    Return()

    # Function_2_26FD end

    def Function_3_37BB(): pass

    label("Function_3_37BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38B2")

    ChrTalk(
        0xFE,
        (
            "Since my husband says he's going back \x01",
            "to City Hall, I think we will go back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the future there're going to be many worries, \x01",
            "but... I feel that if we stay together as a family,\x01",
            "there's nothing we can't overcome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F39")

    label("loc_38B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_38C0")
    Jump("loc_3F39")

    label("loc_38C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3979")

    ChrTalk(
        0xFE,
        (
            "We can't do anything about it, but...\x01",
            "In the last week, I almost couldn't\x01",
            "spot the sight of tourists...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder what will become\x01",
            "of Crossbell from now on...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F39")

    label("loc_3979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A55")

    ChrTalk(
        0xFE,
        (
            "Since for the present I'm resting from my job as a guide,\x01",
            "we three are spending time together as family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about many things in the future, but...\x01",
            "This child's smile is a relief for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F39")

    label("loc_3A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3A63")
    Jump("loc_3F39")

    label("loc_3A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A71")
    Jump("loc_3F39")

    label("loc_3A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A7F")
    Jump("loc_3F39")

    label("loc_3A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A8D")
    Jump("loc_3F39")

    label("loc_3A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A9B")
    Jump("loc_3F39")

    label("loc_3A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3CB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE9")

    ChrTalk(
        0xFE,
        "Ehm, *cough*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What you can see behind to your right,\x01",
            "everyone, is the "Orbal Store".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its name, "Genten", is also famous\x01",
            "throughout the continent as a store\x01",
            "where orbal goods gather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's this era's cutting edge store\x01",
            "naturally popular with the citizens,\x01",
            "but also among all the tourists.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CB0")

    label("loc_3BE9")


    ChrTalk(
        0xFE,
        (
            "Ehm, what you can see behind to your right, \x01",
            "everyone, is the Orbal Store "Genten".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's this era's cutting edge store\x01",
            "naturally popular with the citizens,\x01",
            "but also among all the tourists.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CB0")

    Jump("loc_3F39")

    label("loc_3CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3CFD")

    ChrTalk(
        0xFE,
        (
            "Yes, let's go quickly. Both\x01",
            "Mimi and I are starving.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F39")

    label("loc_3CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D18")
    Call(1, 6)
    Jump("loc_3F0F")

    label("loc_3D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E65")

    ChrTalk(
        0xFE,
        "Ehm, *cough*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What you can see to your right\x01",
            "everyone, is the "Crossbell Bell".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its origin is old, even more than 500 years ago,\x01",
            "said to go back to the Middle Ages era.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After it was excavated in Septian Calendar\x01",
            "1185, even now it's familiarly known among\x01",
            "the citizens as the city's very symbol.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F0F")

    label("loc_3E65")


    ChrTalk(
        0xFE,
        (
            "Ehm, what you can see to your right\x01",
            "everyone, is the "Crossbell Bell".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Its origin is old, even more than 500 years ago,\x01",
            "said to go back to the Middle Ages era.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F0F")

    Jump("loc_3F39")

    label("loc_3F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F22")
    Jump("loc_3F39")

    label("loc_3F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F30")
    Jump("loc_3F39")

    label("loc_3F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3F39")

    label("loc_3F39")

    TalkEnd(0xFE)
    Return()

    # Function_3_37BB end

    def Function_4_3F3D(): pass

    label("Function_4_3F3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_40AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_401E")

    ChrTalk(
        0xFE,
        (
            "Papa says that he's\x01",
            "going to work now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, Lloyd, you're\x01",
            "always working, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mimi you know, is always cheering \x01",
            "for you, so do your best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_40A9")

    label("loc_401E")


    ChrTalk(
        0xFE,
        (
            "Papa and Lloyd and the others too are great, \x01",
            "you're always doing your best at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mimi will do her best too to cheer for you.\x02",
    )

    CloseMessageWindow()

    label("loc_40A9")

    Jump("loc_4C68")

    label("loc_40AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_40BC")
    Jump("loc_4C68")

    label("loc_40BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_41B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_412B")

    ChrTalk(
        0xFE,
        (
            "That orbal vehicle with\x01",
            "the faceplate was cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Father seems to be happy.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_41B1")

    label("loc_412B")


    ChrTalk(
        0xFE,
        (
            "Father says that he got busy\x01",
            "with his job at City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the contrary, the tour operator\x01",
            "mother works for is on vacation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41B1")

    Jump("loc_4C68")

    label("loc_41B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_424A")

    ChrTalk(
        0xFE,
        (
            "Ehm, what you can see to your right,\x01",
            "everyone, is the Crossbell Beeell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Oh, wait...?\x01",
            "Where did the bell go?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_427D")

    label("loc_424A")


    ChrTalk(
        0xFE,
        (
            "I wonder where Crossbell\x01",
            "Bell has gone to...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_427D")

    Jump("loc_4C68")

    label("loc_4282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_43F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4381")

    ChrTalk(
        0xFE,
        (
            "Somehow, today there're many\x01",
            "people with serious faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, Lloyd and the others too...\x01",
            "That's no good, you have to cheer up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FAh, yes, you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FThank you, Mimi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, it's nothing, eh.\x01\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_43EB")

    label("loc_4381")


    ChrTalk(
        0xFE,
        (
            "Somehow, today there're many\x01",
            "people with serious faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mr. Sun smiles upon everyone, you know?\x02",
    )

    CloseMessageWindow()

    label("loc_43EB")

    Jump("loc_4C68")

    label("loc_43F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4430")

    ChrTalk(
        0xFE,
        "Waah, that's true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is he lost, perhaps?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C68")

    label("loc_4430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_44A1")

    ChrTalk(
        0xFE,
        (
            "When an ambulance passes\x01",
            "through, you know, you have\x01",
            "to make way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's a traffic rule.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C68")

    label("loc_44A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4564")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4527")

    ChrTalk(
        0xFE,
        "Broom, broom.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like that father is\x01",
            "thinking about cars again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He really likes them.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_455F")

    label("loc_4527")


    ChrTalk(
        0xFE,
        "Broom, broom.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The passenger's seat is Mimi's.\x02",
    )

    CloseMessageWindow()

    label("loc_455F")

    Jump("loc_4C68")

    label("loc_4564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F0")

    ChrTalk(
        0xFE,
        (
            "Ehm, what you can see to\x01",
            "your right, everyone, is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhhm, your right...is your right, right?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_464E")

    label("loc_45F0")


    ChrTalk(
        0xFE,
        (
            "Uhhm, what was\x01",
            "mother saying again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What you can see to your right is...your right?\x02",
    )

    CloseMessageWindow()

    label("loc_464E")

    Jump("loc_4C68")

    label("loc_4653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_46BE")

    ChrTalk(
        0xFE,
        "Hm hm, I see I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I must absolutely\x01",
            "go to buy some presents.\x01",
            "*flash flash*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C68")

    label("loc_46BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4747")

    ChrTalk(
        0xFE,
        "Eating out, eating out, today I'm eating out♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mimi you know, wants to eat the\x01",
            ""eastern cuisine" of East Street.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C68")

    label("loc_4747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4762")
    Call(1, 6)
    Jump("loc_47B4")

    label("loc_4762")


    ChrTalk(
        0xFE,
        "Hm hm, I see I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I absolutely have to\x01",
            "photograph this.\x01",
            "*flash flash*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B4")

    Jump("loc_4C68")

    label("loc_47B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AF4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E3")
    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "Ah, there's a kid I don't know\x01",
            "with you and the others, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ehehe, those clothes are cool.\x01",
            "They are eastern-like, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        (
            "Ooh, to notice the good quality of these\x01",
            "clothes...you promise quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Ehhem, these are a unique\x01",
            "order made set of clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Older maid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Eeh, so those were\x01",
            "a maid's clothes...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "No, it's not like that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Ha ha, their conversation is\x01",
            "somehow refreshing and funny.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DC, 6)
    Jump("loc_4A69")

    label("loc_49E3")

    TurnDirection(0xB, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "A maid, eh?\x01",
            "Wait, could you actually be a girl?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x1A2,
        "Like I told you, it's not like that...\x02",
    )

    CloseMessageWindow()

    label("loc_4A69")

    Jump("loc_4AEF")

    label("loc_4A6E")


    ChrTalk(
        0xFE,
        (
            "Father says that he won't be able\x01",
            "to play around with Mimi for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "However, since it's work, I'll have to endure.\x02",
    )

    CloseMessageWindow()

    label("loc_4AEF")

    Jump("loc_4C68")

    label("loc_4AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4B9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0F")
    Call(1, 5)
    Jump("loc_4B9A")

    label("loc_4B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B61")

    ChrTalk(
        0xFE,
        "Splish splash, splish splash♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Today is raining, yep.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B9A")

    label("loc_4B61")


    ChrTalk(
        0xFE,
        (
            "Mimi's father is extremely\x01",
            "fond of cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah!\x02",
    )

    CloseMessageWindow()

    label("loc_4B9A")

    Jump("loc_4C68")

    label("loc_4B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C02")

    ChrTalk(
        0xFE,
        (
            "Let's ride cars\x01",
            "respecting the rules!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mimi too knows them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C68")

    label("loc_4C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C14")
    Call(1, 5)
    Jump("loc_4C68")

    label("loc_4C14")


    ChrTalk(
        0xFE,
        (
            "Everyone of the New Special Support Section,\x01",
            "do your best with your job, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C68")

    TalkEnd(0xFE)
    Return()

    # Function_4_3F3D end

    def Function_5_4C6C(): pass

    label("Function_5_4C6C")


    ChrTalk(
        0xB,
        (
            "Ah, Lloyd and Elie!\x01",
            "And...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "What? Where're\x01",
            "Tio and Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Is the Special Support Section\x01",
            "still on holiday for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FNo, it's not that, but...\x01\x02\x03",
            "#00000FThose two have still\x01",
            "some other job to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, and also, these persons are new\x01",
            "members of the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        "Eeh, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "So, from now on, you're the New\x01",
            "Special Support Section, eh?♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHa ha, what an accurate\x01",
            "naming that is, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FHu hu, nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yes, nice to meet you!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12E, 1)
    Return()

    # Function_5_4C6C end

    def Function_6_4EAE(): pass

    label("Function_6_4EAE")

    OP_4B(0xB, 0xFF)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xF, 0x0, 0)

    ChrTalk(
        0xB,
        "Ah, it's Lloyd and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I introduce you to Mimi's mother.\x01",
            "She is a touring guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "*giggle*, pleased to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It appears that you're always\x01",
            "caring about my daughter.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, it's not such\x01",
            "a big deal at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FBe that as it may, how lovely it\x01",
            "is to be working as a tour guide.\x02\x03",
            "Are you working today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "No, I am on holiday during\x01",
            "the Trade Conference period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "And so, during this time I plan to\x01",
            "spend time together with my child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHmm, and yet, you're wearing your uniform?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Eh, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Mimi begged to wear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We're going to play Miss \x01",
            "Guide make-believe now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, I see.\x01",
            "Aren't you happy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Yup, I am!♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Lloyd and friends, stay\x01",
            "safe and see you!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xB, 0x0, 0x0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x14A, 2)
    Return()

    # Function_6_4EAE end

    def Function_7_51EE(): pass

    label("Function_7_51EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_523D")

    ChrTalk(
        0xFE,
        (
            "What's with that giant tree...?\x01",
            "Isn't it...unbelievable?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_523D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_524B")
    Jump("loc_5A4B")

    label("loc_524B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5278")

    ChrTalk(
        0xFE,
        "Mr. Arios was super cool!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_5278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_52FD")

    ChrTalk(
        0xFE,
        (
            "It seems that they're doing\x01",
            "a charity event in the\x01",
            "Governmental DIstrict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why don't we go take a quick look?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_52FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_53D9")

    ChrTalk(
        0xFE,
        (
            "A mysterious armed group, it's too scary!\x01",
            "Papa says that we have to be independent\x01",
            "even for not being made a fool by such guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A local referendum, eh? If we had\x01",
            "been 18 too, we could've voted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_53D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53E7")
    Jump("loc_5A4B")

    label("loc_53E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_545D")

    ChrTalk(
        0xFE,
        (
            "Those ambulances were really impetous.\x01",
            "...I hope they don't get into an accident being in a hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_545D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54F4")

    ChrTalk(
        0xFE,
        "Eeeh, you're stopping dieting!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "J-J-Just because you strangely have a pretty face...\x01",
            "I won't be able to be like you, you know!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_54F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_555B")

    ChrTalk(
        0xFE,
        "............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...All things considered, should I\x01",
            "do sports or restrict my diet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_555B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_560B")

    ChrTalk(
        0xFE,
        (
            "Hey, hey, they say that\x01",
            "Mr. Arios and Archduke\x01",
            "Albert are really good friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How nice! If I could, how I'd like to\x01",
            "become good friends with them too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_560B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_567F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_562B")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_567A")

    label("loc_562B")


    ChrTalk(
        0xFE,
        "Hmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "(...Judging by her reaction,\x01",
            "she isn't doing it at all.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_567A")

    Jump("loc_5A4B")

    label("loc_567F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_573C")

    ChrTalk(
        0xFE,
        (
            "Did you see Archduke Albert!?\x01",
            "Isn't his goatee dreaming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chancellor Osborne is cool too, but\x01",
            "I guess he'd be harder to approach?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Still, both have a nice beard.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_573C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_580A")

    ChrTalk(
        0xFE,
        (
            "It goes without saying that Mr. Arios\x01",
            "is dreamy, but Mayor Dieter too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, more that the lover you'd want,\x01",
            "he feels more like the ideal papa.\x01",
            "I wonder if I could get me adopted...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_580A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5818")
    Jump("loc_5A4B")

    label("loc_5818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5A4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5882")

    ChrTalk(
        0xFE,
        "...Yes? Do you need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm a little busy at the moment...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A4B")

    label("loc_5882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5964")

    ChrTalk(
        0xFE,
        (
            "Just moments ago I was hit\x01",
            "upon by a weird red hair man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was quite cool, but when I\x01",
            "told him he wasn't my type, he said\x01",
            ""You aren't mine too, don't sweat it☆"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "G-GRRRRRR!!!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_59CC")

    label("loc_5964")


    ChrTalk(
        0xFE,
        (
            "I mean, if you're the one hitting on me,\x01",
            "what does it mean "You aren't my type"!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "G-GRRRRRR!!\x02",
    )

    CloseMessageWindow()

    label("loc_59CC")

    Jump("loc_5A4B")

    label("loc_59D1")


    ChrTalk(
        0xFE,
        (
            "Homework?\x01",
            "I don't have time for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, by the way... It seems Mr. Arios\x01",
            "is on a business trip again, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A4B")

    TalkEnd(0xFE)
    Return()

    # Function_7_51EE end

    def Function_8_5A4F(): pass

    label("Function_8_5A4F")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "By the way, Lenalee, are you\x01",
            "keeping up with your jogging?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Eh, oh, yes...\x01",
            "Well, more or less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After thinking that dieting\x01",
            "forcibly is not good, I lately\x01",
            "do it when I feel inclined to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Eeeh, is that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(...Judging by her reaction,\x01",
            "she isn't doing it at all.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_8_5A4F end

    def Function_9_5B84(): pass

    label("Function_9_5B84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BFE")

    ChrTalk(
        0xFE,
        (
            "Yes, it emits a pretty\x01",
            "pale light, but...\x01",
            "It's super ghastly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Is something going to happen...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_5BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5C0C")
    Jump("loc_6486")

    label("loc_5C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5CB5")

    ChrTalk(
        0xFE,
        (
            "Yes, yes, even that white military\x01",
            "uniform suited him greatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I believe that whatever may happen, with\x01",
            "Mr. Arios around we're going to be fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_5CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5D55")

    ChrTalk(
        0xFE,
        (
            "You're right, taking part in something like that...\x01",
            "It appears it would have some meaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you like, let's go invite the others too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_5D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5DEA")

    ChrTalk(
        0xFE,
        "We're still 15, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still, I don't get the pros and cons of independence...\x01",
            "Frankly, I maybe feel relieved I can't vote.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_5DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5DF8")
    Jump("loc_6486")

    label("loc_5DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5E38")

    ChrTalk(
        0xFE,
        (
            "Geez, Pluna, don't say\x01",
            "such alarming things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_5E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5EA9")

    ChrTalk(
        0xFE,
        "...I've made up my mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll quit dieting and find a boy who\x01",
            "likes me for how I am now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_5EA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F45")

    ChrTalk(
        0xFE,
        (
            "*sigh*, isn't there a dieting method that's\x01",
            "neither doing sports nor a diet restriction?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll do anything, so, someone, tell meee!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_5F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5FFB")

    ChrTalk(
        0xFE,
        (
            "Now that I think about it, Mr. \x01",
            "Arios was awarded a decoration\x01",
            "from the Principality of Remiferia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Was that the occasion where those\x01",
            "two became good friends?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_5FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_60AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601B")
    Call(1, 8)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_60A6")

    label("loc_601B")


    ChrTalk(
        0xFE,
        (
            "E-Even if you say "feel inclined",\x01",
            "you have to properly keep at it, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's see, then, today I'll\x01",
            "run and then I'll go home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60A6")

    Jump("loc_6486")

    label("loc_60AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6285")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61BE")

    ChrTalk(
        0xFE,
        (
            "Beard beard beard...\x01",
            "You like it too, eh, Pluna?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More importantly, I guess that my\x01",
            "type is the tall soldier who was \x01",
            "standing near Prince Olivert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even just once, how I'd like to be carried in\x01",
            "the arms of a man with such a physique.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6280")

    label("loc_61BE")


    ChrTalk(
        0xFE,
        (
            "More importantly, I guess that my\x01",
            "type is the tall soldier who was \x01",
            "standing near Prince Olivert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even just once, how I'd like to be carried in\x01",
            "the arms of a man with such a physique.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6280")

    Jump("loc_6486")

    label("loc_6285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_62FC")

    ChrTalk(
        0xFE,
        (
            "Indeed, Mayor Crois could\x01",
            "be the ideal papa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, he doesn't look\x01",
            "old like my papa is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_62FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_630A")
    Jump("loc_6486")

    label("loc_630A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6486")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_636F")

    ChrTalk(
        0xFE,
        "Dangerous driving? Dunnooo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We were too focused\x01",
            "on chatting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_636F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63FA")

    ChrTalk(
        0xFE,
        (
            "...That red hair mister was\x01",
            "somehow weird, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He went inside the department\x01",
            "store...who was he, I wonder?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6486")

    label("loc_63FA")


    ChrTalk(
        0xFE,
        (
            "Aah, now that I think about it, there's Sunday\x01",
            "School today starting in the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Pluna, did you do the homework they gave us?\x02",
    )

    CloseMessageWindow()

    label("loc_6486")

    TalkEnd(0xFE)
    Return()

    # Function_9_5B84 end

    def Function_10_648A(): pass

    label("Function_10_648A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_652F")

    ChrTalk(
        0xFE,
        (
            "W-Why such a huge tree\x01",
            "is floating in the air?\x01",
            "It's physically impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, is it alright for me to\x01",
            "be here giving away balloons...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707A")

    label("loc_652F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_653D")
    Jump("loc_707A")

    label("loc_653D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6611")

    ChrTalk(
        0xFE,
        (
            "Crossbell independence, eh...?\x01",
            "Things really got serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if it's not a festive atmosphere,\x01",
            "for the time being I guess I'll make original\x01",
            "balloons as if for the founding anniversary.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707A")

    label("loc_6611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_661F")
    Jump("loc_707A")

    label("loc_661F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_66E3")

    ChrTalk(
        0xFE,
        (
            "I don't know if they're an armed group or not,\x01",
            "still they do some totally terrible things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel like wanting to tell them "I'll give\x01",
            "you a balloon, so get away at once".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707A")

    label("loc_66E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_66F1")
    Jump("loc_707A")

    label("loc_66F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6783")

    ChrTalk(
        0xFE,
        (
            "Do you want a balloooon?\x01",
            "...I feel it's not the time to say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, an accident, they say.\x01",
            "What on earth has happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707A")

    label("loc_6783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_68D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6858")

    ChrTalk(
        0xFE,
        "Do you want a balloooon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By all means, adults too\x01",
            "are welcome, don't be shy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometimes don't you want to forget about complex\x01",
            "things and retrieve your childish innocence?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_68D4")

    label("loc_6858")


    ChrTalk(
        0xFE,
        (
            "By all means, adults too\x01",
            "are welcome, don't be shy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometimes don't you want to retrieve\x01",
            "your childish innocence?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D4")

    Jump("loc_707A")

    label("loc_68D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6A58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69E8")

    ChrTalk(
        0xFE,
        (
            "Some time ago I was asked\x01",
            "by a tourist child this: \x01",
            ""Why balloons float?"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And so, without a moment's\x01",
            "delay I replied: "Because\x01",
            "they're filled with dreams"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nowadays children are cruel. As soon\x01",
            "as I said that, I was sneered at.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6A53")

    label("loc_69E8")


    ChrTalk(
        0xFE,
        "Let's have more dreams, children.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A gas lighter than air? Nope,\x01",
            "balloons are filled with dreams.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A53")

    Jump("loc_707A")

    label("loc_6A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6AEE")

    ChrTalk(
        0xFE,
        "Do you want a balloooon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I have balloons with printed the crests of the\x01",
            " countries participating at the Trade Conference!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707A")

    label("loc_6AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6B97")

    ChrTalk(
        0xFE,
        "Well then, I guess I'll slowly go back home for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thank goodness today many people passed by\x01",
            "and I was able to hand over a lot of balloons.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707A")

    label("loc_6B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6C57")

    ChrTalk(
        0xFE,
        (
            "Well, when the limousines passed\x01",
            "through here, I was really nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say it, there's a different kind of enthusiasm\x01",
            "from the Founding Anniversary Festival time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707A")

    label("loc_6C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6EB3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DC9")
    TurnDirection(0xE, 0x1A2, 0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "Oh, you there, little boy.\x01",
            "Say, do you want a balloon?\x01",
            "It's fun, it floats lightly and gently...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "...Don't wanna.\x01",
            "That's just a hindrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Alright, then, what color\x01",
            "do you w....wait, what?\x01",
            "A hindrance you said?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Ha ha, it seems that\x01",
            "Shing doesn't like\x01",
            "childish things.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1DD, 1)
    Jump("loc_6E4E")

    label("loc_6DC9")


    ChrTalk(
        0xE,
        (
            "Yes, there're kids who aren't\x01",
            "interested in balloons, but...\x01",
            "To refuse it so bluntly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "That's really a little depressing.\x02",
    )

    CloseMessageWindow()

    label("loc_6E4E")

    Jump("loc_6EAE")

    label("loc_6E53")


    ChrTalk(
        0xFE,
        "Do you want a balloooon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Red, blue, yellow and green.\x01",
            "I have different colooors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EAE")

    Jump("loc_707A")

    label("loc_6EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6EC1")
    Jump("loc_707A")

    label("loc_6EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_707A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F51")

    ChrTalk(
        0xFE,
        (
            "That car just before scared me\x01",
            "and I let fly away some balloons!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, what a waste...\x01",
            "Come baaack...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707A")

    label("loc_6F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FF5")

    ChrTalk(
        0xFE,
        (
            "Do you want a balloooon?\x01",
            "Please take one with you while\x01",
            "touring around Crossbeeell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I assure you it'll put you\x01",
            "in a fun and good moood!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_707A")

    label("loc_6FF5")


    ChrTalk(
        0xFE,
        (
            "I give balloons also to people\x01",
            "who aren't touriiists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's someone who wants one,\x01",
            "please say it whenever you waaant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_707A")

    TalkEnd(0xFE)
    Return()

    # Function_10_648A end

    def Function_11_707E(): pass

    label("Function_11_707E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_END)), "loc_708F")
    Jump("loc_733B")

    label("loc_708F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_714B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_712B")

    ChrTalk(
        0x11,
        "#01203FGrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, staying here like this you\x01",
            "really look like a watch dog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7146")

    label("loc_712B")


    ChrTalk(
        0x11,
        "#01200FGrrowl...woof.\x02",
    )

    CloseMessageWindow()

    label("loc_7146")

    Jump("loc_733B")

    label("loc_714B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_715C")
    Jump("loc_733B")

    label("loc_715C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_716A")
    Jump("loc_733B")

    label("loc_716A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_733B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_718B")
    Call(1, 23)
    Return()

    label("loc_718B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_731C")

    ChrTalk(
        0x11,
        "#01203FGrrrowl......\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72A6")

    ChrTalk(
        0x101,
        "#00005FUhm? Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200F......Woof.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#01100FNope, not at all, he says.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I see. Well, please watch\x02\x03",
            "#00000Fthe house today too, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A5,
        "#01109FZeit, we're goooing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01200FWoof.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7314")

    label("loc_72A6")


    ChrTalk(
        0x101,
        (
            "#00003F(Looks like he still had something\x01",
            "to say... When Tio or KeA are \x01",
            "around, we can understand him.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7314")

    SetScenarioFlags(0x1, 1)
    Jump("loc_7336")

    label("loc_731C")


    ChrTalk(
        0x11,
        "#01203FGrrrowl......\x02",
    )

    CloseMessageWindow()

    label("loc_7336")

    Jump("loc_733B")

    label("loc_733B")

    TalkEnd(0xFE)
    Return()

    # Function_11_707E end

    def Function_12_733F(): pass

    label("Function_12_733F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_751E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_746D")

    ChrTalk(
        0xFE,
        (
            "Things have gotten serious, but\x01",
            "don't be discouraged, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With all the hardships you guys went\x01",
            "through, I'm sure you'll be able to\x01",
            "solve this incident too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I assure you that, you\x01",
            "can go with confidence!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha...\x01",
            "Thank you, senior Kate.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7519")

    label("loc_746D")


    ChrTalk(
        0xFE,
        (
            "I'm sure that you and the others will\x01",
            "be able to solve this incident too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Go with confidence! We from the District Crime\x01",
            "Prevention Section will do our best too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7519")

    Jump("loc_8386")

    label("loc_751E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_752C")
    Jump("loc_8386")

    label("loc_752C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_753A")
    Jump("loc_8386")

    label("loc_753A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7548")
    Jump("loc_8386")

    label("loc_7548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_773F")

    ChrTalk(
        0xFE,
        (
            "It's natural that it seems that many\x01",
            "citizens received a shock from the\x01",
            "Mainz occupation incident, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have the impression that, in some respects, there're\x01",
            "also many people thinking that it's none of their business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, I also have the impression that,\x01",
            "due to the incident, the affirmers for\x01",
            "the national independence rose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, we must pay attention not only to\x01",
            "what people need but also their anxieties, so\x01",
            "that disturbances do not occur.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_780F")

    label("loc_773F")


    ChrTalk(
        0xFE,
        (
            "It appears that among the \x01",
            "citizens many thoughts \x01",
            "are spreading, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, we must pay attention not only to\x01",
            "what people need but also their anxieties, so\x01",
            "that disturbances do not occur.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_780F")

    Jump("loc_8386")

    label("loc_7814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_790E")

    ChrTalk(
        0xFE,
        (
            "After hearing that the transcontinental\x01",
            "railway service was somehow restored\x01",
            "this morning, I really felt relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Above not being able to use the\x01",
            "railway and then this rain...I thought\x01",
            "things would've been hard in many ways.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8386")

    label("loc_790E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_79EF")

    ChrTalk(
        0xFE,
        (
            "A derailment accident...\x01",
            "Another difficult situation has arisen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, the traffic volume of orbal vehicles\x01",
            "is probably going to increase for a while.\x01",
            "I've got to do my best at traffic control!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8386")

    label("loc_79EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7BF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B76")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "*phee pheee, phee pheee*!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please go slow with your orbal vehicles.\x01",
            "Please cooperate to keep the city saaafe!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "Could this be an independence proposal effect...?\x01",
            "I have a feeling that recently the orbal vehicles\x01",
            "coming from abroad have decreased somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, while it may be true, we can't\x01",
            "neglect vigilance towards incidents.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7BF4")

    label("loc_7B76")

    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        "*phee pheee, phee pheee*!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please go slow with your orbal vehicles.\x01",
            "Please cooperate to keep the city saaafe!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BF4")

    Jump("loc_8386")

    label("loc_7BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E41")

    ChrTalk(
        0xFE,
        (
            "It appears that recently the persons\x01",
            "who don't respect traffic rules for\x01",
            "obal vehicles have been increasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Traffic rules" are just words;\x01",
            "before those, what's important are\x01",
            "the drivers' morals and manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Morals that everyone should've been taught at Sunday \x01",
            "School, when they become adults are not respected \x01",
            "anymore...that's a really sad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You too guys, when you hold the\x01",
            "handle, never forget to pay attention\x01",
            "to the surrounding people, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes, that goes without saying!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...We understood very well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7F3D")

    label("loc_7E41")


    ChrTalk(
        0xFE,
        (
            ""Traffic rules" are just words;\x01",
            "before those, what's important are\x01",
            "the drivers' morals and manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Morals that everyone should've been taught at Sunday \x01",
            "School, when they become adults are not respected \x01",
            "anymore...that's a really sad thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F3D")

    Jump("loc_8386")

    label("loc_7F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7FF7")

    ChrTalk(
        0xFE,
        (
            "There's a high possibility that\x01",
            "terrorists will show up...\x01",
            "I really can't let my guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must pay my utmost attention\x01",
            "to suspicious people and things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8386")

    label("loc_7FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_80C6")

    ChrTalk(
        0xFE,
        (
            "They made me lead the limousines\x01",
            "in which the VIPs were riding...\x01",
            "I was really quite tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How should I say it... Although they were\x01",
            "riding in cars, it's like they emanated an aura.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8386")

    label("loc_80C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_81BD")

    ChrTalk(
        0xFE,
        (
            "With the starting of patrols in various \x01",
            "places from today, it seems that illegal\x01",
            "parkings have dropped sharply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How nice would be if this was the normality...\x01",
            "Well, for now it's a good thing, \x01",
            "so I guess I can't complain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8386")

    label("loc_81BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_837D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82D5")
    OP_93(0xFE, 0xB4, 0x0)

    ChrTalk(
        0xFE,
        (
            "*phee pheee, phee pheee*!\x01",
            "Please go slow with your orbal vehicleees.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0xFE,
        (
            "On rainy days, traffic volume increases\x01",
            "somewhat more than normally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The road surface is easy to slip on too,\x01",
            "so more attention than usual is required.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_8378")

    label("loc_82D5")


    ChrTalk(
        0xFE,
        (
            "On rainy days, traffic volume increases,\x01",
            "somewhat more than normally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The road surface is easy to slip on too,\x01",
            "so more attention than usual is required.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8378")

    Jump("loc_8386")

    label("loc_837D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8386")

    label("loc_8386")

    TalkEnd(0xFE)
    Return()

    # Function_12_733F end

    def Function_13_838A(): pass

    label("Function_13_838A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_851D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8481")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C6")
    Call(0, 104)
    Jump("loc_8480")

    label("loc_83C6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "A black wagon? A little while ago it passed\x01",
            "through and went towards East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're chasing it, wouldn't it be\x01",
            "better for you to drive an orbal \x01",
            "vehicle too. No?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_8480")

    Return()

    label("loc_8481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_848F")
    Call(1, 26)
    Return()

    label("loc_848F")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Damn jaegers...\x01",
            "Why did they steal the\x01",
            ""Crossbell Bell"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, even if I think about it,\x01",
            "there's nothing that can be done.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_851D")

    Return()

    # Function_13_838A end

    def Function_14_851E(): pass

    label("Function_14_851E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86A7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_855A")
    Call(0, 104)
    Jump("loc_85CF")

    label("loc_855A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The wagon from some time ago will\x01",
            "arrive at Tangram Gate shortly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I pray for your success, everyone!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_85CF")

    Return()

    label("loc_85D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85DE")
    Call(1, 26)
    Return()

    label("loc_85DE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "For the current CGF, the state\x01",
            "of tension between the two major\x01",
            "powers is the biggest concern of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We look for the "bell"\x01",
            "whereabouts when patrolling, \x01",
            "but that is our top priority.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_86A7")

    Return()

    # Function_14_851E end

    def Function_15_86A8(): pass

    label("Function_15_86A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8714")

    ChrTalk(
        0xFE,
        (
            "The Trade Conference is finally at its climax.\x01",
            "I have to increase my focus even more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8822")

    label("loc_8714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_87A4")

    ChrTalk(
        0xFE,
        (
            "At last, VIPs have\x01",
            "arrived in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I'm relieved that the inauguration\x01",
            "ceremony went without any incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8822")

    label("loc_87A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8822")

    ChrTalk(
        0xFE,
        (
            "City patrols are scheduled to take place\x01",
            "until the last day of the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to do my best!\x02",
    )

    CloseMessageWindow()

    label("loc_8822")

    TalkEnd(0xFE)
    Return()

    # Function_15_86A8 end

    def Function_16_8826(): pass

    label("Function_16_8826")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The "State Guard" is not a force\x01",
            "to "fight" but one to "protect".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are different from those Imperial\x01",
            "and Republican armies savages.\x01",
            "So, please, don't worry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_8826 end

    def Function_17_88D6(): pass

    label("Function_17_88D6")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Stealing the city symbol...\x01",
            "What kind of harassment is this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "They ruined a well known spot.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_88D6 end

    def Function_18_8943(): pass

    label("Function_18_8943")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The talk saying that the bell had\x01",
            "vanished was really true!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An armed group, eh...?\x01",
            "Their true objective is a mystery.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_8943 end

    def Function_19_89CA(): pass

    label("Function_19_89CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AB8")

    ChrTalk(
        0x12,
        "#01111F...........\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F...KeA? What's wrong?\x01",
            "You're spacing out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x0, 500)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#01105FAh...no, it's nothing.\x02\x03",
            "#01109FEveryone, do your best at work todaaay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F...?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x159, 1)
    SetScenarioFlags(0x151, 6)
    Jump("loc_8AEC")

    label("loc_8AB8")


    ChrTalk(
        0x12,
        "#01109FEveryone, do your best at work todaaay!\x02",
    )

    CloseMessageWindow()

    label("loc_8AEC")

    TalkEnd(0xFE)
    Return()

    # Function_19_89CA end

    def Function_20_8AF0(): pass

    label("Function_20_8AF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B0A")
    Call(1, 23)
    Return()

    label("loc_8B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C88")

    ChrTalk(
        0x104,
        "#00302FHeiya, Koppe, doin' good?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Nyaa～～[I'm hungry]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FSomehow he looks\x01",
            "like to be hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FOh, I want to\x01",
            "try feeding him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FKoppe will eat with joy\x01",
            "the fish we catch or\x01",
            ""catfood", you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, do we have any right now...?\x02\x03",
            "#00000FAt any rate, we mustn't forget\x01",
            "to give him food every morning.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 3)
    TalkEnd(0xFE)
    Return()

    label("loc_8C88")

    ClearScenarioFlags(0x1, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8C97")
    Call(1, 22)

    label("loc_8C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1D")

    ChrTalk(
        0x101,
        (
            "#00005F(Now that I think about it...\x01",
            "Did we have some caught fish?)\x02\x03",
            "#00004F(Giving it to Koppe\x01",
            "would be nice.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13A, 0)

    label("loc_8D1D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8D48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_8D43")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D43")

    Jump("loc_8E4B")

    label("loc_8D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8D69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_8D64")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D64")

    Jump("loc_8E4B")

    label("loc_8D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8D8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_8D85")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D85")

    Jump("loc_8E4B")

    label("loc_8D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_8DA6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8DA6")

    Jump("loc_8E4B")

    label("loc_8DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_8DC7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8DC7")

    Jump("loc_8E4B")

    label("loc_8DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8DED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_8DE8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8DE8")

    Jump("loc_8E4B")

    label("loc_8DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8E0E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_8E09")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E09")

    Jump("loc_8E4B")

    label("loc_8E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_8E2A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E2A")

    Jump("loc_8E4B")

    label("loc_8E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8E4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_8E4B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3C5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8E68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3C0")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "Talk")
    MenuCmd(1, 1, "Give Food")
    MenuCmd(1, 1, "Quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8ED3")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8ED3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A38B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_8F0F")
    MenuCmd(1, 1, "Fighter")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_8F31")
    MenuCmd(1, 1, "Snow Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_8F54")
    MenuCmd(1, 1, "Angel Fish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F54")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_8F74")
    MenuCmd(1, 1, "Kasagin")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_8F9A")
    MenuCmd(1, 1, "Armorica Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F9A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_8FBB")
    MenuCmd(1, 1, "Tortoise")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_8FE2")
    MenuCmd(1, 1, "Tiger Rockfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_9004")
    MenuCmd(1, 1, "Rockeater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9004")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_902A")
    MenuCmd(1, 1, "Rainbow Trout")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_902A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_904A")
    MenuCmd(1, 1, "Piranha")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_904A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_9067")
    MenuCmd(1, 1, "Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9067")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_908F")
    MenuCmd(1, 1, "Gluttonous Bass")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_908F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_90AD")
    MenuCmd(1, 1, "Trout")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_90CF")
    MenuCmd(1, 1, "Gladiator")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_90EF")
    MenuCmd(1, 1, "Walleye")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90EF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_9112")
    MenuCmd(1, 1, "Salamander")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9112")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_9131")
    MenuCmd(1, 1, "Salmon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9131")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_9151")
    MenuCmd(1, 1, "Arowana")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9151")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_916D")
    MenuCmd(1, 1, "Eel")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_916D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_9191")
    MenuCmd(1, 1, "Adamantoise")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9191")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_91B4")
    MenuCmd(1, 1, "Queen Crab")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_91D5")
    MenuCmd(1, 1, "Pirarucu")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_91F5")
    MenuCmd(1, 1, "Catfish")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_9219")
    MenuCmd(1, 1, "Gold Salmon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9219")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_END)), "loc_9241")
    MenuCmd(1, 1, "Pale Salamander")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9241")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_END)), "loc_9264")
    MenuCmd(1, 1, "Noble Carp")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9264")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_END)), "loc_9285")
    MenuCmd(1, 1, "Emeraude")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9285")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_END)), "loc_92AD")
    MenuCmd(1, 1, "Tiger Rockeater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_END)), "loc_92D3")
    MenuCmd(1, 1, "Crimson Eater")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_END)), "loc_92F7")
    MenuCmd(1, 1, "Bull Dragon")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_END)), "loc_931E")
    MenuCmd(1, 1, "Giant Pirarucu")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_931E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_933F")
    MenuCmd(1, 1, "Cat Food")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_933F")

    MenuCmd(1, 1, "Quit")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9387")
    Jump("loc_A37C")

    label("loc_9387")

    TalkEnd(0xFE)
    EventBegin(0x1)
    OP_4B(0x10, 0xFF)
    Fade(500)
    SetChrPos(0x10, -21980, 1300, -19300, 270)
    SetChrPos(0x0, -23900, 1300, -19070, 89)
    SetChrPos(0x1, -23540, 1300, -20210, 89)
    SetChrPos(0x2, -25020, 1300, -19860, 89)
    SetChrPos(0x3, -25130, 1300, -18930, 89)
    SetChrPos(0x4, -26200, 1300, -19870, 89)
    SetChrPos(0x5, -26790, 1300, -19180, 89)
    OP_68(-23130, 3900, -19610, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0xFE,
        "Nyannyan......㈱\x02",
    )

    CloseMessageWindow()

    def lambda_9456():

        label("loc_9456")

        TurnDirection(0x0, 0x10, 0)
        Yield()
        Jump("loc_9456")

    QueueWorkItem2(0x0, 1, lambda_9456)

    def lambda_9468():

        label("loc_9468")

        TurnDirection(0x1, 0x10, 0)
        Yield()
        Jump("loc_9468")

    QueueWorkItem2(0x1, 1, lambda_9468)

    def lambda_947A():

        label("loc_947A")

        TurnDirection(0x2, 0x10, 0)
        Yield()
        Jump("loc_947A")

    QueueWorkItem2(0x2, 1, lambda_947A)

    def lambda_948C():

        label("loc_948C")

        TurnDirection(0x3, 0x10, 0)
        Yield()
        Jump("loc_948C")

    QueueWorkItem2(0x3, 1, lambda_948C)

    def lambda_949E():

        label("loc_949E")

        TurnDirection(0x4, 0x10, 0)
        Yield()
        Jump("loc_949E")

    QueueWorkItem2(0x4, 1, lambda_949E)

    def lambda_94B0():

        label("loc_94B0")

        TurnDirection(0x5, 0x10, 0)
        Yield()
        Jump("loc_94B0")

    QueueWorkItem2(0x5, 1, lambda_94B0)
    SetChrFlags(0x10, 0x8000)
    OP_93(0x10, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x10, 0x1)
    Sound(809, 0, 80, 0)

    def lambda_94DC():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_94DC)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_9503():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9503)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_952A():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_952A)
    WaitChrThread(0x10, 1)
    Sleep(2000)
    OP_93(0x10, 0xB4, 0x1F4)
    Sound(809, 0, 80, 0)

    def lambda_955B():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_955B)
    WaitChrThread(0x10, 1)
    Sound(809, 0, 80, 0)

    def lambda_9582():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9582)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 80, 0)

    def lambda_95A9():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_95A9)
    WaitChrThread(0x10, 1)
    SetChrFlags(0x10, 0x1)
    OP_93(0x10, 0x10E, 0x1F4)
    ClearChrFlags(0x10, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    ChrTalk(
        0xFE,
        "Funyaawn......\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_967B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9671")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15E, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x68, 1)

    label("loc_9671")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_967B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_96C5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96BB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15F, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x74),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x74, 1)

    label("loc_96BB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_96C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_970F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9705")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x160, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x79),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x79, 1)

    label("loc_9705")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_970F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_9759")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_974F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x161, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x92),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x92, 1)

    label("loc_974F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9759")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_97A3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9799")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x162, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x84),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x84, 1)

    label("loc_9799")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_97ED")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x163, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x7C, 1)

    label("loc_97E3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_9837")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x164, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB2, 1)

    label("loc_982D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9837")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_9881")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9877")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x165, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x71),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x71, 1)

    label("loc_9877")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9881")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_98CB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98C1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x166, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xBA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xBA, 1)

    label("loc_98C1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_98CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_9915")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_990B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x167, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x9C, 1)

    label("loc_990B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9915")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_995F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9955")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x168, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x64, 1)

    label("loc_9955")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_995F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_99A9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_999F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x169, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x6C, 1)

    label("loc_999F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_99F3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99E9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16A, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x9E, 1)

    label("loc_99E9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_9A3D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A33")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16B, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x8C, 1)

    label("loc_9A33")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_9A87")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A7D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16C, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xAF, 1)

    label("loc_9A7D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_9AD1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16D, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x80),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x80, 1)

    label("loc_9AC7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AD1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_9B1B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B11")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16E, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x8F, 1)

    label("loc_9B11")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_9B65")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B5B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16F, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x9B, 1)

    label("loc_9B5B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_9BAF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BA5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x170, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x88),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x88, 1)

    label("loc_9BA5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_9BF9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BEF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x171, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x97),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x97, 1)

    label("loc_9BEF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BF9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_9C43")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C39")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x172, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x6E, 1)

    label("loc_9C39")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C43")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_9C8D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C83")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x173, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x7E, 1)

    label("loc_9C83")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_9CD7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CCD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x174, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x72, 1)

    label("loc_9CCD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_9D21")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D17")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x175, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB8, 1)

    label("loc_9D17")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_END)), "loc_9D6B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D61")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x176, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x66),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0x66, 1)

    label("loc_9D61")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_END)), "loc_9DB5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DAB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x177, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB6, 1)

    label("loc_9DAB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_END)), "loc_9DFF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DF5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x178, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB5, 1)

    label("loc_9DF5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_END)), "loc_9E49")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E3F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x179, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB4, 1)

    label("loc_9E3F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E49")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_END)), "loc_9E93")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E89")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x17A, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xB1, 1)

    label("loc_9E89")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_END)), "loc_9EDD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9ED3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x17B, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xAE, 1)

    label("loc_9ED3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EDD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_END)), "loc_9F27")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F1D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x17C, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xC6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    AddItemNumber(0xC6, 1)

    label("loc_9F1D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9F27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_9F74")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F6A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D9, 1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x3 received.\x02",
        )
    )

    AddItemNumber(0x12D, 3)

    label("loc_9F6A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9F74")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9F9B")
    SetScenarioFlags(0x13B, 1)
    Jump("loc_A01E")

    label("loc_9F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9FAC")
    SetScenarioFlags(0x13B, 0)
    Jump("loc_A01E")

    label("loc_9FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9FBD")
    SetScenarioFlags(0x13A, 7)
    Jump("loc_A01E")

    label("loc_9FBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9FCE")
    SetScenarioFlags(0x13A, 6)
    Jump("loc_A01E")

    label("loc_9FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_9FDF")
    SetScenarioFlags(0x13A, 5)
    Jump("loc_A01E")

    label("loc_9FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9FF0")
    SetScenarioFlags(0x13A, 4)
    Jump("loc_A01E")

    label("loc_9FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A001")
    SetScenarioFlags(0x13A, 3)
    Jump("loc_A01E")

    label("loc_A001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A012")
    SetScenarioFlags(0x13A, 2)
    Jump("loc_A01E")

    label("loc_A012")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A01E")
    SetScenarioFlags(0x13A, 1)

    label("loc_A01E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 1)), scpexpr(EXPR_END)), "loc_A03B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A03B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 2)), scpexpr(EXPR_END)), "loc_A04E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A04E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 3)), scpexpr(EXPR_END)), "loc_A061")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 4)), scpexpr(EXPR_END)), "loc_A074")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 5)), scpexpr(EXPR_END)), "loc_A087")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 6)), scpexpr(EXPR_END)), "loc_A09A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A09A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13A, 7)), scpexpr(EXPR_END)), "loc_A0AD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A0AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 0)), scpexpr(EXPR_END)), "loc_A0C0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A0C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 1)), scpexpr(EXPR_END)), "loc_A0D3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A0D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1A1")

    ChrTalk(
        0xFE,
        "Nyannyannya～n......♪\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEE, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A158")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xEE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xEE, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_A1A1")

    label("loc_A158")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_A1A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A1E9")

    ChrTalk(
        0x102,
        "#00105FMy...are you giving this to me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A33E")

    label("loc_A1E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A220")

    ChrTalk(
        0x103,
        "#00205FAre you giving me this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A33E")

    label("loc_A220")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A262")

    ChrTalk(
        0x104,
        "#00305FYou mean you're givin' this to me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A33E")

    label("loc_A262")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2A1")

    ChrTalk(
        0x109,
        "#10105FHuh, are you giving this to me?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A33E")

    label("loc_A2A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2DB")

    ChrTalk(
        0x105,
        "#10305FOh my, are giving me this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A33E")

    label("loc_A2DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A310")

    ChrTalk(
        0x106,
        (
            "#10705FEhm...\x01",
            "I can have it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A33E")

    label("loc_A310")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A33E")

    ChrTalk(
        0x10A,
        "#00605FYou giving me this?\x02",
    )

    CloseMessageWindow()

    label("loc_A33E")


    ChrTalk(
        0x101,
        (
            "#0000FHa ha, thanks.\x01",
            "We'll use it with gratitude.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    EventEnd(0x4)
    Return()

    label("loc_A37C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3BB")

    label("loc_A38B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A39F")
    Jump("loc_A3BB")

    label("loc_A39F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3BB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 21)

    label("loc_A3BB")

    Jump("loc_8E68")

    label("loc_A3C0")

    Jump("loc_A3C8")

    label("loc_A3C5")

    Call(1, 21)

    label("loc_A3C8")

    TalkEnd(0xFE)
    Return()

    # Function_20_8AF0 end

    def Function_21_A3CC(): pass

    label("Function_21_A3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A4D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A49F")

    ChrTalk(
        0x10,
        "Nyao...?[What's wrong?]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FKoppe, please watch over\x01",
            "the house just for a little while.\x02\x03",
            "#00200FWe'll bring back\x01",
            "KeA for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "...Nyaaoo～n.[You're absolutely right]\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A4CB")

    label("loc_A49F")


    ChrTalk(
        0x10,
        "...Nyaaoo～n.[You're absolutely right]\x02",
    )

    CloseMessageWindow()

    label("loc_A4CB")

    Jump("loc_A9ED")

    label("loc_A4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_A4DE")
    Jump("loc_A9ED")

    label("loc_A4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A4FE")

    ChrTalk(
        0x10,
        "Fumyaaawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9ED")

    label("loc_A4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A51C")

    ChrTalk(
        0x10,
        "Fumyawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9ED")

    label("loc_A51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A547")

    ChrTalk(
        0x10,
        "Nyaon...?[Who are you?]\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9ED")

    label("loc_A547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A555")
    Jump("loc_A9ED")

    label("loc_A555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A580")

    ChrTalk(
        0x10,
        "Nyaya～～go...[Hold up]\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9ED")

    label("loc_A580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_A59E")

    ChrTalk(
        0x10,
        "Fumyawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9ED")

    label("loc_A59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A5BC")

    ChrTalk(
        0x10,
        "Fumyaaawn.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9ED")

    label("loc_A5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A68C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A675")

    ChrTalk(
        0x10,
        "Nyaao.[So, we meet again... fleshy thing.]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FHu hu...\x01",
            "Long time no see, Koppe.\x02\x03",
            "Starting from today, I'll\x01",
            "give you food too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Nyayayaa～㈱\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A687")

    label("loc_A675")


    ChrTalk(
        0x10,
        "Nyayayaa～㈱\x02",
    )

    CloseMessageWindow()

    label("loc_A687")

    Jump("loc_A9ED")

    label("loc_A68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_A7DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7BD")

    ChrTalk(
        0x10,
        "Nyaago.[It's been a while. How have you been?]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00600FThe Support Section pet cat?\x02\x03",
            "#00603F(*pet, pet*...)\x01",
            "...You have settled in a\x01",
            "toilsome place too, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Nyaa～～o......㈱[That's right]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Mr. Dudley... He's unexpectedly\x01",
            "good in dealing with cats...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A7D6")

    label("loc_A7BD")


    ChrTalk(
        0x10,
        "Nyaon...[I'm tired]\x02",
    )

    CloseMessageWindow()

    label("loc_A7D6")

    Jump("loc_A9ED")

    label("loc_A7DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_END)), "loc_A803")

    ChrTalk(
        0x10,
        "Nyao?[What's wrong?]\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9ED")

    label("loc_A803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A821")

    ChrTalk(
        0x10,
        "Fumyawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9ED")

    label("loc_A821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A849")

    ChrTalk(
        0x10,
        "Nyaa～～[I'm hungry]\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9ED")

    label("loc_A849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_A857")
    Jump("loc_A9ED")

    label("loc_A857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_A9ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9D8")

    ChrTalk(
        0x101,
        (
            "#00005FOh, right, we have\x01",
            "to feed Koppe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "Nyao?[What's wrong?]\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8EB")

    ChrTalk(
        0x1A5,
        "#01100FHe says he's full, now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A91B")

    label("loc_A8EB")


    ChrTalk(
        0x105,
        (
            "#10300FStill, he looks like\x01",
            "he's full now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A91B")


    ChrTalk(
        0x102,
        (
            "#00100FIt seems that Chief has given\x01",
            "him food before going out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FUuh, it's a bit of a pity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, well, shall we bring him\x01",
            "a fish next time we got one?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13B, 2)
    Jump("loc_A9ED")

    label("loc_A9D8")


    ChrTalk(
        0x10,
        "Nyanyayayaa～㈱\x02",
    )

    CloseMessageWindow()

    label("loc_A9ED")

    Return()

    # Function_21_A3CC end

    def Function_22_A9EE(): pass

    label("Function_22_A9EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_A9FC")
    SetScenarioFlags(0x1, 3)

    label("loc_A9FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_AA0A")
    SetScenarioFlags(0x1, 3)

    label("loc_AA0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_AA18")
    SetScenarioFlags(0x1, 3)

    label("loc_AA18")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_AA26")
    SetScenarioFlags(0x1, 3)

    label("loc_AA26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_AA34")
    SetScenarioFlags(0x1, 3)

    label("loc_AA34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_AA42")
    SetScenarioFlags(0x1, 3)

    label("loc_AA42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_AA50")
    SetScenarioFlags(0x1, 3)

    label("loc_AA50")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_AA5E")
    SetScenarioFlags(0x1, 3)

    label("loc_AA5E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_AA6C")
    SetScenarioFlags(0x1, 3)

    label("loc_AA6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_AA7A")
    SetScenarioFlags(0x1, 3)

    label("loc_AA7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_AA88")
    SetScenarioFlags(0x1, 3)

    label("loc_AA88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_AA96")
    SetScenarioFlags(0x1, 3)

    label("loc_AA96")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_AAA4")
    SetScenarioFlags(0x1, 3)

    label("loc_AAA4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_AAB2")
    SetScenarioFlags(0x1, 3)

    label("loc_AAB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_AAC0")
    SetScenarioFlags(0x1, 3)

    label("loc_AAC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_AACE")
    SetScenarioFlags(0x1, 3)

    label("loc_AACE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_AADC")
    SetScenarioFlags(0x1, 3)

    label("loc_AADC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_AAEA")
    SetScenarioFlags(0x1, 3)

    label("loc_AAEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_AAF8")
    SetScenarioFlags(0x1, 3)

    label("loc_AAF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_AB06")
    SetScenarioFlags(0x1, 3)

    label("loc_AB06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_AB14")
    SetScenarioFlags(0x1, 3)

    label("loc_AB14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_AB22")
    SetScenarioFlags(0x1, 3)

    label("loc_AB22")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_AB30")
    SetScenarioFlags(0x1, 3)

    label("loc_AB30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_AB3E")
    SetScenarioFlags(0x1, 3)

    label("loc_AB3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x176, 0x0)"), scpexpr(EXPR_END)), "loc_AB4C")
    SetScenarioFlags(0x1, 3)

    label("loc_AB4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x177, 0x0)"), scpexpr(EXPR_END)), "loc_AB5A")
    SetScenarioFlags(0x1, 3)

    label("loc_AB5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x178, 0x0)"), scpexpr(EXPR_END)), "loc_AB68")
    SetScenarioFlags(0x1, 3)

    label("loc_AB68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x179, 0x0)"), scpexpr(EXPR_END)), "loc_AB76")
    SetScenarioFlags(0x1, 3)

    label("loc_AB76")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17A, 0x0)"), scpexpr(EXPR_END)), "loc_AB84")
    SetScenarioFlags(0x1, 3)

    label("loc_AB84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17B, 0x0)"), scpexpr(EXPR_END)), "loc_AB92")
    SetScenarioFlags(0x1, 3)

    label("loc_AB92")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17C, 0x0)"), scpexpr(EXPR_END)), "loc_ABA0")
    SetScenarioFlags(0x1, 3)

    label("loc_ABA0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_ABAE")
    SetScenarioFlags(0x1, 3)

    label("loc_ABAE")

    Return()

    # Function_22_A9EE end

    def Function_23_ABAF(): pass

    label("Function_23_ABAF")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    SetChrPos(0x101, -25020, 1300, -19860, 90)
    SetChrPos(0x102, -25130, 1300, -18930, 90)
    SetChrPos(0x109, -26200, 1300, -19870, 90)
    SetChrPos(0x105, -26790, 1300, -19180, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC2A")
    SetChrPos(0x1A5, -24820, 1300, -16830, 133)

    label("loc_AC2A")

    OP_68(-24880, 3000, -20830, 0)
    MoveCamera(43, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(10510, 0)
    OP_0D()

    ChrTalk(
        0x11,
        "#01200FGrrrrowl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FZeit and Koppe,\x01",
            "you're together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F*giggle*, they get along nicely as usual.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, the police dog you're keeping\x01",
            "at the Special Support Section, right?\x02\x03",
            "#10300FNice to meet you again, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#01203FGrrowl...woof.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEB0")

    ChrTalk(
        0x1A5,
        (
            "#01104F"Keeping" is not the right word, it is I\x01",
            "who's looking after them" he says.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#6P#10309FAhaha, I used an improper word, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FW-Well...\x01",
            "He's always helping us.\x01",
            "He's very proud as usual...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF35")

    label("loc_AEB0")


    ChrTalk(
        0x101,
        (
            "#00005FSomehow it looks like he\x01",
            "wants to say something else...\x02\x03",
            "#00003FHmm, if Tio or KeA were with\x01",
            "us we could understand him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF35")

    TurnDirection(0x109, 0x10, 500)

    ChrTalk(
        0x109,
        (
            "#6P#10102FHu hu, I was not good around dogs,\x01",
            "but in the end I got used to Zeit.\x02\x03",
            "#10105FAnd...this black cat is?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FAh, he's called Koppe.\x02\x03",
            "It seems he's been living here\x01",
            "since the time the Crossbell\x01",
            "News Service was in this building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PNyaago.[It's been a while. How have you been?]\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FHu hu, how cute.\x02\x03",
            "#10109FAah, from now on I can interact with\x01",
            "a cat at the Support Section...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FDo you like cats, Miss Noｱl?\x01",
            "*giggle*, you'll have a good time from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#11PFumyaawn...\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24690, 1300, -19050, 90)
    SetScenarioFlags(0x139, 7)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0xB4, 0x0)
    OP_4C(0x11, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_ABAF end

    def Function_24_B179(): pass

    label("Function_24_B179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B1B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1B0")
    Call(1, 26)
    Return()

    label("loc_B1B0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "         The "Crossbell's Bell"\x01",
            "A giant bell excavated in the\x01",
            "autonomous state Crossbell in S1185.\x01",
            "From the condition of the unearthed\x01",
            "remains, it is thought to be from the \x01",
            "Middle Ages period.\x01",
            "Made by multiple metals, when\x01",
            "hit it rings of a pleasant low tone.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is surmised it was built by an \x01",
            "influential person of those times, but\x01",
            "it is still debated for what it was used.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_B179 end

    def Function_25_B368(): pass

    label("Function_25_B368")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8A9")

    ChrTalk(
        0x1A2,
        (
            "Gironde Weapons Shop...\x01",
            "I see, it's a lawful weapons store, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        "Alright, let's drop by it for a little.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B445")

    def lambda_B415():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B415)
    Sleep(50)

    def lambda_B425():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B425)
    Sleep(50)

    def lambda_B435():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B435)
    Sleep(300)
    Jump("loc_B4BC")

    label("loc_B445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B483")

    def lambda_B453():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B453)
    Sleep(50)

    def lambda_B463():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B463)
    Sleep(50)

    def lambda_B473():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B473)
    Sleep(300)
    Jump("loc_B4BC")

    label("loc_B483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B4BC")

    def lambda_B491():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B491)
    Sleep(50)

    def lambda_B4A1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B4A1)
    Sleep(50)

    def lambda_B4B1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B4B1)
    Sleep(300)

    label("loc_B4BC")


    ChrTalk(
        0x101,
        (
            "#00003FSorry, Shing. Like you said,\x01",
            "this is a weapons store.\x02\x03",
            "#00001FInside there're dangerous articles too,\x01",
            "so you can imagine that we can't...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Hmph, I just don't have\x01",
            "to touch them, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "I'm interested into this place.\x01",
            "If I say I'm dropping by, I'm doing it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F(*sigh*...\x01",
            "Elie, if you please.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00100F(*giggle*, got it.)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00103FListen, Shing, you're someone very,\x01",
            "very precious who was left in charge to us.\x02\x03",
            "That's why we must eliminate\x01",
            "dangers towards you, even the very\x01",
            "slightest possibility of one.\x02\x03",
            "#00100FBecause you're smart, Shing, you\x01",
            "understand the situation, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Uh... \x01",
            "It makes sense for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, I'm glad you understand.\x01",
            "I knew that you're wise, Shing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A2,
        (
            "Y-Yes...\x01",
            "I'm a wise person!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B81A")

    ChrTalk(
        0x104,
        "#00309F(Ha ha, Milady's effect was tremendous.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8A1")

    label("loc_B81A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B860")

    ChrTalk(
        0x109,
        (
            "#10109F(Ahaha, Miss Elie had\x01",
            "a tremendous effect.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8A1")

    label("loc_B860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B8A1")

    ChrTalk(
        0x105,
        "#10302F(Hu hu, Elie's was tremendously effective.)\x02",
    )

    CloseMessageWindow()

    label("loc_B8A1")

    SetScenarioFlags(0x1DC, 7)
    Jump("loc_B8F3")

    label("loc_B8A9")


    ChrTalk(
        0x101,
        (
            "#00000FShing is currently with us.\x01",
            "Let's not enter the Weapons Shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8F3")

    TalkEnd(0xFF)
    Return()

    # Function_25_B368 end

    def Function_26_B8F7(): pass

    label("Function_26_B8F7")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x14, 0x0)
    OP_4B(0x15, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 150, 0, -3900, 0)
    SetChrPos(0x109, 1330, 0, -4640, 0)
    SetChrPos(0x102, 2590, 0, -3300, 315)
    SetChrPos(0x103, -1610, 0, -4590, 0)
    SetChrPos(0x105, -900, 0, -5970, 0)
    SetChrPos(0x104, 740, 0, -6130, 0)
    OP_68(-1190, 1900, -5280, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(11710, 0)
    SetChrFlags(0xF, 0x8)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 7)), scpexpr(EXPR_END)), "loc_BC50")

    ChrTalk(
        0x14,
        "Hi, Lloyd and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Everyone from the Special Support Section,\x01",
            "Master Sergeant Noｱl, good morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FGood morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "By the way, did you\x01",
            "settle that job?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BB0C")

    ChrTalk(
        0x101,
        (
            "#00002F#2PYeah, just some time ago.\x01",
            "Thanks to you, Frantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Ha ha, I don't really get it, but\x01",
            "it's an honor if I was of help.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBCE")

    label("loc_BB0C")


    ChrTalk(
        0x101,
        (
            "#00003F#2PY-Yeah...we just finished it.\x02\x03",
            "#00006F(Because we ignored what he told us,\x01",
            "the swindler ended up slipping away...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Ha ha, I don't really get it, but\x01",
            "I'm glad you managed to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBCE")


    ChrTalk(
        0x101,
        (
            "#00005F#2PBy the way, Frantz,\x01",
            "you are stationed\x01",
            "here to guard today?\x02\x03",
            "This is the place senior\x01",
            "Kate is always guarding.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD58")

    label("loc_BC50")


    ChrTalk(
        0x14,
        "Hey, if it isn't Lloyd and friends.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Everyone from the Special Support Section,\x01",
            "Master Sergeant Noｱl, good morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FGood morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#2PFrantz, you are stationed\x01",
            "here to guard today?\x02\x03",
            "This is the place senior\x01",
            "Kate is always guarding.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD58")


    ChrTalk(
        0x14,
        (
            "Yes, senior Kate went to another\x01",
            "place for a different case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "It was decided that I'll be\x01",
            "guarding this place temporarily.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2320, 2800, -900, 2000)
    MoveCamera(45, 8, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(15930, 2000)
    Sleep(2500)

    ChrTalk(
        0x102,
        (
            "#12P#00108F"Crossbell Bell"...\x01",
            "It has been stolen by\x01",
            "the Red Constellation...\x02\x03",
            "#00101FStrengthening the guard in this\x01",
            "place is related to that, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "After all, the major cultural\x01",
            "asset of Crossbell was stolen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Just in case, we from the\x01",
            "CGF have come for support.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1190, 1900, -5280, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(660, 2000)
    SetCameraDistance(11710, 2000)
    Sleep(2500)

    ChrTalk(
        0x103,
        (
            "#00206F#3PYou know neither why\x01",
            "they stole it nor where\x01",
            "it was taken to, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Yeah, for now the police\x01",
            "and the CGF too are looking\x01",
            "for it, but it hasn't been found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#4PUncle and the others...\x01",
            "What on earth did \x01",
            "they do this for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#4PHu hu, it's just a slightly\x01",
            "bulky thing to carry around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#2P...Anyway, we leave the\x01",
            ""bell" to you and we will\x01",
            "do our own job.\x02\x03",
            "#00000FBye then, Frantz. Do your\x01",
            "best guarding the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Yeah, see you later.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x14, 0x0)
    OP_4C(0x15, 0x0)
    ClearChrFlags(0xF, 0x8)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 150, 0, -3900, 0)
    SetScenarioFlags(0x190, 4)
    EventEnd(0x5)
    Return()

    # Function_26_B8F7 end

    SaveToFile()

Try(main)
