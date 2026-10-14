import streamlit as st

st.set_page_config(
    page_title="ECD Individualised Learning Generator",
    page_icon="📚",
    layout="centered"
)

st.title("ECD Individualised Learning Activity Generator")
st.write(
    "Create, personalise and edit learning activities "
    "for Early Childhood Development learners."
)

# SIX ECD LEARNING AREAS AND ALIGNED TOPICS
LEARNING_AREAS = {
    "Mathematics": {
        "Counting and number recognition": [
            "Count objects and recognise numbers.",
            "Bottle tops, counters and number cards.",
            "Let the learner count objects and match quantities to number cards.",
            "Ask the learner to count a selected number of objects."
        ],
        "Addition and subtraction": [
            "Solve simple addition and subtraction problems using objects.",
            "Counters, stones and number cards.",
            "Demonstrate joining groups and taking objects away.",
            "Observe whether the learner solves practical problems."
        ],
        "Shapes and patterns": [
            "Recognise basic shapes and continue simple patterns.",
            "Shape cards, blocks and coloured objects.",
            "Ask the learner to identify shapes and complete a pattern.",
            "Check whether the learner identifies shapes and continues patterns."
        ],
        "Sorting and comparing": [
            "Sort objects and compare their sizes or quantities.",
            "Blocks, bottle tops and classroom objects.",
            "Ask the learner to sort objects by colour, shape or size.",
            "Observe how the learner sorts and compares objects."
        ],
        "Measurement": [
            "Compare length, height, weight and capacity using familiar objects.",
            "Cups, containers and classroom objects.",
            "Let the learner compare objects using longer, shorter, heavier, lighter, full and empty.",
            "Ask the learner to compare two objects."
        ]
    },

    "Shona": {
        "Kwaziso ine rukudzo": [
            "Use appropriate and respectful greetings in Shona.",
            "Greeting cards and role-play materials.",
            "Practise greetings such as Mangwanani and Maswera sei.",
            "Observe whether the learner uses appropriate greetings."
        ],
        "Mazita ezvinhu": [
            "Name familiar people, animals and objects in Shona.",
            "Real objects, toys and picture cards.",
            "Show familiar items and ask the learner to name them in Shona.",
            "Record the words the learner names correctly."
        ],
        "Machemero emhuka": [
            "Identify familiar animals and imitate their sounds.",
            "Animal pictures and toy animals.",
            "Show animal pictures and practise the sounds made by each animal.",
            "Check whether the learner identifies the animals and their sounds."
        ],
        "Kuverenga mifananidzo": [
            "Describe pictures and communicate simple ideas in Shona.",
            "Picture cards and storybooks.",
            "Ask the learner to describe what is happening in a picture.",
            "Listen for relevant words and ideas."
        ],
        "Nziyo nenhetembo": [
            "Participate in familiar Shona songs and rhymes.",
            "Familiar songs, rhymes and picture cards.",
            "Sing a familiar Shona song and encourage the learner to join in.",
            "Observe participation and recall of words."
        ]
    },

    "English": {
        "Alphabet recognition": [
            "Recognise and name letters of the English alphabet.",
            "Alphabet charts and letter cards.",
            "Show selected letters and ask the learner to identify them.",
            "Check whether the learner recognises the selected letters."
        ],
        "Phonics and letter sounds": [
            "Recognise letter sounds and match sounds to familiar words.",
            "Letter cards and picture cards.",
            "Say a letter sound and ask the learner to identify a matching picture.",
            "Listen for correct identification of the sound."
        ],
        "Vocabulary development": [
            "Name familiar objects and use simple English words.",
            "Classroom objects and picture cards.",
            "Ask the learner to name objects and describe their features.",
            "Observe the learner's use of relevant vocabulary."
        ],
        "Listening and speaking": [
            "Listen to simple instructions and respond orally.",
            "Familiar objects and picture cards.",
            "Give simple instructions and invite the learner to respond.",
            "Observe listening and speaking skills."
        ],
        "Picture reading and storytelling": [
            "Describe pictures and respond to questions about a short story.",
            "Picture books and story cards.",
            "Read a short story or discuss a picture and ask simple questions.",
            "Check whether the learner recalls characters or events."
        ]
    },

    "Social Science": {
        "My family": [
            "Identify family members and describe their roles.",
            "Family pictures and drawing materials.",
            "Invite the learner to identify family members and discuss how they help one another.",
            "Listen for identification of family members and their roles."
        ],
        "My school and community": [
            "Identify important places and people in the community.",
            "Pictures of schools, clinics, shops and community workers.",
            "Discuss familiar places and match community workers to their roles.",
            "Ask the learner to identify a community worker and explain their role."
        ],
        "Transport and road safety": [
            "Identify forms of transport and practise basic road safety.",
            "Vehicle pictures and road-safety cards.",
            "Discuss vehicles and demonstrate safe road-crossing behaviour.",
            "Ask the learner to identify a safe road-crossing behaviour."
        ],
        "Weather and seasons": [
            "Identify weather conditions and suitable clothing.",
            "Weather pictures and clothing cards.",
            "Discuss the weather and match clothing to different conditions.",
            "Ask the learner to describe the weather and choose suitable clothing."
        ],
        "Culture and heritage": [
            "Recognise familiar cultural practices and local heritage.",
            "Relevant pictures, stories and cultural objects.",
            "Discuss a familiar tradition, celebration or cultural practice.",
            "Invite the learner to describe a familiar cultural practice."
        ]
    },

    "Science and Technology": {
        "Living and non-living things": [
            "Distinguish between living and non-living things.",
            "Pictures of plants, animals and everyday objects.",
            "Ask the learner to sort pictures into living and non-living groups.",
            "Ask the learner to explain one classification."
        ],
        "Plants and their growth": [
            "Identify the basic needs of plants.",
            "Seeds, soil, water and a plant.",
            "Observe a plant and discuss what it needs to grow.",
            "Ask the learner to name basic plant needs."
        ],
        "Animals and their habitats": [
            "Identify familiar animals and describe where they live.",
            "Animal pictures and habitat cards.",
            "Match animals to suitable habitats and discuss their needs.",
            "Check whether the learner matches animals to appropriate habitats."
        ],
        "The human body and senses": [
            "Identify body parts and the five senses.",
            "Body pictures and safe objects to explore.",
            "Discuss how the senses help us understand our surroundings.",
            "Ask the learner to identify a sense and its function."
        ],
        "Materials and everyday technology": [
            "Explore familiar materials and describe the uses of everyday tools.",
            "Safe objects made from wood, plastic, metal or fabric.",
            "Let the learner compare materials and discuss the uses of familiar tools.",
            "Ask the learner to describe a material or explain a tool's use."
        ]
    },

    "Physical Education and Arts": {
        "Movement and balance": [
            "Develop balance and coordination through movement.",
            "Open space and floor markers.",
            "Invite the learner to walk along a line, jump or balance safely.",
            "Observe balance, coordination and safe participation."
        ],
        "Ball skills and games": [
            "Practise rolling, throwing, kicking or catching a soft ball.",
            "Soft balls and a safe playing area.",
            "Demonstrate a simple ball activity and allow the learner to practise.",
            "Observe coordination and participation."
        ],
        "Drawing and colouring": [
            "Express ideas through drawing and colouring.",
            "Paper, crayons and pencils.",
            "Invite the learner to draw and colour a familiar object or experience.",
            "Observe creative choices and expression of ideas."
        ],
        "Painting and printing": [
            "Explore colours, textures and patterns through painting or printing.",
            "Child-safe paint, paper and brushes.",
            "Demonstrate a simple painting or printing technique and allow exploration.",
            "Observe participation and creative use of materials."
        ],
        "Music, singing and dance": [
            "Respond to rhythm through singing, clapping and movement.",
            "Familiar songs and simple musical instruments.",
            "Sing a familiar song, clap a rhythm and invite the learner to move.",
            "Observe participation and response to rhythm."
        ],
        "Modelling and construction": [
            "Create a simple object using safe art or construction materials.",
            "Play dough, paper or large construction blocks.",
            "Invite the learner to make a simple model or construct an object.",
            "Observe creativity, coordination and safe use of materials."
        ]
    }
}

# LEARNER INFORMATION
st.header("1. Learner Information")

col1, col2 = st.columns(2)

with col1:
    age = st.selectbox("Learner's age", [3, 4, 5, 6, 7, 8])

with col2:
    level = st.selectbox(
        "Ability level",
        ["Beginner", "Intermediate", "Advanced"]
    )

area = st.selectbox(
    "Learning area",
    list(LEARNING_AREAS.keys())
)

# Topics change according to the selected learning area
topic = st.selectbox(
    "Topic",
    list(LEARNING_AREAS[area].keys())
)

interest = st.text_input(
    "Learner's interests",
    placeholder="e.g. animals, songs, toys or stories"
)

extra_support = st.checkbox(
    "Learner needs additional support"
)

support_notes = ""
if extra_support:
    support_notes = st.text_area(
        "Describe the learner's individual needs",
        placeholder="e.g. needs demonstrations or shorter instructions"
    )

# GENERATE ACTIVITY
st.header("2. Generate Learning Activity")

if st.button("Generate Activity", type="primary",
             use_container_width=True):

    objective, materials, instructions, assessment = (
        LEARNING_AREAS[area][topic]
    )

    if level == "Beginner":
        instructions += (
            " Start with one simple step, demonstrate first "
            "and allow repeated practice."
        )
        difficulty = "Use fewer items and simple instructions."

    elif level == "Intermediate":
        instructions += (
            " Allow the learner to try the task with occasional guidance."
        )
        difficulty = "Use several examples and gradually reduce assistance."

    else:
        instructions += (
            " Encourage independence and ask the learner to explain "
            "or demonstrate what they have learned."
        )
        difficulty = "Offer an additional challenge suited to the learner."

    if age <= 4:
        difficulty += " Keep the activity short and use concrete materials."
    elif age <= 6:
        difficulty += " Include demonstrations and opportunities for practice."
    else:
        difficulty += " Encourage more independent participation."

    if interest.strip():
        instructions += (
            f" Where appropriate, connect the activity to "
            f"the learner's interest in {interest.strip()}."
        )

    if extra_support:
        personalised_support = (
            "Demonstrate each step, give one instruction at a time, "
            "allow extra practice and offer encouragement."
        )
        if support_notes.strip():
            personalised_support += (
                " Specific support needs: " + support_notes.strip()
            )
    else:
        personalised_support = (
            "Observe the learner's progress and provide help when needed."
        )

    st.session_state["generated"] = True
    st.session_state["objective"] = objective
    st.session_state["materials"] = materials
    st.session_state["instructions"] = instructions
    st.session_state["difficulty"] = difficulty
    st.session_state["personalised_support"] = personalised_support
    st.session_state["assessment"] = assessment
    st.session_state["extension"] = (
        "Invite the learner to practise the skill again "
        "or use it in a new, familiar situation."
    )

# EDITABLE FIELDS
if st.session_state.get("generated", False):

    st.header("3. Edit and Personalise the Activity")
    st.write(
        "Change any field below to meet the learner's individual needs."
    )

    objective = st.text_area(
        "Learning objective",
        value=st.session_state["objective"],
        key="objective_edit"
    )

    materials = st.text_area(
        "Learning materials",
        value=st.session_state["materials"],
        key="materials_edit"
    )

    instructions = st.text_area(
        "Activity instructions",
        value=st.session_state["instructions"],
        key="instructions_edit",
        height=150
    )

    difficulty = st.text_area(
        "Difficulty adjustment",
        value=st.session_state["difficulty"],
        key="difficulty_edit"
    )

    personalised_support = st.text_area(
        "Individual learner support",
        value=st.session_state["personalised_support"],
        key="support_edit"
    )

    assessment = st.text_area(
        "Assessment",
        value=st.session_state["assessment"],
        key="assessment_edit"
    )

    extension = st.text_area(
        "Extension activity",
        value=st.session_state["extension"],
        key="extension_edit"
    )

    lesson_plan = f"""
ECD INDIVIDUALISED LEARNING ACTIVITY

Learning area: {area}
Topic: {topic}
Learner age: {age}
Ability level: {level}
Interests: {interest or "Not specified"}

LEARNING OBJECTIVE
{objective}

LEARNING MATERIALS
{materials}

ACTIVITY INSTRUCTIONS
{instructions}

DIFFICULTY ADJUSTMENT
{difficulty}

INDIVIDUAL LEARNER SUPPORT
{personalised_support}

ASSESSMENT
{assessment}

EXTENSION ACTIVITY
{extension}
"""

    st.header("4. Final Lesson Plan")
    st.text_area(
        "Review your personalised lesson plan",
        value=lesson_plan,
        height=400
    )

    st.download_button(
        "Download Lesson Plan",
        data=lesson_plan,
        file_name="ecd_personalised_lesson_plan.txt",
        mime="text/plain",
        use_container_width=True
    )

st.divider()
st.caption(
    "ECD Learning Generator | Teachers should review activities "
    "and adapt them to each learner's developmental needs."
)
