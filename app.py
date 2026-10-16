Python

import streamlit as st

st.set_page_config(
    page_title="ECD Learn & Grow",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 ECD Learn & Grow")
st.write("An individualised learning activity generator for ECD learners.")

AREAS = {
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
        "Drawing and colouring", "Singing and dancing", "Modelling"
    ]
}

AGES = ["Under 6 years", "7–8 years"]
LEVELS = ["Needs support", "Developing", "Challenging"]
INTERESTS = ["Songs", "Games", "Stories", "Drawing", "Movement", "Animals"]
SUPPORTS = ["None", "Visual aids", "Repetition", "Hands-on activities"]


def generate_activity(area, topic, age, level, interest, support):
    young = age == "Under 6 years"

    if young:
        objective = (
            f"The learner will begin to understand {topic.lower()} "
            "through play, pictures and practical activities."
        )
        duration = "10–15 minutes"
        steps = [
            "Introduce the topic using familiar objects or pictures.",
            "Demonstrate the activity slowly.",
            "Invite the learner to participate through play.",
            "Praise the learner's effort and review what was learned."
        ]
    else:
        objective = (
            f"The learner will demonstrate understanding of "
            f"{topic.lower()} by completing a practical task."
        )
        duration = "20–30 minutes"
        steps = [
            "Introduce the topic and ask questions about prior knowledge.",
            "Explain and demonstrate the task.",
            "Ask the learner to complete an individual or group activity.",
            "Review the answers and encourage the learner to explain their work."
        ]

    materials = {
        "Counting": "Bottle tops, stones or counters",
        "Number recognition": "Number cards and counters",
        "Shapes": "Shape cards and classroom objects",
        "Phonics": "Letter cards and picture cards",
        "Letter recognition": "Alphabet cards and paper",
        "Vocabulary": "Pictures and familiar objects",
        "Picture reading": "Picture cards or a picture book",
        "Storytelling": "Story pictures or puppets",
        "Kwazisana": "Greeting pictures or role-play cards",
        "Mhuka dzepamba": "Pictures of domestic animals",
        "Machemero emhuka": "Animal pictures and sound cards",
        "Nhetembo": "A familiar poem and picture cards",
        "Kutaura nyaya": "Story pictures",
        "Weather": "Weather pictures",
        "Plants": "A plant, leaves and pictures",
        "Domestic animals": "Animal pictures",
        "Simple experiments": "Safe classroom materials",
        "Everyday tools": "Pictures of everyday tools",
        "Family": "Family pictures or drawings",
        "Community helpers": "Pictures of community workers",
        "Culture and heritage": "Cultural pictures and objects",
        "Transport": "Toy vehicles or transport pictures",
        "Child rights": "Pictures showing children's needs and rights",
        "Kicking": "A soft ball and open space",
        "Jumping and balancing": "A safe open space and floor markers",
        "Drawing and colouring": "Paper, crayons and pencils",
        "Singing and dancing": "A familiar song and safe open space",
        "Modelling": "Clay or safe modelling material"
    }.get(topic, "Pictures, paper and familiar classroom objects")

    if level == "Needs support":
        adaptation = "Provide one instruction at a time and demonstrate each step."
    elif level == "Developing":
        adaptation = "Give a demonstration, then allow the learner to try with occasional help."
    else:
        adaptation = "Add a challenge and encourage the learner to work independently."

    interest_ideas = {
        "Songs": "Include a simple song, rhythm or rhyme.",
        "Games": "Turn the task into a short learning game.",
        "Stories": "Introduce the task through a short story.",
        "Drawing": "Ask the learner to draw or illustrate the concept.",
        "Movement": "Include safe movement or actions.",
        "Animals": "Use animal examples, pictures or toys."
    }

    support_ideas = {
        "None": "Offer ordinary verbal instructions and encouragement.",
        "Visual aids": "Use clear pictures, cards, demonstrations or objects.",
        "Repetition": "Repeat instructions and give extra practice.",
        "Hands-on activities": "Let the learner handle safe objects and learn by doing."
    }

    return {
        "objective": objective,
        "materials": materials,
        "duration": duration,
        "steps": steps,
        "adaptation": adaptation,
        "interest": interest_ideas[interest],
        "support": support_ideas[support]
    }


mode = st.radio(
    "Choose a mode",
    ["Learner Mode 🧒", "Teacher Mode 👩‍🏫"],
    horizontal=True
)

with st.form("activity_form"):
    if mode == "Teacher Mode 👩‍🏫":
        learner_name = st.text_input("Learner name or classroom identifier")
    else:
        learner_name = ""

    age = st.selectbox("Learner age group", AGES)
    area = st.selectbox("Learning area", list(AREAS.keys()))
    topic = st.selectbox("Topic", AREAS[area])
    level = st.selectbox("Ability level", LEVELS)
    interest = st.selectbox("Learner's interest", INTERESTS)
    support = st.selectbox("Additional support", SUPPORTS)

    submitted = st.form_submit_button("Generate Activity")

if submitted:
    activity = generate_activity(
        area, topic, age, level, interest, support
    )

    st.session_state["current_activity"] = {
        "area": area,
        "topic": topic,
        "age": age,
        "learner_name": learner_name,
        "activity": activity
    }

if "current_activity" in st.session_state:
    current = st.session_state["current_activity"]
    activity = current["activity"]

    st.divider()
    st.subheader(f"📚 {current['area']}: {current['topic']}")
    if current["learner_name"]:
        st.write("Learner:", current["learner_name"])

    st.write("**Age group:**", current["age"])
    st.write("**Learning objective:**", activity["objective"])
    st.write("**Materials:**", activity["materials"])
    st.write("**Duration:**", activity["duration"])

    st.write("**Personalisation:**", activity["adaptation"])
    st.write("**Interest-based activity:**", activity["interest"])
    st.write("**Additional support:**", activity["support"])

    st.write("### Activity steps")
    for number, step in enumerate(activity["steps"], start=1):
        st.write(f"{number}. {step}")

    st.divider()
    st.subheader("📝 Assessment and feedback")

    performance = st.selectbox(
        "Learner's performance",
        ["Achieved", "Developing", "Needs support"],
        key="performance"
    )
    notes = st.text_area("Teacher observations (optional)")

    if st.button("Suggest Feedback"):
        if performance == "Achieved":
            feedback = "Well done! You have demonstrated understanding of the activity."
            next_steps = "Introduce a slightly more challenging activity."
        elif performance == "Developing":
            feedback = "Good effort! Keep practising to build confidence."
            next_steps = "Repeat the activity with examples and guided practice."
        else:
            feedback = "Thank you for trying. We will learn this step by step."
            next_steps = "Use simpler examples, visual aids and one-to-one support."

        st.write("**Suggested feedback:**", feedback)
        st.write("**Recommended next steps:**", next_steps)

    plan = (
        f"ECD Learn & Grow Activity Plan\n"
        f"Learning area: {current['area']}\n"
        f"Topic: {current['topic']}\n"
        f"Age group: {current['age']}\n"
        f"Objective: {activity['objective']}\n"
        f"Materials: {activity['materials']}\n"
        f"Duration: {activity['duration']}\n"
        f"Personalisation: {activity['adaptation']}\n"
        f"Interest: {activity['interest']}\n"
        f"Support: {activity['support']}\n\n"
        + "\n".join(
            f"{i}. {step}"
            for i, step in enumerate(activity["steps"], start=1)
        )
    )

    st.download_button(
        "Download Activity Plan",
        data=plan,
        file_name="ecd_activity_plan.txt",
        mime="text/plain"
    )

st.caption(
    "Note: Learner information and assessments are not saved to a database. "
    "The current activity is kept temporarily in the app session."
)
