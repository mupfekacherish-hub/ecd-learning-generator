
import streamlit as st

st.set_page_config(
    page_title="ECD Individualised Learning Generator",
    page_icon="📚",
    layout="centered"
)

ACTIVITIES = {
    "Mathematics": {
        "Counting": (
            "Count objects accurately.",
            "Bottle tops, sticks or stones.",
            "Let the child touch and count objects one by one.",
            "Can the child count the objects correctly?"
        ),
        "Shapes": (
            "Identify and name basic shapes.",
            "Shape cards, paper and blocks.",
            "Ask the child to find circles, squares and triangles.",
            "Can the child identify and name the shapes?"
        ),
        "Patterns": (
            "Recognise and continue a simple pattern.",
            "Coloured blocks or bottle tops.",
            "Make a red-blue-red-blue pattern and ask the child to continue it.",
            "Can the child continue the pattern?"
        ),
        "Sorting": (
            "Sort objects according to colour, shape or size.",
            "Buttons, blocks or bottle tops.",
            "Ask the child to group objects using one chosen feature.",
            "Can the child explain how the objects were sorted?"
        )
    },
    "Language and Literacy": {
        "Letter recognition": (
            "Recognise selected letters.",
            "Letter cards and picture cards.",
            "Show a letter and ask the child to find a matching letter.",
            "Can the child recognise the selected letters?"
        ),
        "Phonics": (
            "Recognise the sound of a selected letter.",
            "Picture cards and familiar objects.",
            "Say a sound and ask the child to identify an object beginning with it.",
            "Can the child match the sound to a suitable word?"
        ),
        "Storytelling": (
            "Listen to and retell a simple story.",
            "Picture book or story cards.",
            "Tell a short story and ask the child what happened first and next.",
            "Can the child recall key events?"
        ),
        "Vocabulary": (
            "Name familiar objects and describe them.",
            "Pictures or real objects.",
            "Show familiar objects and invite the child to name and describe them.",
            "Can the child name and describe the objects?"
        )
    },
    "Science": {
        "Weather": (
            "Observe and describe the weather.",
            "Weather pictures and observation space.",
            "Observe the sky together and describe whether it is sunny, cloudy or rainy.",
            "Can the child describe the weather?"
        ),
        "Plants": (
            "Identify basic plant parts.",
            "A plant, pictures or a drawing.",
            "Help the child identify the roots, stem, leaves and flower where present.",
            "Can the child identify the parts shown?"
        ),
        "Animals": (
            "Identify familiar animals and their needs.",
            "Animal pictures or toy animals.",
            "Ask the child to name animals and describe what they need to live.",
            "Can the child name animals and one basic need?"
        ),
        "Senses": (
            "Explore objects using the senses safely.",
            "Safe objects with different textures.",
            "Invite the child to describe how objects feel, look or sound.",
            "Can the child describe an observed feature?"
        )
    },
    "Environmental Studies": {
        "Cleanliness": (
            "Practise personal and environmental cleanliness.",
            "Soap, water and picture cards.",
            "Demonstrate handwashing and let the child practise safely.",
            "Can the child demonstrate important handwashing steps?"
        ),
        "Water": (
            "Identify uses of water.",
            "Pictures and a container of water.",
            "Discuss how people, plants and animals use water.",
            "Can the child name different uses of water?"
        ),
        "Community helpers": (
            "Identify community helpers and their roles.",
            "Pictures of teachers, nurses and farmers.",
            "Match each helper to a task they perform.",
            "Can the child match helpers to their roles?"
        )
    },
    "Art and Creativity": {
        "Colours": (
            "Identify and match colours.",
            "Crayons, coloured paper or blocks.",
            "Ask the child to find and match objects of the same colour.",
            "Can the child identify the selected colours?"
        ),
        "Drawing": (
            "Express an idea through drawing.",
            "Paper and crayons.",
            "Invite the child to draw a familiar object and describe the picture.",
            "Can the child explain something about the drawing?"
        ),
        "Collage": (
            "Create a picture using different materials.",
            "Paper scraps, glue and cardboard.",
            "Help the child arrange and attach materials to create a picture.",
            "Can the child make and describe a collage?"
        )
    },
    "Physical Development": {
        "Balancing": (
            "Develop balance and body control.",
            "A clear, safe space.",
            "Invite the child to walk along a line on the ground with supervision.",
            "Can the child maintain balance during the activity?"
        ),
        "Throwing and catching": (
            "Practise hand-eye coordination.",
            "A soft ball.",
            "Let the child practise rolling, throwing and catching a soft ball at a suitable distance.",
            "Can the child control the ball during practice?"
        ),
        "Fine motor skills": (
            "Develop finger control and coordination.",
            "Large blocks, paper or child-safe tools.",
            "Invite the child to stack blocks or tear and arrange paper.",
            "Can the child manipulate the materials safely?"
        )
    },
    "Social and Emotional Development": {
        "Sharing": (
            "Practise sharing and taking turns.",
            "Toys or building blocks.",
            "Organise a game where children take turns using the same materials.",
            "Can the child take turns with support?"
        ),
        "Feelings": (
            "Recognise and express basic feelings.",
            "Emotion picture cards.",
            "Show faces expressing happiness, sadness or anger and discuss them.",
            "Can the child identify or express a feeling?"
        ),
        "Cooperation": (
            "Work together towards a simple goal.",
            "Blocks or a group puzzle.",
            "Help children work together to build a structure or complete a puzzle.",
            "Can the child participate cooperatively?"
        )
    },
    "Music and Movement": {
        "Action songs": (
            "Follow instructions through song and movement.",
            "A familiar action song.",
            "Sing together and perform actions such as clapping or marching.",
            "Can the child follow the song's actions?"
        ),
        "Rhythm": (
            "Recognise and reproduce a simple rhythm.",
            "Hands or safe musical instruments.",
            "Clap a short rhythm and invite the child to repeat it.",
            "Can the child reproduce the rhythm?"
        ),
        "Musical sounds": (
            "Listen to and compare different sounds.",
            "Safe sound-making objects.",
            "Make different sounds and ask the child to describe or compare them.",
            "Can the child notice differences between sounds?"
        )
    }
}


def generate_activity(
    area, topic, age, level, interest, extra_support
):
    objective, materials, instructions, assessment = (
        ACTIVITIES[area][topic]
    )

    if level == "Beginner":
        difficulty = (
            "Start with 2 or 3 examples. Demonstrate each step "
            "and give the child time to respond."
        )
        task = "Practise the skill using a few familiar examples."
    elif level == "Intermediate":
        difficulty = (
            "Use several examples and ask the child to explain "
            "or demonstrate the skill."
        )
        task = "Complete the task with less adult guidance."
    else:
        difficulty = (
            "Introduce a more challenging example and encourage "
            "reasoning, explanation or independent work."
        )
        task = "Apply the skill to a new example or solve a problem."

    support = (
        "Provide pictures, demonstrations, repetition, shorter "
        "instructions and individual guidance."
        if extra_support
        else "Encourage independence and offer help when needed."
    )

    return {
        "Objective": objective,
        "Materials": materials,
        "Instructions": instructions,
        "Difficulty adjustment": difficulty,
        "Learner challenge": task,
        "Personalisation": (
            f"For a learner aged {age}, use their interest in "
            f"{interest.lower()} to make the activity engaging."
        ),
        "Additional support": support,
        "Assessment": assessment,
        "Extension": (
            "If the child is ready, increase the challenge or "
            "invite the child to demonstrate the skill in a new way."
        )
    }


st.title("📚 ECD Individualised Learning Generator")
st.write(
    "Prepare learning activities for young children across "
    "different learning areas, ages and ability levels."
)

with st.form("activity_form"):
    area = st.selectbox(
        "Learning area",
        list(ACTIVITIES.keys())
    )

    topic = st.selectbox(
        "Topic",
        list(ACTIVITIES[area].keys())
    )

    age = st.selectbox(
        "Learner's age",
        [3, 4, 5, 6, 7, 8]
    )

    level = st.selectbox(
        "Difficulty level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    interest = st.selectbox(
        "Learner's interest",
        ["Animals", "Songs", "Stories", "Drawing",
         "Games", "Building blocks", "Outdoor play"]
    )

    extra_support = st.checkbox(
        "Learner needs extra support",
        value=False
    )

    submitted = st.form_submit_button("Generate Activity")

if submitted:
    result = generate_activity(
        area, topic, age, level, interest, extra_support
    )

    st.success("Your learning activity is ready!")
    st.subheader(f"{topic} — {area}")

    for heading, content in result.items():
        st.markdown(f"**{heading}:** {content}")

