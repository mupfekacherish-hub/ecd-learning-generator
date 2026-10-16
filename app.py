import random
import streamlit as st

st.set_page_config(
    page_title="ECD Learn & Grow",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 ECD Learn & Grow")
st.subheader("Individualised Learning Activity Generator")
st.write(
    "Generate learning activities suited to each learner's "
    "age, ability, interests and support needs."
)

TOPICS = {
    "Mathematics": [
        "Counting", "Number recognition", "Shapes",
        "Sizes and patterns", "Sorting and matching"
    ],
    "English": [
        "Phonics", "Letter recognition", "Vocabulary",
        "Picture reading", "Storytelling"
    ],
    "Shona": [
        "Kwazisana", "Mhuka dzepamba", "Machemero emhuka",
        "Nhetembo", "Kutaura nyaya"
    ],
    "Science and Technology": [
        "Weather", "Plants", "Domestic animals",
        "Simple experiments", "Everyday tools"
    ],
    "Social Science": [
        "Family", "Community helpers", "Culture and heritage",
        "Transport", "Child rights"
    ],
    "Physical Education and Arts": [
        "Kicking", "Jumping and balancing",
        "Drawing and colouring", "Singing and dancing",
        "Modelling"
    ]
}

with st.form("activity_form"):
    age_group = st.selectbox(
        "Learner's age group",
        ["Under 6 years", "7–8 years"]
    )

    area = st.selectbox(
        "Learning area",
        list(TOPICS.keys())
    )

    topic = st.selectbox(
        "Topic",
        TOPICS[area]
    )

    level = st.selectbox(
        "Ability level",
        ["Needs support", "Developing", "Challenging"]
    )

    interest = st.selectbox(
        "Learner's interest",
        ["Songs", "Games", "Stories", "Drawing", "Movement"]
    )

    support = st.selectbox(
        "Additional support",
        ["None", "Visual aids", "Repetition"]
    )

    submitted = st.form_submit_button("Generate Activity")

if submitted:
    young = age_group == "Under 6 years"

    if young:
        objective = (
            f"The learner will begin to understand {topic.lower()} "
            "through play and hands-on experience."
        )
        duration = "10–15 minutes"
        materials = "Pictures, safe everyday objects and locally available materials"
    else:
        objective = (
            f"The learner will demonstrate understanding of "
            f"{topic.lower()} through guided practice."
        )
        duration = "20–30 minutes"
        materials = "Topic-related cards, paper, pencils and learning objects"

    if level == "Needs support":
        instructions = (
            "Demonstrate each step, give one instruction at a time, "
            "and help the learner practise with guidance."
        )
    elif level == "Developing":
        instructions = (
            "Demonstrate the task once, then let the learner try "
            "with prompts and feedback."
        )
    else:
        instructions = (
            "Encourage the learner to complete the task independently "
            "and explain or demonstrate what they have learned."
        )

    interest_ideas = {
        "Songs": "Include a simple song, rhythm or chant related to the topic.",
        "Games": "Turn the task into a playful challenge with clear rules.",
        "Stories": "Introduce the activity through a short, relevant story.",
        "Drawing": "Invite the learner to draw or illustrate the topic.",
        "Movement": "Include safe actions, gestures or movement."
    }

    support_ideas = {
        "None": "Offer encouragement and check understanding during the activity.",
        "Visual aids": "Use clear pictures, demonstrations or real objects.",
        "Repetition": "Repeat key instructions and allow extra practice."
    }

    if area == "Mathematics":
        task = f"Use objects to practise {topic.lower()}."
    elif area == "English":
        task = f"Use words, sounds or pictures to practise {topic.lower()}."
    elif area == "Shona":
        task = f"Use familiar Shona words, oral practice or pictures for {topic.lower()}."
    elif area == "Science and Technology":
        task = f"Explore {topic.lower()} using observation and safe, practical materials."
    elif area == "Social Science":
        task = f"Discuss or role-play a familiar situation connected to {topic.lower()}."
    else:
        task = f"Practise {topic.lower()} through a safe, practical activity."

    if young:
        steps = [
            "Introduce the topic using a picture, object, song or demonstration.",
            f"Guide the learner to {task.lower()}",
            "Allow the learner to practise through play, with help when needed.",
            "Praise the learner's effort and ask a simple question about the activity."
        ]
    else:
        steps = [
            "Introduce the learning objective and discuss what the learner already knows.",
            f"Demonstrate how to {task.lower()}",
            "Ask the learner to complete the task and explain their choices.",
            "Review the work together and give constructive feedback."
        ]

    st.success("Your learning activity is ready!")

    st.markdown("### Activity details")
    st.write("**Learning area:**", area)
    st.write("**Topic:**", topic)
    st.write("**Age group:**", age_group)
    st.write("**Ability level:**", level)
    st.write("**Objective:**", objective)
    st.write("**Estimated duration:**", duration)
    st.write("**Materials:**", materials)

    st.markdown("### Activity")
    st.write(task)

    st.markdown("### Steps")
    for number, step in enumerate(steps, start=1):
        st.write(f"{number}. {step}")

    st.markdown("### Individualisation")
    st.write("**Learner's interest:**", interest)
    st.write(interest_ideas[interest])
    st.write("**Teaching approach:**", instructions)
    st.write("**Additional support:**", support)
    st.write(support_ideas[support])

    st.markdown("### Assessment")
    st.write(
        "Observe participation, understanding and ability to complete "
        "the task. Record progress separately if required."
    )

    st.info(
        "This version generates activities without storing learner "
        "profiles or saving learner details to a database."
    )
